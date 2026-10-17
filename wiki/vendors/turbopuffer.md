---
title: turbopuffer
type: vendor
name: turbopuffer
slug: turbopuffer
aka: [Turbopuffer, tpuf]
primary_category: vector-retrieval
also_listed_in: [entitlement-aware-rag]
website: https://turbopuffer.com/
founded: 2023
hq: Ottawa, Ontario, Canada (offices also in Vancouver and New York)
ownership_state: independent
owner: null
ownership_note: "VC-backed, founder-led. Investors include Lachy Groom and Thrive Capital (undisclosed round reported 2025-12-19). CEO said in ~May 2026 the company was profitable, past $100M run-rate, and had raised under $1M; how that fits with the Thrive round is unclear."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "Undisclosed round, Thrive Capital (new) + Lachy Groom (existing), reported 2025-12-19"
market_position: {vector-retrieval: ai-native-disruptor, entitlement-aware-rag: niche-specialist}
deployment_model: [saas, hybrid]
form_factor: [api]
data_leaves_tenancy: partial
integrations: [aws, gcp, aws-privatelink, gcp-private-service-connect]
mcp_support: unverified
certifications: [soc2-type2, hipaa-baa]
pricing_model: usage
fs_traction: claimed
target_customer: AI-native software companies and large enterprises running high-volume or many-tenant search (engineering-led buyers)
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [vector-database, full-text-search, hybrid-search, object-storage, byoc, multi-tenant, aie-nyc-2026]
sources:
  - {claim: "Object-storage-native vector + BM25 + hybrid search with metadata filtering; SSD/memory cache over S3/GCS; scale claims; customer logos incl. Bridgewater Associates", url: "https://turbopuffer.com/", date: 2026-10-16, confidence: medium}
  - {claim: "SOC 2 Type 2; HIPAA BAA on request; CMEK per namespace (Enterprise); single-tenant clusters; PrivateLink / Private Service Connect; SSO and IP allowlisting on Scale+", url: "https://turbopuffer.com/docs/security", date: 2026-10-16, confidence: high}
  - {claim: "Plan minimums Launch $16/mo, Scale $256/mo, Enterprise $4,096/mo + 35% usage premium; BYOC and single-tenancy Enterprise-only", url: "https://turbopuffer.com/pricing", date: 2026-10-16, confidence: high}
  - {claim: "No built-in row-level access control; permissions implemented by storing user/group IDs on documents and filtering at query time", url: "https://turbopuffer.com/docs/permissions", date: 2026-10-16, confidence: high}
  - {claim: "Undisclosed round from Thrive Capital and Lachy Groom; founded 2023 by ex-Shopify engineers Simon Eskildsen and Justine Li; ~22 staff", url: "https://betakit.com/?p=398272", date: 2025-12-19, confidence: medium}
  - {claim: "CEO: crossed $100M run-rate in March 2026, profitable, <$1M raised; names Bridgewater among customers", url: "https://x.com/Sirupsen/status/2057470756070781400", date: 2026-10-16, confidence: medium}
  - {claim: "AIE NYC 2026 agenda: Bridgewater 'Vault' talk (2026-10-13) does not name turbopuffer or permissions; turbopuffer is a Gold sponsor and listed speaker company", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# turbopuffer

> Primary category: [vector-retrieval](../categories/vector-retrieval.md). Also listed in [entitlement-aware-rag](../categories/entitlement-aware-rag.md), with caveats (see below).

**One-liner** — A search engine (vector, full-text and hybrid) that stores its indexes in cloud object storage and caches hot data on SSD and memory. That makes very large or heavily multi-tenant retrieval cheap, at the cost of slower queries on data that isn't cached.

**What it does** — An API-only database for first-stage retrieval in RAG and agent systems. It does vector search, BM25 full-text search, hybrid ranking and metadata filtering over "namespaces", which are independent indexes. Customers commonly create one namespace per end-customer or per user. The data lives in S3 or GCS. A query against a warm namespace is served from the cache (vendor example: about 14ms p50 for vector search on 10M documents). A cold namespace has to be read from object storage first, which is slower. Vendor scale claims: 1T+ documents in total, up to 128B documents per namespace, 250M+ namespaces. These are marketing figures, but they match the logo list, which is heavy on high-volume AI products (Cursor, Notion, Anthropic, Linear, Superhuman).

**Naming / provenance** — Founded in **2023** by **Simon Eskildsen (CEO)** and **Justine Li (CTO)**, both former Shopify infrastructure engineers. The company is described as Ottawa-based, with offices in Vancouver and New York. The name is written lowercase.

**Ownership & viability** — `independent`, founder-controlled and VC-backed. BetaKit reported an **undisclosed round from Thrive Capital (new) and Lachy Groom (existing)** on 2025-12-19. In a post around May 2026, the CEO said turbopuffer **crossed $100M run-rate in March 2026, is profitable, and had raised under $1M**. Those figures are company-reported and unaudited. Sacra's estimate is consistent with them.
> Contradiction (soft): "<$1M raised" vs a reported Thrive Capital round in Dec 2025 of undisclosed size. Possibly secondary-heavy or primary not counted; not resolvable from public sources. Flagged 2026-10-16.

Viability looks strong for a company this young: it is profitable by its own account and has demanding reference customers. The acquisition-risk question cuts the other way. A cloud provider or data platform could plausibly want it, and AWS's own S3 Vectors already competes on the same architectural idea. BYOC customers would keep their data in their own bucket if the company exited. SaaS customers would depend on the acquirer's roadmap.

**Positioning & differentiators** — `ai-native-disruptor` in vector-retrieval: it is a young company winning AI-native workloads from incumbents on cost and scale. `niche-specialist` in entitlement-aware-rag, because it provides filtering primitives rather than an entitlement product.
- **Versus [pinecone](pinecone.md):** both are managed, API-first services. turbopuffer's bet is object storage as the source of truth, which makes storage cheap and cold data slow. Pinecone is reportedly exploring a sale (see its page), which matters for a long-lived dependency. turbopuffer offers BYOC on Enterprise.
- **Versus [weaviate](weaviate.md) / [opensearch](opensearch.md):** those can be fully self-hosted. turbopuffer cannot. Its nearest option is BYOC, where it runs in your cloud account. OpenSearch brings mature document-level security plugins. turbopuffer has none built in.
- **Versus Amazon S3 Vectors / pgvector:** S3 Vectors makes the same storage bet as a cloud primitive, aimed at cold data. pgvector is the "use what you have" default this wiki recommends for most funds. turbopuffer sits between them: faster than S3 Vectors on warm data, with far more scale headroom than a single Postgres. See [vector-database-landscape](../comparisons/vector-database-landscape.md).
- **Very many namespaces:** per-tenant or per-user namespaces at the hundreds-of-millions scale are the distinctive capability. Namespace-per-user is one way to isolate data, but it does not model shared documents with overlapping access.

**Entitlement-aware RAG: does it belong?** Partly. turbopuffer's own docs say it has **no built-in row-level access control**. Its [Permissions doc](https://turbopuffer.com/docs/permissions) tells you to store `user_id`/`group_ids` arrays on each document and pass the caller's IDs as a filter at query time. The inverted index handles "tens of thousands of IDs" per attribute and arrays of up to 8 MiB. That is a solid **filtering primitive**: the filter is applied during the search rather than after it, so a user's results are not silently cut short. It is **not entitlement sync**. Nothing in turbopuffer reads ACLs from SharePoint or Google Drive, resolves group membership, or reacts when someone's access changes. Your ingestion pipeline and auth layer have to do all of that. Compared with [glean](glean.md) or [microsoft-graph](microsoft-graph.md), which mirror source-system ACLs themselves, turbopuffer covers the enforcement step and leaves the hard work of keeping permissions correct to you. It is listed here because a fund building its own permissioned RAG needs a retrieval layer that can enforce per-user filters at scale, and turbopuffer is credible at that. A buyer should not treat it as an entitlement solution.

**AIE NYC 2026 / Bridgewater** — **Bridgewater Associates is a customer according to the vendor**: it appears in the homepage logo wall and in the CEO's customer list. No published Bridgewater case study exists; the customer stories page has 12 stories and none is Bridgewater. At AI Engineer New York (2026-10-12 to 2026-10-14), Bridgewater gave a main-stage talk on 2026-10-13, *"Vault: Making Unstructured Data Work for Investing"* (Aaron Linsky and Sam Green). turbopuffer was a Gold sponsor and is listed as a speaker company. **The published agenda does not tie the Bridgewater talk to turbopuffer, and its blurb does not mention permissions or access control.** No recording or write-up was found as of 2026-10-16. The claim that the talk showed **row-level permissions enforced at retrieval across millions of documents with changing access scopes is therefore unverified**. If it is accurate, it would most likely describe Bridgewater's own entitlement logic implemented with turbopuffer filters. The vendor's documentation says there is no native row-level permissions feature.

**Who should choose them / anti-fit** — Fits an **engineering-led firm building its own RAG or agent retrieval** at large scale or high tenant counts, where cost per stored GB matters. It also fits one that wants BYOC so the data stays in its own cloud account, and that has (or will build) its own entitlement pipeline. **Anti-fit:** a firm wanting fully air-gapped or on-prem deployment (not offered). A firm expecting the database to handle document permissions for it. A small fund whose corpus fits comfortably in pgvector or [azure-ai-search](azure-ai-search.md). Workloads that need consistently low latency on rarely queried data, because cold namespaces are slower.

**Known weaknesses / gotchas** —
- **No native access control.** Permissions are a filter you construct. If your pipeline gets the ACL arrays wrong, retrieval leaks, and nothing in the database will catch it.
- **Cold-query latency** is inherent to the object-storage design. Pin hot namespaces (up to 256 pinned).
- **SaaS by default.** Single-tenancy, BYOC, CMEK and private networking are all **Enterprise-only**: a $4,096/month minimum plus a 35% usage premium.
- Performance and cost claims ("10x cheaper") are vendor marketing; no independent benchmark was found.

**Deployment & data handling** — Three tiers: multi-tenant SaaS (AWS and GCP regions; data stays "exclusively in the region you select"), single-tenant clusters, and **BYOC**, where the data plane runs in the customer's cloud account (Enterprise; Legora and Atlassian are cited BYOC customers). `data_leaves_tenancy: partial`: on SaaS, documents and embeddings sit in turbopuffer's object storage. With BYOC they stay in your account. The extent of control-plane or telemetry egress under BYOC is unverified. Encryption: AES-256 at rest, with optional per-namespace CMEK. Staff access to customer data requires the customer's written consent and is logged; multi-party approval is a paid add-on. turbopuffer is an API that sits on the retrieval path, not a proxy.

**Integrations & partnerships** — Runs on AWS and GCP, with AWS PrivateLink and GCP Private Service Connect for Enterprise. SSO for the dashboard and IP allowlisting on Scale and above. Audit logs on Scale and above, with log streaming as an add-on. A [Google Cloud customer case study](https://cloud.google.com/customers/turbopuffer) exists (surfaced in search, not reviewed). MCP support and framework integrations (LangChain, LlamaIndex etc.) were not verified for this page.

**Compliance & FS traction** — **SOC 2 Type 2** (report via Trust Center). HIPAA BAA available (Scale and above). GDPR/CCPA DPA for all customers. FS traction is `claimed`: **Bridgewater Associates** is a logo and is named by the CEO, and Kepler (a financial-document search company) has a customer story. No Bridgewater-authored or co-published case study was found. Scale fit is not a concern for a hedge fund; if anything the product is sized for much larger corpora than most funds have.

**Commercial** — Usage-based (storage, writes, queries) with monthly minimums: **Launch $16, Scale $256, Enterprise $4,096 plus a 35% usage premium**. Per-unit rates are on the vendor's pricing calculator and were not captured here.

## Open questions

- Was turbopuffer part of Bridgewater's AIE NYC 2026 "Vault" talk, and what exactly was shown about permissions? Check for the recording.
- How permission *changes* are handled at scale: cost and latency of patching ACL arrays across millions of documents. The docs don't cover it.
- What metadata or telemetry, if any, leaves the customer account under BYOC.
- Actual primary capital raised (CEO's "<$1M" vs the Thrive round) and the size of the Dec-2025 round.
- MCP server or agent-framework integrations.
- Independent latency and cost benchmarks against Pinecone, S3 Vectors and pgvector.

## Sources

- [turbopuffer homepage](https://turbopuffer.com/) — fetched 2026-10-16 — supports: architecture, scale claims, customer logos (incl. Bridgewater Associates); confidence: medium (vendor marketing)
- [turbopuffer Security & Compliance docs](https://turbopuffer.com/docs/security) — fetched 2026-10-16 — supports: SOC 2 Type 2, BAA, CMEK, single-tenant, private networking, SSO; confidence: high
- [turbopuffer pricing](https://turbopuffer.com/pricing) — fetched 2026-10-16 — supports: plan minimums, Enterprise-only BYOC/single-tenancy; confidence: high
- [turbopuffer customers](https://turbopuffer.com/customers) — fetched 2026-10-16 — supports: 12 case studies, BYOC customers, no Bridgewater story; confidence: high
- [turbopuffer Permissions docs](https://turbopuffer.com/docs/permissions) — fetched 2026-10-16 — supports: no built-in row-level access control; filter-based pattern; confidence: high
- [BetaKit, 2025-12-19](https://betakit.com/?p=398272) — fetched 2026-10-16 — supports: Thrive/Lachy Groom round, founders, founding year, HQ, headcount; confidence: medium
- [Simon Eskildsen on X (~2026-05)](https://x.com/Sirupsen/status/2057470756070781400) — text via search snippet 2026-10-16 (page returned HTTP 402) — supports: $100M run-rate, profitable, <$1M raised, Bridgewater named; confidence: medium
- [AI Engineer New York 2026 agenda](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Bridgewater "Vault" talk details, turbopuffer Gold sponsor, no stated link between them; confidence: high
- Cached: `raw/sources/2026-10-16--turbopuffer--product-security-pricing.md`, `raw/sources/2026-10-16--turbopuffer--permissions-docs.md`, `raw/sources/2026-10-16--turbopuffer--funding-bridgewater-aie.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
