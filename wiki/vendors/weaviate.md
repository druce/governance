---
title: Weaviate
type: vendor
name: Weaviate
slug: weaviate
categories: [vector-retrieval]
layer: retrieval
aliases: [SeMI Technologies]
website: "https://weaviate.io/"
founded: 2019
hq: Amsterdam, Netherlands
ownership: independent
ownership_detail: VC-backed independent; Series B $50M (2023, Index Ventures), Series C ~$50M (2025, Battery/Index); ~$118M raised
ownership_confidence: high
funding_total: ~$118M
last_funding: Series C ~$50M (2025)
deployment: [self-hosted, saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [vector-database, retrieval, open-source, independent]
---

# Weaviate

**One-liner** — An open-source, AI-native vector database (plus managed cloud) — the self-hostable alternative to Pinecone for RAG retrieval, so embeddings can stay in your own environment.

**What it does** — Weaviate stores embeddings and serves vector, keyword, and hybrid search, with built-in modules for embedding generation and RAG. In a pipeline it is the **vector-retrieval** layer. Its differentiator versus managed pure-plays is that you can run it yourself (open source) or use Weaviate Cloud — useful when data cannot leave your tenancy.

**Where it sits in the stack** — [vector-retrieval](../categories/vector-retrieval.md), retrieval layer (Day-1 if doing RAG). Lethal-trifecta role: holds **sensitive-data** (your corpus embeddings). Multi-tenancy and RBAC support tenant/entitlement separation; entitlement-aware retrieval is still your wiring.

**Deployment & architecture** — Self-hostable open-source core (BSD-3) deployable in your own cloud/Kubernetes, plus Weaviate Cloud (managed SaaS) and a serverless option. API/SDK-driven; integrates with LangChain/LlamaIndex and major embedding providers.

**Positioning & differentiators** — Open-source + self-host is the key contrast with managed-only [pinecone](pinecone.md); versus [opensearch](opensearch.md) it is purpose-built as a vector DB rather than a search engine with vectors bolted on; versus [azure-ai-search](azure-ai-search.md) it is cloud-neutral. Trade-off: you own the operational burden if you self-host.

**Ownership, funding & M&A** — Independent, VC-backed (company formerly SeMI Technologies). Founded 2019 by Bob van Luijt; HQ Amsterdam. $50M Series B led by Index Ventures (2023); ~$50M Series C led by Battery Ventures and Index Ventures (Oct 2025), reported ~$200M valuation; ~$118M total (reports vary). No M&A; independent as of 2026-06. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG infra and the stronger fit when **data residency / MNPI** rules mean embeddings must stay in your own environment — self-host gives you that. Cost is the ops burden of running a stateful DB yourself; Weaviate Cloud trades that back for third-party hosting.

**Competitors / alternatives** — [pinecone](pinecone.md), [opensearch](opensearch.md), [azure-ai-search](azure-ai-search.md), Qdrant/Milvus (not in registry).

**Open questions / to verify** — Exact total-funding figure (sources range ~$67–118M); Series C valuation.

## Sources
- [Weaviate raises $50M Series B (PR Newswire)](https://www.prnewswire.com/news-releases/weaviate-raises-50-million-series-b-funding-301803296.html) — fetched 2026-06-28 — supports: Series B, founding, HQ; confidence: high
- [raw/sources/2026-06-28--weaviate--funding.md] — supports: Series C 2025, ownership independent; confidence: medium

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); ownership independent/VC-backed (Series B 2023, Series C 2025, high). Positioned as self-hostable Pinecone alternative for data residency.
