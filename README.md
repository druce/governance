# Enterprise AI Governance & Security Vendor Wiki

A research wiki mapping the **enterprise AI governance / security vendor landscape**, written
for a **hedge-fund / asset-manager CTO** trying to understand the space: what each category is
for, when you actually need it (Day-1 vs Day-2), which vendors fill each slot, who owns whom,
and how to tell neighbors apart. It also doubles as scaffolding for a CTO usage/evaluation
**survey**.

Built and maintained by an LLM agent following [Karpathy's LLM-wiki pattern](https://github.com/karpathy/llm-wiki),
adapted for a landscape **researched from the web** rather than a pre-existing corpus. Every
claim that can go stale is dated and anchored to a cached source.

> **As of 2026-06-28.** Ownership/funding/M&A move fast — verify time-sensitive claims against
> the cited primary sources before relying on them. Not investment advice.

---

## What's in here

| | Count | |
|---|---|---|
| **Categories** | 42 | one page per layer-cake slot, across 7 layers |
| **Vendors** | 222 | one page each, fully researched, multi-category tagged |
| **Comparisons** | 6 | filed-back answers to recurring questions |
| **Cached sources** | ~370 | dated primary sources under `raw/sources/`, cited per claim |

Vendor ownership at last pass: **130 independent · 41 public · 36 acquired · 15 subsidiary.**
All `acquired` pages are verified to medium/high confidence against primary sources.

## Start here

- **[wiki/overview.md](wiki/overview.md)** — the thesis: the layer cake, the red/yellow/green
  trust zones, and the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
- **[index.md](index.md)** — the content catalog (every page, grouped, with status).
- **[taxonomy.md](taxonomy.md)** — the canonical 42-category map (source of truth for slugs),
  with **[taxonomy-gaps.md](taxonomy-gaps.md)** recording the reconciliation decisions.

### Comparison pages (the "just tell me" answers)
- [What's actually Day-1 for a ~50-person hedge fund](wiki/comparisons/day-1-for-a-50-person-fund.md)
- [The AI-security M&A map (2023–2026)](wiki/comparisons/ai-security-m-and-a-map.md)
- [AI gateways, head to head](wiki/comparisons/ai-gateways-head-to-head.md)
- [Runtime AI firewalls, compared](wiki/comparisons/runtime-ai-firewalls.md)
- [Entitlement-aware RAG options](wiki/comparisons/entitlement-aware-rag-options.md)
- [Survey blueprint (42 categories → 16/28 questions)](wiki/comparisons/survey-blueprint.md)

## The headline finding

The landscape **consolidated hard in 2025–26.** Roughly a third of named vendors are now
acquired — **Palo Alto, Cisco, Zscaler, CrowdStrike, F5, Snowflake, and Apple are each running
multi-deal AI roll-ups** (e.g. CyberArk→Palo Alto, Wiz→Google, Splunk→Cisco, Symmetry/SplxAI→Zscaler,
TruEra+Natoma→Snowflake). For a buyer this means much of the AI-firewall/guardrail field now
arrives as a *module* inside a platform you may already own. See the
[M&A map](wiki/comparisons/ai-security-m-and-a-map.md).

## Repository layout

```
├── Claude.md                 # the contract: schema, conventions, page formats, workflow
├── index.md                  # content catalog (read first when answering a query)
├── log.md                    # append-only op log (how the build progressed / resumes)
├── taxonomy.md               # canonical category list + layer mapping
├── taxonomy-gaps.md          # reconciliation decisions + open questions
├── raw/
│   ├── seeds/                # the two immutable inputs (layer-cake blog + survey CSV)
│   └── sources/              # ~370 dated, cached web sources (evidence for claims)
└── wiki/
    ├── overview.md           # the thesis
    ├── categories/           # 42 category pages (+ survey scaffolding)
    ├── vendors/              # 222 vendor pages
    └── comparisons/          # 6 cross-cutting comparison pages
```

Pages use Obsidian-style `[[wikilinks]]` (resolve by filename) and YAML frontmatter, so the
repo works in Obsidian, with Dataview, or as a static-site export.

## Proposed updates to the source material

Research surfaced enough drift that the two seed inputs are now dated. Proposed (non-destructive —
the seeds are immutable) refreshes:
- **[proposed-ai-stack-table-2026-06-28.md](proposed-ai-stack-table-2026-06-28.md)** — revised
  layer-cake table with M&A labels, 3 new rows, and category fixes.
- **[proposed-Governance-Security-Stack-seed-2026-06-28.csv](proposed-Governance-Security-Stack-seed-2026-06-28.csv)** —
  updated survey (28 questions; DSPM/DLP and MCP mega-questions split per the
  [survey blueprint](wiki/comparisons/survey-blueprint.md)).

## How it was built / how to reproduce

This wiki was generated end-to-end by an LLM agent (Claude). The reproduction inputs are all in
the repo:
- **[Claude.md](Claude.md)** — the schema/contract the agent follows (directory layout, page
  formats, sourcing rules, lint checklist, build discipline).
- **[raw/seeds/](raw/seeds)** — the two original inputs: the layer-cake blog post
  (`2026-06-19-AI-stack.md`) and the survey CSV.
- **[prompt1.md](prompt1.md) / [prompt2.md](prompt2.md)** — the kickoff prompts.
- **[conversation.txt](conversation.txt)** — the full build transcript (Phase 0 scaffold →
  taxonomy → category pages → 222 vendor research agents → comparisons → lint), useful as a
  worked example of the LLM-wiki pattern at scale.

The build ran in phases (scaffold → taxonomy → category pages → vendor stubs → parallel deep
research with source caching → comparisons → final taxonomy pass + lint), committing after each
step so the run is resumable from `log.md` + `index.md`.

## Caveats

- **Dated snapshot (2026-06-28).** Funding, ownership, and "latest release" claims go stale fast.
- **Verify M&A before relying on it.** Pending/announced deals are labeled as such; primary
  sources are cited per claim.
- **Neutral and comparative, not endorsements.** Vendor marketing is labeled as marketing.
- **Not investment, legal, or compliance advice.**
