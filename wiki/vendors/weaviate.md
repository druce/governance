---
title: Weaviate
type: vendor
name: Weaviate
slug: weaviate
aka: [SeMI Technologies]
primary_category: vector-retrieval
also_listed_in: []
website: https://weaviate.io/
founded: 2019
hq: Amsterdam, Netherlands
ownership_state: independent
owner: null
ownership_note: VC-backed independent; Series B $50M (2023, Index Ventures), Series C ~$50M (2025, Battery/Index); ~$118M raised
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$118M
last_funding: Series C ~$50M (2025)
market_position: null
deployment_model: [self-hosted, saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [vector-database, retrieval, open-source, independent]
---

# Weaviate

**One-liner** — An open-source, AI-native vector database (plus managed cloud) — the self-hostable alternative to Pinecone for RAG retrieval, so embeddings can stay in your own environment.

**What it does** — Weaviate stores embeddings and serves vector, keyword, and hybrid search, with built-in modules for embedding generation and RAG. In a pipeline it is the **vector-retrieval** layer. Its differentiator versus managed pure-plays is that you can run it yourself (open source) or use Weaviate Cloud — useful when data cannot leave your tenancy.

**Where it sits in the stack** — [vector-retrieval](../categories/vector-retrieval.md), retrieval layer (Day-1 if doing RAG). Risk role: it holds sensitive data (your corpus embeddings). Multi-tenancy and RBAC support tenant/entitlement separation; entitlement-aware retrieval is still your wiring.

**Deployment & architecture** — Self-hostable open-source core (BSD-3) deployable in your own cloud/Kubernetes, plus Weaviate Cloud (managed SaaS) and a serverless option. API/SDK-driven; integrates with LangChain/LlamaIndex and major embedding providers.

**Positioning & differentiators** — Open-source + self-host is the key contrast with managed-only [pinecone](pinecone.md); versus [opensearch](opensearch.md) it is purpose-built as a vector DB rather than a search engine with vectors bolted on; versus [azure-ai-search](azure-ai-search.md) it is cloud-neutral. Trade-off: you own the operational burden if you self-host.

**Ownership, funding & M&A** — Independent, VC-backed (company formerly SeMI Technologies). Founded 2019 by Bob van Luijt; HQ Amsterdam. $50M Series B led by Index Ventures (2023); ~$50M Series C led by Battery Ventures and Index Ventures (Oct 2025), reported ~$200M valuation; ~$118M total (reports vary). No M&A; independent as of 2026-06. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG infra and the stronger fit when **data residency / MNPI** rules mean embeddings must stay in your own environment — self-host gives you that. Cost is the ops burden of running a stateful DB yourself; Weaviate Cloud trades that back for third-party hosting.

**Competitors / alternatives** — [pinecone](pinecone.md), [opensearch](opensearch.md), [azure-ai-search](azure-ai-search.md), Qdrant/Milvus (not in registry).

**Open questions / to verify** — Exact total-funding figure (sources range ~$67–118M); Series C valuation.

## Sources
- [Weaviate raises $50M Series B (PR Newswire)](https://www.prnewswire.com/news-releases/weaviate-raises-50-million-series-b-funding-to-meet-soaring-demand-for-ai-native-vector-database-technology-301803296.html) — fetched 2026-06-28, URL corrected 2026-08-16 (the shortened slug now 404s) — supports: Series B, founding, HQ; confidence: high
- [raw/sources/2026-06-28--weaviate--funding.md] — supports: Series C 2025, ownership independent; confidence: medium

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); ownership independent/VC-backed (Series B 2023, Series C 2025, high). Positioned as self-hostable Pinecone alternative for data residency.
