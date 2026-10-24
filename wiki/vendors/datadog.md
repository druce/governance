---
title: Datadog LLM Observability
type: vendor
name: Datadog LLM Observability
slug: datadog
aka: [Datadog, DDOG]
primary_category: llm-observability
also_listed_in: [siem-soc, ai-soc-analysts]
website: https://www.datadoghq.com/product/ai/llm-observability/
founded: 2010
hq: New York, NY
ownership_state: public
owner: null
ownership_note: 'Datadog, Inc. — public (NASDAQ: DDOG). LLM Observability is one module of its platform; GA 2024-06-26'
acquisition: {announced: null, closed: null, price: null}
funding_total: public company (IPO 2019)
last_funding: n/a (public)
market_position: {siem-soc: challenger, ai-soc-analysts: platform-module}
deployment_model: [saas]
form_factor: [sdk, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: existing Datadog enterprise customers; mid-market to large enterprise
last_verified: 2026-06-28
verify_after: null
tags: [observability, apm, enterprise, public-company, cloud-siem, ai-soc]
sources:
  - {claim: "LLM Observability GA 2024-06-26", url: "https://datadog.gcs-web.com/news-releases/news-release-details/datadog-llm-observability-now-generally-available-help/", date: 2026-06-28, confidence: high}
  - {claim: "Cloud SIEM: AI-driven threat detection and incident response on Datadog log management; 800+ detection rules, 1,000+ integrations; Bits AI Security Analyst investigates SIEM signals", url: "https://www.datadoghq.com/product/cloud-siem/", date: 2026-10-23, confidence: medium}
  - {claim: "Bits AI Security Analyst generally available for Cloud SIEM on 2026-03-23; autonomously triages/investigates alerts and returns explained verdicts (performance figures vendor-claimed)", url: "https://itbrief.co.uk/story/datadog-launches-ai-security-analyst-for-cloud-siem", date: 2026-10-23, confidence: medium}
---

# Datadog LLM Observability

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — The LLM/agent observability module inside Datadog's broader monitoring platform — buy it where you already run APM and logs.

**What it does** — End-to-end tracing of LLM and agent chains (root-cause errors and hallucinations), operational metrics (latency, token usage, cost), and out-of-the-box quality + safety evaluations (topic relevance, toxicity) plus sensitive-data scanning. Adds prompt/response clustering, datasets, experiments, a testing playground, offline + online evals, and human review/annotation — all stitched into Datadog APM and the rest of the Datadog platform. GA since 2024-06-26.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer of the model/prompt tier. Mostly dev/ops visibility, but its built-in sensitive-data scanning and safety evals help detect sensitive-data leakage in prompts/outputs. Not an inline firewall — complements [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-gateway](../categories/ai-gateway.md).

**Deployment & architecture** — SaaS only (Datadog's hosted platform); SDK/auto-instrumentation for OpenAI, Anthropic, Gemini, Vertex AI, Bedrock, LangChain, CrewAI, Pydantic, [litellm](litellm.md), Strands Agents, plus an MCP server. Its key differentiator is native correlation with existing Datadog APM traces, infra metrics, logs, and security signals.

**Positioning & differentiators** — The "single pane of glass" play: if you already run Datadog, LLM Observability is a module rather than a new vendor. Versus AI-native specialists ([langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [langsmith](langsmith.md)) it trades some depth/agility for unified correlation, enterprise procurement, and no extra vendor. SaaS-only (no self-host) is the main constraint for data-sensitive shops. (Datadog is also a strategic investor in [arize-phoenix](arize-phoenix.md).)

**Security operations: Cloud SIEM and Bits AI Security Analyst** (added 2026-10-23). Datadog also sells security products on the same platform. These are what survey respondents meant when they put "Datadog" under SIEM/Logging and "Datadog Bits Security Analyst" under AI SOC.
- **[Cloud SIEM](../categories/siem-soc.md)** runs threat detection and incident response on Datadog log management. It ships 800+ out-of-the-box detection rules and uses the same 1,000+ integrations. It is listed in Gartner Peer Insights' SIEM market. No 2025 SIEM Magic Quadrant placement was found (not ruled out).
- **Bits AI Security Analyst** became generally available on **2026-03-23**. It is an agent inside Cloud SIEM that triages and investigates alerts end to end (gathers evidence, correlates signals, decides on escalation) and returns explained verdicts. It draws on the infrastructure, identity, EDR and APM telemetry already in Datadog. This puts it in [ai-soc-analysts](../categories/ai-soc-analysts.md) as a **platform module**: it only investigates Cloud SIEM signals. Standalone AI SOC tools such as [dropzone-ai](dropzone-ai.md) or [prophet-security](prophet-security.md) work on top of any SIEM. Datadog's figures (investigations "as little as 30 seconds", MTTR cut by more than 90%, "up to 98%" faster) are **vendor claims**.
- **Who it fits:** a fund that already sends most logs to Datadog for ops. Cloud SIEM avoids running a second log pipeline. **Anti-fit:** a firm whose SIEM is [microsoft-sentinel](microsoft-sentinel.md) or [splunk](splunk.md) and staying there, because Bits AI Security Analyst does not run on other SIEMs. Data handling is the same as for Datadog generally: security logs leave your boundary into Datadog's SaaS.

**Ownership, funding & M&A** — **Public company, NASDAQ: DDOG** (IPO 2019); founded 2010, HQ New York. LLM Observability is an organically built module, not an acquisition. Confidence: high.

**CTO / hedge-fund lens** — Day-1 and often the path of least resistance for a fund that **already standardizes on Datadog** — no new vendor review, unified ops, billing, and SOC integration. The catch: SaaS-only means prompts/outputs (potential MNPI) leave your boundary into Datadog, which a compliance team must bless; the built-in sensitive-data scanning helps but does not eliminate that. If you are not already a Datadog shop, an AI-native or self-hostable tool may fit better. Not a model-risk/SR 11-7 governance system itself — pair with [ai-governance-platform](../categories/ai-governance-platform.md).

**Competitors / alternatives** — [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [helicone](helicone.md), [comet](comet.md).

**Open questions / to verify**
- Cloud SIEM pricing model (ingest vs. indexed vs. per-signal) and whether Bits AI Security Analyst is priced separately.
- Gartner SIEM MQ / Forrester placement for Datadog Cloud SIEM.
- Any self-hosted/in-region data-residency option for regulated customers (appears SaaS-only).
- Pricing model for LLM Observability relative to core Datadog ingestion.

## Sources
- [Datadog LLM Observability Now Generally Available (Datadog IR press release)](https://datadog.gcs-web.com/news-releases/news-release-details/datadog-llm-observability-now-generally-available-help/) — fetched 2026-06-28 — supports: GA date 2024-06-26, feature set, sensitive-data scanning, integrations; confidence: high.

- [Datadog Cloud SIEM product page](https://www.datadoghq.com/product/cloud-siem/) — fetched 2026-10-23 — supports: Cloud SIEM scope, 800+ rules, Bits AI Security Analyst role; confidence: medium (marketing). Cached: `raw/sources/2026-10-23--datadog--cloud-siem-bits-ai-security-analyst.md`
- [Datadog launches AI security analyst for Cloud SIEM (IT Brief UK, 2026-03-23)](https://itbrief.co.uk/story/datadog-launches-ai-security-analyst-for-cloud-siem) — fetched 2026-10-23 — supports: GA date, functions, vendor performance claims; confidence: medium. (Datadog IR release at investors.datadoghq.com returned 403.)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected `ownership` independent→public (NASDAQ: DDOG), confidence low→high; established LLM Observability as a GA module (2024-06) of the broader platform, SaaS-only, set hedge_fund_fit high (incumbency). No M&A.
- [2026-10-23] Cross-listed in siem-soc (Cloud SIEM) and ai-soc-analysts (Bits AI Security Analyst, GA 2026-03-23) after Oct-2026 CTO survey write-ins ("Datadog" under SIEM/Logging, being implemented; "Datadog Bits Security Analyst" under AI SOC, 1 in production). Added frontmatter `sources:` and per-category market_position. Primary category unchanged (llm-observability).
