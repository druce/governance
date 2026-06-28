---
type: vendor
name: Google Drive
slug: google-drive
categories: [content-sources]
layer: retrieval
aliases: [Google Workspace Drive, Shared Drives]
website: https://workspace.google.com/products/drive/
founded: 2012
hq: Mountain View, CA, USA
ownership: public
ownership_detail: Product of Google LLC / Alphabet Inc. (public, NASDAQ: GOOGL)
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [first-party, content-source, rag-source, google]
---

# Google Drive

**One-liner** — Google Workspace's file storage (Docs, Sheets, Slides, Shared Drives) — the primary unstructured-content corpus for Workspace-centric shops, and a core RAG/Gemini source.

**What it does** — Drive holds the documents and shared files Workspace users create. In an AI stack it is a **content source** for RAG and for [gemini-enterprise](gemini-enterprise.md) / Agentspace. Its retrieval safety hinges on Drive sharing settings (link-sharing, "anyone in domain") which are notoriously permissive — the classic RAG over-sharing risk.

**Where it sits in the stack** — [content-sources](../categories/content-sources.md), retrieval layer (Day-1 if doing RAG). Lethal-trifecta role: **sensitive-data** leg. Requires [entitlement-aware-rag](../categories/entitlement-aware-rag.md) plus classification/DLP before assistant exposure.

**Deployment & architecture** — SaaS (Google Workspace). Surfaced to AI via Workspace APIs, Gemini/Agentspace connectors, Glean and similar, or custom ingestion.

**Positioning & differentiators** — Not a security product; the *content* the stack governs. Sibling sources: [sharepoint](sharepoint.md), [confluence](confluence.md).

**Ownership, funding & M&A** — Product of Google LLC / Alphabet (public, NASDAQ: GOOGL). No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG input you already own. Audit link-sharing and "anyone with the link" exposure before indexing Drive for an AI assistant.

**Competitors / alternatives** — [sharepoint](sharepoint.md), [confluence](confluence.md).

## Sources
- [raw/sources/2026-06-28--retrieval-infra--first-party-ownership.md] — supports: Google/Alphabet ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); brief stub — RAG content source. Ownership Google/Alphabet (public, high).
