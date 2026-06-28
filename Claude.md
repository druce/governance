# CLAUDE.md — AI Governance & Security Vendor Wiki

This repo is a **research wiki** about the enterprise AI governance/security vendor
landscape, built and maintained by you (the LLM agent). It follows Karpathy's
LLM-wiki pattern, adapted for a landscape you **research from the web** rather than
a corpus that already exists on disk.

You write and maintain everything in `wiki/`, `index.md`, `log.md`, `taxonomy.md`,
and `taxonomy-gaps.md`. The human curates direction and asks questions. The two
seed files in `raw/seeds/` are immutable inputs, not gospel.

---

## 1. Purpose & audience

The reader is a **hedge-fund / asset-manager CTO trying to understand this space**:
what each category is for, when they actually need it (Day-1 vs Day-2), which
vendors fill each slot, who owns whom now, and how to tell neighbors apart.

A second consumer is **survey design**: the output will be used to fine-tune an
upcoming survey of what CTOs are currently *using* and *evaluating*. So category
pages must double as survey scaffolding (see §6), and the taxonomy must stay clean
enough to map onto survey questions.

Write for a smart, busy technical buyer. Plain English, no marketing voice, no
hype. Neutral and comparative. Name tradeoffs. Flag uncertainty instead of
papering over it.

---

## 2. Architecture (three layers)

- **`raw/`** — immutable inputs and cached research. You read from it, never edit
  the seeds.
  - `raw/seeds/` — the two original inputs (the layer-cake blog doc + the survey
    CSV). Never modify.
  - `raw/sources/` — research you fetch from the web, saved as dated markdown so
    claims stay anchored to retrievable evidence. Filename:
    `YYYY-MM-DD--<vendor-or-topic-slug>--<short-source-slug>.md`. Top of each file:
    the URL, the fetch date, and a one-line note on what it's good for.
- **`wiki/`** — the pages you generate and own (vendors, categories, comparisons,
  overview).
- **The schema** — this file. It defines structure, conventions, page formats, and
  the ingest/query/lint workflows. You and the human co-evolve it.

### Directory layout

```
/
├── CLAUDE.md            # this file
├── index.md            # content catalog (every page, one-line summary)
├── log.md              # chronological, append-only op log
├── taxonomy.md         # canonical category list + layer mapping (source of truth for slugs)
├── taxonomy-gaps.md    # mismatches, orphans, proposed renames/moves, open questions
├── raw/
│   ├── seeds/          # immutable original inputs
│   └── sources/        # dated cached web research
└── wiki/
    ├── overview.md     # the thesis / map of the whole space
    ├── categories/     # one page per category
    ├── vendors/        # one page per vendor
    └── comparisons/    # cross-cutting comparison pages (filed-back query answers)
```

---

## 3. Conventions

- **Markdown + Obsidian-style `[[wikilinks]]`.** Link by page filename without
  extension, e.g. `[[witnessai]]`, `[[ai-runtime-security]]`. Wikilinks resolve by
  filename regardless of folder, so nesting is fine.
- **Slugs are kebab-case.** Vendor slug = the company, not the product, e.g.
  `palo-alto-networks` with the product noted in the page (Prisma AIRS, Cortex,
  etc.). When a product is the unit people shop for, you may slug the product
  (`prisma-airs`) and cross-link to the parent company — record the choice in
  `log.md` and stay consistent.
- **One page per vendor, multiple category tags.** A vendor that appears in several
  categories (Prisma AIRS, CyberArk, OneTrust, HiddenLayer, Cyberhaven, Astrix…)
  gets **one** vendor page tagged with all relevant `categories`, and is listed on
  each relevant category page. Never create duplicate vendor pages.
- **Split bundled seed entries.** CSV rows like `1Password / Doppler / Infisical`,
  `OPA / Styra`, `Immuta / Collibra` are distinct companies → separate vendor
  pages. Note the split in `log.md`.
- **Skip survey artifacts.** `Other (Please Specify)` rows are survey UI, not
  vendors. Don't make pages for them, but preserve them in category survey
  scaffolding (§6).
- **YAML frontmatter on every page** so Dataview / graph view / a later static-site
  export all work.
- **Dates are ISO** (`YYYY-MM-DD`). Always date claims that can go stale (funding,
  ownership, "latest release").

---

## 4. Page schemas

### 4.1 Vendor page (`wiki/vendors/<slug>.md`)

```yaml
---
type: vendor
name: WitnessAI
slug: witnessai
categories: [ai-access-governance, ai-runtime-security]  # canonical slugs; first = primary
layer: model-prompt                 # layer of the primary category
aliases: []
website:
founded:
hq:
ownership: independent              # independent | public | acquired | subsidiary
ownership_detail:                   # e.g. "acq. by Palo Alto Networks (2025-12); see sources"
ownership_confidence: low           # high | medium | low — verify before raising
funding_total:
last_funding:                       # round + date if known
deployment: []                      # saas | self-hosted | inline-proxy | api | on-prem | sdk
target_customer:                    # enterprise / mid-market / regulated / SMB
hedge_fund_fit: unclear             # high | medium | low | unclear (+ explain in body)
priority: day-2                     # day-1 | day-2 | optional (inherited from category, adjust w/ note)
trifecta_relevance: []              # untrusted-input | sensitive-data | egress | none  (which leg(s) it addresses)
status: stub                        # stub | drafted | researched | verified
confidence: low                     # overall page confidence
sources_count: 0
last_updated:
tags: []
---
```

Body (omit a section only if genuinely N/A):

- **One-liner** — what it is, in a sentence a CTO would repeat.
- **What it does** — plain English; the job it does and why you'd want it.
- **Where it sits in the stack** — link the `[[category]]` page(s) and the layer;
  note its lethal-trifecta role (which leg it breaks: untrusted input / sensitive
  data / egress) and which trust zone(s) it's relevant to.
- **Deployment & architecture** — how it actually runs (inline proxy? API? agent?
  browser? SDK?) and key integrations (AI gateways, SIEM/SOC, IdP, MCP, DSPM).
- **Positioning & differentiators** — what it's known for; how it differs from its
  nearest neighbors (link them).
- **Ownership, funding & M&A** — verified and dated. If the seed flagged an
  acquisition, state whether you confirmed it, with source + date + confidence.
- **CTO / hedge-fund lens** — Day-1/Day-2, SR 11-7 / model-risk relevance if any,
  when you actually need this, what size/posture of shop it fits.
- **Competitors / alternatives** — `[[wikilinks]]`.
- **Open questions / to verify** — explicit unknowns.
- **Sources** — list: `- [title](url) — fetched YYYY-MM-DD — supports: <claim>;
  confidence: high/med/low`. Prefer primary sources (vendor docs, filings, the
  acquirer's release) over aggregators; mark marketing claims as such.
- **History** — append-only. On every re-touch add `- [YYYY-MM-DD] <what changed>`.
  Never silently overwrite a prior substantive claim; supersede it with a dated
  note.

### 4.2 Category page (`wiki/categories/<slug>.md`)

```yaml
---
type: category
name: AI Runtime Security (AI Firewall)
slug: ai-runtime-security
layer: model-prompt                 # foundation | data | model-prompt | retrieval | ux | governance | policy
priority: day-1
trifecta_role:                      # which leg(s) of the lethal trifecta this layer controls
maps_to_seed_doc:                   # the layer-cake row this came from
maps_to_seed_csv:                   # the CSV survey category this came from
vendor_count:
status: drafted
last_updated:
---
```

Body:

- **Business objective** — what this layer is for, in plain English + the "bouncer
  metaphor" register the seed doc uses where it helps.
- **When you need it** — Day-1/Day-2/optional and *why*, for a hedge-fund CTO.
- **Lethal-trifecta role** — which leg(s) it breaks; which trust zone(s) it lives in.
- **Vendors** — bulleted `[[wikilinks]]`, each with a one-line positioning so the
  page reads as a buyer's map, grouped into sub-segments if the category splits
  (e.g. inline-proxy vs API guardrails).
- **Consolidation / M&A dynamics** — who's been acquired, who's rolling up.
- **Adjacent categories** — `[[wikilinks]]` and how they overlap.
- **Survey scaffolding** — see §6.
- **Open taxonomy questions** — overlaps, naming doubts, candidates to split/merge.

### 4.3 Comparison page (`wiki/comparisons/<slug>.md`)

`type: comparison`. A filed-back answer to a recurring question — a table or matrix
plus prose. Examples to build: AI gateways head-to-head; runtime AI firewalls;
the AI-security M&A map; "what's actually Day-1 for a 50-person fund"; entitlement-
aware RAG options. Cite sources; link the vendor/category pages.

### 4.4 Overview (`wiki/overview.md`)

The thesis. The layer cake, the three-zone (red/yellow/green) trust model and the
lethal trifecta, what a minimal vs full stack looks like for a hedge fund,
consolidation trends, and a linked map into every category.

### 4.5 index.md

Content catalog. Group by section (Overview, Categories, Vendors, Comparisons).
Each line: `[[slug]] — one-line summary — (status, last_updated)`. Update on every
ingest. Read it first when answering a query.

### 4.6 log.md

Append-only, chronological. Every entry starts with a greppable prefix:

```
## [YYYY-MM-DD] <op> | <subject>
```

where `<op>` ∈ `setup | taxonomy | stub | research | compare | lint | decision`.
`grep "^## \[" log.md | tail` gives recent activity. Record decisions (slug
choices, splits, renames, moves, contradictions resolved) here.

### 4.7 taxonomy.md

The **source of truth for category slugs**. Categories grouped by layer-cake layer.
For each: `slug`, display name, `priority`, the seed-doc row and seed-CSV category
it reconciles, primary vendors, and notes. When you rename/move a category after
research, edit here and log a `decision` entry.

---

## 5. Taxonomy (reconcile, then revise)

- The **layer-cake doc is the spine** (Foundation → Data → Model/Prompt →
  Retrieval → UX → Governance → Policy). The **CSV survey categories map into it.**
- Reconcile both into **one** category set in `taxonomy.md`. You are free to **add,
  rename, split, or merge** categories where the sources disagree or a better cut
  exists — record every such choice in `taxonomy-gaps.md` and `log.md`.
- After all research is done, do a **final taxonomy pass**: rename categories and
  move vendors based on what you learned, then fix affected links and frontmatter.
- A vendor can belong to several categories. Pick a sensible primary; tag the rest.

---

## 6. Survey scaffolding (on every category page)

Because the output fine-tunes a CTO usage/evaluation survey, end each category page
with a `## Survey` section:

- **Question** — the survey question for this category (use/evaluate framing).
- **Answer options** — the vendor list (the real shortlist), plus
  `Other (Please Specify)`.
- **Response scale** — reuse the seed scale: *multi-select; Interested;
  Considering/evaluating; Pilot/implementing; In production; Would recommend;
  Would not recommend.*
- **Notes for survey design** — which options are table-stakes vs niche, where
  overlap will confuse respondents, M&A that dates an option, and any "ask this
  instead" suggestions.

---

## 7. Research & sourcing rules

- Use web search + fetch. **Cache** what you rely on into `raw/sources/` (dated)
  and cite it. Anchor claims to sources; don't let synthesis drift away from
  evidence.
- **Verify the seed notes** — treat every CSV flag/note (especially M&A) as a hint,
  not a fact. Confirm acquisitions against the acquirer's or a primary source,
  with a date. If you can't confirm, say so and set `ownership_confidence: low`.
- Prefer primary sources; label vendor marketing as marketing; prefer independent
  corroboration for differentiation claims.
- **Never invent.** Unknown founding year, funding, or HQ stays blank with a note,
  not a guess. Distinguish "couldn't find" from "doesn't exist."
- Note the **as-of date** for anything volatile.

---

## 8. Contradictions & confidence

When new info conflicts with a page, classify severity and act:

- **soft / scope-mismatch** — non-blocking. Note it, keep both with context, date
  it. Useful for nuance.

- **hard** — a factual conflict (e.g. two different acquirers). Do **not** silently
  overwrite. Flag inline:

  ```
  > Contradiction (hard): <A> vs <B>. Status: Unresolved — flagged YYYY-MM-DD.
  ```

  and log a `decision` entry. Resolve with a source, or leave flagged for the human.

- Keep page `confidence` honest. Raising `ownership`/`funding` confidence requires a
  dated source.

---

## 9. Operations

**Ingest (research a vendor).** Pick the next unbuilt/lowest-confidence vendor →
search + fetch + cache → write/upgrade the vendor page → update its category
page(s) positioning → verify M&A → update `index.md` → append `log.md` → commit.

**Query.** Read `index.md`, drill into relevant pages, synthesize with citations.
**File good answers back** as a `comparisons/` page so explorations compound.

**Lint** (§10).

---

## 10. Lint checklist

Run periodically and at the end of the build. Cheap deterministic checks first
(shell), reasoning checks scoped to changed pages + their link neighbors:

- Orphans (no inbound `[[links]]`), broken/dangling links.
- Vendors missing a category, or categories with zero vendors.
- Stale pages (old `last_updated`), unverified M&A still at `low` confidence.
- Duplicate vendor pages / inconsistent slugs.
- Frontmatter conformance (every page has `type` + required fields).
- **Commit gate:** grep `wiki/` for `Status: Unresolved`; surface those before
  declaring a clean pass.
- Contradictions across changed pages and their 1st/2nd-degree neighbors.

---

## 11. Build discipline (large, resumable run)

- Work **category by category**, Day-1 layers first; within a category, vendor by
  vendor. **Commit after each vendor** (or at worst each category) so the run is
  resumable and you get version history for free.
- **Idempotent & log-driven:** on any run, read `log.md` + `index.md` to find what's
  already built and continue from the next unbuilt item. Don't redo finished pages.
- Keep `index.md` and `log.md` current as you go — they are how you (and the human)
  resume.
- Proceed autonomously through the phases; only stop for a **hard** contradiction
  you can't resolve, or a taxonomy decision you flag as needing the human. Record
  smaller judgment calls in `log.md` and keep moving.