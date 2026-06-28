---
type: vendor
name: Silverfort
slug: silverfort
categories: [identity-governance, non-human-identity, data-access-governance]
layer: foundation
aliases: []
website: https://www.silverfort.com/
founded: 2016
hq: Tel Aviv, Israel (US presence: Boston / Texas)
ownership: independent
ownership_detail: VC-backed unicorn; ~$222M raised. Series D $116M (Jan 2024) led by Brighton Park Capital at ~$1B valuation.
ownership_confidence: high
funding_total: ~$222M
last_funding: Series D, $116M, 2024-01
deployment: [saas, self-hosted, on-prem, api]
target_customer: enterprise / regulated (hybrid AD + cloud estates)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity, mfa, itdr, non-human-identity, runtime-identity, unicorn]
---

# Silverfort

> **Researched 2026-06-28.** Primary category: [identity-governance](../categories/identity-governance.md) (but see note — its real center of gravity is runtime identity protection / ITDR + NHI).

**One-liner** — A unified, largely agentless/proxyless identity-security platform that extends MFA, conditional access, and threat detection to systems that normally can't get them — legacy apps, service accounts, command-line, OT — across cloud and on-prem.

## What it does
Silverfort sits in-line with the authentication path (notably Active Directory via its security-protocol integration) so it can apply modern controls — MFA, conditional access, blocking — to resources that were previously "un-protectable," without deploying agents on every host or proxies in front of every app. From that vantage point it does: universal MFA, identity threat detection and response (ITDR), and increasingly Non-Human Identity (NHI) security — discovering, monitoring, and protecting service accounts and machine identities, which are hard to put MFA on and are a common lateral-movement path. It markets a "Runtime Access Protection (RAP)" capability.

## Where it sits in the stack
Foundation layer. Tagged [identity-governance](../categories/identity-governance.md), [non-human-identity](../categories/non-human-identity.md), and [data-access-governance](../categories/data-access-governance.md), but its distinctive job is **runtime identity protection / ITDR** layered on the IdP and directory ([microsoft-entra](microsoft-entra.md), [okta](okta.md), Active Directory) — complementary to, not a replacement for, IGA suites. Lethal-trifecta role: none directly; it hardens the identity perimeter and limits lateral movement / blast radius. Strong NHI/service-account story makes it relevant alongside [cyberark](cyberark.md), [token-security](token-security.md), [oasis-security](oasis-security.md).

## Deployment & architecture
Agentless/proxyless inline integration with authentication infrastructure (AD/Kerberos/NTLM, LDAP, plus cloud IdPs and access protocols); delivered as SaaS with on-prem/hybrid components. Integrates with IdPs, MFA providers, SIEM ([microsoft-sentinel](microsoft-sentinel.md), [splunk](splunk.md)), and PAM. Its differentiator is breadth of coverage without per-app agents.

## Positioning & differentiators
Known for the agentless approach that "goes everywhere," including legacy/AD-centric estates where competitors need agents or proxies. Versus pure IGA ([sailpoint](sailpoint.md), [saviynt](saviynt.md), [linx-security](linx-security.md)) it is enforcement/detection at runtime, not certification/lifecycle. Versus PAM ([cyberark](cyberark.md)) it protects existing accounts in place rather than vaulting them. Its NHI push competes with [oasis-security](oasis-security.md), [token-security](token-security.md), [astrix-security](astrix-security.md). Marketing claims of being "the only platform that truly goes everywhere" should be read as marketing.

## Ownership, funding & M&A
Independent, VC-backed unicorn. Founded 2016 by Hed Kovetz (CEO), Yaron Kassner (CTO), and Matan Fattal; Israeli-origin with US presence (Boston/Texas). ~$222M raised total; Series D $116M in January 2024 led by Brighton Park Capital at ~$1B valuation. 2025: Howard Greenfield joined as President/CRO. No acquisition of Silverfort confirmed. Confidence high.

## CTO / hedge-fund lens
Day-2, but among the more relevant identity tools here for a regulated shop with a meaningful on-prem / Active Directory footprint and lots of service accounts. Its sweet spot — putting MFA on legacy apps and locking down service accounts without rip-and-replace — maps well to audit/insurance requirements and to limiting ransomware lateral movement. A cloud-only, Okta/Entra-native fund gets less incremental value. Not a model-risk (SR 11-7) tool, though ITDR coverage supports operational-risk and audit posture.

## Competitors / alternatives
[cyberark](cyberark.md), [oasis-security](oasis-security.md), [token-security](token-security.md), [astrix-security](astrix-security.md), [sailpoint](sailpoint.md), [saviynt](saviynt.md), [linx-security](linx-security.md), [microsoft-entra](microsoft-entra.md) (Identity Protection).

## Open questions / to verify
- Precise current HQ designation (sources list Tel Aviv, Dallas, and Plano TX) — likely dual Israel/US.
- Depth of the cloud-IdP (non-AD) coverage vs the AD-centric core.
- Any funding/valuation change since the Jan-2024 Series D.

## Sources
- [Silverfort — Company](https://www.silverfort.com/company/) — fetched 2026-06-28 — supports: founders, founding year, product/NHI/RAP positioning; confidence: high (vendor, marketing tone).
- [Silverfort now valued at $1B after raising $116M (TechCrunch)](https://techcrunch.com/2024/01/23/silverfort-now-valued-at-1b-after-raising-116m-for-its-holistic-approach-to-identity-security/) — fetched 2026-06-28 — supports: Series D, valuation, total funding; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent unicorn (~$222M raised, $116M Series D Jan-2024 led by Brighton Park, ~$1B valuation), founded 2016 by Kovetz/Kassner/Fattal. Clarified center of gravity is agentless runtime identity protection / ITDR + NHI, not classic IGA. ownership_confidence raised to high.
