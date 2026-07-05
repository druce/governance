---
name: wiki-create
description: Use when adding a new vendor or category page to the wiki, when a survey-v2.csv row has no page, or when a new entrant/category needs scaffolding.
---

# Wiki Create

Scaffold new pages from the templates in this directory, pre-filled from
`survey-v2.csv`, with every unanswered SCHEMA.md question stubbed as an open
question — never invented.

## New vendor page

1. **Check for an existing page first** — one canonical page per vendor.
   Search `wiki/vendors/` for the name, `aka:` values, and post-acquisition
   product names. If it exists, update it (see `wiki-research`); never fork.
2. Slug = kebab-case **company** name (product slug only when the product is
   the shopping unit — record that choice in `log.md`).
3. Copy `templates/vendor-page.md` → `wiki/vendors/<slug>.md`. Prefill from
   the CSV row: name, `primary_category` (map the CSV category via
   `survey_question` in `taxonomy.yaml`), website, and graduate any CSV
   Flag/Note into the Gotchas stub. Everything unknown stays `null` /
   `unverified` with an Open Questions bullet.
4. Register it: CSV row (add one if missing, with Wiki URL), the category
   page's vendor list (one-line positioning), `index.md`.
5. `log.md` `stub` entry → run `wiki-lint` mechanical pass → commit → then
   `wiki-research` to fill it.

## New category page

1. A category exists only if it's in `taxonomy.yaml` — add the entry there
   first (slug, layer, tier, trigger, adjacency, `agent_security_context`),
   run `python3 scripts/gen_taxonomy_md.py`, and log a `decision`.
2. Copy `templates/category-page.md` → `wiki/categories/<slug>.md`; frontmatter
   values must match the taxonomy entry (lint enforces this).
3. Stub all SCHEMA.md §1 sections; add the `## Survey` scaffolding section
   only if `adoption_tier` ≠ `practice`.
4. Register in `index.md`; `log.md` entry; lint; commit.

## Rules

- No page without a `taxonomy.yaml`-valid category. No duplicate vendors.
- Trifecta discussion only if `agent_security_context: true` (SCHEMA.md §0).
- A stub with honest open questions beats a filled-in guess.
