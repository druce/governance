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

## [2026-06-28] research | Wave 1 results — M&A verifications (partial: R2/R3/R6 in)
- **Confirmed:** Splunk→Cisco (2024-03-18, $28B); Robust Intelligence→Cisco (2024-09, → Cisco AI Defense); Pangea→CrowdStrike (2025-09-16, ~$260M); Adaptive Shield→CrowdStrike (2024-11, ~$300M); Prompt Security→SentinelOne (2025-08-05, ~$250M); Promptfoo→OpenAI (2026-03-09).
- **Corrected seed:** Astrix→Cisco is announced INTENT (2026-05-04), NOT closed as of 2026-06-28 — soft contradiction noted on page. Galileo→Cisco intent (2026-04-09), close date medium-confidence.
- **NEW (not in seed):** TrojAI→A10 Networks (NYSE:ATEN), announced 2026-06-15.
- **Confirmed independent:** HiddenLayer ($50M A, 2023), WitnessAI ($86.5M total, Series B 2026-01). 
- **Fixes:** crowdstrike/sentinelone/cisco were mis-stubbed `acquired` (generator regex matched "acquirer") → corrected to public/subsidiary. robust-intelligence → thin alias of [[cisco-ai-defense]].
- Generator-bug note for lint: any acquirer mis-stubbed `acquired`; remaining acquirers (palo-alto-networks, f5, cato-networks) being fixed by their Wave-1 agents.

## [2026-06-28] research | portal26
- Researched Portal26 (ai-access-governance). Established former name = **Titaniam, Inc.** (rebranded 2023-10-10), NOT TripleBlind — build-note hint debunked against vendor rebrand release + website + aggregators. TripleBlind is an unrelated KC privacy startup.
- Ownership: independent, venture-backed (confidence high). Founded 2019 by Arti Arora Raman. Funding $15M total ($6M seed 2022 + $9M Series A 2025-11-04, led by Shasta Ventures, w/ Fusion Fund + Fortune 500 fin-services venture arm). HQ Los Gatos, CA.
- Platform: GenAI visibility / AI TRiSM / Shadow-AI discovery / policy enforcement / FIPS-140-2-marketed forensic vault / agentic-AI governance. SaaS. hedge_fund_fit medium (audit/recordkeeping appeal). 4 sources cached. status stub -> researched.
