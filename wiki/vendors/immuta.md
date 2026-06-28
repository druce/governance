---
type: vendor
name: Immuta
slug: immuta
categories: [data-access-governance, dspm]
layer: data
aliases: []
website: https://www.immuta.com
founded: 2015
hq: Boston, Massachusetts, USA
ownership: independent
ownership_detail: VC-backed private; $100M Series E (2022, led by NightDragon + Snowflake) at $1B valuation. NightDragon is an investor, NOT an acquirer.
ownership_confidence: high
funding_total: ~$267M
last_funding: Series E $100M (2022-06-08, NightDragon + Snowflake)
deployment: [saas]
target_customer: enterprise / regulated (finance, healthcare, government)
hedge_fund_fit: high
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [data-access-governance, dspm, abac, snowflake, databricks]
---

# Immuta

> Data access control / governance for cloud data platforms. Primary category: [data-access-governance](../categories/data-access-governance.md); also [dspm](../categories/dspm.md).

**One-liner** — A data-access-control platform that enforces fine-grained, attribute-based access policies (masking, row/column filtering) natively inside Snowflake, Databricks, and other cloud data platforms, so the right users see the right data.

## What it does
Immuta sits over your cloud data warehouse/lakehouse and centralizes **who can query what**. Instead of hand-coding per-table grants, you write attribute-based access control (ABAC) policies once and Immuta enforces them dynamically — dynamic data masking, row-level filtering, purpose-based access — pushed down into the underlying platform. It also discovers and classifies sensitive columns and provides monitoring/audit of data access. The claim (vendor) is that ABAC cuts the number of policies needed by ~75x vs. role-based grants.

## Where it sits in the stack
Data layer — primary [data-access-governance](../categories/data-access-governance.md), secondary [dspm](../categories/dspm.md). Lethal-trifecta role: the **sensitive-data** leg — it constrains which sensitive data a human, service account, or AI/RAG pipeline can actually retrieve. Critical control for entitlement-aware analytics and [entitlement-aware-rag](../categories/entitlement-aware-rag.md) when the warehouse is the knowledge source.

## Deployment & architecture
SaaS control plane. Policy is **pushed down** into the data platform (native integrations with Snowflake, Databricks, Amazon Redshift, Google BigQuery, Azure Synapse, Starburst) rather than proxying queries — so enforcement happens in-engine and Immuta is not in the data path. Provides audit logs to SIEM.

## Positioning & differentiators
Known as a leader in **policy-as-data-access** for the modern data stack, especially Snowflake/Databricks shops. Nearest neighbor [collibra](collibra.md) is governance/catalog-first (metadata, lineage, cataloging) whereas Immuta is enforcement-first (live access control). Versus pure [dspm](../categories/dspm.md) tools ([cyera](cyera.md), [sentra](sentra.md), [bedrock-security](bedrock-security.md), [symmetry-systems](symmetry-systems.md)) Immuta is less about posture discovery and more about runtime entitlement enforcement. Competes with native warehouse RBAC and with [veza](veza.md)/[sailpoint](sailpoint.md) on the access-governance edge. Snowflake and Databricks are both investors and partners.

## Ownership, funding & M&A
Independent, VC-backed private company. Total funding ~$267M. The $100M Series E (announced 2022-06-08) was led by **NightDragon** (Dave DeWalt) and **Snowflake (Snowflake Ventures)** at a $1B valuation; investors also include Databricks Ventures, Dell Technologies Capital, DFJ Growth, Intel Capital, March Capital, StepStone, Ten Eleven Ventures, Wipro Ventures, ServiceNow. **NightDragon is a growth investor, not an acquirer — no acquisition occurred.** Ownership confidence high.

## CTO / hedge-fund lens
For a fund running analytics on Snowflake/Databricks, Immuta is a strong fit to enforce who-sees-what on sensitive data (MNPI segregation, PII, deal data, entitlement walls) without bespoke per-table grants. **Day-2** in the generic stack but effectively **Day-1 if you do warehouse-backed RAG or broad internal analytics** on regulated data. SR 11-7 relevance is indirect (data-access governance supporting model inputs/audit), not model risk per se. Best fit for shops already standardized on a cloud data platform; overkill if your data is small or not centralized.

## Competitors / alternatives
[collibra](collibra.md), [cyera](cyera.md), [sentra](sentra.md), [varonis](varonis.md), [veza](veza.md), [sailpoint](sailpoint.md), [bedrock-security](bedrock-security.md), [symmetry-systems](symmetry-systems.md), native Snowflake/Databricks RBAC.

## Open questions / to verify
- Latest valuation / any newer round since 2022 Series E.
- Depth of Immuta's own DSPM/discovery vs. dedicated DSPM tools (is the [dspm](../categories/dspm.md) tag earned or aspirational?).
- Current revenue/scale.

## Sources
- [Immuta Series E announcement (Immuta blog)](https://www.immuta.com/blog/series-e-funding-announcement/) — fetched 2026-06-28 — supports: $100M Series E, $267M total, NightDragon+Snowflake lead, product/ABAC, SaaS + native integrations; confidence: high.
- [Immuta — Wikipedia](https://en.wikipedia.org/wiki/Immuta) — fetched 2026-06-28 — supports: founded 2015, Boston HQ, founders, $1B valuation; confidence: med.
- [Immuta valued at $1b after NightDragon-led round (DealStreetAsia)](https://www.dealstreetasia.com/stories/immuta-valued-at-1-billion-295816) — fetched 2026-06-28 — supports: $1B valuation, NightDragon as investor; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (private), Boston, founded 2015, ~$267M raised, $100M Series E at $1B led by NightDragon+Snowflake. Clarified NightDragon is an investor, NOT acquirer — no M&A. Reordered categories (data-access-governance primary). Set ownership_confidence high, confidence high.
