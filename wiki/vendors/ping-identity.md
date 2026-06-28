---
type: vendor
name: Ping Identity
slug: ping-identity
categories: [identity-access]
layer: foundation
aliases: [Ping, ForgeRock]
website: https://www.pingidentity.com
founded: 2002
hq: Denver, Colorado, USA
ownership: acquired
ownership_detail: Taken private by Thoma Bravo (~$2.8B, completed Oct 2022); merged with ForgeRock (~$2.3B) into Ping, completed Aug 2023
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted, on-prem, api]
target_customer: large enterprise / regulated (workforce + CIAM)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity, idp, sso, mfa, ciam, thoma-bravo]
---

# Ping Identity

> Researched 2026-06-28. Primary category: [identity-access](../categories/identity-access.md).

**One-liner** — Enterprise identity provider (workforce + customer IAM), now Thoma Bravo-owned and merged with ForgeRock; favored by large/regulated shops needing flexible, often self-hosted deployment.

## What it does
Ping provides identity and access management: SSO, MFA, access management/authorization, directory, and strong customer identity (CIAM) with orchestration ("DaVinci" no-code identity flows). It competes with [okta](okta.md) and [microsoft-entra](microsoft-entra.md) but differentiates on deployment flexibility (SaaS, software, hybrid, on-prem) and customizable orchestration for complex enterprise and B2C use cases. The ForgeRock merger added a heavy-duty access-management and directory lineage popular in telco/finance/government.

## Where it sits in the stack
The [identity-access](../categories/identity-access.md) foundation — the front door. Governs the **sensitive-data** leg of the lethal trifecta via authentication/authorization. Same Day-1 role as its IdP peers; the AI gateway and RAG layer federate to it.

## Deployment & architecture
Unusually flexible for this tier: fully managed SaaS (PingOne), self-managed software, hybrid, or on-prem — which is why regulated buyers that can't go cloud-only choose it. Standards-based (SAML, OIDC, OAuth2, SCIM, FIDO2). Orchestration via PingOne DaVinci.

## Positioning & differentiators
Known for handling complex, customized, high-assurance identity — especially CIAM at scale and deployments that must run in the customer's own environment. Versus [okta](okta.md) (cloud-first neutral) and [microsoft-entra](microsoft-entra.md) (bundled, Microsoft-centric), Ping is the "flexible deployment + deep orchestration" option, with a correspondingly heavier implementation. The ForgeRock absorption consolidated a direct competitor but also created product-overlap rationalization that buyers should diligence.

## Ownership, funding & M&A
**M&A verified.** Private-equity owned by **Thoma Bravo**: Ping (formerly NYSE: PING, 2019 IPO) was taken private by Thoma Bravo for ~$2.8B, completed **October 2022**. Thoma Bravo then acquired **ForgeRock** (~$2.3B, agreed Oct 2022; DOJ-cleared) and **combined ForgeRock into Ping Identity, completed August 2023**. Combined company led by Ping founder/CEO Andre Durand. This matches the seed flag (ForgeRock acq. by Thoma Bravo/Ping). Ownership confidence high. Stub had `ownership: independent` → corrected to `acquired`.

## CTO / hedge-fund lens
**Day-1** as an IdP choice, but Ping skews toward larger/regulated enterprises with complex requirements; a typical 50–500-person fund usually defaults to Entra (bundled) or Okta (neutral SaaS) rather than Ping's heavier, deployment-flexible stack. Consider Ping if the fund has on-prem/hybrid constraints, demanding CIAM, or already runs Ping/ForgeRock. PE ownership and the post-merger product rationalization are worth weighing for roadmap stability.

## Competitors / alternatives
[okta](okta.md), [microsoft-entra](microsoft-entra.md). Governance neighbors: [sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md).

## Open questions / to verify
- Post-merger product roadmap: which ForgeRock vs Ping components are strategic vs being sunset.
- Whether Ping returns to public markets under Thoma Bravo (no announced IPO as of 2026-06-28).

## Sources
- [Thoma Bravo Completes Acquisition of ForgeRock; Combines ForgeRock into Ping Identity — Thoma Bravo](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-forgerock-combines-forgerock-into-ping-identity) — fetched 2026-06-28 — supports: Thoma Bravo ownership, ForgeRock merger completion Aug 2023; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Thoma Bravo took Ping private (Oct 2022) and merged ForgeRock into it (Aug 2023). Corrected ownership independent→acquired (PE/Thoma Bravo), confidence high. Day-1, medium hedge-fund fit (skews large/regulated).
