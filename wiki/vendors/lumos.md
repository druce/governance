---
type: vendor
name: Lumos
slug: lumos
categories: [identity-governance]
layer: foundation
aliases: []
website: https://www.lumos.com
founded: 2020
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Private, VC-backed; ~$65M raised, latest Series B $35M (May 2024) led by Scale Venture Partners (a16z, Harpoon, Neo)
ownership_confidence: high
funding_total: ~$65M
last_funding: Series B, $35M, May 2024 (Scale Venture Partners-led)
deployment: [saas]
target_customer: mid-market / fast-growing tech (cloud-forward)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity-governance, iga, saas-management, access-reviews]
---

# Lumos

> Researched 2026-06-28. Primary category: [identity-governance](../categories/identity-governance.md).

**One-liner** — Automation-first identity governance and SaaS-access management, pitched as an "Autonomous Identity Platform" for cloud-forward companies.

## What it does
Lumos started as a SaaS management / internal app-store with self-service access requests, then expanded into identity governance (IGA): access reviews/certifications, lifecycle (joiner/mover/leaver), policy automation, least-privilege, and increasingly non-human/agent identity and "agentic" access reviews. The pitch is automating routine identity work (requests, reviews, deprovisioning) that legacy IGA does manually and slowly, plus surfacing SaaS spend/usage as a byproduct.

## Where it sits in the stack
The [identity-governance](../categories/identity-governance.md) foundation. Addresses the **sensitive-data** leg of the lethal trifecta by governing and certifying entitlements — the access substrate AI assistants and [entitlement-aware-rag](../categories/entitlement-aware-rag.md) inherit. SaaS-discovery roots also give it some shadow-IT/shadow-AI visibility adjacency.

## Deployment & architecture
SaaS. Integrates with IdPs ([microsoft-entra](microsoft-entra.md), [okta](okta.md)), HR systems, and a broad catalog of SaaS apps to discover usage, drive access requests/reviews, and automate provisioning/deprovisioning. Workflow-centric (Slack-native approvals) and automation-forward.

## Positioning & differentiators
Known for combining **SaaS management + IGA** in an automation-first package, now marketed as autonomous/AI-driven identity. Lighter and quicker to deploy than [sailpoint](sailpoint.md)/[saviynt](saviynt.md); closest peer is [conductorone](conductorone.md) (both modern, automation-first IGA challengers), with Lumos carrying more SaaS-spend/management DNA. Customers skew fast-growing tech (Pinterest, GitHub, Anduril cited as references — marketing).

## Ownership, funding & M&A
Independent, private, VC-backed. ~$65M raised across two rounds; latest is a **$35M Series B (May 2024)** led by Scale Venture Partners with a16z, Harpoon Ventures, and Neo. Founded 2020 by Andrej Safundzic and Leo Mehr; HQ San Francisco. No acquisition and no confirmed Series C as of 2026-06-28. Ownership confidence high. (No seed M&A flag.)

## CTO / hedge-fund lens
**Day-2.** Like [conductorone](conductorone.md), a lighter, faster IGA option for a small-to-mid hedge fund than legacy incumbents, with the bonus of SaaS discovery/spend visibility (useful for catching shadow SaaS and shadow AI). Fit improves under audit/model-risk or RAG, where access certification matters. Trade-offs: youngest/smallest of this cohort, less compliance pedigree and connector depth than [sailpoint](sailpoint.md) for large regulated estates; diligence whether its governance depth matches the fund's audit requirements.

## Competitors / alternatives
[conductorone](conductorone.md), [veza](veza.md), [sailpoint](sailpoint.md), [saviynt](saviynt.md). Bundled option: [microsoft-entra](microsoft-entra.md) (Entra ID Governance). SaaS-discovery adjacency: [nudge-security](nudge-security.md), [grip-security](grip-security.md).

## Open questions / to verify
- Depth of formal access-certification/compliance reporting vs incumbents; any funding since the 2024 Series B.

## Sources
- [Lumos Secures $35M Series B — Lumos blog](https://www.lumos.com/blog/lumos-secures-35m-series-b-funding-to-unify-the-saas-and-identity-management-industries) — fetched 2026-06-28 — supports: $35M Series B (2024, Scale Venture Partners), founders, HQ, private; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent private; ~$65M raised, $35M Series B (May 2024). Ownership independent confirmed, confidence high. Day-2, medium hedge-fund fit (lightweight IGA + SaaS management).
