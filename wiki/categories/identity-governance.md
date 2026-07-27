---
title: Identity Governance & Visibility (IGA / ISPM)
type: category
name: Identity Governance & Visibility (IGA / ISPM)
slug: identity-governance
category: identity-governance
layer: foundation
survey_question: Identity Governance & Visibility (IGA / ISPM)
adoption_tier: day-2
trigger: enough headcount/apps that joiner-mover-leaver and access certs need automation
maturity_stage_required: null
category_maturity: mature
adjacent: [identity-access, data-access-governance, non-human-identity]
incumbent_coverage: []
vendor_count: 9
maps_to_seed_doc: (folded into Identity & Access + Data Access Gov)
maps_to_seed_csv: Identity Governance & Visibility (IGA / ISPM)
last_verified: 2026-06-28
---

## Business objective

The IdP decides *who you are*; identity governance (IGA) decides *what you should be allowed to do, and proves it*. It runs the joiner/mover/leaver lifecycle (access granted on hire, changed on transfer, revoked on exit), runs periodic access certifications, and gives auditors a defensible answer to "who has access to what, and why." Identity security posture management (ISPM) is the visibility/posture sibling — discovering accounts, entitlements, and risky standing access across the estate.

The job is right-sizing standing privilege: finding the dormant admin account, the contractor who never lost access, and the over-broad role no one reviews.

## When you need it

Day-2 for most funds — you need an IdP first, then governance on top. It becomes pressing under regulatory/audit pressure, at headcount scale where manual access reviews break down, and when agents and service accounts add a flood of new entitlements no human is reviewing. A 50-person fund may run light IGA out of Entra; a larger or heavily regulated shop will want a dedicated platform for certification and audit evidence.

## Security role

Controls access to sensitive data, indirectly. IGA is preventive but out-of-band — it does not inspect traffic; it shrinks the blast radius by ensuring fewer identities (human or non-human) hold standing access to sensitive systems, so a compromised account or rogue agent has less to reach. Lives across all zones as a governance overlay rather than an inline control.

## Vendors

IGA / ISPM platforms:

- [sailpoint](../vendors/sailpoint.md) — the enterprise IGA incumbent; broad, mature, heavy. Also strong in data access (SailPoint DAS).
- [saviynt](../vendors/saviynt.md) — converged identity-governance and cloud-PAM platform; enterprise scale.
- [veza](../vendors/veza.md) — access-graph / authorization visibility ("who can do what to which data"); strong on entitlements across SaaS and data.
- [c1](../vendors/c1.md) — AI-native, modern IGA focused on access requests and certifications (formerly ConductorOne; renamed 2026-04).
- [lumos](../vendors/lumos.md) — AI-native identity/access governance with an app-store/self-service access model.
- [linx-security](../vendors/linx-security.md) — AI-native IGA that also covers non-human identity.
- [hydden](../vendors/hydden.md) — identity visibility/discovery layer that feeds IGA tools (competes with Silverfort/Sharelock/Andromeda per seed).
- [silverfort](../vendors/silverfort.md) — identity security and posture across human and non-human accounts; discovery and MFA enforcement.

Cross-listed:

- [cyberark](../vendors/cyberark.md) — PAM-first incumbent extending into IGA (per seed, acquired by Palo Alto).

## Consolidation / M&A dynamics

- CyberArk — per seed, acquired by Palo Alto Networks (per seed; unverified — to confirm in research).

Two dynamics: incumbents (SailPoint, Saviynt, CyberArk) defending the enterprise install base, and a wave of AI-native challengers (C1 — formerly ConductorOne, renamed 2026-04 — Lumos, Linx) attacking the slow, expensive certification workflows. Veza sits somewhat apart as an access-graph/visibility play that overlaps data-access governance.

## Adjacent categories

- [identity-access](identity-access.md) — the IdP IGA governs on top of.
- [non-human-identity](non-human-identity.md) — IGA extended to service accounts and agents; Linx/Silverfort straddle both.
- [data-access-governance](data-access-governance.md) — strongly overlapping: Veza, SailPoint, C1, Silverfort appear in both; IGA governs identity entitlements, DAG governs data permissions, and they meet at "who can open which file."
- [secrets-management](secrets-management.md) — governs machine credentials; complementary.

## Survey

**Question.** Which identity governance / IGA / ISPM tool(s) is your firm currently using or evaluating?

**Answer options.** SailPoint; Saviynt; Veza; C1 (formerly ConductorOne); Lumos; Linx Security; Hydden; Silverfort; CyberArk; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** SailPoint and Saviynt are the table-stakes incumbents; the AI-native group (C1, Lumos, Linx) will skew toward "evaluating/pilot." Veza and Silverfort overlap [data-access-governance](data-access-governance.md) — respondents may report them under either question, so the two surveys should be cross-referenced. CyberArk is PAM-first and may be reported here for the wrong reason; the CyberArk→Palo Alto deal (per seed) dates that option. Hydden is a visibility layer, not full IGA — niche.

## Open taxonomy questions

- Large overlap with [data-access-governance](data-access-governance.md) (Veza, SailPoint, C1, Silverfort) — confirm the IGA-vs-DAG boundary stays clean for survey mapping.
- ISPM (posture) vs. IGA (lifecycle) could split as posture-only vendors (Hydden) differentiate.
