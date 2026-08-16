---
title: CalypsoAI
type: vendor
name: CalypsoAI
slug: calypsoai
aka: [Calypso AI]
primary_category: ai-runtime-security
also_listed_in: [ai-governance-platform]
website: https://www.f5.com/products/ai-guardrails
founded: 2018
hq: Dublin, Ireland
ownership_state: acquired-closed
owner: F5
ownership_note: Acquired by [f5](f5.md) — announced 2025-09-11 (~$180M headline), closed 2025-09-26 for $145.2M cash per F5's 10-Q. Brand fully retired; now F5 AI Guardrails / F5 AI Red Team
acquisition: {announced: 2025-09-11, closed: 2025-09-26, price: $145.2M cash (announced as ~$180M consideration)}
funding_total: ~$40M+ (pre-acquisition)
last_funding: $23M round announced 2023-06-27 (Paladin Capital Group + strategic investors)
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [acquired, f5, ai-firewall, ai-guardrails, red-teaming]
---

# CalypsoAI

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [f5](f5.md)** (closed 2025-09-26). **Brand fully retired** — `calypsoai.com` now 301-redirects to F5's AI Guardrails product page. This is a historical page: you cannot buy CalypsoAI, only **F5 AI Guardrails**.

**One-liner** — Formerly an AI runtime-security / "guardrails" pure-play (real-time threat defense + automated red teaming for model traffic); since 2025-09-26 it is the AI-security core of [f5](f5.md)'s platform, sold only as F5 AI Guardrails and F5 AI Red Team.

## What it does
CalypsoAI built model-agnostic security for generative and agentic AI: an inline guardrails layer that screens prompts and responses in real time (prompt-injection defense, data-loss prevention, content/abuse controls) plus **red teaming at scale** that continuously attacks your AI systems to surface vulnerabilities. The pitch was consistent protection across whatever models an enterprise uses, decoupled from any single model provider.

That technology ships today as **F5 AI Guardrails**. As of 2026-07-27 the product page advertises adversarial-attack defense (prompt injection, threat research from F5 Labs, model risk scoring via the CASI Model Risk Leaderboard), model-agnostic policy enforcement with natural-language custom policies, prebuilt compliance controls (PII, EU AI Act, PCI, PHI), content moderation, agentic-AI controls that restrict agent actions and tool privileges, and audit-ready logging with visibility into system prompts and tool calls — across public cloud, private cloud, and on-prem. **F5 AI Red Team** is now a separate SKU in the same line.

## Where it sits in the stack
Primary [ai-runtime-security](../categories/ai-runtime-security.md) (the "AI firewall" inline control) with a secondary [ai-governance-platform](../categories/ai-governance-platform.md) tag (its reporting/red-team posture supports AI governance). Layer: model-prompt. Lethal-trifecta role: addresses all three legs at the inference boundary — **untrusted input** (prompt injection), **sensitive data** (DLP on prompts/responses), and **egress** (policy on what model traffic is allowed). Sits at the green↔red boundary.

## Deployment & architecture
SaaS and self-hosted; API-driven and deployable inline in front of model endpoints (model-agnostic across proprietary + open-source LLMs). Post-acquisition it is delivered **only** as **F5 AI Guardrails** (runtime protection) and **F5 AI Red Team** (autonomous attack simulation, advertised >10,000 new attack patterns/month), integrated into the F5 Application Delivery and Security Platform (ADSP). There is no standalone CalypsoAI product, contract, or price list any more — procurement runs through F5.

## Positioning & differentiators
Known for pairing inline guardrails with continuous automated red teaming in one product — defense + offense — and for model-agnostic coverage. It was a Top-Two Finalist in the 2025 RSAC Innovation Sandbox and named to Fast Company's Most Innovative Companies in AI (2025) (vendor/press accolades, noted as such).

**As of 2026-07-27 this is no longer an independent position in the market.** The differentiation now belongs to F5: guardrails and red teaming are two SKUs inside ADSP, and F5 has since added [surepath-ai](surepath-ai.md)'s shadow-AI discovery in front of them. Evaluate the F5 platform story, not a pure-play. The tradeoff shifts accordingly — you gain ADSP integration and a public vendor's support model, and you lose the independence and pace that made the pure-play attractive. Former nearest neighbors, which remain the real shortlist if you are not an F5 shop: [lakera](lakera.md), [prompt-security](prompt-security.md), [witnessai](witnessai.md), [aim-security](aim-security.md), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [enkrypt-ai](enkrypt-ai.md), [splxai](splxai.md).

## Ownership, funding & M&A
Founded **2018**; principal operations in **Dublin, Ireland** (with US roots/Silicon Valley presence). Pre-acquisition funding reported at **over $40M** (Series A $13M led by Paladin Capital Group in 2020; a $23M round announced 2023-06-27; investors incl. Paladin, Lockheed Martin Ventures, Hakluyt Capital). **Acquired by [f5](f5.md)** — announced **2025-09-11**, **closed 2025-09-26**. This confirms the seed flag ("acq by F5"). **Confidence: high** (SEC filing).

On price, two figures circulate and they measure different things:

- **~$180M** — the headline in F5's 2025-09-11 announcement: "$180 million in purchase consideration financed primarily with cash." Nearly all press coverage (GeekWire, SDxCentral, Frontier Enterprise) traces to this number.
- **$145.2M cash** — what F5 actually recorded at closing, per Note 4 of its FY2026 Q1 Form 10-Q: "On September 26, 2025, the Company closed on a transaction for the acquisition of CalypsoAI Corp. … for $145.2 million in cash." Allocation: $14.2M net tangible assets, $16.9M developed technology, $114.2M goodwill (total $145.207M, preliminary).

F5 does not reconcile the ~$35M gap, so this page states both with their basis rather than guessing at holdbacks or retention. The GAAP figure is the better number for "what was paid." F5 also disclosed that CalypsoAI's revenue and earnings were **not material** to its operations — a useful reality check on the pure-play's scale at exit.

> Correction (2026-07-27): this page previously recorded the close as **2025-10-08**. No primary source supports that date — F5's completion blog was published 2025-09-29 and the 10-Q states 2025-09-26. Corrected to 2025-09-26.

## CTO / hedge-fund lens
Day-1 control type (runtime AI firewall) but, as a now-absorbed product, you'd evaluate it as **F5 AI Guardrails** rather than standalone CalypsoAI. Relevant if you're an F5 shop or want guardrails + red-teaming bundled. The red-team capability has mild SR 11-7 / model-validation value (evidence that AI systems were adversarially tested). Best fit: enterprises standardizing on F5; smaller funds would weigh it against lighter SaaS guardrails.

## Competitors / alternatives
[lakera](lakera.md), [prompt-security](prompt-security.md), [witnessai](witnessai.md), [aim-security](aim-security.md), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [enkrypt-ai](enkrypt-ai.md), [splxai](splxai.md), [trojai](trojai.md).

## Open questions / to verify
- ~~Whether the CalypsoAI brand survives or is fully retired into F5 product naming.~~ **Resolved 2026-07-27: fully retired.** `calypsoai.com` 301-redirects to the F5 AI Guardrails product page, which carries no CalypsoAI branding at all.
- Exact total funding (sources say "$40M+"; not itemized to a precise figure).
- What accounts for the ~$35M gap between the announced ~$180M consideration and the $145.2M recorded at close. F5 has not broken this out; unresolved and possibly never disclosed.
- Whether this page should eventually be merged into [f5](f5.md) rather than kept as a standalone historical entry — it is retained for now because the survey and the M&A map still reference the CalypsoAI name.

## Sources
- [F5 Form 10-Q, FY2026 Q1, Note 4 Business Combinations (SEC)](https://www.sec.gov/Archives/edgar/data/1048695/000104869526000023/ffiv-20251231.htm) — fetched 2026-07-27 — supports: **close date 2025-09-26**, **$145.2M cash**, purchase-price allocation, immateriality of CalypsoAI revenue; cached at `raw/sources/2026-07-27--calypsoai--f5-10q-close-date-and-price.md`; confidence: high (primary/SEC)
- [F5 AI Guardrails product page](https://www.f5.com/products/ai-guardrails) — fetched 2026-07-27 — supports: current product name and capabilities, zero CalypsoAI branding, 301 target of calypsoai.com; confidence: high
- [F5 to acquire CalypsoAI… (F5 press release)](https://www.f5.com/company/news/press-releases/f5-to-acquire-calypsoai-to-bring-advanced-ai-guardrails-to-large-enterprises) — fetched 2026-06-28, re-checked 2026-07-27 — supports: acquirer, ~$180M announced consideration, 2025-09-11 announce; confidence: high
- [F5 completes acquisition of CalypsoAI (F5 blog, published 2025-09-29)](https://www.f5.com/company/blog/what-are-ai-guardrails) — fetched 2026-06-28, re-checked 2026-07-27 — supports: completion, AI Guardrails + Red Team launch; note the post states completion but gives no date, which is how 2025-10-08 crept in; confidence: high
- [CalypsoAI Raises $23 Million (Paladin Capital Group)](https://www.paladincapgroup.com/calypsoai-raises-23-million-from-paladin-capital-group-and-strategic-investors-to-drive-secure-enterprise-adoption-of-generative-ai-and-large-language-models/) — fetched 2026-06-28 — supports: funding history, Dublin HQ, founding 2018; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by [f5](f5.md)** (~$180M; announced 2025-09-11, completed 2025-10-08). Seed flag verified. Filled founding (2018), Dublin HQ, funding (~$40M+), product (now F5 AI Guardrails / AI Red Team). Confidence raised to high.
- [2026-07-27] URL audit found `calypsoai.com` 301-redirecting to `https://www.f5.com/products/ai-guardrails`. Re-verified against F5's FY2026 Q1 Form 10-Q and **corrected two facts**: close date **2025-10-08 → 2025-09-26**, and price recorded as **$145.2M cash** alongside the ~$180M announced consideration. Website repointed to the F5 product page; positioning rewritten as a historical/absorbed entry; **brand-retirement open question resolved** (fully retired, no CalypsoAI branding remains). Same corrections applied to [f5](f5.md) and the M&A map.
</content>
