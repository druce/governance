---
title: Vector databases — the landscape
type: comparison
name: Vector databases — the landscape
slug: vector-database-landscape
status: drafted
last_updated: 2026-08-24
confidence: medium
sources_count: 14
---

# Vector databases: the landscape

A **vector database** stores embeddings and answers "what is semantically near
this query" — the index layer between your [content-sources](../categories/content-sources.md)
and whatever assistant or agent consumes the retrieved snippets. The wiki files
this under [vector-retrieval](../categories/vector-retrieval.md), a deliberately
**thin, situational** category with no survey question: which vector DB you pick
is an engineering decision, not a governance control (decision D9/Q3 in
`taxonomy-gaps.md`). The control that *does* matter sits one layer up, in
[entitlement-aware-rag](../categories/entitlement-aware-rag.md).

This page is the landscape scan behind that stance — filed back from a scoping
query (2026-08-24), covering the vendors that come up in every RAG conversation
but do not each earn a vendor page. Four already have pages: [pinecone](../vendors/pinecone.md),
[weaviate](../vendors/weaviate.md), [azure-ai-search](../vendors/azure-ai-search.md),
[opensearch](../vendors/opensearch.md).

## The market has four shapes

Almost every option is one of these, and the shape matters more than the
benchmark:

1. **Managed pure-play SaaS** — Pinecone, Weaviate Cloud, Zilliz Cloud, Qdrant
   Cloud. You send embeddings to someone else's cloud.
2. **Self-hosted OSS engines** — Qdrant, Milvus, Weaviate OSS. You run a stateful
   distributed database; embeddings never leave your tenancy.
3. **Embedded / in-process libraries** — Chroma, LanceDB. The index is a file or a
   library inside your app, not a server you operate.
4. **"Use what you already have"** — pgvector on Postgres, OpenSearch/Elasticsearch,
   MongoDB Atlas Vector Search, Redis, Azure AI Search, S3 Vectors. No new vendor,
   no new data store, no new DPA.

For a fund with an existing Postgres or Elastic estate, shape 4 is usually the
right default and shapes 1–3 need a reason.

## The pure-plays

As of 2026-08. Funding and ownership figures are dated because they move.

| Product | Shape | License | Ownership / funding (as of 2026-08) | Notes |
|---|---|---|---|---|
| **[pinecone](../vendors/pinecone.md)** | Managed SaaS only | Proprietary | Independent; ~$138M raised, $100M Series B (2023) at ~$750M. **Reportedly exploring a sale** — see M&A below | The original managed pure-play; serverless, lowest ops burden; not self-hostable, so embeddings live in their cloud |
| **[weaviate](../vendors/weaviate.md)** | OSS + managed cloud | BSD-3 | Independent; Series B $50M (2023), Series C (2025); RICOH Innovation Fund investment 2026-03-13 | Hybrid (vector + keyword) search, GraphQL API; self-host is the residency story |
| **Qdrant** | OSS + Cloud / Hybrid Cloud / Edge | Apache 2.0 | Independent; **$50M Series B announced 2026-03-12** (led by AVP; Bosch Ventures, Unusual, Spark, 42CAP), ~$87.8M total | Rust engine; the performance/filtering pick. Hybrid Cloud runs the data plane in *your* infrastructure with their control plane — the interesting shape for regulated buyers |
| **Milvus / Zilliz** | OSS + Zilliz Cloud | Apache 2.0 (LF AI & Data project) | Zilliz ~$113M raised; last round a $60M Series B extension (2022-08); ~139 employees (2026-03) | The billion-scale option; heaviest to operate. Vendor funding is old — worth watching |
| **Chroma** | Embedded-first + Chroma Cloud | Apache 2.0 | Independent; $18M seed (2023, led by Quiet Capital) — no later round found | The developer-experience/prototyping default; `pip install` and you have an index. Chroma Cloud (serverless on object storage, Rust core) GA **2025-08** |
| **LanceDB** | Embedded + cloud, on the Lance columnar format | OSS core | Independent; $30M Series A (2025-06) | Multimodal ("lakehouse") angle — text, image, video, plus SQL and full-text over the same files; used as an agent-memory substrate (e.g. CrewAI), Netflix and ByteDance cited as users |

## The substrate options

Not pure-plays; usually the cheaper and more governable answer.

| Option | Why it shows up |
|---|---|
| **pgvector** (Postgres) | The 2026 default for production RAG at fund scale. Vectors sit next to relational data, inherit your backup/DR/audit posture, and Postgres **row-level security** can enforce tenant/entitlement isolation *inside* the query (see the pre- vs post-filter trap below) |
| **[opensearch](../vendors/opensearch.md) / Elasticsearch** | Hybrid keyword+vector in an engine most shops already run for logs |
| **[azure-ai-search](../vendors/azure-ai-search.md)** | Azure-native; supports security-trimming via document-level ACLs — the closest thing to entitlement-aware retrieval you get for free |
| **MongoDB Atlas Vector Search, Redis** | Same "already in the estate" logic |
| **Amazon S3 Vectors** | Native vector storage in S3; GA 2025-12, expanded to 17 more regions 2026-03. AWS claims up to 90% cost reduction (vendor figure). Aimed at cold/large corpora, not low-latency serving |
| **turbopuffer** | Object-storage-native search engine; vendor cites 2.5T+ vectors and ~$0.02/GB storage. Same architectural bet as S3 Vectors and Chroma Distributed |
| **Vespa, Vertex AI Vector Search** | Large-scale hybrid search; GCP-native equivalent of Azure AI Search |

## One layer up: RAG platforms (not vector DBs)

These get named alongside vector databases but are a different purchase — they
bundle retrieval, generation, and (increasingly) governance. They belong nearer
[enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) and
[entitlement-aware-rag](../categories/entitlement-aware-rag.md) than to this page:

- **Vectara** — managed RAG/agent platform whose differentiator is
  **hallucination detection**: the Hughes Hallucination Evaluation Model (HHEM)
  and its public leaderboard, with HHEM-2.3 behind the API and HHEM-2.1-Open
  weights published. ~$53.5M raised ($25M Series A led by FPV Ventures and Race
  Capital). The measurable-groundedness angle also touches
  [llm-observability](../categories/llm-observability.md).
- **Contextual AI** — "RAG 2.0" enterprise RAG-agent platform from Douwe Kiela
  and Amanpreet Singh (ex-FAIR/Hugging Face; Kiela led the team behind the
  original 2020 RAG paper). ~$100M raised ($80M Series A); sells into banking and
  financial services (HSBC, Qualcomm cited).
- **Glean** already has a page under [entitlement-aware-rag](../categories/entitlement-aware-rag.md)
  — the permissions-mirroring index is the governance-relevant version of this
  same idea.

Neither Vectara nor Contextual AI has a wiki page yet; both are plausible
candidates and are flagged in open questions.

## Consolidation / M&A dynamics

The standalone vector DB is under pressure from both directions — bundling from
below (every OLTP and search engine added vectors) and object-storage economics
from above.

- **Pinecone is reportedly exploring a sale.** Secondary coverage (via *The
  Information*) says bankers were engaged, with speculation of a valuation above
  $2B against its last $750M mark, and Oracle, IBM, MongoDB and Snowflake floated
  as buyers. Founder Edo Liberty moved from CEO to Chief Scientist on
  **2025-09-08**, with Ash Ashutosh (founder of Actifio, acquired by Google 2020)
  named CEO; Ashutosh has publicly said an acquisition is not the goal.
  **Unconfirmed — no transaction announced as of 2026-08-24.**

  > Note (soft): this is press reporting, not a primary source, and "exploring a
  > sale" is not a deal. Tracked as a watch item, not an M&A state change.

- **The bear case is now said out loud.** Elastic CEO Ashutosh Kulkarni:
  *"Vector databases are a feature. They are never going to be a business in and
  of themselves."* Self-interested, but it matches the pgvector-wins pattern.
- **Money is still flowing to the OSS engines** — Qdrant's $50M Series B
  (2026-03), Ricoh's strategic investment in Weaviate (2026-03) — which suggests
  the survivors are the ones with a self-host story, not the managed pure-plays.
- **Zilliz's last disclosed round is 2022.** Not a red flag by itself for an
  OSS project with a foundation home, but worth noting before making Milvus a
  dependency.

For a buyer, the practical read: **prefer options with a credible exit path.**
Apache-2.0 engines and Postgres extensions survive their vendors; a proprietary
managed API does not.

## What actually matters for governance

The database choice is mostly not a security decision. Four things are:

1. **The index is a copy of your corpus with the ACLs stripped off.** Permissions
   lived on the SharePoint folder, not on the embedding. This is the classic RAG
   failure mode and it is a property of *the pipeline*, not the DB. See
   [entitlement-aware-rag-options](entitlement-aware-rag-options.md).
2. **Pre-filter, not post-filter.** Enforcement must happen *inside* the
   similarity query (namespace, metadata filter, Postgres RLS) — filtering the
   top-k after retrieval both leaks timing/existence signal and produces the
   "empty results" failure that tempts engineers to loosen the filter.
3. **Embeddings are sensitive data.** They are a lossy but partially invertible
   representation of the source text, so an embedding store holding MNPI is an
   MNPI store: it needs the same residency, encryption/BYOK, retention, and
   deletion treatment as the documents. This is why the shape (managed SaaS vs
   self-hosted vs embedded) is the decision that matters — it determines whether
   sensitive content leaves your tenancy at all. Adjacent: [dspm](../categories/dspm.md).
4. **Deletion has to propagate.** Removing a document from the system of record
   does nothing to its embedding, its chunks, or any agent memory built on top of
   it — see [agent-memory-landscape](agent-memory-landscape.md), where the same
   store reappears as the persistence layer for agent recall.

## Choosing, in one paragraph

If you already run Postgres, start with **pgvector** and stop; if you already run
Elastic/OpenSearch, start there. Reach for a pure-play only on a specific trigger:
scale past what Postgres serves comfortably, or a genuine need for hybrid/filtered
search performance (**Qdrant**), or billion-vector scale (**Milvus**), or
multimodal corpora (**LanceDB**). Choose **Pinecone** for lowest operational
burden *if* you accept third-party hosting of embeddings — a real MNPI/residency
question for a fund, and now also a vendor-continuity question. Use **Chroma** for
prototypes and expect to migrate.

## Open questions

- **Do Vectara and Contextual AI earn vendor pages?** Both make governance-relevant
  claims (measurable groundedness; regulated-industry RAG). Neither has been
  verified against primary sources. Probable homes:
  `enterprise-ai-assistant` / `entitlement-aware-rag`, with `llm-observability`
  cross-listing for Vectara.
- **Should Qdrant, Chroma, LanceDB, Milvus get stub vendor pages**, or does this
  page discharge the coverage obligation? Current answer: this page — they add
  nothing to the governance story that [weaviate](../vendors/weaviate.md) does not
  already carry.
- **[pinecone](../vendors/pinecone.md) needs a watch date** on the sale reporting;
  page updated 2026-08-24 with `verify_after`.
- Funding/pricing figures here are from secondary sources and vendor blogs, not
  cached primary filings. Promote and cache before any claim moves onto a vendor
  page.

## Sources

Accessed 2026-08-24; secondary/roundup-heavy except where noted. Two cached to
`raw/sources/` (the Pinecone and Qdrant items, which back page edits):

- [Qdrant Series B announcement (vendor, 2026-03-12)](https://qdrant.tech/blog/series-b-announcement/) — primary; supports round size, investors, licensing, product line
- [Qdrant raises $50M (TechTarget)](https://www.techtarget.com/searchdatamanagement/news/366640132/Qdrant-raises-50M-in-funding-to-fuel-vector-database-growth) — corroborates total raised
- [Pinecone founder moves to Chief Scientist, Ash Ashutosh named CEO (VentureBeat, 2025-09-08)](https://venturebeat.com/data-infrastructure/pinecone-founder-edo-liberty-appoints-googler-ash-as-ceo) — leadership change, sale reporting, funding
- [Elastic CEO on vector databases amid Pinecone sale talks (AIM Media House, 2025-08-31, upd. 2026-02-10)](https://aimmediahouse.com/market-industry/elastic-ceo-says-vector-databases-were-never-a-business-amid-pinecone-sale-talks) — the "feature, not a business" quote; sale talks
- [Vector database vendor Pinecone eyes future under new CEO (TechTarget)](https://www.techtarget.com/searchdatamanagement/news/366631366/Vector-database-vendor-Pinecone-eyes-future-under-new-CEO) — Ashutosh on acquisition intent
- [Ricoh invests in Weaviate via RICOH Innovation Fund (2026-03-13)](https://www.ricoh.com/release/2026/0616_1) — primary
- [Zilliz $60M Series B extension (vendor newsroom)](https://zilliz.com/news/vector-database-company-zilliz-series-b-extension) — funding; [Zilliz Crunchbase profile](https://www.crunchbase.com/organization/zilliz) — total raised, last round date
- [Chroma raises $18M seed (vendor)](https://www.trychroma.com/company/seed) and [SiliconANGLE coverage (2023-04-06)](https://siliconangle.com/2023/04/06/chroma-bags-18m-speed-ai-models-embedding-database/) — seed round, lead investor
- [LanceDB raises $30M Series A (vendor, 2025-06)](https://www.lancedb.com/blog/series-a-funding) — round, multimodal lakehouse framing, named users
- [Amazon S3 Vectors GA (AWS, 2025-12)](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-vectors-generally-available/) and [17-region expansion (AWS, 2026-03)](https://aws.amazon.com/about-aws/whats-new/2026/03/s3-vectors-expands-17-regions) — primary
- [turbopuffer](https://turbopuffer.com/) — vendor claims on scale and pricing
- [Vectara HHEM v2 / hallucination detection (vendor blog)](https://www.vectara.com/blog/hhem-v2-a-new-and-improved-factual-consistency-scoring-model) and [Vectara $25M Series A (BigDATAwire)](https://www.hpcwire.com/bigdatawire/this-just-in/vectara-secures-25m-series-a-funding-to-advance-rag-trustworthiness-with-new-mockingbird-llm/) — HHEM, funding
- [Contextual AI Series A (vendor)](https://contextual.ai/blog/announcing-series-a) and [Contextual AI (Wikipedia)](https://en.wikipedia.org/wiki/Contextual_AI) — founders, RAG 2.0, customers
- [Multi-tenant RAG isolation / document-level RBAC (Truto)](https://truto.one/blog/how-to-architect-strict-data-isolation-in-multi-tenant-rag-pipelines/) and [hard multi-tenancy for pgvector with RLS](https://pradeepbhandari.com/blog/pgvector-multi-tenancy-postgresql-rls-guide) — pre- vs post-filter failure mode
