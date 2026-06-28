---
title: Microsoft Entra ID
type: vendor
name: Microsoft Entra ID
slug: microsoft-entra
categories: [identity-access]
layer: foundation
aliases: [Azure AD, Azure Active Directory, AAD, Entra ID]
website: "https://www.microsoft.com/security/business/identity-access/microsoft-entra-id"
founded: 2000
hq: Redmond, Washington, USA
ownership: public
ownership_detail: "Product of Microsoft (Nasdaq: MSFT); part of the Microsoft Entra family"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise / mid-market / SMB (anyone on Microsoft 365 or Azure)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity, idp, sso, mfa, microsoft]
---

# Microsoft Entra ID

> Researched 2026-06-28. Primary category: [identity-access](../categories/identity-access.md).

**One-liner** — Microsoft's cloud identity provider (the former Azure Active Directory): the SSO/MFA/Conditional-Access front door for everyone already living in Microsoft 365 and Azure.

## What it does
Entra ID is the directory and identity-provider (IdP) layer that authenticates users and apps, issues tokens, and enforces access policy. Core jobs: single sign-on (SSO) to thousands of SaaS apps, multi-factor authentication (MFA), Conditional Access (risk- and context-based access rules), user/group lifecycle, and identity protection (anomaly detection on sign-ins). For most enterprises it is the de-facto corporate directory because it ships with Microsoft 365.

It was renamed from **Azure Active Directory (Azure AD)** to Microsoft Entra ID in July 2023 — a rename only, no feature change. "Microsoft Entra" is the broader family: Entra ID (the IdP), Entra ID Governance (IGA), Entra Permissions Management (CIEM), Entra Verified ID, Entra Internet/Private Access (SSE), and newer Entra Agent ID for agent identities.

## Where it sits in the stack
The [identity-access](../categories/identity-access.md) foundation — the human (and increasingly agent) front door. In lethal-trifecta terms it governs the **sensitive-data** leg by deciding who/what is authenticated and authorized before anything reaches data or models. It's the IdP that AI gateways, [entitlement-aware-rag](../categories/entitlement-aware-rag.md), and downstream tools federate against.

## Deployment & architecture
SaaS, multi-tenant, delivered as part of Azure / Microsoft 365. Standards-based (SAML, OIDC, OAuth2, SCIM) so it federates to virtually any app. Integrates natively with [microsoft-purview](microsoft-purview.md), [microsoft-sentinel](microsoft-sentinel.md), [microsoft-defender](microsoft-defender.md), Intune, and Microsoft 365 Copilot. Licensed in tiers (Free, P1, P2); governance and CIEM are add-ons.

## Positioning & differentiators
Default-by-bundling: if you pay for Microsoft 365 you already have Entra ID, which makes it the path of least resistance versus standalone [okta](okta.md) or [ping-identity](ping-identity.md). Strongest where the estate is Microsoft-centric (Windows, Office, Azure). Weaker as a neutral, best-of-breed IdP for heterogeneous or heavy-CIAM environments, where Okta/Auth0 or Ping are often preferred. Governance (Entra ID Governance) is newer and lighter than dedicated [sailpoint](sailpoint.md)/[saviynt](saviynt.md).

## Ownership, funding & M&A
Microsoft product; not separately funded. Public parent (Nasdaq: MSFT). Ownership confidence high. No M&A relevant to the unit itself.

## CTO / hedge-fund lens
**Day-1, and for most funds it's already there.** A hedge fund running Microsoft 365 effectively already owns its IdP — the work is configuration (Conditional Access, MFA, privileged-role protection), not procurement. For AI specifically, Entra is what your AI gateway, Copilot, and RAG layer should authenticate against so access decisions inherit existing entitlements. Bundled cost and tight Microsoft integration usually make it the default; the question is whether you also want best-of-breed governance on top.

## Competitors / alternatives
[okta](okta.md), [ping-identity](ping-identity.md). Governance neighbors: [sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md), [conductorone](conductorone.md), [lumos](lumos.md).

## Open questions / to verify
- Exact split of what's licensed P1 vs P2 vs Governance add-on for a given fund's needs (verify at purchase).

## Sources
- [New name for Azure Active Directory — Microsoft Learn](https://learn.microsoft.com/en-us/entra/fundamentals/new-name) — fetched 2026-06-28 — supports: Azure AD→Entra ID rename (July 2023), Entra family scope, ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established it as Microsoft's IdP (former Azure AD, renamed July 2023), part of the Entra family; ownership set to public (Microsoft), confidence high; Day-1, high hedge-fund fit (bundled with M365).
