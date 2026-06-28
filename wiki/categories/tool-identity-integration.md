---
type: category
name: Tool Identity & Integration
slug: tool-identity-integration
layer: model-prompt
priority: day-2
trifecta_role: sensitive-data, egress (manages agent identity/credentials to tools; the universal adapter, not content inspection)
maps_to_seed_doc: Tool Identity & Integration Layer
maps_to_seed_csv: MCP / Agent Gateway & Tool Access (split)
vendor_count: 7
status: drafted
last_updated: 2026-06-28
---

# Tool Identity & Integration

## Business objective

This layer is the **universal adapter that lets agents reach SaaS tools securely** —
managed authentication plus prebuilt connectors, so agents call Salesforce, GitHub,
Google Workspace, Slack, etc. without every team hand-rolling OAuth flows and stashing
tokens. In the seed doc's words: "managed auth and prebuilt connectors so agents reach
SaaS tools without hand-built OAuth." It solves two coupled problems: **integration**
(the connector catalog and the glue code) and **identity** (how the agent authenticates —
on its own behalf or delegated on a user's behalf — and where the credentials live).

The distinction from neighbours: an [mcp-gateway](mcp-gateway.md) governs *which* tools an agent may
reach and audits the calls; this layer provides *the credentialed connection itself* — the
managed OAuth, token vaulting, and connector that actually makes the call work.

## When you need it

Day-2 — needed **when agents integrate with SaaS systems**, i.e. once your agents do real
work against external apps rather than just chat or read internal docs. The trigger is
**connector and credential sprawl**: hand-built OAuth per integration, long-lived tokens
in code, no central view of which agent can act in which SaaS app as whom. Buy or adopt
this to avoid a pile of bespoke, poorly-secured integrations. For a small fund it may
arrive bundled with the agent platform; standalone adoption signals a real agent program.

## Lethal-trifecta role

This layer governs the **sensitive-data** and **egress** legs by controlling *how an agent
authenticates to the systems holding data and the paths out*. Done well — short-lived,
scoped, per-user-delegated credentials, vaulted not hardcoded — it shrinks what a
compromised or injected agent can reach and do. Done badly (broad, long-lived tokens) it
*widens* the trifecta. It does not inspect prompt content. It supports the
[trust-zone-segmentation](trust-zone-segmentation.md) design by making agent→tool access least-privilege and
revocable. Lives in yellow/green zones alongside the gateway.

## Vendors

**Agent integration / connector platforms**
- [composio](../vendors/composio.md) — managed tool-calling/integration layer with a large connector catalog and auth handling for agents.
- [stackone](../vendors/stackone.md) — unified API / connector platform for agents to reach SaaS systems.
- [arcade](../vendors/arcade.md) — tool-calling platform with built-in auth for agents; spans connectors and gateway. Cross-listed to [mcp-gateway](mcp-gateway.md).

**Agent / non-human auth (identity for tool access)**
- [descope](../vendors/descope.md) — auth platform with agent/non-human identity and delegated tool access. Cross-listed to [non-human-identity](non-human-identity.md).
- [stytch](../vendors/stytch.md) — auth/identity platform offering agent and connected-app auth. Cross-listed to [non-human-identity](non-human-identity.md).
- [workos](../vendors/workos.md) — enterprise auth/SSO and connector platform extending to agent auth. Cross-listed to [identity-access](identity-access.md).
- [cyberark](../vendors/cyberark.md) — secrets/PAM and machine-identity heritage applied to agent-to-tool credentials. Cross-listed to [non-human-identity](non-human-identity.md), [secrets-management](secrets-management.md), [identity-governance](identity-governance.md).

## Consolidation / M&A dynamics

Per seed flag (**unverified — to confirm in research**): CyberArk acq. by Palo Alto — an
identity/secrets incumbent moving into the agent-credential space. Otherwise this is an
emerging mix of agent-integration startups (Composio, StackOne, Arcade) and auth/identity
platforms (Descope, Stytch, WorkOS) repositioning toward "identity for agents." Expect
overlap pressure from both [non-human-identity](non-human-identity.md) (issuing agent identity) and
[mcp-gateway](mcp-gateway.md) (brokering tool access) — this layer sits between them and could be
absorbed by either as the stack matures.

## Adjacent categories

- [mcp-gateway](mcp-gateway.md) — governs *which* tools agents reach and audits calls; this layer supplies the *credentialed connection*. Arcade spans both; complementary chokepoints.
- [non-human-identity](non-human-identity.md) — the broader discipline of identity for workloads/agents; tool-identity is the *tool-facing* slice (auth + connectors). Descope, Stytch, CyberArk span both.
- [authorization-engine](authorization-engine.md) — decides *what* an authenticated agent may do; this layer establishes *who the agent is* to the tool.
- [secrets-management](secrets-management.md) — vaults the credentials this layer issues/uses for agent→tool auth.
- [identity-access](identity-access.md) — the human/agent front door (IdP/SSO) that delegated agent auth builds on.

## Survey

**Question.** Which tool-identity / agent-integration products is your organization using
or evaluating to give agents managed, secure access to SaaS tools? *(Select all that
apply and indicate stage.)*

**Answer options.** Composio · StackOne · Arcade · Descope · Stytch · WorkOS · CyberArk ·
Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- Mixed bag of two sub-jobs — **connectors/integration** (Composio, StackOne, Arcade) vs **agent auth/identity** (Descope, Stytch, WorkOS, CyberArk). Respondents may only recognize the half that matches their problem; consider splitting into two sub-questions if responses are noisy.
- **Overlap risk:** Arcade also appears under [mcp-gateway](mcp-gateway.md); Descope, Stytch, and CyberArk also appear under [non-human-identity](non-human-identity.md). CyberArk in particular spans several categories and may be selected for its PAM/secrets role rather than agent integration.
- This was part of the same bundled CSV question as [mcp-gateway](mcp-gateway.md) and [authorization-engine](authorization-engine.md) — keep scope tight ("managed auth + connectors for agent→SaaS," not the gateway or the policy engine).

## Open taxonomy questions

- **This is the third of three rows the CSV bundled** into "MCP / Agent Gateway & Tool Access." Per Q1 in taxonomy-gaps.md we keep [mcp-gateway](mcp-gateway.md), [authorization-engine](authorization-engine.md), and [tool-identity-integration](tool-identity-integration.md) split because they are distinct jobs — **gateway (broker/allowlist tools) vs engine (allow/deny decision) vs identity & connectors (authenticate agents to tools)** — while accepting that several vendors cover two of three. Overlaps flagged here: Arcade (also mcp-gateway), Descope/Stytch/CyberArk (also non-human-identity).
- **Boundary with [non-human-identity](non-human-identity.md) is genuinely fuzzy:** "identity for agents" is claimed by both. The cut used here is *tool-facing* (auth + connectors to SaaS for action) vs the broader NHI discipline (issuing/governing workload & agent identities org-wide). Candidate to merge or re-slice after research.
- The category mixes a connector/integration play and an auth play under one name; the final taxonomy pass should decide whether "Tool Integration" and "Agent/Tool Identity" deserve to separate.
