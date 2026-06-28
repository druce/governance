---
title: Open Policy Agent (OPA)
type: vendor
name: Open Policy Agent (OPA)
slug: open-policy-agent
categories: [authorization-engine, policy-as-code]
layer: model-prompt
aliases: [OPA, Rego]
website: "https://www.openpolicyagent.org"
founded: 2016
hq: "CNCF project (originated at Styra, Redwood City, CA)"
ownership: independent
ownership_detail: "Open-source CNCF Graduated project (Apache-2.0). Created by Styra; donated to CNCF 2018. Core maintainers acqui-hired by Apple (2025-08); project remains under CNCF governance."
ownership_confidence: high
funding_total: n/a (open-source project, not a company)
last_funding: n/a
deployment: [self-hosted, sdk, on-prem]
target_customer: enterprise (platform/devops/security teams)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [authorization, pdp, open-source, cncf, policy-as-code, rego]
---

# Open Policy Agent (OPA)

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). Open-source **CNCF Graduated** project — not a company. Created by [styra](styra.md); core maintainers acqui-hired by Apple (Aug 2025), project stays under CNCF.

**One-liner** — The de-facto open-source, general-purpose policy engine: ship your access rules (written in **Rego**) to a decision point that any app, service, or agent can call for a fast allow/deny.

## What it does
OPA is a general-purpose **Policy Decision Point**. You express policy in **Rego**, a declarative language for querying complex hierarchical data (JSON), and OPA evaluates a decision given input + data. It started in cloud-native infra — Kubernetes admission control, microservice authz, CI/CD guardrails ([policy-as-code](../categories/policy-as-code.md)) — and the same engine is now pointed at **agent/tool authorization**: define in code what an agent or MCP tool is allowed to do and enforce it consistently. It is decision-only: it does not store relationship data or do content inspection.

## Where it sits in the stack
Dual-primary: [authorization-engine](../categories/authorization-engine.md) (per-request allow/deny) and [policy-as-code](../categories/policy-as-code.md) (infra/CI guardrails) — it is genuinely both. Layer: model-prompt. Lethal-trifecta role: constrains the **sensitive-data** and **egress** legs by deciding whether an action is permitted; it does **not** inspect prompts for injection (that's [ai-runtime-security](../categories/ai-runtime-security.md) / [agent-runtime-security](../categories/agent-runtime-security.md)). The center of gravity for externalized authz — many neighbors wrap or compete with it.

## Deployment & architecture
Self-hosted OSS (**Apache-2.0**); runs as a sidecar/daemon (REST API), an embedded Go library, or WebAssembly. Stateless evaluation — you push policy bundles and supply input/data; pairs with your IdP and data sources rather than replacing them. Widely embedded in K8s (Gatekeeper), service meshes, API gateways, and increasingly MCP/agent gateways that call OPA for decisions.

## Positioning & differentiators
The **OSS standard PDP** — broadest adoption, largest ecosystem, most general-purpose. Rego is powerful but has a learning curve, which is exactly the gap commercial neighbors sell against: [styra](styra.md) (enterprise management of OPA), [permit-io](permit-io.md) (developer-friendly hosted layer over OPA/Cedar), [cerbos](cerbos.md) (simpler YAML policies), [oso](oso.md) (Polar DSL), [authzed](authzed.md) (Zanzibar/ReBAC graph). If you want vendor-neutral, embeddable, ubiquitous authz, OPA is the default; if you want managed tooling on top, you buy one of the others.

## Ownership, funding & M&A
**Not a company** — an open-source project created at **[styra](styra.md)** (Tim Hinrichs, Torin Sandall, Teemu Koponen) ~2016, donated to **CNCF** (accepted 2018, Incubating 2019, **Graduated 2021-01-29**). **Aug 2025: Apple acqui-hired the three OPA creators plus several Styra engineers** (see [styra](styra.md)). Crucially, OPA stays under **CNCF governance** — license, governance, and release cadence unchanged — so the project itself is insulated, though some observers note Apple-acqui-hire precedent (FoundationDB) as a watch item. Confidence high.

## CTO / hedge-fund lens
Day-2, but often **already owned**: if your platform/devops team does Kubernetes admission control or policy-as-code, OPA is probably in production already, so "adopting" it for agent authz can be re-use rather than a new buy. SR 11-7 angle is indirect (consistent, auditable access decisions support control documentation). Best fit for shops with engineering depth willing to write Rego; smaller funds may prefer a managed layer ([permit-io](permit-io.md), [cerbos](cerbos.md) Cloud, [oso](oso.md) Cloud).

## Competitors / alternatives
[styra](styra.md) (commercial OPA), [cerbos](cerbos.md), [permit-io](permit-io.md), [oso](oso.md), [authzed](authzed.md), [hashicorp-sentinel](hashicorp-sentinel.md), [kyverno](kyverno.md) (infra-policy neighbors).

## Open questions / to verify
- Long-term health of OPA development under CNCF now that core maintainers are inside Apple — watch release cadence and maintainer diversity through 2026.
- Status of formerly-Styra enterprise tooling (Enterprise OPA/EOPA, Regal linter) reportedly moving to OSS.

## Sources
- [Open Policy Agent (OPA) — CNCF project page](https://www.cncf.io/projects/open-policy-agent-opa/) — fetched 2026-06-28 — supports: CNCF graduated dates, general-purpose policy engine, Rego; confidence: high
- [OPA maintainers join Apple; OSS community to maintain Styra products (Oso blog)](https://www.osohq.com/post/opa-maintainers-join-apple-oss-community-to-maintain-styra-products) — fetched 2026-06-28 — supports: Apple acqui-hire of OPA creators Aug 2025, CNCF retains OPA, Styra commercial future uncertain; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed CNCF Graduated project (created by Styra, donated 2018, graduated 2021). Documented **Apple acqui-hire of OPA core maintainers (Aug 2025)** with OPA remaining under CNCF. Raised ownership_confidence to high; corrected ownership_detail. Cross-linked [styra](styra.md).
