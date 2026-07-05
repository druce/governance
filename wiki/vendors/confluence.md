---
title: Confluence (Atlassian)
type: vendor
name: Confluence (Atlassian)
slug: confluence
aka: [Atlassian Confluence]
primary_category: content-sources
also_listed_in: []
website: https://www.atlassian.com/software/confluence
founded: 2004
hq: Sydney, Australia
ownership_state: public
owner: Atlassian Corp
ownership_note: 'Product of Atlassian Corp (public, NASDAQ: TEAM)'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas, self-hosted]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [first-party, content-source, rag-source, atlassian]
---

# Confluence (Atlassian)

**One-liner** — Atlassian's enterprise wiki/knowledge base — where engineering and operational teams document runbooks, decisions, and processes, making it a high-value (and often sensitive) RAG corpus.

**What it does** — Confluence stores structured team documentation (spaces, pages). For an AI stack it is a **content source**: a clean, text-rich corpus that RAG and enterprise assistants index well. Like all content sources, its retrieval safety depends on its page/space permissions — RAG must honor them, not flatten them.

**Where it sits in the stack** — [content-sources](../categories/content-sources.md), retrieval layer (Day-1 if doing RAG). The risk it concentrates is **sensitive-data** exposure. Needs [entitlement-aware-rag](../categories/entitlement-aware-rag.md) and classification/DLP discipline before exposure to an assistant.

**Deployment & architecture** — SaaS (Confluence Cloud) or self-hosted (Confluence Data Center; Server is EOL). Surfaced to AI via Atlassian's APIs/Rovo, Glean and other connectors, or custom ingestion.

**Positioning & differentiators** — Not a security product; the *content* the stack governs. Sibling sources: [sharepoint](sharepoint.md), [google-drive](google-drive.md).

**Ownership, funding & M&A** — Product of Atlassian Corp (public, NASDAQ: TEAM; founded 2002). No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG input you already own. Watch for over-broad space permissions and stale sensitive pages before indexing it for an assistant.

**Competitors / alternatives** — [sharepoint](sharepoint.md), [google-drive](google-drive.md).

## Sources
- [raw/sources/2026-06-28--retrieval-infra--first-party-ownership.md] — supports: Atlassian ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); brief stub — RAG content source. Ownership Atlassian (public, high).
