---
type: vendor
name: StackOne
slug: stackone
categories: [tool-identity-integration]
layer: model-prompt
aliases: [StackOne Technologies]
website: "https://www.stackone.com"
founded: 2023
hq: London, UK (registered office Newbury, Berkshire; team across Europe and US)
ownership: independent
ownership_detail: Venture-backed, independent as of 2026-06. $24M raised; no acquisition found.
ownership_confidence: high
funding_total: ~$24M (vendor-stated)
last_funding: Series A, $20M, 2025-05-06 (led by GV/Google Ventures)
deployment: [saas, api, sdk]
target_customer: B2B SaaS vendors and enterprises building/deploying AI agents (HR/ATS/CRM/LMS-heavy)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [tool-identity-integration, unified-api, agent-tooling, mcp, saas-connectors]
---

# StackOne

> A managed integration layer that gives AI agents real-time, authenticated access to enterprise
> SaaS (HR, ATS, CRM, LMS) through one set of connectors and tool-calls — so an agent can read and
> act across a customer's stack without you hand-building each integration.

**One-liner** — Unified-API / agent-tooling infrastructure: one interface that turns hundreds of
SaaS apps into authenticated, governed tool-calls an AI agent can invoke.

**Categories** — [tool-identity-integration](../categories/tool-identity-integration.md)

## What it does

StackOne is an integration platform aimed at AI-agent builders and B2B SaaS vendors. Instead of a
team writing and maintaining a separate integration for every customer system, StackOne exposes a
large library of pre-built connectors (vendor-stated 400+ connectors and 25,000+ "actions" as of
mid-2026; the May-2025 Series A release cited ~200 connectors / 10,000+ actions, so the numbers are
growing fast) behind a single interface. Those actions are surfaced to agents and apps via MCP, SDKs,
CLI, and REST/API, with managed authentication and permissions handled by StackOne rather than the
agent developer.

The angle that distinguishes it from a classic "unified API" (one normalized schema across, say, all
HRIS systems) is its push toward **agent tool-calling**: StackOne markets a proprietary tool-calling
LLM / AI agent that builds use-cases on top of complex native APIs and exposes each app's *native*
actions (not just a lowest-common-denominator unified model), plus a builder to extend or tune
connectors. It also claims execution optimizations to reduce token spend and security features such
as prompt-injection detection — these last claims are vendor marketing and unverified here.

## Where it sits in the stack

Primary category: [tool-identity-integration](../categories/tool-identity-integration.md) (AI model/prompt layer; the "Tool Identity &
Integration" row). This is the plumbing that lets an agent actually *do things* in enterprise SaaS —
the managed agent→SaaS connector + auth layer that sits between an agent framework and the outside
world.

In lethal-trifecta terms StackOne lives on the **egress / external-action** leg and the
**sensitive-data** leg: it is precisely the conduit by which an agent reaches out to third-party
systems and pulls or writes sensitive records (employee data, candidate records, CRM/customer data).
That makes it a trust-boundary chokepoint — useful as a place to enforce scoping and auth, but also a
component that, if compromised or over-permissioned, *is* the data-exfiltration path. Its
prompt-injection-detection marketing nods at the **untrusted-input** leg, but StackOne is integration
infrastructure, not a dedicated guardrail/runtime-security product; do not treat it as one.

## Deployment & architecture

- **Managed SaaS / API** — StackOne hosts the connectors and the OAuth/credential vault; the
  developer integrates via API and an embedded auth/permissions hub that end-customers use to connect
  their own SaaS accounts.
- **Agent surfaces** — actions are exposed to agents via **MCP**, SDKs, CLI, and REST, so they drop
  into common agent frameworks and AI clients as callable tools.
- **Connector builder** — a UI/AI builder to create, extend, or tune connectors and expose native
  per-app actions rather than only normalized unified-API objects.
- **Compliance posture** — vendor claims SOC 2 / HIPAA / GDPR alignment (unverified here).
- Domain coverage skews to people/operational SaaS: HRIS, ATS, CRM, LMS, plus a long tail.

## Positioning & differentiators

StackOne's pitch is "integration infrastructure for the AI-agent era": it competes both with legacy
unified-API players (Merge, Finch, Apideck) and with the newer agent-tooling/auth crowd. Versus
nearest neighbors:

- [composio](composio.md) — the closest comparable: a tool-calling/integration layer that gives agents
  authenticated access to hundreds of apps. Both chase the "managed tools + auth for agents" slot;
  StackOne leans into enterprise unified-API depth (HR/ATS/CRM) and its own tool-calling model.
- [arcade](arcade.md) — overlaps on agent tool-calling and auth, but Arcade is more developer/runtime and
  MCP-gateway flavored (it's cross-listed under [mcp-gateway](../categories/mcp-gateway.md)); StackOne emphasizes breadth of
  managed enterprise SaaS connectors.
- [workos](workos.md) — adjacent but different job: WorkOS is auth/enterprise-readiness (SSO/SCIM/directory
  sync) infrastructure; it secures the *identity* front door, whereas StackOne provides the *action/
  data* connectors. They can be complementary rather than substitutes.

What StackOne is known for: large managed connector/action catalog, native (not just unified) actions,
a proprietary tool-calling LLM, and MCP-native delivery. Differentiation claims (accuracy of its
tool-calling model, token optimization, prompt-injection detection) are vendor marketing.

## Ownership, funding & M&A

Independent and venture-backed. Founded **2023** by **Romain Sestier** (Co-Founder & CEO) and
**Guillaume Lebedel** (Co-Founder & CTO); HQ London (UK registered office in Newbury, Berkshire), team
distributed across Europe and the US. Funding: a **$20M Series A on 2025-05-06 led by GV (Google
Ventures)**, with Workday Ventures, XTX Ventures, and existing investors Episode 1 and Playfair, plus
angels associated with OpenAI, DeepMind, Microsoft and MuleSoft; an earlier seed round (reported ~€3.3M
/ ~$3.6M, led by Episode 1) brings **vendor-stated total funding to ~$24M**. **No acquisition found** —
the seed registry carried no M&A flag and nothing in research indicates one; ownership set to
`independent` with `high` confidence on the independent status (funding figures are vendor/press, not
filings). The seed-round figure was not re-fetched from a primary source here (the EU-Startups article
returned 403); only the $20M Series A and $24M total are corroborated by vendor + Tech.eu.

## CTO / hedge-fund lens

This is a **build-side / developer-infrastructure** product, not a security control a fund buys off the
shelf. It is **Day-2 (or N/A)** for most asset managers. You would care about StackOne only if you are
**building your own AI agents that need to act across many third-party SaaS systems** and want to avoid
hand-rolling and maintaining those integrations. For a hedge fund, the relevant SaaS estate (HRIS/ATS/
LMS) is rarely where agentic automation creates edge, and most funds will consume agents through
[enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) platforms rather than wiring custom tool-calling into back-office SaaS — so
**hedge_fund_fit: low**.

If you *do* adopt it, treat it as a high-privilege trust boundary: it holds OAuth tokens to your SaaS
and is on the data-egress/action path. Governance questions (least-privilege scoping per agent, audit
logging, where credentials are vaulted, data residency, and its SOC 2 posture) matter more than the
feature list. It has no direct SR 11-7 / model-risk role; it is plumbing, and the model-risk
obligations sit with whatever agent/model uses it.

## Competitors / alternatives

[composio](composio.md), [arcade](arcade.md), [workos](workos.md), plus legacy unified-API vendors (Merge, Finch, Apideck — no
pages) and MCP-gateway/tool-access players ([mcp-gateway](../categories/mcp-gateway.md) category: [mintmcp](mintmcp.md), [obot](obot.md),
[natoma](natoma.md)). For agent identity/auth specifically, see [descope](descope.md) and [stytch](stytch.md).

## Open questions / to verify

- Primary-source confirmation of the seed round amount/date/lead (EU-Startups fetch was blocked).
- Whether the SOC 2 / HIPAA / GDPR and prompt-injection-detection claims are independently verifiable.
- How credentials/tokens are stored and whether self-hosted/on-prem deployment is offered (appears
  managed-SaaS-only).
- Current revenue/customer scale and headcount.
- Exact split of "unified" vs "native" actions and how authorization scoping is enforced per agent.

## Sources

- [StackOne raises $20m Series A led by GV (press release)](https://www.stackone.com/press-releases/stackone-raises-20m-series-a-led-by-gv-google-ventures-to-reinvent-saas-and-ai-agent-integrations) — fetched 2026-06-28 — supports: $20M Series A 2025-05-06, lead GV + investor list, $24M total, founders, HQ London, connector/action counts, tool-calling LLM; confidence: high (vendor primary on funding).
- [StackOne — Company / About](https://www.stackone.com/company/) — fetched 2026-06-28 — supports: founded 2023, founders/roles, registered office Newbury, current connector/action counts, HRIS/ATS/CRM/LMS focus, MCP delivery, SOC2/HIPAA/GDPR + prompt-injection claims, investor list; confidence: med (vendor marketing).
- [StackOne raises $20M for easier API integration (Tech.eu)](https://tech.eu/2025/05/06/stackone-raises-20m-for-easier-api-integration-led-by-big-tech-backers/) — fetched 2026-06-28 — supports: independent corroboration of $20M Series A, investors, $24M total, HQ London, product/problem framing; confidence: high (trade press).
- Seed round (~€3.3M, Episode 1, Mar 2024): EU-Startups (fetch returned 403; not cached) — confidence: low/med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023, HQ London (registered Newbury), founders Romain Sestier (CEO) & Guillaume Lebedel (CTO), $20M Series A (2025-05-06, led by GV) / ~$24M total, independent (no M&A). Documented managed-SaaS unified-API + agent tool-calling (MCP/SDK/API) product, HR/ATS/CRM/LMS connector focus; positioned vs [composio](composio.md), [arcade](arcade.md), [workos](workos.md); placed on egress/sensitive-data trifecta legs. Set hedge_fund_fit low (build-side infra), status: researched, confidence medium. 3 sources cached.
