---
title: OpenFGA (Auth0 / Okta FGA)
type: vendor
name: OpenFGA (Auth0 / Okta FGA)
slug: openfga
aka: [OpenFGA, Auth0 FGA, Okta FGA, Okta Fine Grained Authorization, Auth0 Fine-Grained Authorization]
primary_category: authorization-engine
also_listed_in: [entitlement-aware-rag]
website: https://openfga.dev
founded: 2022
hq: CNCF project (originated at Auth0/Okta, San Francisco, CA)
ownership_state: oss-foundation
owner: null
ownership_note: 'Open-source CNCF project (Apache-2.0). Created by the Auth0 FGA team at Okta; open-sourced 2022-06; accepted to CNCF Sandbox 2022-09-14; moved to Incubating 2025-10-28. Okta (NASDAQ: OKTA) sells the managed SaaS version, Auth0 FGA (also branded Okta FGA), which is built on OpenFGA. Grafana Labs and independent contributors are among the maintainers.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (open-source project, not a company)
last_funding: n/a
market_position: {authorization-engine: challenger, entitlement-aware-rag: niche-specialist}
deployment_model: [self-hosted, saas]
form_factor: [api, sdk]
data_leaves_tenancy: "false"
integrations: [postgresql, mysql, sqlite, langchain, langgraph, llamaindex, vercel-ai-sdk, auth0, okta, gravitee]
mcp_support: unverified
certifications: []
pricing_model: oss (Apache-2.0, free); Auth0/Okta FGA SaaS priced per monthly active user, sales-quoted
fs_traction: unverified
target_customer: Engineering teams building multi-user apps, RAG pipelines and agents whose permissions follow sharing and ownership relationships (documents, folders, teams, funds, accounts)
last_verified: 2026-10-26
verify_after: null
tags: [authorization, rebac, zanzibar, open-source, cncf, cncf-incubating, rag-authorization, agent-authorization, okta, auth0]
sources:
  - {claim: "Accepted to CNCF 2022-09-14; moved to Incubating 2025-10-28", url: "https://www.cncf.io/projects/openfga/", date: 2025-10-28, confidence: high}
  - {claim: "CNCF TOC voted OpenFGA to Incubation (CNCF blog dated 2025-11-11)", url: "https://www.cncf.io/blog/2025/11/11/openfga-becomes-a-cncf-incubating-project/", date: 2025-11-11, confidence: high}
  - {claim: "Incubation post: adopters Canonical, Docker, Grafana Labs, Read AI (RAG for enterprise search), Agicap, Headspace, Zuplo, Sourcegraph; Grafana Labs joined maintainers; 600+ contributors; joined Sandbox December 2022", url: "https://openfga.dev/blog/incubation-announcement", date: 2026-01-07, confidence: high}
  - {claim: "Originally developed by Auth0/Okta, open-sourced June 2022, donated to CNCF; created by the Auth0 FGA team; Zanzibar-inspired", url: "https://openfga.dev/project", date: 2026-10-26, confidence: high}
  - {claim: "Apache-2.0; PostgreSQL/MySQL/SQLite storage; in-memory for dev; used in production by Auth0 FGA since December 2021; ~6.0k stars", url: "https://github.com/openfga/openfga", date: 2026-10-26, confidence: high}
  - {claim: "Auth0 FGA RAG pattern: fetch from vector DB, then check each document with FGA before passing to the LLM; LangChain/LangGraph, LlamaIndex, Vercel AI SDK samples", url: "https://auth0.com/ai/docs/intro/authorization-for-rag", date: 2026-10-26, confidence: high}
  - {claim: "Okta FGA launch coverage; Limited Early Access late 2023", url: "https://www.helpnetsecurity.com/2024/03/05/okta-fga/", date: 2024-03-05, confidence: medium}
  - {claim: "Okta FGA FAQ: priced per monthly active user, no public rate card, trial only, 99.99% SLA (search snippet; direct fetch returned 404)", url: "https://community.auth0.com/t/frequently-asked-questions-on-okta-fine-grained-authorization/129768", date: 2026-10-26, confidence: low}
---

# OpenFGA (Auth0 / Okta FGA)

> Primary category: [authorization-engine](../categories/authorization-engine.md). Also listed in [entitlement-aware-rag](../categories/entitlement-aware-rag.md). Open-source **CNCF Incubating** project, not a company. This page also covers Okta's managed version (**Auth0 FGA**, also sold as **Okta FGA**), which runs OpenFGA. Sources cached under `raw/sources/2026-10-26--openfga--*`.

**One-liner**: An open-source permissions database modelled on Google's Zanzibar. You record who is related to what ("Alice is an analyst on Fund A", "Fund A owns this research folder") and ask it "can Alice read this document?" in milliseconds. Okta created it and sells it as a hosted service. Auth0 promotes it for filtering RAG results and limiting what agents can reach.

**What it does**: OpenFGA is a **relationship-based access control (ReBAC)** engine. You write an authorization model (types, relations, and how permissions derive from relations, such as "viewer of a document = viewer of its parent folder"). Your app writes relationship tuples as things change. The main queries are **Check** ("may user X do Y on Z?") and **ListObjects** ("which Zs may X see?"). Unlike stateless engines such as [open-policy-agent](open-policy-agent.md) or [amazon-verified-permissions](amazon-verified-permissions.md), it **stores** the relationship data (PostgreSQL, MySQL, or SQLite in beta), so callers don't have to send it with every request. This puts it in the same design family as [authzed](authzed.md)'s SpiceDB.

**AI and agent use**: The AI pitch comes mostly from Okta, not the project. Auth0's "Authorization for RAG" docs describe a **post-retrieval filter**: the app retrieves candidate chunks from the vector database, then asks FGA whether the user may view each source document, and only allowed documents reach the model. Auth0 publishes samples for LangChain/LangGraph, LlamaIndex and Vercel AI SDK. The same model can include agents as principals, so an agent acting for a user only reaches the documents and tools that user could. In the project's own adopter list, Read AI uses OpenFGA for "collaboration and RAG for enterprise search". [gravitee](gravitee.md) uses OpenFGA to authorize individual MCP methods in its MCP proxy. OpenFGA itself has **no MCP-specific authorization feature** that we found. Its docs MCP server and "agent skill" help developers write models; they are not enforcement points.

## Agent-security role: the lethal trifecta

The lethal trifecta is the core agent-security threat model: untrusted input, sensitive data and outbound access in one agent context. OpenFGA cuts the **sensitive-data** leg most directly. If every retrieval and record read is checked against the user the agent works for, a prompt-injected agent can only reach what that user could already see. It touches the **egress** leg only if you model tools and destinations as resources and your gateway calls it before each tool call. It does not inspect content, so it won't detect an injection. It also cannot catch oversharing that is already in the source permissions: if your tuples mirror a messy SharePoint, the agent inherits the mess (the problem [knostic](knostic.md) targets).

**Naming / provenance**: Created by the **Auth0 FGA team** at Okta, inspired by the Zanzibar paper. Auth0 FGA had used it in production since December 2021. It was open-sourced in **June 2022**, and the CNCF accepted it as a **Sandbox** project on **2022-09-14**. The project blog says "December 2022", which is probably the onboarding date rather than the vote; this is a soft discrepancy. It moved to **Incubating on 2025-10-28**; the CNCF announcement is dated 2025-11-11. The commercial service has used two names. Okta announced **"Okta FGA"** in Limited Early Access in late 2023 and covered it publicly in March 2024. Current Okta/Auth0 marketing uses **"Auth0 FGA"**. The SDK package `@auth0/fga` is titled "Okta Fine Grained Authorization" and now points users to the OpenFGA SDK. They are the same product; we found no formal rename notice.

**Ownership & viability**: `oss-foundation` (CNCF Incubating, Apache-2.0). Okta (NASDAQ: OKTA; see [okta](okta.md)) is the original and main sponsor because its paid FGA service runs on OpenFGA. That gives the project a funded steward with a commercial reason to keep it healthy. It also means much of the roadmap follows what Auth0 FGA customers need. Maintainer diversity is improving: Grafana Labs joined the maintainers, and the first independent maintainer was onboarded. The project reports 600+ contributors and about 6k GitHub stars (2026-10-26). Incubation is the CNCF's middle tier, one step below OPA's Graduated status. If Okta lost interest the project would still be under CNCF, but its main sponsor would be gone. We don't see a sign of that.

**Positioning & differentiators**:
- **vs [authzed](authzed.md) (SpiceDB)**: the closest peer, also an open-source Zanzibar engine. SpiceDB follows the Zanzibar paper more strictly (consistency tokens, Spanner/CockroachDB backends) and is backed by a venture-funded specialist that sells Dedicated and Enterprise editions. OpenFGA is foundation-governed with Okta's SaaS behind it and tends to be easier to start with (Postgres/MySQL, an FGA modelling language). Choose on operating model and support, not on core capability.
- **vs [open-policy-agent](open-policy-agent.md) / [cerbos](cerbos.md) / [amazon-verified-permissions](amazon-verified-permissions.md)**: those evaluate rules over attributes you pass in and store no relationships. OpenFGA fits when permissions come from ownership and sharing graphs (fund to team to analyst to folder to document). It is less natural for attribute rules like "only during market hours" or "only under $1M". The project blog describes conditional relationships for some of these cases (not verified in detail here), but it is not a general policy language.
- **vs [glean](glean.md) / [microsoft-graph](microsoft-graph.md)** in entitlement-aware RAG: those come with permissions already enforced for content they index. OpenFGA is a **component you build with**. You have to keep its tuples in sync with each source system's ACLs, which is the hard part.

*Market position*: `challenger` in [authorization-engine](../categories/authorization-engine.md). It is one of the two leading open-source Zanzibar engines, CNCF Incubating, but OPA remains the default PDP most firms already run. `niche-specialist` in [entitlement-aware-rag](../categories/entitlement-aware-rag.md): a building block for custom RAG, not a turnkey product.

**Who should choose them / anti-fit**: Fits firms **building their own RAG or agent applications** over content with real sharing structure (research libraries, deal rooms, client folders, fund and strategy hierarchies), and that want an open-source, foundation-governed engine or are already on Okta/Auth0 and want it hosted. **Anti-fit**: firms that only use off-the-shelf assistants (Copilot, Glean, ChatGPT Enterprise), where entitlement is the platform's job. Firms whose rules are mostly attributes and context (use OPA, Cerbos or Cedar). Small teams that cannot own the hard part, which is keeping relationship tuples in sync with source-system ACLs.

**Known weaknesses / gotchas**:
- **Sync is your problem.** OpenFGA only knows the relationships you write into it. If SharePoint or Confluence permissions change and your sync lags, it gives wrong answers. Each retrieval source needs a reliable feed.
- **Post-filtering can leak through counts and latency.** The documented Auth0 RAG flow retrieves first and filters after. For large corpora, also look at pre-filtering with ListObjects to avoid empty result pages and timing differences.
- **Stateful service to run.** Self-hosting means operating a database-backed service on the request path of every agent action. The alternative is a hosted SaaS outside your tenancy.
- **Two brands for one product.** Auth0 FGA and Okta FGA are the same thing. Contracts and docs use both names.

**Deployment & data handling**: Self-hosted open source runs as a server (binary, Docker or Kubernetes) with your own Postgres or MySQL. Nothing leaves your environment, so `data_leaves_tenancy: "false"` for the OSS deployment. **Auth0/Okta FGA** is multi-tenant SaaS (API at `*.fga.dev`). With it, relationship tuples (user IDs, object IDs, relations) are stored at Okta. Document content and prompts are not, unless you encode them in IDs. Regions and residency for the SaaS were not verified. Either way it is **inline**: each check is a synchronous call on the request path. No latency figures were verified.

**Integrations & partnerships**: Storage: PostgreSQL 14+, MySQL 8, SQLite (beta). SDKs for major languages (OpenFGA SDKs replace the old Auth0 FGA SDKs). AI frameworks through the Auth0 AI SDK samples: LangChain/LangGraph, LlamaIndex, Vercel AI SDK. Used inside [gravitee](gravitee.md)'s MCP proxy for method-level authorization. Named adopters: Canonical, Docker, Grafana Labs, Read AI, Agicap, Headspace, Zuplo, Sourcegraph. `mcp_support: unverified`: no MCP enforcement feature in the project itself.

**Compliance & FS traction**: The OSS project carries no certifications. Okta's SaaS sits under Okta's compliance programme, which was not verified for FGA specifically here. No financial-services adopter appears in the project's incubation post. FS evidence is `unverified`.

**Commercial**: OpenFGA is free (Apache-2.0). Per an Okta FAQ (search snippet only; direct fetch failed), Auth0/Okta FGA is priced **per monthly active user**, counted when a user ID appears in Check or ListObjects calls. Pricing is quoted by sales, a trial is available with no self-serve production free tier, and the SLA is 99.99%.

## Open questions

- Current Auth0/Okta FGA pricing, regions/data residency, and whether "Okta FGA" or "Auth0 FGA" is the contract name today.
- Any named financial-services adopter of OpenFGA or Auth0 FGA.
- Whether OpenFGA has, or plans, a CNCF Graduation application.
- Production performance figures at RAG scale (ListObjects on large corpora).
- Whether Okta's agent-identity products (Auth0 for AI Agents and similar) depend on FGA. Not checked on this pass.

## Sources

- [CNCF: OpenFGA](https://www.cncf.io/projects/openfga/) — fetched 2026-10-26 — supports: accepted 2022-09-14, Incubating 2025-10-28; confidence: high
- [CNCF blog: OpenFGA becomes a CNCF incubating project](https://www.cncf.io/blog/2025/11/11/openfga-becomes-a-cncf-incubating-project/) — fetched 2026-10-26 (via search) — supports: TOC vote, announcement 2025-11-11; confidence: high
- [OpenFGA blog: Accepted into CNCF Incubation](https://openfga.dev/blog/incubation-announcement) — fetched 2026-10-26 — supports: adopters, maintainers, Read AI RAG use; confidence: high
- [openfga.dev/project](https://openfga.dev/project) — fetched 2026-10-26 — supports: Auth0/Okta origin, June 2022 open-sourcing; confidence: high
- [openfga/openfga on GitHub](https://github.com/openfga/openfga) — fetched 2026-10-26 — supports: Apache-2.0, storage backends, Auth0 FGA production since 2021-12; confidence: high
- [Auth0: Authorization for RAG](https://auth0.com/ai/docs/intro/authorization-for-rag) — fetched 2026-10-26 — supports: RAG post-filter pattern and framework samples; confidence: high (vendor docs)
- [Help Net Security: Okta FGA](https://www.helpnetsecurity.com/2024/03/05/okta-fga/) — via search 2026-10-26 — supports: Okta FGA naming, late-2023 LEA; confidence: medium
- [Okta FGA FAQ (Auth0 community)](https://community.auth0.com/t/frequently-asked-questions-on-okta-fine-grained-authorization/129768) — search snippet 2026-10-26, page 404 on fetch — supports: MAU pricing, SLA; confidence: low

## History

- [2026-10-26] Page created and researched in one pass (user-requested addition). One page for the OSS project and Okta's managed Auth0/Okta FGA, slugged on the project, because Okta has no separate FGA company and [okta](okta.md) already exists for the parent. Cross-listed to entitlement-aware-rag because Auth0 documents an FGA RAG-filtering pattern and the project names a RAG adopter (Read AI). It is a build-it-yourself component, not a turnkey product. Confirmed CNCF Incubating (2025-10-28).
