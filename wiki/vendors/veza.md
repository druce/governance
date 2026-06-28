---
title: Veza
type: vendor
name: Veza
slug: veza
categories: [identity-governance, data-access-governance]
layer: foundation
aliases: [Veza Access Platform, Access Graph]
website: "https://veza.com"
founded: 2020
hq: Los Gatos, California, USA
ownership: acquired
ownership_detail: Acquired by ServiceNow — announced 2025-12-02, closed 2026-03-02 (reported ~$1B; value undisclosed by ServiceNow)
ownership_confidence: high
funding_total: ~$235M (pre-acquisition)
last_funding: Series D, $108M, Apr 2025, $808M valuation (NEA-led)
deployment: [saas]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [identity-security, access-graph, iga, data-access-governance, nhi, servicenow]
---

# Veza

> Researched 2026-06-28. Primary category: [identity-governance](../categories/identity-governance.md).

**One-liner** — Identity-security "Access Graph" that maps and controls *who (or what) can do what* across apps, data, cloud, and AI agents — now part of ServiceNow.

## What it does
Veza's Access Platform builds an authorization graph across systems and normalizes their disparate permission models into one answer to "who can take which action on which resource." On that it runs access intelligence, privileged-access monitoring, access reviews/certifications, separation-of-duties, non-human-identity (NHI) security, and SaaS/data access governance. Rather than replacing the IdP or classic IGA workflow engine, it adds the deep *effective-permissions visibility* that those tools historically lacked.

## Where it sits in the stack
The [identity-governance](../categories/identity-governance.md) foundation plus [data-access-governance](../categories/data-access-governance.md). It addresses the **sensitive-data** leg of the lethal trifecta by exposing and right-sizing effective access — directly relevant to keeping [entitlement-aware-rag](../categories/entitlement-aware-rag.md) and AI assistants from surfacing data a user/agent shouldn't reach. Strong on non-human/agent identity, which matters as agentic systems proliferate.

## Deployment & architecture
SaaS. Connects broadly across IdPs ([microsoft-entra](microsoft-entra.md), [okta](okta.md)), cloud (AWS/Azure/GCP), SaaS apps, data systems (Snowflake, etc.), and infrastructure to ingest permission metadata into the Access Graph. Integrates with SIEM/ITSM workflows; now folding into ServiceNow's Security & Risk portfolio and AI Control Tower.

## Positioning & differentiators
Known for **authorization visibility** — the "Access Graph" of effective permissions — versus the workflow/certification heritage of [sailpoint](sailpoint.md)/[saviynt](saviynt.md). Positioned as AI-native identity security and a leader in NHI. Differentiator is depth of cross-system permission analysis rather than provisioning. Overlaps data-access neighbors [varonis](varonis.md), [cyera](cyera.md), [sentra](sentra.md) on the data side and [conductorone](conductorone.md) on access reviews.

## Ownership, funding & M&A
**M&A verified — material change from seed.** ServiceNow announced the acquisition of Veza on **December 2, 2025**, and the deal **closed March 2, 2026** (reported ~$1B by SecurityWeek; ServiceNow did not disclose value). Founded 2020 (CEO Tarun Thakur), HQ Los Gatos, CA; had raised ~$235M, most recently a $108M Series D (Apr 2025, NEA-led, $808M valuation). Seed registry listed it as independent with no M&A flag → **corrected to `acquired` (ServiceNow subsidiary)**, confidence high.

## CTO / hedge-fund lens
**Day-2**, moving toward Day-1 for funds doing RAG or under model-risk/audit pressure, where proving and minimizing effective access is the control. Veza's strength — answering "who can actually touch this data/model, including agents" — is exactly the question AI access governance raises. Now-under-ServiceNow: attractive if the fund already runs ServiceNow (single pane of glass, ITSM-integrated remediation); watch for product integration/roadmap churn typical post-acquisition, and pricing moving to ServiceNow's enterprise model.

## Competitors / alternatives
[sailpoint](sailpoint.md), [saviynt](saviynt.md), [conductorone](conductorone.md), [lumos](lumos.md). Data-access neighbors: [varonis](varonis.md), [cyera](cyera.md), [sentra](sentra.md). Bundled option: [microsoft-entra](microsoft-entra.md).

## Open questions / to verify
- Post-close product/branding integration into ServiceNow and impact on standalone availability and pricing.

## Sources
- [ServiceNow to Acquire Veza — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-to-Expand-Security-Portfolio-With-Acquisition-of-Vezas-Leading-AI-native-Identity-Security-Platform/default.aspx) — fetched 2026-06-28 — supports: ServiceNow acquisition, announced 2025-12-02 / closed 2026-03-02; confidence: high
- [Veza Raises $108M Series D — Veza press room](https://veza.com/company/press-room/series-d-announcement/) — fetched 2026-06-28 — supports: founding 2020, HQ, $108M Series D at $808M (Apr 2025), ~$235M total; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified ServiceNow acquisition (announced 2025-12-02, closed 2026-03-02). Corrected ownership independent→acquired (ServiceNow), confidence high — material change not flagged in seed. Day-2, medium hedge-fund fit.
