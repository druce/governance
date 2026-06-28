---
title: Haize Labs
type: vendor
name: Haize Labs
slug: haize-labs
categories: [ai-red-teaming]
layer: model-prompt
aliases: [Haize, j1]
website: "https://www.haizelabs.com"
founded: 2023
hq: New York, NY
ownership: independent
ownership_detail: VC-backed; $12.5M seed (2024-08) led by General Catalyst at ~$100M valuation (no acquisition)
ownership_confidence: high
funding_total: ~$12.5M
last_funding: Seed $12.5M (2024-08)
deployment: [saas, api]
target_customer: AI labs / enterprise building LLM apps
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [ai-red-teaming, jailbreak, evaluation, judge-models]
---

# Haize Labs

> AI-safety startup that automatically stress-tests ("haizes") LLMs at scale to find
> jailbreaks and failure modes, then hardens them — plus judge/evaluation models.

**One-liner** — Automated red-teaming that algorithmically discovers how an LLM fails
(jailbreaks, harmful or wrong outputs) so you can fix it before shipping.

**Categories** — [ai-red-teaming](../categories/ai-red-teaming.md)

## What it does
Haize Labs runs large-scale automated adversarial testing — "haizing" — to surface the
inputs that make an LLM or AI app misbehave (jailbreaks, unsafe content, hallucination,
policy violations). It generates massive attack campaigns, ranks discovered failure
modes, and feeds them back for hardening. It also builds evaluation/**judge models**
(the **j1** line) and reliability tooling, pitching "deploy 99.9% reliable AI."
Anthropic is named among its customers.

## Where it sits in the stack
[ai-red-teaming](../categories/ai-red-teaming.md) in the model/prompt layer. Lethal-trifecta role: the
**untrusted-input** leg — it specializes in finding adversarial inputs that break the
model. It is a pre-production/assurance tool and a source of evaluators, not an inline
runtime firewall, so it complements [ai-runtime-security](../categories/ai-runtime-security.md) rather than replacing it.

## Deployment & architecture
SaaS / API: a red-team suite plus judge models callable in evaluation pipelines.
Public deployment/integration detail is limited (early-stage); see open questions.

## Positioning & differentiators
Known for **research-driven, automated jailbreak discovery** and a high-profile young
founding team; counts a frontier lab (Anthropic) as a customer, which is strong
signal for the adversarial-testing thesis. Nearest neighbors are red-team testers
[mindgard](mindgard.md), [splxai](splxai.md), [promptfoo](promptfoo.md) and the eval-leaning [patronus-ai](patronus-ai.md),
[maxim-ai](maxim-ai.md). Differentiates on attack-generation depth and judge models (j1) vs.
broader eval/observability platforms.

## Ownership, funding & M&A
Independent, VC-backed. Founded 2023 by Leonard Tang (CEO), Richard Liu, and Steve Li
(Harvard undergrads; Tang and Li were Berkeley AI Research undergrad researchers).
Raised a **$12.5M seed in August 2024 led by General Catalyst at a ~$100M valuation**
(angels include founders of Okta and Hugging Face, Amjad Masad/Replit, Scott Wu/
Cognition, Demi Guo/Pika, Neil Shen, Soma Capital, OVO Fund). No seed M&A flag and no
acquisition — **ownership confirmed independent** (confidence high).

## CTO / hedge-fund lens
Day-2 and niche. Relevant only to teams **building their own frontier-grade LLM
features/agents** that want deep adversarial assurance — the buyer profile skews toward
AI labs and AI-native product teams, not a typical hedge fund consuming enterprise AI
assistants. Limited direct SR 11-7 utility beyond serving as adversarial-testing
evidence. Early-stage vendor: weigh maturity for production-critical reliance.

## Competitors / alternatives
[mindgard](mindgard.md), [splxai](splxai.md), [promptfoo](promptfoo.md), [patronus-ai](patronus-ai.md), [maxim-ai](maxim-ai.md), [hiddenlayer](hiddenlayer.md).

## Open questions / to verify
- Productization/pricing and how the j1 judge models are packaged.
- Deployment specifics (self-host vs. hosted) and enterprise integrations.
- Any funding round since the 2024 seed.

## Sources
- [General Catalyst-led round values Haize Labs at $100M (PitchBook)](https://pitchbook.com/news/articles/general-catalyst-haize-labs-100-million-valuation) — fetched 2026-06-28 — supports: $12.5M seed, ~$100M valuation, Aug 2024, founders, Anthropic customer; confidence: high (press).
- [Haize Labs valued at $100M (NextRound)](https://nextround.ai/2024/08/07/young-ai-safety-startup-haize-labs-valued-at-100m-in-funding-round-led-by-general-catalyst/) — fetched 2026-06-28 — supports: seed details, founders; confidence: med (press).
- [Haize Labs — Crunchbase](https://www.crunchbase.com/organization/haize-labs) — fetched 2026-06-28 — supports: founding 2023, HQ NYC, investors; confidence: med (aggregator).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (2023, NYC, Harvard founders; $12.5M seed General Catalyst Aug-2024 at ~$100M val; Anthropic customer); no acquisition. Set ownership_confidence high, hedge_fund_fit low.
