---
title: Giskard
type: vendor
name: Giskard
slug: giskard
categories: [llm-observability, ai-red-teaming]
layer: model-prompt
aliases: []
website: "https://www.giskard.ai"
founded: 2021
hq: Paris, France
ownership: independent
ownership_detail: Independent, early-stage. ~$1.5–2M seed (~2022, Elaia + angels); ~€3M Bpifrance/France 2030 grant (2024). No later round confirmed.
ownership_confidence: medium
funding_total: ~$1.5–2M (seed) + ~€3M non-dilutive grant
last_funding: Seed, ~$1.5–2M, ~2022
deployment: [sdk, self-hosted, saas, api]
target_customer: enterprise / regulated (EU), ML & GenAI teams
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [evaluation, red-teaming, open-source, testing, eu-ai-act]
---

# Giskard

> Researched 2026-06-28. Primary category: [llm-observability](../categories/llm-observability.md); also [ai-red-teaming](../categories/ai-red-teaming.md).

**One-liner** — A French open-source LLM/ML testing and red-teaming platform that scans AI models and agents for quality, security, and vulnerability issues.

**What it does** — Giskard provides an open-source Python library to test ML and LLM applications — detecting quality regressions, robustness gaps, bias, and security vulnerabilities — plus an LLM vulnerability scanner that runs adversarial, multi-turn probes (prompt injection, jailbreaks, harmful/off-topic outputs). The commercial **Giskard Hub** wraps this for teams: continuous red teaming, collaborative test management, and evaluation reporting for agents. The job: systematically probe your AI before and after shipping, with evidence for risk/compliance.

**Where it sits in the stack** — Sits across [llm-observability](../categories/llm-observability.md) (the evaluation/testing sub-segment) and [ai-red-teaming](../categories/ai-red-teaming.md) (adversarial probing/guardrail validation). It breaks the **untrusted-input** leg by surfacing how a model misbehaves under hostile prompts — a pre-production and continuous-assurance tool, not an inline runtime firewall.

**Deployment & architecture** — OSS library (`giskard-oss` on GitHub) installed as an SDK in your own environment; Giskard Hub available as SaaS or self-managed for enterprises. Integrates with common LLM frameworks and CI; partners listed across AWS/GCP/Azure and consultancies (Accenture, PwC, EY, KPMG — marketing).

**Positioning & differentiators** — Known as **open-source-first, EU-based, and red-teaming-forward**, with an explicit EU AI Act compliance angle. Closest neighbors: [trulens](trulens.md) and [arize-phoenix](arize-phoenix.md) (OSS eval/tracing), [promptfoo](promptfoo.md) and [patronus-ai](patronus-ai.md) (eval + red-teaming), and dedicated red-teamers like [mindgard](mindgard.md) and [splxai](splxai.md). Differs from production-monitoring platforms ([fiddler-ai](fiddler-ai.md), [arthur-ai](arthur-ai.md)) by centering testing/vulnerability scanning over live observability. European data-residency and AI-Act framing are its distinctive pitch.

**Ownership, funding & M&A** — Independent and early-stage. Founded 2021 in Paris by Alex Combessie and Jean-Marie John-Mathews (now co-CEOs); CTO Matteo Dora. Raised a small seed (~$1.5–2M, ~2022; sources disagree on the exact figure) from Elaia and angels including founders/CTOs from Hugging Face, Mistral AI, and Uber (e.g., Charles Gorintin). Won a ~€3M Bpifrance / France 2030 grant (2024) to lead an LLM-evaluation R&D consortium with Mistral AI, Artefact, INA, and BnF. No M&A; no later equity round confirmed. (confidence: medium)

**CTO / hedge-fund lens** — Day-1 useful if you build LLM/agent apps and want a cheap, code-first way to red-team and test them — the OSS library is free, and the EU AI Act framing suits a fund with European entities or regulators. It is an assurance/testing tool, not a production monitor or a SR 11-7 governance system of record; pair it with a monitoring/governance layer. Early-stage vendor — diligence the Hub's roadmap and support before depending on it.

**Competitors / alternatives** — [promptfoo](promptfoo.md), [patronus-ai](patronus-ai.md), [mindgard](mindgard.md), [splxai](splxai.md), [trulens](trulens.md), [arize-phoenix](arize-phoenix.md), [guardrails-ai](guardrails-ai.md).

**Open questions / to verify**
- Exact seed amount and total funding (sources report $1.5M vs $2M); any round since 2022.
- Current paid-customer roster vs marketing logos (AXA, BNP Paribas, Michelin, Google DeepMind cited by vendor).

## Sources
- [About Giskard](https://www.giskard.ai/about) — fetched 2026-06-28 — supports: founders, product scope, red-teaming/EU AI Act positioning; confidence: med (vendor/marketing).
- [Giskard-AI/giskard-oss (GitHub)](https://github.com/Giskard-AI/giskard-oss) — fetched 2026-06-28 — supports: OSS testing/eval library; confidence: high.
- [Giskard — Crunchbase](https://www.crunchbase.com/organization/giskard-ai) / [Startup Intros](https://startupintros.com/orgs/giskard) — fetched 2026-06-28 — supports: founding 2021, Paris, seed funding, Bpifrance grant; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent, founded 2021 Paris, small seed (~$1.5–2M) + ~€3M Bpifrance grant. OSS testing/red-teaming + Giskard Hub. No M&A. Set ownership_confidence medium (exact funding figures conflict).
