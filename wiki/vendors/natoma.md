---
type: vendor
name: Natoma
slug: natoma
categories: [non-human-identity, mcp-gateway]
layer: foundation
aliases: [Natoma Labs]
website: "https://natoma.ai"
founded: 2024
hq: San Francisco, California, USA
ownership: acquired
ownership_detail: "Snowflake announced intent to acquire (2026-05-27); deal subject to customary closing conditions, terms undisclosed; see sources"
ownership_confidence: high
funding_total: "$7M (seed)"
last_funding: "Seed, May 2025 (led by Index Ventures and Greylock)"
deployment: [saas, self-hosted, on-prem, api]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [mcp, ai-agents, non-human-identity, agentic]
---

# Natoma

> **One-liner** — An enterprise Model Context Protocol (MCP) governance gateway that gives AI agents identity-scoped, audited, policy-controlled access to enterprise tools and data — being acquired by Snowflake.

**Categories** — [non-human-identity](../categories/non-human-identity.md) (primary), [mcp-gateway](../categories/mcp-gateway.md)

## What it does
Natoma sits between AI clients/agents and the enterprise systems they want to call (SaaS apps, databases, APIs, cloud, on-prem). It standardizes those connections through MCP, then layers identity, authorization, credential management, and audit on top so an agent acts with scoped, governed permissions rather than a broad static key. Marketing positions it as the "control and governance fabric" for agent-to-tool connections: a verified MCP server library, role/intent-based tool bundles ("Profiles"), attribute-based authorization, managed-or-BYO credentials, full audit trails, and shadow-AI discovery.

## Where it sits in the stack
Foundation layer, at the intersection of [non-human-identity](../categories/non-human-identity.md) (governing the agent's identity and entitlements) and [mcp-gateway](../categories/mcp-gateway.md) (the runtime broker for MCP tool calls). Lethal-trifecta role: it primarily constrains the **egress / action** leg (what an agent is allowed to do and reach) and helps protect the **sensitive-data** leg by scoping tool/data access per identity and logging it. It does not itself inspect prompts for untrusted input — that's [ai-runtime-security](../categories/ai-runtime-security.md) territory.

## Deployment & architecture
Hybrid: cloud-hosted, VPC, on-premises, and desktop (for local tool access). Acts as a gateway/broker for MCP servers. Integrations called out: SIEM, EDR, MDM; identity-aware access controls; credential vaulting (managed or bring-your-own). SOC2 certified; GDPR/CCPA compliant per vendor.

## Positioning & differentiators
Natoma is an MCP-native entrant (founded 2024, as MCP itself was emerging) rather than a legacy NHI/secrets vendor extending into agents. Its pitch is governance *at the MCP layer* — a verified server registry plus identity-aware, attribute-based authorization on every tool call — which differentiates it from secrets-lifecycle players like [entro-security](entro-security.md) and [clutch-security](clutch-security.md) and from pure MCP brokers like [mintmcp](mintmcp.md), [obot](obot.md), or [arcade](arcade.md). Against [mcp-gateway](../categories/mcp-gateway.md) peers it leans harder on identity governance and shadow-AI discovery; against [non-human-identity](../categories/non-human-identity.md) peers it leans harder on the agent/MCP runtime.

## Ownership, funding & M&A
- **Independent funding:** $7M seed, May 2025, led by Index Ventures and Greylock. Founder/CEO Pratyus Patnaik (previously founded atSpoke, acquired by Okta in 2021; then senior director at Okta). Founding team drawn from Okta, Microsoft, Google, Salesforce.
- **M&A — confirmed:** On **2026-05-27** Snowflake announced a **definitive agreement to acquire Natoma** to provide secure connectivity for the "agentic enterprise"; Natoma's capabilities are slated to integrate with Snowflake Intelligence, Cortex Agents, and Cortex Code. Deal is subject to customary closing conditions; financial terms undisclosed; close date not stated. Confirmed against Snowflake's own press release (high confidence). Ownership set to `acquired` (was `independent` in the stub — corrected).

## CTO / hedge-fund lens
Day-2 for most funds: relevant once you are actually deploying internal AI agents that call live enterprise systems and you need per-agent entitlements and an audit trail rather than shared API keys. The Snowflake acquisition matters two ways: (1) if you are a Snowflake shop, this likely becomes a native governance feature rather than a separate buy; (2) if you are not, Natoma's roadmap and standalone availability now carry integration-uncertainty risk. No direct SR 11-7 / model-risk role, but the audit trail and access scoping support operational-risk and access-control evidence for agentic workflows.

## Competitors / alternatives
[mintmcp](mintmcp.md), [obot](obot.md), [arcade](arcade.md), [ibm-contextforge](ibm-contextforge.md), [pomerium](pomerium.md) (MCP gateways); [entro-security](entro-security.md), [clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md) (non-human / agent identity); [astrix-security](astrix-security.md).

## Open questions / to verify
- Deal close date and whether Natoma remains available standalone post-acquisition.
- Whether Natoma will continue selling to non-Snowflake customers.
- Hard numbers on customers/scale (only vendor-stated metrics found).

## Sources
- [Snowflake Announces Intent to Acquire Natoma](https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-natoma-providing-secure-connectivity-for-the-agentic-enterprise/) — fetched 2026-06-28 — supports: acquisition (2026-05-27), what Natoma does, founder; confidence: high
- [Natoma Platform](https://natoma.ai/platform) — fetched 2026-06-28 — supports: product/MCP features, deployment, integrations (vendor marketing); confidence: med
- Web search (Crunchbase, Index Ventures, press) — fetched 2026-06-28 — supports: founded 2024, HQ San Francisco, $7M seed May 2025 (Index/Greylock), CEO Pratyus Patnaik; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Snowflake acquisition (intent announced 2026-05-27, primary PR) — corrected ownership independent→acquired (high confidence); established founded 2024, HQ San Francisco, $7M seed (May 2025, Index/Greylock), CEO Pratyus Patnaik; MCP governance gateway / NHI positioning; hedge_fund_fit medium.
