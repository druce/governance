---
type: vendor
name: Adaptive Security
slug: adaptive-security
categories: [anti-deepfake]
layer: foundation
aliases: []
website: "https://www.adaptivesecurity.com"
founded: 2025
hq: New York, NY, USA
ownership: independent
ownership_detail: VC-backed independent; OpenAI Startup Fund and a16z are investors (not owners). No acquisition.
ownership_confidence: high
funding_total: $146.5M (as of 2025-12-16)
last_funding: Series B, $81M, 2025-12-16 (led by Bain Capital Ventures)
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [deepfake, social-engineering, security-awareness-training, phishing-simulation, vishing]
---

# Adaptive Security

> Primary category: [anti-deepfake](../categories/anti-deepfake.md).

**One-liner** — AI-native security awareness training and social-engineering attack simulation (phishing, vishing, smishing, and deepfake voice/video) that drills employees against the kind of AI-generated impersonation attacks they now actually face.

## What it does

Adaptive Security is a human-layer defense vendor. It runs simulated social-engineering campaigns against an organization's own staff — AI-generated phishing emails, SMS (smishing), voice calls (vishing), and deepfake voice/video personas — then measures who falls for them and delivers personalized security-awareness training shaped to each user's risk profile. It adds real-time threat triage and AI-driven risk scoring. The pitch is that legacy awareness-training tools (KnowBe4-style) were built for generic phishing, whereas attackers can now cheaply clone a CEO's voice or face, so the training and simulations need to be AI-native too. (Vendor framing — marketing.)

## Where it sits in the stack

Sits in [anti-deepfake](../categories/anti-deepfake.md) at the foundation layer. This is a **people-and-process** control, not an inline technical guardrail: it does not sit in the model/prompt path or inspect application traffic. Its lethal-trifecta relevance is, at most, **untrusted-input adjacent** — it hardens the human against malicious inbound social-engineering content, but it does not break any of the three legs at the system level. Trust-zone relevance: the human perimeter (red zone / external untrusted contact), not the AI application data path.

## Deployment & architecture

SaaS platform. Delivers simulated attacks across email, SMS, voice, and video channels and reports results; training is delivered to end users. Integrations to verify (IdP/SSO, email/HRIS for user provisioning, SIEM for reporting) — not confirmed from primary sources here. No inline proxy, API-gateway, or model-path component; this is an admin-console + simulation-delivery product, not a runtime security control.

## Positioning & differentiators

Known for being the OpenAI-backed, AI-native entrant in security awareness training, explicitly targeting deepfake and multi-channel (voice/video/SMS) social engineering rather than email-only phishing. Differs from digital-risk-protection peers like [doppel](doppel.md) (which scans the external internet for impersonation of your brand/executives) — Adaptive points inward at your own employees, training them. Differs from media-authentication vendors [reality-defender](reality-defender.md), [getreal](getreal.md), and [pindrop](pindrop.md), which detect whether a given piece of media or a call is synthetic; Adaptive instead uses synthetic media offensively to test and train staff. Named customers (vendor-stated): PayPal, Xerox, Bose, NHL, PGA, Figma, Ramp, Vimeo, Perplexity.

## Ownership, funding & M&A

Independent, VC-backed. No acquisition (seed carried no M&A flag; confirmed none found). Founded 2025 (public launch January 2025); HQ New York; co-founders Brian Long (CEO) and Andrew Jones.

Funding trajectory, all confirmed against primary releases:
- **Series A — $43M**, announced 2025-04-02, co-led by **Andreessen Horowitz (a16z)** and the **OpenAI Startup Fund** (noted as OpenAI's first cybersecurity investment).
- **Series A extension — to $55M total**, announced 2025-09-09, via an OpenAI Startup Fund follow-on.
- **Series B — $81M**, announced 2025-12-16, led by **Bain Capital Ventures**, with NVentures (NVIDIA), OpenAI Startup Fund, a16z, Abstract Ventures, Capital One Ventures, Citi Ventures. **Total raised $146.5M.**

> The brief's special-check item — "verify the OpenAI-led funding claim" — is **confirmed**: the OpenAI Startup Fund co-led the April 2025 Series A and extended it in September 2025 (primary PR Newswire releases). Note nuance: OpenAI is an *investor*, not the sole "lead" of the original round (a16z co-led) and not an owner.

## CTO / hedge-fund lens

**Day-2, medium fit.** Deepfake-enabled vishing/BEC against finance staff (fraudulent wire approvals, fake-CEO calls) is a real and rising threat for asset managers, so AI-native awareness training and deepfake-call simulation are reasonable for a fund with meaningful headcount and treasury/payment operations. But this is a human-risk control, not part of the AI-application security stack the rest of this wiki covers, and it competes with incumbent awareness-training the fund may already license. No direct SR 11-7 / model-risk relevance. Small funds (sub-50 people) may get more leverage from payment-process controls (callback verification, dual approval) than from a dedicated training platform. Young company (founded 2025) — diligence product maturity and contract terms.

## Competitors / alternatives

- [doppel](doppel.md) — external digital-risk protection / impersonation detection (outward-facing vs Adaptive's inward training).
- [reality-defender](reality-defender.md), [getreal](getreal.md), [pindrop](pindrop.md) — deepfake/synthetic-media detection (detection vs training).
- Incumbent security-awareness-training vendors (e.g. KnowBe4, Proofpoint) — not yet covered here; the legacy category Adaptive is attacking.

## Open questions / to verify
- Exact integration set (IdP/SSO, SIEM, HRIS) — not confirmed from primary sources.
- Pricing / packaging and whether deepfake-call simulation is a separate module.
- Real-world efficacy vs incumbent awareness-training (independent evidence, not vendor claims).

## Sources
- [Adaptive Security Raises $43M from a16z and OpenAI Startup Fund (PR Newswire)](https://www.prnewswire.com/news-releases/adaptive-security-raises-43m-from-a16z-and-openai-startup-fund-to-combat-ai-powered-cyber-attacks-including-deepfakes-vishing-and-smishing-302417695.html) — fetched 2026-06-28 — supports: Series A $43M, a16z + OpenAI Startup Fund co-lead (2025-04-02), product scope, CEO Brian Long; confidence: high
- [OpenAI Fund Extends Investment in Adaptive Security, Raising Total to $55M in Series A (PR Newswire)](https://www.prnewswire.com/news-releases/openai-fund-extends-investment-in-adaptive-security-raising-total-to-55-million-in-series-a-302549706.html) — fetched 2026-06-28 — supports: OpenAI follow-on, $55M Series A total (2025-09-09); confidence: high
- [Adaptive Security Raises $81M Series B to Stop AI-Powered Cyber Threats (PR Newswire)](https://www.prnewswire.com/news-releases/adaptive-security-raises-81-million-series-b-to-stop-ai-powered-cyber-threats-302643174.html) — fetched 2026-06-28 — supports: Series B $81M Bain-led (2025-12-16), $146.5M total, HQ New York, founders, customers, founded 2025; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed OpenAI Startup Fund co-led/extended Series A (primary PR Newswire, Apr & Sep 2025) and Bain-led $81M Series B (Dec 2025, $146.5M total); independent (no M&A); founded 2025, HQ New York, founders Brian Long & Andrew Jones; SaaS human-layer training/simulation; set hedge_fund_fit medium, trifecta untrusted-input, ownership_confidence high.
