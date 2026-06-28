---
title: Styra
type: vendor
name: Styra
slug: styra
categories: [authorization-engine, policy-as-code]
layer: model-prompt
aliases: [Styra DAS, Declarative Authorization Service, Enterprise OPA]
website: "https://www.styra.com"
founded: 2015
hq: Redwood City, CA, USA
ownership: acquired
ownership_detail: "Acqui-hire: Apple hired Styra's core OPA maintainers (Tim Hinrichs, Torin Sandall, Teemu Koponen) + several engineers (announced ~2025-08-20). NOT a clean corporate acquisition; Styra commercial products (DAS) reported wound down / being open-sourced. OPA stays under CNCF."
ownership_confidence: medium
funding_total: ~$54M
last_funding: "Series B $40M (2021-05, Battery Ventures)"
deployment: [saas, self-hosted, on-prem]
target_customer: enterprise (platform/security teams)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [authorization, policy-as-code, opa, acqui-hire, apple]
---

# Styra

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). The **commercial company behind [open-policy-agent](open-policy-agent.md)**. **Apple acqui-hired its OPA core team (~Aug 2025)**; commercial future uncertain.

**One-liner** — The company that created Open Policy Agent and sold enterprise management on top of it (Styra DAS / Enterprise OPA) — until Apple hired away its core team in 2025.

## What it does
Styra built and open-sourced [open-policy-agent](open-policy-agent.md), then commercialized it. **Styra DAS** (Declarative Authorization Service) was the enterprise control plane for authoring, distributing, testing, and monitoring Rego policy across fleets of OPA agents at scale; **Enterprise OPA (EOPA)** was a hardened OPA distribution. The job: give large organizations the management, governance, and support that raw OPA leaves to you.

## Where it sits in the stack
Dual: [authorization-engine](../categories/authorization-engine.md) and [policy-as-code](../categories/policy-as-code.md) — Styra is the managed/enterprise layer over OPA in both. Layer: model-prompt. Lethal-trifecta role: same as OPA — constrains **sensitive-data** and **egress** by deciding whether actions are permitted; not content inspection. OPA's gravity (via Styra and [policy-as-code](../categories/policy-as-code.md)) has been the center of mass for externalized authz.

## Deployment & architecture
SaaS control plane (Styra DAS) managing self-hosted OPA/EOPA agents (sidecars/daemons); on-prem options. Integrates with K8s, service meshes, CI/CD, IdP. After the 2025 acqui-hire, active development of the commercial offerings is in question — evaluate current product status directly before relying on it.

## Positioning & differentiators
Styra's differentiator was **being the source** of OPA plus enterprise-grade policy lifecycle tooling — versus [permit-io](permit-io.md) (developer-first hosted authz over OPA/Cedar), [cerbos](cerbos.md) (simpler stateless engine), [oso](oso.md) (Polar), [authzed](authzed.md) (Zanzibar/ReBAC). That moat eroded when the founding team left for Apple. The OSS project ([open-policy-agent](open-policy-agent.md)) is unaffected and continues under CNCF.

## Ownership, funding & M&A
Founded **2015** (Redwood City, CA); created OPA and donated it to CNCF (2018). Funding ~**$54M**: Series A **$14M** (Accel) and Series B **$40M** (**2021-05**, Battery Ventures, with CapitalOne Ventures, Citi Ventures, Accel, Unusual, A.Capital).

**M&A — acqui-hire, not a clean acquisition.** Around **2025-08-20**, **Apple hired Styra's core OPA maintainers (Hinrichs, Sandall, Koponen) and several engineers.** Reporting is consistent that this was an **acqui-hire** — Apple did *not* announce buying the Styra corporate entity — and that Styra's commercial products (DAS) face an uncertain roadmap / are being open-sourced, while OPA stays under CNCF. I mark `ownership: acquired` to flag the material change but keep **confidence medium** because the corporate-entity status (still operating? wound down? assets sold?) is not cleanly documented in a primary Apple/Styra release.

> Contradiction (soft): sources variously frame this as "Apple acquires the developer of OPA" (heise, Cloud Native Now) vs "acqui-hire, Styra corp not acquired" (Oso, HN). Reconciled as an **acqui-hire of the team** with the commercial entity's future unclear. Status: noted 2026-06-28, non-blocking.

## CTO / hedge-fund lens
Day-2 and now **low fit** as a *new* purchase: with the core team gone and the commercial roadmap uncertain, a fund standing up agent/policy authz today should default to [open-policy-agent](open-policy-agent.md) directly (CNCF-stewarded, unaffected) or a managed alternative ([permit-io](permit-io.md), [cerbos](cerbos.md) Cloud, [oso](oso.md)). Existing Styra DAS customers should treat this as a vendor-risk event and plan a migration path.

## Competitors / alternatives
[open-policy-agent](open-policy-agent.md) (the project it stewarded), [permit-io](permit-io.md), [cerbos](cerbos.md), [oso](oso.md), [authzed](authzed.md), [hashicorp-sentinel](hashicorp-sentinel.md).

## Open questions / to verify
- **Corporate status of Styra Inc. post-Apple** — still operating, wound down, or assets transferred? No primary release found.
- Fate of Styra DAS / Enterprise OPA / Regal — confirmed OSS path vs end-of-life and timelines.
- Whether Apple makes any product (vs pure talent) commitments.

## Sources
- [OPA maintainers join Apple; OSS community to maintain Styra products (Oso blog)](https://www.osohq.com/post/opa-maintainers-join-apple-oss-community-to-maintain-styra-products) — fetched 2026-06-28 — supports: Apple acqui-hire ~Aug 2025, named maintainers, Styra DAS uncertain future, OPA stays CNCF; corroborated by Cloud Native Now and heise; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed founder/creator of OPA, 2015 founding, Redwood City, ~$54M (Series B $40M 2021). Documented **Apple acqui-hire of core team (~2025-08)**; set ownership=acquired (confidence medium) with soft-contradiction note on framing. Cross-linked [open-policy-agent](open-policy-agent.md).
