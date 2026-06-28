---
type: vendor
name: Kyverno
slug: kyverno
categories: [policy-as-code]
layer: governance
aliases: []
website: "https://kyverno.io/"
founded: 2019
hq: (open-source project; commercial backer Nirmata, San Jose, CA)
ownership: independent
ownership_detail: CNCF graduated project (graduated 2026-03-24); created by Nirmata, contributed to CNCF in 2020. Apache-2.0 OSS.
ownership_confidence: high
funding_total:
last_funding:
deployment: [self-hosted]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, cncf, policy-as-code, kubernetes]
---

# Kyverno

**One-liner** — A Kubernetes-native, open-source policy engine that enforces policy-as-code as YAML — validating, mutating, and generating cluster resources so non-compliant workloads are blocked at admission.

**What it does** — Kyverno runs as a Kubernetes admission controller. You write policies as native Kubernetes YAML (no separate language), and it validates incoming resources against them (e.g. "no privileged containers," "images must come from approved registries," "every namespace gets these defaults"), mutates resources to enforce defaults, and generates required objects. Extended to image verification, and policies for resources beyond core Kubernetes. It is the "guardrails as software" layer for anything running on Kubernetes — which, for an AI stack, includes most self-hosted model-serving, agent, and RAG infrastructure.

**Where it sits in the stack** — [policy-as-code](../categories/policy-as-code.md), governance layer. Lethal-trifecta role: indirect/meta — it governs the Kubernetes substrate, enforcing the cluster-level controls behind [trust-zone-segmentation](../categories/trust-zone-segmentation.md) and [promotion-gates](../categories/promotion-gates.md). Not in the prompt/data path.

**Deployment & architecture** — Self-hosted; deployed into your Kubernetes clusters as an admission controller plus policy CRDs. GitOps-friendly (policies live in Git). Pairs with CI/CD promotion gates. Apache-2.0 licensed; commercial support and a management plane available from Nirmata.

**Positioning & differentiators** — Kubernetes-native and **YAML-based**, which is its key contrast with [open-policy-agent](open-policy-agent.md) / [styra](styra.md) (Rego, general-purpose, works beyond Kubernetes). Kyverno is easier for Kubernetes teams (no new language) but Kubernetes-scoped; OPA is more portable but steeper. Unlike [hashicorp-sentinel](hashicorp-sentinel.md), it is open and not tied to one vendor's products. CNCF **graduated** (2026-03-24), the foundation's highest maturity tier.

**Ownership, funding & M&A** — Open-source CNCF **graduated project**; created by **Nirmata**, contributed to CNCF in 2020, incubating 2022, graduated 2026-03-24. Independent/community-governed; Nirmata provides commercial backing. No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-2. Relevant if you self-host AI workloads on Kubernetes and want admission-time guardrails enforcing your zone and hardening policies. Low cost (OSS), strong governance signal (CNCF graduated). If you are not on Kubernetes it does not apply; for cross-system policy, weigh [open-policy-agent](open-policy-agent.md).

**Competitors / alternatives** — [open-policy-agent](open-policy-agent.md) (+ Gatekeeper), [styra](styra.md), [hashicorp-sentinel](hashicorp-sentinel.md) (IaC-side).

**Open questions / to verify** — Maturity of non-Kubernetes (JSON/any-resource) policy use beyond clusters.

## Sources
- [CNCF Announces Kyverno's Graduation](https://www.cncf.io/announcements/2026/03/24/cloud-native-computing-foundation-announces-kyvernos-graduation/) — fetched 2026-06-28 — supports: CNCF graduated 2026-03-24, Nirmata origin, what Kyverno is; confidence: high
- [Kyverno | CNCF](https://www.cncf.io/projects/kyverno/) — fetched 2026-06-28 — supports: CNCF timeline (accepted 2020, incubating 2022); confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established ownership = independent CNCF graduated project (2026-03-24), created by Nirmata. Contrasted with OPA/Sentinel.
