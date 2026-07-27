---
title: Adaptive Shield
type: vendor
name: Adaptive Shield
slug: adaptive-shield
aka: [CrowdStrike Falcon Shield]
primary_category: sspm
also_listed_in: []
website: https://www.crowdstrike.com/en-us/platform/falcon-shield/
founded: 2019
hq: Tel Aviv, Israel
ownership_state: acquired-closed
owner: CrowdStrike
ownership_note: Acquired by CrowdStrike — announced 2024-11-06 at Fal.Con Europe, closed 2024-11-20 (per CrowdStrike FY2025 10-K, Note 12). Accounting purchase price ~$214.4M ($213.7M cash net of cash acquired + $0.7M replacement equity awards); the press-reported "~$300M" also counts $22.8M of vesting stock plus retention grants treated as post-combination comp. Now CrowdStrike's SSPM offering, branded Falcon Shield; adaptive-shield.com redirects to the CrowdStrike product page.
acquisition: {announced: 2024-11-06, closed: 2024-11-20, price: ~$214.4M (10-K purchase price; ~$300M press-reported incl. retention)}
funding_total: ~$44M (pre-acquisition)
last_funding: Series A / growth (Insight Partners, Okta Ventures, Vertex Ventures Israel, Blackstone Growth)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / mid-market
last_verified: 2026-07-27
verify_after: null
tags: [sspm, saas-security, itdr, shadow-ai, crowdstrike]
---

# Adaptive Shield

> Primary category: [sspm](../categories/sspm.md). **Acquired by [crowdstrike](crowdstrike.md)** (announced 2024-11-06, closed 2024-11-20). Brand retired — now **CrowdStrike Falcon Shield**.

**One-liner** — A SaaS Security Posture Management (SSPM) leader — misconfiguration, entitlement, and shadow-app visibility across 150+ SaaS apps — now CrowdStrike's SSPM/SaaS-protection product.

## What it does
Adaptive Shield continuously checks SaaS applications (Microsoft 365, Salesforce, Google Workspace, etc.) for misconfigurations, over-broad entitlements, risky third-party app connections, and identity exposures, for both human and non-human identities. It adds SaaS identity threat detection and response (ITDR) and **GenAI app security** — monitoring AI SaaS apps for config drift and surfacing **shadow AI** adoption. The job: keep your SaaS estate configured securely and spot risky/unsanctioned (AI) apps before they leak data.

## Where it sits in the stack
Foundation layer, [sspm](../categories/sspm.md). It primarily addresses sensitive-data exposure (via SaaS misconfiguration and shadow apps), in the green/yellow trust zones. Its shadow-AI discovery overlaps the [ai-access-governance](../categories/ai-access-governance.md) story, but its core is posture management of SaaS, not inline AI traffic control.

## Deployment & architecture
SaaS, API-based — connects to SaaS apps via their admin APIs/OAuth; agentless. Post-acquisition it is integrated into [crowdstrike](crowdstrike.md) Falcon as **Falcon Shield**, feeding the same identity and exposure telemetry.

## Positioning & differentiators
- One of the established SSPM pure-plays alongside [appomni](appomni.md), [obsidian-security](obsidian-security.md), [grip-security](grip-security.md), [valence-security](valence-security.md), [wing-security](wing-security.md), [docontrol](docontrol.md).
- Differentiator post-deal: tight coupling with CrowdStrike's identity/cloud telemetry — the "unify cloud and identity with SaaS protection" pitch.
- Shadow-AI discovery is a feature, not a full CASB-for-AI; compare [grip-security](grip-security.md) (which straddles SSPM + shadow-AI) and dedicated [ai-access-governance](../categories/ai-access-governance.md) tools.

## Ownership, funding & M&A
**Seed flag "acq by CrowdStrike" — CONFIRMED.** Announced 2024-11-06 at Fal.Con Europe (Amsterdam) and **closed 2024-11-20** — well inside CrowdStrike's fiscal Q4, and two months earlier than the "~Jan 2025" this page previously estimated from the press release's "expected to close in fiscal Q4" language. Per CrowdStrike's FY2025 10-K (Note 12), the accounting purchase price was **~$214.4M**: $213.7M in cash net of $13.7M cash acquired, plus $0.7M of replacement equity awards attributable to pre-acquisition service; allocated to $31.1M of intangibles (developed technology $23.6M, customer relationships $7.5M), $7.7M of net tangible liabilities, and $191.0M of goodwill. The widely reported "~$300M" is not wrong so much as a different number: the same 10-K discloses $22.8M of Class A stock issued to Adaptive Shield stockholders subject to service-based vesting, plus retention RSU/PSU grants, all excluded from the purchase price as post-combination compensation. Pre-acquisition: independent, founded 2019 in Tel Aviv (CEO Maor Bin), ~$44M raised (Insight Partners, Okta Ventures, Vertex Ventures Israel, Blackstone Growth). Confidence: high on the acquisition, close date, and purchase price (SEC-filed primary source).

## CTO / hedge-fund lens
Day-2. SSPM matters if you run a meaningful SaaS estate (most funds do — M365/Google, Salesforce, etc.) and want to catch misconfigurations and shadow apps, including shadow AI. For a CrowdStrike shop it's a natural add-on. For others, weigh against [appomni](appomni.md)/[obsidian-security](obsidian-security.md) or whether your existing CASB/Defender coverage suffices. Not an SR 11-7/model-risk tool.

## Competitors / alternatives
[appomni](appomni.md), [obsidian-security](obsidian-security.md), [grip-security](grip-security.md), [valence-security](valence-security.md), [wing-security](wing-security.md), [docontrol](docontrol.md), [reco](reco.md).

## Open questions / to verify
- ~~Exact close date and final price~~ — resolved 2026-07-27 from CrowdStrike's FY2025 10-K: closed 2024-11-20, ~$214.4M purchase price.
- ~~Current CrowdStrike product branding (Falcon Shield vs. Falcon for SaaS)~~ — resolved 2026-07-27: **Falcon Shield** (adaptive-shield.com redirects to the Falcon Shield product page).

## Sources
- [CrowdStrike and Adaptive Shield Unify Cloud and Identity with SaaS Protection](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-acquires-adaptive-shield-and-integrates-saas-protection/) — fetched 2026-06-28 — supports: acquisition (2024-11-06), SSPM/GenAI capabilities, close in fiscal Q4; confidence: high
- [CrowdStrike to Acquire Adaptive Shield in Reported $300M Deal (SecurityWeek)](https://www.securityweek.com/crowdstrike-to-acquire-adaptive-shield-in-reported-300-million-deal/) — fetched 2026-06-28 — supports: ~$300M press-reported value, founded 2019, Tel Aviv, ~$44M raised; confidence: med
- [CrowdStrike Holdings FY2025 Form 10-K (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1535527/000153552725000009/crwd-20250131.htm) — fetched 2026-07-27 — supports: close date 2024-11-20, ~$214.4M purchase price, purchase-price allocation, $22.8M vesting stock excluded as post-combination comp; confidence: high — cached at `raw/sources/2026-07-27--adaptive-shield--crowdstrike-10k-close-date-and-price.md`
- [Falcon Shield product page (CrowdStrike)](https://www.crowdstrike.com/en-us/platform/falcon-shield/) — fetched 2026-07-27 — supports: live product branding "CrowdStrike Falcon® Shield"; adaptive-shield.com 301 target; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by CrowdStrike (announced 2024-11-06 at Fal.Con Europe, ~$300M, closed ~Jan 2025) — raised ownership_confidence to high. Established founded 2019, HQ Tel Aviv, CEO Maor Bin, ~$44M raised. Filled SSPM/shadow-AI body; set hedge_fund_fit medium.
- [2026-07-27] URL audit: `adaptive-shield.com` now 301-redirects to the live CrowdStrike Falcon Shield product page (`crowdstrike.com/en-us/platform/falcon-shield/`, HTTP 200, "CrowdStrike Falcon® Shield") — standalone brand retired. Updated `website`. Also corrected `acquisition.closed`, which had been a copy of the announce date (2024-11-06): CrowdStrike's FY2025 10-K Note 12 puts the close at **2024-11-20** and the purchase price at **~$214.4M**, not the ~$300M press figure (the difference is $22.8M of vesting stock plus retention grants, excluded as post-combination comp). Both open questions closed.
