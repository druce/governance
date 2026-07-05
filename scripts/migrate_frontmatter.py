#!/usr/bin/env python3
"""Migrate wiki page frontmatter from schema v1 (old CLAUDE.md §4) to schema v2
(SCHEMA.md §4).

One-shot and idempotent: vendor pages already carrying `primary_category` and
category pages already carrying `adoption_tier` are skipped, so re-running is
safe.

Everything that cannot be mapped mechanically (undated acquisitions, unknown
enum values, low-confidence ownership) is written to migration-report.md —
that list seeds the wiki-research queue.

Usage: python3 scripts/migrate_frontmatter.py [--dry-run]
"""

import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, cat_index, dump_page, iter_pages, load_taxonomy, parse_page

TODAY = datetime.date.today()

ISO_DATE = re.compile(r"\b(20\d{2}-\d{2}(?:-\d{2})?)\b")
MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_STOP = r"(?=\s*[(,;.—–]|\s+for\s|\s*$)"
_NAME = r"([A-Z][\w&.' -]{1,40}?)"
OWNER_PATTERNS = [
    re.compile(r"(?:acquired by|acq\.? by|taken private by|bought by|subsidiary of|owned by|unit of|now part of|merged into)\s+" + _NAME + _STOP, re.I),
    re.compile(r"product(?:\s+\w+)? of\s+" + _NAME + _STOP, re.I),
    re.compile(r"(?:^|[.;:]\s+)" + _NAME.replace(" -", "-") + r"\s+(?:announced intent to acquire|announced acquisition|acquired\b|acquires\b|to acquire\b|hired)", re.M),
    re.compile(_NAME + r"\s+majority shareholder", 0),
]
PE_HINT = re.compile(r"pe-owned|private equity|taken private|pe-backed", re.I)


def extract_owner(detail):
    d = MD_LINK.sub(r"\1", detail)
    for pat in OWNER_PATTERNS:
        m = pat.search(d)
        if m:
            owner = m.group(1).strip().rstrip(".")
            owner = re.sub(r"(?:\s+in)?\s+20\d{2}$", "", owner)  # "CyberArk 2017", "Apple in 2025"
            if owner.lower().startswith("the "):
                continue
            return owner
    return None

# old `deployment` values → (deployment_model, form_factor)
DEPLOY_MODEL = {"saas", "self-hosted", "on-prem", "hybrid", "in-tenant"}
FORM_FACTOR = {
    "api": "api",
    "sdk": "sdk",
    "inline-proxy": "inline-proxy",
    "browser-extension": "browser-extension",
    "endpoint-agent": "agent",
    "browser": "platform",
    "edge": "platform",
    "container": "platform",
}


def parse_date(s):
    """'2026-05-29' or '2025-12' → datetime.date (day defaults to 1)."""
    parts = [int(p) for p in s.split("-")]
    while len(parts) < 3:
        parts.append(1)
    return datetime.date(*parts)


def map_ownership(own, detail, confidence, flags):
    """Return (ownership_state, owner, acquisition, verify_after)."""
    owner = extract_owner(detail)
    acq: dict = {"announced": None, "closed": None, "price": None}
    verify_after = None
    dates = ISO_DATE.findall(detail)
    low = detail.lower()

    if own in ("independent", "public"):
        state = own
    elif own in ("acquired", "subsidiary") and PE_HINT.search(detail):
        state = "pe-owned"
        if dates:
            acq["announced"] = parse_date(dates[0])
        if not owner:
            flags.append("pe-owned: could not extract sponsor name from ownership_detail")
    elif own in ("acquired", "subsidiary"):
        pending = ("pending" in low or "announced" in low) and not any(
            w in low for w in ("closed", "completed", "complete")
        )
        if pending:
            state = "acquired-pending"
            if dates:
                acq["announced"] = parse_date(dates[0])
            verify_after = TODAY + datetime.timedelta(days=60)
            flags.append("acquired-pending: confirm whether the deal has closed")
        else:
            state = "acquired-closed"
            if dates:
                # v1 pages rarely distinguish announce vs close; record the date
                # as announced and leave close date for research to confirm.
                acq["announced"] = parse_date(dates[0])
                if any(w in low for w in ("closed", "completed")):
                    acq["closed"] = parse_date(dates[-1])
                else:
                    flags.append("acquired-closed: close date unconfirmed (v1 date recorded as announced)")
            else:
                flags.append("acquired/subsidiary with no date in v1 ownership_detail")
        if not owner:
            flags.append("could not extract acquirer name from ownership_detail")
    else:
        state = own or None
        flags.append(f"unmapped v1 ownership value: {own!r} (kept as-is; fails lint)")

    if confidence == "low":
        flags.append("v1 ownership_confidence was low — verify ownership")
    return state, owner, acq, verify_after


def split_deployment(dep, flags):
    model, form = [], []
    for d in dep or []:
        if d in DEPLOY_MODEL:
            model.append(d)
        elif d in FORM_FACTOR:
            f = FORM_FACTOR[d]
            if f not in form:
                form.append(f)
            if FORM_FACTOR[d] != d:
                flags.append(f"deployment value {d!r} mapped to form_factor {f!r} — review")
        else:
            flags.append(f"unmapped v1 deployment value: {d!r} (dropped)")
    return model, form


def migrate_vendor(fm, flags, names=None):
    new = {k: fm.get(k) for k in ("title", "type", "name", "slug")}
    new["aka"] = fm.get("aliases") or []
    cats = fm.get("categories") or []
    if not cats:
        flags.append("no categories in v1 frontmatter")
    new["primary_category"] = cats[0] if cats else None
    new["also_listed_in"] = cats[1:]
    for k in ("website", "founded", "hq"):
        new[k] = fm.get(k)

    state, owner, acq, verify_after = map_ownership(
        (fm.get("ownership") or "").strip(),
        str(fm.get("ownership_detail") or ""),
        fm.get("ownership_confidence"),
        flags,
    )
    if owner and names:
        owner = names.get(owner.lower(), owner)  # '[f5](f5.md)' link text → page name
    new["ownership_state"] = state
    new["owner"] = owner
    detail = fm.get("ownership_detail")
    new["ownership_note"] = detail if detail else None
    new["acquisition"] = acq
    new["funding_total"] = fm.get("funding_total")
    new["last_funding"] = fm.get("last_funding")

    new["market_position"] = None  # editorial: set per category with justification
    model, form = split_deployment(fm.get("deployment"), flags)
    new["deployment_model"] = model
    new["form_factor"] = form
    new["data_leaves_tenancy"] = "unverified"
    new["integrations"] = []
    new["mcp_support"] = "unverified"
    new["certifications"] = []
    new["pricing_model"] = None
    new["fs_traction"] = "unverified"
    new["target_customer"] = fm.get("target_customer")
    new["last_verified"] = fm.get("last_updated")
    new["verify_after"] = verify_after
    new["tags"] = fm.get("tags") or []
    return new


def migrate_category(fm, tax_cat, flags):
    new = {k: fm.get(k) for k in ("title", "type", "name", "slug")}
    new["category"] = fm["slug"]
    if fm.get("layer") != tax_cat["layer"]:
        flags.append(f"layer mismatch: page {fm.get('layer')!r} vs taxonomy {tax_cat['layer']!r} (taxonomy wins)")
    new["layer"] = tax_cat["layer"]
    new["survey_question"] = tax_cat["survey_question"]
    new["adoption_tier"] = tax_cat["adoption_tier"]
    new["trigger"] = tax_cat["trigger"]
    new["maturity_stage_required"] = None
    new["category_maturity"] = tax_cat["category_maturity"]
    new["adjacent"] = tax_cat["adjacent"]
    new["incumbent_coverage"] = []
    new["vendor_count"] = fm.get("vendor_count")
    new["maps_to_seed_doc"] = fm.get("maps_to_seed_doc")
    new["maps_to_seed_csv"] = fm.get("maps_to_seed_csv")
    new["last_verified"] = fm.get("last_updated")
    return new


def main():
    dry = "--dry-run" in sys.argv
    tax = cat_index(load_taxonomy())
    report = {}  # path → flags
    migrated = skipped = 0

    names = {}  # vendor slug → display name, for resolving wikilinked owners
    for path in iter_pages("vendors"):
        fm, _ = parse_page(path)
        if fm and fm.get("slug") and fm.get("name"):
            names[str(fm["slug"]).lower()] = fm["name"]

    for path in iter_pages("vendors", "categories"):
        fm, body = parse_page(path)
        rel = str(path.relative_to(ROOT))
        if fm is None:
            report[rel] = ["NO FRONTMATTER — fix by hand"]
            continue
        flags = []
        if fm.get("type") == "vendor":
            if "primary_category" in fm:
                skipped += 1
                continue
            new = migrate_vendor(fm, flags, names)
        elif fm.get("type") == "category":
            if "adoption_tier" in fm:
                skipped += 1
                continue
            tc = tax.get(fm.get("slug"))
            if tc is None:
                report[rel] = [f"category slug {fm.get('slug')!r} not in taxonomy.yaml — fix by hand"]
                continue
            new = migrate_category(fm, tc, flags)
        else:
            report[rel] = [f"unexpected type {fm.get('type')!r} in vendors/categories dir"]
            continue
        if not dry:
            dump_page(path, new, body)
        migrated += 1
        if flags:
            report[rel] = flags

    lines = [
        "# Frontmatter migration report (schema v1 → v2)",
        "",
        f"Run: {TODAY}. Migrated {migrated} pages, skipped {skipped} already-migrated.",
        "Items below could not be mapped mechanically — they seed the wiki-research queue.",
        "",
    ]
    for rel in sorted(report):
        lines.append(f"## {rel}")
        lines += [f"- {f}" for f in report[rel]]
        lines.append("")
    out = ROOT / "migration-report.md"
    if not dry:
        out.write_text("\n".join(lines))
    print(f"migrated {migrated}, skipped {skipped}, {len(report)} pages flagged")
    print(f"report: {out}" if not dry else "(dry run — nothing written)")


if __name__ == "__main__":
    main()
