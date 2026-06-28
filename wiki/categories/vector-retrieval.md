---
title: Vector Retrieval
type: category
name: Vector Retrieval
slug: vector-retrieval
layer: retrieval
priority: day-1
trifecta_role: sensitive-data
maps_to_seed_doc: Vector Retrieval
maps_to_seed_csv: "—"
vendor_count: 4
status: drafted
last_updated: 2026-06-28
---

> **STUB.** This is retrieval *infrastructure*, not a governance control. The governance-critical part of retrieval is **[entitlement-aware-rag](entitlement-aware-rag.md)** — read that page. A vector store with no permission enforcement is exactly how a RAG system surfaces documents a user was never allowed to see.

## Business objective

The AI's card catalog: turns documents into searchable "meaning" (embeddings) so the model finds the right snippet to ground its answer. Semantic search and retrieval infrastructure — the index layer between your [content-sources](content-sources.md) and the [enterprise-ai-assistant](enterprise-ai-assistant.md).

## When you need it

Day-1 *if you are doing RAG*; otherwise N/A. It is a build choice (which vector database / search service), not a security control. Many assistants ship their own retrieval and you never touch a standalone vector store. The governance question is not "which vector DB" but "does retrieval respect the user's permissions" — and that lives in [entitlement-aware-rag](entitlement-aware-rag.md).

## Lethal-trifecta role

The **sensitive-data** leg, as a store. A vector index is a *copy* of your sensitive content, often stripped of the source system's ACLs — which is the classic RAG failure mode: the permissions lived on the SharePoint folder, not on the embedding. Whether the index re-checks entitlements at query time is the whole game. Lives in the yellow/green zone.

## Vendors

Infrastructure choices, not a competitive survey shortlist:

- [azure-ai-search](../vendors/azure-ai-search.md) — Azure's managed search/vector service; default for Microsoft-stack RAG, supports security-trimming via document-level ACLs.
- [pinecone](../vendors/pinecone.md) — managed vector database; popular standalone choice for custom RAG builds.
- [weaviate](../vendors/weaviate.md) — open-source / managed vector database.
- [opensearch](../vendors/opensearch.md) — open-source search engine with vector support; the self-hosted option.

## Consolidation / M&A dynamics

N/A — mix of cloud-platform services (Azure) and independent infra vendors; not a seed-flagged M&A category.

## Adjacent categories

- [entitlement-aware-rag](entitlement-aware-rag.md) — the layer that makes retrieval permission-aware; the part that matters for governance.
- [content-sources](content-sources.md) — the systems of record this index is built from.
- [enterprise-ai-assistant](enterprise-ai-assistant.md) — the consumer of retrieved snippets.

## Survey

No standalone survey question. Vector database choice is an engineering decision, not a CTO governance survey item. Where it matters, it is captured under [entitlement-aware-rag](entitlement-aware-rag.md) and [enterprise-ai-assistant](enterprise-ai-assistant.md).

## Open taxonomy questions

- Like [content-sources](content-sources.md), this is infra rather than a buying-decision category. Kept as a stub to preserve the layer-cake row; the security-relevant content all routes to [entitlement-aware-rag](entitlement-aware-rag.md).
