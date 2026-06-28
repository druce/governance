---
type: vendor
name: SailPoint
slug: sailpoint
categories: [identity-governance, data-access-governance]
layer: foundation
aliases: [SailPoint Technologies, IdentityNow, IdentityIQ, Atlas]
website: "https://www.sailpoint.com"
founded: 2005
hq: Austin, Texas, USA
ownership: public
ownership_detail: Re-IPO'd on Nasdaq (SAIL) Feb 2025; ~88% owned/controlled by Thoma Bravo post-IPO
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted, on-prem]
target_customer: large enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity-governance, iga, access-certification, thoma-bravo]
---

# SailPoint

> Researched 2026-06-28. Primary category: [identity-governance](../categories/identity-governance.md).

**One-liner** — The category-defining identity governance (IGA) vendor: who has access to what, access certifications, and joiner/mover/leaver lifecycle at enterprise scale.

## What it does
SailPoint governs identity: it discovers and certifies access, runs access reviews/recertifications, automates provisioning/deprovisioning across the joiner-mover-leaver lifecycle, enforces separation-of-duties policy, and increasingly applies AI/ML to access risk. Its modern stack is the cloud Identity Security Cloud (Atlas; formerly IdentityNow); IdentityIQ is the legacy on-prem product still in regulated estates. Extends to data access governance (SailPoint DAS) over unstructured data.

## Where it sits in the stack
The [identity-governance](../categories/identity-governance.md) foundation (IGA/ISPM), and [data-access-governance](../categories/data-access-governance.md) for files/data. It addresses the **sensitive-data** leg of the lethal trifecta by controlling and attesting *who can reach what* — the entitlement substrate that AI assistants and [entitlement-aware-rag](../categories/entitlement-aware-rag.md) must inherit so an LLM never surfaces data the user can't see.

## Deployment & architecture
SaaS (Atlas/Identity Security Cloud) plus legacy on-prem (IdentityIQ). Connects to IdPs ([microsoft-entra](microsoft-entra.md), [okta](okta.md), [ping-identity](ping-identity.md)), HR systems, and hundreds of target apps for provisioning and access collection. Sits above the IdP: the IdP authenticates, SailPoint governs/certifies.

## Positioning & differentiators
The incumbent enterprise IGA leader — deepest connector catalog, strongest certification/compliance pedigree, the safe choice for large regulated buyers. Trade-off: heavyweight and implementation-intensive versus newer automation-first challengers ([lumos](lumos.md), [conductorone](conductorone.md)) and visibility-first platforms ([veza](veza.md)). Competes head-on with [saviynt](saviynt.md).

## Ownership, funding & M&A
**Verified.** SailPoint returned to public markets on **Nasdaq (ticker SAIL) in February 2025**, raising $1.38B (60M shares at $23). It first IPO'd in 2017, was taken private by **Thoma Bravo** in 2022 (~$6.9B), and re-IPO'd in 2025 — but Thoma Bravo retained ~**88%** and board control post-IPO, so it's public-but-PE-controlled. Matches the brief's re-IPO note. Ownership set public, confidence high. (Stub had `independent` → corrected to `public`.)

## CTO / hedge-fund lens
**Day-2** for most funds — IGA is a maturity/compliance layer you add after the IdP, SIEM, and DLP basics. It becomes **Day-1-ish under SR 11-7-style model-risk / audit regimes or heavy RAG**, where you must prove access entitlements and recertify them. For a 50–500-person fund, SailPoint is often heavier than needed; lighter automation-first tools may fit better unless the fund is large, regulated, or already standardized on it.

## Competitors / alternatives
[saviynt](saviynt.md), [veza](veza.md), [conductorone](conductorone.md), [lumos](lumos.md). Microsoft's bundled option: [microsoft-entra](microsoft-entra.md) (Entra ID Governance). Data-access neighbors: [varonis](varonis.md), [cyera](cyera.md).

## Open questions / to verify
- Pace of migration from legacy IdentityIQ to Atlas; agent/NHI governance roadmap depth.

## Sources
- [Cybersecurity firm SailPoint's IPO raises $1.38 billion (Reuters via U.S. News)](https://money.usnews.com/investing/news/articles/2025-02-13/cybersecurity-firm-sailpoints-ipo-raises-1-38-billion-in-us-ipo) — fetched 2026-06-28 — supports: Feb 2025 Nasdaq re-IPO, Thoma Bravo ~88% control, 2017 IPO / 2022 take-private history; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Feb 2025 Nasdaq re-IPO under Thoma Bravo (~88% retained). Corrected ownership independent→public, confidence high. Day-2 (Day-1 under model-risk/RAG), medium hedge-fund fit.
