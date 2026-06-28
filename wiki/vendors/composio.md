---
type: vendor
name: Composio
slug: composio
categories: [tool-identity-integration]
layer: model-prompt
aliases: [Sampark Inc.]
website: https://composio.dev
founded: 2023
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Venture-backed and independent as of 2026-06; no acquisition found. Legal entity Sampark Inc.
ownership_confidence: medium
funding_total: ~$29M (vendor-stated total)
last_funding: Series A, $25M, 2025-07 (led by Lightspeed Venture Partners)
deployment: [saas, api, sdk, self-hosted]
target_customer: developers / engineering teams building AI agents; startups to enterprise
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [tool-identity-integration, agent-tooling, managed-auth, oauth, mcp, tool-calling]
---

# Composio

> A managed tool-calling and integration platform that gives AI agents authenticated access to
> hundreds of SaaS apps (Gmail, Slack, GitHub, etc.), handling the OAuth/API-key plumbing for them.

**One-liner** — Developer infrastructure that lets an AI agent securely call external SaaS tools
through one API, with Composio managing the authentication (OAuth flows, API keys, tokens) so the
builder doesn't have to.

**Categories** — [tool-identity-integration](../categories/tool-identity-integration.md)

## What it does

Composio sits between AI agents/LLMs and the outside world of SaaS applications. It exposes a large
catalog of pre-built tool integrations — Gmail, Slack, GitHub, Notion, Jira, Google Calendar,
Salesforce and many more (vendor claims range from ~250 to "3,000+" apps depending on source and
date) — as functions an agent can call. The hard part it solves is **authentication**: connecting an
agent to a user's third-party accounts normally means handling per-user OAuth consent flows, storing
and refreshing tokens, juggling API keys, scopes and rate limits. Composio manages that credential
lifecycle on the developer's behalf. In its SDK pattern, a builder creates a session with a `user_id`,
retrieves the available tools, and passes them to whatever LLM framework they use; Composio resolves
the right per-user credentials transparently at execution time.

The platform also markets an "experience/skills" layer — a reinforcement-learning component meant to
let agents improve at using tools over time and share learned workflows across the platform — but the
core, shippable value today is **managed agent→SaaS connectivity with auth handled**.

## Where it sits in the stack

Primary category: [tool-identity-integration](../categories/tool-identity-integration.md) (Model/Prompt layer, Day-2). This is the plumbing
that connects agents to the tools they act on. Composio's relevance to the **lethal trifecta** is
indirect but real: by brokering an agent's authenticated access to external SaaS systems, it governs
two legs — **sensitive-data** access (the agent can now read your Gmail/Drive/Salesforce) and
**egress** (the agent can now *write* — send mail, post to Slack, open GitHub PRs). It does **not**
itself filter untrusted input or inspect prompts; a compromised or prompt-injected agent with broad
Composio scopes is a meaningful blast-radius concern. Composio is therefore a capability enabler that
needs to be paired with authorization/guardrail controls ([ai-runtime-security](../categories/ai-runtime-security.md),
[authorization-engine](../categories/authorization-engine.md), [mcp-gateway](../categories/mcp-gateway.md)) rather than a security control in its own right. Trust-zone
wise it lives at the boundary between the agent runtime and third-party SaaS.

## Deployment & architecture

- **API + SDKs** — Python and TypeScript SDKs; a unified tool-calling API. Framework-agnostic (works
  with common agent frameworks / direct LLM tool-calling).
- **Managed auth** — handles OAuth 2.0 consent flows, token storage/refresh, and API-key management
  per end-user (`user_id`-scoped credentials).
- **MCP support** — exposes tools via the Model Context Protocol in addition to native provider
  packages, so it doubles as an MCP server layer (overlaps [mcp-gateway](../categories/mcp-gateway.md)).
- **Deployment models** — primarily SaaS/cloud; docs reference self-hosted options as well.
- **Integrations** — the catalog itself is the integration surface (SaaS apps); on the consuming side
  it plugs into agent frameworks and LLM providers.

## Positioning & differentiators

Composio's pitch is "auth + tools for agents, batteries included" — a broad pre-built connector
catalog plus managed authentication, aimed at developers who don't want to hand-roll OAuth for every
SaaS an agent touches. It is developer/SDK-first and integration-breadth-led.

Nearest neighbors differ in emphasis: [arcade](arcade.md) is the closest comparable (tool-calling + agent auth,
also MCP-oriented) and competes head-on; [stackone](stackone.md) focuses on managed, enterprise-grade SaaS
integrations (often HR/ATS/CRM) delivered as agent tools; [descope](descope.md), [stytch](stytch.md) and [workos](workos.md) come
at the same problem from the **identity** side — they provide agent/app auth, OAuth token vaulting and
"connect to third-party APIs on a user's behalf" primitives, but with less of a pre-built *tool
catalog*. [cyberark](cyberark.md) addresses the adjacent non-human/secrets angle for enterprises. Composio's
differentiation is breadth of ready-made tools + the managed-auth convenience; its weaker story
(for a security buyer) is governance — fine-grained authorization, audit and least-privilege scoping
are not its headline.

## Ownership, funding & M&A

Independent, venture-backed. Founded **2023** by IIT-Bombay alumni **Soham Ganatra** (CEO) and
**Karan Vaidya**; legal entity **Sampark Inc.**, headquartered in **San Francisco**. Funding: a
**$25M Series A led by Lightspeed Venture Partners** (announced ~July 2025), with SV Angel and angels
including Dharmesh Shah (HubSpot); the vendor states **~$29M total** raised (Series A plus an earlier
seed). **No acquisition found** — the seed registry carried no M&A flag and nothing in research
indicates one; ownership set to `independent`, confidence `medium` (no primary cap-table doc reviewed;
funding figures from the Series A announcement + vendor blog).

> Soft note: an aggregator (Tracxn) dates the Series A to 2025-03-25, while the Series A press
> coverage and vendor blog are from ~July 2025. Treated as aggregator imprecision, not a hard
> conflict; the ~$29M total is consistent across sources.

## CTO / hedge-fund lens

**Day-2, and niche** for a hedge fund. Composio is builder infrastructure: you'd only care about it if
your firm is **building its own AI agents** that need to act inside SaaS systems (e.g. an internal
agent that triages email, files in Jira, or pulls from GitHub). For a shop that mostly *buys* AI
assistants ([enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)) rather than building agents, it is not on the critical path.
Where it is relevant, the governance questions dominate: handing a third-party platform brokered OAuth
access to your Gmail/Slack/GitHub means Composio holds (or mediates) tokens to sensitive systems — a
vendor-risk, data-residency and least-privilege review item ([vendor-risk](../categories/vendor-risk.md)), and an SR 11-7 concern
only insofar as such an agent feeds a model-driven process. It is **not** a control you deploy for
safety; if you use it, wrap it with authorization ([authorization-engine](../categories/authorization-engine.md)), runtime guardrails
([ai-runtime-security](../categories/ai-runtime-security.md)) and human-in-the-loop approvals on consequential actions. Best fit: a
fund with a real internal-engineering / agent-building effort, not a 50-person shop standing up basic
AI hygiene.

## Competitors / alternatives

[arcade](arcade.md), [stackone](stackone.md), [descope](descope.md), [stytch](stytch.md), [workos](workos.md), [cyberark](cyberark.md); adjacent: [mcp-gateway](../categories/mcp-gateway.md)
tooling and DIY (hand-rolled OAuth + per-tool integrations).

## Open questions / to verify

- Exact current integration count (sources span ~250 to 3,000+) and how many are write-capable.
- Where credentials/tokens are stored and under what certifications (SOC 2, data residency) — material
  for a vendor-risk review; not confirmed from a primary doc.
- Whether the self-hosted/enterprise deployment keeps tokens inside the customer boundary.
- Seed-round size/date and full investor list (only ~$29M total and the $25M Series A are confirmed).
- Maturity and real-world adoption of the "skills/RL experience" layer vs. the core tool-calling product.

## Sources

- [Composio raises $25M in funding to ease AI agent development (SiliconANGLE)](https://siliconangle.com/2025/07/22/composio-raises-25m-funding-ease-ai-agent-development/) — fetched 2026-06-28 — supports: $25M Series A led by Lightspeed (~$29M total), founders Soham Ganatra/Karan Vaidya, legal name Sampark Inc., managed-auth/tool-calling product, MCP, 200+ customers incl. Glean; confidence: high (trade press, primary on funding).
- [We raised $29M to build skills that evolve with your agents (Composio blog)](https://composio.dev/blog/series-a) — fetched 2026-06-28 — supports: ~$29M total raise (vendor-stated), Series A framing, product thesis, independent ownership; confidence: med (vendor primary).
- [Composio Docs](https://docs.composio.dev/) — fetched 2026-06-28 — supports: managed OAuth/API-key auth, tool-calling, Python/TypeScript SDKs, MCP + native modes, SaaS/API/SDK/self-hosted deployment, `user_id`-scoped credential model; confidence: high (vendor primary on product/deployment).
- Founding year (2023), HQ (San Francisco), founders' background, employee count, integration counts: corroborated via Tracxn/Crunchbase/Forbes India search results (aggregators; not separately cached) — confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023 (legal entity Sampark Inc.), HQ San Francisco, founders Soham Ganatra (CEO) & Karan Vaidya, $25M Series A led by Lightspeed (~July 2025) / ~$29M total, independent (no M&A). Documented managed-auth + tool-calling product, Python/TS SDKs, MCP support, SaaS/API/SDK/self-hosted deployment; positioned vs [arcade](arcade.md)/[stackone](stackone.md)/[descope](descope.md)/[stytch](stytch.md)/[workos](workos.md); framed as Day-2/low hedge-fund fit (builder infra, governance-light). Set status: researched, confidence medium. 3 sources cached.
