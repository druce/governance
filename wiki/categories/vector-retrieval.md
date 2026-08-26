---
title: Vector Retrieval
type: category
name: Vector Retrieval
slug: vector-retrieval
category: vector-retrieval
layer: retrieval
survey_question: null
adoption_tier: situational
trigger: doing RAG
maturity_stage_required: null
category_maturity: growth
adjacent: [content-sources, entitlement-aware-rag]
incumbent_coverage: []
vendor_count: 4
maps_to_seed_doc: Vector Retrieval
maps_to_seed_csv: —
last_verified: 2026-08-24
---

> **STUB.** This is retrieval *infrastructure*, not a governance control. The governance-critical part of retrieval is **[entitlement-aware-rag](entitlement-aware-rag.md)** — read that page. A vector store with no permission enforcement is exactly how a RAG system surfaces documents a user was never allowed to see.

## Business objective

The AI's card catalog: turns documents into searchable "meaning" (embeddings) so the model finds the right snippet to ground its answer. Semantic search and retrieval infrastructure — the index layer between your [content-sources](content-sources.md) and the [enterprise-ai-assistant](enterprise-ai-assistant.md).

## When you need it

Day-1 *if you are doing RAG*; otherwise N/A. It is a build choice (which vector database / search service), not a security control. Many assistants ship their own retrieval and you never touch a standalone vector store. The governance question is not "which vector DB" but "does retrieval respect the user's permissions" — and that lives in [entitlement-aware-rag](entitlement-aware-rag.md).

## Security role

A **sensitive-data store**, not a control. A vector index is a *copy* of your sensitive content, often stripped of the source system's ACLs — which is the classic RAG failure mode: the permissions lived on the SharePoint folder, not on the embedding. Whether the index re-checks entitlements at query time is the whole game. Lives in the yellow/green zone.

## Vendors

Infrastructure choices, not a competitive survey shortlist. Pages exist for four:

- [azure-ai-search](../vendors/azure-ai-search.md) — Azure's managed search/vector service; default for Microsoft-stack RAG, supports security-trimming via document-level ACLs.
- [pinecone](../vendors/pinecone.md) — managed vector database; popular standalone choice for custom RAG builds.
- [weaviate](../vendors/weaviate.md) — open-source / managed vector database.
- [opensearch](../vendors/opensearch.md) — open-source search engine with vector support; the self-hosted option.

**Also in this space** (named for completeness; no vendor pages — they add nothing to the governance story the four above do not already carry):

- **Qdrant** — Apache-2.0 Rust engine; the filtering/performance pick. Hybrid Cloud keeps the data plane in your infrastructure. $50M Series B, 2026-03.
- **Milvus / Zilliz** — Apache-2.0 (LF AI & Data); the billion-scale option, heaviest to operate.
- **Chroma** — embedded-first, Apache 2.0; the prototyping default. Chroma Cloud GA 2025-08.
- **LanceDB** — embedded + cloud over the Lance columnar format; the multimodal angle, and a common agent-memory substrate.
- **pgvector, MongoDB Atlas Vector Search, Redis, Vespa, Amazon S3 Vectors, turbopuffer** — the "use what you already have" and object-storage-native options. For most funds pgvector on existing Postgres is the right default.

Full comparison, market shapes, and consolidation dynamics: [vector-database-landscape](../comparisons/vector-database-landscape.md).

## Consolidation / M&A dynamics

Not a seed-flagged M&A category, but the standalone vector DB is under pressure — bundled from below (every OLTP engine and search engine added vectors) and undercut from above by object-storage-native indexes. [pinecone](../vendors/pinecone.md) is **reportedly** exploring a sale (unconfirmed, no deal announced as of 2026-08-24), while the Apache-2.0 engines keep raising. Detail and sourcing: [vector-database-landscape](../comparisons/vector-database-landscape.md).

## Adjacent categories

- [entitlement-aware-rag](entitlement-aware-rag.md) — the layer that makes retrieval permission-aware; the part that matters for governance.
- [content-sources](content-sources.md) — the systems of record this index is built from.
- [enterprise-ai-assistant](enterprise-ai-assistant.md) — the consumer of retrieved snippets.

## Survey

No standalone survey question. Vector database choice is an engineering decision, not a CTO governance survey item. Where it matters, it is captured under [entitlement-aware-rag](entitlement-aware-rag.md) and [enterprise-ai-assistant](enterprise-ai-assistant.md).

## Open taxonomy questions

- Like [content-sources](content-sources.md), this is infra rather than a buying-decision category. Kept as a stub to preserve the layer-cake row; the security-relevant content all routes to [entitlement-aware-rag](entitlement-aware-rag.md).
- [2026-08-24] Confirmed the stub stance rather than minting stub pages for Qdrant/Milvus/Chroma/LanceDB — coverage discharged by [vector-database-landscape](../comparisons/vector-database-landscape.md). Open: whether the RAG *platforms* (Vectara, Contextual AI) earn pages under [enterprise-ai-assistant](enterprise-ai-assistant.md) / [entitlement-aware-rag](entitlement-aware-rag.md).
