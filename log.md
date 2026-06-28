# Op log

Append-only, chronological. Each entry: `## [YYYY-MM-DD] <op> | <subject>` where
`<op>` ∈ `setup | taxonomy | stub | research | compare | lint | decision`.
`grep "^## \[" log.md | tail` → recent activity.

## [2026-06-28] setup | scaffold & seeds
- `git init`; created directory layout per CLAUDE.md §2 (`raw/seeds`, `raw/sources`, `wiki/{categories,vendors,comparisons}`).
- Moved the two immutable seeds into `raw/seeds/`: `2026-06-19-AI-stack.md` (layer-cake spine) and `Governance & Security Stack — seed.csv` (survey categories). Not to be edited from here.

## [2026-06-28] taxonomy | reconciled layer-cake doc + CSV into 42 canonical categories
- Built `taxonomy.md`: doc = spine (7 layers), CSV mapped in. 42 canonical categories.
- Built `taxonomy-gaps.md` with decisions D1–D9 and open questions Q1–Q4.

## [2026-06-28] decision | taxonomy reconciliation choices
- D2: keep DSPM and DLP split against the CSV's merged question.
- D3: merge "AI Access Governance (CASB for AI)" + "Shadow-AI / Insider risk" → `ai-access-governance`.
- D4: merge doc "AI SecOps / Security Automation" → `ai-soc-analysts`.
- D5: split CSV "MCP / Agent Gateway & Tool Access" into `authorization-engine` + `mcp-gateway` + `tool-identity-integration`.
- D6: promote CSV-only `ai-red-teaming`, `identity-governance`, `non-human-identity` to canonical.
- D7: keep `comms-surveillance` separate from `ai-governance-platform`.
- D8: split bundled vendor cells (1Password/Doppler/Infisical, OPA/Styra, Immuta/Collibra, Obot/MintMCP); `Other (Please Specify)` excluded as vendors.
- Flagged Q1 (agent-security granularity), Q2 (process pages), Q3 (retrieval depth), Q4 (survey blueprint) for the human.

## [2026-06-28] decision | human sign-off on taxonomy + Q1–Q4 resolved
- Human approved the 42-category spine. Answers: Q1 = keep all 5 agent categories, note multi-category coverage. Q2 = 5 thin process pages. Q3 = stubs for `content-sources`/`vector-retrieval` pointing at `entitlement-aware-rag`. Q4 = build `comparisons/survey-blueprint.md` in Phase 4.
- Proceeding to Phase 1 (category pages) → 2 (vendor stubs) → 3 (research) → 4 (comparisons) → 5 (taxonomy pass + lint).

## [2026-06-28] setup | skeleton index.md + overview.md stub
- Created `index.md` content catalog (sections only; populated in Phase 1+).
- Created `wiki/overview.md` thesis stub from the layer-cake doc.
- **PAUSED for human sign-off on taxonomy before building pages (Phase 0 step 5).**

## [2026-06-28] stub | Phase 1 complete — 42 category pages (8 parallel agents)
- All 42 category pages drafted by 8 parallel subagents (by layer), each with frontmatter, body sections, exact-slug wikilinks, and `## Survey` scaffolding (skipped for pure-process pages). content-sources/vector-retrieval are stubs pointing at entitlement-aware-rag.
- Regenerated `index.md` from frontmatter (42 categories + 222 vendors, grouped by layer / primary category).

## [2026-06-28] research | Phase 3 Wave 1 launched — M&A verification (6 parallel agents)
- Priority wave: ~30 M&A-flagged + anchor vendors grouped by acquirer (Palo Alto, Cisco, CrowdStrike/SentinelOne, F5/Cato/CheckPoint/Tenable, big-infra, OpenAI/misc). Each verifies seed acquisition claims against primary sources, caches to raw/sources/, fills the vendor page.
