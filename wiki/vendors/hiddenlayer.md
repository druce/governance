---
type: vendor
name: HiddenLayer
slug: hiddenlayer
categories: [ai-runtime-security, ai-red-teaming, ai-spm]
layer: model-prompt
aliases: []
website: "https://www.hiddenlayer.com"
founded: 2022
hq: Austin, Texas (US)
ownership: independent
ownership_detail: "Independent, VC-backed; no acquisition found as of 2026-06-28"
ownership_confidence: high
funding_total: ~$50M+ (Series A $50M; earlier seed undisclosed)
last_funding: "Series A $50M, 2023-09-19 (M12 / Microsoft + Moore Strategic Ventures lead)"
deployment: [saas, self-hosted, api, sdk]
target_customer: enterprise; regulated; government / defense
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [ai-firewall, model-scanning, red-teaming, ai-spm, independent]
---

# HiddenLayer

> **One-liner** — AI/ML model-security pioneer offering model scanning, supply-chain checks, runtime detection & response, and adversarial red teaming for ML models and GenAI apps.

**Categories** — [ai-runtime-security](../categories/ai-runtime-security.md), [ai-red-teaming](../categories/ai-red-teaming.md), [ai-spm](../categories/ai-spm.md)

## What it does
HiddenLayer secures the **model itself**, not just the prompt. Its AISec Platform spans four jobs: **AI discovery / model scanning** (detect malicious models, backdoored or tampered weights, unsafe serialization, and vulnerable dependencies before deployment — e.g. catching exploit-laden model files pulled from Hugging Face), **AI supply-chain security**, **runtime defense via AI Detection & Response (MLDR)** — non-invasive, software-based monitoring of model inputs/outputs to catch adversarial attacks, prompt injection, and data extraction in production — and **attack simulation / red teaming**. The through-line is a research-led, model-centric view: protect against adversarial ML and model-supply-chain threats that prompt-only firewalls miss.

## Where it sits in the stack
Cross-listed across [ai-runtime-security](../categories/ai-runtime-security.md) (MLDR runtime defense), [ai-red-teaming](../categories/ai-red-teaming.md) (attack simulation), and [ai-spm](../categories/ai-spm.md) (discovery/inventory + supply-chain posture). In lethal-trifecta terms it breaks **untrusted-input** (adversarial prompts/inputs, malicious models as an input vector) and **sensitive-data** (model-extraction / leakage detection). Sits at the model/prompt layer and uniquely reaches *below* the prompt to the model artifact and its supply chain — overlapping with [software-supply-chain](../categories/software-supply-chain.md) for ML artifacts.

## Deployment & architecture
SaaS plus self-hosted options; the model scanner and MLDR are software/API-based and "non-invasive" (no model retraining or in-line model surgery required). Integrates into MLOps pipelines, model registries (e.g. Hugging Face, MLflow), CI/CD, and SOC/SIEM for runtime alerts. Provides a community model scanner that drove early adoption among ML engineers.

## Positioning & differentiators
Best known as the **adversarial-ML / model-security specialist** with a high-profile research team (notable disclosures around model file-format exploits and AI attack techniques). Differs from prompt-firewall-first peers ([prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [prompt-security](prompt-security.md), [lakera](lakera.md)) by leading with **model scanning and supply-chain** coverage; differs from pure red-teaming tools ([mindgard](mindgard.md), [splxai](splxai.md), [promptfoo](promptfoo.md)) by adding runtime detection & response; overlaps [ai-spm](../categories/ai-spm.md) players ([noma-security](noma-security.md)) on discovery/inventory. Strong government/defense and large-enterprise credibility (Booz Allen, IBM, Capital One among strategic backers).

## Ownership, funding & M&A
**No seed M&A flag; confirmed independent.** Founded **March 2022** (out of stealth July 2022) in **Austin, Texas**; CEO/co-founder **Chris "Tito" Sestito**. Raised a **$50M Series A on 2023-09-19**, led by **M12 (Microsoft's Venture Fund)** and **Moore Strategic Ventures**, with Booz Allen Ventures, IBM Ventures, Capital One Ventures, and Ten Eleven Ventures — at the time the largest AI-security Series A of 2023 (vendor claim). **Independent** as of 2026-06-28 (no acquisition found; ~169 employees per third-party data). `ownership_confidence: high` for independence; total funding likely understated (earlier seed undisclosed).

## CTO / hedge-fund lens
**Day-1 if you self-host or fine-tune models, or pull models from public hubs** — the model-scanning/supply-chain angle addresses a real risk (poisoned or trojaned model artifacts) that prompt firewalls and gateways don't. If you only consume hosted SaaS assistants, HiddenLayer is more **Day-2** and its model-supply-chain value drops. SR 11-7 / model-risk angle: discovery + scanning supports a model inventory and pre-deployment validation evidence; MLDR adds runtime monitoring for model-validation and ongoing-monitoring requirements. Fit **medium** for a typical hedge fund (high if you run open-weight models in-house, lower if fully SaaS). Heavier/more specialized than a fund needs unless model self-hosting is on the roadmap.

## Competitors / alternatives
[prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [trojai](trojai.md), [pillar-security](pillar-security.md), [mindgard](mindgard.md), [splxai](splxai.md), [noma-security](noma-security.md).

## Open questions / to verify
- Total funding (earlier seed amount undisclosed) and any post-2023 round.
- Current revenue/scale and degree of government vs. commercial mix.
- Extent of GenAI/agent runtime coverage vs. classic ML-model focus in latest platform.

## Sources
- [HiddenLayer Raises $50M in Series A Funding to Safeguard AI](https://www.hiddenlayer.com/news/hiddenlayer-raises-50m-in-series-a-funding-to-safeguard-ai/) — fetched 2026-06-28 — supports: founding, HQ, founder, $50M Series A 2023-09-19, investors, platform scope; confidence: high
- [PR Newswire mirror of Series A announcement](https://www.prnewswire.com/news-releases/hiddenlayer-raises-50m-in-series-a-funding-to-safeguard-ai-301931260.html) — fetched 2026-06-28 — supports: funding, investors; confidence: high
- (cached: `raw/sources/2026-06-28--hiddenlayer--series-a-and-platform.md`)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED **independent** (no acquisition), set ownership_confidence high. Established founding 2022 (Austin; CEO Chris Sestito), $50M Series A 2023-09-19 (M12/Moore lead). Documented four-pillar platform (model scanning / supply chain / MLDR runtime / red teaming). hedge_fund_fit = medium.
