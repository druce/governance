---
title: Confluence (Atlassian)
type: vendor
name: Confluence (Atlassian)
slug: confluence
categories: [content-sources]
layer: retrieval
aliases: [Atlassian Confluence]
website: "https://www.atlassian.com/software/confluence"
founded: 2004
hq: Sydney, Australia
ownership: public
ownership_detail: "Product of Atlassian Corp (public, NASDAQ: TEAM)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [first-party, content-source, rag-source, atlassian]
---

# Confluence (Atlassian)

**One-liner** — Atlassian's enterprise wiki/knowledge base — where engineering and operational teams document runbooks, decisions, and processes, making it a high-value (and often sensitive) RAG corpus.

**What it does** — Confluence stores structured team documentation (spaces, pages). For an AI stack it is a **content source**: a clean, text-rich corpus that RAG and enterprise assistants index well. Like all content sources, its retrieval safety depends on its page/space permissions — RAG must honor them, not flatten them.

**Where it sits in the stack** — [content-sources](../categories/content-sources.md), retrieval layer (Day-1 if doing RAG). Lethal-trifecta role: **sensitive-data** leg. Needs [entitlement-aware-rag](../categories/entitlement-aware-rag.md) and classification/DLP discipline before exposure to an assistant.

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
