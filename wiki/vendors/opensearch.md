---
type: vendor
name: OpenSearch
slug: opensearch
categories: [vector-retrieval]
layer: retrieval
aliases: [Amazon OpenSearch Service]
website: https://opensearch.org/
founded: 2021
hq: (open-source project; OpenSearch Software Foundation under the Linux Foundation)
ownership: independent
ownership_detail: Apache-2.0 OSS; AWS transferred it to the Linux Foundation (OpenSearch Software Foundation) on 2024-09-16. AWS still offers the managed Amazon OpenSearch Service.
ownership_confidence: high
funding_total:
last_funding:
deployment: [self-hosted, saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [vector-database, retrieval, open-source, linux-foundation, aws]
---

# OpenSearch

**One-liner** — An open-source search, analytics, and observability engine (the AWS-led fork of Elasticsearch) with a vector-search engine built in — usable as the retrieval layer for RAG while doubling as your log/search platform.

**What it does** — OpenSearch indexes documents and serves keyword, vector (k-NN), and hybrid search. For RAG it is the **vector-retrieval** layer; it is also widely used for logging/SIEM-style analytics, so some shops reuse one platform for both. Originated in 2021 when AWS forked Elasticsearch/Kibana 7.10 after Elastic's license change.

**Where it sits in the stack** — [vector-retrieval](../categories/vector-retrieval.md), retrieval layer (Day-1 if doing RAG). Lethal-trifecta role: holds **sensitive-data** (indexed corpus + embeddings). Document-level/field-level security supports entitlement-aware retrieval if configured.

**Deployment & architecture** — Self-hostable open-source (Apache-2.0), or the managed **Amazon OpenSearch Service** (SaaS) on AWS; also offered by other providers. API/SDK-driven; k-NN plugin for vectors.

**Positioning & differentiators** — The open, self-hostable, dual-purpose (search + vectors + logs) option. Contrast: [pinecone](pinecone.md) (managed pure-play), [weaviate](weaviate.md) (purpose-built vector DB), [azure-ai-search](azure-ai-search.md) (Azure-native). Governance note: as of 2024-09 the project is **Linux-Foundation-governed**, not AWS-controlled — a vendor-neutrality plus.

**Ownership, funding & M&A** — Open-source project; AWS **transferred OpenSearch to the Linux Foundation (OpenSearch Software Foundation) on 2024-09-16**. Apache-2.0, community-governed; AWS, SAP, Uber are premier members. No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG infra if you want open-source, self-hostable retrieval with full data residency, or already run OpenSearch for logs/SIEM and want to reuse it. Cost is operational (running and tuning a cluster). The Linux Foundation move reduces single-vendor lock-in risk.

**Competitors / alternatives** — [pinecone](pinecone.md), [weaviate](weaviate.md), [azure-ai-search](azure-ai-search.md), [elastic](elastic.md) (the upstream it forked from), Qdrant/Milvus (not in registry).

**Open questions / to verify** — Vector-search performance/scale vs. purpose-built vector DBs for large RAG workloads.

## Sources
- [Linux Foundation announces OpenSearch Software Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-opensearch-software-foundation-to-foster-open-collaboration-in-search-and-analytics) — fetched 2026-06-28 — supports: AWS→Linux Foundation transfer 2024-09-16, vector-database use; confidence: high
- [raw/sources/2026-06-28--opensearch--linux-foundation.md] — supports: governance, origin as Elasticsearch fork; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established ownership = independent OSS under Linux Foundation (OpenSearch Software Foundation, transferred by AWS 2024-09-16, high). Noted AWS-originated Elasticsearch fork.
