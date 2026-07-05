#!/usr/bin/env python3
"""Regenerate taxonomy.md (human-readable) from taxonomy.yaml (source of truth).

Never edit taxonomy.md by hand — edit taxonomy.yaml and re-run this.

Usage: python3 scripts/gen_taxonomy_md.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, load_taxonomy

LAYER_TITLES = {
    "foundation": "Foundation layer",
    "data": "Data layer",
    "model-prompt": "AI model & prompt layer",
    "retrieval": "Retrieval layer",
    "ux": "User experience layer",
    "governance": "Governance layer",
    "policy": "Policy / process layer",
}


def esc(v):
    return "—" if v in (None, "", []) else str(v).replace("|", "\\|")


def main():
    tax = load_taxonomy()
    cats = tax["categories"]
    lines = [
        "---",
        'title: "Taxonomy"',
        "---",
        "",
        "# Taxonomy — canonical category set",
        "",
        f"**GENERATED from `taxonomy.yaml` by `scripts/gen_taxonomy_md.py` — do not edit by hand.**",
        "",
        "`taxonomy.yaml` is the machine source of truth for category slugs, layers,",
        "adoption tiers, and controlled vocabularies (see `SCHEMA.md`). The layer-cake",
        "blog doc remains the spine (Foundation → Data → Model/Prompt → Retrieval → UX →",
        "Governance → Policy/Process); the survey categories map into it.",
        "",
        "Legend — **Tier**: `day-1` (before any AI in production) · `day-2` (once",
        "scaling/agents) · `situational` (depends on deployment pattern; see trigger) ·",
        "`firm-type-specific` · `practice` (a process, not a purchase). **Agent-sec** =",
        "`agent_security_context`: the lethal trifecta is a core concern for this",
        "category (SCHEMA.md §0); trifecta framing elsewhere fails editorial lint.",
        "",
        f"Counts: **{len(cats)} canonical categories** across {len(tax['layers'])} layers.",
        "",
        "---",
    ]
    for layer in tax["layers"]:
        group = [c for c in cats if c["layer"] == layer]
        if not group:
            continue
        lines += ["", f"## {LAYER_TITLES.get(layer, layer)}", "",
                  "| slug | display name | tier | agent-sec | trigger | survey question | notes |",
                  "|---|---|---|---|---|---|---|"]
        for c in group:
            lines.append(
                f"| `{c['slug']}` | {esc(c['display_name'])} | {esc(c['adoption_tier'])} "
                f"| {'✓' if c.get('agent_security_context') else '—'} | {esc(c['trigger'])} "
                f"| {esc(c['survey_question'])} | {esc(c.get('notes'))} |"
            )
    appendix = tax.get("appendix")
    if appendix:
        lines += ["", "---", "", appendix.rstrip()]
    (ROOT / "taxonomy.md").write_text("\n".join(lines) + "\n")
    print(f"taxonomy.md regenerated ({len(cats)} categories)")


if __name__ == "__main__":
    main()
