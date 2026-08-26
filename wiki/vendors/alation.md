---
title: Alation
type: vendor
name: Alation
slug: alation
aka: []
primary_category: data-access-governance
also_listed_in: [entitlement-aware-rag]
website: https://www.alation.com/
founded: 2012
hq: Redwood City, CA, USA
ownership_state: independent
owner: null
ownership_note: VC-backed. $340M total raised across five rounds; $123M Series E announced 2022-11 at a >$1.7B valuation, led by Thoma Bravo, Sanabil Investments and Costanoa Ventures, with Databricks Ventures joining. No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: $340M
last_funding: Series E $123M at >$1.7B valuation, 2022-11
market_position: {data-access-governance: leader}
deployment_model: [saas, self-hosted]
form_factor: [platform, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: null
tags: [data-catalog, data-governance, lineage, metadata, data-intelligence]
sources:
  - {claim: "$123M Series E at >$1.7B valuation announced November 2022, led by Thoma Bravo, Sanabil Investments and Costanoa Ventures with Databricks Ventures participating; $340M total raised", url: "https://www.thomabravo.com/press-releases/alation-raises-123m-series-e-to-meet-surging-global-demand-for-data-intelligence-platforms", date: 2026-08-26, confidence: high}
  - {claim: "Named a Leader in Forrester Wave: Data Governance Solutions Q1 2025; 2026 Gartner MQ for Data & Analytics Governance Platforms elevated AI model governance to a mandatory evaluation criterion", url: "https://research.isg-one.com/analyst-perspectives/alations-data-governance-accelerates-data-intelligence", date: 2026-08-26, confidence: medium}
---

# Alation

> Primary category: [data-access-governance](../categories/data-access-governance.md). Also listed in [entitlement-aware-rag](../categories/entitlement-aware-rag.md).

**One-liner** — The data catalog that grew into a governance platform: it inventories what data the firm has, where it came from, who owns it and what it means — the metadata layer that determines whether a RAG or agent deployment can be governed at all.

**What it does** — Alation crawls the firm's data estate (warehouses, lakes, BI tools, databases) and builds a searchable **catalog** of tables, columns, dashboards and reports, enriched with **lineage** (where a figure came from and what transformations it passed through), **business glossary** terms, ownership, quality signals and usage telemetry — Alation's original trick was mining query logs to infer which data people actually use and trust. On top of the catalog sit **policy** definition, stewardship workflow, and a data-products marketplace.

Why an AI-governance wiki cares: the catalog and its policy metadata are the substrate for everything downstream. You cannot restrict what a retrieval pipeline surfaces, prove to an examiner what a model was trained or grounded on, or answer "does this agent have access to MNPI?" without an accurate map of the data estate first. The **2026 Gartner Magic Quadrant for Data and Analytics Governance Platforms made AI model governance a mandatory evaluation criterion** — the category's own recognition that governing the data estate no longer suffices without governing what AI does with it.

**Naming / provenance** — Founded 2012, Redwood City. Single brand; the market label has drifted from "data catalog" to "data intelligence platform" without a product rename.

**Ownership & viability** — `independent`, VC-backed, **$340M raised** across five rounds. The **$123M Series E in November 2022 valued it above $1.7B**, led by **Thoma Bravo**, Sanabil and Costanoa, with **Databricks Ventures** joining — a strategically significant investor given how much of this market Databricks Unity Catalog and Microsoft Purview are absorbing from below. No round since 2022 and no acquisition as of 2026-08-26. Thoma Bravo on the cap table at a $1.7B mark makes a take-private a natural eventual outcome.

**Positioning & differentiators** —
- **Versus [collibra](collibra.md):** the long-standing head-to-head. Collibra is stronger on formal governance process and stewardship workflow; Alation is stronger on discovery, search and analyst adoption. The cliché — Collibra for the governance office, Alation for the people who use data — is roughly right.
- **Versus [immuta](immuta.md):** a different job entirely. Immuta *enforces* policy at query time; Alation *describes and documents* the estate. Firms doing entitlement-aware retrieval seriously often need both — see [entitlement-aware-rag](../categories/entitlement-aware-rag.md).
- **Versus the platform-native catalogs** (Databricks Unity Catalog, Microsoft Purview, Snowflake Horizon): the standing threat. Alation's answer is heterogeneity — it covers estates that span several platforms, which is the normal condition at a firm running Snowflake plus a legacy SQL Server plus vendor market-data feeds.
- **Agentic direction.** Forrester named it a Leader in Data Governance Solutions (Q1 2025), citing its agentic AI platform and data-products marketplace. How real the AI-model-governance capability is, versus catalog features relabelled, is an open question below.

**Who should choose them / anti-fit** — Fits a firm with a **heterogeneous data estate and a genuine discovery problem** — analysts who cannot find or trust data — that is now trying to point retrieval or agents at internal data. This describes a great many asset managers. **Anti-fit:** a firm entirely inside one platform (all-Databricks, all-Snowflake, all-Microsoft), where the native catalog is cheaper and better integrated; and any firm whose actual need is *enforcement* rather than *documentation* — buy [immuta](immuta.md) or [varonis](varonis.md) instead.

**Known weaknesses / gotchas** — Enterprise price point and a real implementation effort: a catalog is only as good as the stewardship put into it, and half-populated catalogs are the standard failure mode of this category. Squeezed from below by platform-native catalogs. **It documents; it does not enforce** — a distinction firms routinely blur when they assume buying a catalog gives them access control.

**Deployment & data handling** — SaaS (Alation Cloud Service) and customer-managed deployment. Alation ingests **metadata**, not primary data, in normal operation — an important and reassuring distinction — but the specifics of what is transmitted (query logs contain fragments of business content) are **unverified** and worth diligencing.

**Integrations & partnerships** — Broad connector library across warehouses, lakes, BI and ETL; Databricks partnership reinforced by the Series E investment. MCP support unverified.

**Compliance & FS traction** — **Unverified** here; the customer base is enterprise-wide and financial services is a stated vertical, but no named references were confirmed.

**Commercial** — Not public. Enterprise subscription, typically scaled by connected sources and user seats.

## Open questions

- What "AI model governance" actually means in Alation's product versus catalog features relabelled for the 2026 Gartner criterion.
- Whether query-log ingestion transmits business content, and retention/training terms.
- MCP or agent-framework support — can an agent query the catalog to resolve permissions and semantics at runtime?
- Named financial-services customers; certifications held.
- Any funding or ownership change since the 2022 Series E — Thoma Bravo's presence makes this worth re-checking.

## Sources

- [Alation Raises $123M Series E (Thoma Bravo)](https://www.thomabravo.com/press-releases/alation-raises-123m-series-e-to-meet-surging-global-demand-for-data-intelligence-platforms) — fetched 2026-08-26 — supports: round size, valuation, investors, total raised; confidence: high (primary)
- [Alation's Data Governance Accelerates Data Intelligence (ISG Research)](https://research.isg-one.com/analyst-perspectives/alations-data-governance-accelerates-data-intelligence) — fetched 2026-08-26 — supports: Forrester Leader placement, 2026 Gartner MQ AI-governance criterion; confidence: medium
- Cached: `raw/sources/2026-08-26--alation--funding-and-analyst-position.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier B, score 7) — surfaced as a peer of Immuta and Collibra; promoted to inclusion because the data-catalog layer is a prerequisite for entitlement-aware retrieval at an asset manager.
