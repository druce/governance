---
type: category
name: MCP Gateway / Tool Access Control
slug: mcp-gateway
layer: model-prompt
priority: day-2
trifecta_role: untrusted-input, egress (single broker/allowlist for the tools agents can reach); yellow/green zone
maps_to_seed_doc: MCP Gateway / Tool Access Control
maps_to_seed_csv: MCP / Agent Gateway & Tool Access (split)
vendor_count: 11
status: drafted
last_updated: 2026-06-28
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

## Lethal-trifecta role

The MCP gateway attacks the **egress** leg most directly — it is the broker that decides
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
- [obot](../vendors/obot.md) — open-source MCP gateway / agent platform.

**Commercial / managed gateways**
- [mintmcp](../vendors/mintmcp.md) — managed MCP gateway for enterprise tool access control.
- [arcade](../vendors/arcade.md) — tool-calling/agent platform with auth and a gateway for the tools agents invoke. Cross-listed to [tool-identity-integration](tool-identity-integration.md).
- [kong](../vendors/kong.md) — API-gateway vendor extending into MCP/agent tool ACLs. Cross-listed to [ai-gateway](ai-gateway.md).
- [truefoundry](../vendors/truefoundry.md) — AI platform with an MCP gateway alongside its AI gateway. Cross-listed to [ai-gateway](ai-gateway.md).
- [natoma](../vendors/natoma.md) — non-human-identity vendor offering MCP/agent gateway controls. Cross-listed to [non-human-identity](non-human-identity.md).
- [pomerium](../vendors/pomerium.md) — identity-aware proxy used to broker MCP/tool access. Cross-listed to [authorization-engine](authorization-engine.md).
- [prisma-airs](../vendors/prisma-airs.md) — Palo Alto's AI security platform includes an AI Agent Gateway. Cross-listed to [ai-runtime-security](ai-runtime-security.md) and [ai-spm](ai-spm.md).

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
Prisma AIRS Agent Gateway · Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- Very new and OSS-heavy — expect **low production adoption**, lots of "evaluating," and self-built solutions hiding in "Other."
- **Overlap risk is high:** the CSV asked MCP gateway, authorization engine, and tool identity as *one* question. Here they're split; respondents will still conflate them. A scope line ("the *doorway/allowlist* that brokers tool calls — not the auth engine or the connectors") helps. Cerbos/OPA/Styra/Permit.io/Oso belong on the [authorization-engine](authorization-engine.md) question; Composio/Descope/Stytch/WorkOS on [tool-identity-integration](tool-identity-integration.md).
- Kong, TrueFoundry, and Prisma AIRS also appear on the [ai-gateway](ai-gateway.md) question — same vendor, different door.

## Open taxonomy questions

- **This is the second of three rows the CSV bundled** into "MCP / Agent Gateway & Tool Access." Per Q1 in taxonomy-gaps.md we keep [mcp-gateway](mcp-gateway.md), [authorization-engine](authorization-engine.md), and [tool-identity-integration](tool-identity-integration.md) as three granular categories because they're distinct jobs — **gateway (broker/allowlist tools) vs engine (decide allow/deny) vs identity/connectors (authenticate to tools)** — while flagging that vendors frequently cover two of the three. Overlaps to expect: Cerbos & Permit.io (also authz), Pomerium (also authz), Arcade & Natoma (also tool-identity / NHI).
- Overlap with [ai-gateway](ai-gateway.md): as model and tool traffic converge, "agent gateway" may collapse the two. Whether MCP gateway stays separate from AI gateway is a candidate to revisit after research.
- The term "MCP gateway" is protocol-specific (MCP). If the agent-tooling ecosystem standardizes differently, the category may need a more neutral name ("agent tool gateway"). Flag for the final taxonomy pass.
