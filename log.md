---
title: "Build log"
---

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
- **Fixes:** crowdstrike/sentinelone/cisco were mis-stubbed `acquired` (generator regex matched "acquirer") → corrected to public/subsidiary. robust-intelligence → thin alias of [cisco-ai-defense](wiki/vendors/cisco-ai-defense.md).
- Generator-bug note for lint: any acquirer mis-stubbed `acquired`; remaining acquirers (palo-alto-networks, f5, cato-networks) being fixed by their Wave-1 agents.

## [2026-06-28] research | portal26
- Researched Portal26 (ai-access-governance). Established former name = **Titaniam, Inc.** (rebranded 2023-10-10), NOT TripleBlind — build-note hint debunked against vendor rebrand release + website + aggregators. TripleBlind is an unrelated KC privacy startup.
- Ownership: independent, venture-backed (confidence high). Founded 2019 by Arti Arora Raman. Funding $15M total ($6M seed 2022 + $9M Series A 2025-11-04, led by Shasta Ventures, w/ Fusion Fund + Fortune 500 fin-services venture arm). HQ Los Gatos, CA.
- Platform: GenAI visibility / AI TRiSM / Shadow-AI discovery / policy enforcement / FIPS-140-2-marketed forensic vault / agentic-AI governance. SaaS. hedge_fund_fit medium (audit/recordkeeping appeal). 4 sources cached. status stub -> researched.

## [2026-06-28] research | ibm-contextforge
Researched IBM ContextForge MCP Gateway (github.com/IBM/mcp-context-forge). Established: Apache-2.0 OSS MCP/A2A/REST-gRPC gateway+registry+proxy, Python/FastAPI, self-host via PyPI/Docker/K8s (Redis federation), transports stdio/SSE/streamable-HTTP/WebSocket/JSON-RPC, REST-to-MCP wrapping, virtual servers, auth (Basic/JWT/OAuth), OTel observability, 40+ plugins. Used in IBM watsonx Orchestrate tutorials (on Code Engine). Ownership=public (IBM, NYSE:IBM, Armonk), confidence high; commercial support model unconfirmed — appears community/corporate-backed OSS, flagged to verify. Latest release v1.0.4 (2026-06-23). hedge_fund_fit=medium. Kept category [mcp-gateway](wiki/categories/mcp-gateway.md). Cached 2 source files. No contradictions.

## [2026-06-28] research | github-advanced-security
Researched GHAS. Product (not company) of GitHub, a Microsoft subsidiary (acq. announced 2018-06, closed 2018-10-26, ~$7.5B) — ownership: subsidiary, high confidence. Components: CodeQL SAST/code scanning, secret scanning + push protection, Dependabot/dependency review, Copilot Autofix. Verified 2025 repackaging into two separately purchasable products: GitHub Secret Protection ($19/committer/mo) and GitHub Code Security ($30/committer/mo), announced 2025-03-04, GA to Team plans 2025-04-01 via metered billing. Deployment SaaS + Enterprise Server. hedge_fund_fit: high (Day-1 if shipping AI-generated code on GitHub; tier upgrade, not new vendor). 2 sources cached. status stub -> researched.

## [2026-06-28] research | gitlab
Researched GitLab (Ultimate). Public company, NASDAQ: GTLB, IPO 2021-10-14 (~$10B), founded 2014 (Zaporozhets & Sijbrandij), all-remote SF HQ — ownership: public, high confidence. Ultimate tier bundles SAST/DAST/dependency scanning/secret detection/container scanning/license compliance. Deployment SaaS + self-managed/on-prem. M&A: verified Datadog acquisition is RUMORED/UNCONFIRMED (Reuters 2024-07; renewed Oct 2025 ~$60/share buzz; Wolfe Research skeptical) — no definitive agreement or 8-K found as of 2026-06-28; kept ownership public with dated note. No hard contradiction. hedge_fund_fit: high. 2 sources cached. status stub -> researched.

## [2026-06-28] research | jfrog
Researched JFrog (NASDAQ: FROG). Public — IPO Sept 2020 (~$509M at ~$3.9B); founded 2008 Netanya (Ben Haim/Landman/Simon); dual HQ Sunnyvale+Netanya. Artifactory (universal binary repo) + Xray (SCA/scanning) = software-supply-chain spine; JFrog ML / model-management via Qwak acquisition (announced 2024-06-25, ~$230M press-reported, undisclosed by JFrog). ownership=public, confidence high. hedge_fund_fit medium (Day-1 if shipping AI-gen code at scale). 2 sources cached. status stub -> researched.

## [2026-06-28] research | sonatype
Researched Sonatype. CORRECTION to seed brief: Vista Equity Partners majority interest was announced 2019-11-18 (NOT ~2024/2025); majority stake, existing investors retained some — PE-controlled. Founded 2008 Fulton MD by Maven creators Brian Fox & Jason van Zyl; stewards Maven Central. Products: Nexus Repository + Lifecycle/IQ SCA + Repository Firewall (blocks malicious OSS). ownership=acquired (Vista), confidence high on 2019 event. hedge_fund_fit medium. 2 sources cached. status stub -> researched.

## [2026-06-28] research | aikido-security
Researched Aikido Security. Independent VC-backed; founded 2022 Ghent, Belgium (Delbare/Delrue/Garriau). Funding ~$84M total: pre-seed €2M (Jan 2023), seed €5M (Nov 2023), Series A $17M (May 2024, Singular), Series B $60M (Jan 2026, $1B unicorn, led by DST Global w/ PSG Equity/Notion/Singular) — fastest EU cyber unicorn. Consolidated dev-first all-in-one AppSec (SCA/SAST/secrets/IaC/container/DAST/cloud); SaaS, no binary repo. ownership=independent, confidence high. hedge_fund_fit medium (Day-1 candidate for small fund shipping AI-gen code). 2 sources cached. status stub -> researched.

## [2026-06-28] research | Phase 3 complete — all 222 vendors researched (Waves 1–4)
- Wave 1 (M&A core), Wave 2 (Day-1 AI-native), Wave 3 (Day-2 agent/AI + governance), Wave 4 (foundation/infra). ~378 sources cached to raw/sources/.
- ~30 seed M&A flags verified against primary sources; ~20 NEW deals discovered (not in seed) — see [ai-security-m-and-a-map](wiki/comparisons/ai-security-m-and-a-map.md).

## [2026-06-28] compare | Phase 4 — overview thesis + 6 comparison pages
- Built: ai-security-m-and-a-map, ai-gateways-head-to-head, runtime-ai-firewalls, entitlement-aware-rag-options, day-1-for-a-50-person-fund, survey-blueprint. Fleshed overview.md into full thesis.

## [2026-06-28] decision | Phase 5 taxonomy pass — 42-category spine held; vendor moves R1–R9
- jazz-security→dlp; immuta→data-access-governance primary; collibra→ai-governance-platform primary; aurascape +ai-runtime-security; symmetry-systems ownership corrected (Zscaler). See taxonomy-gaps.md "Phase 5".

## [2026-06-28] lint | clean pass
- 0 broken wikilinks, 0 orphans, 0 stubs (222/222 researched), 0 "Status: Unresolved", 0 unverified-M&A (acquired+low). Both commit gates pass. 6 zero-vendor categories are intentional (process + third-party-ai-apps). Regenerated index.md.

## [2026-06-28] decision | converted [[wikilinks]] -> relative markdown links (Option A)
- Converted 5,415 `[[slug]]` / `[[slug|alias]]` links across 275 md files to relative `[text](path.md)` links so they render as clickable in GitHub's repo view (GHFM does not resolve `[[ ]]`). 0 unresolved, 0 broken targets, 0 wikilinks remaining. Excluded Claude.md (convention examples) and conversation.txt (transcript). Updated Claude.md §3 note.

## [2026-06-28] decision | Quartz published site on GitHub Pages
- Added .github/workflows/deploy-quartz.yml (clones Quartz v4 at build time, assembles repo md as content preserving layout so relative links resolve, builds, deploys to Pages). quartz.config.ts + quartz.layout.ts at root. Site: https://druce.ai/governance/ . Excludes raw/, conversation.txt, prompts, Claude.md from the published site. CustomOgImages disabled for build speed.

## [2026-06-30] research | artemis-security
- Added vendor (user request). Category: ai-soc-analysts (AI-native SecOps / agentic SOC / SIEM-replacement). Flagged soft scope note: "AI for security," not "security for AI" — defends enterprise infra with AI agents, does not govern LLM usage/egress; trifecta = none. Established: emerged from stealth 2026-04-15 with $70M ($15M seed + $55M Series A, Felicis lead); NYC HQ, Israeli-founded; founders Shachar Hirshberg (ex-Demisto/AWS GuardDuty, CEO) & Dan Shiebler (ex-Abnormal AI, CTO); federated-query architecture. ownership_confidence high; customer logos + metrics unverified. Cached 1 source. Updated ai-soc-analysts (vendor + survey, count 9→10) + index.

## [2026-06-30] research | audition-ai
- Added vendor (user request). Primary category: enterprise-ai-assistant (finance-vertical, in-tenant secure AI assistant + agent platform); secondary tags ai-governance-platform (usage GRC) + dlp. Cross-listed on all three category pages. Established: product of Saberin Data Platform, Inc. (Saberin Group, founded 2007), Hauppauge NY; private/bootstrapped — no external/VC funding found (recorded as none, not a guess); no M&A; ownership_confidence high, funding confidence med (absence of evidence). Deploys into customer's Azure tenant via Azure AI Foundry (multi-model), Entra zero-trust, permission-aware retrieval, dual-layer DLP + "Generative Rules", immutable audit. Trifecta: strong sensitive-data, partial egress, weak untrusted-input (Sidekick shell/browser/file agents flagged as open risk). hedge_fund_fit high (purpose-built) with small-vendor caveat. Cached 1 source. Updated enterprise-ai-assistant (vendor + survey + design note, count 8→9), ai-governance-platform, dlp + index.

## [2026-07-05] decision | schema v2: SCHEMA.md + taxonomy.yaml + skills + scripts
- Promoted the user's draft spec (draft.md, now deleted) to SCHEMA.md: richer vendor/category page questions, controlled vocabularies, mechanical (§5.1) + editorial (§5.2) lint rules, research question bank. taxonomy.yaml is now the machine source of truth (42 categories, vocab enums); taxonomy.md is GENERATED via scripts/gen_taxonomy_md.py. survey-v2.csv committed as the canonical survey list (lint rule 1 bijection target). Added scripts/ (wiki_lint.py, migrate_frontmatter.py, gen_taxonomy_md.py) and project skills .claude/skills/{wiki-create,wiki-research,wiki-lint}. index.md is now generated by wiki_lint.py --write-index. Claude.md slimmed to conventions + pointers. Vocab extensions vs draft: adoption_tier `practice`, multi-valued `form_factor`, `alias_of` for redirect stubs.

## [2026-07-05] decision | lethal trifecta scoped to agent-security contexts
- Policy (SCHEMA.md §0): the trifecta is the core agent-security threat model, discussed only where agent_security_context: true (ai-runtime-security, agent-runtime-security, mcp-gateway, authorization-engine, tool-identity-integration, enterprise-browser, browser-security-extension, trust-zone-segmentation) + overview.md. Removed trifecta_relevance/trifecta_role frontmatter everywhere; rewrote 177 vendor + 34 category pages in plain risk language ("## Lethal-trifecta role" → "## Security role"); reframed the 8 agent-security category pages ("## Agent-security role: the lethal trifecta") and overview.md §3. Editorial lint rule 18 enforces the scoping. Note: a handful of History log lines contained trifecta jargon and were minimally reworded in place (terminology only, dates/facts preserved) to satisfy the zero-grep sweep.

## [2026-07-05] taxonomy | frontmatter migrated v1 → v2 (266 pages)
- scripts/migrate_frontmatter.py: vendors — categories→primary_category/also_listed_in, ownership→ownership_state (incl. pe-owned detection), acquirer extracted to owner, acquisition dates split announced/closed, deployment split into deployment_model+form_factor, last_updated→last_verified; dropped layer/hedge_fund_fit/priority/trifecta_relevance/status/confidence/sources_count/ownership_confidence (confidence now lives per-source). Categories — tier/trigger/adjacency/maturity pulled from taxonomy.yaml. migration-report.md flags 24 pages (unmapped values, unconfirmed close dates) → research queue. Hand-fixes: astrix-security (pending, not closed — "(not closed)" phrasing defeated the pending heuristic), layerx owner, robust-intelligence alias_of.

## [2026-07-05] lint | first schema-v2 pass: 0 errors
- reports/lint-2026-07-05.md: 0 errors, 41 warns, 6 research-needed across 273 pages. Warns: 18 infra pages not in survey CSV (expected — content-sources/vector-retrieval etc.), 14 acquired vendors whose CSV option lacks "X (Acquirer)" rendering (survey-design queue), 9 CSV Flag/Note phrases with no trace on the page. Research queue: unconfirmed close dates (galileo, normalyze, github-codespaces, hashicorp-sentinel, ibm-watsonx-governance) + astrix/natoma pending re-verify. Both commit gates pass. index.md regenerated.

## [2026-07-09] research | entro-security acquired by SailPoint (verified, closed)
- User flag verified against SailPoint's close press release (GlobeNewswire wire copy) + SecurityWeek: intent announced 2026-06-18, **closed 2026-06-29**; price not officially disclosed, ~$200M reported by Calcalist (med confidence). Founders Alvas/Cheriki joined SailPoint; product sold standalone while integrating into SailPoint Agentic Fabric. Updates: entro-security.md (ownership independent → acquired-closed, owner SailPoint, dates/price, body, sources, history), sailpoint.md (as-acquirer note), non-human-identity.md + secrets-management.md (positioning, M&A dynamics, survey option "Entro Security (SailPoint)"), survey-v2.csv (row flag + SailPoint IGA row note; fixed "Sailpoint" → "SailPoint"), ai-security-m-and-a-map.md (new closed-deal row). Cached 2 sources in raw/sources/.

## [2026-07-09] decision | knostic recategorized entitlement-aware-rag → agent-runtime-security
- User flag verified against knostic.ai (2026-07-09): site now leads with "Security Across the Agentic Lifecycle" — Kirin (runtime least-privilege / injection-blocking for agents, coding assistants, MCP servers), AgentMesh (supply-chain reputation; VirusTotal Crowdsourced AI 2026-06), Shadow AI Spotlight, OpenAnt. CSA Agentic AI Security Innovator Market Map places Knostic in Governance/Observability/Supply Chain Integrity. The original need-to-know/Copilot-oversharing product is still offered, so this is a re-lead, not a replacement: primary_category → agent-runtime-security; also_listed_in [entitlement-aware-rag, ai-access-governance, enterprise-ai-assistant]. Updated knostic.md, agent-runtime-security.md (vendor list + survey option), entitlement-aware-rag.md (note; option stays), ai-access-governance.md (Shadow AI Spotlight cross-list), taxonomy.yaml notes (+ regenerated taxonomy.md), survey-v2.csv (new Agent Security row; entitlement row note updated). Cached 1 source.

## [2026-07-13] stub | surepath-ai (created + researched same day)
- User-requested addition (not in seeds): SurePath AI (surepath.ai). Primary category **ai-access-governance** — network-based shadow-AI discovery (network redirects + out-of-band analysis, no per-app integrations), intent classification, inline redaction/RBAC, sanctioned enterprise GenAI portal, agent/MCP call tracing (F5 claim). Founded 2023, Denver CO; $5.2M seed 2024-11-14 (Uncork Capital, Operator Collective; $6.3M total). **Acquisition by F5 announced 2026-06-22** with the F5 AI Security Platform launch — close date not stated → ownership_state acquired-pending, verify_after 2026-10-01. Updates: new surepath-ai.md, ai-access-governance.md (vendor list, count 11→12, M&A dynamics, survey option "SurePath AI (F5)"), f5.md (second-acquisition ripple), survey-v2.csv (new Shadow-AI row). Cached 3 sources in raw/sources/.

## [2026-07-13] stub | google-cloud-identity + aws-iam (CSV gap fill)
- The human's "edit csv" commit (0bb1c33) added General Identity options "Google Cloud Identity" and "AWS" with no wiki pages, tripping lint R1 errors. Scaffolded both as stubs: google-cloud-identity.md (Google's IdP/SSO, Workspace-shop default) and aws-iam.md ("AWS" scoped to IAM + IAM Identity Center, parallel to aws-secrets-manager slugging — cloud IAM more than workforce IdP). Updated identity-access.md (vendor list, count 5→7, survey options + AWS-ambiguity design note), survey-v2.csv Wiki URLs. All facts beyond ownership left TBD for wiki-research.

## [2026-07-13] research | acuvity + teleskope added; SurePath-competitor triage
- User pasted Google's list of SurePath "competitors" for triage. **Added 2:** acuvity.md (primary ai-access-governance, cross-listed agent-runtime-security; RYNO platform, shadow-AI from endpoints/browsers + agent/MCP runtime; $9M seed Foundation Capital; **acquired by Proofpoint, announced as completed 2026-02-12**, terms undisclosed — Proofpoint's 2nd data/AI buy after Normalyze) and teleskope.md (primary dspm, cross-listed dlp; agentic DSPM with native remediation + external-LLM egress prevention; NYC, founded 2022, Elizabeth Nammour ex-Airbnb; $32.2M total, $25M Series A M13 2025-10-31; independent). Updated: ai-access-governance (count 13, M&A, survey "Acuvity (Proofpoint)"), agent-runtime-security (count 8, cross-list), dspm (count 16, survey option), dlp (cross-list), surepath-ai.md (competitors), ai-security-m-and-a-map.md (Acuvity→Proofpoint row + backfilled SurePath→F5 row), survey-v2.csv (2 rows). Cached 3 sources.

## [2026-07-13] decision | SurePath-competitor triage: skipped candidates (recorded so we don't re-litigate)
- **Aona AI** — genuine ai-access-governance fit (workforce shadow-AI, positions vs SurePath) but Sydney pre-seed micro-startup: ~$350K raised (Antler/Tenity), 1–10 employees. Below survey-shortlist bar; revisit if it raises a real round.
- **Sekura.ai** — mislabeled by Google: autonomous pentesting/AppSec (SAST/DAST + LLM-security testing), not shadow-AI governance; closest slot would be ai-red-teaming but it's app-pentest-led and micro-scale. Skip.
- **SolasAI** (algorithmic fairness for credit/insurance decisioning, BLDS spin-out) and **FairNow** ($3.5M seed AI-governance GRC, HR/bias-audit skew) — real ai-governance-platform-adjacent products but fair-lending/HR-compliance focus, low hedge-fund relevance and low recognition; skip for survey purposes.
- **Zendata** — $2M seed no-code privacy/AI governance; too early. Skip.
- **Fractal Analytics / EXL / Artefact** — consultancies/services, out of wiki scope. **Dataiku / SageMaker / Google Dataplex / Azure Responsible AI / Unity Catalog** — DS/MLOps platforms and hyperscaler toolkits, not the security/governance product survey. Google's "competitor" list conflates category neighbors with actual rivals; only Acuvity (and marginally Aona) truly compete with SurePath.

## [2026-07-13] lint | R5 acquirer-rendering pass: CSV options renamed, 3 misclassifications fixed
- Fixed lint bucket "acquired vendor lacks X (Acquirer) rendering" (user request). **Renamed 10 CSV options** to the recognizable "X (Acquirer)" form: Langfuse (ClickHouse), TruLens (Snowflake), TrojAI (A10 Networks), Natoma (Snowflake) ×2 rows, LayerX (Akamai) (was "LayerX browser extension"), Seraphic (CrowdStrike), Conjur (CyberArk), Symmetry Systems (Zscaler), GitHub Advanced Security (Microsoft). Convention: acquirer suffix applied for pending deals too (recognition > deal-status precision; status stays in the Flag column) — consistent with SurePath AI (F5) / CalypsoAI (F5).
- **3 pages were misclassified, not mislabeled** — fixed the frontmatter instead of the CSV: forcepoint acquired-closed → **pe-owned** (Francisco Partners take-private 2021; also cleared stray acquisition dates that belonged to the TPG/G2CI carve-out), sonatype acquired-pending → **pe-owned** (Vista majority 2019; "pending" was a migration artifact, cleared verify_after), ibm-watsonx-governance acquired-closed → **public** (first-party IBM product; also clears its R4 unconfirmed-close research item).

## [2026-07-15] decision | citizen-dev primer spec
Approved outline for a new document: "Citizen Development in a Hedge Fund — A Primer
and Implementation Guide" (CTO audience, full program playbook, enterprise-grade tool
scope). Spec: `docs/superpowers/specs/2026-07-15-citizen-dev-primer-design.md`.
Draws on the 12-dimension maturity framework (druce.ai ai_maturity.html), the
2026-04 ai-implementation post (Crawl→Fly), and this wiki's trust-zone / risk-tier /
promotion-gate categories. Ch 6 tool claims flagged for research-at-writing-time.

## [2026-07-27] research | optro (ex-auditboard)
User flagged AuditBoard rename. VERIFIED: AuditBoard renamed to **Optro** (announced 2026-03-09 at IIA Great Audit Minds; new domain optro.ai). Ownership unchanged (Hg PE, 2024, >$3B). Also picked up: new CEO Raul Villar Jr. (2025-07), FairNow (AI governance) acquired fall 2025. Sources cached: `raw/sources/2026-07-27--optro--rebrand-announcement.md`.

## [2026-07-27] decision | slug rename auditboard → optro
Per slug convention (vendor slug = company name), `wiki/vendors/auditboard.md` → `wiki/vendors/optro.md` (git mv), `aka: [AuditBoard, SOXHUB]`. All inbound links updated (archer, logicgate, onspring, servicenow, enterprise-grc, risk-tiers). CSV product renamed to "Optro (formerly AuditBoard)" — keep the "formerly" qualifier on survey options while the new name is unfamiliar.

## [2026-07-27] decision | survey question labels renamed
User renamed CSV category labels: "Enterprise GRC" → "Enterprise Governance, Risk & Compliance"; "Vendor Risk" → "Vendor Risk Rating & Monitoring". Rippled into `taxonomy.yaml` `survey_question` + both category pages' frontmatter; taxonomy.md regenerated. `seed_csv`/`maps_to_seed_csv` keep the original seed names. Also fixed unquoted comma in the new GRC label that broke CSV parsing.

## [2026-07-27] stub | drata, venminder, whistic
User asked whether to add Drata, Venminder, Whistic. Added all three, created + researched same day:
- **drata** → enterprise-grc (compliance automation, Vanta's closest rival; independent, $2B valuation Series C 2022; NO SailPoint acquisition found — rumor checked and unsubstantiated).
- **venminder** → vendor-risk (TPRM assessments; acquired by Ncontracts announced 2024-09-04 via Hg buyout).
- **whistic** → vendor-risk (questionnaire automation / vendor-profile network; independent, Series B 2022 JMI Equity).
Category pages, survey options, taxonomy notes, and CSV rows updated.

## [2026-07-27] research | c1 (ex-conductorone)
User flagged c1.ai. VERIFIED: ConductorOne renamed to **C1** (announced 2026-04-06, "We Are C1" blog; new domain c1.ai; agentic-era repositioning). No ownership change — still independent, VC-backed ($79M Series B Oct 2025). Source cached: `raw/sources/2026-07-27--c1--rebrand-announcement.md`.

## [2026-07-27] decision | slug rename conductorone → c1
Per slug convention, `wiki/vendors/conductorone.md` → `wiki/vendors/c1.md` (git mv), `aka: [ConductorOne]`. Inbound links updated (microsoft-entra, okta, sailpoint, saviynt, veza, lumos, hydden, linx-security, identity-governance, data-access-governance, survey-blueprint); taxonomy notes + both CSV rows updated. Survey options render as "C1 (formerly ConductorOne)" — doubly important because an unrelated IT-services MSP (ConvergeOne) also brands as "C1" since 2023; disambiguation note added to the vendor page.

## [2026-07-27] research | proofpoint-dspm (ex-normalyze)
User flagged normalyze.ai redirect. VERIFIED: normalyze.ai 301-redirects to proofpoint.com/us/normalyze-is-now-proofpoint; product now sold as **Proofpoint Data Security Posture Management** (product page live). Resolves the page's open question — Normalyze brand retired. Source cached: `raw/sources/2026-07-27--proofpoint-dspm--normalyze-brand-retired.md`.

## [2026-07-27] decision | slug rename normalyze → proofpoint-dspm
Product-slugged (`proofpoint-dspm`), not `proofpoint`, per the product-as-shopping-unit convention (prisma-airs precedent): "Proofpoint" alone is ambiguous — Proofpoint also owns Acuvity and its core email/DLP franchise, and no company-level proofpoint page exists. `aka: [Normalyze]`; website → Proofpoint DSPM product URL; inbound links (rubrik, wiz, bedrock-security, symmetry-systems, teleskope, acuvity, dspm category, M&A map), taxonomy notes, and CSV row updated. Survey option renders "Proofpoint DSPM (formerly Normalyze)".

## [2026-07-27] decision | delete styra page — company wound down
`wiki/vendors/styra.md` **deleted** (git rm). Not a rename — a vendor-is-gone case. Styra
(creator of OPA, sold Styra DAS / Enterprise OPA) is no longer a going concern: Apple
acqui-hired its founding OPA maintainers (Teemu Koponen, Tim Hinrichs, Torin Sandall) plus
much of engineering (~2025-08), the commercial enterprise products were discontinued /
open-sourced (Cloud Native Now, osohq.com, TechCrunch-HN reporting), and **styra.com now
fails to resolve (DNS SERVFAIL, confirmed independently 2026-07-27)**. The page's soft
contradiction from 2026-06-28 ("acquired the developer of OPA" vs "acqui-hire only") is
thereby resolved in favor of *acqui-hire followed by wind-down*, and the page's open
question "corporate status of Styra Inc. post-Apple" is answered: wound down.

OPA itself is unaffected — still a CNCF Graduated project under unchanged governance — and
its content already lives at `wiki/vendors/open-policy-agent.md`. survey-v2.csv row 93 was
already renamed to "Open Policy Agent (OPA)" in a prior session with an explanatory note;
**confirmed still correct, no CSV change made**. `index.md` intentionally left stale — it is
regenerated once at the end of this cleanup batch.

**12 files repaired** (link removal, judged case-by-case rather than find-replace):
- Delinked + kept as historical plain text where Styra's history is load-bearing:
  `wiki/vendors/open-policy-agent.md` (created-at-Styra lineage, expanded to record the
  wind-down and the dead domain), `wiki/comparisons/ai-security-m-and-a-map.md` (M&A row
  retained — the acqui-hire happened — now pointing at open-policy-agent),
  `wiki/categories/authorization-engine.md` + `wiki/categories/policy-as-code.md` (M&A
  dynamics sections rewritten from "uncertain roadmap" to "wound down").
- Dropped entirely from competitor / alternatives / positioning lists, since a defunct
  company is not a live alternative: `oso.md`, `kyverno.md`, `hashicorp-sentinel.md`,
  `authzed.md`, `permit-io.md`, `cerbos.md`. Stale prose "standing up OPA+Styra yourself"
  → "standing up and operating OPA yourself" (permit-io, cerbos).
- Dropped as a **survey answer option** in both category pages, with a note explaining the
  removal so survey design keeps the context (a "Styra" write-in = legacy DAS, not net-new).
  Same stale option cleaned out of `wiki/comparisons/survey-blueprint.md` (Q11) and
  `wiki/categories/mcp-gateway.md` (overlap note) — plain-text mentions, no dangling links,
  but they named Styra as a live choice.
- Left deliberately: `taxonomy.yaml` / `taxonomy.md` / `taxonomy-gaps.md` historical record
  of the `OPA / Styra` → two-page split (a record of a past decision, not a live pointer),
  and `raw/` sources (immutable).

## [2026-07-27] decision | delete whylabs page — company discontinued operations
`wiki/vendors/whylabs.md` **deleted** (git rm). Second vendor-is-gone case in this cleanup
batch (after `styra`). Fresh fetch of https://whylabs.ai (2026-07-27) returns a shutdown
notice, not a product site: "WhyLabs, Inc. is discontinuing operations," with the full
WhyLabs platform, `whylogs`, and LangKit released to the community as open source. No
redirect, no acquirer landing page, no rebrand. There is no successor product to point a
reader at, so the page was removed rather than rewritten.

**Apple-attribution discrepancy — investigated and resolved as NOT an error.** The audit
task flagged a suspicion that this page's `owner: Apple` was a mix-up with the
Styra/OPA→Apple acqui-hire logged earlier today. It is not. The two are independent,
separately sourced events that happened to involve the same acquirer in the same year:
- Styra: Apple hired Teemu Koponen / Tim Hinrichs / Torin Sandall (OPA maintainers), ~2025-08.
- WhyLabs: GeekWire, "Founders at Seattle startup WhyLabs join Apple following an
  under-the-radar acquisition" (2025) names WhyLabs specifically; corroborated by Andrew
  Ng's AI Fund portfolio page ("acquired in 2025"), a Crunchbase acquisition record
  (`apple-acquires-whylabs`), an ex-AI-Fund GP's LinkedIn ("ACQ BY APPLE"), and European
  Commission DMA filings. Cached at
  `raw/sources/2026-06-28--whylabs--apple-acquisition.md`.

So the Apple acqui-hire claim stands at its original **medium** confidence (Apple never
officially confirms acquisitions), and the fresh "discontinuing operations / open-sourcing"
finding does **not** contradict it — it completes it. Same shape as Styra: team absorbed,
corporate shell wound down, code thrown over the wall. Note the shutdown page itself does
not mention Apple, which is expected of an acqui-hire wind-down notice and is not evidence
against the deal. No `Contradiction (hard)` flag warranted. The deleted page had already
recorded both halves of this story since 2026-06-28.

**5 files repaired** (inbound links, judged case-by-case):
- Dropped entirely from **Competitors / alternatives** lists — a company that has ceased
  operations is not a live alternative, and the trailing "(wound down)" hedges went with
  it: `wiki/vendors/fiddler-ai.md`, `wiki/vendors/arize-phoenix.md`,
  `wiki/vendors/arthur-ai.md`.
- `wiki/categories/llm-observability.md` — removed the vendor bullet from the
  enterprise-monitoring list; removed **WhyLabs as a survey answer option** and added a
  survey-design note so a write-in is read as legacy `whylogs`/LangKit usage rather than a
  live vendor relationship.
- `wiki/comparisons/ai-security-m-and-a-map.md` — M&A row **retained** but delinked to
  plain text (the acqui-hire did happen; it belongs in the historical record), with the
  wind-down and page removal noted inline. The prose line naming Apple's two
  open-source-adjacent acqui-hires (WhyLabs, Styra/OPA) is accurate as written and left
  alone.

`survey-v2.csv` checked — **no WhyLabs row exists** (this is exactly the orphan that lint
rule R1 has been reporting against `wiki/vendors/whylabs.md` since 2026-07-05; deleting the
page clears that finding). `index.md` intentionally left stale — regenerated once at the end
of this batch. `raw/sources/` left untouched (immutable), as are the seed files and
`proposed-*` snapshots that name WhyLabs as a point-in-time record.

## [2026-07-27] research | apex-security

**Trigger:** URL audit — `apexsec.com` no longer serves Apex content. Confirmed 2026-07-27:
both `https://apexsec.com` and `https://www.apexsec.com` return HTTP 404 (server: Kestrel);
the audit also observed a 302 to a HugeDomains "domain for sale" parking page ($15,595).
The domain has lapsed entirely — the Apex brand has no web presence left.

**Verified (primary sources, cached to
`raw/sources/2026-07-27--apex-security--tenable-close-and-ai-exposure.md`):**

- **Acquisition CLOSED — June 2025.** Tenable Holdings Form 10-Q for the quarter ended
  2025-06-30, Note 6: *"In June 2025, we acquired Apex Security, Inc. ... We acquired 100%
  of Apex's equity through a share purchase agreement for total consideration of $47.8
  million, including $47.7 million in cash, net of $2.0 million cash acquired, and $0.1
  million fair value of replacement equity."* Allocation: $6.8M intangibles (proprietary
  technology, 5-yr life), $41.3M goodwill. This resolves the standing open question
  ("confirm the deal closed") that had the page at `acquired-pending` with
  `verify_after: 2026-09-03`. The 10-Q gives **month precision only**; Tenable filed no
  close 8-K (immaterial at that size), so no day-level close date exists in any primary
  source — recorded as `2025-06` rather than guessed, per the never-invent rule.
- **Successor product + live URL.** Apex's technology now ships as **Tenable One AI
  Exposure**: private customer preview announced on the Tenable blog 2025-08-06 (agentless,
  built into Tenable One), **GA announced 2026-01-27** ("Tenable Extends Exposure Management
  to AI Attack Surface"). Live product page: **https://www.tenable.com/products/ai-exposure**.
  Neither the product page nor the GA release mentions Apex by name — the brand is fully
  absorbed, which also answers the second standing open question. GA platform coverage is
  narrower than acquisition-era messaging implied: OpenAI ChatGPT Enterprise + Microsoft
  Copilot / 365 Copilot / Studio Copilot, with Gemini "forthcoming."

**Decision — price contradiction resolved (soft).** The page had carried Calcalist's
reported **">$105M"** since 2026-06-28. Tenable's own SEC filing says **$47.8M** total
consideration. Resolved in favor of the 10-Q: it is authoritative for consideration
transferred, and the higher press figure most likely folded in retention/incentive packages,
which are compensation expense rather than purchase price under ASC 805. Both figures are
kept on the page with that explanation, flagged `Contradiction (soft, resolved)` — **not**
`Status: Unresolved`, so the commit gate is unaffected. Calcalist source entry downgraded to
`confidence: low` (superseded on price; still fine as a deal-happened corroborant).

**Changed — `wiki/vendors/apex-security.md`:** `website` → the Tenable AI Exposure product
page; `ownership_state` acquired-pending → **acquired-closed**; `acquisition` →
`{announced: 2025-05-29, closed: 2025-06, price: $47.8M}`; `ownership_note` rewritten;
`aka` += `Tenable One AI Exposure`, `Tenable AI Exposure`; `verify_after` → null;
`last_verified` → 2026-07-27; added frontmatter `sources:` entries for the close/price and
the rebrand. Body: header banner and one-liner now say closed-and-rebranded; "What it does"
gained a present-tense Tenable One AI Exposure paragraph incl. GA platform coverage;
deployment section notes agentless delivery and that no standalone Apex deployment remains;
positioning reframed — the differentiator post-integration is co-location in Tenable's
exposure graph, a consolidation play rather than depth against agent-security pure-plays;
CTO lens notes there is no Apex contract/pricing path and that adopting this means adopting
Tenable One; open questions replaced (exact close day, module pricing, non-Microsoft/OpenAI
coverage); Sources and History updated.

**Changed — `survey-v2.csv` row 65:** Vendor URL → `https://www.tenable.com/products/ai-exposure`;
product option → "Apex Security (Tenable One AI Exposure)"; Flag/Note extended (not replaced)
with closed date, corrected price, dead domain and new product name. Survey-design note: this
option should probably be *retired* in favor of a plain "Tenable One AI Exposure" answer in the
next survey revision — respondents will not recognize "Apex". Flagging, not acting.

`index.md` deliberately left stale — regenerated once at the end of this batch.

## [2026-07-27] research | acuvity

**Trigger:** URL audit — `acuvity.ai` issues a hard 301. Verified 2026-07-27:
`https://acuvity.ai` → `301 Moved Permanently`, `Location:
https://www.proofpoint.com/us/platform/ai-security`. That page is 100% Proofpoint-branded;
**neither "Acuvity" nor "RYNO" appears on it**, nor on any of the three product pages.
Unlike Normalyze, Proofpoint published **no lineage/transition page** —
`/us/acuvity-is-now-proofpoint` 404s.

**No new acquisition facts.** The frontmatter was already correct: acquired by Proofpoint,
announced-as-completed **2026-02-12** (PR past tense, no separate close date), **terms
undisclosed**. Confirmed against the same Proofpoint press release plus Thoma Bravo's
newsroom and BusinessWire. So `ownership_state: acquired-closed` stands; price stays null.
What changed is **brand status**: Acuvity is retired, and the capability now ships as three
Proofpoint SKUs — **AI Access Security** (AI app/agent discovery and inventory, runtime
observability, 18 built-in detectors, forensic audit trails, SIEM/SOAR routing),
**Agentic AI Security**, and **AI MCP Security** (MCP discovery + risk classification,
gateway-style inline enforcement, transaction forensics, an 800-plus trusted-MCP-server
registry).

**Changed — `wiki/vendors/acuvity.md`:** `website` → the Proofpoint AI Security platform page;
`aka` += `Proofpoint AI Security`; `mcp_support` unverified → **gateway** (the MCP SKU brokers
and inspects requests inline, not passive monitoring); `tags` += `thoma-bravo`;
`ownership_note` extended with the redirect/brand-retirement and SKU names; `last_verified` →
2026-07-27; added three frontmatter `sources:` entries. Body: header banner and one-liner now
say brand retired / shop it as Proofpoint AI Security; "What it does" gained a present-tense
SKU breakdown; new "Naming / provenance" section; deployment notes the MCP gateway;
positioning adds Proofpoint's "intent-aware" AI-security-plus-data-security pitch (labelled as
the platform's marketing claim, not an Acuvity differentiator); CTO lens tells buyers to ask
for SKU names because "Acuvity" is ~5 months dead as a purchasing term. **Two open questions
resolved** (does RYNO survive as a brand → no; MCP depth → gateway); remaining opens now
include SKU packaging/pricing.

**Decision — slug kept as `acuvity`, NOT renamed.** This deliberately breaks precedent with
`normalyze` → `proofpoint-dspm` (same acquirer, same batch). Reason: Normalyze became exactly
one shopping unit ("Proofpoint DSPM"), so a product slug was the unit buyers shop for. The
Acuvity technology was **split across three SKUs**, so no single product slug is faithful —
`proofpoint-ai-security` would name the platform, not the unit, and the three SKUs do not each
deserve a page yet. The acquired-company slug plus a `Naming / provenance` section is the
honest representation. Revisit if Proofpoint consolidates the three into one purchasable
product.

**Changed — `survey-v2.csv` row 128:** Vendor URL `https://acuvity.ai` →
`https://www.proofpoint.com/us/platform/ai-security`; product option "Acuvity (Proofpoint)" →
"Proofpoint AI Security (formerly Acuvity)"; Flag/Note extended with brand retirement, the
redirect and the three SKU names. Same survey-design caveat as the Apex/Tenable row:
respondents will not recognize "Acuvity", so the next survey revision should probably lead
with the Proofpoint name. Flagging, not acting.

**Source cached:** `raw/sources/2026-07-27--acuvity--brand-retired-proofpoint-ai-security.md`
(supersedes nothing — sits alongside `2026-07-13--acuvity--proofpoint-acquisition-pr.md`,
which remains the acquisition-facts anchor).

`index.md` deliberately left stale — regenerated once at the end of this batch.

---

## [2026-07-27] research | aim-security

**Trigger:** automated URL audit — `https://www.aim.security` returns **HTTP 301 →
`https://www.catonetworks.com/`**, a completely different company's SASE homepage with zero
Aim branding. Page frontmatter still said `ownership_state: acquired-pending`.

**Verified — the deal CLOSED, it was never really "pending".** Cato's 2025-09-03 press release
is written entirely in the past tense ("Cato Networks **Acquires** Aim Security"), contains no
"definitive agreement", no expected-close window and no regulatory condition, and told existing
Aim customers they could deploy "today" — that is a post-close integration plan. Same-day
independent coverage (SecurityWeek, CyberScoop, SiliconANGLE, Help Net Security, Network World)
all reported it as done. There is no separate completion announcement, which is normal for a
private cash-and-stock deal of this size. `acquired-pending` was an over-cautious read of the
original PR on 2026-06-28, not a signal of an actual pending close.

**Verified — brand fully retired and the technology is GA inside Cato.** Cato's 2026-03-17
press release ("first GPU-powered SASE platform with native AI Security") states Cato is
"launching **Cato AI Security**, converging advanced AI governance and protection capabilities
from its recent acquisition of Aim Security into the Cato SASE Platform", generally available
worldwide, running on **Cato Neural Edge** (NVIDIA GPUs deployed across Cato's private
backbone). The product hub `catonetworks.com/platform/ai-security-aisec/` carries **no Aim
branding whatsoever**. Aim's three legs survive functionally, renamed: AI Security for End
Users (shadow AI), AI Security for Applications (the AI Firewall), Agentic AI Security
(agent↔model↔MCP visibility), plus AI-SPM. This closes the long-standing open question on both
this page and `cato-networks.md`: "whether the Aim brand survives inside Cato" — it does not.

**Changed — `wiki/vendors/aim-security.md`:**
- `website` `https://www.aim.security` → `https://www.catonetworks.com/platform/ai-security-aisec/`
  (the Aim-lineage product hub, not the generic Cato homepage the redirect lands on — more
  specific and more useful to a buyer; same choice made for Acuvity/Proofpoint and
  Apex/Tenable in this batch).
- `ownership_state` `acquired-pending` → `acquired-closed`; `acquisition.closed` `null` →
  `2025-09-03`; `verify_after` `2026-09-03` → `null` (it existed only to satisfy the
  acquired-pending schema requirement).
- `aka` gained "Cato AI Security"; `tags` gained `cato`; `last_verified` → 2026-07-27;
  three `sources:` entries added; `ownership_note` rewritten.
- Body: One-liner and header banner now lead with brand-retired; Deployment section notes the
  integration is finished and names Cato Neural Edge; Positioning gained a post-acquisition
  paragraph mapping the old three legs onto the new SKU names and calling out that the
  differentiator is now a platform argument, not a best-of-breed one; CTO lens now says
  plainly you cannot buy Aim and that any shortlist still carrying the name is stale;
  History entry appended.

**Price left `null`.** Cato has still never disclosed terms. Press reports range ~$350M
(Calcalist) to $350–400M. Recorded in prose as reported-not-confirmed; not promoted into
`acquisition.price`.

**Changed — `survey-v2.csv` row 57:** Vendor URL `https://www.aim.security` →
`https://www.catonetworks.com/platform/ai-security-aisec/`; product option "Aim Security
(Cato)" → "Cato AI Security (formerly Aim Security)"; Flag/Note updated to closed-2025-09-03 +
brand retired + GA date. Row 20 (Cato Networks, SSE/SASE category) left alone — its note
"acquired Aim Security (2025)" is still accurate. **Survey-design note:** AI-SPM respondents
in 2026 will not recognize "Aim Security", and the same option now effectively duplicates the
Cato Networks row in the SASE category for anyone who buys the whole platform. Worth deciding
in the next survey revision whether the AI-SPM row should stay at all. Flagging, not acting.

**Not changed — `wiki/vendors/cato-networks.md`.** Its open question "whether the Aim
brand/standalone product persists" is now answerable and its `ownership_note` could gain the
close date, but Cato is a separate research item in this batch's queue; folding it in here
would have made this commit two vendors wide. Left for the cato-networks pass.

**Source cached:** `raw/sources/2026-07-27--aim-security--cato-ai-security-brand-retired.md`
(supersedes nothing; the 2025-09-03 acquisition PR remains the deal-facts anchor).

`index.md` deliberately left stale — regenerated once at the end of this batch.
