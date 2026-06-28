---
type: vendor
name: Collibra
slug: collibra
categories: [ai-governance-platform, dspm]
layer: data
aliases: []
website: https://www.collibra.com
founded: 2008
hq: Brussels, Belgium + New York, NY, USA
ownership: independent
ownership_detail: VC-backed private; $250M Series G at $5.25B valuation (2021, Sequoia Global Equities + Sofina). No M&A.
ownership_confidence: high
funding_total: ~$596M
last_funding: Series G $250M (2021, $5.25B valuation)
deployment: [saas]
target_customer: large enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [data-governance, data-catalog, data-lineage, ai-governance]
---

# Collibra

> Data governance / catalog leader, with an AI Governance module. Primary category: [ai-governance-platform](../categories/ai-governance-platform.md); also tagged [dspm](../categories/dspm.md) (loosely — see below).

**One-liner** — An enterprise data intelligence platform: a data catalog plus governance, lineage, and quality, now extended with an AI Governance module to inventory and govern AI models and their data.

## What it does
Collibra is the system of record for **what data you have and whether you can trust it**: a business-glossary-driven data catalog, data governance workflows (ownership, stewardship, policies), end-to-end data lineage, and data quality monitoring. Its AI Governance offering layers a registry/workflow for AI use cases and models on top of that metadata — mapping models to the data and policies that apply, for compliance (EU AI Act, internal model risk). It is governance/metadata-first, not a security enforcement tool.

## Where it sits in the stack
Data layer for cataloging/governance, and [ai-governance-platform](../categories/ai-governance-platform.md) for the AI-model-governance use. Lethal-trifecta role is indirect — it documents and classifies the **sensitive-data** leg (knowing what data is sensitive and where) but does not enforce access or block egress. The [dspm](../categories/dspm.md) tag is loose: Collibra catalogs and governs data, it is not a security-posture scanner like [cyera](cyera.md)/[bedrock-security](bedrock-security.md); treat its DSPM membership as adjacency, not equivalence.

## Deployment & architecture
SaaS ("Data Intelligence/Governance Cloud") with edge-cloud architecture, open APIs, and graph-based metadata analytics. Connects to source systems to harvest metadata and lineage; integrates with data platforms, BI, and DSPM/quality tools.

## Positioning & differentiators
The long-standing catalog/governance leader, competing with [microsoft-purview](microsoft-purview.md), Alation, Informatica, and Atlan. Distinct from [immuta](immuta.md): Collibra governs/catalogs metadata and policy (the "what/who-owns" layer) while Immuta *enforces* live data access. Its AI Governance push positions it against [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), [ibm-watsonx-governance](ibm-watsonx-governance.md), and [onetrust](onetrust.md) for model inventory/compliance — but anchored to its data-catalog roots rather than model-risk/ML-eval depth.

## Ownership, funding & M&A
Independent, VC-backed private company; ~$596M raised over ~9 rounds. The $250M Series G, led by Sequoia Capital Global Equities and Sofina (with Tiger Global, Battery, CapitalG, Dawn, Durable, ICONIQ, Index), set a **$5.25B valuation** — more than double its April-2020 $2.3B mark. (The $5.25B figure dates to the 2021 Series G and may be stale; private valuations have broadly reset since.) No acquisition; no seed M&A flag. Ownership confidence high; valuation-as-of-2021 confidence med.

## CTO / hedge-fund lens
Collibra is heavyweight enterprise data-governance tooling — a fit for large, data-mature organizations with formal stewardship programs. For a typical hedge fund it is likely **Day-2 or optional**: valuable if you have a sprawling data estate and need a catalog/lineage/AI-model registry for regulators, but heavier than most mid-size funds need. Its AI Governance module has **SR 11-7 / EU AI Act relevance** (model inventory, documentation, policy mapping), though dedicated model-risk platforms may go deeper on validation/monitoring.

## Competitors / alternatives
[microsoft-purview](microsoft-purview.md), [immuta](immuta.md), [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), [ibm-watsonx-governance](ibm-watsonx-governance.md), [onetrust](onetrust.md) (catalog: Alation, Informatica, Atlan — no pages).

## Open questions / to verify
- Current (2025-26) valuation and whether any newer round/secondary has occurred.
- Depth/adoption of Collibra AI Governance vs. dedicated model-risk platforms.
- Whether the [dspm](../categories/dspm.md) tag should be dropped in the final taxonomy pass (Collibra is catalog/governance, not security DSPM).

## Sources
- [Collibra Raises $250M, $5.25B valuation (Collibra newsroom)](https://www.collibra.com/company/newsroom/press-releases/collibra-raises-250-million-in-funding-round-led-by-sequoia-capital-global-equities-and-sofina-more-than-doubling-its-valuation-to-5-25-billion) — fetched 2026-06-28 — supports: Series G amount, lead investors, $5.25B valuation, product; confidence: high.
- [Collibra valued at $5.25bn following $250m Series G (FinTech Futures)](https://www.fintechfutures.com/data-privacy-security/data-governance-platform-collibra-valued-at-5-25bn-following-250m-series-g) — fetched 2026-06-28 — supports: same, plus prior $2.3B mark; confidence: med.
- Tracxn / getlatka profiles — supports: founded 2008, ~$596M total, ~$210M ARR (2025); confidence: low/med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (private), Brussels+NY, founded 2008, ~$596M raised, $250M Series G at $5.25B (2021). No M&A. Made ai-governance-platform the primary category and flagged the dspm tag as loose (catalog/governance, not security DSPM). Set ownership_confidence high.
