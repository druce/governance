---
title: Gravitee
type: vendor
name: Gravitee
slug: gravitee
aka: [Gravitee.io, Gravitee AI Gateway, Gravitee AI Agent Management, Gravitee APIM]
primary_category: ai-gateway
also_listed_in: [mcp-gateway]
website: https://www.gravitee.io
founded: 2015
hq: Denver, Colorado, USA (engineering origin Lille, France; London office)
ownership_state: independent
owner: null
ownership_note: Private, VC-backed. Series C $60M announced 2025-05-20 led by Sixth Street Growth; ~$125M total raised. Not acquired, not public as of 2026-07-27.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$125M
last_funding: Series C, $60M, 2025-05-20 (Sixth Street Growth lead; Riverside Acceleration Capital, AlbionVC)
market_position: {ai-gateway: challenger, mcp-gateway: challenger}
deployment_model: [saas, self-hosted, hybrid, on-prem]
form_factor: [inline-proxy, api, platform]
data_leaves_tenancy: partial
integrations: [openai, anthropic, aws-bedrock, google-gemini, google-vertex, openfga, opentelemetry, kafka]
mcp_support: gateway
certifications: [iso-27001, iso-27701, soc2-type2, pci-dss]
pricing_model: platform
fs_traction: claimed
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [ai-gateway, mcp-gateway, api-management, llm-proxy, a2a, agent-gateway, open-source]
sources:
  - {claim: series-c-funding, url: "https://www.gravitee.io/blog/gravitee-raises-series-c-for-agentic-api-and-event-management", date: 2025-05-20, confidence: high}
  - {claim: ai-gateway-capabilities, url: "https://www.gravitee.io/platform/ai-gateway", date: 2026-07-27, confidence: medium}
  - {claim: mcp-gateway-capabilities, url: "https://www.gravitee.io/blog/gravitee-mcp-the-complete-guide-to-mcp-support", date: 2026-07-27, confidence: medium}
---

# Gravitee

> This page is scoped to **Gravitee's AI angle** — the **Gravitee AI Gateway** (LLM Proxy, MCP Proxy, A2A Proxy) and the surrounding "AI Agent Management" bundle. Gravitee is primarily an API- and event-management company (Gravitee APIM, Access Management, Kafka/event-native gateway); general API-management history is kept brief. Primary category: [ai-gateway](../categories/ai-gateway.md).

**One-liner** — Gravitee is an open-source-rooted API- and event-management vendor whose **AI Gateway** puts LLM calls, MCP tool calls, and agent-to-agent traffic behind one protocol-aware proxy with shared authentication, policy, and OpenTelemetry observability — the "your API gateway should govern AI too" play, with an unusually strong identity/authorization story attached.

## What it does

Gravitee's core is **Gravitee API Management (APIM)** — a self-hostable gateway with an
unusual event-native streak (native Kafka/MQTT/WebSocket entrypoints alongside REST).
The AI work is layered on the same v4 gateway as **three protocol-aware proxy types**,
each a distinct API type rather than a bag of plugins:

- **LLM Proxy** — sits between an LLM consumer and one or more providers, exposing an
  **OpenAI-compatible interface**. Named providers: OpenAI, Anthropic, AWS Bedrock,
  Google Gemini and Vertex. Token-aware quotas and rate limits, **semantic caching**,
  and cost attribution by team, model, use case, or agent.
- **MCP Proxy** — the tool path. Introduced in Gravitee 4.10, it introspects JSON-RPC
  2.0 payloads so policy targets **MCP method and tool names** rather than URL paths.
  The **MCP ACL policy** gates `tools/list`, `tools/call`, `prompts/list`,
  `resources/subscribe`, and `resources/read` individually. Tool-invocation throttling
  caps a misbehaving agent. Runs in Proxy and Studio modes.
- **A2A Proxy** — agent-to-agent delegation with what Gravitee describes as fully
  traceable on-behalf-of chains.

Two adjacent pieces matter for the MCP story:

- **MCP Tool Server** — converts an existing REST API into MCP tools straight from its
  **OpenAPI spec**, no backend changes, by enabling an MCP entrypoint on a v4 proxy API.
  This is MCP-server *generation*, the same trick [kong](kong.md) ships; the MCP Proxy
  above is the actual *gateway* in front of MCP servers you didn't build.
- **AI IAM** — standards-based authorization for agent tool access, separating decision
  from enforcement, using **OpenFGA** (relationship-based access control) and the
  **AuthZen** standard. Auth is OAuth 2.1 + PKCE backed by Gravitee Access Management,
  with Dynamic Client Registration and an **MCP Resource Server v2** (4.11) that handles
  token introspection so MCP servers can delegate authentication upstream.

Guardrail-side features are thinner than the routing/identity side: PII filtering and
prompt guardrails are listed, but with no independent evidence of detection quality.

## Where it sits in the stack

- Primary: [ai-gateway](../categories/ai-gateway.md) (model-prompt layer) — one governed
  exit door for model traffic, with cost, caching, and audit attached.
- Secondary: [mcp-gateway](../categories/mcp-gateway.md) — a genuine MCP proxy with
  method-level ACLs, not just an MCP-server generator.

**Risk role:** an inline chokepoint on outbound model and tool traffic. It decides which
models and which MCP methods/tools are reachable, authenticates the caller, throttles,
and writes an audit trail per interaction tied to agent identity and OAuth client. PII
filtering reduces leakage on the way out but is redaction, not full DLP; content
inspection is not where Gravitee's strength lies. It sits at the boundary between
internal apps/agents and external model and tool providers.

## Deployment & architecture

- **Inline proxy on the v4 data plane.** AI traffic traverses the same gateway as the
  rest of your APIs — no separate runtime if you already run Gravitee.
- **Deployment modes:** Gravitee Cloud (SaaS), fully self-hosted, and hybrid (Gravitee
  control plane + your data planes). A **customer-hosted control plane** is available on
  higher tiers subject to approval — the relevant option for a fund that will not put a
  control plane in a vendor's cloud.
- **Data handling:** self-hosted and customer-hosted-control-plane deployments keep
  prompt/response traffic in your tenancy; Gravitee Cloud does not. Frontmatter is
  therefore `partial` — it depends entirely on which mode you buy. Retention and
  training-use policy for the SaaS mode is unverified (see open questions).
- **Observability:** OpenTelemetry-native, with traces enriched by catalog entity IDs
  and the policy decisions taken at each hop, plus an MCP Analytics dashboard.

## Positioning & differentiators

- **API-management incumbent extending into AI — the same shape as [kong](kong.md).**
  Both pitch "you already need a gateway, let it govern AI too," both self-host, both
  generate MCP servers from OpenAPI specs. Gravitee is the smaller of the two by
  funding and mindshare, and is a **challenger** in both categories on that basis.
- **vs [kong](kong.md) specifically** — Gravitee's differentiators are (a) treating LLM,
  MCP, and A2A as three *first-class API types* with their own policy surfaces rather
  than plugins on a REST proxy, (b) a deeper native identity/authorization stack
  (Gravitee Access Management, OpenFGA/AuthZen-based AI IAM) where Kong leans on
  external IdPs, and (c) event-native ingest (Kafka) as a first-class citizen. Kong
  counters with far broader deployment base, more guardrail partnerships (Lakera, Azure
  Content Safety, Bedrock Guardrails), and a built-in PII sanitizer with published
  category/language coverage.
- **vs [litellm](litellm.md)** — LiteLLM is a developer-first OSS LLM proxy that a team
  stands up in an afternoon; Gravitee is enterprise gateway infrastructure with an
  operations cost, and is only rational if you want one control plane for APIs, events,
  and AI.
- **vs [portkey](portkey.md) and [truefoundry](truefoundry.md)** — those are AI-native;
  Gravitee's model-layer features (guardrails, prompt management, evals) are shallower,
  but it beats them on general API governance, self-hosting depth, and identity.
- **vs MCP-gateway-native peers ([agentgateway](agentgateway.md),
  [mintmcp](mintmcp.md), [ibm-contextforge](ibm-contextforge.md),
  [docker-mcp-gateway](docker-mcp-gateway.md))** — those are purpose-built and lighter to
  adopt for a team that only has an MCP sprawl problem. Gravitee's edge is that the MCP
  ACL sits in the same policy plane as your existing API authorization, and its OpenFGA
  integration gives fine-grained tool authorization that most OSS MCP gateways leave to
  a separate [authorization-engine](../categories/authorization-engine.md).
- **Publishes list prices**, which is rare in this space and useful for budgeting.

## Ownership, funding & M&A

- **Independent, private, VC-backed.** Founded **2015** in **Lille, France** as an
  open-source API-management project; now presents Denver, Colorado as its US base with
  offices in London and Lille. Founder-led: Rory Blundell (CEO), David Brassely (CTO),
  plus Nicolas Géraud, Titouan Compiegne, and Azize Elamrani.
- **Series C: $60M announced 2025-05-20**, led by **Sixth Street Growth** with Riverside
  Acceleration Capital and AlbionVC. TechCrunch put total raised at **just over $125M**.
  Valuation not disclosed. Prior: **$30M Series B (September 2022)**, Riverside
  Acceleration Capital lead, with Kreos Capital, AlbionVC, and Oxx; ~$11M Series A
  (2021).
- **No M&A.** Not acquired, not public, as of **2026-07-27**.
- **Acquisition-risk note:** a growth-stage API-management vendor sitting in a
  consolidating category is a plausible target for a networking or security platform —
  the same logic that took [portkey](portkey.md) into Palo Alto and CalypsoAI into
  [f5](f5.md). The mitigant for a buyer is that the Community Edition is Apache 2.0 and
  the gateway self-hosts, so an exit does not strand the data plane. Gravitee has not
  been reported as being in a process.
- **Analyst signal:** Gravitee claims Leader placement in the **Gartner Magic Quadrant
  for API Management (2025)** — a vendor claim, and note it is the *API Management* MQ,
  not any AI-gateway ranking.

## Who should choose them / anti-fit

- **Good fit:** a firm that already needs enterprise API management, wants one
  self-hostable control plane for APIs, events, and AI/agent traffic, and cares
  specifically about fine-grained, externalized authorization on the tool path. The
  customer-hosted control plane and Apache-2.0 core suit shops that will not send
  prompts through a vendor SaaS.
- **Anti-fit:** a fund whose only problem is "route model calls and log them." Gravitee
  is gateway infrastructure with real operational weight — [litellm](litellm.md) or a
  SaaS gateway ([cloudflare](cloudflare.md), [portkey](portkey.md)) gets you there in
  days. Also an anti-fit if you want deep AI-specific guardrails, red-teaming, or
  prompt/eval tooling out of the box; pair it with an
  [ai-runtime-security](../categories/ai-runtime-security.md) product instead. Teams
  standardized on Kong or another incumbent gateway have little reason to add a second.

## Known weaknesses / gotchas

- **The AI/agent features are a paid add-on.** Agent Management and Enterprise Auth are
  priced as separate packages on top of the API-management tier — the AI gateway is not
  included in the base subscription, and the Community Edition's coverage of these
  features is not documented.
- **Very new.** MCP Proxy landed in 4.10 (2026-01-22) and MCP Resource Server v2 in
  4.11. Treat production maturity of the MCP/A2A paths as unproven.
- **Guardrails are the thin part.** PII filtering and prompt guardrails exist but are
  described only at a marketing level, with no published detection coverage and no named
  guardrail partners of the sort Kong lists.
- **Smaller ecosystem** than Kong or the hyperscaler gateways: fewer integrations,
  smaller hiring pool, less community troubleshooting material.
- Most of what is documented above comes from **vendor sources**; independent
  corroboration of the AI-gateway capabilities was not found.

## Compliance & FS traction

- **Certifications:** ISO/IEC 27001 and ISO/IEC 27701, certified **2021-12-15**
  (certificate 175256, NQA/UKAS), scoped to API management, design, and security
  software. The Trust Center additionally lists **SOC 2 Type 2** and **PCI DSS v4.0.0**,
  with reports available on request. No FedRAMP found.
- **FS evidence:** `claimed`. Gravitee publishes a **Tide** case study (UK business
  banking / open banking), and markets open-banking API management as a use case. No
  asset-manager or hedge-fund reference found; named public logos skew industrial and
  postal (Michelin, Swiss Post, Posten Bring, Sedex). Nothing indicates the product
  assumes 10k seats — pricing starts at a size a mid-market firm can absorb.

## Commercial

Public list pricing, which is unusual here. API Management: **Planet $2,500/mo**,
**Galaxy** (mid-tier, event-broker support, consumption option), **Universe** (custom,
unlimited gateways). Event Management: **Comet $1,250/mo**, **Meteor**, **Asteroid**
(custom). **Agent Management** and **Enterprise Auth** are separately priced packages.
Community Edition is open source under Apache 2.0.

## Competitors / alternatives

[kong](kong.md) (closest analogue), [litellm](litellm.md), [portkey](portkey.md),
[truefoundry](truefoundry.md), [cloudflare](cloudflare.md), [f5](f5.md) in
[ai-gateway](../categories/ai-gateway.md); [agentgateway](agentgateway.md),
[mintmcp](mintmcp.md), [ibm-contextforge](ibm-contextforge.md),
[docker-mcp-gateway](docker-mcp-gateway.md) in
[mcp-gateway](../categories/mcp-gateway.md).

## Open questions / to verify

- Which AI/MCP features are in the Apache-2.0 Community Edition vs gated behind the
  Enterprise Agent Management package — the docs do not say.
- Gravitee Cloud (SaaS) data handling: prompt/response retention period and whether
  telemetry or content is used for any vendor purpose. Not published; `data_leaves_tenancy`
  is `partial` pending this.
- The registered legal HQ. The company page lists Denver, London, and Lille without
  designating one; the entity's origin is French. Recorded as Denver with the origin noted.
- SOC 2 Type 2 report period and auditor — listed in the Trust Center but not public.
- Gartner MQ for API Management 2025 Leader placement is a vendor claim; the report was
  not fetched.
- Independent (non-vendor) evaluation of the LLM Proxy and MCP Proxy in production —
  none found as of 2026-07-27.
- Whether the A2A Proxy is GA or preview, and which A2A spec version it tracks.

## Sources

- [Gravitee Raises Series C for Agentic API and Event Management (Gravitee blog)](https://www.gravitee.io/blog/gravitee-raises-series-c-for-agentic-api-and-event-management) — fetched 2026-07-27 — supports: $60M Series C announced 2025-05-20, Sixth Street Growth lead, customer names; confidence: high (vendor, corroborated below)
- [Gravitee raises $60M (TechCrunch, 2025-05-20)](https://techcrunch.com/2025/05/20/gravitee-a-platform-that-helps-companies-manage-apis-raises-60m/) — fetched 2026-07-27 — supports: ~$125M total raised, independent corroboration of the round; confidence: high
- [AI Gateway for LLM, MCP & A2A Governance (Gravitee product page)](https://www.gravitee.io/platform/ai-gateway) — fetched 2026-07-27 — supports: LLM/MCP/A2A proxies, provider list, semantic caching, PII filtering, OAuth 2.1, OpenTelemetry, SaaS/self-hosted/hybrid; confidence: medium (vendor marketing)
- [Gravitee 4.10: One Control Point to Secure & Govern AI Agents, MCP, and LLMs (Gravitee blog)](https://www.gravitee.io/blog/gravitee-4.10-one-control-point-to-secure-govern-ai-agents-mcp-and-llms) — fetched 2026-07-27 — supports: 4.10 release 2026-01-22, MCP Proxy, AI IAM, OpenFGA/AuthZen; confidence: medium (vendor)
- [Gravitee MCP: The Complete Guide to MCP Support (Gravitee blog)](https://www.gravitee.io/blog/gravitee-mcp-the-complete-guide-to-mcp-support) — fetched 2026-07-27 — supports: MCP Proxy vs MCP Tool Server, MCP ACL policy methods, MCP Resource Server v2 in 4.11, tool throttling, MCP Analytics; confidence: medium (vendor)
- [Gravitee pricing](https://www.gravitee.io/pricing) — fetched 2026-07-27 — supports: list prices, Agent Management as a separate package, deployment tiers; confidence: high (vendor's own price list)
- [Gravitee achieves ISO 27001 and ISO 27701 certification (Gravitee news)](https://www.gravitee.io/news/gravitee-achieves-iso-27001-and-iso-27701-certification) — fetched 2026-07-27 — supports: ISO 27001/27701 certified 2021-12-15, certificate 175256, NQA/UKAS; confidence: high
- [Gravitee Trust Center](https://trust.gravitee.io/) — fetched 2026-07-27 — supports: SOC 2 Type 2, PCI DSS v4.0.0 listings; confidence: medium
- [How Tide Scaled and Secured their API & Open Banking Initiatives with Gravitee](https://www.gravitee.io/case-studies/tide) — fetched 2026-07-27 — supports: FS/open-banking customer evidence; confidence: medium (vendor case study)
- [Gravitee company page](https://www.gravitee.io/company) — fetched 2026-07-27 — supports: founded 2015, founders, Denver/London/Lille offices, Gartner MQ Leader claim; confidence: medium (vendor)

## History

- [2026-07-27] Stub created and researched in one pass (user-requested addition, not a seed/CSV row). Established: founded 2015 in Lille, France; independent VC-backed, Series C $60M (2025-05-20, Sixth Street Growth), ~$125M total raised, no M&A. Confirmed a genuine AI-gateway and MCP-gateway product line (LLM Proxy / MCP Proxy / A2A Proxy, MCP ACL policy, AI IAM on OpenFGA/AuthZen) rather than generic API management. Filed primary `ai-gateway`, cross-listed `mcp-gateway`; position `challenger` in both. 3 sources cached.
