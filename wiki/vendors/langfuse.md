---
type: vendor
name: Langfuse
slug: langfuse
categories: [llm-observability]
layer: model-prompt
aliases: []
website: https://langfuse.com
founded: 2022
hq: Berlin, Germany (+ San Francisco)
ownership: acquired
ownership_detail: "Acquired by ClickHouse, Inc. (announced 2026-01-26); operates within ClickHouse, core remains open source"
ownership_confidence: high
funding_total: "~$4.5M pre-acquisition (Lightspeed, La Famiglia; also backed by Y Combinator, General Catalyst)"
last_funding: "Seed (pre-acquisition); acquired by ClickHouse 2026-01"
deployment: [saas, self-hosted, sdk, api]
target_customer: "developers / engineering teams; enterprise (19 Fortune 50, 63 Fortune 500 cited)"
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, observability, evals, yc-w23]
---

# Langfuse

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — Open-source LLM engineering platform for tracing, evaluating, and managing prompts of AI apps; now owned by ClickHouse.

**What it does** — Langfuse instruments an LLM/agent application and records every step (calls, tool use, latency, token cost) as traces. On top of that it offers evals (LLM-as-a-judge + custom scores), prompt management/versioning, a playground, and datasets for regression testing. It is the open-source default many teams reach for to answer "what did my agent actually do, what did it cost, and is output quality regressing?" Self-host the whole stack or use Langfuse Cloud.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer of the AI model/prompt tier. This is a development- and operations-time visibility tool, not an inline control: it does not by itself break any leg of the lethal trifecta (untrusted input / sensitive data / egress), though traces help you detect prompt-injection or data-leak incidents after the fact. Lives alongside (and downstream of) the [ai-gateway](../categories/ai-gateway.md) and [ai-runtime-security](../categories/ai-runtime-security.md) controls.

**Deployment & architecture** — SDK/OpenTelemetry-based instrumentation (Python, JS/TS) plus integrations with LangChain, the OpenAI SDK, [litellm](litellm.md), and others. Backed by ClickHouse for trace storage (the reason for the acquisition — "LLM observability is fundamentally a data problem"). Fully self-hostable (MIT-licensed core) or SaaS. Integrates into CI for eval gating.

**Positioning & differentiators** — Strongest open-source community position in the category, OpenTelemetry-native, broad framework-agnostic instrumentation. Versus [langsmith](langsmith.md) (tied to the LangChain ecosystem, closed-source) Langfuse is framework-neutral and self-hostable; versus [arize-phoenix](arize-phoenix.md) it overlaps heavily on OSS tracing/evals; versus [helicone](helicone.md) it is SDK/OTel-based rather than proxy-based; versus [braintrust](braintrust.md) it is open-source and observability-first rather than eval-first.

**Ownership, funding & M&A** — **Acquired by ClickHouse, Inc., announced 2026-01-26** (confirmed via deal-counsel announcement; terms undisclosed). Langfuse continues as an open-source product inside ClickHouse, pitched as part of a combined open-source build/monitor/optimize stack. Founded 2022 (YC W23) by Max Deichmann, Clemens Rawert, Marc Klingen; HQ Berlin with SF presence. Pre-acquisition funding modest (~$4.5M reported; backers Lightspeed, La Famiglia, General Catalyst, YC). Confidence: high on the acquisition fact and date.

**CTO / hedge-fund lens** — Day-1 if you are building or buying any internal LLM/agent app and want cost + quality visibility without a Datadog-scale contract. The self-host option is attractive for a fund that wants traces (which may contain prompts/MNPI-adjacent content) to stay inside its own boundary. ClickHouse ownership lowers vendor-continuity risk versus a tiny startup. Not a model-risk/SR 11-7 governance tool on its own — pair with an [ai-governance-platform](../categories/ai-governance-platform.md) for that.

**Competitors / alternatives** — [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [helicone](helicone.md), [datadog](datadog.md), [comet](comet.md).

**Open questions / to verify**
- Exact acquisition price (undisclosed).
- Whether Langfuse Cloud pricing/SLAs change under ClickHouse.
- Reconcile founding year (2022 per founders/YC W23 vs "2023" cited in acquisition release).

## Sources
- [Langfuse Acquired by ClickHouse, Inc. (Orrick deal announcement)](https://www.orrick.com/en/News/2026/01/Open-source-LLM-Observability-Langfuse-Acquired-by-ClickHouse-Inc) — fetched 2026-06-28 — supports: acquisition by ClickHouse, date 2026-01-26, open-source continuity, customer/funding background; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Langfuse acquired by ClickHouse (2026-01-26, confirmed) — changed `ownership` independent→acquired, confidence low→high; filled founding (2022, YC W23), Berlin HQ, OSS deployment, funding. No seed M&A flag existed but acquisition found and recorded.
