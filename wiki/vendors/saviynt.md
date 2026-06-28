---
type: vendor
name: Saviynt
slug: saviynt
categories: [identity-governance]
layer: foundation
aliases: [Saviynt Enterprise Identity Cloud, EIC]
website: https://saviynt.com
founded: 2010
hq: El Segundo, California, USA
ownership: independent
ownership_detail: Private, VC/PE-backed; $700M Series B growth round (Dec 2025) led by KKR at ~$3B valuation
ownership_confidence: high
funding_total: ~$870M
last_funding: Series B (growth), $700M, Dec 2025 (KKR-led)
deployment: [saas]
target_customer: large enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity-governance, iga, cloud-pam, converged-identity]
---

# Saviynt

> Researched 2026-06-28. Primary category: [[identity-governance]].

**One-liner** — Cloud-native converged identity security platform: IGA plus privileged access and app/data access governance in one SaaS, the main challenger to SailPoint.

## What it does
Saviynt's Enterprise Identity Cloud converges several identity disciplines that legacy vendors sell separately: identity governance & administration (access requests, certifications, lifecycle, SoD), cloud privileged access management (PAM), application access governance (deep ERP/SoD controls, e.g. SAP), and third-party/non-human identity governance — increasingly with AI/agent identity. The pitch is one cloud platform instead of stitched-together point tools.

## Where it sits in the stack
The [[identity-governance]] foundation (IGA/ISPM). It addresses the **sensitive-data** leg of the lethal trifecta by governing and attesting entitlements — the access substrate AI assistants and [[entitlement-aware-rag]] must inherit.

## Deployment & architecture
Cloud-native SaaS (born in the cloud, unlike SailPoint's on-prem IdentityIQ heritage). Connects to IdPs ([[microsoft-entra]], [[okta]], [[ping-identity]]), HR, cloud platforms, and enterprise apps; notable depth in SAP/ERP access controls and cloud PAM.

## Positioning & differentiators
Known for **convergence** (IGA + PAM + app-access in one platform) and strength in application/ERP access governance and regulated-industry compliance. Direct competitor to [[sailpoint]]; differentiates on single-platform breadth and cloud-native architecture. Heavier and more compliance-oriented than automation-first challengers [[lumos]]/[[conductorone]] and visibility-first [[veza]].

## Ownership, funding & M&A
Independent, private company. Raised a **$700M Series B growth round in December 2025 at ~$3B valuation, led by KKR** (with Sixth Street Growth, TenEleven, and existing Carrick Capital); ~$870M total raised. Founded 2010, HQ El Segundo, CA. No acquisition; ownership confidence high. (No seed M&A flag; ownership remains independent.)

## CTO / hedge-fund lens
**Day-2**, same logic as [[sailpoint]]: a governance/compliance layer added after IdP/SIEM/DLP basics, moving toward Day-1 under SR 11-7-style model-risk or heavy-RAG regimes where entitlements must be proven and recertified. Convergence (governance + PAM in one tool) can simplify procurement for a mid-to-large fund that wants fewer vendors. For a small fund, still likely heavier than necessary.

## Competitors / alternatives
[[sailpoint]], [[veza]], [[conductorone]], [[lumos]]. Bundled option: [[microsoft-entra]] (Entra ID Governance). PASM/secrets neighbor: [[cyberark]].

## Open questions / to verify
- Depth/maturity of agent and non-human identity governance relative to newer NHI-focused vendors.

## Sources
- [Saviynt Raises $700M at ~$3B Valuation in KKR-Led Round — PR Newswire](https://www.prnewswire.com/news-releases/saviynt-raises-700m-at-approximately-3b-valuation-in-kkr-led-round-to-establish-identity-security-as-the-foundation-for-the-ai-era-302636194.html) — fetched 2026-06-28 — supports: private ownership, $700M Dec 2025 round, ~$3B valuation, HQ; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent private (no M&A); $700M KKR-led round Dec 2025 at ~$3B. Ownership independent confirmed, confidence high. Day-2, medium hedge-fund fit.
