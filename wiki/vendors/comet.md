---
type: vendor
name: Comet (Opik)
slug: comet
categories: [llm-observability]
layer: model-prompt
aliases: [Comet ML, Opik]
website: https://www.comet.com
founded: 2017
hq: New York, NY
ownership: independent
ownership_detail: "Comet ML, Inc. — independent, VC-backed (~$70M raised, Series B led by OpenView). Opik is its open-source LLM eval product"
ownership_confidence: high
funding_total: "~$70M"
last_funding: "Series B (led by OpenView Venture Partners)"
deployment: [saas, self-hosted, sdk, api]
target_customer: "ML/AI engineering teams; enterprise (150+ customers incl. Netflix, Uber, Cisco)"
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, evals, observability, mlops]
---

# Comet (Opik)

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — Established MLOps vendor (Comet) whose open-source Opik product brings LLM tracing, evaluation, and monitoring.

**What it does** — Opik (launched 2024-09-17, Apache-2.0 OSS) records every step an LLM/agent app takes (tracing), runs built-in eval metrics and LLM judges (hallucination, factuality), supports "model unit testing" and scoring, and ships production dashboards. It sits on top of Comet's longer-standing platform for ML experiment management, model management, and production monitoring — so a buyer gets both classic MLOps and LLM observability from one vendor.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer of the model/prompt tier. Dev/CI- and ops-time tracing and eval; not an inline runtime guardrail, so it does not directly break a leg of the lethal trifecta. Complements [ai-red-teaming](../categories/ai-red-teaming.md) and [ai-runtime-security](../categories/ai-runtime-security.md).

**Deployment & architecture** — SDK-based instrumentation; Opik self-hostable via OSS (GitHub, ~19k+ stars, 40+ framework/provider integrations) or run on Comet's managed/enterprise platform with collaboration, user management, and security controls. Pairs naturally with Comet's experiment-tracking for teams that train/fine-tune as well as call APIs.

**Positioning & differentiators** — Differentiated by the MLOps lineage: useful if you also do traditional ML and want one platform spanning experiments → models → LLM evals. Opik's OSS + permissive license puts it alongside [langfuse](langfuse.md) and [arize-phoenix](arize-phoenix.md) on the open-source axis; versus eval-first [braintrust](braintrust.md) and proxy-based [helicone](helicone.md) it is SDK-based and observability+eval-oriented. The nearest direct comparison is W&B Weave ([weights-and-biases](weights-and-biases.md)) — both extend an incumbent ML-experiment platform into LLM observability.

**Ownership, funding & M&A** — Independent, VC-backed. Comet ML founded 2017; HQ New York; ~$70M raised (Series B led by OpenView; earlier seed rounds led by Trilogy Equity Partners). 150+ enterprise customers (Netflix, Uber, Cisco, Etsy, Zappos). No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 for a quant/ML-heavy fund that already trains models and wants LLM observability without adding a separate vendor — the unified MLOps + LLM story is the draw. Opik OSS self-hosting keeps traces (potential MNPI) in-boundary. Smaller/older funding base than the hottest LLM-native startups, but the company is well-established with real enterprise traction. Not a governance/SR 11-7 system itself — pair with [ai-governance-platform](../categories/ai-governance-platform.md).

**Competitors / alternatives** — [langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [langsmith](langsmith.md), [helicone](helicone.md), [datadog](datadog.md), [weights-and-biases](weights-and-biases.md).

**Open questions / to verify**
- Exact latest funding round size/date (only "~$70M total, Series B led by OpenView" confirmed).
- Opik OSS vs Comet-managed feature boundary.

## Sources
- [Comet Launches Opik, an Open Source LLM Evaluation Platform (Comet press release)](https://www.comet.com/site/about-us/news-and-events/press-releases/comet-launches-opik/) — fetched 2026-06-28 — supports: Opik launch 2024-09-17, OSS, Comet founding/HQ/funding/customers, core MLOps platform; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (Comet ML, ~$70M, Series B OpenView), established Opik (OSS LLM eval, launched 2024-09) vs core MLOps platform, filled founding/HQ/deployment. No M&A. `ownership_confidence` low→high.
