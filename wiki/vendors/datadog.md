---
type: vendor
name: Datadog LLM Observability
slug: datadog
categories: [llm-observability]
layer: model-prompt
aliases: [Datadog, DDOG]
website: "https://www.datadoghq.com/product/ai/llm-observability/"
founded: 2010
hq: New York, NY
ownership: public
ownership_detail: "Datadog, Inc. — public (NASDAQ: DDOG). LLM Observability is one module of its platform; GA 2024-06-26"
ownership_confidence: high
funding_total: "public company (IPO 2019)"
last_funding: "n/a (public)"
deployment: [saas, sdk, api]
target_customer: "existing Datadog enterprise customers; mid-market to large enterprise"
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [observability, apm, enterprise, public-company]
---

# Datadog LLM Observability

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — The LLM/agent observability module inside Datadog's broader monitoring platform — buy it where you already run APM and logs.

**What it does** — End-to-end tracing of LLM and agent chains (root-cause errors and hallucinations), operational metrics (latency, token usage, cost), and out-of-the-box quality + safety evaluations (topic relevance, toxicity) plus sensitive-data scanning. Adds prompt/response clustering, datasets, experiments, a testing playground, offline + online evals, and human review/annotation — all stitched into Datadog APM and the rest of the Datadog platform. GA since 2024-06-26.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer of the model/prompt tier. Mostly dev/ops visibility, but its built-in sensitive-data scanning and safety evals give it a light touch on the **sensitive-data** leg of the lethal trifecta (detecting leakage in prompts/outputs). Not an inline firewall — complements [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-gateway](../categories/ai-gateway.md).

**Deployment & architecture** — SaaS only (Datadog's hosted platform); SDK/auto-instrumentation for OpenAI, Anthropic, Gemini, Vertex AI, Bedrock, LangChain, CrewAI, Pydantic, [litellm](litellm.md), Strands Agents, plus an MCP server. Its key differentiator is native correlation with existing Datadog APM traces, infra metrics, logs, and security signals.

**Positioning & differentiators** — The "single pane of glass" play: if you already run Datadog, LLM Observability is a module rather than a new vendor. Versus AI-native specialists ([langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [langsmith](langsmith.md)) it trades some depth/agility for unified correlation, enterprise procurement, and no extra vendor. SaaS-only (no self-host) is the main constraint for data-sensitive shops. (Datadog is also a strategic investor in [arize-phoenix](arize-phoenix.md).)

**Ownership, funding & M&A** — **Public company, NASDAQ: DDOG** (IPO 2019); founded 2010, HQ New York. LLM Observability is an organically built module, not an acquisition. Confidence: high.

**CTO / hedge-fund lens** — Day-1 and often the path of least resistance for a fund that **already standardizes on Datadog** — no new vendor review, unified ops, billing, and SOC integration. The catch: SaaS-only means prompts/outputs (potential MNPI) leave your boundary into Datadog, which a compliance team must bless; the built-in sensitive-data scanning helps but does not eliminate that. If you are not already a Datadog shop, an AI-native or self-hostable tool may fit better. Not a model-risk/SR 11-7 governance system itself — pair with [ai-governance-platform](../categories/ai-governance-platform.md).

**Competitors / alternatives** — [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [helicone](helicone.md), [comet](comet.md).

**Open questions / to verify**
- Any self-hosted/in-region data-residency option for regulated customers (appears SaaS-only).
- Pricing model for LLM Observability relative to core Datadog ingestion.

## Sources
- [Datadog LLM Observability Now Generally Available (Datadog IR press release)](https://datadog.gcs-web.com/news-releases/news-release-details/datadog-llm-observability-now-generally-available-help/) — fetched 2026-06-28 — supports: GA date 2024-06-26, feature set, sensitive-data scanning, integrations; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected `ownership` independent→public (NASDAQ: DDOG), confidence low→high; established LLM Observability as a GA module (2024-06) of the broader platform, SaaS-only, set hedge_fund_fit high (incumbency). No M&A.
