# SCHEMA.md — Page Schema & Lint Spec (v2)

The definitive spec for wiki pages: (1) the questions every **category page** and
**vendor page** must answer, (2) controlled vocabularies so answers are comparable
and lintable, and (3) lint rules enforced by the `wiki-lint` skill. Audience for
the wiki itself: hedge fund / asset manager CTOs (the AITEC survey).

Companion files:
- **`taxonomy.yaml`** — machine source of truth for category slugs, layers,
  adoption tiers, adjacency, and all vocab enums. `taxonomy.md` is regenerated
  from it (`scripts/gen_taxonomy_md.py`); never edit `taxonomy.md` by hand.
- **`survey-v2.csv`** — canonical survey list; the CSV↔wiki bijection is linted.
- Skills: `.claude/skills/wiki-create`, `wiki-research`, `wiki-lint`.
- History: promoted from `draft.md`, 2026-07-05 (see `log.md`).

---

## 0. Lethal-trifecta policy

The lethal trifecta (untrusted input + access to sensitive data + external
egress in one agent context) is the **core agent-security threat model** — and
it is discussed **only** where agent security is specifically in play:

- **In scope:** category pages with `agent_security_context: true` in
  `taxonomy.yaml` (currently: ai-runtime-security, agent-runtime-security,
  mcp-gateway, authorization-engine, tool-identity-integration,
  enterprise-browser, browser-security-extension, trust-zone-segmentation),
  vendor pages whose `primary_category` is one of those, and `wiki/overview.md`
  (where it frames the agent-security portion of the thesis).
- **Out of scope:** everywhere else. No per-page `trifecta_*` frontmatter
  fields exist in schema v2. On non-agent-security pages, describe risk in
  plain terms (what the product inspects, blocks, or governs) instead of
  trifecta framing. Editorial lint rule 18 flags violations.

---

## 1. Category pages — questions to always answer

### 1.1 Definition & scope
- **One-sentence job-to-be-done.** What problem does this category solve, in buyer language?
- **Business objective.** Extended discussion of what it does, how it fits into the landscape, and the threat/risk it mitigates (data loss, compliance, supply chain…). *Agent-security categories only:* which leg(s) of the lethal trifecta it cuts.
- **In scope / out of scope.** Explicitly name the adjacent thing this is NOT (e.g., Comms Surveillance ≠ capture/archival; AI Red Teaming (offensive testing) vs. runtime guardrails).
- **Framework mapping.** Where it lands in OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF — one line each, for CISO-facing credibility.

### 1.2 Adoption tier & triggers
- **Tier** (vocab §3.1): `day-1` | `day-2` | `situational` | `firm-type-specific` | `practice`
- **Trigger condition.** The deployment pattern that makes it relevant:
  - Entitlement-aware RAG → only if you do RAG over internal permissioned data
  - MCP gateway / agent authz / NHI governance → only once agents hold credentials and call tools
  - Comms surveillance → registered advisers / regulated comms
  - Model risk (SR 11-7 flavor) → bank-affiliated or model-validation-mandated firms
- **Maturity-model mapping.** Which Crawl/Walk/Run/Fly stage first requires it, and which stage makes it table stakes.
- **Firm-type applicability.** Hedge fund vs. long-only vs. PE vs. bank-affiliated; small (<200) vs. large; Microsoft-shop vs. best-of-breed.

### 1.3 Sourcing posture
- **Buy / build / free / already-covered.** Standalone purchase, module of an incumbent (SASE AI Guard, Purview, GitHub Advanced Security), credible OSS self-host (LiteLLM, OPA, NeMo Guardrails), or absorbed by a platform bundle?
- **"Feature vs. company" risk.** Will this category survive as standalone products, or is it being absorbed? Cite the acquisition pattern as evidence.
- **Incumbent coverage check.** "If you own Zscaler/Netskope/Palo Alto/Microsoft E5, you may already have X" — say it explicitly per category. Conversely: if you own X, you still need this for these gaps.

### 1.4 Market structure
- **Category maturity** (vocab §3.5): `nascent` | `growth` | `consolidating` | `mature`
- **Consolidation ledger.** Who bought whom (dates, announced vs. closed), and what that implies for shortlists.
- **Overlap map.** Adjacent categories + which vendors are cross-listed and why (Cyera: DSPM + DLP + DAG; Prisma AIRS: runtime + AI-SPM + gateway + browser). One canonical table per page.

### 1.5 Selection guidance
- **Evaluation checklist.** 5–10 capability questions a CTO should ask in a POC (deployment model, inline vs. out-of-band, latency budget, IdP/SIEM integration, agent/MCP support, data residency).
- **Decision tree / archetype guidance.** "If you are X kind of firm with Y stack, start with Z." (The highest-value editorial content — everything else supports it.)
- **Procurement notes.** Typical pricing motion (per-seat, per-token/usage, platform bundle) and rough magnitude band if known.
- **What happens if you skip it.** Concrete failure scenario, ideally a real incident.

### 1.6 Hygiene
- Last-verified date, open questions, and survey linkage (which survey question this page backs).

---

## 2. Vendor pages — questions to always answer

### 2.1 Identity & classification
- **One-liner:** what it does, for whom.
- **Primary category** + cross-listed categories (must match the CSV; one canonical page per vendor).
- **Naming/provenance:** founding year, renames (Fairly AI → Asenion), product renames post-acquisition (CalypsoAI → F5 AI Guardrails, Pangea → Falcon AIDR, Portkey → Prisma AIRS gateway), disambiguation notes (M365 Copilot vs. GitHub/Windows Copilot; Holistic AI vs. Paris "H").

### 2.2 Ownership & viability (the most churn-prone section)
- **Ownership state** (vocab §3.2): public (ticker) | pe-owned (sponsor) | independent (stage, last round, amount, date) | acquired (acquirer, price, **announced vs. closed dates**) | acquisition-pending (verify-by date) | OSS (license, foundation, who employs maintainers).
- **Viability signals:** funding runway/stage, headcount trend if visible, maintenance-mode flags (Helicone), key-person/steward risk (OPA post-Styra), "acquired and shelved vs. acquired and invested" judgment.
- **Acquisition-risk note** for independents: potential acquirers, and what happens to customers if it exits (contract, roadmap, on-prem continuity).

### 2.3 Market position & differentiation
- **Position label** (vocab §3.3) plus one sentence justifying it; a vendor may hold different positions in different categories.
- **Key differentiators:** 2–4 bullets vs. named category peers (not vs. the abstract category). "Lineage-based vs. content-detection DLP" is the model.
- **Who should choose them** (ideal buyer profile) and — equally important — **who should not** (anti-fit).
- **Known weaknesses / gotchas**, stated plainly: OpenRouter = hosted aggregator, data leaves tenancy; Perplexity = weak comms archival for regulated shops. CSV flag-notes graduate into this standing section.

### 2.4 Deployment & data handling (decisive for this audience)
- **Deployment model** (vocab §3.4) and **form factor** (vocab §3.6); single-tenant option?
- **Does data leave the tenancy?** Prompts, embeddings, logs, telemetry — where do they go, retention, training-use policy.
- **Inline vs. out-of-band** (for runtime/gateway/DLP products) and latency implications.

### 2.5 Integrations & partnerships
- **Upstream/downstream integrations:** gateways ↔ observability (Portkey ↔ Langfuse), guardrails ↔ gateways, SIEM export targets, IdP support (Entra/Okta), EDR/SASE hooks, cloud marketplaces (AWS/Azure/GCP listing = procurement shortcut).
- **Agent-era support:** MCP support (client/server/gateway), agent framework integrations (LangGraph, Claude Agent SDK, etc.), OpenAI/Anthropic/Bedrock/Vertex coverage.
- **Named partnerships / reseller channels** relevant to FS buyers.

### 2.6 Compliance & FS traction
- **Certifications:** SOC 2 Type II, ISO 27001, ISO 42001, FedRAMP where relevant.
- **Financial-services evidence:** named FS customers or case studies, hedge-fund-scale fit (does it assume 10k seats?), audit/exam-readiness features (evidence export, retention).

### 2.7 Commercial
- **Pricing model** (seat/usage/platform/OSS+support) and rough band if public or community-sourced; free tier / OSS core vs. enterprise gating.

### 2.8 Hygiene
- **Sources** (dated links for every load-bearing claim, esp. M&A) and **last-verified date**.
- **Open questions** — explicit "unverified" list rather than silent gaps.

---

## 3. Controlled vocabularies

Authoritative enum values live in the `vocab:` block of **`taxonomy.yaml`**;
lint validates against that file, not this prose. Summary + rules:

### 3.1 `adoption_tier`
`day-1` (table stakes before any AI in production) · `day-2` (required once scaling/agents) · `situational` (depends on deployment pattern; must state trigger) · `firm-type-specific` (must state firm type) · `practice` (a process, not a purchase — no survey scaffolding)

### 3.2 `ownership_state`
`public` · `pe-owned` · `independent` · `acquired-closed` · `acquired-pending` · `oss-foundation` · `oss-vendor-backed` · `maintenance-mode` · `defunct`
Rules: `acquired-*` requires acquirer + announced date; `acquired-closed` additionally requires close date; `acquired-pending` requires a `verify_after` date.

### 3.3 `market_position`
`leader` · `challenger` · `legacy-incumbent` · `ai-native-disruptor` · `platform-module` · `oss-default` · `niche-specialist`
Rule: label must be justified in one sentence on the page; per-category labels allowed (Cloudflare: leader in SASE, challenger in AI gateway).

### 3.4 `deployment_model`
`saas` · `self-hosted` · `hybrid` · `in-tenant` · `on-prem` (multi-valued)

### 3.5 `category_maturity`
`nascent` · `growth` · `consolidating` · `mature`

### 3.6 `form_factor` (v2 extension)
`inline-proxy` · `api` · `sdk` · `agent` · `browser-extension` · `platform` (multi-valued) — how the product is consumed, orthogonal to where it runs.

### 3.7 `mcp_support`
`none` · `client` · `server` · `gateway` · `unverified`

---

## 4. Front-matter schemas

Fields beyond the draft spec kept for tooling compatibility: `title` (Quartz
page title — required on every page), `type` (vendor|category|comparison|overview),
`slug`, and the identity fields `website`, `founded`, `hq`, `tags`.
Confidence lives per-source (in `sources:`), not as a page-level field.

### Vendor page YAML

```yaml
---
title: Portkey
type: vendor
name: Portkey
slug: portkey
aka: [Prisma AIRS AI Gateway]
primary_category: ai-gateway          # canonical slug from taxonomy.yaml
also_listed_in: []
website: "https://portkey.ai"
founded: 2023
hq: San Francisco, California, USA
ownership_state: acquired-closed
owner: Palo Alto Networks
acquisition: {announced: 2025-12-01, closed: 2026-05-29, price: null}
market_position: {ai-gateway: challenger}
deployment_model: [saas, self-hosted]
form_factor: [inline-proxy, api]
data_leaves_tenancy: "false"          # "true" / "false" / partial / unverified — explain in body
integrations: [langfuse, litellm-compat, entra, okta, splunk]
mcp_support: gateway
certifications: [soc2-type2]
pricing_model: usage
fs_traction: unverified
last_verified: 2026-07-05
verify_after: null                    # required if ownership_state: acquired-pending
tags: []
sources:
  - {claim: acquisition-close, url: "...", date: 2026-05-29, confidence: high}
---
```

### Category page YAML

```yaml
---
title: AI Gateway
type: category
name: AI Gateway
slug: ai-gateway
category: ai-gateway
layer: model-prompt                   # from taxonomy.yaml
survey_question: "AI Gateway"         # null for practice / doc-only categories
adoption_tier: day-1
trigger: "any LLM API traffic beyond a single vendor SDK"
maturity_stage_required: walk         # crawl | walk | run | fly (null until assessed)
category_maturity: consolidating
adjacent: [llm-observability, ai-runtime-security, mcp-gateway]
incumbent_coverage: [cloudflare, f5, palo-alto-networks]
maps_to_seed_doc: "AI Gateway"        # provenance, optional
maps_to_seed_csv: "AI Gateway"        # provenance, optional
last_verified: 2026-07-05
---
```

Null/`unverified` values are legal — they mean "not yet researched" and feed
the research queue. They are never silently guessed.

---

## 5. Lint rules

### 5.1 Mechanical (`scripts/wiki_lint.py`, no LLM needed)
1. **CSV ↔ wiki bijection.** Every `survey-v2.csv` product row (excluding `Other (Please Specify)`) has a wiki page at its stated Wiki URL path; every vendor page maps to ≥1 CSV row or is flagged `orphan`.
2. **One canonical page per vendor.** Cross-listed vendors resolve to a single file; category pages link, never fork. No two files with near-duplicate `name`.
3. **Front-matter schema validation.** Required fields present; enum values in `taxonomy.yaml` vocab; dates ISO-8601; `primary_category`/`also_listed_in`/`category` values are canonical slugs.
4. **M&A state machine.** `acquired-pending` requires `verify_after`; if `verify_after` < today → flagged for re-research. `acquired-closed` requires close date + a source entry.
5. **Naming convention.** Acquired vendors rendered "X (Acquirer)" consistently in CSV and page titles; renames get `aka:` entries and a redirect/stub at the old slug.
6. **URL liveness + redirect detection** (`--online` flag). Vendor URLs that 404 or redirect to an acquirer domain → flag (early acquisition-integration signal).
7. **Staleness.** `last_verified` older than N days (60 for `acquired-pending`/independents in consolidating categories, 120 otherwise) → re-research queue.
8. **Dated-claim sourcing.** Any body sentence containing a date or dollar amount must have a source entry.
9. **CSV note ↔ page consistency.** Every CSV Flag/Note assertion appears on the page; contradiction → error.
10. **Cross-reference integrity.** Every `adjacent:`/`also_listed_in:` value and every relative markdown link resolves to an existing page.

### 5.2 Editorial (LLM-judged, in the `wiki-lint` skill)
11. **Required sections present and non-empty** per §1/§2 (a header with "TBD" counts as missing → goes to open-questions, not silently absent).
12. **Differentiation is comparative.** "Key differentiators" must name at least one category peer; generic marketing language ("comprehensive platform," "industry-leading") → flag.
13. **Anti-fit stated.** Every vendor page says who should NOT buy it. If the page can't, that's a research task.
14. **Announced ≠ closed language.** Prose must not say "acquired by" for pending deals; must say "acquisition announced."
15. **Tier justification.** Category `adoption_tier` must be defended by the trigger condition, not asserted.
16. **Scope-boundary line present** for categories with known confusion (comms surveillance vs. capture; red teaming vs. guardrails; AI-SPM vs. SSPM vs. shadow-AI; DSPM vs. DAG vs. DLP).
17. **No stale position labels.** If ownership changed since `market_position` was set (independent → platform-module post-acquisition), flag for re-label.
18. **Trifecta scoping (§0).** Lethal-trifecta framing on a page outside the `agent_security_context: true` set (or `wiki/overview.md`) → flag for rewrite in plain risk language. Any `trifecta_*` frontmatter key anywhere → error.

---

## 6. Research question bank (for the `wiki-research` skill's search loop)

Per vendor, in priority order:
1. Ownership/funding change since `last_verified`? (query: "<vendor> acquisition OR funding OR shutdown <year>")
2. Product rename or platform absorption?
3. New integrations/partnerships, esp. gateway↔observability↔guardrails pairings and MCP support?
4. FS customer evidence or case studies?
5. Deployment/data-residency changes (new self-hosted option, new region)?
6. Pricing/packaging changes?
7. Notable incidents, CVEs, or negative signal (layoffs, exec departures)?

Per category:
1. New entrants worth an "Other" write-in row?
2. New consolidation events changing the overlap map?
3. Analyst-framework changes (new Gartner/Forrester category naming) worth aligning terminology to?
4. Regulatory developments changing the adoption tier (SEC/FINRA guidance, EU AI Act milestones)?

---

## 7. Skill decomposition

- **`wiki-lint`** — runs §5.1 mechanically (`scripts/wiki_lint.py` over front-matter + CSV), then §5.2 via LLM pass; emits a triaged issue list (error / warn / research-needed) to `reports/`.
- **`wiki-research`** — takes the research-needed queue, runs the §6 question bank with web search, caches evidence to `raw/sources/`, updates pages + `last_verified` + sources.
- **`wiki-create`** — scaffolds new vendor/category pages from the §4 templates, pre-filled from the `survey-v2.csv` row, with all §1/§2 headers stubbed as open questions.
- All three validate against **`taxonomy.yaml`**.
