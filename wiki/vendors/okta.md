---
type: vendor
name: Okta
slug: okta
categories: [identity-access]
layer: foundation
aliases: [Auth0]
website: "https://www.okta.com"
founded: 2009
hq: San Francisco, California, USA
ownership: public
ownership_detail: "Independent public company (Nasdaq: OKTA); IPO April 2017"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise / mid-market (vendor-neutral IdP); Auth0 for CIAM/developers
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity, idp, sso, mfa]
---

# Okta

> Researched 2026-06-28. Primary category: [identity-access](../categories/identity-access.md).

**One-liner** — The leading independent (vendor-neutral) identity provider: SSO, MFA, and lifecycle for the workforce, plus Auth0 for customer/developer identity.

## What it does
Okta authenticates users and apps and brokers access to SaaS and on-prem resources. Two clouds: **Workforce Identity** (SSO, adaptive MFA, lifecycle/provisioning, Identity Governance, and a growing privileged-access and device-access set) for employees/contractors/partners; and **Customer Identity (Auth0)** for developers building login into their own products (CIAM). Its pitch is being a neutral hub that integrates with everything rather than favoring one cloud vendor.

## Where it sits in the stack
The [identity-access](../categories/identity-access.md) foundation — the front door. It governs the **sensitive-data** leg of the lethal trifecta by deciding authentication/authorization before access to data, apps, or models. For AI deployments it's the IdP that gateways, assistants, and [entitlement-aware-rag](../categories/entitlement-aware-rag.md) federate against.

## Deployment & architecture
SaaS, multi-tenant; standards-based (SAML, OIDC, OAuth2, SCIM). Large pre-built integration network (the Okta Integration Network). Feeds and consumes from SIEM ([microsoft-sentinel](microsoft-sentinel.md), [splunk](splunk.md)), and is commonly paired with governance tools. Auth0 is delivered as developer-facing APIs/SDKs.

## Positioning & differentiators
Best-of-breed, cloud-neutral alternative to [microsoft-entra](microsoft-entra.md): preferred where the estate is heterogeneous (not all-Microsoft) or where Auth0-grade CIAM is needed. Strong integration breadth and a mature governance/PAM expansion. Trade-offs: it's a separately purchased product (Entra is bundled with M365), and Okta's security reputation took hits from breaches (notably the 2023 support-system breach), which buyers weigh. Heavier IGA still goes to [sailpoint](sailpoint.md)/[saviynt](saviynt.md).

## Ownership, funding & M&A
Independent public company, Nasdaq: OKTA, IPO April 2017. Founded 2009 by Todd McKinnon and Frederic Kerrest (ex-Salesforce). Acquired **Auth0** in 2021 (~$6.5B all-stock) for customer identity. Ownership confidence high.

## CTO / hedge-fund lens
**Day-1.** A fund not standardized on Microsoft — or one wanting a neutral IdP across mixed SaaS — often picks Okta. It's the same Day-1 control surface as Entra: stand up SSO/MFA/Conditional-Access before go-live, and make your AI gateway and RAG layer authenticate against it. Cost is a real consideration versus "free with M365" Entra; the offset is neutrality and integration depth. Auth0 matters only if the fund builds customer-facing apps.

## Competitors / alternatives
[microsoft-entra](microsoft-entra.md), [ping-identity](ping-identity.md). Governance neighbors: [sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md), [conductorone](conductorone.md), [lumos](lumos.md).

## Open questions / to verify
- Current depth/maturity of Okta Privileged Access and Identity Governance vs dedicated IGA/PAM tools.

## Sources
- [Okta, Inc. — Wikipedia](https://en.wikipedia.org/wiki/Okta,_Inc.) / [SEC EDGAR CIK 0001660134](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001660134) — fetched 2026-06-28 — supports: founding 2009, HQ, Nasdaq OKTA public status, Auth0 acquisition; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established as independent public IdP (Nasdaq: OKTA, IPO 2017), Auth0 acquired 2021; ownership set to public, confidence high; Day-1, high hedge-fund fit.
