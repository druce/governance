---
type: vendor
name: TruLens
slug: trulens
categories: [llm-observability]
layer: model-prompt
aliases: [TruEra]
website: "https://www.trulens.org"
founded: 2021
hq: Redwood City, California, USA (TruEra; now part of Snowflake)
ownership: acquired
ownership_detail: Created by TruEra; Snowflake acquired the TruEra AI Observability platform (announced 2024-05-22). TruLens kept open source under Snowflake stewardship.
ownership_confidence: high
funding_total: n/a (TruLens is an OSS project; TruEra was VC-backed pre-acquisition — total not verified here)
last_funding: n/a (acquired by Snowflake 2024)
deployment: [sdk, self-hosted, api]
target_customer: developers / ML & GenAI engineering teams (esp. Snowflake users)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [observability, evaluation, open-source, rag, snowflake]
---

# TruLens

> Researched 2026-06-28. Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — An open-source Python library for evaluating and tracing LLM, RAG, and agent applications, now stewarded by Snowflake.

**What it does** — TruLens instruments an LLM/RAG/agent app and scores it with "feedback functions" — programmatic evaluators for things like context relevance, groundedness, and answer relevance (the "RAG triad"), plus toxicity, bias, and custom criteria. It records traces of each call and surfaces a local dashboard to compare app versions experiment-over-experiment. The job: measure whether your LLM app is actually correct/grounded before and after you ship, without hand-built eval harnesses.

**Where it sits in the stack** — [llm-observability](../categories/llm-observability.md) (model/prompt layer), specifically the **evaluation** sub-segment. Its groundedness/relevance checks touch the **untrusted-input** leg (catching hallucination/injection-driven bad outputs) but TruLens is a measurement/eval library, not an inline guardrail or firewall — it observes, it doesn't block.

**Deployment & architecture** — A pip-installable OSS SDK (Apache-licensed, GitHub `truera/trulens`) that runs in your own environment; feedback functions can call any model provider as the judge. Ships a Streamlit dashboard for local/self-hosted review. Integrates tightly with the Snowflake ecosystem (Cortex, Arctic, Streamlit) but works standalone with LangChain/LlamaIndex and arbitrary stacks.

**Positioning & differentiators** — Known as a developer-first, **open-source evaluation** library — lighter and more eval-focused than full hosted observability platforms. The productized, commercial version of this technology now lives inside Snowflake (Cortex AI Observability) rather than being sold as a separate "TruLens" product, so TruLens itself is best understood as the free OSS layer. Nearest neighbors: [arize-phoenix](arize-phoenix.md) (also OSS eval/tracing), [langfuse](langfuse.md) (OSS tracing + evals), [giskard](giskard.md) (OSS testing/red-teaming), [braintrust](braintrust.md) and [comet](comet.md) (Opik).

**Ownership, funding & M&A** — **M&A CONFIRMED.** TruLens was created by **TruEra**; **Snowflake** announced a definitive agreement to acquire the TruEra AI Observability platform on **2024-05-22** (primary source: Snowflake blog). TruEra co-founders Anupam Datta, Shayak Sen, and Will Uppington joined Snowflake. Snowflake publicly committed to keeping TruLens open source and now maintains it (adding parallelized feedback eval, LangChain compatibility, dashboard speedups). Deal terms not disclosed. (confidence: high)

> Seed flag "(Snowflake/TruEra)" verified: correct. TruLens is the OSS project; the company TruEra was acquired by Snowflake.

**CTO / hedge-fund lens** — Day-1 for any team building RAG/agent apps that wants a cheap, code-first way to prove output quality and groundedness — the OSS library has no license cost. Especially natural if your data already lives in **Snowflake**. It is an engineering tool, not a governance/audit platform: it gives you eval evidence but not the SR 11-7 reporting wrapper that [fiddler-ai](fiddler-ai.md) or [arthur-ai](arthur-ai.md) aim at. Good complement to, not replacement for, a governance layer.

**Competitors / alternatives** — [arize-phoenix](arize-phoenix.md), [langfuse](langfuse.md), [langsmith](langsmith.md), [giskard](giskard.md), [braintrust](braintrust.md), [comet](comet.md), [patronus-ai](patronus-ai.md).

**Open questions / to verify**
- Current degree of separation between the standalone OSS TruLens and Snowflake's commercial Cortex AI Observability offering.
- Whether Snowflake continues independent TruLens releases vs folding it into Cortex.

## Sources
- [Snowflake to Acquire TruEra AI Observability Platform](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/) — fetched 2026-06-28 — supports: acquirer, date (2024-05-22), founders; confidence: high (primary, acquirer).
- [TruLens ❤️ Snowflake OSS](https://www.snowflake.com/en/blog/trulens-open-source-ai/) — fetched 2026-06-28 — supports: OSS commitment, capabilities; confidence: high (primary).
- [truera/trulens (GitHub)](https://github.com/truera/trulens) — fetched 2026-06-28 — supports: OSS library, eval/tracing scope; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED Snowflake acquired TruEra (creators of TruLens), announced 2024-05-22; TruLens remains open source under Snowflake. Set ownership=acquired, confidence high. Seed flag verified correct.
