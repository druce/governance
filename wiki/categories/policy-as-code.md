---
type: category
name: Policy-as-Code
slug: policy-as-code
layer: governance
priority: day-2
trifecta_role: none-detection
maps_to_seed_doc: Policy-as-Code
maps_to_seed_csv: (OPA appears in MCP/Agent)
vendor_count: 5
status: drafted
last_updated: 2026-06-28
---

## Business objective

Your rules written as software, so the guardrails enforce themselves instead of living
in a PDF nobody reads. Policy-as-code expresses governance rules — who may deploy what,
which configurations are allowed, what an agent may call, which infrastructure is
compliant — as **version-controlled, testable, automatically-enforced code** evaluated
at decision points (CI/CD pipelines, Kubernetes admission, infrastructure provisioning,
API/agent calls). Instead of a human checking a checklist, an engine returns
allow/deny against a declarative policy. It is the automation substrate beneath
[promotion-gates](promotion-gates.md), [trust-zone-segmentation](trust-zone-segmentation.md), and increasingly agent authorization.

## When you need it

**Day-2 — automate after manual policy.** You write the policy in English first
([acceptable-use-policies](acceptable-use-policies.md), [risk-tiers](risk-tiers.md)) and enforce it manually via review; you
adopt policy-as-code when manual enforcement does not scale or when you need provable,
consistent gating. For a hedge-fund CTO, the typical entry points are cloud/Kubernetes
governance (a platform team already running OPA or Sentinel) and, newer, **agent/tool
authorization** — deciding in code whether an agent may invoke a given tool or reach a
given zone. It is plumbing: valuable, but adopted by platform/security engineering once
the manual process exists and the scale justifies codifying it.

## Lethal-trifecta role

**None-detection / enforcement substrate (potentially all).** Policy-as-code is not
itself a trifecta control; it is the **mechanism** by which other controls are enforced.
Used for trust-zone admission and agent authorization it can help break **any** leg —
denying egress, blocking access to sensitive data, or refusing an untrusted action — but
only as configured. It lives in the **green (governed) zone** as the engine that turns
zone and promotion rules into enforced decisions. Closely related to the
[authorization-engine](authorization-engine.md) category (same engines — OPA, Cerbos — applied to
fine-grained agent/tool authz rather than infra policy).

## Vendors

OSS projects and the general-purpose policy engines:

- [open-policy-agent](../vendors/open-policy-agent.md) — CNCF general-purpose policy engine (Rego); the de facto standard for cloud/K8s and externalized authz.
- [styra](../vendors/styra.md) — commercial OPA: management, distribution, and control plane (DAS) for OPA at scale.
- [hashicorp-sentinel](../vendors/hashicorp-sentinel.md) — policy-as-code embedded in the HashiCorp stack (Terraform/Vault), governing infrastructure provisioning.
- [kyverno](../vendors/kyverno.md) — Kubernetes-native policy engine using YAML/CRDs instead of a dedicated policy language.
- [terraform-cloud](../vendors/terraform-cloud.md) — cross-listed: enforces Sentinel/OPA policy on infrastructure changes at provisioning time.

For policy-as-code applied specifically to **agent and tool authorization**, see the
[authorization-engine](authorization-engine.md) vendors ([cerbos](../vendors/cerbos.md), [permit-io](../vendors/permit-io.md), [authzed](../vendors/authzed.md), [oso](../vendors/oso.md)) —
the same idea pointed at runtime agent decisions.

## Consolidation / M&A dynamics

A largely open-source-anchored space: OPA (CNCF) commercialized by Styra; Kyverno
(CNCF); Sentinel proprietary to HashiCorp — and HashiCorp itself flagged as acquired by
IBM (per seed; unverified — to confirm in research), which would place Sentinel and
Terraform Cloud under IBM stewardship. No heavy roll-up otherwise; the live trend is
these engines being repurposed from infra governance toward **agent/MCP authorization**.

## Adjacent categories

- [authorization-engine](authorization-engine.md) — the same policy engines applied to fine-grained agent/tool authz (the runtime cousin of infra policy-as-code).
- [promotion-gates](promotion-gates.md) — the CI/CD sign-off practice that policy-as-code automates.
- [trust-zone-segmentation](trust-zone-segmentation.md) — zone admission rules are a natural policy-as-code use case.
- [ephemeral-environments](ephemeral-environments.md) — Terraform Cloud / Sentinel govern what zone-scoped environments may be provisioned.
- [mcp-gateway](mcp-gateway.md) — increasingly enforces policy-as-code on agent tool calls.

## Survey

**Question.** Which policy-as-code engines does your firm use to enforce
version-controlled policy (infrastructure, Kubernetes, or agent/tool authorization)?

**Answer options.** Open Policy Agent (OPA); Styra; HashiCorp Sentinel; Kyverno;
Terraform Cloud (Sentinel/OPA); Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** OPA is table-stakes / de facto standard; Styra is the
commercial wrapper around it, so respondents may legitimately select both — not a
contradiction. Sentinel selection usually tracks Terraform adoption; Kyverno tracks
Kubernetes adoption. Heavy conceptual overlap with the [authorization-engine](authorization-engine.md) survey
(OPA, Cerbos appear in both) — clarify whether you are asking about infra policy vs
agent/tool authz, or respondents will conflate them. HashiCorp's ownership (IBM, per
seed) may date the Sentinel/Terraform options.

## Open taxonomy questions

- Strong overlap with [authorization-engine](authorization-engine.md): OPA and Styra appear in both. The cut
  here is infra/CI/CD policy vs runtime agent/tool authorization — worth a comparison
  page rather than merging.
- Is this a "governance" category or a "policy/process" enabler? Kept under governance
  because it has real products and a survey, unlike the pure-process rows.
