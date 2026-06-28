---
type: vendor
name: CalypsoAI
slug: calypsoai
categories: [ai-runtime-security, ai-governance-platform]
layer: model-prompt
aliases: [Calypso AI]
website: https://calypsoai.com
founded: 2018
hq: Dublin, Ireland
ownership: acquired
ownership_detail: "Acquired by [[f5]] for ~$180M — announced 2025-09-11, completed 2025-10-08; now F5 AI Guardrails / F5 AI Red Team"
ownership_confidence: high
funding_total: ~$40M+ (pre-acquisition)
last_funding: "$23M round announced 2023-06-27 (Paladin Capital Group + strategic investors)"
deployment: [saas, api, self-hosted]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [acquired, ai-firewall, ai-guardrails, red-teaming]
---

# CalypsoAI

> **Researched 2026-06-28.** Primary category: [[ai-runtime-security]]. **Acquired by [[f5]]** (completed 2025-10-08).

**One-liner** — An AI runtime-security / "guardrails" pure-play (real-time threat defense + automated red teaming for model traffic), now the AI-security core of [[f5]]'s platform.

## What it does
CalypsoAI builds model-agnostic security for generative and agentic AI: an inline guardrails layer that screens prompts and responses in real time (prompt-injection defense, data-loss prevention, content/abuse controls) plus **red teaming at scale** that continuously attacks your AI systems to surface vulnerabilities. The pitch is consistent protection across whatever models an enterprise uses, decoupled from any single model provider.

## Where it sits in the stack
Primary [[ai-runtime-security]] (the "AI firewall" inline control) with a secondary [[ai-governance-platform]] tag (its reporting/red-team posture supports AI governance). Layer: model-prompt. Lethal-trifecta role: addresses all three legs at the inference boundary — **untrusted input** (prompt injection), **sensitive data** (DLP on prompts/responses), and **egress** (policy on what model traffic is allowed). Sits at the green↔red boundary.

## Deployment & architecture
SaaS and self-hosted; API-driven and deployable inline in front of model endpoints (model-agnostic across proprietary + open-source LLMs). Post-acquisition it is delivered as **F5 AI Guardrails** (runtime protection) and **F5 AI Red Team** (autonomous attack simulation, advertised >10,000 new attack patterns/month), integrated into the F5 Application Delivery and Security Platform (ADSP).

## Positioning & differentiators
Known for pairing inline guardrails with continuous automated red teaming in one product — defense + offense — and for model-agnostic coverage. It was a Top-Two Finalist in the 2025 RSAC Innovation Sandbox and named to Fast Company's Most Innovative Companies in AI (2025) (vendor/press accolades, noted as such). Nearest neighbors: [[lakera]], [[prompt-security]], [[witnessai]], [[aim-security]], [[hiddenlayer]], [[prisma-airs]], [[enkrypt-ai]], [[splxai]].

## Ownership, funding & M&A
Founded **2018**; principal operations in **Dublin, Ireland** (with US roots/Silicon Valley presence). Pre-acquisition funding reported at **over $40M** (Series A $13M led by [[Paladin Capital Group]] in 2020; a $23M round announced 2023-06-27; investors incl. Paladin, Lockheed Martin Ventures, Hakluyt Capital). **Acquired by [[f5]]** for ~$180M — announced **2025-09-11**, **completed 2025-10-08**. This confirms the seed flag ("acq by F5"). Verified against F5's press release/blog and CalypsoAI/Paladin sources. **Confidence: high.**

## CTO / hedge-fund lens
Day-1 control type (runtime AI firewall) but, as a now-absorbed product, you'd evaluate it as **F5 AI Guardrails** rather than standalone CalypsoAI. Relevant if you're an F5 shop or want guardrails + red-teaming bundled. The red-team capability has mild SR 11-7 / model-validation value (evidence that AI systems were adversarially tested). Best fit: enterprises standardizing on F5; smaller funds would weigh it against lighter SaaS guardrails.

## Competitors / alternatives
[[lakera]], [[prompt-security]], [[witnessai]], [[aim-security]], [[hiddenlayer]], [[prisma-airs]], [[cisco-ai-defense]], [[enkrypt-ai]], [[splxai]], [[trojai]].

## Open questions / to verify
- Whether the CalypsoAI brand survives or is fully retired into F5 product naming.
- Exact total funding (sources say "$40M+"; not itemized to a precise figure).

## Sources
- [F5 to acquire CalypsoAI… (F5 press release)](https://www.f5.com/company/news/press-releases/f5-to-acquire-calypsoai-to-bring-advanced-ai-guardrails-to-large-enterprises) — fetched 2026-06-28 — supports: acquirer, ~$180M, 2025-09-11 announce; confidence: high
- [F5 completes acquisition of CalypsoAI (F5 blog)](https://www.f5.com/company/blog/what-are-ai-guardrails) — fetched 2026-06-28 — supports: completion 2025-10-08, AI Guardrails + Red Team; confidence: high
- [CalypsoAI Raises $23 Million (Paladin Capital Group)](https://www.paladincapgroup.com/calypsoai-raises-23-million-from-paladin-capital-group-and-strategic-investors-to-drive-secure-enterprise-adoption-of-generative-ai-and-large-language-models/) — fetched 2026-06-28 — supports: funding history, Dublin HQ, founding 2018; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by [[f5]]** (~$180M; announced 2025-09-11, completed 2025-10-08). Seed flag verified. Filled founding (2018), Dublin HQ, funding (~$40M+), product (now F5 AI Guardrails / AI Red Team). Confidence raised to high.
</content>
