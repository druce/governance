---
type: vendor
name: Permit.io
slug: permit-io
categories: [authorization-engine, mcp-gateway]
layer: model-prompt
aliases: [Permit, Authorizon, OPAL]
website: "https://www.permit.io"
founded: 2021
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: "VC-backed; ~$14M raised (Series A $8M, 2024-02, Scale Venture Partners)"
ownership_confidence: high
funding_total: ~$14M
last_funding: "Series A $8M (2024-02, Scale Venture Partners)"
deployment: [saas, self-hosted, sdk, api]
target_customer: mid-market / enterprise (developer-led)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [authorization, pdp, authorization-as-a-service, opal, agent-authz, mcp]
---

# Permit.io

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). Independent, VC-backed (Series A).

**One-liner** — Developer-first authorization-as-a-service: a hosted policy decision point plus SDKs and a no-code policy editor, so engineers add fine-grained access control (RBAC/ReBAC/ABAC) without building it from scratch — increasingly aimed at AI agents and MCP.

## What it does
Permit.io wraps proven open-source engines ([open-policy-agent](open-policy-agent.md) / OPA and AWS **Cedar**) behind a managed control plane and SDKs. You model roles, resources, and relationships in a UI or as code; Permit distributes policy to PDPs you run or it hosts, and your app/agent calls a simple `permit.check()` for allow/deny. It also maintains **OPAL** (Open Policy Administration Layer), its open-source project for real-time policy/data sync to OPA. Newer products (Approval Flows, agent authorization) target **AI bots and agents** asking for fine-grained, identity-aware tool access.

## Where it sits in the stack
Primary [authorization-engine](../categories/authorization-engine.md); cross-listed to [mcp-gateway](../categories/mcp-gateway.md) because it pitches agent/MCP tool-access authorization. Layer: model-prompt. Lethal-trifecta role: constrains **sensitive-data** and **egress** by deciding whether an agent's action is permitted per request; not prompt-content inspection (that's [ai-runtime-security](../categories/ai-runtime-security.md) / [agent-runtime-security](../categories/agent-runtime-security.md)). Building block of [trust-zone-segmentation](../categories/trust-zone-segmentation.md); yellow/green zones.

## Deployment & architecture
Hybrid: Permit hosts the control plane (policy authoring, audit) while the **PDP can run locally** (sidecar/container) so authorization decisions and sensitive data stay in your environment — useful for regulated shops. SDKs across major languages; REST API for policy management. Built on OPA/Cedar + OPAL. Integrates with existing auth/IdP (it authorizes, it doesn't authenticate).

## Positioning & differentiators
Known for **developer experience and speed-to-implement** — no-code editor plus code, and "don't write your own authz." Versus [open-policy-agent](open-policy-agent.md) (raw engine, write your own Rego), [styra](styra.md) (enterprise OPA management), [cerbos](cerbos.md) (stateless OSS engine, also hosted), [oso](oso.md) (Polar DSL), [authzed](authzed.md) (Zanzibar/ReBAC graph). Permit's hedge is engine-agnostic (OPA *and* Cedar) with a managed wrapper; its agent/MCP messaging is early but active.

## Ownership, funding & M&A
Founded **2021** (originally "Authorizon") by **Or Weis** (CEO) and **Asaf Cohen**; HQ **Tel Aviv**. Raised **~$14M**: ~$6M early round then **Series A $8M** (**2024-02**, led by Scale Venture Partners, with NFX, Firestreak, Roosh, Verissimo). **No M&A** — independent (no seed flag). Confidence high.

## CTO / hedge-fund lens
Day-2. Good fit when you want externalized, fine-grained agent/tool authz **without** standing up and operating OPA+Styra yourself — the local-PDP model keeps decisions and data in-house, which matters for a fund. Lower engineering lift than raw OPA; more opinionated than Cerbos. Diligence the maturity of the agent/MCP features (newer than the core authz product) before betting an agent program on them. Series-A vendor — weigh vendor-risk for a core control.

## Competitors / alternatives
[open-policy-agent](open-policy-agent.md), [styra](styra.md), [cerbos](cerbos.md), [oso](oso.md), [authzed](authzed.md), [pomerium](pomerium.md).

## Open questions / to verify
- Maturity/production references for the **agent / MCP authorization** features specifically (vs core app authz).
- Any funding since the 2024 Series A.

## Sources
- [Permit.io Raises $8 Million for Authorization Platform (SecurityWeek)](https://www.securityweek.com/permit-io-raises-8-million-for-authorization-platform/) — fetched 2026-06-28 — supports: Series A $8M 2024-02 Scale VP, ~$14M total, Tel Aviv, founders, full-stack authz, agent/AI support; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2021 founding (ex-Authorizon), Tel Aviv HQ, founders (Weis/Cohen), ~$14M funding (Series A $8M 2024 Scale VP), OPA/Cedar + OPAL architecture, agent/MCP positioning. No M&A — independent. Confidence high.
