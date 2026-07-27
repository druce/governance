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

## [2026-07-27] research | astrix-security

**Cisco/Astrix deal CLOSED — `acquired-pending` → `acquired-closed`.** URL audit found
`https://astrix.security` still loading live under Astrix branding (title "Identity Security
for AI Agents & NHIs | Astrix Security") but banner-ing "Astrix Security is now part of
Cisco" plus "Astrix has ended standalone sales of new licenses effective June 30th, 2026."

**Close confirmed from a primary source.** Cisco's own 2026-05-04 "announces intent to
acquire" blog now carries a dated update note at the top: *"June 29, 2026 Update: We have
completed the acquisition of Astrix Security. Welcome to Cisco!"* No separate completion
press release was issued — the update banner on the announcement post is the completion
notice, which is normal for a private deal of this size. Cisco's corporate-development
acquisitions pages return HTTP 403 to automated fetches and could not corroborate directly.
→ `announced: 2026-05-04`, `closed: 2026-06-29`.

**Price stays `null`.** Cisco disclosed no terms in either the announcement or the update.
Calcalist/Ctech reports ~$400M (earlier talks reported at up to $350M). Per CLAUDE.md §7 the
unofficial figure is cited in prose and in the source cache, not promoted into frontmatter.

**`website` kept as `https://astrix.security`.** Checked whether the capability had landed in
a named Cisco SKU to repoint at — it has not. Cisco states Astrix will be integrated into
**Cisco Identity Intelligence** and extended across **Secure Access**, **Duo** and
**Splunk**, but as of 2026-07-27 nothing ships under a Cisco brand and no Cisco product page
mentions Astrix. Astrix's own domain remains the authoritative page. **This is a different
pattern from Aim/Cato and Normalyze/Proofpoint** (this batch's two prior closes), where the
acquired domain 301s and the brand is retired: here the brand and domain survive as a
transition landing page for existing customers. Worth watching — the domain may yet 301.

**Changed — `wiki/vendors/astrix-security.md`:** `ownership_state` acquired-pending →
acquired-closed; `acquisition.closed` null → 2026-06-29; `verify_after` 2026-09-03 → null (no
longer required once closed, SCHEMA.md §3.2); `last_verified` → 2026-07-27; `ownership_note`
rewritten; added a `sources:` frontmatter block (acquisition-close, standalone-sales-ended).
Body: header callout, deployment paragraph (integration announced-but-not-shipped),
positioning ("no longer a buying unit"), Ownership section rewritten with the close and the
sales-end, CTO lens rewritten into new-buyer / existing-customer / Cisco-shop guidance,
open questions re-cut, Sources and History updated.

**Soft contradiction resolved.** The 2026-06-28 flag (seed said flat "acquired", reality was
intent-announced/pending) is marked **Resolved 2026-07-27** — the seed was premature, not
wrong. Left the flag in place with the resolution rather than deleting it, so the correction
history stays legible.

**Changed — `survey-v2.csv` rows 56 and 148** (AI-SPM and Non-Human Identity categories):
Flag/Note "Acq. announced 2026-05-04 (~$400M) — pending, not closed" → closed-2026-06-29 +
standalone-sales-ended. Vendor URL left at `https://astrix.security` (still live and
authoritative). Product option left as "Astrix (Cisco)" — unlike the Aim→Cato case there is
no successor product name to rename to yet. **Survey-design note:** by fielding time these
two rows may be unbuyable-but-recognizable — respondents can legitimately answer "In
production" (existing customers) but never "Considering/evaluating" (can't buy it). If a
Cisco SKU name lands before fielding, rename both rows to it.

**Source cached:** `raw/sources/2026-07-27--astrix-security--cisco-deal-closed.md`.

**Follow-ups:** (1) re-check which named Cisco product absorbs Astrix and whether
`astrix.security` starts redirecting; (2) `wiki/vendors/cisco.md`, if it exists, may want the
close date — not touched here to keep this commit one vendor wide.

`index.md` deliberately left stale — regenerated once at the end of this batch.

## [2026-07-27] research | azure-dev-boxes

**Product sunset, not an ownership change.** URL audit found a transition banner on
`https://azure.microsoft.com/en-us/products/dev-box`, verbatim: *"Capabilities of Microsoft
Dev Box are transitioning to Windows 365. Existing customers can continue using Dev Box, but
new sign-ups will no longer be accepted as of November 1, 2025."* Confirmed against a second
Microsoft primary source — the Dev Box **roadmap** page on Microsoft Learn
(`/azure/dev-box/dev-box-windows-365-announcement`, `ms.date` 2026-05-01) has been replaced
in place by a maintenance-mode notice: *"Dev Box is now in maintenance mode, with no
additional features planned. Microsoft's investments for developer cloud environments are
focused on Windows 365."* Existing dev boxes, pools and configurations "remain fully
functional and supported." **No end-of-service date has been announced** — treat retirement
timing as unknown, not indefinite.

**It's a merge, not a rename — so "Windows 365" was NOT added to `aka`.** Windows 365
predates Dev Box (Dev Box was always built on the Windows 365 / Cloud PC platform), is still
sold, and has its own SKUs and admin surface (Intune / M365 admin center rather than the
Azure Dev Center resource model). Directions on Microsoft calls it "a capability merge rather
than a simple rename." Adding it as an alias would wrongly imply the Dev Box slug and the
Windows 365 slug denote the same buying unit.

**Successor capabilities identified** (Windows Developer Blog, Build 2026, 2026-06-02 —
primary). Two things, at deliberately different maturities: **Windows 365 with Developer
configuration** (*public preview*) is the direct replacement for a Dev Box pool image —
preconfigured Win11 with VS Code, Git, GitHub CLI, WSL from first sign-in; **Windows 365 for
Agents** (*GA*, within Agent 365) gives AI agents Intune-managed Cloud PCs isolated from the
user's own machine to run multi-step workflows. Worth flagging for this wiki's thesis: the
successor line ships a **separately-branded agent-containment SKU at GA while the developer
image is still preview** — Microsoft's investment is weighted toward the agent case, and Dev
Box never had an agent-specific offering at all.

**Licensing left at medium confidence.** Directions on Microsoft and Licensing Lore & Law
both report developer scenarios are enabled via **Windows 365 Frontline** at ~50% over
Windows 365 Enterprise, one license covering up to three Cloud PCs; the same analysts report
an onboarding-exception form for orgs that evaluated Dev Box before the cutoff. **Neither
Microsoft page states a required SKU**, so per CLAUDE.md §7 this stays analyst-reported in
prose and out of frontmatter.

**Cancelled-before-GA features noted as governance gaps.** The maintenance-mode page lists
seven killed features; two matter to a regulated buyer inheriting a Dev Box estate — firewall
**Service Tags** (egress rules) and automatic **developer offboarding** on leaver/transfer.
Those are egress-control and JML gaps that will never be filled in this product.

**Changed — `wiki/vendors/azure-dev-boxes.md`:** `last_verified` 2026-06-28 → 2026-07-27;
`verify_after` null → 2027-01-31 (re-check for an announced end-of-service date);
`ownership_note` extended with the sunset; tags += `maintenance-mode`,
`closed-to-new-customers`; added a 4-entry `sources:` block. `ownership_state` **unchanged**
at `public` — Microsoft owned it before and owns the successor. Note `maintenance-mode` *is*
a legal `ownership_state` enum value (SCHEMA.md §3.2), but selecting it would destroy the
ownership fact; followed the existing `wiki/vendors/helicone.md` precedent of recording
frozen status as a **tag** alongside a real ownership state. Body: added a closure callout
under the H1, a new "Product status & the Windows 365 transition" section, rewrote
Positioning, Ownership, CTO lens and Competitors, expanded open questions, Sources and
History.

**`market_position` left `null` deliberately.** None of the SCHEMA.md §3.3 labels (leader /
challenger / legacy-incumbent / platform-module / oss-default / niche-specialist /
ai-native-disruptor) honestly describes a product withdrawn from sale, and the rule requires
justifying the label in a sentence — which can't be done here without misleading. Stated as
such on the page rather than left as a silent null.

**CTO lens re-cut around buying-relevance**, which is the material change: a new evaluator
cannot buy this and should look at Windows 365 (budgeting for Frontline, expecting preview
quality on the developer image); an existing estate should schedule migration as Day-2 work
and get the end date from their account team; the underlying thesis — governed ephemeral
cloud workstations to keep dev and agent work off local endpoints — is unchanged, only the
SKU moved.

**`survey-v2.csv`: no change needed.** No Azure Dev Box row exists, and correctly so —
`ephemeral-environments` is `adoption_tier: practice` with `survey_question: null`, so per
CLAUDE.md §6 the category carries no survey scaffolding. GitHub Codespaces is likewise absent.
Nothing to flag.

**Source cached:**
`raw/sources/2026-07-27--azure-dev-boxes--windows-365-transition.md`.

**Follow-ups:** (1) **No `wiki/vendors/windows-365.md` exists** — Windows 365 is now the live
product in the ephemeral-environments slot and arguably warrants a page, especially Windows
365 for Agents, which is agent-containment infrastructure and relevant well beyond this
category; flagged for the human as a scope call rather than created unilaterally. (2) Re-check
2027-01-31 for an announced Dev Box end-of-service date. (3) Confirm the Frontline licensing
requirement with a Microsoft primary source if one ever publishes. (4)
`wiki/categories/ephemeral-environments.md` and `wiki/vendors/github-codespaces.md` both
reference Dev Box as a live option and may want the closure noted — not touched here to keep
this commit one vendor wide.

## [2026-07-27] research | amazon-q-business

**Internal product sunset, not M&A.** URL audit found an End of Support Notice on
`https://aws.amazon.com/q/business/`, verbatim: *"Amazon Q Business will no longer be open to
new customers starting on July 30, 2026. If you would like to use the service, please sign up
prior to July 30, 2026."* Confirmed against AWS's own docs — the **Amazon Q Business
availability change** page (`/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html`),
which also carries the full migration guide: *"Amazon Q Business remains fully supported and
AWS will continue to provide bug fixes and security updates for existing customers, however new
feature requests will no longer be considered."* That is maintenance mode. **No end-of-service
date has been announced** — retirement timing unknown, not indefinite.

> Contradiction (soft): AWS's product page says the closure starts **July 30, 2026**; AWS's
> docs banner says **July 31, 2026**. Both instruct sign-up *prior to July 30, 2026*. A one-day
> discrepancy inside AWS's own copy, immaterial to the guidance — recorded on the page and in
> the cached source so it isn't later mistaken for a transcription error. Not escalated.

**Amazon Quick is a capability merge, NOT a rename — so "Amazon Quick" was NOT added to `aka`.**
This was the judgment call the task hinged on, and the evidence is one-sided. AWS's own framing
sentence — *"Amazon Quick represents the next evolution of Amazon Q Business"* — is positioning
written for the Q Business reader. Quick is actually the **QuickSight** service lineage:
AWS announced on **2025-10-09** that QuickSight (BI product, GA since 2016) "evolves to Amazon
Quick Suite," bundling the existing BI engine with new generative features (Quick Research,
Flows, Automate, Index, Chat); by the **2026-04-28** "What's Next with AWS" event the name is
plain **"Amazon Quick"** — the "Suite" suffix has been dropped from AWS's 2026 copy. The
plumbing settles it: Quick setup asks for a Region for *"initial data storage capacity, called
SPICE"*; AWS's own migration script calls `boto3.client('quicksight')` and
`quicksight.update_folder_permissions` against `arn:aws:quicksight:…` principals; Quick sits in
the console under **Analytics**; and Q Business's non-IDC auth mode is literally named
`AWS_QUICKSIGHT_IDP`. So Quick's scope is materially wider than Q Business's (BI dashboards +
workflow automation + agentic research *alongside* enterprise-content Q&A). Adding it as an
alias would wrongly assert the two slugs denote the same buying unit. **Same call as
`azure-dev-boxes` → Windows 365**, decided on the same reasoning three commits earlier.

**The finding that actually matters for this wiki: the successor is weaker on entitlement.**
Q Business earns its `entitlement-aware-rag` tag because connectors crawl source ACLs and
retrieval is filtered per user. AWS's migration guide documents that several of those
properties do **not** survive the move — these are AWS's words, not analysis:
- **Non-IDC mode loses per-user entitlement outright**: *"all Amazon Quick users automatically
  receive access to connected Q Business indexes… you lose the per-user and per-group access
  distinctions that Q Business enforced at the index level."* Under IAM Identity Center it *is*
  preserved. **The IdP choice is therefore a security decision, not a convenience one** — a
  firm with Chinese-wall obligations should treat a non-IDC migration as a control failure.
- **Guardrails and Actions are "explicitly excluded from the BYOI capability"** — topic and
  global controls must be rebuilt, and guardrails configured in Q Business do not apply through
  BYOI.
- **The User Store has no equivalent**; user management drops to the knowledge-base level.
- **Document-level ACLs cover only S3, Confluence Cloud, SharePoint and Google Drive**, versus
  Q Business's broader connector-side ACL crawling. Elsewhere AWS's advice is to shard content
  into per-role knowledge bases and script permissions — manual work, not automatic.
- One genuine *improvement*: Quick's ingest default is stricter — it *"does not ingest documents
  that lack an associated ACL entry,"* where Q Business granted all users access to S3 prefixes
  absent from the ACL file. Migrators must give every document an explicit ACL entry first or
  silently lose content.

**Migration path** is BYOI (Bring Your Own Index) — non-destructive, runs in parallel, index and
Quick instance must share account+Region. Quotas: max **two** Q Business indexes per Region
(not increasable), and once selected an index **cannot be unselected**. Q Apps must be hand-
rebuilt as Quick Flows (forms unsupported). Connectors without native Quick equivalents are
bridged via **MCP**, which cannot back a knowledge base (actions only), has a fixed 60s timeout,
static tool lists and no step-up auth. Anonymous-access / API-integration customers get no
documented self-serve path — AWS tells them to contact Support.

**Frontmatter:** `last_verified` → 2026-07-27; `verify_after` 2027-01-31 to re-check for an
announced end-of-service date. `ownership_state` unchanged (`public`, AWS/Amazon.com) — this is
an internal sunset, not M&A; detail added to `ownership_note`, and `maintenance-mode` /
`closed-to-new-customers` tags added, following the `helicone` / `azure-dev-boxes` precedent of
tagging frozen status rather than overloading `ownership_state`.

**`market_position` left `null` deliberately**, same reasoning as `azure-dev-boxes`: no
SCHEMA.md §3.3 label honestly describes a product withdrawn from sale, and the rule requires
justifying the label in a sentence. Stated on the page rather than left a silent null.

**Body re-cut around buying-relevance.** Page now leads with a "Product status — closed to new
customers" block; adds an "Amazon Quick: what it actually is" section carrying the lineage
evidence, the BYOI path and the entitlement regressions; CTO lens split into *evaluating now*
(you can't buy it — look at Quick, budget for the Enterprise subscription since Professional
can't create knowledge bases or connectors) vs *existing estate* (Day-2, not a fire drill — no
end date — but insist on IDC and re-derive guardrails/ACL coverage). Four new open questions
added, the sharpest being **whether the no-training commitment carries over to Quick** — the
primary-sourced "does not use customer data… for improving underlying LLMs" language is a *Q
Business* doc and was NOT verified for Quick. That is the single most important thing for a
fund to confirm before migrating, and it is deliberately left unverified rather than assumed.

**`survey-v2.csv`:** row 6 (`Enterprise AI Assistant, Amazon Q Business`) **kept** — existing
deployments remain in production and must stay answerable — with a Flag/Note recording the
closure, the Quick successor, and that future rounds should rename the option to "Amazon Quick"
or list both during the migration window. **No `Amazon Quick` row added**: no `amazon-quick`
wiki page exists, and adding an unbacked row would break the CSV↔wiki bijection lint enforces.

**Source cached:** `raw/sources/2026-07-27--amazon-q-business--amazon-quick-transition.md`.

**Follow-ups:** (1) **No `wiki/vendors/amazon-quick.md` exists** — Quick is now the live product
in this slot and spans `enterprise-ai-assistant`, `entitlement-aware-rag` and BI/automation
territory this wiki doesn't currently cover; creating it would also unblock the survey option
rename. Flagged for the human as a scope call rather than created unilaterally. (2) Verify
Quick's no-training commitment and compliance attestations (does it inherit Q Business's HIPAA/
ISO 42001, or QuickSight's?). (3) Re-check 2027-01-31 for an announced Q Business end-of-service
date. (4) `wiki/categories/enterprise-ai-assistant.md` and
`wiki/categories/entitlement-aware-rag.md` both reference Q Business as a live option and will
want the closure noted — not touched here to keep this commit one vendor wide. (5) Unrelated but
noted while researching: **Amazon Q Developer** (the IDE coding assistant, a different product)
is separately being sunset in **2027** in favour of **Kiro** — worth a check for whether this
wiki lists it anywhere.

## [2026-07-27] research | bedrock-security
URL audit flagged `https://www.bedrock.security` 301-redirecting to `https://bedrockdata.ai/`,
raising the question of which name is current — the frontmatter said `name: Bedrock Security`
with `aka: [Bedrock Data]` (implying Bedrock Data was the *old* name), while the page body
already said "now operating as Bedrock Data." VERIFIED, direction was backwards in the
frontmatter: **Bedrock Security → Bedrock Data, announced 2025-08-05** (first-party newsroom
post + BusinessWire wire copy, "Bedrock Security Rebrands as Bedrock Data to Advance Data
Governance, Security and Management in the AI Era"). Brand change only — legal entity stays
**Bedrock Labs, Inc.** (d/b/a Bedrock Data), no ownership event. Same-entity confirmed on four
independent points: CEO/co-founder **Bruno Kurtic** (named CEO under the old brand
2024-07-23), same Menlo Park HQ, same patented Metadata Lake product, and the vendor rehosting
its Bedrock Security press archive on bedrockdata.ai — ruling out a coincidental domain squat.
Timeline reconciles: the 2025-11-19 $25M Series A release the page already cited was titled
"*Bedrock Data* Announces...", i.e. post-rebrand, which is why the body was right and the
frontmatter wrong. Also recorded a name-collision hazard: an **unrelated** "Bedrock Data" at
`bedrockdata.com` (.406 Ventures-backed SaaS data-integration vendor, product Fusion, active
at least 2016–2018) — different domain/product/investors, current status unverified.
Source cached: `raw/sources/2026-07-27--bedrock-security--rebrand-to-bedrock-data.md`.

## [2026-07-27] decision | bedrock-security naming direction corrected; slug rename deferred
Fixed the inverted `aka`: `title`/`name` → **Bedrock Data**, `aka: [Bedrock Security, Bedrock
Labs]`, `website` → `https://bedrockdata.ai/`, `ownership_note` gains the rename line,
`last_verified` → 2026-07-27. Body: new naming paragraph under Ownership, disambiguation
callout for the unrelated bedrockdata.com, 3 new sources, dated History line. Rippled into
`survey-v2.csv` (option "Bedrock Security" → "Bedrock Data (formerly Bedrock Security)",
vendor URL updated — same "formerly" convention as Optro/C1/Proofpoint DSPM), `dspm.md`
(vendor-list line + survey option), and `taxonomy.yaml` notes ("Bedrock" was ambiguous →
"Bedrock Data (ex-Bedrock Security)"); taxonomy.md regenerated.
**Slug rename deferred, not decided.** The `conductorone → c1` and `auditboard → optro`
precedents say the slug should follow the current company name (`bedrock-data`), but that
needs `git mv` + inbound-link updates across rubrik, wiz, symmetry-systems, teleskope,
proofpoint-dspm, collibra and the dspm category, plus the CSV Wiki URL. Left as
`bedrock-security` with an Open-questions flag on the page for the human to confirm —
all links remain valid meanwhile.

## [2026-07-27] research | calypsoai

URL audit flagged `calypsoai.com` as 301-redirecting to `https://www.f5.com/products/ai-guardrails`.
Verified: the redirect resolves 200 to a live **F5 AI Guardrails** page with **zero CalypsoAI
branding**. The existing `ownership_state: acquired-closed` / `owner: F5` was correct — but two
recorded facts were **wrong**, and the fix required a primary source rather than the press.

**Corrections (source: F5 Form 10-Q, FY2026 Q1, Note 4 Business Combinations, SEC):**

- **Close date `2025-10-08` → `2025-09-26`.** The 10-Q states verbatim: "On September 26, 2025,
  the Company closed on a transaction for the acquisition of CalypsoAI Corp." No primary source
  supports 2025-10-08. The bad date came from dating the F5 completion blog, which announces
  completion but carries **no close date** and was in fact published 2025-09-29.
- **Price `null` → `$145.2M cash`.** The 10-Q records $145.2M ($14.2M net tangible assets,
  $16.9M developed technology, $114.2M goodwill; total $145.207M, preliminary allocation). The
  widely-cited **~$180M** is the 2025-09-11 *announced* purchase consideration.

Treated as **soft / scope-mismatch**, not a hard contradiction (CLAUDE.md §8): the two price
figures measure different things — announced headline consideration vs. GAAP purchase price
allocated at close. Both are now stated on-page with their basis. F5 does **not** reconcile the
~$35M gap, so no explanation is asserted; logged as an open question instead of a guess. Also
noted from the filing: CalypsoAI's revenue and earnings were **not material** to F5 — a useful
scale check on the pure-play at exit.

**Resolved open question:** "Whether the CalypsoAI brand survives or is fully retired into F5
product naming" — **fully retired**, on both `calypsoai.md` and `f5.md`.

Edits: `calypsoai.md` — website → the F5 product page, `acquisition` filled, `ownership_note`
rewritten, `last_verified` → 2026-07-27, `brand-retired` tag added; body reframed as a
historical/absorbed entry (no standalone product, contract or price list; evaluate F5 AI
Guardrails instead), current F5 capability list added, inline correction note, 2 new sources,
dated History line. Rippled the same corrections into `f5.md` (frontmatter note, M&A paragraph,
sources, History, open questions) and `wiki/comparisons/ai-security-m-and-a-map.md` (F5 table
row), plus `survey-v2.csv` (vendor URL + flag-note). Source cached to
`raw/sources/2026-07-27--calypsoai--f5-10q-close-date-and-price.md`.

**Worth generalizing:** the 2025-10-08 error came from treating a completion blog post's
publication date as the close date. Where a deal's close date traces only to a vendor blog,
check the acquirer's 10-Q/10-K — public acquirers state the exact closing date and the actual
consideration, and both can differ from the announcement.

## [2026-07-27] research | conjur

URL audit flagged `conjur.org` as 301-redirecting to
`https://www.paloaltonetworks.com/idira/machine/secrets-management` — a live Palo Alto
Networks page with **zero Conjur or CyberArk branding**. Verified the redirect by curl and
confirmed the cause.

**Second-order acquisition.** Conjur Inc. → CyberArk (May 2017, ~$42M) → CyberArk → Palo
Alto Networks (announced 2025-07-30, closed 2026-02-11, ~$25B). In **May 2026** PANW
rebranded the acquired CyberArk portfolio as **Idira**, and the secrets line landed in
Idira's *Machine Identity* pillar as **Secrets Manager** (SaaS or self-hosted). Two renames
stack here: CyberArk had already gone Conjur Cloud → "Secrets Manager, SaaS" and Conjur
Enterprise → "Secrets Manager, Self-Hosted"; Idira just carried that name forward. The
**commercial Conjur brand is retired**; the name survives only as the open-source project
and in SDK repo names (`conjur-api-go` is documented as the "Go client for the CyberArk
Secrets Manager API").

Changes to `wiki/vendors/conjur.md`: `website` → the Idira Secrets Manager page; `owner`
**CyberArk → Palo Alto Networks**; `acquisition.announced` **2026-02-11 → 2025-07-30**
(the close date had been wrongly duplicated into the announce field); `ownership_note`
rewritten to spell out the two-step chain; `aka` += `Idira Secrets Manager`,
`Palo Alto Networks Secrets Manager`; tags += `idira`, `renamed`; `last_verified` →
2026-07-27. Body: re-verified header banner, rewritten one-liner / what-it-does / M&A /
CTO-lens paragraphs, new **Open source status** section, 4 new sources, dated History line.
Brand-survival open question **resolved**. `survey-v2.csv` row 203 vendor URL + flag note
updated. Source cached to
`raw/sources/2026-07-27--conjur--panw-idira-secrets-management.md`.

**Conjur Open Source is a genuinely open question, not a resolved one.**
`github.com/cyberark/conjur` is still public, unarchived, and LGPL v3.0 — but its README now
carries a "Migrating to CyberArk Secrets Manager, Self-Hosted" section, and the marketing
domain that fronted the project is gone. No PANW statement addresses the OSS roadmap. Left
flagged as absence-of-evidence rather than inferring a sunset.

**Ordering note:** `cyberark.md` had **not** been processed when this ran (still
`last_verified: 2026-06-28`, no Idira mention), so this page led rather than followed. Facts
used here were taken from the existing `cyberark.md` frontmatter (owner `Palo Alto Networks`,
announced 2025-07-30, closed 2026-02-11) plus fresh research on the Idira rebrand — the
cyberark task should reuse the cached source above and stay consistent with the naming and
dates recorded here. `palo-alto-networks.md` and the M&A map may also need the Idira brand
noted; not touched in this pass.

**Minor, deferred:** the CSV answer option is still labelled `Conjur (CyberArk)`. Under the
"X (Acquirer)" convention (logged 2026-07-27) the acquirer is now Palo Alto, but "Conjur
(CyberArk)" is still the more *recognizable* string for survey respondents and the
convention explicitly optimizes recognition over deal-status precision. Left as-is; the flag
column now carries the Idira/PANW status. Revisit if the cyberark pass renames its own row.

**Worth generalizing:** a redirect audit that lands on an unfamiliar brand may be reporting a
*second-order* acquisition — the vendor's acquirer got acquired. Two rename events can stack
(product rename under acquirer #1, then platform rebrand under acquirer #2), so reconstruct
the full chain before assuming the redirect target is the direct buyer.

## [2026-07-27] research | cyberark

Companion to the `conjur` entry above — same deal, opposite end of the chain. Conjur is the
product two acquisitions deep; **this is the parent**. URL audit found `cyberark.com` **still
live and unredirected (HTTP 200)** — unlike `conjur.org`, which 301s — but now leading with
the banner *"Palo Alto Networks Completes Acquisition of CyberArk to Secure the AI Era"* and
the headline *"CyberArk is now Idira,"* linking to `paloaltonetworks.com/idira`.

**Went to primary SEC filings rather than press coverage**, per the cost-verification lesson
from earlier in this sweep. Two findings, one confirming and one correcting:

**Close date CONFIRMED exactly — 2026-02-11.** PANW Form 8-K (event date 2026-02-11, accession
0001193125-26-045600) defines the term in Item 1.01: *"on February 11, 2026 (the 'Closing
Date')"*, and Item 8.01 states PANW *"completed the acquisition of CyberArk pursuant to the
Agreement and Plan of Merger, dated as of July 30, 2025."* Corroborated by CyberArk's own
same-day Form 25-NSE (Nasdaq delisting), POSASR and 15× S-8 POS, plus Form 15-12G
deregistration on 2026-02-23. **No drift between the blog "completion" date and the legal
close** — this time the press release and the filing agree, which is itself worth knowing
after the earlier task where they didn't. Also learned: reverse-triangle merger via Israeli
Merger Sub "Athens Strategies Ltd."; **CyberArk Software Ltd. was not dissolved** and survives
as a wholly owned PANW subsidiary, which matters for who you actually contract with.

**Price CORRECTED — this is the discrepancy vs. the conjur entry.** Both `cyberark.md` and
`conjur.md` carried "~$25B," which is the *announced equity value* from 2025-07-30. PANW's Q3
FY2026 10-Q (period 2026-04-30, filed 2026-06-03), Note 7, gives the **final purchase
consideration as $21.1 billion** — $2,308M cash + $18,488M in 112M PANW shares + $265M
replacement equity awards = $21,061M. Not a contradiction, a **measurement-date difference**:
~88% of consideration was PANW stock at a *fixed* 2.2005 exchange ratio, so the six-and-a-half
months from signing to close repriced it. Recorded `acquisition.price` as
`$21.1B final consideration (announced as ~$25B equity value)` — both numbers, each labelled.
Left `conjur.md` alone; ~$25B is defensible there as the announced figure and the precise
consideration isn't load-bearing for a product page two levels down.

**Bonus signal from purchase accounting:** PANW assigned the acquired **trade name a 1-year
useful life** (vs. $3.5B of "platform renewals" at 12–14 years). PANW was amortizing the
CyberArk brand to zero before it publicly announced retiring it — the rebrand three months
after close was clearly planned at signing. Purchase price allocation also shows $14.8B
goodwill, $6.3B intangibles, and a $59M post-close workforce optimization plan running through
FY2027.

**Idira is real, not marketing.** It appears as **Idira™** in PANW's own 10-Q business
description under a new "Identity Security" segment heading, with five modules: Workforce
Identity Security; IT and Developer Identity Security (Modern PAM); Machine Identity Security;
IGA; AI Agents Security. Rebrand announced **2026-05-12** per PANW investor relations — this
**settles the 2026-05-12 vs 2026-05-13 ambiguity the conjur source file flagged**: 05-12 is
the PANW release date, 05-13 is SDxCentral's story date.

**`ownership_state: acquired-closed` verified correct and not a false positive.** The task
flagged a risk of confusing CyberArk-as-acquirer with CyberArk-as-target — real risk, since
CyberArk bought Conjur, Idaptive, Venafi and Zilla Security. It is genuinely the target here;
the page now separates the two explicitly in the M&A section so a future reader doesn't
re-litigate it.

Changes to `wiki/vendors/cyberark.md`: `website` → the Idira platform page (`cyberark.com` is
live but transitional and signposting its own replacement); `aka` += `Idira`,
`Palo Alto Networks Idira`, `CyberArk Software Ltd.`; `ownership_note` rewritten with both
price figures and the entity-survival fact; `acquisition.price` set; tags += `agentic-identity`,
`palo-alto`, `idira`, `renamed`; `last_verified` → 2026-07-27; structured `sources:` block added
(3 entries). Body: new **Idira product-map table** (module → legacy SKU), rewritten
positioning, expanded M&A, five-point CTO checklist, 5 new sources, dated History line.
Source cached to `raw/sources/2026-07-27--cyberark--panw-close-sec-filings-and-idira.md`.

**Positioning rewritten, not just annotated.** The old page called CyberArk the "PAM gold
standard" and left the framing intact. "Independent PAM leader" is now simply false — it is one
pillar of a four-pillar PANW platform. The page argues both directions (consolidation leverage
and a genuine ZSP capability gain at no extra cost, vs. loss of a best-of-breed vendor and new
concentration risk), and flags **vendor concentration as the live buyer question** for any fund
already running PAN-OS/Cortex. That's a risk-committee item, not a technical one, and it's the
thing most likely to surprise someone.

**Conjur open question resolved from this end too:** "does Conjur stay separately marketed"
— no, it's Idira Secrets Manager.

**`survey-v2.csv`, 3 rows (116, 147, 194) — renamed, diverging from the conjur decision.**
Option label `CyberArk (Palo Alto)` → **`CyberArk / Idira (Palo Alto)`**; vendor URL → the
Idira page; flag notes now carry the 2026-05-12 rebrand date. Reasoning: the recognition-over-
precision convention (logged 2026-07-27) says keep the string respondents know — but here
*both* strings are recognizable. The vendor's own homepage says "CyberArk is now Idira," and a
respondent whose console has already flipped may not connect a bare "CyberArk" to what they're
running. Leading with CyberArk preserves recognition; appending Idira catches the other half.
This does **not** overturn the conjur row staying `Conjur (CyberArk)` — that case is different
in kind: Conjur's replacement name is the generic "Secrets Manager," which is unrecognizable
standing alone and would collide with every other secrets product in the option list. Rename
where the new brand is distinctive; don't where it's generic.

**Method note worth keeping:** for any acquisition where consideration is substantially
*stock* at a fixed exchange ratio, the announced headline value and the final GAAP
consideration will differ by however the acquirer's share price moved between signing and
close — and the gap grows with the time to close (here, ~6.5 months and ~$4B, ~16%). The
acquirer's first post-close 10-Q, Note "Acquisitions," is the authoritative number. Press
coverage almost always keeps repeating the announced figure. Applies to several other
still-pending items in this sweep; record both figures rather than picking one.

## [2026-07-27] research | entro-security

URL audit found `entro.security` **still live under the Entro brand** — HTTP 200, no redirect,
`<title>` "Agentic AI & Non-Human Identity Security Platform | Entro Security" — but with a
footer reading **"© 2026 SailPoint Technologies, Inc."**. Task was to confirm the existing
`ownership_state: acquired-closed` / `owner: SailPoint` was accurate rather than stale from
some earlier status.

**Ownership CONFIRMED, correctly attributed.** SailPoint completed the acquisition **2026-06-29**
per SailPoint's own release ("today announced it has completed its acquisition of Tel Aviv-based
Entro Security", datelined June 29, 2026 09:00 ET). No change needed to `ownership_state` or
`owner`.

**Announce date CORRECTED: 2026-06-18 → 2026-06-15.** The 06-18 came from the 2026-07-09 pass and
was in fact the **publication date of the SecurityWeek write-up**, which never states when the
announcement happened — it only says "SailPoint has announced an agreement to acquire Entro."
SailPoint's own intent-to-acquire release is datelined **"AUSTIN, Texas, June 15, 2026 (GLOBE
NEWSWIRE)"**, the newswire URL path is `/news-release/2026/06/15/3311837/`, and SailPoint's IR
listing dates it June 15. Three-way consistent, high confidence. *Lesson, same shape as the
CyberArk/PANW one above but a different failure mode: there the risk was blog-vs-filing date
drift; here it was **trade-press publication date silently substituted for the announce date**.
When a page records an announce date, check that the cited source actually asserts it rather than
merely being dated that day.*

**SEC check per the prefer-filings rule — nothing to find, and that is the finding.** SailPoint,
Inc. is **CIK 0002030781** (the pre-re-IPO "Sailpoint Technologies Holdings, Inc." is CIK
0001627857 — do not use). EDGAR full-text search for "Entro" restricted to that CIK returns **0
hits** as of today; a control query returns hits, so FTS is working. Filing history explains it:
the last 10-Q was **filed 2026-06-10 for the quarter ended 2026-04-30**, i.e. *before* the 06-15
announcement, and **no 8-K was filed for the deal** — consistent with undisclosed terms and an
acquisition immaterial at PANW/CyberArk scale. So unlike the CyberArk task, there is no filing to
adjudicate the dates; the acquirer press releases remain the best primary source. First filing
expected to carry a business-combination footnote (and possibly an official price) is the **Q2
FY2027 10-Q, period ending 2026-07-31, due ~Sept 2026**. Set `verify_after: 2026-10-01`.

**Price unchanged and still soft:** officially undisclosed ("Financial terms of this transaction
were not disclosed"); **~$200M reported by Calcalist** only, medium confidence, single press
source.

Incidental: the intent PR guided the close to **Q3 FY2027**, but it closed 2026-06-29 = **Q2
FY2027** (SailPoint FY ends Jan 31) — closed ahead of guidance, not late. Worth noting because a
"closed earlier than guided" gap can otherwise look like a data error.

**Brand PERSISTS — surviving sub-brand, not a retired one.** entro.security serves 200 with no
redirect, keeps the Entro-branded title, carries a co-branded **SailPoint | Entro** lockup
(`SailPoint-Entro.png`), and only the corporate plumbing has moved (copyright + privacy policy now
SailPoint's). Matches the close PR: Entro's NHI/credentials products are "available now to
SailPoint customers as **standalone offerings** ... as native platform integration continues."
This is the **opposite** of the absorb-and-retire outcome recorded for Normalyze earlier in this
sweep (normalyze.ai 301s; product sold only as Proofpoint DSPM). Consequence for the wiki:
`website` **stays** `https://entro.security` and, per the "rename only if the new brand is
distinctive" rule, the survey row **keeps the Entro Security name** — no rename, just an ownership
note. Explicitly flagged in the CSV not to fold it into the SailPoint row, since buyers still shop
"Entro" as its own line item.

Updated `wiki/vendors/entro-security.md` (announce date, ownership_note, last_verified 2026-07-27,
verify_after, brand-persistence + SEC-status bullets, 3 new source entries, history line) and the
`survey-v2.csv` flag note. Cached
`raw/sources/2026-07-27--entro-security--sailpoint-announce-date-correction.md`.

## [2026-07-27] research | forgerock

**Confirmation-only pass — no factual change.** URL audit flagged that the `website` on file,
www.pingidentity.com, loads live with pure Ping Identity branding (PingOne, PingOne Advanced
Identity Cloud, Helix AI) and zero ForgeRock branding. That is old news, and the page already
documented it: `ownership_state: acquired-closed`, `owner: Thoma Bravo`, acquisition announced
2022-10-11 / closed 2023-08-23, `website` already pointed at pingidentity.com, and the body already
described the fold-in to Ping. A prior researcher (2026-06-28) had handled the merger correctly.

Only edits: bumped `last_verified` 2026-06-28 → 2026-07-27, and added the current SaaS product name
**PingOne Advanced Identity Cloud** (the successor to ForgeRock Identity Cloud) to the Deployment &
architecture section, since the page named only the retired ForgeRock brand. No re-research, no new
sources cached, no ownership fields touched.

`survey-v2.csv` checked: there is no ForgeRock row, by design — the brand is folded into the
**Ping Identity** row (`General Identity,Ping Identity,Thoma Bravo (incl. ForgeRock)`), which
already carries the ForgeRock lineage in its ownership note. Consistent; no CSV change.

## [2026-07-27] research | helicone

**URL audit question resolved: "Helicone Joins Mintlify" is a closed acquisition, not a
partnership.** The audit found helicone.ai live (200, no redirect) with a prominent
"🎉 Helicone Joins Mintlify 🚀" banner, and asked whether the soft "Joins" language covered an
acquisition, a merger, an acqui-hire, or a commercial partnership. Both counterparties'
announcement posts (2026-03-03) are unambiguous: Helicone wrote "Helicone **has been acquired**
by Mintlify, and our team will be joining them in San Francisco" — completed past tense on
announcement day — and Mintlify wrote "Mintlify **is acquiring** Helicone" plus "Mintlify has
acquired @helicone_ai" on X. Not a merger (Helicone is absorbed; Mintlify is the sole surviving
brand and entity) and not a partnership (no commercial-agreement framing anywhere). It is a real
company acquisition with strong **acqui-hire / technology-absorption** character: founders Justin
Torre and Cole Gottdank moved to Mintlify, the tech is being folded into Mintlify's assistant/
agent/workflow products, and the standalone product was frozen rather than invested in.

Moved `ownership_state` **acquired-pending → acquired-closed**. No separate closing date was ever
disclosed by either party, so `acquisition.closed` is set to the announcement date **2026-03-03**
as the effective date, justified by the target's completed past-tense language plus five months of
subsequent Mintlify operational control (roadmap decisions, customer migrations). That single
field is recorded at **medium** confidence; the deal itself is high. Terms undisclosed
(`price: null`, per the dominant CSV/frontmatter convention for undisclosed).

**Brand decision: no rename.** Applying this sweep's rule — rename only if the new brand is
distinctive and the old brand is retiring — Helicone fails both halves. `helicone.ai` is live,
200, no redirect to mintlify.com, still self-describes as "AI Gateway & LLM Observability", and
still sells (free trial, pricing page). The Helicone brand persists as an operating legacy brand
under Mintlify. `website` left at https://www.helicone.ai.

Also added a body section on what the deal means for the product, since that is the part a buyer
actually needs: Helicone's capabilities survive **inside Mintlify's** docs/AI-knowledge platform,
not as a standalone line; the standalone product stays in maintenance mode (security updates, bug
fixes, new-model support only); Mintlify has committed to "work closely with every customer to
support a smooth migration to another platform" — i.e. the vendor is steering its own customers
off; and **no sunset or shutdown date has been announced** as of 2026-07-27. Flagged the mismatch
that helicone.ai's homepage still reads promotional with no maintenance-mode notice — the frozen
status is disclosed only in the linked post. Softened the CTO lens accordingly: no fire drill for
existing users, but plan the exit rather than waiting for a sunset notice.

Updated `wiki/vendors/helicone.md` (ownership_state, acquisition.closed, ownership_note,
last_verified 2026-07-27, verify_after 2026-10-27, new deal-consequence section, third open
question, three source entries, history line). Cached
`raw/sources/2026-07-27--helicone--mintlify-acquisition-closed.md`.

`survey-v2.csv` checked: **no Helicone row exists** (zero matches, case-insensitive), so there was
nothing to renote — no CSV change. Crunchbase and Dealroom acquisition entries both 403 to direct
fetch; used as title-level corroboration only, not cited as primary evidence.

## [2026-07-27] research | lakera

**Check Point / Lakera is closed, and both the close date and the price came from the acquirer's
own SEC filings rather than press.** The URL audit flagged an ambiguous signal: `lakera.ai` loads
200 with no redirect and the unchanged title "Lakera: The AI-Native Security Platform to
Accelerate GenAI" — i.e. it still presents as an independent vendor — but the footer reads
"©1994-2026 Check Point Software Technologies Ltd." 1994 is Check Point's founding year, three
decades before Lakera existed, so that copyright line is a parent company's boilerplate on a
property it owns. Ownership changed; the marketing site did not.

Check Point is a foreign private issuer (NASDAQ: CHKP), so it files 6-K/20-F rather than 8-K/10-Q.
EDGAR full-text search returned seven Lakera-mentioning filings. The **FY2025 Form 20-F** (filed
2026-03-31), Note 3: Acquisitions, item (f), is definitive:

> "On **October 22, 2025**, the Company **completed the acquisition** of all outstanding shares of
> **Lakera AI AG** ('Lakera'), a privately-held Swiss company. … The Company acquired Lakera for
> **total consideration of approximately $201.8** [million]."

The filing's XBRL contexts corroborate (`chkp:LakeraAiAgMember` acquisition-date context tagged
`2025-10-01 – 2025-10-22`). Moved `ownership_state` **acquired-pending → acquired-closed**,
`acquisition.closed` null → **2025-10-22**, `verify_after` cleared. Sign-to-close was 36 days
against a press-release estimate of "Q4 2025."

**Price correction, and a discrepancy worth recording.** The page carried "~$300M reported"
(Calcalist, repeated widely). The audited figure is **$201.8M total consideration** — roughly
$100M lower. Logged as a **soft / scope-mismatch** contradiction, not a hard one: accounting
"total consideration" excludes amounts expensed as post-close compensation, and retention/earn-out
packages routinely inflate the number journalists are briefed on. But **no primary source itemizes
the gap**, so the page says so explicitly rather than asserting retention. $201.8M is now the
authoritative price in frontmatter; the ~$300M press figure is retained in the sources list at
lowered confidence specifically to document the discrepancy.

**The purchase price allocation turned out to be the most decision-relevant thing in the filing.**
Goodwill $150.1M (74% of price, "primarily attributed to synergies"); core technology $44.0M over
**7 years**; customer relationships $4.4M over **1 year**; trademark $0.3M over **1 year**. Check
Point's own accounting assumption is that the Lakera *brand* and the acquired *standalone customer
base* have about a year of remaining economic value from October 2025, while the *engine* has
seven. That is the fingerprint of absorb-the-product/retire-the-identity. Recorded the useful lives
as filing facts and labeled the intent reading as our inference.

**Brand decision: no rename**, per this sweep's rule (rename only when the old brand is retiring
*and* the new brand is distinctive). Lakera fails the first half today — live site, own name, own
marketing, still sold. `website` stays `https://www.lakera.ai`, slug stays `lakera`, survey option
stays "Lakera (Check Point)". Added an explicit open question and a note that the 1-year trademark
life means this specific decision should be revisited inside a year.

Also rewrote the framing, since "acquired" changes what this vendor *is* to a buyer. Positioning
previously read as best-of-breed pure-play; it now groups Lakera with the 2025 platform-absorption
wave — [prisma-airs](wiki/vendors/prisma-airs.md) (Palo Alto), [cisco-ai-defense](wiki/vendors/cisco-ai-defense.md),
[calypsoai](wiki/vendors/calypsoai.md) (F5), [aim-security](wiki/vendors/aim-security.md) (Cato),
[prompt-security](wiki/vendors/prompt-security.md) (SentinelOne) — and notes that the technical
differentiation survives the deal while the *neutrality* argument does not. Checked each
"independent alternative" against its own page before listing it, which caught prompt-security
(SentinelOne-owned, so moved to the absorbed list); witnessai, enkrypt-ai, mindgard and hiddenlayer
remain `independent`. CTO lens reworked around the commercial consequences: you now contract with
Check Point; ask for standalone-availability and renewal protection in writing given the 1-year
trademark life; but counterparty risk arguably *fell* — a $201.8M cash purchase with a 7-year
technology life and a Center-of-Excellence mandate is an investment case, not an acqui-hire.

Updated `wiki/vendors/lakera.md` (ownership_state, acquisition close + price, ownership_note,
last_verified 2026-07-27, verify_after cleared, tags +check-point, new frontmatter `sources:`
entries, new Brand-status section, rewritten Positioning / Ownership / CTO-lens / open-questions,
three new body sources, history line). Cached
`raw/sources/2026-07-27--lakera--checkpoint-20f-close-date-and-price.md`.

`survey-v2.csv`: **two** Lakera rows (AI Runtime Security line 45, AI Red Teaming line 160), both
carrying "close exp. Q4 2025 — verify" / "verify close". Both flag-notes updated to the closed date
and filed price; product names left as "Lakera (Check Point)" and both vendor URLs left at
lakera.ai, consistent with the no-rename decision.

## [2026-07-27] research | layerx

URL-audit follow-up. layerxsecurity.com came back live (200, no redirect) carrying the banner
"Akamai acquires LayerX, delivering end-to-end security and real-time AI usage control", while the
page still said `ownership_state: acquired-pending` with "close expected Q3 2026".

**Deal is closed.** Akamai's own completion press release (2026-07-02, dateline "CAMBRIDGE, Mass.,
July 02, 2026"): "announced the completion of its acquisition of LayerX... The deal, valued at
approximately US$205 million, was initially announced on May 14." So announced 2026-05-14, closed
**2026-07-02** — Q3 2026 guidance met on the first business days of the quarter.

**Price caveat, per this sweep's public-company rule.** Akamai is NASDAQ: AKAM, so I went to EDGAR
for an audited figure and there isn't one yet. Checked the submissions index directly: **no 8-K**
was filed for the completion (Akamai's May 8-Ks are credit-agreement/notes-offering and
annual-meeting items — a ~$205M deal is below its significant-acquisition threshold, so Item 2.01
never triggered), and the last 10-Q on file is Q1 2026 (period ended 2026-03-31, filed 2026-05-08),
i.e. *before* the deal was announced. The Q2 2026 10-Q was not yet filed on 2026-07-27, and since
the close landed two days after the 2026-06-30 quarter-end it could only appear there as a
subsequent event anyway. The audited purchase-price allocation should first show up in the **Q3
2026 10-Q, ~Nov 2026**. Recorded ~US$205M as acquirer-stated and unaudited, in both the
`acquisition:` price field and the body, and set `verify_after: 2026-11-30` to go get the real
number — the same PPA check that has already corrected press-reported prices for
[calypsoai](wiki/vendors/calypsoai.md) and [lakera](wiki/vendors/lakera.md) in this sweep.

**Brand decision: no rename — but this one is genuinely borderline**, unlike the other holds this
sweep. The split: layerxsecurity.com is live, unredirected and still fully LayerX-branded ("LayerX
Interaction Security Platform"), which fails the "old brand is retiring" half of the rule; but on
akamai.com the product page is *already* titled **"Akamai Workforce Protector (Formerly LayerX)"**,
with a Gartner Peer Insights listing under the new name. That is further along than e.g. Lakera,
where Check Point picked no successor name at all. So the acquirer has chosen and shipped a
replacement — the old brand is retiring, just not yet on its own domain. Held at slug `layerx`,
`website: https://layerxsecurity.com`, survey option "LayerX (Akamai)" for now, added
"Akamai Workforce Protector" to `aka`, and logged an explicit open question to move the slug when
layerxsecurity.com starts redirecting. Expect to revisit this well inside a year.

Rewrote the framing since it is no longer independent: added a "Brand status" section documenting
the two-sided transition; positioning now groups LayerX with the platform-absorption wave —
[prisma-airs](wiki/vendors/prisma-airs.md) (Palo Alto), [cisco-ai-defense](wiki/vendors/cisco-ai-defense.md),
[calypsoai](wiki/vendors/calypsoai.md) (F5), [aim-security](wiki/vendors/aim-security.md) (Cato),
[lakera](wiki/vendors/lakera.md) (Check Point), [prompt-security](wiki/vendors/prompt-security.md)
(SentinelOne) — and notes that the extension-based technical differentiation survives while the
neutrality argument does not. Checked each competitor against its own page: island, menlo-security
and grip-security are all still `independent` (now a differentiator worth naming),
chrome-enterprise is Alphabet-owned, so that comparison is Akamai's stack vs Google's. CTO lens
reworked around commercial consequences: quote under the new product name, ask in writing whether
it is still sold standalone or only bundled with Zero Trust/ZTNA, counterparty risk arguably *fell*
(profitable public acquirer vs a $10M-ARR startup), and diligence artifacts (SOC 2, DPA,
sub-processor list) need re-requesting under Akamai's entity.

Updated `wiki/vendors/layerx.md` (ownership_state → acquired-closed, acquisition closed date +
price, rewritten ownership_note, aka, tags +acquired/+akamai, last_verified 2026-07-27,
verify_after 2026-11-30, four new frontmatter `sources:` entries, new lede, new Brand-status
section, rewritten Positioning / Ownership / CTO-lens / open questions, four new body sources,
history line). Cached `raw/sources/2026-07-27--layerx--akamai-close-2026-07-02.md`.

`survey-v2.csv`: one LayerX row (Enterprise Browser Security, line 133). Flag-note updated from
"announced 2026-05-14" to the closed date, price caveat and the Akamai Workforce Protector name;
product name left "LayerX (Akamai)" and vendor URL left at layerxsecurity.com per the no-rename
decision above.

## [2026-07-27] research | natoma
Re-verified the Snowflake deal against primary sources after a URL audit found natoma.ai
live (200, no redirect) with a banner reading "Natoma is joining forces with Snowflake" and
a blog post still using "has signed a definitive agreement to acquire" — announcement, not
completion, language two months after signing.

Primary evidence: Snowflake Inc. Form 10-Q for the quarter ended 2026-04-30 (filed
2026-05-29, accession 0001640147-26-000030), Note "Subsequent Events — Business
Combinations": definitive agreement signed **2026-05-24** to acquire all outstanding capital
stock of **Natoma Labs, Inc.** for total stated consideration of **~$110.0 million**,
primarily Snowflake common stock with the remainder in cash, ~30% of the equity
consideration subject to vesting (post-combination SBC). "The transaction is expected to
close in June 2026, subject to satisfaction of certain closing conditions." The disclosure
is XBRL-tagged `us-gaap:SubsequentEventMember srt:ScenarioForecastMember
snow:NatomaLabsInc.Member 2026-06-01 2026-06-30` — a forecast, machine-readable
confirmation it was not consummated at filing.

Close status searched and NOT confirmed as of 2026-07-27: EDGAR full-text search for
"Natoma" (all forms) returns no 8-K Item 2.01 completion filing; Snowflake's newsroom
carries only the "Announces Intent to Acquire" release; natoma.ai remains live on its own
domain with unchanged announcement wording; no trade-press report of consummation
(Reuters, The Register, Forbes, CIO, BigDATAwire all report intent only). Caveat recorded on
the page: at ~$110M the deal is likely below Snowflake's Reg S-X significance threshold, so
no completion 8-K would be required — absence is weak evidence, not proof of non-close.

Source cached: `raw/sources/2026-07-27--natoma--snowflake-10q-subsequent-event.md`.
Frontmatter: `closed: null`, price "~$110.0M (stock + cash)", `last_verified: 2026-07-27`,
`verify_after: 2026-09-15`. Body gained a dated History line, an expanded M&A section, a
strategic-intent note (AI agent enablement / governed access being folded into Snowflake
Intelligence, Cortex Agents, Cortex Code), and a procurement caveat in the CTO lens.
survey-v2.csv: both Natoma rows' flag-notes refreshed with the agreement date, price, and
explicit "close unconfirmed as of 2026-07-27" (both already said PENDING — correct).

## [2026-07-27] decision | natoma status correction
**Contradiction (hard) resolved: page said `acquired-closed`, evidence says pending.**

wiki/vendors/natoma.md carried `ownership_state: acquired-closed` with
`acquisition: {announced: 2026-05-27, closed: 2026-05-27, ...}` — a close date identical to
the announcement date — while the same page's body read "Deal is subject to customary
closing conditions; financial terms undisclosed; **close date not stated**." The page
contradicted itself, and no source entry supported any close date. Diagnosis: the `closed`
field was populated by duplicating `announced` during the 2026-06-28 research pass rather
than from evidence — exactly the failure mode CLAUDE.md §7's "Announced ≠ closed" rule
exists to prevent.

Resolution: corrected to `ownership_state: acquired-pending` with `closed: null` and
`verify_after: 2026-09-15`, per SCHEMA.md §5 rule 4 (`acquired-closed` requires a close date
plus a source entry; `acquired-pending` requires `verify_after`). Chose the conservative
state deliberately: the expected June 2026 close window has elapsed, so the deal may well
have closed quietly, but "probably closed" is not a verifiable close date and must not be
recorded as one. The next authoritative checkpoint is Snowflake's Q2 FY2027 10-Q (quarter
ended 2026-07-31, normally filed late Aug / early Sept), where a closed deal appears in
purchase-price accounting rather than as a forecast subsequent event — hence the
2026-09-15 verify_after.

Process note for the rest of this sweep: a `closed` date equal to the `announced` date is a
smell, not a fact. Worth grepping other `acquired-closed` pages for that pattern.

## [2026-07-27] research | portkey
URL audit + M&A re-verification. `portkey.ai` live (HTTP 200, no redirect), unchanged as the
canonical vendor URL, now carrying a banner "Palo Alto Networks has completed the acquisition
of Portkey" linking to PANW's completion release.

**Explicitly checked for the `closed == announced` copy-paste bug flagged by the natoma task
earlier in this sweep — NOT present on this page.** portkey.md already carried
`announced: 2026-04-30, closed: 2026-05-29` (distinct dates), and both survive primary-source
re-verification. The 2026-06-28 research pass on this page was sound; no correction needed and
no contradiction to log.

Primary source: **PANW Form 10-Q for the quarter ended 2026-04-30, filed 2026-06-03**
(CIK 0001327567, accession 0001327567-26-000015), found via EDGAR full-text search. Note 6
Business Combinations: "On April 30, 2026, we entered into a definitive agreement to acquire
Portkey, Inc., a privately-held AI Gateway company ... in exchange for total consideration of
$140 million in cash and replacement awards, subject to adjustments." Note 17 Subsequent
Events: "On May 29, 2026, we completed the acquisition of Portkey." MD&A repeats the close
date. Recorded as a business combination in PANW fiscal Q4 2026. The PANW completion press
release (dateline May 29, 2026) corroborates the close date independently.

**New fact recovered: the purchase price.** Both PANW press releases withheld terms, so the
page had carried `price: null` and an open question "acquisition price (undisclosed)". The
10-Q discloses it — **$140M in cash and replacement awards** — confirming the SEC-filings-over-
blog-posts lesson from the cyberark/conjur tasks: for a public acquirer, the filing routinely
supplies the one number the press release omits. Context on scale: PANW closed CyberArk at
$21.1B (2026-02-11) and Koi Security at $231M (2026-04-14) in the same fiscal year, so Portkey
is the smallest of the FY2026 tuck-ins.

Source cached: `raw/sources/2026-07-27--portkey--panw-10q-close-date-and-price.md`.
Frontmatter: `ownership_state: acquired-closed` retained (justified — real close date plus
source entries, per SCHEMA.md §5 rule 4), `price` null -> "$140M cash + replacement awards",
expanded `ownership_note`, `last_verified: 2026-07-27`, three `sources:` entries added (10-Q
for close and price, PANW announcement release for the announced date). YAML re-parsed clean.
Body: dated History line; header note that the vendor is no longer independent; M&A section
rewritten around the filing; positioning rewritten (the differentiator is now the Prisma AIRS
bundle — AI Runtime Security + Idira agent identity + Chronosphere telemetry — which is also
the lock-in); CTO lens gained two procurement points (get standalone-SKU availability in
writing before renewal; the genuinely neutral gateway option is now OSS, since the commercial
independents in this category keep getting acquired).

survey-v2.csv: AI Gateway / "Portkey (Palo Alto)" flag-note expanded with announce date, close
date, price, and the standalone-SKU caveat; the AI Runtime Security row's Prisma AIRS note
now dates the Portkey component too. Vendor URL left as `https://portkey.ai` (still live and
still the product's own site).

## [2026-07-27] research | splunk

Confirmation-only pass, triggered by the automated URL audit: `splunk.com` is live with no
redirect and states "Splunk is now a Cisco company", with references to Cisco Talos threat
intel and Cisco support resources. This is long-settled news — Cisco closed the acquisition
2024-03-18 — and the page already documented it correctly in `ownership_state`
(`acquired-closed`), `owner` (Cisco), `ownership_note`, the M&A section and the body. No
re-research performed; the two existing sources (Network World completion coverage and the
Splunk 8-K) already support every claim on the page.

Not a pure no-op, though. The `acquisition:` frontmatter had its dates **transposed** —
`{announced: 2024-03-18, closed: 2023-09-21}` — i.e. a close date preceding the announcement,
contradicting the `ownership_note` and the M&A section on the same page, both of which read
correctly (announced 2023-09-21, completed 2024-03-18). Almost certainly a field-order slip
when the stub was filled on 2026-06-28. Corrected to `{announced: 2023-09-21, closed:
2024-03-18}`. Worth noting for the rest of the URL-audit sweep: a bulk ownership check that
only looks at `ownership_state`/`owner` will not catch this class of error, since both of
those fields were right — only the structured dates were wrong.

Also filled `price`, which had been `null` despite the body and both cited sources stating
the figure: `~$28B ($157.00/share cash)`, matching the price-format convention used by the
cyberark/portkey/koi rows. `last_verified` 2026-06-28 -> 2026-07-27.

survey-v2.csv checked, no change needed: the SIEM/SOAR/SecOps row already reads
`Splunk (Cisco)` with flag-note "Acq. by Cisco (closed 2024-03-18; $28B)" — consistent with
the corrected frontmatter. Open question about post-acquisition Splunk + Cisco XDR bundling
and current licensing left standing; it needs pricing research, not an ownership check.

## [2026-07-27] research | splxai
URL audit + M&A re-verification against primary SEC filings. `splx.ai` live (HTTP 200, no
redirect), title "SPLX | End-to-End Security for AI", banner "SPLX is now part of Zscaler".
The SPLX brand and the Probe product both survive the acquisition (Probe still has its own
login at `probe.splx.ai`), so `website` stays `https://splx.ai` — no rebrand redirect to
zscaler.com, unlike several other pages in this sweep.

**Both bug patterns flagged earlier in this sweep were checked; the natoma-style fabricated
close date WAS present.** `acquisition:` read
`{announced: 2025-11-03, closed: 2025-11-03, price: null}` — a close date identical to the
announcement date, with no source entry supporting any close date, while the body simultaneously
admitted under Open Questions that the "exact close date within Zscaler Q1 FY2026" was unknown.
Same failure mode as natoma: the `closed` field was populated by duplicating `announced` during
the 2026-06-28 pass. The splunk-style transposition was not present.

Primary source: **Zscaler Form 10-Q for the quarter ended 2025-10-31**, filed 2025-11-25
(CIK 0001713683, accession 0001713683-25-000205), Note 6 *Business Combinations*:

> On October 31, 2025, we acquired all the equity of SPLXAI Inc. ("SPLX") [...] We acquired SPLX
> for a total cash purchase price consideration of $40.6 million.

Corroborated by the filing's own XBRL contexts, which tag `zs:SPLXAIIncMember` at `2025-10-31`
and `zs:RedCanaryIncMember` at `2025-08-01` — two separate closings inside Q1 FY2026.

Corrections applied:
- `closed` 2025-11-03 → **2025-10-31** (verified).
- `price` null → **$40.6M cash**. The page had claimed the SPLX figure was "not separately
  disclosed" and was only available inside the $692.0M Red Canary + SPLX aggregate. That was
  wrong — the aggregate covers two deals and the 10-Q breaks SPLX out explicitly. Also captured:
  $16.6M grant-date fair value of service-conditioned retention RSUs (expensed post-combination,
  not purchase price) and 50,180 deferred shares for key-employee re-vesting.
- `ownership_state: acquired-closed` **confirmed correct** and now genuinely sourced, rather than
  resting on a duplicated date.
- `last_verified` → 2026-07-27; added three `sources:` entries; added `acquired` tag.

Body: rewrote competitive positioning, which still read as though SPLX were an independent
pure-play. Reframed around platform ownership and noted that the AI red-teaming category has now
almost entirely consolidated into incumbents (Lakera→Check Point, promptfoo→OpenAI, CalypsoAI→F5,
SPLX→Zscaler), with [mindgard](wiki/vendors/mindgard.md) the notable remaining independent — each
of those four cross-references verified against the repo's own vendor pages rather than asserted
from memory. Added the buyer-relevant read of the $40.6M price: a small tuck-in, roughly a third
of it retention equity, so expect a Zscaler SKU rather than a preserved standalone franchise.

survey-v2.csv: answer option `SplxAI (Zscaler)` → `SplxAI / SPLX (Zscaler)` (live brand is SPLX;
kept the old name for respondent recognition), Flag/Note updated with verified dates and price.
Vendor URL unchanged. Bijection is keyed on the Wiki URL column, so the rename is lint-safe.

Cached: `raw/sources/2026-07-27--splxai--zscaler-10q-close-date-price.md`.

## [2026-07-27] decision | splxai close date and price correction
**Second confirmed instance of the natoma `closed == announced` fabrication pattern.** Recording
it separately because it sharpens the lesson from the natoma entry earlier today.

At natoma the suspicious date was easy to spot because the deal was genuinely still pending, and
the conservative fix was to downgrade to `acquired-pending`. Here the deal really had closed, so
the wrong date sat undetected behind a *correct* `ownership_state`. **A correct ownership state is
not evidence that the dates under it were ever verified.** The tell was the same in both cases and
was visible without any external research: the page contradicted itself, asserting a precise
`closed` value in frontmatter while its own Open Questions section said the close date was unknown.

The correction here runs the opposite direction from natoma — the real close date (2025-10-31) is
*earlier* than the recorded one, because Zscaler closed the deal on the last day of its fiscal Q1
and only announced it publicly three days later, on 2025-11-03, with language that already read
"has acquired." So `announced` legitimately post-dates `closed` on this page. That inversion looks
like an error and will likely be re-flagged by a future audit; the frontmatter `ownership_note`,
the body, and the cached source all state explicitly that the ordering is deliberate. Worth
generalising: for deals a public acquirer discloses *after* completing them, "announced" means
"made public," not "signed," and the announced ≥ closed ordering is normal rather than suspect.

Method note reinforcing the portkey/cyberark/lakera pattern: for a public acquirer, the 10-Q
business-combination note is strictly better than any press release. It gave both the exact close
date and a SPLX-specific price ($40.6M) that no press release disclosed and that this page had
recorded as undisclosable. The XBRL context tags are a fast cross-check — they date each
acquisition separately even when the narrative aggregates them, which is exactly what
disentangled SPLX from Red Canary inside the $692.0M headline figure.

## [2026-07-27] research | stytch

Re-verified the Twilio acquisition of Stytch against **primary SEC filings** as part of the URL-audit
sweep. The audit flagged stytch.com as live (200, no redirect) with a banner reading "Stytch has
joined Twilio to build the intelligent identity layer for the internet."

**Neither bug pattern found.** This page was clean on the two failure modes that turned up elsewhere
in this sweep:

- *Transposed dates* (the splunk.md pattern): no. Announced 2025-10-30 precedes closed 2025-11-14,
  in the right order.
- *Fabricated close date copied from the announced date* (the natoma.md / splxai.md pattern): no.
  The two dates were distinct, 15 days apart, and both independently corroborated.

Verified from Twilio's own filings rather than trusting the cached blog post:

- **Announced 2025-10-30** — Twilio Form 10-Q for Q3 2025 (filed 2025-10-31): "On October 30, 2025,
  we entered into a definitive agreement to acquire Stytch, Inc., an identity platform for AI agents.
  We expect the transaction to close in the fourth quarter of 2025, subject to customary closing
  conditions." The same filing lists "the timing and completion of our proposed acquisition of
  Stytch, Inc." as a forward-looking statement — a clean announced-≠-closed marker in the primary
  record.
- **Closed 2025-11-14** — Twilio Form 10-K FY2025, Note 11 (Business Combinations): "On November 14,
  2025, the Company acquired all outstanding shares of Stytch, Inc." Corroborated by Stytch's own
  changelog the same day ("Twilio's acquisition of Stytch is now final").

**Material addition: the price, previously `null`.** Twilio's blog said terms were undisclosed, but
the FY2025 10-K discloses the whole purchase-price allocation: **$104.1M paid in cash, $58.5M net of
cash acquired** — cash acquired $45.6M, identifiable intangibles $11.8M (developed technology $9.9M
/ 5yr, customer relationships $2.0M / 4yr), goodwill $48.5M. This repeats the lesson from the splxai
and portkey entries: **a "terms undisclosed" press release is not evidence that terms are
undisclosable.** When the acquirer is public, the next 10-Q or 10-K usually prices the deal, and
EDGAR should be checked before recording `price: null`.

Editorially the number matters. $104.1M gross is **below the ~$120M Stytch raised in disclosed
primary rounds** ($30M Series A + $90M Series B) and roughly a tenth of its 2021 $1B Series B
valuation, with effective enterprise value near $58.5M and only $11.8M booked as identifiable
technology and customer intangibles. That reads as a soft landing rather than a premium strategic
exit, so the page now frames roadmap durability as an open diligence question and rewrites the
competitive section to treat Stytch as a Twilio platform component, with [descope](wiki/vendors/descope.md)
noted as the remaining independent comparable in developer-first agent/MCP auth.

Brand persists: stytch.com still resolves, still Stytch-branded, product names (Connected Apps,
IsAgent, Device Fingerprinting) intact; Twilio Inc. is parent/data controller with Stytch, Inc. as
day-to-day processor. `website` left at https://stytch.com; `ownership_state` stays `acquired-closed`
(a real, cited close date supports it). last_verified → 2026-07-27; frontmatter `sources:` added.
Source cached to `raw/sources/2026-07-27--stytch--twilio-sec-filings.md`. survey-v2.csv row 114
Flag-Note upgraded to the verified dates + price.

No `decision` entry: nothing recorded on the page was wrong, so there was no contradiction to
resolve under CLAUDE.md §8 — this was a confirmation plus a fill of a null field.

## [2026-07-27] research | surepath-ai

URL audit found `surepath.ai` live (HTTP 200, no redirect) carrying a **"SurePath AI is now a part of
F5"** banner linking to F5's 2026-06-22 press release and to the F5 AI Security Platform page. The
page was recorded `acquired-pending` with `closed: null` and `verify_after: 2026-10-01`.

**Is this the CalypsoAI deal? No — it is a separate, second F5 acquisition.** Different target
(Denver, network-based shadow-AI discovery vs Dublin, AI runtime guardrails), different fiscal year
(F5 FY2026 Q3 vs FY2025 Q4), different money. CalypsoAI closed 2025-09-26 for $145.2M; SurePath
closed nine months later. F5 stacks them as complementary — SurePath finds the AI usage, the
CalypsoAI-derived F5 AI Red Team tests it and F5 AI Guardrails polices it.

**Close established without an F5 completion notice.** F5 published no separate closing date, filed
**no 8-K** for the deal, and as of 2026-07-27 **no F5 SEC filing names SurePath AI** — EDGAR
full-text search for the phrase returns exactly one hit across all filers, SurePath's own 2024 Form
D. Three converging pieces of evidence nonetheless establish that the deal is done:

1. The 2026-06-22 press release uses completed-transaction language throughout ("F5 acquires…", "F5
   also announced the acquisition of…", "The addition of SurePath AI powers…") with **none** of the
   "definitive agreement / subject to customary closing conditions / expected to close" hedging F5
   used during CalypsoAI's pending phase.
2. `surepath.ai` states the company "is now a part of F5."
3. **F5's own GAAP cash flows.** The Q3 FY2026 earnings release (8-K Ex-99.1, filed 2026-07-27)
   shows **$47.619M** of "acquisition of businesses, net of cash acquired" for the **nine** months
   ended 2026-06-30, against **nil** on the same line for the **six** months ended 2026-03-31 (Q2
   FY2026 10-Q). So acquisition cash actually moved inside 2026-04-01 → 2026-06-30, and SurePath is
   the only acquisition F5 announced in that window.

Recorded as **closed 2026-06-22** (announce and close effectively simultaneous), `ownership_state`
→ `acquired-closed`.

**Price: inferred, not disclosed.** The same arithmetic implies **~$47.6M cash net of cash
acquired** — roughly 7.5× on $6.3M of venture funding for a 3-year-old company. F5 has not itemized
the figure and does not name SurePath in the filing, so the page states it as an inference from F5's
cash-flow statement with that caveat, not as a disclosed number. This is the inverse of the pattern
from the splxai / portkey / stytch entries: there the 10-Q *supplied* a price the press release
withheld; here the 10-Q that would supply it (**Q3 FY2026, period 2026-06-30**) had not been filed
as of 2026-07-27. `verify_after` set to **2026-08-10** to re-check EDGAR for a Note 4
business-combination disclosure with the exact date and purchase-price allocation. Precedent for why
that matters: F5's FY2026 Q1 10-Q moved CalypsoAI's close date by 12 days and its price by ~$35M
against the press narrative (logged 2026-07-27).

**Brand outcome is the opposite of CalypsoAI's, and that is the load-bearing editorial finding.**
`website` stays `https://www.surepath.ai` — the site is live, unredirected, fully SurePath-branded,
still taking demo requests, `admin.surepath.ai` still the console — whereas `calypsoai.com`
301-redirects to F5's AI Guardrails page with the CalypsoAI name gone. F5 CTO Jimmy White is quoted
saying F5 will continue "to offer SurePath AI as an independent platform" alongside ADSP
integration. Nor has SurePath been renamed into an F5 SKU: the F5 AI Security Platform page lists
**AI discovery** as one of four pillars, but the only named products under it remain **Guardrails**
and **Red teaming** — **there is no F5-branded "AI Discovery" product** as of 2026-07-27. Both
brand-survival open questions on the page resolved accordingly (with "for how long" left open — the
independent-platform commitment carries no stated horizon, and CalypsoAI's brand lasted ~10 months).

Also updated [f5](wiki/vendors/f5.md) for consistency (its ownership_note and body still said
"pending close as of 2026-07-13"; last_verified 2026-06-28 → 2026-07-27, verify_after 2026-08-10)
and survey-v2.csv rows 28 (F5) and 127 (SurePath AI) — row 28 additionally still carried the stale
"acquired CalypsoAI 2025-10", which the 2026-07-27 CalypsoAI pass had corrected on row 46 but missed
here. Source cached to `raw/sources/2026-07-27--surepath-ai--f5-close-evidence.md`.

## [2026-07-27] decision | surepath-ai ownership_state pending → closed on inference-plus-primary evidence

CLAUDE.md §7 requires a real, cited close date before `acquired-closed`, and the acquirer never
published one. Recording `closed: 2026-06-22` rests on the press release's completed-transaction
grammar plus F5's cash-flow statement bounding the payment inside the quarter ended 2026-06-30 —
strong, but one inferential step short of "F5 said it closed on date X."

Decision: **record it as closed rather than leaving it pending**, because leaving `acquired-pending`
would assert something affirmatively false (that a transaction which has already been paid for and
absorbed is still awaiting completion), and that is the worse error for a reader doing vendor
diligence. The inference is disclosed in the body, in the `acquisition.price` field, and in the
cached source rather than laundered into a bare fact, and `verify_after: 2026-08-10` queues the
Q3 FY2026 10-Q as the confirmation. If that filing gives a different close date, correct the page in
place with a dated History line — the calypsoai precedent.

Separately, the **~$47.6M price is labelled an inference everywhere it appears** and is deliberately
*not* stated as a plain figure in `acquisition.price`; per CLAUDE.md §7 an unverified value would
otherwise stay null, and the compromise is to carry the number with its derivation attached so the
next pass can confirm or drop it rather than re-derive it.

## [2026-07-27] research | symmetry-systems
URL audit + M&A re-verification against primary SEC filings. Verified status: **`acquired-pending`**, Zscaler
(NASDAQ: ZS), **$175.0M** total consideration.

Primary source: Zscaler **Form 10-Q for the quarter ended 2026-04-30** (filed 2026-05-26, accession
0001713683-26-000096), **Note 17 *Subsequent Event***: "On May 19, 2026, we entered into a definitive agreement to
acquire Symmetry Systems, Inc. ... for total consideration of $175.0 million, consisting of cash and restricted
shares subject to future employment services. ... The transaction is expected to close in the fourth quarter of
fiscal 2026, subject to the satisfaction of closing conditions." Zscaler FY ends 2026-07-31.

Negative evidence for non-close as of 2026-07-27: no Item 2.01 completion 8-K (EDGAR full-text search for
"Symmetry" on CIK 0001713683 returns exactly 2 hits, both 2026-05-26 — this 10-Q and the same-day earnings 8-K);
Zscaler's submissions feed shows only Forms 4 and 144 since 2026-05-26; no completion press release; every headline
still reads "to acquire"; symmetry-systems.com live on its own domain with a "Zscaler to acquire" banner and a
2026-05-21 post whose forward-looking-statements section says "the proposed acquisition."

Frontmatter: `ownership_state` acquired-closed→acquired-pending; `acquisition.closed` 2026-05-21→null;
`acquisition.price` null→"$175.0M (cash + restricted shares)"; `last_verified` 2026-07-27; `verify_after`
2026-09-15 (post Zscaler FY2026 10-K, expected ~2026-09-11); added 3 `sources:` entries; tags += zscaler,
acquired-pending. `website` unchanged (symmetry-systems.com still live, no redirect).

Body: rewrote the Ownership section around the signed-not-closed distinction; added a **two Zscaler deals** table
contrasting SPLX (closed 2025-10-31, $40.6M, model/prompt layer) with Symmetry (pending, $175.0M, data layer) and
noting the two are complementary rather than overlapping — with the caveat that the combined Access-Graph +
inline-enforcement story is roadmap, not shipped; added a mid-transaction buy-side caveat to the CTO lens (air-gapped/
on-prem deployment is the differentiator most at risk under a cloud-delivered SSE owner); resolved the price open
question and added a "did it close?" open question.

survey-v2.csv: enriched both affected rows (Symmetry DSPM row + Zscaler SSE/SASE row) with the verified price and
explicit PENDING-as-of-2026-07-27 wording. Both already said "pending" — the CSV was **right** and the wiki page was
wrong, which is itself a useful signal.

Cached: `raw/sources/2026-07-27--symmetry-systems--zscaler-10q-pending-175m.md`

## [2026-07-27] decision | symmetry-systems ownership_state closed → pending (unsourced close date)
**Correction, not a hard contradiction** — the page's own cited evidence never supported the closed state, so there
were never two competing sources to reconcile.

The 2026-06-28 pass recorded `acquisition: {announced: 2026-05-21, closed: 2026-05-21, ...}` and
`ownership_state: acquired-closed`. The `closed` value was a duplicate of `announced` with **no citation** — it was
inferred from the cached source's own hedge, "close expected shortly after announcement," which is anticipation, not
completion. Zscaler's 10-Q Note 17 shows the deal was still subject to closing conditions five days *after* the
announcement, and no filing since confirms close. Per CLAUDE.md §7 (announced ≠ closed) the state is corrected to
`acquired-pending` with `closed: null` and a `verify_after` date.

**Third instance of the same defect pattern in this sweep**, and the pattern is now well characterised: an
announcement date copied into the `closed` field, converting a pending deal into a false closed one.
- [natoma](wiki/vendors/natoma.md) — Snowflake, same shape, corrected earlier today.
- [splxai](wiki/vendors/splxai.md) — Zscaler; the *inverse* failure. There `closed` was also set equal to the
  announcement date (2025-11-03), but that deal had genuinely closed — on **2025-10-31**, three days *earlier*. The
  state was right by luck; the date was wrong.

Common root cause: treating the announcement date as the close date whenever a real close date is not to hand. The
two directions of error are worth naming separately — Natoma/Symmetry overstate ownership (pending sold as closed,
the more dangerous direction for a buyer), while SPLX merely misdated a real close. Both are fixed the same way: get
the acquirer's 10-Q/8-K and read the business-combination or subsequent-event note.

**Suggested follow-up (not actioned here):** sweep all remaining `acquired-closed` pages for
`acquisition.closed == acquisition.announced` with no `sources:` entry backing the close — that predicate cheaply
identifies the whole affected population rather than catching them one page at a time. Recorded against the sweep's
open follow-ups item.

## [2026-07-27] research | trojai
URL audit + M&A re-verification against A10's primary disclosures and EDGAR. Verified status:
**`acquired-closed` — CONFIRMED, no correction needed.** A10 Networks (**NYSE**: ATEN), announced *and*
closed **2026-06-15**, **price undisclosed**.

Re-checked because the 2026-06-28 pass had recorded `acquisition: {announced: 2026-06-15, closed:
2026-06-15}` — a `closed` value identical to `announced` with no separate citation, which is the exact
defect shape corrected on natoma and symmetry-systems earlier in this sweep. Here the state survives
scrutiny.

Affirmative evidence for close:
- A10's own release, verbatim lead (identical across two independent retrievals — a10networks.com and
  StockTitan's reproduction of the wire): *"SAN JOSE, Calif., June 15, 2026 – A10 Networks (NYSE: ATEN)
  today announced that it **has acquired** TrojAI…"* Completed-transaction grammar, with **no**
  definitive-agreement, closing-conditions, regulatory-approval, or expected-close language anywhere.
  Ordinary simultaneous sign-and-close for a small private tuck-in needing no clearance.
- **Brand integration already live**: troj.ai (200, no redirect) serves a logo reading "TrojAI by A10
  Networks" plus a "New! A10 Networks Acquires TrojAI" banner. Putting the acquirer's name in the
  target's logo is post-close behaviour — pre-close, that is what gun-jumping rules forbid. Contrast
  symmetry-systems.com, still on its own domain with a "Zscaler *to acquire*" banner.

Negative SEC evidence, consistent with a closed-but-immaterial tuck-in rather than against close:
**no 8-K filed** (A10's only 8-Ks since 2026-05-01 are 2026-05-01 and 2026-05-07, both Item 5.02
officer changes — no Item 2.01); **EDGAR full-text search for "TrojAI" across all 10-K/10-Q/8-K returns
zero hits** (the only three EDGAR hits for the string anywhere are TrojAI, Inc.'s own 2024-04-24 Form Ds,
CIK 0002019012). Item 2.01 is triggered only by acquiring a *significant* amount of assets, and A10
stated the deal is immaterial to FY2026 — so no filing obligation arises. A10's most recent 10-Q covers
the quarter ended 2026-03-31 and predates the deal; the quarter ended 2026-06-30 is the first period
containing it, due early Aug 2026.

Price stays **null** — never disclosed, and unlike the F5/SurePath case there is no filed cash-flow
statement covering the period to bound it against. Not guessed at, per CLAUDE.md §7.

Frontmatter: `ownership_state` unchanged (acquired-closed, now actually sourced); `acquisition`
unchanged but now cited; `ownership_note` rewritten to state the sign-and-close basis explicitly;
`last_verified` 2026-06-28→2026-07-27; `verify_after` null→**2026-08-15** (A10's Q2 FY2026 10-Q, the
first filing that could carry a purchase-price allocation); added 4 `sources:` entries; tags +=
a10-networks, acquired-closed. `website` unchanged — troj.ai is live with no redirect and the brand
persists as a sub-brand, so it stays the canonical URL.

Body: rewrote Ownership around *why* closed is defensible here (verbatim grammar + brand integration +
absence-of-8-K reasoning) rather than asserting it; added a new section on the acquisition as a genuine
**diversification** — A10 is a ~$250M ADC/load-balancer/DDoS vendor moving from the packet/flow layer to
the model/prompt layer, a different engineering substrate sold to a different buyer, with "sovereign AI
security" (on-prem hardware AI firewall + TrojAI's software Detect/Defend) as the stated thesis and the
self-hosted posture flagged as both the most durable rationale and the capability most at risk of being
diluted toward appliance attach. Resolved the close-date open question; added open questions on price,
on the newer **Defend for MCP** / **Defend for Employees** SKUs seen on the post-acquisition site, and on
founder retention.

Incidental verifications: TrojAI HQ (Saint John, New Brunswick) independently confirmed against TrojAI,
Inc.'s SEC Form D business address, 14 King St. Suite 102. A10's exchange confirmed as **NYSE** via
`data.sec.gov` submissions (`exchanges: ["NYSE"], tickers: ["ATEN"]`) — the page's "NYSE: ATEN" was
already correct; a NASDAQ attribution raised during the sweep was wrong.

survey-v2.csv: the TrojAI row said "announced 2026-06-15 — **pending**", which was **wrong**; corrected to
CLOSED with the verified date, ticker, undisclosed terms, and the sub-brand note. Note this is the mirror
image of the symmetry-systems finding, where the CSV was right and the wiki page wrong — the two artifacts
drift independently and neither can be treated as authoritative over the other.

Cached: `raw/sources/2026-07-27--trojai--a10-close-verification.md`

## [2026-07-27] decision | trojai acquired-closed retained — sign-and-close distinguished from unsourced-close
No status change, but recording the reasoning because this is the first page in the sweep where the
suspicious `closed == announced` pattern turned out to be **legitimate**, and the discriminator is worth
having written down.

The pattern flagged on natoma and symmetry-systems is an announcement date copied into `closed` where the
underlying deal was still subject to closing conditions. That is a fabrication. But `closed == announced`
is *also* the correct, truthful encoding of a simultaneous sign-and-close, which is the norm for small
private acquisitions needing no regulatory clearance. The two are indistinguishable from the date fields
alone — the discriminator is the acquirer's own grammar plus observable integration:

- **Pending** looks like: "entered into a definitive agreement," "expected to close in Q4," "subject to
  the satisfaction of closing conditions"; target still on its own domain and brand; acquirer's filings
  describe a *proposed* transaction. (Zscaler/Symmetry.)
- **Closed** looks like: "has acquired," no conditions language at all, and the target's brand already
  absorbed into the acquirer's. (A10/TrojAI.)

Decision: **retain `acquired-closed`**, and treat the absence of an 8-K as neutral rather than as evidence
of pendency — Item 2.01 has a significance threshold this deal explicitly does not meet, so demanding a
filing here would import a false standard. The residual uncertainty is real but narrow: A10 has never
published a close *date* as such, so 2026-06-15 rests on the release's past tense. `verify_after:
2026-08-15` queues A10's Q2 FY2026 10-Q; if its business-combination note gives a different acquisition
date, correct in place with a dated History line — the calypsoai precedent.

Sweep tally for this defect pattern is now: **natoma** (false closed → pending), **symmetry-systems**
(false closed → pending), **splxai** (right state, wrong date), **surepath-ai** (pending → closed on
inference), **trojai** (closed, correctly). The lesson is that `closed == announced` is a *prompt to
verify*, not a defect in itself.

## [2026-07-27] research | trulens

URL audit flagged `trulens.org` as live with no redirect while the page carried
`ownership_state: acquired-pending`, `acquisition: {announced: 2024-05-22, closed: null}`. The site's own
copy — "Originally created by TruEra" and "Since TruEra's acquisition by Snowflake, Snowflake now actively
oversees and supports the development of TruLens in open source" — presents the deal as settled historical
fact. Re-verified against primary sources.

**What the deal actually was.** Not a company acquisition. Snowflake's Q1 FY2025 earnings release (SEC Form
8-K EX-99.1, filed 2024-05-22) states it "announced its **intent to acquire certain technology assets and
hire key employees from TruEra**." The same-day Snowflake blog says "the TruEra AI Observability platform"
— the platform, not the entity. Asset purchase + acqui-hire (~37 people incl. all three co-founders:
Uppington, Datta, Sen). That structure explains why the TruEra corporate brand simply evaporated rather
than surviving as a subsidiary.

**Close.** Bounded, never precisely disclosed. Snowflake's 10-Q for the quarter ended 2024-07-31 books a
completed business combination in Note 7; Snowflake's 2024-06-24 blog writes "in the weeks since the
acquisition" in the past tense while listing shipped TruLens improvements. So close ∈ [2024-05-22,
2024-06-24] → recorded `closed: 2024-06` (apex-security month-granularity precedent).

**Price.** Note 7 reads: "the Company acquired certain technology assets and hired key employees from a
privately-held company for **$10.8 million in cash**" ($2.5M developed technology, $8.3M goodwill).
Snowflake does not name the counterparty, and never does — EDGAR full-text search for "TruEra" across all
Snowflake 8-K/10-Q/10-K returns exactly one hit, the 2024-05-22 EX-99.1; the FY2025 10-K does not mention
it at all. But the 10-Q phrasing is a verbatim match for Snowflake's own TruEra press-release language and
falls in the quarter immediately after the announcement. Recorded as `price: undisclosed (~$10.8M cash —
inferred …)`, explicitly labelled inference, per the surepath-ai precedent for reading an unnamed
purchase-consideration line.

**TruEra vs TruLens, resolved.** TruEra = the commercial ML/LLM-observability company (Redwood City,
founded 2019), platform and team absorbed, brand retired, `truera.com` now a frozen 2024 page. TruLens =
TruEra's open-source eval library, which survived. The commercial successor is **AI Observability in
Snowflake Cortex**, GA 2025-07-31 — and it is *not a fork*: Snowflake's docs say "TruLens is the platform
that Snowflake uses to track your applications" and require `trulens-core` / `trulens-connectors-snowflake`
/ `trulens-providers-cortex` ≥ 2.1.2. Cortex AI Observability is a managed deployment of the same OSS.
Both standing open questions on the page are now closed.

**Other corrections.** License was wrong: **MIT, not Apache-2.0** (LICENSE file, copyright "Truera, Inc.";
PyPI classifier agrees). Repo still lives at `truera/trulens` — there is no `snowflakedb/trulens` (404).
OSS is demonstrably alive: not archived, pushed 2026-07-27, ~3.5k stars, PyPI `trulens` 2.9.0 released
2026-07-23 on a ~6-week cadence through 2026.

**Slug retained as `trulens`.** Per CLAUDE.md §3, vendor slug = the company — which would argue for
`truera`. Overridden here: the company no longer exists, the product does, and the OSS project is what a
CTO actually shops for and what the CSV option names. `TruEra` stays in `aka`, and the page now opens with
an explicit TruEra-vs-TruLens paragraph so the lineage is not lost.

Frontmatter: `ownership_state` acquired-pending → acquired-closed; `owner: Snowflake`; `hq` reworded;
rewritten `ownership_note`; `acquisition: {announced: 2024-05-22, closed: 2024-06, price: undisclosed
(~$10.8M …)}`; `last_verified` → 2026-07-27; `verify_after` → null; tag `acquired`; six `sources:` entries.
Website unchanged (`https://www.trulens.org`, 200, no redirect). CSV Flag/Note rewritten to say CLOSED.
1 new source cached: `raw/sources/2026-07-27--trulens--snowflake-truera-closed.md`.

## [2026-07-27] decision | trulens — stale `acquired-pending` corrected to `acquired-closed`

Per CLAUDE.md §8 this is a **soft contradiction**, not hard: no two sources name different acquirers or
different facts. One source (`truera.com`) is simply frozen in 2024 forward-looking tense — "TruEra **has
agreed to** join Snowflake!" — while every live source treats the deal as long done. Resolved by recency
and source authority, no `Status: Unresolved` flag needed.

Root cause worth recording: the original 2026-06-28 research correctly confirmed the acquisition but had
no close date, so `closed: null` + a `verify_after` produced `acquired-pending` on a deal that was two
years old. **Heuristic: `acquired-pending` on a deal announced more than ~12 months ago is a defect until
proven otherwise.** Regulatory-clearance megadeals aside, a private, immaterial tech-asset purchase does
not stay pending for two years. Where the acquirer's own product ships on the target's technology and its
docs treat the target as an internal component (Cortex AI Observability on TruLens), the deal is closed
regardless of whether a close date was ever published — reconstruct the date from filings and past-tense
acquirer prose rather than leaving the state pending.

Explicitly **not** related to the other Snowflake deal in this repo: [natoma](wiki/vendors/natoma.md),
announced 2026-05-27 (~$110M stock+cash), genuinely still `acquired-pending` as of 2026-07-27 with
`verify_after: 2026-09-15`. Two Snowflake deals, two states, two years apart — cross-noted on both the
trulens page and here so a future sweep does not conflate them.

Sweep tally for the closed-vs-pending defect pattern is now: **natoma** (false closed → pending),
**symmetry-systems** (false closed → pending), **splxai** (right state, wrong date), **surepath-ai**
(pending → closed on inference), **trojai** (closed, correctly), **trulens** (stale pending → closed;
first case where the staleness came from an abandoned target-side page rather than a mis-read filing).

## [2026-07-27] research | venminder

URL-audit follow-up on the stub created earlier today. `venminder.com` is live (200, no redirect)
and now carries **"Venminder by Ncontracts"** sub-brand copy in body text, with careers links
routed to ncontracts.com. Title, wordmark, domain and product names (Vendiligence, Ven-monitor)
are all still Venminder, and ncontracts.com does not mention Venminder on its homepage while still
marketing its own **Nvendor** vendor-risk line — so this is "X by Y" sub-brand naming, not product
consolidation. Recorded the roadmap question (two overlapping TPRM platforms, one owner) as an
open question for buyers.

Deal dates re-checked against the closed-vs-pending defect pattern from this sweep: **not** a
defect. The 2024-09-04 acquirer press release reads "has acquired" / "Hg **has** bought out prior
shareholders" — completed-deal language, so `announced == closed == 2024-09-04` is genuine, not a
placeholder copy. Sweep tally unchanged.

Updated `aka`, `ownership_note`, naming/provenance, sources and History; `last_verified` stays
2026-07-27. `survey-v2.csv` row ("Venminder (Ncontracts)") already correct — brand persists, no
rename. Cached `raw/sources/2026-07-27--venminder--by-ncontracts-branding.md`.

## [2026-07-27] research | adaptive-shield

URL-fix pass that turned up a real date defect. `adaptive-shield.com` 301s to
`crowdstrike.com/en-us/platform/falcon-shield/` (200, "CrowdStrike Falcon® Shield") — updated
`website`; the standalone brand is retired.

Closed-vs-announced check: **defect confirmed.** `acquisition.closed` was 2024-11-06, a copy of
the announce date, while the body said "closed ~Jan 2025" (an estimate read off the press
release's "expected to close in fiscal Q4"). Neither was right. CrowdStrike's FY2025 10-K Note 12
gives the close as **2024-11-20** and the purchase price as **~$214.4M** ($213.7M cash net of
cash acquired + $0.7M replacement equity awards), vs. the press-reported ~$300M — the gap is
$22.8M of Class A stock subject to vesting plus retention RSU/PSU grants, all excluded from the
purchase price as post-combination comp. Cash-flow line corroborates ($310.3M for Flow Security +
Adaptive Shield, less Flow's $96.4M). Filled `acquisition.price`, which had been null.

Both standing open questions resolved (exact close date/price; Falcon Shield vs. Falcon for SaaS
→ **Falcon Shield**). `survey-v2.csv` row updated (URL + the "closed ~2025-01" note).
Cached `raw/sources/2026-07-27--adaptive-shield--crowdstrike-10k-close-date-and-price.md`.

## [2026-07-27] research | prisma-access-browser

Light-touch URL fix. `paloaltonetworks.com/sase/access-browser` returns a hard **404**; the live
equivalent is `paloaltonetworks.com/sase/prisma-browser` (**200**, "Secure Browser | Prisma
Browser - Palo Alto Networks"). Same company, same ex-Talon lineage — a **URL path change plus a
naming simplification** from "Prisma Access Browser" to "Prisma Browser", *not* a rebrand to a
different company and *not* an ownership event. `ownership_state: acquired-closed` (Talon → Palo
Alto Networks, closed 2023-12-28) was already correct and is untouched.

Updated `website`, `last_verified` → 2026-07-27, `title`/`name` → "Prisma Browser
(Palo Alto/Talon)", and added "Prisma Access Browser" to `aka` — the longer name still appears in
PANW datasheet titles, so both are live search terms. Also filled `form_factor:
[agent, browser-extension]`: PANW now markets three form factors (dedicated desktop browser,
extension for existing consumer browsers, mobile app), which narrows the gap with the
browser-security-extension category.

Slug **not** renamed — `prisma-access-browser` stays, to avoid breaking inbound links and the
`survey-v2.csv` wiki URL; flagged in the page's open questions to revisit if PANW drops the long
name entirely. `survey-v2.csv` needed no edit — its Vendor URL column already pointed at
`/sase/prisma-browser`; its answer-option label still reads "Prisma Access Browser (Palo Alto;
former Talon)", left as-is since that name remains recognizable to survey respondents.

## [2026-07-27] research | prisma-airs

Broken-URL fix flagged by the automated link audit. The `website` on file,
`https://www.paloaltonetworks.com/prisma/prisma-airs`, returns a hard HTTP 404. The live
equivalent is `https://www.paloaltonetworks.com/ai-security/prisma-airs` — verified 2026-07-27,
serving current Prisma AIRS content (AI Gateway, Agent Security, AI Red Teaming, AI Runtime
Security, AI Model Security, AI Posture Management; page links reference AIRS 3.0).

Diagnosis: **site-nav reorganization only.** PANW moved the product out of the `/prisma/` path
into a dedicated `/ai-security/` section — consistent with AIRS being marketed as its own AI
security platform rather than a Prisma sub-brand. No rebrand, no acquisition, no ownership
change; product name, vendor, and scope are unchanged, so no frontmatter beyond `website` and
`last_verified` (→ 2026-07-27) needed touching. Slug, `title`, and `aka` left as-is.

`survey-v2.csv`: two rows carried the dead URL (AI Runtime Security / AI Firewall, and AI-SPM);
both updated to the `/ai-security/` path. The third Prisma AIRS-linked row (MCP Gateway /
"Prisma AIRS AI Agent Gateway") points at `/sase` and was left alone — different page, not
part of this 404.

Light-touch pass: no full lint run, `index.md` untouched (no page added/removed/renamed).

## [2026-07-27] research | relativity-trace

Broken-URL fix flagged by the automated link audit. The `website` on file,
`https://www.relativity.com/data-breach-response/communication-surveillance/`, returns a hard
HTTP 404.

Unlike the other URL fixes in this batch, there is **no successor product page to move to**.
The obvious candidate, `https://www.relativity.com/data-solutions/communication-surveillance/`
— still the link used in Relativity's own Trace press releases — 301s to
`https://www.relativity.com/data-solutions/corporations/`, a generic "Relativity for
Corporations" page with no Trace or surveillance content. (`/data-solutions/compliance/` chains
into the same redirect.) Wayback CDX shows the surveillance path has been a 301 since at least
2024-01. Also checked and ruled out: `/relativity-trace/`, `/trace/`,
`/ediscovery-software/trace/`, `/ediscovery-software/app-hub/relativity-trace/` (App Hub moved
to `apphub.relativity.com`; Trace is not in its catalog — it is first-party, not a partner app),
and `help.relativity.com` current-version Trace docs. Relativity's own HTML sitemap
(`/sitemap/`, 247 links, listing every `/data-solutions/` and `/ediscovery-software/` product
page) contains no Trace or communication-surveillance entry. The XML sitemap is incomplete and
was not treated as evidence.

Diagnosis: **marketing-site consolidation, not a sunset.** Relativity retired the dedicated
Trace landing page from its site IA while the product remains actively marketed — Proofpoint
Enterprise Archive partnership, AI data-cleansing releases, and Relativity Fest 2026
surveillance sessions all reference Trace as a current AI-powered communication surveillance
product. No rebrand, acquisition, or ownership change, so ownership frontmatter is untouched.

Per CLAUDE.md §7 ("never invent"), `website` falls back to the root domain
`https://www.relativity.com/` rather than pointing at a redirect target that does not describe
the product. `last_verified` → 2026-07-27. Added an open question to track whether Trace is
being de-emphasized, folded into a broader compliance offering, or renamed.

`survey-v2.csv`: no edit — the Comms Surveillance block (Behavox, SteelEye, Theta Lake, Shield,
NICE Actimize, Other) has no Relativity Trace row. Noting for a later pass that this is a
CSV ↔ wiki bijection gap (lint rule), pre-existing and out of scope here.

Light-touch pass: no full lint run, `index.md` untouched (no page added/removed/renamed).

## [2026-07-27] research | cloudflare-workers

URL fix, no substantive change. `https://workers.cloudflare.com/` 301-redirects to
`https://www.cloudflare.com/products/workers/`, titled "Cloudflare Workers - Global Serverless
Functions Platform". Fetched and confirmed live and current: serverless functions across 330+
cities, with the surrounding platform (Workers AI, R2, D1, KV, Queues) actively marketed.

Diagnosis: **domain consolidation onto the main marketing site.** Same company, same product,
no rebrand, acquisition, or ownership change — Cloudflare, Inc. (NYSE: NET) frontmatter
untouched.

Changes: `website` → `https://www.cloudflare.com/products/workers/`; `last_verified` →
2026-07-27; `## Sources` entry re-pointed and re-dated; dated History line noting the
consolidation.

`survey-v2.csv`: no edit — there is no "Cloudflare Workers" row. The two Cloudflare rows
(AI-aware Network Security (SSE/SASE), AI Gateway) both point at the AI Gateway product URL and
the parent [cloudflare](wiki/vendors/cloudflare.md) page, which is correct for those categories.

Light-touch pass: no full lint run, `index.md` untouched (no page added/removed/renamed).

## [2026-07-27] research | hashicorp-sentinel

URL fix, no substantive change. `https://docs.hashicorp.com/sentinel` 308-redirects to
`https://developer.hashicorp.com/sentinel`, titled "Sentinel | HashiCorp Developer". Fetched
and confirmed live and current: Sentinel presented as HashiCorp's policy-as-code tool with
getting-started docs, use cases, and the hosted policy playground.

Diagnosis: **docs-platform domain migration.** HashiCorp consolidated all product docs onto the
`developer.hashicorp.com` portal. Same company, same product — no rebrand or ownership change.
Ownership frontmatter untouched (HashiCorp, acq. IBM closed 2025-02-27, $6.4B).

Changes: `website` → `https://developer.hashicorp.com/sentinel`; `last_verified` → 2026-07-27;
dated History line noting the migration. The `## Sources` list needed no edit — both entries
point at the IBM newsroom acquisition release and a cached `raw/sources/` file, neither on the
retired docs domain. No live `docs.hashicorp.com` link remains anywhere in the repo — the only
occurrences left are historical prose in this entry and the page's History line.

`survey-v2.csv`: no edit — there is no "HashiCorp Sentinel" row. The one HashiCorp row
(Secrets Manager, HashiCorp Vault (IBM)) points at `hashicorp.com/products/vault`, a marketing
URL on a different host, out of scope for this fix.

Light-touch pass: no full lint run, `index.md` untouched (no page added/removed/renamed).

## [2026-07-27] research | microsoft-edge-business

URL audit follow-up — **resolved as "keep the existing URL," not a swap.**
`https://www.microsoft.com/en-us/edge/business/` 301s then **302**s to
`https://explore.microsoft.com/en-us/edge/business/`, titled "An Industry-Leading Secure
Enterprise Browser | Microsoft Edge for Business". Fetched and confirmed live and current
(Forrester TEI + IDC recognition, Configure/Pilot/Adopt adoption flow). Same company, same
product — a marketing-site domain shift, no rebrand or ownership change.

Diagnosis: **domain not yet proven permanent.** The whole `/en-us/edge/business/*` subtree moves
together (`/security`, `/download`, `/management`, `/productivity` all redirect alike), which
argues for a real migration. But three signals argue against treating `explore.microsoft.com` as
canonical yet:
1. the www -> explore hop is a **302 (temporary)**, not a 301;
2. the redirect appends a campaign tracking param, `?form=MA13FJ`;
3. the served page's own `og:url` still declares `https://www.microsoft.com/en-us/edge/business/`,
   contradicting its `rel=canonical`, which points at `explore.microsoft.com`.

`explore.microsoft.com` is a Microsoft marketing microsite host that has carried temporary
campaign content before. Decision: keep `website` on the `www` brand domain — it still resolves
200, is not a dead link, and stays correct whichever way Microsoft settles this. Recorded the
conflict as a dated open question on the page rather than papering over it.

Changes: `last_verified` -> 2026-07-27; `verify_after` -> 2027-01-27 (re-check whether the 302
hardens into a 301, then switch); dated History line; new open-questions entry. `website`
deliberately unchanged. The `## Sources` entry pointing at `.../edge/business/security` also
left as-is — it redirects the same way and still resolves 200.

`survey-v2.csv`: no edit needed — the "Microsoft Edge for Business" row (line 131) already
carries `https://www.microsoft.com/en-us/edge/business/`, consistent with this decision.

Light-touch pass: no full lint run, `index.md` untouched (no page added/removed/renamed).

## [2026-07-27] research | bot-blocked vendor refresh (apiiro, haize-labs, openai-chatgpt-enterprise, perplexity-enterprise, robust-intelligence)

Light-touch confirmation pass on the five vendors whose homepages the automated URL
audit could not check because they serve anti-bot interstitials (HTTP 403 Cloudflare
"Just a moment..." / Akamai "Access Denied") rather than being dead, parked, or
rebranded domains.

**Fetch results — all five stayed blocked.** Re-tried each URL directly; every one
returned HTTP 403 to the fetcher, so no page content was retrieved for any vendor.
Verification therefore rests on corroborating evidence (search results, vendor press
activity, aggregator profiles, third-party product coverage) rather than the vendor
site itself.

| Vendor | URL | Block | Verdict |
|---|---|---|---|
| apiiro | apiiro.com | Cloudflare 403 | Active, still independent |
| haize-labs | haizelabs.com | Cloudflare 403 | Active, still independent |
| openai-chatgpt-enterprise | openai.com/enterprise/ | Cloudflare 403 (site-wide) | Active, unchanged |
| perplexity-enterprise | perplexity.ai/enterprise | Cloudflare 403 | Active, unchanged |
| robust-intelligence | cisco.com/…/ai-defense/ | Akamai WAF 403 | Active, acquisition already reflected |

Corroboration notes:
- **Apiiro** — 2026 company-news activity (Guardian Agent AppSec agent, 2026-01-28);
  Tracxn/CB Insights profiles show no acquisition. The 2023-era Palo Alto Networks
  acquisition rumor remains unconfirmed and never closed — `ownership_state` stays
  `independent`.
- **Haize Labs** — GitHub/HuggingFace/X presence live under Haize Labs branding;
  continued j1 judge/reward-model releases (j1-nano, j1-micro). No M&A.
- **ChatGPT Enterprise** — Enterprise/Business/Edu tiers all current with ongoing 2026
  release activity; OpenAI Foundation-controlled PBC ownership unchanged.
- **Perplexity Enterprise** — "Enterprise Pro" and "Enterprise Max" remain the current
  tier names and are actively sold; independent/venture-backed, no M&A.
- **Robust Intelligence** — Cisco still hosts a "Robust Intelligence Is Now Part of
  Cisco" page; AI Defense had a major 2026 expansion. Alias page already correct.

**Changes:** `last_verified` 2026-06-28 → 2026-07-27 on all five, plus one History line
each recording the bot-block and the corroborating basis. No other content edits, no
ownership-field changes, no survey-v2.csv changes, no new contradictions.

Note for future audits: these five URLs are expected to keep returning 403 to automated
fetchers. Treat that signal as "unverifiable by fetch," not as a broken link.

## [2026-07-27] stub | gravitee

Created `wiki/vendors/gravitee.md` — user-requested addition (not from the seed
CSV). Slug = company (`gravitee`), consistent with the `kong` precedent: one page
scoped to the vendor's AI angle, with the general API-management business kept
brief. Registered two `survey-v2.csv` rows (both target categories have a non-null
`survey_question`): "AI Gateway → Gravitee" and "MCP Gateway / Tool Access Control
→ Gravitee MCP Proxy", both pointing at the single canonical page. Added to the
vendor list and survey answer options on both category pages; bumped
`vendor_count` 7→8 (ai-gateway) and 11→12 (mcp-gateway).

## [2026-07-27] research | gravitee

Researched and filled in the same pass (single vendor, not a queue item).

- **Placement decision.** `primary_category: ai-gateway`,
  `also_listed_in: [mcp-gateway]`. Gravitee is structurally the same animal as
  [kong](wiki/vendors/kong.md) — an API-management incumbent extending into AI —
  so it files where Kong files. The MCP cross-listing is earned, not courtesy:
  Gravitee ships an **MCP Proxy** (a native v4 API type, 4.10) that fronts
  upstream MCP servers, an **MCP ACL policy** gating `tools/list`, `tools/call`,
  `prompts/list`, `resources/subscribe`, `resources/read` individually, and
  OpenFGA/AuthZen-based fine-grained tool authorization. It also generates MCP
  servers from OpenAPI specs (**MCP Tool Server**) — the same trick Kong ships,
  and *not* on its own sufficient for the mcp-gateway category.
- **Confirmed a real AI product line**, not rebranded API management: LLM Proxy
  (OpenAI-compatible, OpenAI/Anthropic/Bedrock/Gemini/Vertex, token quotas,
  semantic caching), MCP Proxy, A2A Proxy, AI IAM, MCP Analytics.
- **Ownership:** independent, private, VC-backed. Founded **2015** in Lille,
  France; now Denver/London/Lille. **Series C $60M announced 2025-05-20** led by
  Sixth Street Growth (Riverside Acceleration Capital, AlbionVC); ~$125M total
  raised per TechCrunch. No M&A. `market_position: challenger` in both
  categories — smaller than Kong in both funding and mindshare.
- **Certifications:** ISO 27001 + ISO 27701 (2021-12-15, cert 175256, NQA/UKAS);
  Trust Center also lists SOC 2 Type 2 and PCI DSS v4.0.0. FS traction `claimed`
  (Tide open-banking case study; no asset-manager reference found).
- **Trifecta scoping:** primary category `ai-gateway` has
  `agent_security_context: false`, so the vendor page uses plain risk language
  only — no trifecta framing (SCHEMA.md §0, editorial rule 18).
- `data_leaves_tenancy: partial` — depends on Gravitee Cloud vs self-hosted vs
  customer-hosted control plane; SaaS retention/training-use policy not published
  and left as an open question. Other open questions: Community-Edition vs
  Enterprise split for the AI/MCP features, registered legal HQ, SOC 2 report
  period, A2A Proxy GA status, and the absence of any non-vendor evaluation.
- 3 sources cached to `raw/sources/2026-07-27--gravitee--*.md`.

## [2026-07-27] lint | url-audit-sweep final pass

Wrap-up pass closing out the day's URL-audit / M&A-verification sweep.

**Sweep totals.** 52 `[2026-07-27]` entries in this log across **~40 distinct vendor
pages** touched today, plus 2 vendor pages deleted (`styra`, `whylabs`), 1 vendor page
added (`gravitee`), and 3 slug renames (`auditboard`→`optro`, `conductorone`→`c1`,
`normalyze`→`proofpoint-dspm`). Committed one-per-vendor throughout, per CLAUDE.md §11.

**Date-sanity sweep (new work this pass).** A scratch script parsed the frontmatter of
all 231 `wiki/vendors/*.md` pages looking for three signatures of the acquisition-date
defect that kept surfacing during the sweep: (a) `closed < announced` (transposition),
(b) `acquired-closed` with `closed == announced` and no citation for the close (the
fabricated-close pattern), and (c) `acquired-pending` announced >12 months ago (stale
status, per the heuristic logged on `trulens`).

Raw hits: 2 transposed, 11 same-day closes, 4 pending, 6 state/date inconsistencies.
After excluding the 8 vendors already verified earlier today and triaging the rest,
**6 pages carried genuine defects and all 6 were fixed** against primary sources
(SEC filings preferred), each with a cached source, a dated History line and its own
commit:

- `github-advanced-security` — **transposed**: `{announced: 2018-10-01, closed:
  2018-06-01}`, i.e. closed 4 months before announced. Microsoft 8-K dates the
  announcement 2018-06-04; FY2019 10-K Note 8 and FY2019 Q2 10-Q Note 7 both put the
  close at **2018-10-25**. Price filled ($7.5B stock, $6,924M allocated). Noted the
  10-25 vs 10-26 trap — 10-26 is the day *completion was announced*.
- `prompt-security` — **fabricated close**: `closed` copied `announced` (2025-08-05)
  while the note said the deal closed in fiscal Q3 FY2026. SentinelOne's 8-K and 10-Q
  Note 4 both say **2025-09-05**. Price filled (~$180M per 8-K, $159.3M GAAP
  consideration); the ~$250M Calcalist figure demoted to unconfirmed press estimate.
- `pangea` — **fabricated close**: `closed` copied `announced` (2025-09-16) behind a
  "completed ~Sept 2025" hedge. CrowdStrike's press release announced only a *signed
  agreement*; audited FY2026 10-K Note 12 gives **2025-09-26**. Price filled ($222.7M
  as filed); the ~$260M press figure demoted.
- `prisma-access-browser` — **fabricated announce date**: `announced` copied the close
  date (2023-12-28) while the body already said "intent announced Nov 2023". PANW's Q1
  FY2024 10-Q Note 15 dates the Talon agreement **2023-11-06** with explicit pending
  language. Close 2023-12-28 confirmed. The ~$625M in the body appears in no PANW
  filing — replaced with $458.6M final GAAP consideration (~$550.0M at signing).
- `hashicorp-sentinel` + `terraform-cloud` — **conflated announce/close**, same deal:
  both had `acquired-closed` next to `closed: null` (self-contradictory) with
  `announced: 2025-02-27` actually holding the *close* date. IBM announced **2024-04-24**
  and completed **2025-02-27**; HashiCorp's closing 8-K states both dates in one
  sentence. Ten-month gap was the UK CMA inquiry (Phase 1 clearance 2025-02-25). Price
  filled; `owner: IBM 2025-02-27` normalized to `owner: IBM`.
- `promptfoo` — **self-contradicting close**, the variant this sweep kept finding:
  `acquired-closed` with `closed` copied from `announced` (2026-03-09), while the page's
  own Open Questions admitted "only the announcement was public" and the body said OpenAI
  "announced it *would* acquire". Both primary posts use pending language and carry
  "The closing of the acquisition is subject to customary closing conditions"; no
  completion notice exists and neither party is an SEC filer. Corrected to
  `acquired-pending`, `closed: null`, `verify_after: 2026-10-01`.

Checked and confirmed **not** defects: `splxai` (closed 2025-10-31 genuinely precedes the
2025-11-03 announcement — Zscaler announced an already-completed deal, 10-Q sourced),
`apex-security` and `trulens` (honest month-precision close dates), and all 4
`acquired-pending` pages (none stale — oldest is 195 days, all carry `verify_after`).

**Follow-ups, not chased this pass** (low impact, no reader-misleading claim):
- `relativity-trace` — `ownership_state: acquired-closed` with `owner: Relativity` really
  describes a 2021 Silver Lake **minority growth investment**, not an acquisition. The
  note is honest about it; the state field is the wrong shape. Taxonomy question more
  than a fact error. Still an open R4.
- `github-codespaces` — `acquired-closed` with an all-null `acquisition` block; it is a
  first-party Microsoft/GitHub product, not an acquired company. Same shape problem.
  Still an open R4.

**Housekeeping.** `taxonomy.yaml` appendix still routed `OPA / Styra` to a `styra` page
deleted earlier today — rewritten to point at `open-policy-agent` alone with the
wind-down recorded; `taxonomy.md` regenerated. `index.md` regenerated.

**Final lint status: 0 errors · 27 warns · 2 research-needed · 280 pages.** Commit gate
clean — zero errors and no `Status: Unresolved` anywhere in `wiki/`. Research queue is
down from 4 to 2 (the two shape questions above); the 27 warns are the long-standing R1
orphan and R9 CSV-note backlog, unchanged in character by this sweep. Verified no live
markdown link anywhere in `wiki/`, `index.md` or `survey-v2.csv` still points at
`styra.md` or `whylabs.md`; remaining mentions are intentional historical plain text on
`open-policy-agent`, `policy-as-code` and `authorization-engine`, plus `log.md` and
`migration-report.md` history.

## [2026-07-27] decision | slug rename bedrock-security → bedrock-data
Human confirmed the rename deferred earlier today. Per the slug convention (vendor slug =
the company's current name) and the `conductorone → c1` / `normalyze → proofpoint-dspm`
precedents, `wiki/vendors/bedrock-security.md` → `wiki/vendors/bedrock-data.md` (git mv,
history preserved); frontmatter `slug: bedrock-data`, `aka: [Bedrock Security, Bedrock Labs]`
kept so the former name stays searchable. Mechanical only — no facts changed: the 2025-08-05
rebrand (brand change, legal entity still Bedrock Labs, Inc.) was already verified and written
up in today's research entry.
Inbound links updated in `wiki/categories/dspm.md` and vendors `rubrik`, `wiz`,
`symmetry-systems`, `teleskope`, `proofpoint-dspm`, `collibra`, `immuta` (immuta was **not**
on the originally-flagged list — caught by a repo-wide grep). `survey-v2.csv` Wiki URL →
`.../bedrock-data.md`; the survey option text already read "Bedrock Data (formerly Bedrock
Security)" and is unchanged. `taxonomy.yaml`/`taxonomy.md` needed no edit — they reference the
display name ("Bedrock Data (ex-Bedrock Security)"), not the slug. Page banner and Open-
questions flag rewritten from "pending decision" to "done"; History line added. `index.md`
regenerated. Intentionally left pointing at the old string: the cached source filename
`raw/sources/2026-07-27--bedrock-security--rebrand-to-bedrock-data.md` (raw/ is immutable),
the vendor's own press-release URL, and prior `log.md` history.
