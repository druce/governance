---
type: vendor
name: Pomerium
slug: pomerium
categories: [mcp-gateway, authorization-engine]
layer: model-prompt
aliases: [Pomerium Inc]
website: https://www.pomerium.com
founded: 2019
hq: California, US
ownership: independent
ownership_detail: "Pomerium, Inc. — independent, VC-backed; open-source core + commercial Enterprise edition. Series A $13.75M led by Benchmark (2024-06-20)."
ownership_confidence: high
funding_total: "~$18M (as of 2024-06)"
last_funding: "Series A — $13.75M — 2024-06-20 (Benchmark lead; Bain Capital, Haystack, SNR)"
deployment: [self-hosted, inline-proxy, saas]
target_customer: enterprise / regulated (also startups via OSS)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ztna, identity-aware-proxy, reverse-proxy, mcp, zero-trust, open-source]
---

# Pomerium

> Open-source identity- and context-aware reverse proxy (ZTNA). An established
> zero-trust access proxy that re-checks every request against policy using
> identity + context, now extended to broker and authorize access to **MCP** servers.

**Categories** — [mcp-gateway](../categories/mcp-gateway.md), [authorization-engine](../categories/authorization-engine.md)

## One-liner
A self-hosted reverse proxy that puts continuous, per-request authorization in
front of any app, API, or MCP server — no VPN, every request re-evaluated against
identity and context.

## What it does
Pomerium sits inline in the network path. Instead of a client connecting directly
to a protected service, traffic flows through Pomerium, which authenticates the
caller against your IdP (OIDC/SSO) and then evaluates **every request** against
policy — not just at login. Policies can key off user/role, group, device posture,
IP/geo, time of day, and request path, replacing static, connection-level VPN trust
with continuous per-request authorization. This is the classic "identity-aware
proxy" / ZTNA pattern (BeyondCorp-style), and it has been Pomerium's core product
since 2019.

The newer angle is **MCP**: Pomerium can sit between AI agents (MCP clients) and
MCP servers, proxying all MCP traffic and enforcing policy on it. Its notable claim
here is **tool-level authorization** — policy can allow or deny specific MCP tools
/ methods (e.g. permit `search`/`fetch`, deny `customer.delete`), not just allow or
block the whole endpoint. It validates external OAuth tokens and mints short-lived,
scoped JWTs injected into headers (reducing token sprawl), and logs each MCP call
with agent identity, tool, method, and the authorization decision. Per Pomerium,
you don't modify MCP clients or servers — you point them through the proxy — and it
stays MCP-spec compliant.

## Where it sits in the stack
Primary fit is [mcp-gateway](../categories/mcp-gateway.md) (the inline broker/PEP for agent-to-tool traffic)
and [authorization-engine](../categories/authorization-engine.md) (the per-request policy decision point). Layer:
`model-prompt` / runtime control plane. Note the **dual identity**: Pomerium is
first and foremost a general ZTNA/identity-aware access proxy for human and service
access to internal apps; MCP authorization is a recent, additive use of the same
proxy + policy engine, not a ground-up agent product.

Lethal-trifecta role: it controls **egress** (what an agent/tool can reach, and
which tool calls are permitted) and helps gate **untrusted-input** paths by forcing
all agent↔tool traffic through an authenticated, policy-checked chokepoint with
clean attribution. It lives at the boundary between a trusted zone (internal
tools/data) and less-trusted callers (agents, remote users).

## Deployment & architecture
- **Inline reverse proxy**, self-hosted (open-source core) or run with the
  commercial **Pomerium Enterprise** console/managed control plane. Terminates TLS,
  performs authN/authZ at session establishment, then proxies approved traffic at
  wire speed; supports WebSockets and HTTP/2 streaming (relevant for MCP transports).
- **Policy**: YAML-based route configuration combining identity conditions with
  per-route authorization; MCP controls expressed as route policy (e.g.
  `mcp_tool: { in: ["search","fetch"] }`). This is Pomerium's own policy model — not
  Rego — though it occupies the same PDP/PEP role as [open-policy-agent](open-policy-agent.md).
- **IdP integration**: OIDC/SSO with Okta, Azure AD / Entra, Google Workspace, etc.;
  agents inherit user-level identity for attribution.
- **Logging**: per-request decision logs with identity, tool/method, and allow/deny
  reason — useful for audit.

## Positioning & differentiators
Pomerium's pitch for MCP is "you already need a zero-trust proxy; extend the one you
trust to agents." That contrasts with **purpose-built MCP gateways** designed agent-
first — [agentgateway](agentgateway.md), [obot](obot.md), [mintmcp](mintmcp.md), [docker-mcp-gateway](docker-mcp-gateway.md),
[ibm-contextforge](ibm-contextforge.md), [arcade](arcade.md) — which start from the MCP/agent use case rather
than retrofitting a mature ZTNA product. Strengths Pomerium brings: a battle-tested
inline proxy (years in production, ~1B Docker pulls claimed by 2023), real continuous
authorization, and a single policy plane spanning humans, services, and agents.
Tradeoff: it is a network/infra proxy first, so agent-specific niceties (MCP server
catalogs, tool discovery UX, prompt-layer inspection) may be thinner than in
dedicated tools, and its YAML policy model is its own rather than a standard like Rego.

As a pure policy engine it overlaps with [open-policy-agent](open-policy-agent.md), [cerbos](cerbos.md), and
[permit-io](permit-io.md), but those are decision libraries/services you embed; Pomerium is an
inline enforcement proxy that bundles the decision point with the data path.

## Ownership, funding & M&A
- **Independent**, VC-backed. Pomerium, Inc. founded **2019** by **Bobby DeSimone**
  (CEO). HQ in **California** (exact city not firmly confirmed — sources list both
  Solana Beach, CA and Beaverton, OR; treat city as unverified).
- **Series A: $13.75M**, announced **2024-06-20**, led by **Benchmark**, with Bain
  Capital, Haystack, and SNR. **Total raised ~$18M** as of that date (one aggregator
  lists ~$17.5M; minor discrepancy, non-blocking).
- **Open-source core** (Apache-style OSS proxy) plus commercial **Pomerium
  Enterprise** edition. No M&A; no acquisition flag.

## CTO / hedge-fund lens
**Day-2.** This is infrastructure you adopt when you have internal apps/MCP servers
to expose to people or agents and want one continuous-authorization chokepoint
rather than VPN-level trust. The strongest case: **a shop that already runs (or is
considering) Pomerium for ZTNA can extend the same proxy and policy plane to MCP
tool access**, getting per-request, tool-level control and audit without standing up
a separate agent gateway. For a fund with no existing Pomerium footprint and only a
light MCP need, a purpose-built MCP gateway or a SaaS option may be faster to stand
up. Self-hosting means you own the deployment and HA. Open-source core lowers
procurement friction and allows code review — a plus for security-conscious,
regulated buyers; Enterprise edition adds the managed console and support.

## Competitors / alternatives
- MCP gateways: [agentgateway](agentgateway.md), [obot](obot.md), [mintmcp](mintmcp.md), [docker-mcp-gateway](docker-mcp-gateway.md),
  [ibm-contextforge](ibm-contextforge.md), [arcade](arcade.md)
- Policy/authorization engines: [open-policy-agent](open-policy-agent.md), [cerbos](cerbos.md), [permit-io](permit-io.md)

## Open questions / to verify
- Exact HQ city (Solana Beach, CA vs Beaverton, OR — aggregators disagree).
- Precise total funding (~$18M per SecurityWeek vs ~$17.5M per aggregators).
- Maturity / GA status of the MCP authorization features vs. roadmap (much of the
  MCP material is vendor blog content; depth of production MCP deployments unclear).
- Whether tool-level MCP policy inspects payloads/arguments or only tool/method names.
- OSS license specifics and the OSS-vs-Enterprise feature split for MCP features.

## Sources
- [Pomerium — homepage](https://www.pomerium.com/) — fetched 2026-06-28 — supports: identity- and context-aware access proxy positioning; confidence: high
- [Secure Access for MCP (Pomerium blog)](https://www.pomerium.com/blog/secure-access-for-mcp) — fetched 2026-06-28 — supports: per-request authz, tool-level MCP authorization, OIDC/IdP, JWT minting, reverse-proxy deployment; confidence: medium (vendor blog)
- [About — Pomerium](https://www.pomerium.com/about/) — fetched 2026-06-28 — supports: founded 2019, founder, OSS + commercial model, scale claims; confidence: high
- [Access Management Startup Pomerium Raises $13.75 Million (SecurityWeek)](https://www.securityweek.com/access-management-startup-pomerium-raises-13-75-million/) — fetched 2026-06-28 — supports: Series A $13.75M 2024-06-20, Benchmark lead, ~$18M total, founder Bobby DeSimone, CA HQ; confidence: high
- [github.com/pomerium/pomerium](https://github.com/pomerium/pomerium) — fetched 2026-06-28 — supports: "identity and context-aware access proxy", open-source core; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed company (founded 2019, Bobby DeSimone, CA), Series A $13.75M led by Benchmark 2024-06-20 (~$18M total), open-source ZTNA identity-aware proxy with newer inline MCP authorization (per-request + tool-level policy via YAML, OIDC IdP). Ownership confidence high; HQ city and exact total funding flagged as minor open items.
