---
type: vendor
name: Descope
slug: descope
categories: [tool-identity-integration, non-human-identity]
layer: model-prompt
aliases: [Descope Agentic Identity Hub]
website: "https://www.descope.com"
founded: 2022
hq: Los Altos, California, USA
ownership: independent
ownership_detail: Venture-backed and independent as of 2026-06; no acquisition found. Founded by ex-Demisto team (Demisto itself acq. by Palo Alto Networks 2019, pre-Descope).
ownership_confidence: high
funding_total: $88M (seed + extension)
last_funding: Seed extension, +$35M, 2025-09-30 (existing investors); brings total to $88M
deployment: [saas, api, sdk]
target_customer: developers / B2B SaaS and enterprise app builders; security teams adopting agentic AI
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [ciam, authentication, passwordless, agentic-identity, mcp, non-human-identity, oauth]
---

# Descope

> A drag-and-drop customer-identity (CIAM) and authentication platform that has extended
> into issuing scoped, ephemeral identities to AI agents and MCP servers.

**One-liner** — Developer-first authentication/CIAM with visual auth flows that now doubles
as an "identity provider for AI agents," handing agents short-lived OAuth credentials to reach
tools and MCP servers.

**Categories** — [tool-identity-integration](../categories/tool-identity-integration.md) (primary), [non-human-identity](../categories/non-human-identity.md)

## What it does

Descope started as a **customer identity and access management (CIAM)** platform: a no-code/
low-code way for developers to build and run end-user authentication — passwordless, social
login, SSO, MFA, risk-based step-up — using a drag-and-drop flow builder ("identity journeys")
instead of hand-coding auth. The pitch is "descoping" authentication from the application
developer's daily work.

Since 2025 it has pushed hard into **agentic AI identity** via the **Agentic Identity Hub**
(2.0 announced 2026-01-26). The premise: human credentials (SSO/passwords) are too broad and
hard to revoke for an autonomous agent, and static service-account API keys can't do
contextual, least-privilege access. Descope issues agents their own **first-class identities**
with **ephemeral, scoped credentials**, lets users authorize an agent through OAuth consent
flows (so there's an auditable chain from an agent action back to the delegating human), and
acts as an **OAuth 2.1 / PKCE auth layer in front of MCP servers**. A built-in credential vault
stores OAuth tokens and API keys with 50+ prebuilt connection templates so an agent can reach
third-party SaaS tools; audit events stream to a SIEM.

## Where it sits in the stack

Primary category: [tool-identity-integration](../categories/tool-identity-integration.md) (the Tool Identity & Integration layer of the
model/prompt stack) — the layer that gives agents a managed way to authenticate to SaaS tools
and MCP servers. It also tags into [non-human-identity](../categories/non-human-identity.md) because it treats agents as managed
identities with their own scoped credentials and lifecycle.

Lethal-trifecta role: it primarily constrains the **egress / action** leg — by scoping and
shortening what an agent is allowed to reach and do (least-privilege per agent/tool/tenant/MCP
server, short-lived tokens, revocable consent), it limits how far a compromised or
prompt-injected agent can act. It does **not** inspect prompts (untrusted input) or scan data
content (sensitive data) — those legs need runtime/DLP tooling. It lives at the boundary
between the agent and the tools/zones it calls.

## Deployment & architecture

- **SaaS** control plane; integrate via **SDKs/APIs** (client and backend SDKs, plus the visual
  flow builder). No-code/low-code configuration.
- **Agent/MCP path:** OAuth 2.1 + PKCE, Dynamic Client Registration (DCR) and CIMD support to
  put protocol-compliant auth in front of internal and external **MCP servers**; per-agent
  tool-level scopes; native hooks for FastMCP, Vercel, and Reflex.
- **Bring Your Own Auth (BYOA):** layers on top of an existing IdP ([okta](okta.md), Microsoft Entra)
  rather than replacing it — Descope handles the MCP/agent-specific OAuth flows.
- **Credential vault** for outbound tokens/keys; **SIEM export** of audit events; multi-tenant
  gateway architectures.

## Positioning & differentiators

Descope's calling card is the **visual, developer-first** approach to auth, and a credible
**agentic-identity** story shipped early relative to incumbents. Versus nearest neighbors:

- [stytch](stytch.md) — the closest comparison: another developer-first auth/CIAM company that also moved
  into agent/MCP auth and "Connected Apps." Descope leans on its no-code flow builder; both
  target the same MCP-auth use case.
- [workos](workos.md) — developer auth aimed at making apps **enterprise-ready** (SSO/SCIM/directory
  sync); more B2B-enterprise-readiness, less drag-and-drop journey building.
- [okta](okta.md) — the incumbent workforce/customer IdP (Auth0 for developers). Bigger, broader, but
  heavier; Descope positions as lighter and as a layer that can sit on top of Okta for the
  agent/MCP piece.
- [aembit](aembit.md) — a pure **non-human / workload identity** play (secretless workload-to-workload
  access). Aembit comes at agent identity from the NHI/workload side; Descope comes at it from
  the CIAM/app-auth side. Overlap is the agent-to-tool credentialing problem.

Heritage is a differentiator buyers cite: the founding team built **Demisto** (SOAR; acquired by
Palo Alto Networks, became Cortex XSOAR), which lends security credibility.

## Ownership, funding & M&A

Independent, venture-backed. Founded **2022**; HQ **Los Altos, California**. Eight co-founders —
the four Demisto co-founders (Slavik Markovich, CEO; Rishi Bhargava; Dan Sarel, CPO; Guy Rinat)
plus Demisto's first four employees (Aviad Lichtenstadt, Doron Sharon, Meir Wahnon, Gilad
Shriki). Funding: launched from stealth in **Feb 2023 with a $53M seed** (led by Lightspeed and
GGV/Notable Capital, with Dell Technologies Capital, Unusual Ventures, Cerca Partners and
others — notably large for a seed), later **extended by $35M (announced 2025-09-30)** from
existing investors to a **$88M total**. **No acquisition found** — the seed registry carried no
M&A flag and research found none; ownership `independent`, confidence `high`. (Note: it is the
founders' *prior* company Demisto that Palo Alto Networks acquired in 2019 — that is not
Descope.)

## CTO / hedge-fund lens

This is mostly a **builder's tool**, so it is **Day-2 and niche** for a hedge-fund CTO. You only
need Descope if you are **building your own customer-facing app or internal agentic application**
and want to outsource the auth layer — or specifically if you are **standing up MCP servers /
agents** and need to put OAuth-based, least-privilege, revocable access in front of the tools
they call. For a fund that is mainly a **buyer** of AI assistants (ChatGPT/Claude Enterprise,
Copilot) and SaaS, identity needs are met by the workforce IdP ([okta](okta.md) / Microsoft Entra) and
this layer is not required. No direct SR 11-7 / model-risk relevance. If/when the fund's
engineers do build agents that take actions against internal systems, the agent-identity and
audit-trail capabilities become relevant — but evaluate it against the workforce-IdP's own
emerging agent features and against NHI specialists ([aembit](aembit.md)) before adding a new vendor.

## Competitors / alternatives

[stytch](stytch.md), [workos](workos.md), [okta](okta.md), [aembit](aembit.md), [cyberark](cyberark.md), [arcade](arcade.md), [composio](composio.md)

## Open questions / to verify

- Exact split of the $53M seed lead investors (sources name Lightspeed + GGV/Notable Capital;
  GGV rebranded to Notable Capital — confirm naming).
- Production maturity / reference customers for the Agentic Identity Hub (vs. the mature CIAM
  product) — much of the agentic messaging is recent (2025–2026).
- Pricing model and whether agent identities are priced separately from CIAM MAUs.
- Employee count / revenue scale (not found).

## Sources

- [Our company | Descope](https://www.descope.com/about) — fetched 2026-06-28 — supports: founded 2022, eight co-founders incl. Markovich/Sarel/Bhargava/Rinat, Demisto heritage, mission; confidence: high (vendor primary).
- [Descope Extends and Closes Seed Round With $88M Total Funding](https://www.descope.com/press-release/seed-funding-advisory-board) — fetched 2026-06-28 — supports: $88M total ($53M seed + $35M extension, 2025-09-30), HQ Los Altos CA, investors, CIAM+agent product scope, founders/roles; confidence: high (vendor primary).
- [Descope Unveils Agentic Identity Hub 2.0](https://www.descope.com/press-release/agentic-identity-hub-2.0) — fetched 2026-06-28 — supports: 2026-01-26 launch, MCP OAuth 2.1/PKCE/DCR, agents as first-class identities, delegated access/credential vault, SIEM export, SaaS deployment; confidence: high (vendor primary).
- [Identity provider for AI Agents and MCP Servers (use case)](https://www.descope.com/use-cases/ai) — fetched 2026-06-28 — supports: ephemeral credentials, delegated/least-privilege access, BYOA, layering on Okta/Entra, SDK/SaaS deployment, FastMCP/Vercel/Reflex integrations; confidence: med (vendor marketing).
- [Passwordless authentication startup Descope lands $53M seed (TechCrunch, 2023-02-15)](https://techcrunch.com/2023/02/15/passwordless-authentication-startup-descope-lands-whopping-53m-seed-round/) — not separately cached — supports: $53M seed, Feb-2023 launch from stealth, Demisto founders; confidence: high (trade press).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022, HQ Los Altos CA, eight ex-Demisto co-founders (Markovich CEO), $53M seed (Feb 2023) extended +$35M to $88M total (2025-09-30), independent/no M&A (confidence high). Documented CIAM/passwordless core + Agentic Identity Hub (MCP OAuth 2.1, ephemeral agent credentials, delegated access, credential vault, SIEM export). Positioned vs Stytch/WorkOS/Okta/Aembit. Set ownership_confidence high, page confidence medium, hedge_fund_fit low (builder's tool). Filled all frontmatter; 4 sources cached.
