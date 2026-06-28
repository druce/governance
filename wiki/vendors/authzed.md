---
type: vendor
name: AuthZed (SpiceDB)
slug: authzed
categories: [authorization-engine]
layer: model-prompt
aliases: [SpiceDB, Zanzibar]
website: "https://authzed.com"
founded: 2020
hq: New York, NY, USA
ownership: independent
ownership_detail: "VC-backed; ~$16M raised (Series A $12M, 2024-06, General Catalyst)"
ownership_confidence: high
funding_total: ~$16M
last_funding: "Series A $12M (2024-06, General Catalyst)"
deployment: [self-hosted, saas, on-prem]
target_customer: enterprise (platform/security teams)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [authorization, rebac, zanzibar, permissions-database, open-source, spicedb]
---

# AuthZed (SpiceDB)

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). Independent, VC-backed (Series A).

**One-liner** — A Google-Zanzibar-style **permissions database** (open-source **SpiceDB**) that stores relationships between users, resources, and groups and answers fine-grained "who can access what" at scale — relationship-based access control (ReBAC).

## What it does
AuthZed builds and commercializes **SpiceDB**, an open-source implementation of **Google's Zanzibar** model (the system behind Google Drive/Docs sharing). Unlike a stateless policy engine, SpiceDB is a **database**: you write relationship tuples ("user X is editor of doc Y," "team A owns folder Z") and a schema, then query permissions; it computes answers across deep relationship graphs consistently and quickly. This makes it the natural choice when access is fundamentally about **relationships and nesting** (sharing, hierarchies, multi-tenancy) rather than role/attribute rules alone.

## Where it sits in the stack
Primary [authorization-engine](../categories/authorization-engine.md) — the ReBAC/Zanzibar member of the category. Layer: model-prompt. Lethal-trifecta role: constrains the **sensitive-data** and **egress** legs by deciding whether a principal (user or agent) may access a specific resource; not prompt-content inspection (that's [ai-runtime-security](../categories/ai-runtime-security.md) / [agent-runtime-security](../categories/agent-runtime-security.md)). For agents, it answers "may this agent, acting for this user, see this exact record?" — relevant to **entitlement-aware** designs (cf. [entitlement-aware-rag](../categories/entitlement-aware-rag.md)).

## Deployment & architecture
Open-source **SpiceDB** (Apache-2.0) self-hosted; **AuthZed** offers managed **Dedicated** (single-tenant cloud), **Serverless**, and on-prem **Enterprise** editions with SLAs. Stores its own relationship data (stateful) backed by Postgres/CockroachDB/Spanner-class stores; exposes a gRPC/HTTP permissions API with Zanzibar-style consistency tokens (zookies). Pairs with your IdP for identity; it stores the *relationships*, not credentials. Current site markets it as "the authorization platform for AI and modern applications."

## Positioning & differentiators
The **Zanzibar/ReBAC specialist** — deepest fit when permissions are relationship-graph-shaped at scale. Versus [open-policy-agent](open-policy-agent.md) / [cerbos](cerbos.md) (stateless policy engines that evaluate rules over attributes you supply but don't store relationships), [oso](oso.md) (Polar DSL, does ReBAC too but less Zanzibar-purist), [permit-io](permit-io.md) (managed wrapper over OPA/Cedar), [styra](styra.md) (enterprise OPA). The tradeoff: SpiceDB owns a stateful permissions store (more power for relationship data, more to operate) where stateless engines push data-fetching to the caller.

## Ownership, funding & M&A
Founded **2020** by **Jimmy Zelinskie, Jake Moshenko, and Joseph (Joey) Schorr/Zwicker** — ex-CoreOS/Quay infrastructure engineers. HQ **New York, NY** (some sources list SF). Raised **~$16M**: Series A **$12M** (**2024-06**, led by General Catalyst, with Work-Bench, Y Combinator, Amplify Partners). **No M&A** — independent (no seed flag). Confidence high.

## CTO / hedge-fund lens
Day-2. The right pick specifically when your authorization is **relationship/sharing-heavy** — document/folder hierarchies, nested teams, multi-tenant data — and you want consistent, fast checks an agent can call before reading a record. Heavier to run than a stateless engine (it's a database you operate, or you buy the managed tier). For a fund doing entitlement-aware RAG over shared content, SpiceDB-style ReBAC is a strong primitive; for simple role/attribute checks, [cerbos](cerbos.md) / [open-policy-agent](open-policy-agent.md) are lighter. Series-A vendor — manage vendor-risk, though the OSS core limits lock-in.

## Competitors / alternatives
[open-policy-agent](open-policy-agent.md), [cerbos](cerbos.md), [oso](oso.md), [permit-io](permit-io.md), [styra](styra.md).

## Open questions / to verify
- Exact NY-vs-SF HQ and any funding since the 2024 Series A.
- Production references for *agent* authz specifically (vs application ReBAC).

## Sources
- [AuthZed Raises $12 Million in Series A (BusinessWire, via startupintros/authzed.com)](https://startupintros.com/orgs/authzed) — fetched 2026-06-28 — supports: Series A $12M 2024-06 General Catalyst, ~$16M total, 2020 founding, founders, NY HQ, SpiceDB/Zanzibar/ReBAC; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2020 founding, NY HQ, founders (ex-CoreOS/Quay), ~$16M funding (Series A $12M 2024 General Catalyst), SpiceDB/Zanzibar/ReBAC positioning. No M&A — independent. Confidence high.
