---
title: MCP Gateway / Tool Access Control
type: category
name: MCP Gateway / Tool Access Control
slug: mcp-gateway
category: mcp-gateway
layer: model-prompt
survey_question: MCP Gateway / Tool Access Control
adoption_tier: day-2
trigger: agents call tools via MCP; the tool path needs a policy choke point
maturity_stage_required: null
category_maturity: nascent
adjacent: [authorization-engine, tool-identity-integration, ai-gateway, agent-runtime-security]
incumbent_coverage: []
vendor_count: 20
maps_to_seed_doc: MCP Gateway / Tool Access Control
maps_to_seed_csv: MCP / Agent Gateway & Tool Access (split)
last_verified: 2026-07-27
---

# MCP Gateway / Tool Access Control

## Business objective

An MCP gateway is the **single doorway for the tools an agent is allowed to reach**. As
agents adopt the Model Context Protocol (MCP) to call tools and external services, you
end up with many MCP servers and a sprawl of tool integrations; the gateway centralizes
them — allowlisting which servers/tools are sanctioned, brokering and authenticating the
connections, applying policy, and **logging every tool call for audit**. In the seed
doc's terms: "control, allowlist, broker, audit for the tools agents call — only
sanctioned MCP servers/tools get through."

If [ai-gateway](ai-gateway.md) is the single exit door for *model* traffic, the MCP gateway is the
single exit door for *tool* traffic. It's the chokepoint that turns "agents can call
whatever MCP server someone wired up" into a governed, observable set of actions.

## When you need it

Day-2 — needed **when agents start using tools**, especially third-party or
developer-installed MCP servers. A fund with chat-only assistants doesn't need it; a fund
where engineers and agents are spinning up MCP servers to reach internal and SaaS systems
does, because unmanaged MCP servers are an obvious prompt-injection and exfiltration
surface. The trigger is **MCP/tool sprawl** — when you can't enumerate which tools your
agents can invoke. Strongly paired with [trust-zone-segmentation](trust-zone-segmentation.md) and
[authorization-engine](authorization-engine.md).

## Agent-security role: the lethal trifecta

In agent security the core threat model is the lethal trifecta: untrusted input,
sensitive-data access, and external egress converging in one agent context — and the
tool path is where an injected instruction becomes a real action. The MCP gateway
attacks the **egress** leg most directly — it is the broker that decides
*which tools can be called at all*, so it can stop an injected instruction from reaching a
data-moving or Internet-facing tool. By allowlisting tool surfaces it also limits the
**untrusted-input** blast radius (fewer attacker-reachable tools). It belongs in the
**yellow/green zones**, sitting between agents and the systems they're permitted to touch.
It enforces; an [authorization-engine](authorization-engine.md) often supplies the per-call decision.

## Vendors

**Open-source / self-hosted gateways**
- [agentgateway](../vendors/agentgateway.md) — Solo.io's open-source agent/MCP gateway (kgateway lineage); data-plane for agent and tool traffic.
- [ibm-contextforge](../vendors/ibm-contextforge.md) — IBM's open-source MCP gateway/registry for cataloguing and brokering MCP servers.
- [docker-mcp-gateway](../vendors/docker-mcp-gateway.md) — Docker's gateway for running and gating containerized MCP servers.
- [obot](../vendors/obot.md) — open-source (MIT) MCP gateway and registry that has grown into a broader AI governance platform: LLM gateway, device-level audit and enforcement for local coding agents (Obot Sentry, beta), self-hosted Claude sessions (experimental). SSO connectors free up to 100 users since 2026-07-31. (refreshed 2026-10-20)
- [agentregistry](../vendors/agentregistry.md) — Solo.io's Apache-2.0 catalog of approved agents, MCP servers and skills; the paid Solo Enterprise edition adds OIDC sign-in, roles, an admin approval queue, runtime authorization enforced at agentgateway, and read-only discovery of agents in AgentCore, Foundry and Copilot Studio. CNCF Sandbox vote passed 2026-09-29, onboarding pending. Cross-listed to [ai-spm](ai-spm.md). (added 2026-10-20)
- [litellm](../vendors/litellm.md) — the open-source LiteLLM proxy's MCP Gateway: one fixed endpoint for all MCP tools, key/team/org access control and upstream OAuth 2.0 auth. Primary is [ai-gateway](ai-gateway.md). (added 2026-10-23)

**Commercial / managed gateways**
- [mintmcp](../vendors/mintmcp.md) — managed MCP gateway for enterprise tool access control.
- [arcade](../vendors/arcade.md) — tool-calling/agent platform with auth and a gateway for the tools agents invoke. Cross-listed to [tool-identity-integration](tool-identity-integration.md).
- [kong](../vendors/kong.md) — API-gateway vendor extending into MCP/agent tool ACLs. Cross-listed to [ai-gateway](ai-gateway.md).
- [truefoundry](../vendors/truefoundry.md) — MCP Gateway module of TrueFoundry's AI gateway platform, which since 2026 also includes an Agent Gateway and a managed agent harness (TrueForge). Cross-listed to [ai-gateway](ai-gateway.md).
- [gravitee](../vendors/gravitee.md) — API-management vendor whose MCP Proxy gates individual MCP methods (`tools/call`, `resources/read`) with OpenFGA-backed fine-grained authorization. Cross-listed to [ai-gateway](ai-gateway.md).
- [natoma](../vendors/natoma.md) — non-human-identity vendor offering MCP/agent gateway controls. Cross-listed to [non-human-identity](non-human-identity.md).
- [pomerium](../vendors/pomerium.md) — identity-aware proxy used to broker MCP/tool access. Cross-listed to [authorization-engine](authorization-engine.md).
- [prisma-airs](../vendors/prisma-airs.md) — Palo Alto's AI security platform includes an AI Agent Gateway. Cross-listed to [ai-runtime-security](ai-runtime-security.md) and [ai-spm](ai-spm.md).
- [runlayer](../vendors/runlayer.md) — MCP gateway turned "AI control plane": approved catalog of MCP servers/skills across AI clients, IdP-mapped permissions, tool-call scanning, shadow-AI discovery; SaaS or self-hosted. $42M raised; in trade-secret litigation with Rippling (filed 2026-07-28). The closest peer to mintmcp and natoma. (added 2026-10-16)
- [speakeasy](../vendors/speakeasy.md) — ex-SDK-generation vendor whose AGPL Gram platform became an MCP gateway: IdP-provisioned access, OAuth brokering, inline secret/PII detectors and agent hooks; cloud, self-hosted or air-gapped. Cross-listed to [tool-identity-integration](tool-identity-integration.md). (added 2026-10-16)
- [tetrate](../vendors/tetrate.md) — Agent Router Enterprise (the commercial build of the open-source Envoy AI Gateway, now Agent Router under AAIF) governs MCP alongside LLM traffic. Primary is [ai-gateway](ai-gateway.md). (added 2026-10-16)
- [docker-sandboxes](../vendors/docker-sandboxes.md) — Docker Sandboxes (`sbx`) has its own built-in MCP gateway (`sbx mcp`, since v0.38.0, 2026-08) with Cedar policy set through the paid Docker AI Governance; it governs only agents running inside Docker Sandboxes and is separate from the open-source [docker-mcp-gateway](../vendors/docker-mcp-gateway.md). Primary is [ephemeral-environments](ephemeral-environments.md). (added 2026-10-20)
- [portkey](../vendors/portkey.md) — Portkey MCP Gateway: central MCP server/tool registry, OAuth 2.1/JWT/IdP auth, RBAC, tool allowlisting and audited tool calls. Now branded "Prisma AIRS AI Gateway" after the Palo Alto Networks acquisition, so it overlaps the [prisma-airs](../vendors/prisma-airs.md) entry above. Primary is [ai-gateway](ai-gateway.md). (added 2026-10-23)
- [quilr](../vendors/quilr.md) — QuilrAI MCP Gateway (vendor marketing, 2026-10): sits in front of MCP servers, scopes each agent to a subset of tools, verifies identity on each call and logs tool calls. Primary is [ai-spm](ai-spm.md). (added 2026-10-23)

## Consolidation / M&A dynamics

No seed M&A flags specific to the gateways, but the **competitive squeeze is obvious**:
API-gateway incumbents (Kong), AI-platform vendors (TrueFoundry), identity vendors
(Natoma, Pomerium), and AI-security platforms (Prisma AIRS) are all adding MCP-gateway
features, against a base of fast-moving OSS projects (agentgateway, IBM ContextForge,
Docker, Obot). Expect MCP gateway to become a *feature* of adjacent platforms rather than
a durable standalone category for most buyers — a key thing to retest in research.

## Adjacent categories

- [authorization-engine](authorization-engine.md) — the decision engine the gateway calls to allow/deny a tool action; gateway = enforcement point, engine = decision point. Cerbos/Permit.io span both.
- [tool-identity-integration](tool-identity-integration.md) — provides the *managed identity and connectors* agents use to authenticate to tools; the gateway governs *which* tools. Arcade spans both.
- [ai-gateway](ai-gateway.md) — sibling chokepoint for model (LLM) traffic; same "single exit door" pattern, different traffic. Kong/TrueFoundry/Prisma do both.
- [agent-runtime-security](agent-runtime-security.md) — watches agent *behaviour*; the gateway controls *tool reachability*. Complementary.
- [non-human-identity](non-human-identity.md) — issues the agent/workload identities the gateway authenticates.

## Survey

**Question.** Which MCP gateway / tool-access-control products is your organization using
or evaluating to broker and govern the tools your agents can reach? *(Select all that
apply and indicate stage.)*

**Answer options.** Solo.io agentgateway · Kong MCP Gateway · TrueFoundry MCP Gateway ·
Arcade · IBM ContextForge · Docker MCP Gateway · Obot · MintMCP · Natoma · Pomerium ·
Prisma AIRS Agent Gateway · Gravitee MCP Proxy · Runlayer · Speakeasy Gram ·
Tetrate Agent Router · agentregistry (Solo.io) · Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- Very new and OSS-heavy — expect **low production adoption**, lots of "evaluating," and self-built solutions hiding in "Other."
- **Overlap risk is high:** the CSV asked MCP gateway, authorization engine, and tool identity as *one* question. Here they're split; respondents will still conflate them. A scope line ("the *doorway/allowlist* that brokers tool calls — not the auth engine or the connectors") helps. Cerbos/OPA/Permit.io/Oso belong on the [authorization-engine](authorization-engine.md) question; Composio/Descope/Stytch/WorkOS on [tool-identity-integration](tool-identity-integration.md).
- Kong, TrueFoundry, and Prisma AIRS also appear on the [ai-gateway](ai-gateway.md) question — same vendor, different door.
- **Two Docker options, two products (2026-10-20).** "Docker MCP Gateway" is the open-source Desktop/Engine gateway; Docker Sandboxes' built-in `sbx mcp` gateway is a separate, proprietary feature governed through Docker AI Governance (asked on the [agent-runtime-security](agent-runtime-security.md) question). Respondents will merge them; a parenthetical on the answer option helps.
- agentregistry is a *catalog*, not a proxy; its rules are enforced at agentgateway. Expect respondents using both to tick only agentgateway.

## Open taxonomy questions

- **This is the second of three rows the CSV bundled** into "MCP / Agent Gateway & Tool Access." Per Q1 in taxonomy-gaps.md we keep [mcp-gateway](mcp-gateway.md), [authorization-engine](authorization-engine.md), and [tool-identity-integration](tool-identity-integration.md) as three granular categories because they're distinct jobs — **gateway (broker/allowlist tools) vs engine (decide allow/deny) vs identity/connectors (authenticate to tools)** — while flagging that vendors frequently cover two of the three. Overlaps to expect: Cerbos & Permit.io (also authz), Pomerium (also authz), Arcade & Natoma (also tool-identity / NHI).
- Overlap with [ai-gateway](ai-gateway.md): as model and tool traffic converge, "agent gateway" may collapse the two. Whether MCP gateway stays separate from AI gateway is a candidate to revisit after research.
- The term "MCP gateway" is protocol-specific (MCP). If the agent-tooling ecosystem standardizes differently, the category may need a more neutral name ("agent tool gateway"). Flag for the final taxonomy pass.
