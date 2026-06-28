---
title: Adaptive Shield
type: vendor
name: Adaptive Shield
slug: adaptive-shield
categories: [sspm]
layer: foundation
aliases: [CrowdStrike Falcon Shield]
website: "https://www.adaptive-shield.com"
founded: 2019
hq: Tel Aviv, Israel
ownership: acquired
ownership_detail: "Acquired by CrowdStrike — announced 2024-11-06 at Fal.Con Europe, closed ~Jan 2025 (CrowdStrike fiscal Q4); reported ~$300M. Now CrowdStrike's SSPM offering (Falcon Shield)."
ownership_confidence: high
funding_total: ~$44M (pre-acquisition)
last_funding: "Series A / growth (Insight Partners, Okta Ventures, Vertex Ventures Israel, Blackstone Growth)"
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [sspm, saas-security, itdr, shadow-ai, crowdstrike]
---

# Adaptive Shield

> Primary category: [sspm](../categories/sspm.md). **Acquired by [crowdstrike](crowdstrike.md)** (announced 2024-11-06, closed ~Jan 2025).

**One-liner** — A SaaS Security Posture Management (SSPM) leader — misconfiguration, entitlement, and shadow-app visibility across 150+ SaaS apps — now CrowdStrike's SSPM/SaaS-protection product.

## What it does
Adaptive Shield continuously checks SaaS applications (Microsoft 365, Salesforce, Google Workspace, etc.) for misconfigurations, over-broad entitlements, risky third-party app connections, and identity exposures, for both human and non-human identities. It adds SaaS identity threat detection and response (ITDR) and **GenAI app security** — monitoring AI SaaS apps for config drift and surfacing **shadow AI** adoption. The job: keep your SaaS estate configured securely and spot risky/unsanctioned (AI) apps before they leak data.

## Where it sits in the stack
Foundation layer, [sspm](../categories/sspm.md). It primarily addresses the **sensitive-data** leg of the lethal trifecta (data exposure via SaaS misconfiguration and shadow apps), in the green/yellow trust zones. Its shadow-AI discovery overlaps the [ai-access-governance](../categories/ai-access-governance.md) story, but its core is posture management of SaaS, not inline AI traffic control.

## Deployment & architecture
SaaS, API-based — connects to SaaS apps via their admin APIs/OAuth; agentless. Post-acquisition it is integrated into [crowdstrike](crowdstrike.md) Falcon (branded Falcon Shield / Falcon for SaaS), feeding the same identity and exposure telemetry.

## Positioning & differentiators
- One of the established SSPM pure-plays alongside [appomni](appomni.md), [obsidian-security](obsidian-security.md), [grip-security](grip-security.md), [valence-security](valence-security.md), [wing-security](wing-security.md), [docontrol](docontrol.md).
- Differentiator post-deal: tight coupling with CrowdStrike's identity/cloud telemetry — the "unify cloud and identity with SaaS protection" pitch.
- Shadow-AI discovery is a feature, not a full CASB-for-AI; compare [grip-security](grip-security.md) (which straddles SSPM + shadow-AI) and dedicated [ai-access-governance](../categories/ai-access-governance.md) tools.

## Ownership, funding & M&A
**Seed flag "acq by CrowdStrike" — CONFIRMED.** Announced 2024-11-06 at Fal.Con Europe (Amsterdam); structured predominantly in cash with a vesting stock component; reported ~$300M (SecurityWeek/Calcalist; not officially disclosed). Expected to close in CrowdStrike's fiscal Q4 (~end of January 2025). Pre-acquisition: independent, founded 2019 in Tel Aviv (CEO Maor Bin), ~$44M raised (Insight Partners, Okta Ventures, Vertex Ventures Israel, Blackstone Growth). Confidence: high on the acquisition; medium on exact price.

## CTO / hedge-fund lens
Day-2. SSPM matters if you run a meaningful SaaS estate (most funds do — M365/Google, Salesforce, etc.) and want to catch misconfigurations and shadow apps, including shadow AI. For a CrowdStrike shop it's a natural add-on. For others, weigh against [appomni](appomni.md)/[obsidian-security](obsidian-security.md) or whether your existing CASB/Defender coverage suffices. Not an SR 11-7/model-risk tool.

## Competitors / alternatives
[appomni](appomni.md), [obsidian-security](obsidian-security.md), [grip-security](grip-security.md), [valence-security](valence-security.md), [wing-security](wing-security.md), [docontrol](docontrol.md), [reco](reco.md).

## Open questions / to verify
- Exact close date and final price (press-reported ~$300M).
- Current CrowdStrike product branding (Falcon Shield vs. Falcon for SaaS).

## Sources
- [CrowdStrike and Adaptive Shield Unify Cloud and Identity with SaaS Protection](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-acquires-adaptive-shield-and-integrates-saas-protection/) — fetched 2026-06-28 — supports: acquisition (2024-11-06), SSPM/GenAI capabilities, close in fiscal Q4; confidence: high
- [CrowdStrike to Acquire Adaptive Shield in Reported $300M Deal (SecurityWeek)](https://www.securityweek.com/crowdstrike-to-acquire-adaptive-shield-in-reported-300-million-deal/) — fetched 2026-06-28 — supports: ~$300M value, founded 2019, Tel Aviv, ~$44M raised; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by CrowdStrike (announced 2024-11-06 at Fal.Con Europe, ~$300M, closed ~Jan 2025) — raised ownership_confidence to high. Established founded 2019, HQ Tel Aviv, CEO Maor Bin, ~$44M raised. Filled SSPM/shadow-AI body; set hedge_fund_fit medium.
