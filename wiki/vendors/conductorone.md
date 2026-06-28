---
title: ConductorOne
type: vendor
name: ConductorOne
slug: conductorone
categories: [identity-governance, data-access-governance]
layer: foundation
aliases: [C1]
website: "https://www.conductorone.com"
founded: 2020
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Private, VC-backed; $79M Series B (Oct 2025) led by Greycroft, with CrowdStrike Falcon Fund, Accel, Felicis
ownership_confidence: high
funding_total: ~$111M
last_funding: Series B, $79M, Oct 2025 (Greycroft-led)
deployment: [saas]
target_customer: mid-market / enterprise (cloud-forward)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity-governance, iga, access-reviews, jit-access, ispm]
---

# ConductorOne

> Researched 2026-06-28. Primary category: [identity-governance](../categories/identity-governance.md).

**One-liner** — Modern, automation-first identity governance: access reviews, just-in-time access requests, and identity security posture for the cloud/agentic era.

## What it does
ConductorOne automates the access lifecycle: self-service access requests with policy-based approvals, just-in-time (JIT) and time-bound grants, automated access reviews/certifications, least-privilege analysis, and identity security posture management (ISPM). It increasingly targets non-human and agent identity governance. The pitch is a lighter, faster, more automated alternative to legacy IGA for cloud-forward companies.

## Where it sits in the stack
The [identity-governance](../categories/identity-governance.md) foundation plus [data-access-governance](../categories/data-access-governance.md). Addresses the **sensitive-data** leg of the lethal trifecta by controlling and certifying entitlements (and shrinking standing privilege via JIT) — the access substrate AI assistants and [entitlement-aware-rag](../categories/entitlement-aware-rag.md) inherit.

## Deployment & architecture
SaaS. Connects to IdPs ([microsoft-entra](microsoft-entra.md), [okta](okta.md)), cloud platforms, and SaaS apps to collect entitlements, drive reviews, and provision JIT access. Workflow/automation-centric (Slack-native approvals, etc.) rather than the heavy connector-and-config model of incumbents.

## Positioning & differentiators
Founded by ex-[okta](okta.md) leaders (Alex Bovee, Paul Querna); positions as **AI-native, automation-first IGA** for the agentic era. Lighter and faster to deploy than [sailpoint](sailpoint.md)/[saviynt](saviynt.md); overlaps [lumos](lumos.md) (modern IGA challengers) and [veza](veza.md) on access reviews, though Veza leans visibility/graph while ConductorOne leans workflow/JIT. CrowdStrike Falcon Fund investment signals a security-ecosystem tilt.

## Ownership, funding & M&A
Independent, private, VC-backed. **$79M Series B (October 2025)** led by Greycroft, with new investor CrowdStrike Falcon Fund and existing Accel and Felicis; ~$111M total raised. Founded 2020, HQ San Francisco. No acquisition; ownership confidence high. (No seed M&A flag.)

## CTO / hedge-fund lens
**Day-2**, but a stronger fit than legacy IGA for a small-to-mid hedge fund: lighter weight, automation-first, JIT access reduces standing privilege (a real risk-reducer), and faster to stand up. Becomes more pressing under model-risk/audit or RAG, where you must certify and minimize access. Trade-off vs incumbents: younger company, shallower connector catalog and compliance pedigree than [sailpoint](sailpoint.md) for very large regulated estates.

## Competitors / alternatives
[lumos](lumos.md), [veza](veza.md), [sailpoint](sailpoint.md), [saviynt](saviynt.md). Bundled option: [microsoft-entra](microsoft-entra.md) (Entra ID Governance).

## Open questions / to verify
- Depth of non-human/agent identity governance vs NHI specialists; connector breadth vs incumbents.

## Sources
- [ConductorOne Raises $79 Million Series B — ConductorOne](https://www.conductorone.com/news/press-release/conductorone-raises-79-million-series-b/) — fetched 2026-06-28 — supports: $79M Series B Oct 2025 (Greycroft, CrowdStrike Falcon Fund), ~$111M total, founders, HQ, private; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent private; $79M Series B Oct 2025 (Greycroft-led). Ownership independent confirmed, confidence high. Day-2, medium hedge-fund fit (good lightweight IGA option).
