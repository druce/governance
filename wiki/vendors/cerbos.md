---
type: vendor
name: Cerbos
slug: cerbos
categories: [authorization-engine, mcp-gateway]
layer: model-prompt
aliases: [Cerbos PDP, Cerbos Hub, Cerbos Cloud]
website: "https://www.cerbos.dev"
founded: 2021
hq: London, UK (remote-first)
ownership: independent
ownership_detail: "VC-backed; ~$11M raised (seed $3.5M 2021 Crane; extended seed $7.5M Mar 2023, OMERS Ventures)"
ownership_confidence: high
funding_total: ~$11M
last_funding: "Extended seed $7.5M (2023-03, OMERS Ventures)"
deployment: [self-hosted, saas, sdk]
target_customer: enterprise / mid-market (developer-led)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [authorization, pdp, open-source, rbac, abac, policy-as-code]
---

# Cerbos

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). Independent, VC-backed (seed-stage).

**One-liner** — Open-source, stateless authorization layer (a Policy Decision Point) that answers "can this principal do this action on this resource?" so you stop hard-coding permissions into every app and agent.

## What it does
Cerbos decouples authorization logic from application code. You write access policies (human-readable YAML, with conditions) for roles and resources; the **Cerbos PDP** evaluates them and returns allow/deny over an API. Because it is **stateless** it scales horizontally and runs close to the workload (sidecar, container, or embedded). **Cerbos Hub** is the managed control plane for distributing, testing, and observing policies; **Cerbos Cloud** is the hosted offering. For agentic AI the pitch is the same engine pointed at agent/tool calls — decide per request whether an agent acting for a given user may take an action.

## Where it sits in the stack
Primary [authorization-engine](../categories/authorization-engine.md) (the externalized PDP), cross-listed to [mcp-gateway](../categories/mcp-gateway.md) because Cerbos markets itself as the authz decision point an MCP/tool layer can call. Layer: model-prompt. Lethal-trifecta role: constrains the **sensitive-data** and **egress** legs — it can deny the read or the action per request — but it does **not** inspect prompt content for injection (that's [ai-runtime-security](../categories/ai-runtime-security.md) / [agent-runtime-security](../categories/agent-runtime-security.md)). A building block of [trust-zone-segmentation](../categories/trust-zone-segmentation.md); lives in yellow/green zones wherever decisions are made.

## Deployment & architecture
Self-hosted OSS (Apache-2.0) as a sidecar/microservice exposing REST/gRPC; **Cerbos Lite** compiles policies to WebAssembly for on-device/edge; **Cerbos Hub/Cloud** for managed policy distribution and audit. Stateless by design — no database; identity/attributes are passed in by the caller (so it pairs with your IdP, not replaces it). Audit logs for regulated industries. SDKs across major languages.

## Positioning & differentiators
Known for being **lightweight, stateless, and developer-friendly** with human-readable policies, versus [open-policy-agent](open-policy-agent.md)'s more general-purpose Rego, [oso](oso.md)'s Polar DSL, or [authzed](authzed.md)'s Zanzibar/ReBAC graph database. Cerbos does not store relationship data itself (unlike SpiceDB) — it evaluates policy against attributes you supply, which keeps it simple but pushes data-fetching to you. Closest neighbors: [permit-io](permit-io.md) (also hosted, developer-first), [oso](oso.md), [open-policy-agent](open-policy-agent.md).

## Ownership, funding & M&A
Founded **2021** by Emre Baran (CEO) and Charith Ellawala (CTO); HQ **London**, remote-first. Raised **~$11M**: a **$3.5M** seed (2021, Crane) and a **$7.5M** extended seed (**2023-03**, led by OMERS Ventures) with angels including a Brevan Howard Digital CTO. **No M&A** — independent (no seed flag). Confidence high.

## CTO / hedge-fund lens
Day-2. You reach for an externalized engine like Cerbos when agents (or microservices) must make **fine-grained, per-action, identity-aware** decisions at scale and you want one auditable place for them. For a fund running a single read-only assistant, the underlying app's permissions usually suffice; Cerbos earns its place once agents *act* across systems on behalf of different users. Lighter-weight and easier to adopt than standing up OPA+Styra; SaaS option lowers ops burden. Open-source core means low lock-in.

## Competitors / alternatives
[open-policy-agent](open-policy-agent.md), [styra](styra.md), [permit-io](permit-io.md), [oso](oso.md), [authzed](authzed.md), [pomerium](pomerium.md).

## Open questions / to verify
- Current total funding / any Series A since 2023 (sources show seed-stage only as of fetch).
- Real-world adoption for *agent* authz vs traditional app authz (usage stats are vendor marketing).

## Sources
- [Cerbos Closes $7.5 Million in Seed Funding (GlobeNewswire)](https://www.globenewswire.com/news-release/2023/04/12/2645616/0/en/Cerbos-Supercharges-the-Ability-to-Manage-and-Enforce-Authorization-Policies-at-Limitless-Scale-Closes-7-5-Million-in-Seed-Funding.html) — fetched 2026-06-28 — supports: founders, 2021 founding, London HQ, $11M raised, stateless PDP, Cerbos Cloud, deployment; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2021 founding, London HQ, founders (Baran/Ellawala), ~$11M seed-stage funding (OMERS-led 2023), stateless OSS PDP positioning. No M&A — independent. Confidence high.
