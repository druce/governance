---
type: vendor
name: Wing Security
slug: wing-security
categories: [sspm]
layer: foundation
aliases: []
website: "https://wing.security"
founded: 2020
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: "Seed hint of acquisition by Zscaler COULD NOT be confirmed (no Zscaler/primary source). Wing issued its own press release as an independent company on 2025-09-30; appears independent as of 2026-06-28."
ownership_confidence: low
funding_total: ~$26M
last_funding: Series A $20M (Mar 2022), led by GGV Capital
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sspm, itdr, shadow-ai, saas-security]
---

# Wing Security

> Agentless, API-first SaaS security: discovers all SaaS and AI apps, hardens their configuration and OAuth posture, and detects identity threats (ITDR) — recently repositioned as an AI-security-centric platform.

**One-liner** — An SSPM + SaaS identity-threat-detection platform that inventories SaaS and AI apps, fixes risky configuration and OAuth grants, and watches for account takeover and malicious-app activity.

## What it does

Wing combines three jobs in one platform: (1) **SSPM** — continuous discovery of every SaaS app, including shadow IT and shadow AI, with vendor context and data-flow mapping and misconfiguration hardening; (2) **AI security & governance** — AI-specific guardrails such as access scopes, data-retention controls, and OAuth token hygiene for AI-enabled apps; and (3) **threat detection & response (ITDR)** — real-time detection of malicious or compromised apps, suspicious automation, password spraying, account takeovers, and risky OAuth behavior. In September 2025 Wing publicly repositioned from "SSPM vendor" to an **AI-security-centric** company while keeping the SaaS posture core (vendor framing; marketing).

## Where it sits in the stack

Primary category [sspm](../categories/sspm.md); with its AI-governance guardrails and shadow-AI discovery it also overlaps [ai-access-governance](../categories/ai-access-governance.md). Layer: foundation.

Lethal-trifecta role: **sensitive-data** and **egress** — it governs which SaaS/AI apps can access corporate data and constrains OAuth-granted data flow; the ITDR side adds detection of compromised-identity abuse. Not an inline model/prompt firewall.

## Deployment & architecture

**Agentless, API-first**; connects to IdP and SaaS apps via API/OAuth and is designed to scale from ~1,000 to 50,000+ employees without endpoint agents. No browser extension component (contrast [grip-security](grip-security.md)). Integrates with identity providers for discovery and threat signals.

## Positioning & differentiators

Known for a **multi-layer SSPM + ITDR** combination and, since late 2025, an AI-security emphasis. Nearest neighbors: [grip-security](grip-security.md) (adds a browser extension and leans identity-discovery), [appomni](appomni.md) and [obsidian-security](obsidian-security.md) (deeper config-posture + ITDR for major SaaS estates), [valence-security](valence-security.md) and [reco](reco.md) (SaaS posture + remediation), [nudge-security](nudge-security.md) (OAuth-discovery and offboarding). Differentiation claims are vendor marketing.

## Ownership, funding & M&A

Founded 2020 by Noam Shaar and Galit Lubetzky Sharon (IDF cyber veterans); HQ Tel Aviv, Israel. Total funding ~$26M; most recent disclosed round a $20M Series A (March 2022) led by GGV Capital, with S-Capital, Harmony Partners, and Silicon Valley CISO Investments Group. CEO: Galit Lubetzky Sharon.

**M&A — seed hint NOT confirmed.** The seed flagged a possible acquisition by [zscaler](zscaler.md). I could not confirm this against any Zscaler press release, reputable press, or aggregator record as of 2026-06-28. Wing issued its OWN press release as an independent company on 2025-09-30, and no acquisition appears in Crunchbase/Tracxn. Zscaler's actual recent SaaS/AI-security acquisitions are **different** companies (SPLX, Symmetry Systems, Red Canary, SquareX) — none is Wing. Because there is no competing acquirer claim, this is an **unconfirmed hint, not a hard contradiction**. Possible seed confusion with one of Zscaler's other buys. Ownership left **independent / low confidence** pending a primary source.

## CTO / hedge-fund lens

**Day-2.** SSPM/ITDR secures the SaaS apps a fund already runs and is increasingly useful for **shadow-AI discovery** and reining in OAuth grants to AI tools. The agentless, API-first model is attractive for a lean security team (no endpoint rollout). No direct SR 11-7 / model-risk role. Fit is **medium** — sensible for a fund with a broad SaaS estate and an SSO backbone; smaller shops may cover the basics with their IdP. Note the unsettled ownership question when assessing vendor durability.

## Competitors / alternatives

[grip-security](grip-security.md), [appomni](appomni.md), [obsidian-security](obsidian-security.md), [valence-security](valence-security.md), [reco](reco.md), [docontrol](docontrol.md), [nudge-security](nudge-security.md).

## Open questions / to verify

- **Ownership:** confirm or refute any Zscaler (or other) acquisition with a primary source; raise/lower confidence accordingly.
- Funding since 2022 — any later round beyond the ~$26M total?
- Real-world depth of the post-2025 "AI security" capabilities vs. core SSPM/ITDR.

## Sources

- [Wing Security Evolves into an AI Security–Centric Company (press release)](https://www.globenewswire.com/news-release/2025/09/30/3158498/0/en/Wing-Security-Evolves-into-an-AI-Security-Centric-Company-Extends-Platform-to-Govern-and-Protect-SaaS-AI-Applications.html) — fetched 2026-06-28 — supports: platform (SSPM/AI-gov/ITDR), agentless API-first, Tel Aviv HQ, INDEPENDENT as of 2025-09-30; confidence: med (vendor marketing).
- [Wing Security Series A $20M (Calcalist/CTech) + Crunchbase profile](https://www.calcalistech.com/ctechnews/article/rk2811n11m5) — fetched 2026-06-28 — supports: founded 2020 (Shaar, Lubetzky Sharon), ~$26M total, $20M Series A (GGV Capital, Mar 2022), no acquisition on record; confidence: med (press + aggregator).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2020, Tel Aviv, ~$26M raised ($20M Series A led by GGV Capital), SSPM+ITDR repositioned to AI-security-centric (Sept 2025). Seed's Zscaler-acquisition hint COULD NOT be confirmed and no different acquirer found (Wing self-published as independent 2025-09-30) — kept ownership independent/low, flagged as open question. Not a hard contradiction (no competing acquirer claim).
