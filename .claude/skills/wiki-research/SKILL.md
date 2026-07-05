---
name: wiki-research
description: Use when verifying or refreshing wiki facts — stale last_verified dates, unconfirmed acquisitions, null/unverified frontmatter fields, items in the lint or migration research queue, or when asked to research/update a specific vendor or category.
---

# Wiki Research

Work the research queue: verify churn-prone facts (ownership, funding,
renames, deployment, FS traction) against primary sources and upgrade pages to
answer every SCHEMA.md §2 (vendor) / §1 (category) question.

## Queue sources (in priority order)

1. `reports/lint-*.md` → `research` section (most recent report)
2. `migration-report.md` (unmapped v1 fields)
3. A vendor/category the user names

## Per-vendor loop (commit after each)

1. **Search** the SCHEMA.md §6 question bank, ownership first:
   `"<vendor> acquisition OR funding OR rename <year>"`. Prefer primary sources
   (acquirer's press release, filings, vendor docs) over aggregators.
2. **Cache** every load-bearing source to
   `raw/sources/YYYY-MM-DD--<vendor-slug>--<source-slug>.md` — top of file:
   URL, fetch date, one-line "good for" note.
3. **Update frontmatter** (vocab per `taxonomy.yaml`): `ownership_state`,
   `owner`, `acquisition` (keep **announced vs closed** dates distinct),
   `market_position` (per category, justified in body), `deployment_model`,
   `form_factor`, `data_leaves_tenancy`, `integrations`, `mcp_support`,
   `certifications`, `pricing_model`, `fs_traction`. Set `last_verified` to
   today; set/clear `verify_after` (required while `acquired-pending`).
   Add `sources:` entries `{claim, url, date, confidence}` for each changed claim.
4. **Update body** per SCHEMA.md §2 — especially differentiators vs named
   peers, anti-fit ("who should not buy"), gotchas, data-handling. Append a
   dated `History` line; never silently overwrite a prior claim (contradiction
   rules: CLAUDE.md §8).
5. **Ripple**: update the category page's one-line positioning if it changed;
   update the `survey-v2.csv` Flag/Note if ownership/naming changed.
6. `log.md` `research` entry → run `wiki-lint` mechanical pass on touched
   pages → commit.

## Hard rules

- **Never invent.** Unknown stays `null`/`unverified` + an Open Questions
  bullet. "Couldn't find" ≠ "doesn't exist."
- Announced ≠ closed: prose must not say "acquired by" until the deal closed.
- Trifecta framing only where `agent_security_context: true` (SCHEMA.md §0).
- Date every volatile claim; confidence lives on the source entry.
