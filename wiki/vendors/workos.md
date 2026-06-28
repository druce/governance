---
type: vendor
name: WorkOS
slug: workos
categories: [tool-identity-integration, identity-access]
layer: model-prompt
aliases: [AuthKit]
website: https://workos.com
founded: 2019
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Venture-backed, independent as of 2026-06. $100M Series C (2026-03-02) at $2B valuation, led by Meritech and Sapphire. Itself an acquirer — bought Warrant (FGA) on/around 2024-04-23.
ownership_confidence: high
funding_total: ~$180M (cumulative across Series A/B/C; ~$100M raised pre-Series-C plus $100M Series C — see note)
last_funding: Series C, $100M, 2026-03-02 (led by Meritech & Sapphire; $2B valuation)
deployment: [api, saas, sdk]
target_customer: software vendors / SaaS & AI app builders (developer platform); indie to enterprise
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [tool-identity-integration, identity-access, agent-identity, mcp, oauth, authorization, developer-platform]
---

# WorkOS

> Developer APIs that make a SaaS or AI app "enterprise-ready" (SSO/SAML, SCIM directory sync,
> RBAC, audit logs, fine-grained authorization) — and, increasingly, the auth layer for AI agents
> and MCP servers.

**One-liner** — A developer platform of drop-in APIs for enterprise auth features (SSO, SCIM,
RBAC, audit logs, fine-grained authorization), now extended to give AI agents their own scoped
identities and to secure MCP servers.

**Categories** — [[tool-identity-integration]], [[identity-access]]

## What it does

WorkOS sells "enterprise readiness as an API." When a software company needs to land enterprise
customers, those customers demand SAML SSO, SCIM directory sync (auto-provisioning/deprovisioning
from Okta/Entra), role-based access control, an admin portal for IT, and exportable audit logs.
Building all of that in-house takes months; WorkOS provides it as APIs/SDKs you wire into your own
app in days. Its **AuthKit** product is a hosted authentication/user-management layer (a CIAM
front door) that competitors position against Auth0. The broader suite includes Enterprise SSO,
Directory Sync, Admin Portal, Audit Logs, MFA, RBAC, Fine-Grained Authorization (FGA), plus newer
pieces (Radar abuse detection, Vault encryption, Pipes integrations).

The reason it appears in this wiki is its **agent/MCP** push: WorkOS now markets giving AI agents
their **own** credentials and identities (not a borrowed user session), issuing short-lived scoped
tokens, and acting as a spec-compatible OAuth 2.1 authorization server for **MCP servers** so an
agent can only call the specific tools its permissions map to.

## Where it sits in the stack

Primary category: [[tool-identity-integration]] (Model/Prompt layer) — the "managed agent→app
connectors + agent auth" slot — with a secondary tag of [[identity-access]] because the core
business is the identity/SSO front door for applications. Note: WorkOS is fundamentally a
**developer/builder** tool (you embed it in the app *you* ship), not a control a CTO buys to govern
their own employees' AI use.

Lethal-trifecta role: its agent-auth/FGA work is about constraining what an agent can *do and
reach* — scoped, revocable tokens and tool-level authorization limit the **egress**/action leg
(an over-permissioned or compromised agent can't act beyond its granted tools). It does not inspect
prompts (untrusted-input) or classify/redact sensitive data, so it is not a runtime firewall or DLP.
Trust-zone relevance: it helps enforce least privilege at the boundary between an agent and the
tools/SaaS it calls.

## Deployment & architecture

- **API / SDK developer platform** — REST APIs and SDKs you integrate into your own application;
  hosted by WorkOS (SaaS). No inline proxy, no agent on employee endpoints.
- **AuthKit** — hosted auth/user-management UI + flows (CIAM), authorization-code + PKCE.
- **Agent identity** — user-authorized agents get a separate scoped token via auth-code-with-PKCE;
  background/M2M agents use OAuth 2.1 Client Credentials (revocable per-agent without touching user
  sessions); tokens short-lived (minutes–hours).
- **MCP auth** — AuthKit as a spec-compatible OAuth 2.1 authorization server (metadata discovery,
  Dynamic Client Registration, PKCE, JWT validation, RBAC). Alternatively **Connect** runs as
  middleware in front of an existing IdP, handling only the MCP OAuth flows (no migration).
- **FGA** — Zanzibar-style (Google relationship-based) fine-grained authorization for tool-level
  scoping.
- Integrations: standard IdPs (Okta, Entra, etc.) on the SSO/SCIM side; MCP clients on the agent side.

## Positioning & differentiators

WorkOS's brand is "Stripe for enterprise features" — clean developer experience, fast integration,
usage-based/transparent pricing, and a roster of marquee AI customers (OpenAI, Anthropic, xAI,
Cursor, Perplexity, Vercel, Replit per its Series C post; vendor claim). Its differentiator versus
neighbors is breadth across **authn + authz + auditability** in one developer platform, and an early,
aggressive move into agent/MCP auth.

Versus nearest neighbors:
- [[stytch]] and [[descope]] — also developer-first auth platforms that have pivoted hard into agent
  identity / MCP auth; the three are the closest comparison set in this category. Stytch leans into
  device/fraud and "Connected Apps"; Descope is a no-code/drag-and-drop auth flow builder.
- [[okta]] (and Auth0, which Okta owns) — the incumbent IdP/CIAM giant WorkOS/AuthKit displaces for
  startups; Okta is an employee/workforce IdP and a buyer-side control, whereas WorkOS is something
  you embed in the product you sell.
- [[composio]] — comes at agent→SaaS connectivity from the **integration/tool-catalog** side
  (managed connectors + auth to hundreds of SaaS APIs) rather than from the identity-provider side.
  WorkOS gives you the authorization-server primitives; Composio gives you the pre-built tool
  connectors.

## Ownership, funding & M&A

Independent, venture-backed. Founded **2019** by **Michael Grinich** (CEO; previously founded Nylas),
HQ **San Francisco**. Funding: $15M Series A (2021-03), $80M Series B (2022-06, led by Greenoaks),
and a **$100M Series C on 2026-03-02 led by Meritech and Sapphire at a $2B valuation** (unicorn;
vendor + press confirmed). Cumulative funding is ~$180M (≈$95–100M pre-Series-C reported as "~$100M
total" by mid-2022 coverage, plus the $100M Series C); treat the exact total as approximate — not
reconciled against a single primary cap-table doc.

WorkOS-as-**acquirer**: it acquired **Warrant**, a Fine-Grained Authorization (Zanzibar-model) service
for developers, on/around **2024-04-23** (confirmed via WorkOS's own announcement, its X post, and
press; terms undisclosed). Warrant became WorkOS FGA. (The brief's aside about Stytch/AuthKit is a
misnomer — AuthKit is WorkOS's own product, not an acquisition; no acquisition of Stytch by WorkOS
exists.) No indication WorkOS itself has been acquired — it is independent.

## CTO / hedge-fund lens

**Low direct fit / Day-2 (mostly N/A as a buy).** WorkOS is a tool you adopt if **you are building
software** — embedding enterprise auth into an internal or customer-facing app your fund ships. It is
not a control you deploy to govern employees' AI usage, and it has no SR 11-7 / model-risk angle. A
hedge-fund CTO would encounter WorkOS primarily as (a) infrastructure inside SaaS/AI vendors they buy
(many of their AI tools likely run on it), or (b) a build-side choice if an in-house dev team is
standing up an internal agentic app and wants ready-made SSO + agent/MCP authorization rather than
rolling their own. For governing *consumed* AI, the relevant controls live in other categories
([[ai-access-governance]], [[ai-runtime-security]], [[mcp-gateway]], [[authorization-engine]]).
Where it does matter: if your team builds agents, WorkOS (or [[stytch]]/[[descope]]) gives agents
scoped, revocable, least-privilege credentials — a genuinely useful pattern for the agent **egress**
leg.

## Competitors / alternatives

[[stytch]], [[descope]], [[okta]], [[composio]], [[arcade]], [[cyberark]] (agent/non-human identity
from the enterprise security side), [[permit-io]] / [[authzed]] (FGA/authorization-engine
alternatives to WorkOS FGA).

## Open questions / to verify

- Exact cumulative funding total (Series A/B/C reconciliation against a primary source).
- Whether agent-identity/MCP features are GA and in production at scale, or still early/marketing-led.
- Warrant deal terms (undisclosed).
- Any buyer-side (vs builder-side) packaging that would change its relevance to a CTO governing
  employee AI use.

## Sources

- [WorkOS raises $100M Series C, hits $2B valuation](https://workos.com/blog/series-c) — fetched 2026-06-28 — supports: $100M Series C 2026-03-02, $2B valuation, Meritech/Sapphire lead, founder Grinich, product list, AI customer logos; confidence: high (vendor primary on funding).
- [WorkOS acquires Warrant (Daring Fireball link; orig. workos.com/blog/workos-acquires-warrant 404 on fetch)](https://daringfireball.net/linked/2024/04/28/workos) — fetched 2026-06-28 — supports: WorkOS acquired Warrant FGA ~2024-04-23, Zanzibar model; confidence: high (corroborated by WorkOS X post).
- [Secure auth for MCP servers (WorkOS)](https://workos.com/mcp) — fetched 2026-06-28 — supports: OAuth 2.1 authorization server for MCP, AuthKit/Connect, tool-level FGA scoping, deployment; confidence: med (vendor marketing).
- [Give your AI agents their own credentials (WorkOS)](https://workos.com/blog/ai-agent-credentials) — fetched 2026-06-28 — supports: agents as first-class principals, scoped/revocable tokens, M2M client credentials, short-lived tokens; confidence: med (vendor).
- Founded year (2019), HQ (San Francisco), Series A/B history: WebSearch synthesis of Crunchbase/Contrary Research/press (not separately cached) — confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2019 (Michael Grinich, ex-Nylas), HQ San Francisco, independent venture-backed, $100M Series C 2026-03-02 at $2B valuation (Meritech/Sapphire), ~$180M cumulative. Confirmed WorkOS-as-acquirer of Warrant (FGA/Zanzibar) ~2024-04-23. Documented developer-platform (API/SDK) model, AuthKit, and the agent-identity/MCP OAuth-2.1 angle (scoped revocable agent tokens, tool-level FGA). Positioned vs [[stytch]], [[descope]], [[okta]], [[composio]]. Set hedge_fund_fit low (builder-side tool, not a buyer-side AI-governance control), status researched, confidence medium. Fixed frontmatter (was independent/low → independent/high with detail). 4 sources cached.
