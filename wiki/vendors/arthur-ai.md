---
type: vendor
name: Arthur AI
slug: arthur-ai
categories: [llm-observability, ai-governance-platform]
layer: model-prompt
aliases: [Arthur]
website: https://www.arthur.ai
founded: 2018
hq: New York City, New York, USA
ownership: independent
ownership_detail: Independent, VC-backed. ~$63M total raised; $42M Series B (Sept 2022, Acrew Capital + Greycroft).
ownership_confidence: high
funding_total: ~$63M
last_funding: Series B, $42M, 2022-09
deployment: [saas, self-hosted, on-prem, api, sdk]
target_customer: enterprise / regulated (financial services, government)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [observability, model-monitoring, explainability, guardrails, governance, agents]
---

# Arthur AI

> Researched 2026-06-28. Primary category: [llm-observability](../categories/llm-observability.md); also [ai-governance-platform](../categories/ai-governance-platform.md).

**One-liner** — An enterprise AI monitoring and governance platform that evaluates, monitors, and guardrails ML models, LLMs, and agents in production.

**What it does** — Arthur began as a model-monitoring platform — tracking performance, data drift, bias/fairness, and explainability across tabular, computer-vision, NLP, and (later) LLM models. It has repositioned around agents: continuous evaluations across the lifecycle, agent discovery and governance (find agents, enforce policy, keep oversight), and built-in guardrails (a "firewall") to block misuse and off-brand outputs. The CTO pitch is one control plane to ship reliable AI agents and prove they behave.

**Where it sits in the stack** — Primarily [llm-observability](../categories/llm-observability.md) (model/prompt layer) with a clear [ai-governance-platform](../categories/ai-governance-platform.md) story (policy, oversight, audit). Its guardrails touch the **untrusted-input** leg of the lethal trifecta; the platform is observe-evaluate-and-govern first, with inline guardrailing as a feature rather than a dedicated [ai-runtime-security](../categories/ai-runtime-security.md) firewall.

**Deployment & architecture** — SDK/API instrumentation feeding a platform deployable as SaaS, **on-premises**, or via GCP/AWS marketplace — the strong self-hosted option matters for regulated buyers who won't send model traffic to a vendor cloud. Maintains open source: **Arthur Engine** (GitHub `arthur-ai/arthur-engine`) and previously Arthur Bench (LLM eval benchmark).

**Positioning & differentiators** — The closest analogue to [fiddler-ai](fiddler-ai.md) — both are NYC/Bay-area enterprise platforms born from ML monitoring + explainability + bias detection, both pivoting to agents/governance, both with serious on-prem stories for regulated customers. Differs from developer-first OSS tracers ([langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [trulens](trulens.md)) by leading with enterprise governance and an open-source guardrails engine. Differs from pure red-teaming/eval tools ([giskard](giskard.md), [patronus-ai](patronus-ai.md)) by centering production monitoring.

**Ownership, funding & M&A** — Independent and VC-backed. Founded 2018, HQ New York City. Raised a $3.3M seed at launch and a **$42M Series B in September 2022** led by Acrew Capital and Greycroft, with Index Ventures and Work-Bench; ~$63M total. No M&A. (confidence: high)

**CTO / hedge-fund lens** — Day-1-ish for shops running production AI that needs monitoring + governance evidence. The bias/explainability/audit heritage maps well to **SR 11-7 / model-risk** expectations, and the on-prem option suits a fund unwilling to route model traffic externally. For a small fund it's likely heavier than an OSS tracer; it fits mid-market-to-enterprise with a formal model-risk or compliance function. The OSS Arthur Engine is a low-commitment way to trial the guardrails/eval piece.

**Competitors / alternatives** — [fiddler-ai](fiddler-ai.md), [arize-phoenix](arize-phoenix.md), [whylabs](whylabs.md) (wound down), [langfuse](langfuse.md), [braintrust](braintrust.md), [giskard](giskard.md), [datadog](datadog.md).

**Open questions / to verify**
- Any funding/ownership changes since the 2022 Series B (no later round confirmed).
- How the Arthur guardrails/firewall compares on latency/coverage with dedicated [ai-runtime-security](../categories/ai-runtime-security.md) vendors.

## Sources
- [Arthur AI homepage](https://www.arthur.ai/) — fetched 2026-06-28 — supports: current product scope, deployment, Arthur Engine OSS; confidence: med (vendor/marketing).
- [Arthur.ai gathers steam with $42M investment (TechCrunch, 2022-09-27)](https://techcrunch.com/2022/09/27/arthur-ais-machine-learning-monitoring-gathering-steam-with-42m-investment/) — fetched 2026-06-28 — supports: Series B, investors, ML-monitoring heritage; confidence: high.
- [Arthur — Crunchbase](https://www.crunchbase.com/organization/arthur-ai) — fetched 2026-06-28 — supports: founding year, ~$63M total; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (~$63M total, $42M Series B 2022), founded 2018 NYC. Set ownership_confidence high. ML-monitoring/explainability heritage pivoting to agent governance + OSS Arthur Engine. No M&A.
