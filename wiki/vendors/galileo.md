---
type: vendor
name: Galileo
slug: galileo
categories: [ai-red-teaming, llm-observability]
layer: model-prompt
aliases: [Galileo Technologies, Rungalileo, galileo.ai]
website: https://galileo.ai
founded: 2021
hq: San Francisco, California, USA
ownership: acquired
ownership_detail: "Acquired by Cisco — intent announced 2026-04-09; secondary press reports completion 2026-05-22 (Cisco said expected close Q4 FY2026). Folding into Splunk Observability. Terms undisclosed. Prior: independent, ~$68M raised."
ownership_confidence: medium
funding_total: ~$68M (pre-acquisition)
last_funding: Series B $45M (2024-10), led by Scale Venture Partners
deployment: [saas, api, sdk]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [llm-eval, observability, guardrails, cisco]
---

# Galileo

> Primary category: [ai-red-teaming](../categories/ai-red-teaming.md) (with heavy [llm-observability](../categories/llm-observability.md) overlap). Acquired by [cisco](cisco.md), folding into Splunk Observability.

**One-liner** — An AI/agent **evaluation and observability** platform that measures LLM/agent output quality, catches failures (hallucination, bias, unsafe output) before they reach users, and enforces real-time guardrails across the agent development lifecycle.

**What it does** — Galileo instruments the full **agent development lifecycle (ADLC)** — prompt optimization, model selection, offline evaluation, and production monitoring — and adds **real-time guardrails** for multi-agent systems. It scores responses for quality, hallucination, bias, safety and cost, so teams can both *evaluate* models pre-deployment and *watch* them in production. It straddles two jobs: evaluation/guardrails (red-teaming-adjacent) and observability (tracing/monitoring AI apps).

**Where it sits in the stack** — Primary [ai-red-teaming](../categories/ai-red-teaming.md)/guardrails with a strong [llm-observability](../categories/llm-observability.md) leg at the model/prompt layer. Trifecta role: mainly **untrusted-input** (guardrails catching jailbreaks/unsafe prompts and outputs); its bigger contribution is **trust/quality assurance** rather than blocking egress. Adjacent to [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [langfuse](langfuse.md), [braintrust](braintrust.md) (observability/eval) and [patronus-ai](patronus-ai.md), [lakera](lakera.md), [promptfoo](promptfoo.md) (eval/red-teaming).

**Deployment & architecture** — SaaS with SDK/API instrumentation dropped into the AI app/agent pipeline; supports offline eval and live production monitoring. Post-acquisition, Cisco is integrating Galileo into **Splunk Observability Cloud**, extending Splunk's AI Agent Monitoring across the full ADLC with guardrails.

**Positioning & differentiators** — Known for "evaluation intelligence" — quantitative eval metrics for GenAI teams — and for moving from pure eval into runtime guardrails. Backed pre-acquisition by strategic investors (Databricks, ServiceNow, SentinelOne, Citi/Amex Ventures). Differentiates from pure observability tools by bundling evaluation + guardrails; from pure red-teamers by the production-monitoring side. Note: distinct from the unrelated "Galileo AI" UI-design tool acquired by Google.

## Ownership, funding & M&A

**Acquired by [cisco](cisco.md)**. Galileo (Galileo Technologies, Inc. / galileo.ai; formerly Rungalileo) was founded **2021** in San Francisco by **Vikram Chatterji** (CEO), **Atindriyo Sanyal** and **Yash Sheth**, and raised **~$68M**, including a **$45M Series B (2024-10) led by Scale Venture Partners**. Cisco **announced intent 2026-04-09**; secondary press (Network World, Channel Insider) reports the deal **completed 2026-05-22**, while Cisco's own note said expected close in Q4 FY2026. Intent is high confidence; the exact **close date is medium** (no Cisco closing PR located). Terms undisclosed.

## CTO / hedge-fund lens

**Day-2** for most funds: you need this once you're building or seriously evaluating LLM/agent applications and want quantitative quality/safety signals plus production monitoring. The evaluation output is genuinely useful **SR 11-7 / model-risk evidence** — documented, repeatable testing of model behavior over time. For a Splunk shop the integration is the draw; standalone, weigh it against [arize-phoenix](arize-phoenix.md), [langsmith](langsmith.md), [braintrust](braintrust.md) (eval/observability) and [patronus-ai](patronus-ai.md) (eval). If you're not yet building AI apps, it's premature.

## Competitors / alternatives

[langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [langfuse](langfuse.md), [braintrust](braintrust.md), [patronus-ai](patronus-ai.md), [maxim-ai](maxim-ai.md), [lakera](lakera.md), [promptfoo](promptfoo.md).

## Open questions / to verify

- Confirm the Cisco **close date** with a primary (intent + secondary close found).
- Standalone product/pricing continuity post-Splunk integration.

## Sources
- [Cisco Blogs — Cisco Announces Intent to Acquire Galileo](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) — fetched 2026-06-28 — supports: intent 2026-04-09, AI observability/eval/guardrails, into Splunk Observability; confidence: high
- [Galileo Raises $45M Series B (PRNewswire)](https://www.prnewswire.com/news-releases/galileo-raises-45m-series-b-funding-to-bring-evaluation-intelligence-to-generative-ai-teams-everywhere-302276383.html) — fetched 2026-06-28 — supports: Series B $45M (Oct 2024), founders, ~$68M total, SF/2021; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Cisco acquisition of Galileo (intent 2026-04-09; reported closed 2026-05-22). Galileo = AI eval/observability + guardrails (galileo.ai / formerly Rungalileo), founded 2021 SF, ~$68M raised. Distinguished from Google's unrelated "Galileo AI". ownership=acquired, confidence medium on close date.
