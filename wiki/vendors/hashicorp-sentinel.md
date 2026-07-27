---
title: HashiCorp Sentinel
type: vendor
name: HashiCorp Sentinel
slug: hashicorp-sentinel
aka: [Sentinel]
primary_category: policy-as-code
also_listed_in: []
website: https://developer.hashicorp.com/sentinel
founded: 2017
hq: San Francisco, CA, USA
ownership_state: acquired-closed
owner: IBM
ownership_note: 'HashiCorp policy framework. HashiCorp acquired by IBM (NYSE: IBM) — announced 2024-04-24, completed 2025-02-27 after a 10-month wait on UK CMA clearance. $6.4B enterprise value at $35.00/share cash; $7,433M total consideration as booked under ASC 805. Now an IBM company.'
acquisition: {announced: 2024-04-24, closed: 2025-02-27, price: '$6.4B enterprise value ($35.00/share cash); ~$7.2B equity value; $7,433M ASC 805 consideration (IBM Q1 2025 10-Q Note 5)'}
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
last_verified: 2026-07-27
verify_after: null
tags: [first-party, policy-as-code, hashicorp, ibm]
---

# HashiCorp Sentinel

**One-liner** — HashiCorp's embedded policy-as-code framework that enforces fine-grained, logic-based guardrails inside Terraform, Vault, Nomad, and Consul Enterprise/HCP — blocking non-compliant changes before they apply.

**What it does** — Sentinel lets you write policies in its own language and attach them as enforcement gates (advisory / soft-mandatory / hard-mandatory) to HashiCorp workflows — e.g. "no public S3 buckets," "only approved instance types," "secrets must have a TTL." Policies run at plan/apply or request time, so violations are stopped rather than detected after the fact. It is the "guardrails as software" layer on HashiCorp's provisioning and secrets tools.

**Where it sits in the stack** — [policy-as-code](../categories/policy-as-code.md), governance layer. Tightly coupled to [terraform-cloud](terraform-cloud.md) (its most common host) and [hashicorp-vault](hashicorp-vault.md). Its risk role is indirect/meta — it doesn't sit in the prompt or data path; it governs the infrastructure and secrets workflows that everything else depends on, and underpins [trust-zone-segmentation](../categories/trust-zone-segmentation.md) and [promotion-gates](../categories/promotion-gates.md).

**Deployment & architecture** — Embedded framework, not a standalone server: runs inside Terraform Cloud/Enterprise (HCP Terraform), Vault, Nomad, Consul Enterprise. Available on paid/Enterprise tiers. CLI for local policy testing.

**Positioning & differentiators** — Proprietary and **HashiCorp-ecosystem-specific** — its strength (deep, native integration with Terraform/Vault) is also its limit. Contrast the open, general-purpose engines: [open-policy-agent](open-policy-agent.md) (Rego, cloud-native, works across many systems) and [kyverno](kyverno.md) (Kubernetes-native, YAML). Pick Sentinel when you are standardized on HashiCorp Enterprise; pick OPA/Kyverno for portability.

**Ownership, funding & M&A** — Part of HashiCorp, which **IBM agreed to acquire on 2024-04-24 and completed on 2025-02-27** at $35.00/share cash — $6.4B enterprise value, ~$7.2B equity value, $7,433M consideration as booked under ASC 805. The ten-month gap was regulatory: stockholders approved 2024-07-15, the UK CMA signalled a review 2024-08-01 and formally opened its inquiry 2024-12-30, cleared it at Phase 1 on 2025-02-25, and the deal closed two days later. Sentinel is now an IBM product; no separate M&A of its own. Confidence: high (both sides' SEC filings plus both IBM newsroom releases).

**CTO / hedge-fund lens** — Day-2. Relevant only if you run HashiCorp Enterprise/HCP and want policy gates on infrastructure and secrets. Not an AI-specific control, but a credible mechanism to enforce trust-zone and promotion-gate rules in IaC. If you are not a HashiCorp shop, [open-policy-agent](open-policy-agent.md) or [kyverno](kyverno.md) is the more neutral choice.

**Competitors / alternatives** — [open-policy-agent](open-policy-agent.md), [kyverno](kyverno.md).

**Open questions / to verify** — Post-IBM roadmap; whether Sentinel stays HashiCorp-exclusive or broadens.

## Sources
- [IBM Form 10-Q, Q1 2025](https://www.sec.gov/Archives/edgar/data/51143/000005114325000032/ibm-20250331.htm), Note 5 *Acquisitions* — fetched 2026-07-27 — supports: **close date 2025-02-27** (also IBM's XBRL tag `ibm:HashiCorpMember`), ~$7.2B equity value, $7,433M ASC 805 consideration; confidence: high (primary). Cached: `raw/sources/2026-07-27--hashicorp--ibm-acquisition-dates.md`
- [HashiCorp Form 8-K — merger agreement (2024-04-24)](https://www.sec.gov/Archives/edgar/data/1720671/000119312524114310/d804229d8k.htm) — fetched 2026-07-27 — supports: **announce date 2024-04-24**, Agreement and Plan of Merger among IBM, McCloud Merger Sub and HashiCorp, $35.00/share; confidence: high (primary)
- [HashiCorp Form 8-K — closing (2025-02-27)](https://www.sec.gov/Archives/edgar/data/1720671/000119312525037910/d898526d8k.htm) — fetched 2026-07-27 — supports: "consummation on February 27, 2025 (the 'Closing Date') of the transaction contemplated by that certain Agreement and Plan of Merger, dated April 24, 2024" — both dates in one sentence; confidence: high (primary)
- [IBM Completes Acquisition of HashiCorp](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform) — fetched 2026-06-28, re-checked 2026-07-27 — supports: HashiCorp/Sentinel now IBM-owned as of 2025-02-27, $6.4B; confidence: high
- [IBM to Acquire HashiCorp](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) — fetched 2026-07-27 — supports: announcement dateline April 24, 2024, $6.4B enterprise value; confidence: high
- [UK CMA — IBM/HashiCorp merger inquiry](https://www.gov.uk/cma-cases/ibm-slash-hashicorp-merger-inquiry) — fetched 2026-07-27 — supports: why the deal took ten months to close (Phase 1 clearance 2025-02-25); confidence: high (regulator primary)
- [raw/sources/2026-06-28--terraform-cloud--ibm-completes-hashicorp.md] — supports: ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established ownership = subsidiary (HashiCorp, acq. IBM 2025-02-27, high). Described as ecosystem-specific policy-as-code vs OPA/Kyverno.
- [2026-07-27] Date-sanity sweep — **fixed a conflated announce/close date**. `ownership_state: acquired-closed` sat next to `closed: null` (self-contradictory), and `announced: 2025-02-27` was actually holding the *close* date. IBM announced the HashiCorp deal on **2024-04-24** (HashiCorp 8-K Item 1.01; IBM newsroom dateline) and completed it on **2025-02-27** (HashiCorp's closing 8-K states both dates in one sentence; IBM's Q1 2025 10-Q Note 5 and XBRL tag agree). Ten-month gap explained by the UK CMA inquiry, cleared at Phase 1 on 2025-02-25. Also filled the null `price` ($6.4B enterprise value / $35.00 per share; $7,433M ASC 805 consideration) and normalized `owner: IBM 2025-02-27` → `owner: IBM` (the field should carry the company, not a date). Cached 1 new source, shared with `terraform-cloud`.
- [2026-07-27] URL fix: `docs.hashicorp.com/sentinel` 308-redirects to `developer.hashicorp.com/sentinel` (HashiCorp consolidated product docs onto the developer portal). Docs-platform domain migration only — same company, same product. Verified live; `last_verified` bumped.
