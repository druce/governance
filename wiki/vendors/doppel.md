---
title: Doppel
type: vendor
name: Doppel
slug: doppel
categories: [anti-deepfake]
layer: foundation
aliases: [Doppel Vision]
website: "https://www.doppel.com"
founded: 2022
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: VC-backed independent; ~$600M valuation at Series C (2025-11-19). No acquisition.
ownership_confidence: high
funding_total: $124M (as of 2025-11-19)
last_funding: Series C, $70M, 2025-11-19 (led by Bessemer Venture Partners)
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [deepfake, digital-risk-protection, impersonation, brand-protection, executive-protection, social-engineering]
---

# Doppel

> Primary category: [anti-deepfake](../categories/anti-deepfake.md).

**One-liner** — AI-driven digital risk protection / "social engineering defense": continuously scans the open web, social media, app stores, paid ads, domains, and the dark web for impersonation of your brand and executives — fake accounts, lookalike domains, phishing pages, deepfakes — and drives takedowns.

## What it does

Doppel hunts external impersonation. Autonomous AI agents (the platform is branded "Doppel Vision") crawl social networks, messaging apps, paid ad networks, domain registrations, and dark-web sources to find fake profiles, spoofed brands, fraudulent ads, phishing infrastructure, and deepfake content impersonating a company or its leaders, then prioritizes and pursues takedowns. The company frames the broader category as "social engineering defense (SED)," spanning brand protection, executive protection, phishing-page detection, and — via integration — deepfake media verification. It has also extended into phishing simulation, security awareness training, and email security with deepfake-driven simulations (vendor-stated). Deepfake media authentication is delivered partly through a partnership with [getreal](getreal.md) (GetReal Security) to verify videos/images/audio.

## Where it sits in the stack

Sits in [anti-deepfake](../categories/anti-deepfake.md) at the foundation layer. Like [adaptive-security](adaptive-security.md), this is a **perimeter / brand-and-people** control rather than an inline AI-application guardrail — it doesn't sit in the model/prompt path. Lethal-trifecta relevance is **untrusted-input adjacent**: it reduces exposure to externally-originated impersonation and phishing aimed at staff and customers, but does not break a trifecta leg inside an AI system. Trust-zone relevance: the external untrusted internet (red zone), monitoring how your identity is abused outside your perimeter.

## Deployment & architecture

SaaS. The product is a monitoring + takedown service: AI agents continuously scan external channels, surface impersonation/deepfake threats in a console, and handle takedown workflows. Deepfake media verification via the [getreal](getreal.md) partnership. Integration details (SIEM/SOAR, ticketing, brand/IP feeds) not fully confirmed from the primary sources cited here.

## Positioning & differentiators

Positioned as the AI-native digital-risk-protection (DRP) / social-engineering-defense platform, distinguished by autonomous-agent scanning breadth (social, ads, domains, dark web) and Fortune 500 traction in financial services, energy, tech, healthcare, and media (vendor-stated). Differs from [adaptive-security](adaptive-security.md), which points inward (training your own employees) — Doppel points outward (finding others impersonating you). Differs from pure media-authentication vendors [reality-defender](reality-defender.md), [getreal](getreal.md), and [pindrop](pindrop.md): Doppel is a monitoring-and-takedown service that *consumes* deepfake detection (partnering with GetReal) rather than being primarily a detection engine. CrowdStrike CEO George Kurtz invested personally in the Series C (vendor-stated).

## Ownership, funding & M&A

Independent, VC-backed. No acquisition (seed carried no M&A flag; none found). Founded **2022**; HQ **San Francisco**; co-founders **Kevin Tian** (CEO) and **Rahul Madduluri** (CTO), both ex-Uber engineers.

Funding, confirmed against primary/reputable sources:
- **Series B — $35M**, led by **Bessemer Venture Partners** (with 9Yards Capital, Sozo Ventures); brought total to ~$54.4M at ~$205M valuation (SecurityWeek).
- **Series C — $70M**, announced **2025-11-19**, led by **Bessemer Venture Partners**, at **>$600M valuation**; **total funding $124M** (Doppel press release). Returning investors include a16z, South Park Commons, Script Capital, 9Yards, Sozo, Strategic Cyber Ventures; new investors include George Kurtz and NTT DOCOMO Ventures.

## CTO / hedge-fund lens

**Day-2, medium fit.** Brand/executive impersonation — fake "fund" accounts soliciting investors, spoofed domains, deepfake videos of a portfolio manager promoting a scam — is a genuine reputational and fraud risk for asset managers, and DRP/takedown is the control for it. But it's an external-brand-protection service, not part of the internal AI-application security stack, and is most valuable for firms with a public-facing brand and retail/investor surface; a small, low-profile fund may not need it. No direct SR 11-7 / model-risk relevance. Evaluate against incumbent DRP vendors (ZeroFox, Netcraft, Recorded Future, BforeAI) — not yet covered here.

## Competitors / alternatives

- [adaptive-security](adaptive-security.md) — inward employee training/simulation vs Doppel's outward impersonation monitoring.
- [getreal](getreal.md) — deepfake media authentication; a Doppel *partner* for media verification as well as a category neighbor.
- [reality-defender](reality-defender.md), [pindrop](pindrop.md) — deepfake/synthetic-media and voice detection.
- Incumbent DRP vendors (ZeroFox, Netcraft, Recorded Future) — not yet covered here.

## Open questions / to verify
- Exact founding details and whether HQ is San Francisco vs Covina, CA (sources vary; SF is the operating HQ).
- Integration set (SIEM/SOAR, ticketing) and how takedown SLAs work.
- Scope/depth of the GetReal partnership vs native deepfake detection.

## Sources
- [Doppel Raises Series C to Meet Rising Demand for AI-Driven Social Engineering Defense (Doppel press release)](https://www.doppel.com/company/press-releases/doppel-raises-series-c-to-meet-rising-demand-for-ai-driven-social-engineering-defense) — fetched 2026-06-28 — supports: Series C $70M Bessemer-led (2025-11-19), >$600M valuation, $124M total, HQ San Francisco, CEO Kevin Tian, product scope; confidence: high
- [Doppel Banks $35M for AI-Based Digital Risk Protection (SecurityWeek)](https://www.securityweek.com/doppel-banks-35m-for-ai-based-digital-risk-protection/) — fetched 2026-06-28 — supports: Series B $35M Bessemer-led, ~$54.4M total/~$205M valuation, founded 2022, founders Kevin Tian & Rahul Madduluri, Doppel Vision agents, GetReal deepfake-detection partnership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent VC-backed (no M&A); founded 2022, HQ San Francisco, co-founders Kevin Tian (CEO) & Rahul Madduluri (CTO); Series C $70M Bessemer-led at >$600M valuation, $124M total (2025-11-19); DRP/social-engineering-defense (web/social/ads/domains/dark web) + deepfake verification via GetReal partner; set hedge_fund_fit medium, trifecta untrusted-input, ownership_confidence high.
