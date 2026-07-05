---
title: Weights & Biases (Weave)
type: vendor
name: Weights & Biases (Weave)
slug: weights-and-biases
aka: [W&B, wandb, Weave]
primary_category: llm-observability
also_listed_in: []
website: https://wandb.ai
founded: 2017
hq: San Francisco, USA
ownership_state: acquired-closed
owner: CoreWeave
ownership_note: 'Acquired by CoreWeave (Nasdaq: CRWV); announced 2025-03-04, closed 2025-05-05. Reported ~$1.7B (terms not officially disclosed).'
acquisition: {announced: 2025-03-04, closed: 2025-05-05, price: null}
funding_total: ~$250-300M (pre-acquisition)
last_funding: $50M (2023-08, led by existing investors)
market_position: null
deployment_model: [saas, self-hosted, on-prem]
form_factor: [sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / ML & AI engineering teams
last_verified: 2026-06-28
verify_after: null
tags: [llm-observability, ml-experiment-tracking, evaluation, weave, coreweave]
---

# Weights & Biases (Weave)

> **One-liner** — The ML developer platform for experiment tracking and model management, whose **Weave** product does LLM/agent observability and evaluation; acquired by GPU-cloud CoreWeave in 2025.

**Categories** — [llm-observability](../categories/llm-observability.md)

## What it does
W&B started as the standard tool for **ML experiment tracking** (logging runs, metrics, hyperparameters, datasets, model versions) and grew into a model/AI developer platform. Its LLM-relevant product is **Weave**: tracing, logging, evaluation and monitoring of LLM and agent applications — capturing prompts, responses, tool calls, latency/cost, and running evals. The job here: see what your LLM apps actually did, measure quality/regressions, and debug agent behavior.

## Where it sits in the stack
Model/prompt layer, [llm-observability](../categories/llm-observability.md). Lethal-trifecta leg: **none directly** — it is observability/evaluation, not an inline guardrail; but evals and tracing are how you catch unsafe or degraded model behavior before and after release. Adjacent to [ai-red-teaming](../categories/ai-red-teaming.md) (eval overlap) and complementary to inline [ai-runtime-security](../categories/ai-runtime-security.md).

## Deployment & architecture
SaaS, plus dedicated/self-managed and on-prem options; primary integration is via **SDK** instrumentation in training/inference code. Framework-agnostic; works across clouds and model providers. CoreWeave has committed to keeping the platform interoperable (any cloud/infra/model/framework) rather than locking it to CoreWeave GPUs.

## Positioning & differentiators
Known for being the default experiment-tracking tool in the ML research community (OpenAI among customers) and for Weave's eval-centric LLM observability. Nearest neighbors in LLM observability: [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [helicone](helicone.md), [datadog](datadog.md), [comet](comet.md) (Opik). W&B's edge is the breadth from classic ML training through LLM/agent eval; the open question is neutrality now that it is owned by a GPU cloud.

## Ownership, funding & M&A
**Verified.** Acquired by **CoreWeave** (Nasdaq: CRWV) — announced **2025-03-04**, **closed 2025-05-05**. Deal value **not officially disclosed**; widely reported at **~$1.7B** (The Information). Founded 2017 by Lukas Biewald, Chris Van Pelt, Shawn Lewis; HQ San Francisco; raised ~$250-300M pre-deal (investors incl. Insight Partners, Felicis, Coatue). Now a CoreWeave subsidiary; CoreWeave states it will keep the platform interoperable. Ownership confidence **high** on acquirer/dates; price reported, not confirmed.

## CTO / hedge-fund lens
**Day-1 if you build or fine-tune models / ship LLM apps in-house**; not needed if you only consume third-party AI assistants. For a quant/ML-heavy fund, W&B/Weave is a strong choice for experiment tracking + LLM eval and supports self-hosting for data-control reasons. The CoreWeave ownership is the main diligence point: assess data-residency, neutrality, and whether you are comfortable with a GPU-cloud vendor owning your ML metadata plane. Relevant to model-risk/validation evidence under SR 11-7-style processes (eval and lineage records).

## Competitors / alternatives
[langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [helicone](helicone.md), [datadog](datadog.md), [comet](comet.md), [fiddler-ai](fiddler-ai.md).

## Open questions / to verify
- Official deal price (only reported, not disclosed).
- Concrete data-residency/neutrality guarantees post-CoreWeave for non-CoreWeave customers.

## Sources
- [CoreWeave Completes Acquisition of Weights & Biases](https://www.prnewswire.com/news-releases/coreweave-completes-acquisition-of-weights--biases-302445966.html) — fetched 2026-06-28 — supports: acquirer CoreWeave, close 2025-05-05, interoperability commitment; confidence: high
- [CoreWeave acquires AI developer platform Weights & Biases (TechCrunch)](https://techcrunch.com/2025/03/04/coreweave-acquires-ai-developer-platform-weights-biases/) — fetched 2026-06-28 — supports: announce 2025-03-04, ~$1.7B reported, OpenAI customer; confidence: med
- [About Weights & Biases / Crunchbase](https://wandb.ai/site/company/about-us/) — fetched 2026-06-28 — supports: founded 2017, founders, HQ, funding; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified CoreWeave acquisition (announced 2025-03-04, closed 2025-05-05, ~$1.7B reported), raised ownership_confidence low→high; filled founding/HQ/funding, clarified Weave = LLM observability product.
