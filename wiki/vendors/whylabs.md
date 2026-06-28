---
title: WhyLabs
type: vendor
name: WhyLabs
slug: whylabs
categories: [llm-observability]
layer: model-prompt
aliases: [WhyLabs AI Observatory, WhyLogs]
website: "https://whylabs.ai"
founded: 2019
hq: Seattle, Washington, USA
ownership: acquired
ownership_detail: Acquired by Apple in 2025 (under-the-radar acqui-hire; founders joined Apple). Standalone product discontinued; platform open-sourced.
ownership_confidence: medium
funding_total: ~$14M
last_funding: Series A, $10M, 2021
deployment: [saas, sdk, self-hosted, api]
target_customer: ML/data engineering teams (historically); product now wound down
hedge_fund_fit: low
priority: day-1
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [observability, model-monitoring, data-monitoring, open-source, wound-down]
---

# WhyLabs

> Researched 2026-06-28. Primary category: [llm-observability](../categories/llm-observability.md). **Note: product effectively wound down after Apple acquisition (2025).**

**One-liner** — A data-and-ML monitoring / AI observability platform (now acquired by Apple and discontinued as a standalone product).

**What it does** — WhyLabs let teams monitor data pipelines and ML models at scale — detecting data drift, data-quality problems, and model performance degradation — built around its open-source `whylogs` data-logging library that computes lightweight statistical profiles without moving raw data. It later added LangKit (LLM metrics) and real-time GenAI security/quality monitoring (toxicity, hallucination, prompt-injection signals).

**Where it sits in the stack** — [llm-observability](../categories/llm-observability.md) (model/prompt layer), with strong roots in data/ML monitoring. The GenAI monitoring touched the **untrusted-input** leg (flagging toxic/injection-driven outputs), but as an observe-and-alert tool, not an inline blocker.

**Deployment & architecture** — SaaS observatory fed by the `whylogs` SDK (privacy-preserving profiles, so raw data stays in your environment); API and self-hosted options. Integrated with common ML pipelines and notebooks.

**Positioning & differentiators** — Known for the **privacy-preserving, profile-based** approach (`whylogs`) and for scaling to large data/ML monitoring rather than per-request LLM tracing. Incubated at the Allen Institute for AI (AI2) by ex-Amazon ML engineers; backed by Andrew Ng's AI Fund and Jeff Bezos. Nearest neighbors were [arize-phoenix](arize-phoenix.md), [fiddler-ai](fiddler-ai.md), [arthur-ai](arthur-ai.md) (all ML-monitoring lineage).

**Ownership, funding & M&A** — **M&A CONFIRMED (medium confidence).** Apple acquired WhyLabs in **2025** in an under-the-radar deal; the founders (CEO Alessya Visnjic and co-founders) joined Apple in AI roles. There is no official Apple announcement (Apple rarely confirms acquisitions), but it is corroborated by GeekWire's reporting, AI Fund's portfolio page listing WhyLabs as "acquired in 2025," LinkedIn ("ACQ BY APPLE"), and European Commission Digital Markets Act filings. The WhyLabs site now states the company is **discontinuing operations** and open-sourcing its platform. Funded 2019; ~$14M total ($4M Madrona seed + $10M Series A in 2021 co-led by AI Fund and Defy Partners, with Bezos Expeditions). HQ Seattle.

> Seed had no M&A flag and stub said `independent` — corrected to `acquired` (Apple, 2025).

**CTO / hedge-fund lens** — **Low fit going forward: do not select for new builds.** The standalone product is being wound down; only the open-source `whylogs`/LangKit code remains usable. Listed here for completeness and because the seed/registry carried it as an active observability option — flag it as M&A-dated in any survey. If you liked the profile-based monitoring approach, the OSS libraries persist but without a vendor behind them.

**Competitors / alternatives** — [arize-phoenix](arize-phoenix.md), [fiddler-ai](fiddler-ai.md), [arthur-ai](arthur-ai.md), [langfuse](langfuse.md), [datadog](datadog.md), [comet](comet.md).

**Open questions / to verify**
- Exact close date and any disclosed terms of the Apple deal (likely never officially confirmed).
- Long-term maintenance status of the open-sourced WhyLabs platform / `whylogs`.

## Sources
- [Founders at WhyLabs join Apple following under-the-radar acquisition (GeekWire, 2025)](https://www.geekwire.com/2025/founders-at-seattle-startup-whylabs-join-apple-following-under-the-radar-acquisition/) — fetched 2026-06-28 — supports: Apple acquisition, wind-down; confidence: med (reputable press, no official confirmation).
- [Apple appears to have acquired WhyLabs (MacDailyNews, 2025-06-05)](https://macdailynews.com/2025/06/05/apple-appears-to-have-acquired-whylabs-a-jeff-bezos-backed-ai-security-startup/) — fetched 2026-06-28 — supports: AI Fund/LinkedIn corroboration, founders, funding; confidence: med.
- [WhyLabs acquired by Apple — Crunchbase acquisition profile](https://www.crunchbase.com/acquisition/apple-acquires-whylabs--d9da39cb) — fetched 2026-06-28 — supports: acquisition record; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Apple acquired WhyLabs in 2025 (acqui-hire, product wound down / open-sourced). Corrected ownership independent→acquired, confidence medium (no official Apple statement). Founded 2019 Seattle, ~$14M raised.
