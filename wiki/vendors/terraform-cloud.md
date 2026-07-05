---
title: Terraform Cloud (HCP Terraform)
type: vendor
name: Terraform Cloud (HCP Terraform)
slug: terraform-cloud
aka: [HCP Terraform, Terraform Enterprise]
primary_category: ephemeral-environments
also_listed_in: [policy-as-code]
website: https://www.hashicorp.com/products/terraform
founded: 2012
hq: San Francisco, CA, USA
ownership_state: acquired-closed
owner: IBM 2025-02-27
ownership_note: HashiCorp; acquired by IBM 2025-02-27 ($6.4B). Now an IBM company.
acquisition: {announced: 2025-02-27, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas, self-hosted]
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
tags: [first-party, infrastructure-as-code, hashicorp, ibm, policy-as-code]
---

# Terraform Cloud (HCP Terraform)

**One-liner** — HashiCorp's managed service for running Terraform infrastructure-as-code with remote state, collaboration, and policy enforcement — the control plane through which you provision (and govern) the cloud environments your AI stack runs in.

**What it does** — Terraform Cloud (rebranded **HCP Terraform**; the self-hosted edition is **Terraform Enterprise**) runs Terraform plans/applies in a managed environment, stores state centrally, and gates changes through policy checks before they hit cloud accounts. For the AI-governance reader it shows up two ways: (1) it is how you stand up and tear down the **ephemeral/isolated environments** behind trust-zone design, declaratively and repeatably; and (2) it is the host for [hashicorp-sentinel](hashicorp-sentinel.md) / OPA policy-as-code that blocks non-compliant infrastructure at plan time.

**Where it sits in the stack** — primary [ephemeral-environments](../categories/ephemeral-environments.md) (provisioning the zones), also [policy-as-code](../categories/policy-as-code.md) (the gate that runs against plans). Governance layer. Its risk role is indirect — it doesn't sit in the data/prompt path; it builds and guardrails the substrate the rest of the stack runs on. Enabler of [trust-zone-segmentation](../categories/trust-zone-segmentation.md) and [promotion-gates](../categories/promotion-gates.md).

**Deployment & architecture** — SaaS (HCP Terraform) or self-hosted (Terraform Enterprise). Integrates VCS (GitHub/GitLab), cloud providers, [hashicorp-sentinel](hashicorp-sentinel.md) and [open-policy-agent](open-policy-agent.md) for policy, and HashiCorp [hashicorp-vault](hashicorp-vault.md) for secrets. Run triggers / API drive CI/CD.

**Positioning & differentiators** — The canonical managed IaC control plane; deepest Terraform integration (it is the source's vendor). Sentinel policy-as-code is gated behind its paid tiers. Note the 2023 BSL license change for the Terraform CLI that spawned the OpenTofu fork — relevant if license terms matter to you.

**Ownership, funding & M&A** — HashiCorp was acquired by **IBM on 2025-02-27** for $6.4B; Terraform (and Sentinel, Vault) are now IBM products. The seed flag "(HashiCorp/IBM)" is **confirmed** against IBM's newsroom release. Confidence: high.

**CTO / hedge-fund lens** — Day-2 infrastructure, not an AI-security purchase. Relevant to the AI program because clean, policy-gated, ephemeral infrastructure provisioning is what makes trust-zone segmentation enforceable rather than aspirational. Most shops doing serious cloud already run Terraform; the AI angle is wiring Sentinel/OPA gates to your zone model.

**Competitors / alternatives** — [cloudflare-workers](cloudflare-workers.md) (different layer), OpenTofu + self-managed CI, Pulumi, env0/Spacelift (not in registry). For the policy gate: [hashicorp-sentinel](hashicorp-sentinel.md), [open-policy-agent](open-policy-agent.md), [kyverno](kyverno.md) (k8s-side).

**Open questions / to verify** — Post-IBM roadmap/branding changes to HCP Terraform; whether Sentinel remains Terraform-exclusive.

## Sources
- [IBM Completes Acquisition of HashiCorp](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform) — fetched 2026-06-28 — supports: IBM owns HashiCorp/Terraform as of 2025-02-27, $6.4B; confidence: high
- [raw/sources/2026-06-28--terraform-cloud--ibm-completes-hashicorp.md] — supports: ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); CONFIRMED HashiCorp acquired by IBM 2025-02-27 → ownership subsidiary (high). Filled out ephemeral-environments + policy-as-code roles.
