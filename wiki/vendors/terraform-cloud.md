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
owner: IBM
ownership_note: 'HashiCorp; acquired by IBM (NYSE: IBM) — announced 2024-04-24, completed 2025-02-27 after a 10-month wait on UK CMA clearance. $6.4B enterprise value at $35.00/share cash; $7,433M total consideration as booked under ASC 805. Now an IBM company.'
acquisition: {announced: 2024-04-24, closed: 2025-02-27, price: '$6.4B enterprise value ($35.00/share cash); ~$7.2B equity value; $7,433M ASC 805 consideration (IBM Q1 2025 10-Q Note 5)'}
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
last_verified: 2026-07-27
verify_after: null
tags: [first-party, infrastructure-as-code, hashicorp, ibm, policy-as-code]
---

# Terraform Cloud (HCP Terraform)

**One-liner** — HashiCorp's managed service for running Terraform infrastructure-as-code with remote state, collaboration, and policy enforcement — the control plane through which you provision (and govern) the cloud environments your AI stack runs in.

**What it does** — Terraform Cloud (rebranded **HCP Terraform**; the self-hosted edition is **Terraform Enterprise**) runs Terraform plans/applies in a managed environment, stores state centrally, and gates changes through policy checks before they hit cloud accounts. For the AI-governance reader it shows up two ways: (1) it is how you stand up and tear down the **ephemeral/isolated environments** behind trust-zone design, declaratively and repeatably; and (2) it is the host for [hashicorp-sentinel](hashicorp-sentinel.md) / OPA policy-as-code that blocks non-compliant infrastructure at plan time.

**Where it sits in the stack** — primary [ephemeral-environments](../categories/ephemeral-environments.md) (provisioning the zones), also [policy-as-code](../categories/policy-as-code.md) (the gate that runs against plans). Governance layer. Its risk role is indirect — it doesn't sit in the data/prompt path; it builds and guardrails the substrate the rest of the stack runs on. Enabler of [trust-zone-segmentation](../categories/trust-zone-segmentation.md) and [promotion-gates](../categories/promotion-gates.md).

**Deployment & architecture** — SaaS (HCP Terraform) or self-hosted (Terraform Enterprise). Integrates VCS (GitHub/GitLab), cloud providers, [hashicorp-sentinel](hashicorp-sentinel.md) and [open-policy-agent](open-policy-agent.md) for policy, and HashiCorp [hashicorp-vault](hashicorp-vault.md) for secrets. Run triggers / API drive CI/CD.

**Positioning & differentiators** — The canonical managed IaC control plane; deepest Terraform integration (it is the source's vendor). Sentinel policy-as-code is gated behind its paid tiers. Note the 2023 BSL license change for the Terraform CLI that spawned the OpenTofu fork — relevant if license terms matter to you.

**Ownership, funding & M&A** — **IBM agreed to acquire HashiCorp on 2024-04-24 and completed the deal on 2025-02-27** at $35.00/share cash — $6.4B enterprise value, ~$7.2B equity value, $7,433M consideration as booked under ASC 805. The ten-month gap was regulatory: stockholders approved 2024-07-15, the UK CMA signalled a review 2024-08-01 and formally opened its inquiry 2024-12-30, cleared it at Phase 1 on 2025-02-25, and the deal closed two days later — which is why the original 8-K's "expected to close by end of 2024" language slipped. Terraform (and Sentinel, Vault) are now IBM products. The seed flag "(HashiCorp/IBM)" is **confirmed** against both sides' SEC filings and both IBM newsroom releases. Confidence: high.

**CTO / hedge-fund lens** — Day-2 infrastructure, not an AI-security purchase. Relevant to the AI program because clean, policy-gated, ephemeral infrastructure provisioning is what makes trust-zone segmentation enforceable rather than aspirational. Most shops doing serious cloud already run Terraform; the AI angle is wiring Sentinel/OPA gates to your zone model.

**Competitors / alternatives** — [cloudflare-workers](cloudflare-workers.md) (different layer), OpenTofu + self-managed CI, Pulumi, env0/Spacelift (not in registry). For the policy gate: [hashicorp-sentinel](hashicorp-sentinel.md), [open-policy-agent](open-policy-agent.md), [kyverno](kyverno.md) (k8s-side).

**Open questions / to verify** — Post-IBM roadmap/branding changes to HCP Terraform; whether Sentinel remains Terraform-exclusive.

## Sources
- [IBM Form 10-Q, Q1 2025](https://www.sec.gov/Archives/edgar/data/51143/000005114325000032/ibm-20250331.htm), Note 5 *Acquisitions* — fetched 2026-07-27 — supports: **close date 2025-02-27** (also IBM's XBRL tag `ibm:HashiCorpMember`), ~$7.2B equity value, $7,433M ASC 805 consideration; confidence: high (primary). Cached: `raw/sources/2026-07-27--hashicorp--ibm-acquisition-dates.md`
- [HashiCorp Form 8-K — merger agreement (2024-04-24)](https://www.sec.gov/Archives/edgar/data/1720671/000119312524114310/d804229d8k.htm) — fetched 2026-07-27 — supports: **announce date 2024-04-24**, Agreement and Plan of Merger among IBM, McCloud Merger Sub and HashiCorp, $35.00/share; confidence: high (primary)
- [HashiCorp Form 8-K — closing (2025-02-27)](https://www.sec.gov/Archives/edgar/data/1720671/000119312525037910/d898526d8k.htm) — fetched 2026-07-27 — supports: "consummation on February 27, 2025 (the 'Closing Date') of the transaction contemplated by that certain Agreement and Plan of Merger, dated April 24, 2024" — both dates in one sentence; confidence: high (primary)
- [IBM Completes Acquisition of HashiCorp](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform) — fetched 2026-06-28, re-checked 2026-07-27 — supports: IBM owns HashiCorp/Terraform as of 2025-02-27, $6.4B; confidence: high
- [IBM to Acquire HashiCorp](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) — fetched 2026-07-27 — supports: announcement dateline April 24, 2024, $6.4B enterprise value; confidence: high
- [UK CMA — IBM/HashiCorp merger inquiry](https://www.gov.uk/cma-cases/ibm-slash-hashicorp-merger-inquiry) — fetched 2026-07-27 — supports: why the deal took ten months to close (Phase 1 clearance 2025-02-25); confidence: high (regulator primary)
- [raw/sources/2026-06-28--terraform-cloud--ibm-completes-hashicorp.md] — supports: ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); CONFIRMED HashiCorp acquired by IBM 2025-02-27 → ownership subsidiary (high). Filled out ephemeral-environments + policy-as-code roles.
- [2026-07-27] Date-sanity sweep — **fixed a conflated announce/close date** (same defect as `hashicorp-sentinel`, same deal). `ownership_state: acquired-closed` sat next to `closed: null` (self-contradictory), and `announced: 2025-02-27` was actually holding the *close* date. IBM announced the HashiCorp deal on **2024-04-24** (HashiCorp 8-K Item 1.01; IBM newsroom dateline) and completed it on **2025-02-27** (HashiCorp's closing 8-K states both dates in one sentence; IBM's Q1 2025 10-Q Note 5 and XBRL tag agree). Ten-month gap explained by the UK CMA inquiry, cleared at Phase 1 on 2025-02-25. Also filled the null `price` ($6.4B enterprise value / $35.00 per share; $7,433M ASC 805 consideration) and normalized `owner: IBM 2025-02-27` → `owner: IBM`. Cited the source cached for `hashicorp-sentinel`.
