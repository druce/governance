---
type: vendor
name: Linx Security
slug: linx-security
categories: [identity-governance, non-human-identity]
layer: foundation
aliases: []
website: https://www.linx.security/
founded: 2023
hq: New York, NY
ownership: independent
ownership_detail: VC-backed; $83M raised across rounds. Series B $50M led by Insight Partners (2026-03-31), with Cyberstarts and Index Ventures.
ownership_confidence: high
funding_total: $83M
last_funding: Series B, $50M, 2026-03-31
deployment: [saas, api]
target_customer: enterprise / regulated (banks, healthcare, Fortune 500)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [iga, ispm, identity, ai-native, non-human-identity]
---

# Linx Security

> **Researched 2026-06-28.** Primary category: [identity-governance](../categories/identity-governance.md).

**One-liner** — An AI-native identity governance (IGA) platform that continuously maps, monitors, and governs every identity in the enterprise — human, non-human, and AI agent — instead of running periodic, form-driven access reviews.

## What it does
Linx is positioned as a modern rebuild of identity governance and administration (IGA). Traditional IGA tools (joiner/mover/leaver workflows, quarterly access certifications) were built for a world of mostly human employees and relatively static apps. Linx's pitch is that the identity estate is now dominated by service accounts, machine identities, and AI agents — which it claims outnumber humans by roughly 80 to 1 — and that governing them requires continuous, automated discovery and correlation rather than spreadsheet-driven recerts. It markets "Linx Autopilot," an autonomous agent that drives identity governance tasks.

## Where it sits in the stack
Foundation layer, [identity-governance](../categories/identity-governance.md) (IGA/ISPM), with a strong [non-human-identity](../categories/non-human-identity.md) angle. It sits downstream of the IdP ([microsoft-entra](microsoft-entra.md), [okta](okta.md)) and reconciles identities/entitlements across the estate. Lethal-trifecta role: none directly — this is an access-hygiene and least-privilege control, not a prompt/data/egress firewall. It reduces blast radius by limiting standing access and over-entitlement.

## Deployment & architecture
SaaS, integrating via API/connectors to IdPs, cloud, and SaaS apps to build and continuously update an identity graph. (Exact connector catalog not verified.)

## Positioning & differentiators
"AI-native" continuous governance vs the legacy suites ([sailpoint](sailpoint.md), [saviynt](saviynt.md)) and the newer access-request/least-privilege challengers ([lumos](lumos.md), [conductorone](conductorone.md)). Its explicit framing around AI agents and non-human identities overlaps with the visibility pitch of [hydden](hydden.md) and the access-graph pitch of [veza](veza.md). Nearest neighbors in spirit: [veza](veza.md) (authorization/entitlement graph), [conductorone](conductorone.md), [lumos](lumos.md).

## Ownership, funding & M&A
Independent, VC-backed. Founded 2023 by Israel Duanis (CEO) and Niv Goldenberg; HQ New York. $83M total funding; $50M Series B led by Insight Partners announced 2026-03-31, with continued participation from Cyberstarts and Index Ventures. No M&A. Confidence high (primary announcement + Insight Partners).

## CTO / hedge-fund lens
Day-2. IGA is a real need for a regulated shop (access certifications, least privilege, SOX/audit evidence), but Linx is young (founded 2023) — a credible modernization play, not yet a safe default. A 50-person fund likely does not need a dedicated IGA platform on day one; identity governance can start inside Entra/Okta. Worth watching if you have a sprawling SaaS estate and a growing fleet of service accounts/agents. Not a model-risk (SR 11-7) tool.

## Competitors / alternatives
[sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md), [conductorone](conductorone.md), [lumos](lumos.md), [hydden](hydden.md), [silverfort](silverfort.md).

## Open questions / to verify
- Concrete connector/integration list and whether it does access certifications vs only visibility.
- Real customer references in financial services; production maturity.
- Pricing/deployment model specifics.

## Sources
- [Linx Security Raises $50M Series B](https://www.linx.security/blog/linx-security-raises-50m-series-b) — fetched 2026-06-28 — supports: funding, founders, HQ, founding year, AI/NHI positioning; confidence: high.
- [Insight Partners — Linx Series B](https://www.insightpartners.com/ideas/linx-security-raises-50m-series-b-as-identity-becomes-securitys-biggest-failure-point/) — fetched 2026-06-28 — supports: lead investor, round; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent/VC-backed, $83M total, $50M Series B (Insight Partners, 2026-03-31), founded 2023 NY by Duanis & Goldenberg, AI-native IGA + NHI positioning. ownership_confidence raised to high.
