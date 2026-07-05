# CLAUDE.md — AI Governance & Security Vendor Wiki

This repo is a **research wiki** about the enterprise AI governance/security vendor
landscape, built and maintained by you (the LLM agent). It follows Karpathy's
LLM-wiki pattern, adapted for a landscape you **research from the web** rather than
a corpus that already exists on disk.

You write and maintain everything in `wiki/`, `index.md`, `log.md`, and the
taxonomy. The human curates direction and asks questions. The two seed files in
`raw/seeds/` are immutable inputs, not gospel.

**Where things are defined (schema v2, 2026-07-05):**

| Concern | Source of truth |
|---|---|
| Page schemas, required questions, lint rules, research question bank | `SCHEMA.md` |
| Category slugs, layers, adoption tiers, controlled vocabularies | `taxonomy.yaml` (machine-readable; `taxonomy.md` is **generated** from it) |
| Canonical survey list | `survey-v2.csv` (lint enforces CSV ↔ wiki bijection) |
| Workflows | `.claude/skills/`: `wiki-create` (scaffold), `wiki-research` (verify/fill), `wiki-lint` (check) |
| Mechanical tooling | `scripts/`: `wiki_lint.py`, `migrate_frontmatter.py`, `gen_taxonomy_md.py` |

---

## 1. Purpose & audience

The reader is a **hedge-fund / asset-manager CTO trying to understand this space**:
what each category is for, when they actually need it (Day-1 vs Day-2), which
vendors fill each slot, who owns whom now, and how to tell neighbors apart.

A second consumer is **survey design**: the output fine-tunes a survey of what CTOs
are currently *using* and *evaluating*. Category pages double as survey scaffolding
(SCHEMA.md §1.6, §4) and the taxonomy must map cleanly onto survey questions.

Write for a smart, busy technical buyer. Plain English, no marketing voice, no
hype. Neutral and comparative. Name tradeoffs. Flag uncertainty instead of
papering over it.

**Lethal-trifecta policy (SCHEMA.md §0):** the trifecta (untrusted input +
sensitive data + egress in one agent context) is the core **agent-security**
threat model. Discuss it only on pages whose category has
`agent_security_context: true` in `taxonomy.yaml`, and in `wiki/overview.md`.
Everywhere else, describe risk in plain terms — no trifecta framing, no
`trifecta_*` frontmatter. Editorial lint rule 18 enforces this.

---

## 2. Architecture (three layers)

- **`raw/`** — immutable inputs and cached research. You read from it, never edit
  the seeds.
  - `raw/seeds/` — the two original inputs (layer-cake blog doc + original survey
    CSV). Never modify.
  - `raw/sources/` — research you fetch from the web, saved as dated markdown so
    claims stay anchored to retrievable evidence. Filename:
    `YYYY-MM-DD--<vendor-or-topic-slug>--<short-source-slug>.md`. Top of each file:
    the URL, the fetch date, and a one-line note on what it's good for.
- **`wiki/`** — the pages you generate and own (vendors, categories, comparisons,
  overview).
- **The schema** — `SCHEMA.md` + `taxonomy.yaml` + this file. You and the human
  co-evolve them; log every schema change as a `decision`.

### Directory layout

```
/
├── CLAUDE.md            # working agreements (this file)
├── SCHEMA.md            # page schemas + lint rules + research question bank
├── taxonomy.yaml        # SOURCE OF TRUTH: categories, vocab enums
├── taxonomy.md          # GENERATED from taxonomy.yaml — never hand-edit
├── taxonomy-gaps.md     # mismatches, orphans, proposed renames, open questions
├── survey-v2.csv        # canonical survey list (categories × products)
├── index.md             # content catalog — regenerate via wiki_lint.py --write-index
├── log.md               # chronological, append-only op log
├── migration-report.md  # v1→v2 migration flags (research queue seed)
├── reports/             # dated lint reports
├── scripts/             # wiki_lint.py, migrate_frontmatter.py, gen_taxonomy_md.py
├── .claude/skills/      # wiki-create, wiki-research, wiki-lint
├── raw/                 # seeds/ (immutable) + sources/ (dated cache)
└── wiki/
    ├── overview.md      # the thesis / map of the whole space
    ├── categories/      # one page per category
    ├── vendors/         # one page per vendor
    └── comparisons/     # cross-cutting comparison pages (filed-back answers)
```

---

## 3. Conventions

- **Markdown + relative links.** The published GitHub/Quartz site needs standard
  markdown links, so pages use `[slug](../vendors/slug.md)` form. If you author
  with Obsidian-style `[[wikilinks]]`, convert before pushing (decision logged
  2026-06-28). Lint rule 10 checks link integrity.
- **Slugs are kebab-case.** Vendor slug = the company, not the product, e.g.
  `palo-alto-networks` with products noted on the page. When a product is the unit
  people shop for, you may slug the product (`prisma-airs`) and cross-link the
  parent — record the choice in `log.md` and stay consistent.
- **One page per vendor, multiple category tags** (`primary_category` +
  `also_listed_in`). Never create duplicate vendor pages; category pages link,
  never fork.
- **Split bundled seed entries** (e.g. `1Password / Doppler / Infisical`) into
  separate vendor pages; note the split in `log.md`.
- **Skip survey artifacts.** `Other (Please Specify)` rows are survey UI, not
  vendors.
- **YAML frontmatter on every page** per SCHEMA.md §4; `title:` is required
  (Quartz uses it).
- **Dates are ISO** (`YYYY-MM-DD`). Always date claims that can go stale.

---

## 4. Page formats

Vendor and category page schemas — frontmatter fields, required body questions,
controlled vocabularies — live in **`SCHEMA.md`** (§1–§4). Templates:
`.claude/skills/wiki-create/templates/`. Two formats defined here:

### 4.1 log.md

Append-only, chronological. Every entry starts with a greppable prefix:

```
## [YYYY-MM-DD] <op> | <subject>
```

where `<op>` ∈ `setup | taxonomy | stub | research | compare | lint | decision`.
`grep "^## \[" log.md | tail` gives recent activity. Record decisions (slug
choices, splits, renames, moves, contradictions resolved, schema changes) here.

### 4.2 index.md

Content catalog, one line per page, grouped by section. **Generated**: run
`python3 scripts/wiki_lint.py --write-index` after any batch of page changes.
Read it first when answering a query.

---

## 5. Taxonomy

- `taxonomy.yaml` is the single source of truth: category slugs, display names,
  layers, adoption tiers, triggers, adjacency, `agent_security_context` flags,
  and every vocab enum the lint validates against.
- To add/rename/move a category: edit `taxonomy.yaml`, run
  `python3 scripts/gen_taxonomy_md.py`, log a `decision`, and fix affected pages
  (lint rule 3 catches stragglers).
- A vendor can belong to several categories: pick a sensible `primary_category`,
  tag the rest in `also_listed_in`.
- Open taxonomy questions live in `taxonomy-gaps.md`.

---

## 6. Survey scaffolding

Category pages with a non-null `survey_question` end with a `## Survey` section:
question (use/evaluate framing), answer options (the real shortlist +
`Other (Please Specify)`), the seed response scale (*multi-select; Interested;
Considering/evaluating; Pilot/implementing; In production; Would recommend; Would
not recommend*), and notes for survey design (table-stakes vs niche, confusing
overlaps, M&A that dates an option). `practice`-tier categories carry **no**
survey section.

---

## 7. Research & sourcing rules

- Use web search + fetch. **Cache** what you rely on into `raw/sources/` (dated)
  and cite it. Anchor claims to sources; don't let synthesis drift from evidence.
- **Verify seed/CSV notes** — treat every flag (especially M&A) as a hint, not a
  fact. Confirm acquisitions against the acquirer's or another primary source,
  with a date. **Announced ≠ closed** — track both dates; `acquired-pending`
  requires a `verify_after` date.
- Prefer primary sources; label vendor marketing as marketing; prefer independent
  corroboration for differentiation claims.
- **Never invent.** Unknown values stay `null`/`unverified` with an open-questions
  note, not a guess. Distinguish "couldn't find" from "doesn't exist."
- Note the **as-of date** for anything volatile; confidence lives on the source
  entry (`sources:` in frontmatter or the `## Sources` list).

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

  and log a `decision` entry. Resolve with a source, or leave flagged for the
  human. The lint commit gate blocks on `Status: Unresolved`.

---

## 9. Operations

| Job | Skill | Notes |
|---|---|---|
| Add a vendor/category page | `wiki-create` | scaffold from template + CSV row; stub unknowns |
| Verify/refresh facts, work the research queue | `wiki-research` | SCHEMA.md §6 question bank; cache sources; commit per vendor |
| Check health, pre-commit gate | `wiki-lint` | `scripts/wiki_lint.py` (mechanical) + editorial LLM pass |

**Query.** Read `index.md`, drill into relevant pages, synthesize with citations.
**File good answers back** as a `comparisons/` page so explorations compound.

---

## 10. Lint

Rules live in SCHEMA.md §5. Run `python3 scripts/wiki_lint.py --report` for the
mechanical pass (add `--online` ~monthly for URL liveness; `--write-index` to
regenerate the catalog); the `wiki-lint` skill layers the editorial pass on top.
**Commit gate:** zero `error`-severity findings and no `Status: Unresolved` in
`wiki/` before declaring a clean pass. `research`-severity findings are the
`wiki-research` queue, not failures.

---

## 11. Build discipline (large, resumable runs)

- Work **category by category**, Day-1 tiers first; within a category, vendor by
  vendor. **Commit after each vendor** (or at worst each category) so the run is
  resumable and you get version history for free.
- **Idempotent & log-driven:** on any run, read `log.md` + `index.md` to find
  what's already built and continue from the next unbuilt item. Don't redo
  finished pages.
- Keep `index.md` and `log.md` current as you go — they are how you (and the
  human) resume.
- Proceed autonomously; only stop for a **hard** contradiction you can't resolve,
  or a taxonomy decision you flag as needing the human. Record smaller judgment
  calls in `log.md` and keep moving.
