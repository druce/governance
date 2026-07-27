---
title: HashiCorp Sentinel
type: vendor
name: HashiCorp Sentinel
slug: hashicorp-sentinel
aka: [Sentinel]
primary_category: policy-as-code
also_listed_in: []
website: https://docs.hashicorp.com/sentinel
founded: 2017
hq: San Francisco, CA, USA
ownership_state: acquired-closed
owner: IBM 2025-02-27
ownership_note: HashiCorp policy framework; HashiCorp acquired by IBM 2025-02-27 ($6.4B). Now an IBM company.
acquisition: {announced: 2025-02-27, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [self-hosted, saas]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [first-party, policy-as-code, hashicorp, ibm]
---

# HashiCorp Sentinel

**One-liner** — HashiCorp's embedded policy-as-code framework that enforces fine-grained, logic-based guardrails inside Terraform, Vault, Nomad, and Consul Enterprise/HCP — blocking non-compliant changes before they apply.

**What it does** — Sentinel lets you write policies in its own language and attach them as enforcement gates (advisory / soft-mandatory / hard-mandatory) to HashiCorp workflows — e.g. "no public S3 buckets," "only approved instance types," "secrets must have a TTL." Policies run at plan/apply or request time, so violations are stopped rather than detected after the fact. It is the "guardrails as software" layer on HashiCorp's provisioning and secrets tools.

**Where it sits in the stack** — [policy-as-code](../categories/policy-as-code.md), governance layer. Tightly coupled to [terraform-cloud](terraform-cloud.md) (its most common host) and [hashicorp-vault](hashicorp-vault.md). Its risk role is indirect/meta — it doesn't sit in the prompt or data path; it governs the infrastructure and secrets workflows that everything else depends on, and underpins [trust-zone-segmentation](../categories/trust-zone-segmentation.md) and [promotion-gates](../categories/promotion-gates.md).

**Deployment & architecture** — Embedded framework, not a standalone server: runs inside Terraform Cloud/Enterprise (HCP Terraform), Vault, Nomad, Consul Enterprise. Available on paid/Enterprise tiers. CLI for local policy testing.

**Positioning & differentiators** — Proprietary and **HashiCorp-ecosystem-specific** — its strength (deep, native integration with Terraform/Vault) is also its limit. Contrast the open, general-purpose engines: [open-policy-agent](open-policy-agent.md) (Rego, cloud-native, works across many systems) and [kyverno](kyverno.md) (Kubernetes-native, YAML). Pick Sentinel when you are standardized on HashiCorp Enterprise; pick OPA/Kyverno for portability.

**Ownership, funding & M&A** — Part of HashiCorp, **acquired by IBM 2025-02-27** ($6.4B); now an IBM product. No separate M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-2. Relevant only if you run HashiCorp Enterprise/HCP and want policy gates on infrastructure and secrets. Not an AI-specific control, but a credible mechanism to enforce trust-zone and promotion-gate rules in IaC. If you are not a HashiCorp shop, [open-policy-agent](open-policy-agent.md) or [kyverno](kyverno.md) is the more neutral choice.

**Competitors / alternatives** — [open-policy-agent](open-policy-agent.md), [kyverno](kyverno.md).

**Open questions / to verify** — Post-IBM roadmap; whether Sentinel stays HashiCorp-exclusive or broadens.

## Sources
- [IBM Completes Acquisition of HashiCorp](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform) — fetched 2026-06-28 — supports: HashiCorp/Sentinel now IBM-owned; confidence: high
- [raw/sources/2026-06-28--terraform-cloud--ibm-completes-hashicorp.md] — supports: ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established ownership = subsidiary (HashiCorp, acq. IBM 2025-02-27, high). Described as ecosystem-specific policy-as-code vs OPA/Kyverno.
