#!/usr/bin/env python3
"""Mechanical lint for the wiki — SCHEMA.md §5.1 rules 1–10 plus the mechanical
half of rule 18 (trifecta scoping) and the `Status: Unresolved` commit gate.

Severities:
  error    — schema/consistency violation; fix before commit
  warn     — suspicious; human judgment needed
  research — page is fine but a claim needs (re)verification → wiki-research queue

Usage:
  python3 scripts/wiki_lint.py                 # lint, print summary
  python3 scripts/wiki_lint.py --report        # also write reports/lint-YYYY-MM-DD.md
  python3 scripts/wiki_lint.py --online        # add rule 6 (URL liveness) — slow
  python3 scripts/wiki_lint.py --write-index   # regenerate index.md from pages

Exit code 1 if any errors (not warns/research)."""

import csv
import datetime
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, cat_index, iter_pages, load_taxonomy, parse_page

TODAY = datetime.date.today()
CSV_PATH = ROOT / "survey-v2.csv"
ISO = re.compile(r"^20\d{2}-\d{2}-\d{2}$")
MD_LINK = re.compile(r"\]\(([^)#\s]+\.md)\)")

VENDOR_REQUIRED = ["title", "type", "name", "slug", "primary_category",
                   "ownership_state", "deployment_model", "last_verified"]
CATEGORY_REQUIRED = ["title", "type", "name", "slug", "category", "layer",
                     "adoption_tier", "trigger", "last_verified"]

issues = []  # (severity, rule, relpath, message)


def add(sev, rule, path, msg):
    rel = str(Path(path).relative_to(ROOT)) if str(path).startswith(str(ROOT)) else str(path)
    issues.append((sev, rule, rel, msg))


def as_date(v):
    if isinstance(v, datetime.date):
        return v
    if isinstance(v, str) and ISO.match(v):
        return datetime.date.fromisoformat(v)
    return None


def load_all():
    pages = {}
    for sub in ("vendors", "categories", "comparisons"):
        for p in iter_pages(sub):
            fm, body = parse_page(p)
            pages[p] = (fm, body)
    ov = ROOT / "wiki" / "overview.md"
    if ov.exists():
        fm, body = parse_page(ov)
        pages[ov] = (fm, body)
    return pages


def load_csv_rows():
    with open(CSV_PATH) as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        url = r.get("Wiki URL") or ""
        m = re.search(r"/(?:blob|tree)/[^/]+/(.+)$", urllib.parse.urlparse(url).path)
        r["_wiki_path"] = m.group(1) if m else None
        r["_is_other"] = (r.get("Product (answer option)") or "").strip().lower().startswith("other (")
    return rows


# ---------------------------------------------------------------- rules

def rule1_bijection(pages, rows):
    vendor_files = {str(p.relative_to(ROOT)) for p in pages if p.parent.name == "vendors"}
    referenced = set()
    for r in rows:
        if r["_is_other"]:
            continue
        prod = r.get("Product (answer option)", "")
        wp = r["_wiki_path"]
        if not wp:
            add("error", 1, CSV_PATH, f"CSV row {prod!r} has no parsable Wiki URL")
            continue
        referenced.add(wp)
        if wp not in vendor_files and not (ROOT / wp).exists():
            add("error", 1, CSV_PATH, f"CSV row {prod!r} points at missing page {wp}")
    for vf in sorted(vendor_files - referenced):
        add("warn", 1, ROOT / vf, "vendor page not referenced by any survey-v2.csv row (orphan)")


def rule2_duplicates(pages):
    seen = {}
    for p, (fm, _) in pages.items():
        if not fm or fm.get("type") != "vendor":
            continue
        key = re.sub(r"[^a-z0-9]", "", str(fm.get("name", "")).lower())
        if key in seen:
            add("error", 2, p, f"near-duplicate vendor name with {seen[key].name}")
        else:
            seen[key] = p


def rule3_schema(pages, tax):
    vocab = tax["vocab"]
    cats = cat_index(tax)
    for p, (fm, _) in pages.items():
        if fm is None:
            add("error", 3, p, "no YAML frontmatter")
            continue
        if not fm.get("title"):
            add("error", 3, p, "missing title (Quartz requires it)")
        t = fm.get("type")
        if t not in vocab["type"]:
            add("error", 3, p, f"type {t!r} not in vocab")
            continue
        if t == "vendor":
            for k in VENDOR_REQUIRED:
                if fm.get(k) in (None, "", []):
                    add("error", 3, p, f"missing required field {k}")
            for slug in [fm.get("primary_category")] + (fm.get("also_listed_in") or []):
                if slug and slug not in cats:
                    add("error", 3, p, f"category slug {slug!r} not in taxonomy.yaml")
            os_ = fm.get("ownership_state")
            if os_ and os_ not in vocab["ownership_state"]:
                add("error", 3, p, f"ownership_state {os_!r} not in vocab")
            for field, vname in (("deployment_model", "deployment_model"),
                                 ("form_factor", "form_factor")):
                for v in fm.get(field) or []:
                    if v not in vocab[vname]:
                        add("error", 3, p, f"{field} value {v!r} not in vocab")
            for field in ("mcp_support", "fs_traction"):
                v = fm.get(field)
                if v is not None and str(v) not in vocab[field]:
                    add("error", 3, p, f"{field} value {v!r} not in vocab")
            v = fm.get("data_leaves_tenancy")
            if v is not None and str(v).lower() not in [s.lower() for s in vocab["data_leaves_tenancy"]]:
                add("error", 3, p, f"data_leaves_tenancy value {v!r} not in vocab")
            mp = fm.get("market_position")
            if isinstance(mp, dict):
                for cslug, label in mp.items():
                    if cslug not in cats:
                        add("error", 3, p, f"market_position key {cslug!r} not a category")
                    if label not in vocab["market_position"]:
                        add("error", 3, p, f"market_position label {label!r} not in vocab")
            elif mp is not None:
                add("error", 3, p, "market_position must be null or {category-slug: label}")
            for field in ("last_verified", "verify_after"):
                v = fm.get(field)
                if v is not None and as_date(v) is None:
                    add("error", 3, p, f"{field} is not an ISO date: {v!r}")
        elif t == "category":
            for k in CATEGORY_REQUIRED:
                if fm.get(k) in (None, ""):
                    add("error", 3, p, f"missing required field {k}")
            slug = fm.get("category")
            if slug not in cats:
                add("error", 3, p, f"category slug {slug!r} not in taxonomy.yaml")
            else:
                tc = cats[slug]
                for field in ("layer", "adoption_tier", "survey_question"):
                    if fm.get(field) != tc[field]:
                        add("error", 3, p, f"{field} {fm.get(field)!r} disagrees with taxonomy.yaml {tc[field]!r}")
            cm = fm.get("category_maturity")
            if cm is not None and cm not in vocab["category_maturity"]:
                add("error", 3, p, f"category_maturity {cm!r} not in vocab")


def rule4_ma_state(pages):
    for p, (fm, body) in pages.items():
        if not fm or fm.get("type") != "vendor":
            continue
        state = fm.get("ownership_state")
        acq = fm.get("acquisition") or {}
        has_sources = bool(fm.get("sources")) or bool(re.search(r"^## Sources\s*\n+\s*- ", body, re.M))
        if state == "acquired-pending":
            va = as_date(fm.get("verify_after"))
            if va is None:
                add("error", 4, p, "acquired-pending requires verify_after date")
            elif va < TODAY:
                add("research", 4, p, f"verify_after {va} has passed — re-check whether the deal closed")
            if not acq.get("announced"):
                add("research", 4, p, "acquired-pending with no announced date")
        elif state == "acquired-closed":
            if not acq.get("closed"):
                add("research", 4, p, "acquired-closed with unconfirmed close date")
            if not has_sources:
                add("research", 4, p, "acquired-closed with no source entries")
        if state in ("acquired-pending", "acquired-closed") and not fm.get("owner"):
            add("error", 4, p, f"{state} but owner is empty")


def rule5_naming(pages, rows):
    by_path = {}
    for r in rows:
        if r["_wiki_path"]:
            by_path.setdefault(r["_wiki_path"], []).append(r)
    for p, (fm, _) in pages.items():
        if not fm or fm.get("type") != "vendor":
            continue
        if fm.get("ownership_state") not in ("acquired-closed", "acquired-pending"):
            continue
        rel = str(p.relative_to(ROOT))
        rs = by_path.get(rel, [])
        if rs and all("(" not in r["Product (answer option)"] for r in rs):
            add("warn", 5, p, f'acquired vendor: CSV option {rs[0]["Product (answer option)"]!r} '
                              f'lacks "X ({fm.get("owner") or "Acquirer"})" rendering')


def rule6_urls(pages):
    for p, (fm, _) in pages.items():
        if not fm or fm.get("type") != "vendor" or not fm.get("website"):
            continue
        url = str(fm["website"])
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (wiki-lint)"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                final = resp.geturl()
            orig = urllib.parse.urlparse(url).netloc.removeprefix("www.")
            dest = urllib.parse.urlparse(final).netloc.removeprefix("www.")
            if orig.split(".")[-2:] != dest.split(".")[-2:]:
                add("warn", 6, p, f"website redirects off-domain: {url} → {final} (acquisition-integration signal?)")
        except Exception as e:
            add("warn", 6, p, f"website unreachable: {url} ({e})")


def rule7_staleness(pages, tax):
    cats = cat_index(tax)
    for p, (fm, _) in pages.items():
        if not fm or fm.get("type") not in ("vendor", "category"):
            continue
        lv = as_date(fm.get("last_verified"))
        if lv is None:
            continue  # rule 3 already flags missing
        if fm.get("type") == "vendor":
            cat = cats.get(fm.get("primary_category")) or {}
            hot = (fm.get("ownership_state") in ("acquired-pending", "independent")
                   and cat.get("category_maturity") == "consolidating")
            limit = 60 if hot else 120
        else:
            limit = 120
        age = (TODAY - lv).days
        if age > limit:
            add("research", 7, p, f"last_verified {lv} is {age}d old (limit {limit}d)")


def rule8_dated_claims(pages):
    dated = re.compile(r"\$\s?\d|\b20\d{2}-\d{2}\b")
    for p, (fm, body) in pages.items():
        if not fm or fm.get("type") != "vendor":
            continue
        prose = re.split(r"^## Sources", body, flags=re.M)[0]
        if dated.search(prose):
            has_sources = bool(fm.get("sources")) or bool(re.search(r"^## Sources\s*\n+\s*- ", body, re.M))
            if not has_sources:
                add("error", 8, p, "body contains dated/dollar claims but page has no Sources entries")


def rule9_csv_notes(pages, rows):
    stop = {"renamed", "independent", "please", "specify", "acquired", "acquisition",
            "announced", "pending", "formerly", "from", "with", "their", "vendor"}
    fm_by_path = {str(p.relative_to(ROOT)): (fm, body) for p, (fm, body) in pages.items()}
    for r in rows:
        note = (r.get("Flag / Note") or "").strip()
        if not note or r["_is_other"] or not r["_wiki_path"]:
            continue
        page = fm_by_path.get(r["_wiki_path"])
        if not page:
            continue
        fm, body = page
        words = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9'&.-]{4,}", note)
                 if w.lower() not in stop]
        if not words:
            continue
        text = (str(fm) + body).lower()
        if not any(w.lower() in text for w in words):
            add("warn", 9, ROOT / r["_wiki_path"],
                f"CSV note {note!r} — no trace of it on the page")


def rule10_xrefs(pages):
    for p, (fm, body) in pages.items():
        for target in MD_LINK.findall(body):
            if target.startswith("http"):
                continue
            if not (p.parent / target).resolve().exists():
                add("error", 10, p, f"broken relative link: {target}")
        if not fm:
            continue
        for field in ("adjacent", "also_listed_in"):
            for slug in fm.get(field) or []:
                if not (ROOT / "wiki" / "categories" / f"{slug}.md").exists():
                    add("error", 10, p, f"{field} entry {slug!r} has no category page")
        for slug in fm.get("incumbent_coverage") or []:
            if not (ROOT / "wiki" / "vendors" / f"{slug}.md").exists():
                add("warn", 10, p, f"incumbent_coverage entry {slug!r} has no vendor page")


def rule18_trifecta(pages, tax):
    agent_cats = {c["slug"] for c in tax["categories"] if c.get("agent_security_context")}
    for p, (fm, body) in pages.items():
        if fm:
            for k in fm:
                if k.startswith("trifecta"):
                    add("error", 18, p, f"schema v2 forbids frontmatter key {k!r}")
        if "trifecta" not in body.lower():
            continue
        allowed = (
            p.name == "overview.md"
            or (fm and fm.get("type") == "category" and fm.get("category") in agent_cats)
            or (fm and fm.get("type") == "vendor" and fm.get("primary_category") in agent_cats)
            or (fm and fm.get("type") == "comparison")  # comparisons may quote the model in agent-security context
        )
        if not allowed:
            add("warn", 18, p, "lethal-trifecta framing outside agent-security context (SCHEMA.md §0) — rewrite in plain risk language")


def commit_gate(pages):
    for p, (_, body) in pages.items():
        if "Status: Unresolved" in body:
            add("error", 0, p, "unresolved contradiction (Status: Unresolved) — commit gate")


# ---------------------------------------------------------------- index

def one_liner(_fm, body):
    m = re.search(r"\*\*One-liner\*\*\s*[—–-]+\s*(.+)", body)
    if m:
        line = m.group(1).strip()
    else:
        paras = [l.strip() for l in body.splitlines()
                 if l.strip() and not l.startswith(("#", ">", "|", "-", "!"))]
        line = paras[0] if paras else ""
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)  # strip links
    return (line[:157] + "…") if len(line) > 160 else line


def write_index(pages, tax):
    lines = ["---", 'title: "Index"', "---", "",
             "# Index — content catalog", "",
             f"Regenerated {TODAY} by `scripts/wiki_lint.py --write-index`. "
             "One page per line: link — one-line summary — (key facts).", ""]
    ov = ROOT / "wiki" / "overview.md"
    if ov in pages:
        lines += ["## Overview", "",
                  f"- [overview](wiki/overview.md) — {one_liner(*pages[ov])}", ""]
    def section(title, sub, fmt):
        items = [(p, fm, body) for p, (fm, body) in sorted(pages.items())
                 if fm and p.parent.name == sub]
        lines.append(f"## {title} ({len(items)})")
        lines.append("")
        for p, fm, body in items:
            lines.append(fmt(p, fm, body))
        lines.append("")
    section("Categories", "categories", lambda p, fm, body:
            f"- [{fm['name']}](wiki/categories/{p.name}) — {one_liner(fm, body)} — "
            f"({fm.get('adoption_tier')}, {fm.get('last_verified')})")
    section("Vendors", "vendors", lambda p, fm, body:
            f"- [{fm['name']}](wiki/vendors/{p.name}) — {one_liner(fm, body)} — "
            f"({fm.get('ownership_state')}, {fm.get('last_verified')})")
    section("Comparisons", "comparisons", lambda p, fm, body:
            f"- [{fm.get('name') or fm.get('title')}](wiki/comparisons/{p.name}) — {one_liner(fm, body)}")
    (ROOT / "index.md").write_text("\n".join(lines).rstrip() + "\n")
    print("index.md regenerated")


# ---------------------------------------------------------------- main

def main():
    args = set(sys.argv[1:])
    tax = load_taxonomy()
    pages = load_all()
    rows = load_csv_rows()

    rule1_bijection(pages, rows)
    rule2_duplicates(pages)
    rule3_schema(pages, tax)
    rule4_ma_state(pages)
    rule5_naming(pages, rows)
    if "--online" in args:
        rule6_urls(pages)
    rule7_staleness(pages, tax)
    rule8_dated_claims(pages)
    rule9_csv_notes(pages, rows)
    rule10_xrefs(pages)
    rule18_trifecta(pages, tax)
    commit_gate(pages)

    if "--write-index" in args:
        write_index(pages, tax)

    sev_order = {"error": 0, "warn": 1, "research": 2}
    issues.sort(key=lambda i: (sev_order[i[0]], i[1], i[2]))
    counts = {s: sum(1 for i in issues if i[0] == s) for s in sev_order}
    print(f"\nlint: {counts['error']} errors, {counts['warn']} warns, "
          f"{counts['research']} research-needed across {len(pages)} pages")
    for sev, rule, rel, msg in issues:
        print(f"{sev:8} R{rule:<2} {rel}: {msg}")

    if "--report" in args:
        rep = ROOT / "reports" / f"lint-{TODAY}.md"
        rep.parent.mkdir(exist_ok=True)
        out = [f"# Wiki lint report — {TODAY}", "",
               f"{counts['error']} errors · {counts['warn']} warns · {counts['research']} research-needed "
               f"· {len(pages)} pages linted (mechanical rules; editorial rules 11–18 run in the wiki-lint skill)", ""]
        for sev in ("error", "warn", "research"):
            group = [i for i in issues if i[0] == sev]
            if not group:
                continue
            out.append(f"## {sev} ({len(group)})")
            out.append("")
            out += [f"- **R{rule}** `{rel}` — {msg}" for _, rule, rel, msg in group]
            out.append("")
        rep.write_text("\n".join(out))
        print(f"\nreport: {rep}")

    sys.exit(1 if counts["error"] else 0)


if __name__ == "__main__":
    main()
