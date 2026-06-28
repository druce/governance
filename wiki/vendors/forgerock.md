---
type: vendor
name: ForgeRock
slug: forgerock
categories: [identity-access]
layer: foundation
aliases: [ForgeRock Identity Platform]
website: "https://www.pingidentity.com"
founded: 2010
hq: San Francisco, USA (origins in Norway)
ownership: acquired
ownership_detail: "Acquired by Thoma Bravo (~$2.3B, $23.25/share) and merged into Ping Identity; announced 2022-10-11, closed 2023-08-23. No longer an independent brand."
ownership_confidence: high
funding_total: "n/a (was public, NYSE: FORG, before take-private)"
last_funding: IPO Sep 2021
deployment: [saas, self-hosted, on-prem]
target_customer: enterprise / regulated (workforce + CIAM)
hedge_fund_fit: low
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [iam, ciam, identity-access, thoma-bravo, ping-identity]
---

# ForgeRock

> **One-liner** — An enterprise identity & access management platform (workforce + customer IAM, governance, orchestration); acquired by Thoma Bravo and folded into [ping-identity](ping-identity.md) — effectively no longer a standalone brand.

**Categories** — [identity-access](../categories/identity-access.md)

## What it does
ForgeRock provided a full IAM platform: access management/SSO, customer identity (CIAM), identity governance, and identity orchestration — built originally on the open-source OpenAM/OpenIDM lineage. The job: be the front door that authenticates and authorizes humans (and increasingly workloads) into applications, including AI assistants. It served 1,300+ organizations at acquisition.

## Where it sits in the stack
Foundation layer, [identity-access](../categories/identity-access.md) — the human/agent front door that everything else gates on. Lethal-trifecta leg: **none directly**, but it is the identity substrate that access governance, [entitlement-aware-rag](../categories/entitlement-aware-rag.md) and agent authz all depend on. Adjacent to [identity-governance](../categories/identity-governance.md) and [non-human-identity](../categories/non-human-identity.md).

## Deployment & architecture
SaaS (ForgeRock Identity Cloud) plus self-managed/on-prem deployments — historically stronger than pure-SaaS rivals at complex on-prem/hybrid and CIAM scenarios. Standards-based (OIDC, SAML, OAuth2, SCIM).

## Positioning & differentiators
Was known for deployment flexibility (self-managed + cloud), heavy-duty CIAM, and identity orchestration. Nearest neighbors: [ping-identity](ping-identity.md) (now the parent brand), [okta](okta.md), [microsoft-entra](microsoft-entra.md). Post-merger, ForgeRock capabilities are being consolidated into the Ping Identity portfolio, so it is increasingly a feature set under Ping rather than a separate product to shop.

## Ownership, funding & M&A
**Verified — both seed flags confirmed.** Acquired by **Thoma Bravo** in an all-cash deal (~**$2.3B**, **$23.25/share**) and **merged into Ping Identity** (also Thoma Bravo-owned). Announced **2022-10-11**; stockholder approval 2023-01-12; **closed 2023-08-23**. Delisted from NYSE (was FORG). Founded 2010 (origins in Norway, ex-Sun Microsystems team); HQ San Francisco; previously public (IPO Sep 2021). Ownership confidence **high**.

## CTO / hedge-fund lens
**Day-1 in the sense that an IdP is table-stakes — but you would not buy "ForgeRock" net-new today**; you would evaluate [ping-identity](ping-identity.md) (the surviving brand), [microsoft-entra](microsoft-entra.md) or [okta](okta.md). ForgeRock remains relevant mainly to existing customers managing the migration/consolidation into Ping. For a typical fund already on Entra or Okta, this is not a fresh buying decision. Note the Thoma Bravo identity roll-up (Ping + ForgeRock + others) as a market-concentration trend.

## Competitors / alternatives
[ping-identity](ping-identity.md), [okta](okta.md), [microsoft-entra](microsoft-entra.md), [sailpoint](sailpoint.md) (governance overlap), [saviynt](saviynt.md).

## Open questions / to verify
- Long-term product roadmap: which ForgeRock components survive vs are sunset under Ping.
- Migration path/timeline pushed to existing ForgeRock customers.

## Sources
- [Thoma Bravo Completes Acquisition of ForgeRock; Combines into Ping Identity](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-forgerock-combines-forgerock-into-ping-identity) — fetched 2026-06-28 — supports: acquirer Thoma Bravo, $2.3B, $23.25/share, close 2023-08-23, merge into Ping; confidence: high
- [Thoma Bravo Completes Acquisition of ForgeRock (PR Newswire)](https://www.prnewswire.com/news-releases/thoma-bravo-completes-acquisition-of-forgerock-combines-forgerock-into-ping-identity-301908059.html) — fetched 2026-06-28 — supports: deal terms, 1,300+ orgs, IAM positioning; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified BOTH seed flags — Thoma Bravo acquisition (~$2.3B, closed 2023-08-23) AND merger into Ping Identity; raised ownership_confidence low→high; filled founding/HQ, noted brand consolidation under Ping.
