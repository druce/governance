---
type: vendor
name: Obot
slug: obot
categories: [mcp-gateway]
layer: model-prompt
aliases: [Obot AI, Acorn Labs, GPTScript]
website: "https://obot.ai"
founded: 2022
hq: Cupertino, California, USA
ownership: independent
ownership_detail: "Independent VC-backed startup; formerly Acorn Labs, rebranded to Obot AI 2025-09-23. No M&A."
ownership_confidence: high
funding_total: "$35M (seed)"
last_funding: "Seed, $35M, announced 2025-09-23 (co-led by Mayfield and Nexus Venture Partners)"
deployment: [self-hosted, saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [mcp, open-source, oauth, audit, agent-platform]
---

# Obot

> Researched 2026-06-28. Primary category: [mcp-gateway](../categories/mcp-gateway.md).

**One-liner** — An open-source MCP gateway and platform that puts a governed control plane between AI agents (Claude, Cursor, ChatGPT, internal bots) and the MCP servers they call, centralizing OAuth, per-tool access policy, a curated server catalog, and audit logging.

## What it does

Obot sits between AI clients and Model Context Protocol (MCP) servers — local, remote, or hosted — and brokers every connection. Rather than each developer wiring agents directly to MCP tools (with credentials scattered in client configs), Obot gives an organization a single entry point that:

- **Catalog / registry** — a curated, vetted list of approved MCP servers employees can discover and self-serve from, conforming to MCP registry specs. This is the "shadow MCP" antidote: instead of staff installing arbitrary community servers, IT publishes a trusted catalog.
- **Centralized OAuth & token brokering** — Obot handles OAuth 2.1 server-side and brokers tokens so downstream credentials are not exposed to the AI client. Identity comes from your IdP.
- **Per-user / per-group / per-tool access policy** — fine-grained RBAC over which users and agents can reach which servers and which individual tools, with predefined roles (Owner, Admin, Power User, Basic User, Auditor).
- **Audit logging** — every tool call recorded with user, agent, server, arguments, and outcome; real-time usage dashboards; compliance-ready trails.
- **Hosting & proxying** — it can also run/host MCP servers (Docker or Kubernetes, Node/Python/container) and proxy local, remote, and hosted servers behind one console.

The broader Obot project also ships an MCP-standards chat client ("Obot Chat") with RAG and memory, but the gateway is the piece relevant to governance.

## Where it sits in the stack

Primary category: [mcp-gateway](../categories/mcp-gateway.md) — the **model/prompt → tool-access** layer. Obot is infrastructure that governs how agents reach tools and data, not a content guardrail or DLP product.

Lethal-trifecta role: it touches two legs. By gating *which* MCP servers/tools an agent can invoke and brokering credentials, it constrains **egress** (what an agent can act on / exfiltrate to) and limits exposure to **untrusted input** from rogue or unvetted MCP servers (the curated catalog reduces supply-chain risk). It does not by itself inspect prompt/response content for sensitive-data leakage — pair it with a runtime guardrail / DLP layer for that.

Trust zones: it lives at the boundary between an internal agent (yellow zone) and external tools/SaaS (red zone), acting as the policy enforcement point on that boundary.

## Deployment & architecture

- **Open-source edition** — MIT-licensed, self-hosted on Kubernetes or Docker on your own infrastructure ("your data never leaves your environment").
- **Enterprise edition** — adds advanced IdP integrations (Okta, Microsoft Entra), SLAs, and vendor support.
- **Managed Cloud** — a dedicated, fully-hosted gateway option.

Integrations: identity via Google, GitHub, Okta, Auth0, JumpCloud, Microsoft Entra; MCP servers (local/remote/hosted); model providers including OpenAI and Anthropic (for the chat client); GitOps or UI for policy management; client connection URLs for Claude Desktop, Cursor, VSCode, and enterprise chat clients. A companion repo (`obot-platform/mcp-oauth-proxy`) implements the OAuth 2.1 proxy.

## Positioning & differentiators

Obot's pitch is "complete MCP platform" — not just a proxy but hosting + registry + gateway + client — with a strong open-source / self-host story (MIT, run it forever). Its credibility rests on the founding team's infrastructure pedigree (Rancher/SUSE, Cloud.com/Citrix), which signals it is built by people who ship enterprise platform software.

Nearest neighbors:
- [mintmcp](mintmcp.md) — the other half of the seed's "Obot / MintMCP" bundle; also an MCP gateway, more SaaS-leaning. Direct comparator.
- [docker-mcp-gateway](docker-mcp-gateway.md) — Docker's own gateway; strong on container packaging and the Docker MCP catalog, less on multi-user IdP governance.
- [ibm-contextforge](ibm-contextforge.md) — IBM's open-source MCP gateway/registry (ContextForge); enterprise-vendor-backed alternative with similar registry+gateway scope.
- [agentgateway](agentgateway.md) — data-plane / proxy-oriented gateway (often paired with service-mesh thinking).
- [arcade](arcade.md) — tool-calling / auth platform with a developer-SDK emphasis rather than admin control-plane.
- [pomerium](pomerium.md) — identity-aware access proxy extending into MCP; comes from the zero-trust access-proxy world.
- [natoma](natoma.md) — managed MCP gateway / identity-for-agents, more SaaS/governance-as-a-service positioning.

Obot differentiates on breadth (catalog + hosting + gateway + client in one MIT-licensed package) and self-host control; it is less of a fit if you want a pure managed SaaS you never operate.

## Ownership, funding & M&A

- **Independent, VC-backed.** Founded **2022** as **Acorn Labs** in **Cupertino, CA**; rebranded to **Obot AI** on **2025-09-23**. No acquisition (no seed M&A flag, and none found).
- **Funding:** **$35M seed**, announced **2025-09-23** alongside the rebrand ("Obot AI Secures $35M Seed to Build Enterprise MCP Gateway"), co-led by **Mayfield** and **Nexus Venture Partners**. (Some aggregators tie Acorn Labs funding to its 2022/2023 founding; the $35M is the publicly stated figure as of the 2025 rebrand — prior-round detail not fully confirmed.)
- **Founders / leadership:** Sheng Liang (CEO, co-founder), Darren Shepherd, Shannon Williams, Will Chan — the team behind **Rancher Labs** (acq. SUSE) and **Cloud.com** (acq. Citrix).
- **Product lineage:** earlier projects **GPTScript** (natural-language LLM scripting) and an earlier "Obot" agent platform evolved into today's Obot MCP Platform/Gateway. The pivot is from agent-building toward enterprise MCP governance.

Ownership confidence: **high** (independent startup, primary rebrand announcement dated). Funding-history confidence: medium (round amount and co-leads confirmed; full prior-round chronology not).

## CTO / hedge-fund lens

This is a **Day-2** capability. You only need an MCP gateway once agents are actually calling tools/MCP servers against real systems; before that it is premature. When that day comes, an MCP gateway is the natural choke point for governance — and for a regulated fund the appeal of Obot specifically is the **self-host, MIT-licensed** option: you can run the control plane inside your own environment so agent-to-tool traffic and credentials never leave, which matters for data-residency and audit posture. The audit log (per-tool-call, with arguments and outcomes) is the kind of artifact compliance and incident response want.

Caveats for a buyer: the company and product are **young** (gateway launched mid-2025, rebrand late 2025), the category itself is early and unsettled, and the enterprise IdP integrations you'd likely require (Okta/Entra) sit behind the paid Enterprise edition. For a small fund, running and operating a self-hosted Kubernetes control plane is real overhead — the Managed Cloud or a SaaS competitor may fit better. Treat as **medium fit**: architecturally well-aligned, but evaluate maturity, support, and operational burden before committing.

## Competitors / alternatives

[mintmcp](mintmcp.md), [docker-mcp-gateway](docker-mcp-gateway.md), [ibm-contextforge](ibm-contextforge.md), [agentgateway](agentgateway.md), [arcade](arcade.md), [pomerium](pomerium.md), [natoma](natoma.md)

## Open questions / to verify

- Exact funding chronology — was the $35M a single 2025 seed, or cumulative including an earlier Acorn Labs round? Aggregator data is inconsistent.
- Precise feature split between OSS and Enterprise editions (beyond IdP/SLA/support) — what governance features are paywalled.
- Production references / scale — any named enterprise deployments, and how mature the audit/RBAC features are in practice vs. roadmap.
- Whether Obot offers any content inspection (DLP/guardrail) or strictly access/identity governance.

## Sources

- [Obot MCP Gateway Platform](https://obot.ai/mcp-gateway-platform/) — fetched 2026-06-28 — supports: gateway features, IdP list, OSS/Enterprise/Managed tiers, RBAC roles, token brokering; confidence: med (vendor marketing).
- [GitHub: obot-platform/obot](https://github.com/obot-platform/obot) — fetched 2026-06-28 — supports: MIT license, platform scope (hosting/registry/gateway/chat), Docker/K8s deployment, OAuth 2.1; confidence: high.
- [Obot MCP Gateway launch coverage](https://www.helpnetsecurity.com/2025/08/15/obot-mcp-gateway-adoption-mcp-servers/) — fetched 2026-06-28 — supports: open-source positioning, creator Acorn Labs / CEO Sheng Liang, control-plane/catalog/audit features; confidence: high (independent trade press).
- [Acorn Labs is Now Obot AI](https://obot.ai/acorn-labs-is-now-obot-ai/) — fetched 2026-06-28 — supports: rename date 2025-09-23, $35M seed, founders, Cupertino HQ, GPTScript lineage; confidence: high (primary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Obot = open-source MIT-licensed MCP gateway/platform (catalog + OAuth + per-tool RBAC + audit) from Obot AI, formerly Acorn Labs (founded 2022, Cupertino), rebranded 2025-09-23 with a $35M seed co-led by Mayfield and Nexus; founders are the Rancher/Cloud.com team; lineage GPTScript → Obot. Kept primary category [mcp-gateway](../categories/mcp-gateway.md). Ownership high confidence (independent, no M&A); funding-history confidence medium. hedge_fund_fit set to medium (good self-host story, but young/OSS, IdP behind Enterprise tier). 4 sources cached.
