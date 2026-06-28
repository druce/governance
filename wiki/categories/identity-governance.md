---
type: category
name: Identity Governance & Visibility (IGA / ISPM)
slug: identity-governance
layer: foundation
priority: day-2
trifecta_role: sensitive-data (right-sizes standing access so fewer identities can reach sensitive systems)
maps_to_seed_doc: (folded into Identity & Access + Data Access Gov)
maps_to_seed_csv: Identity Governance & Visibility (IGA / ISPM)
vendor_count: 9
status: drafted
last_updated: 2026-06-28
---

## Business objective

The IdP decides *who you are*; identity governance (IGA) decides *what you should be allowed to do, and proves it*. It runs the joiner/mover/leaver lifecycle (access granted on hire, changed on transfer, revoked on exit), runs periodic access certifications, and gives auditors a defensible answer to "who has access to what, and why." Identity security posture management (ISPM) is the visibility/posture sibling — discovering accounts, entitlements, and risky standing access across the estate.

The job is right-sizing standing privilege: finding the dormant admin account, the contractor who never lost access, and the over-broad role no one reviews.

## When you need it

Day-2 for most funds — you need an IdP first, then governance on top. It becomes pressing under regulatory/audit pressure, at headcount scale where manual access reviews break down, and when agents and service accounts add a flood of new entitlements no human is reviewing. A 50-person fund may run light IGA out of Entra; a larger or heavily regulated shop will want a dedicated platform for certification and audit evidence.

## Lethal-trifecta role

The sensitive-data leg, indirectly. IGA does not inspect traffic — it shrinks the blast radius by ensuring fewer identities (human or non-human) hold standing access to sensitive systems, so a compromised account or rogue agent has less to reach. Lives across all zones as a governance overlay rather than an inline control.

## Vendors

IGA / ISPM platforms:

- [[sailpoint]] — the enterprise IGA incumbent; broad, mature, heavy. Also strong in data access (SailPoint DAS).
- [[saviynt]] — converged identity-governance and cloud-PAM platform; enterprise scale.
- [[veza]] — access-graph / authorization visibility ("who can do what to which data"); strong on entitlements across SaaS and data.
- [[conductorone]] — AI-native, modern IGA focused on access requests and certifications.
- [[lumos]] — AI-native identity/access governance with an app-store/self-service access model.
- [[linx-security]] — AI-native IGA that also covers non-human identity.
- [[hydden]] — identity visibility/discovery layer that feeds IGA tools (competes with Silverfort/Sharelock/Andromeda per seed).
- [[silverfort]] — identity security and posture across human and non-human accounts; discovery and MFA enforcement.

Cross-listed:

- [[cyberark]] — PAM-first incumbent extending into IGA (per seed, acquired by Palo Alto).

## Consolidation / M&A dynamics

- CyberArk — per seed, acquired by Palo Alto Networks (per seed; unverified — to confirm in research).

Two dynamics: incumbents (SailPoint, Saviynt, CyberArk) defending the enterprise install base, and a wave of AI-native challengers (ConductorOne, Lumos, Linx) attacking the slow, expensive certification workflows. Veza sits somewhat apart as an access-graph/visibility play that overlaps data-access governance.

## Adjacent categories

- [[identity-access]] — the IdP IGA governs on top of.
- [[non-human-identity]] — IGA extended to service accounts and agents; Linx/Silverfort straddle both.
- [[data-access-governance]] — strongly overlapping: Veza, SailPoint, ConductorOne, Silverfort appear in both; IGA governs identity entitlements, DAG governs data permissions, and they meet at "who can open which file."
- [[secrets-management]] — governs machine credentials; complementary.

## Survey

**Question.** Which identity governance / IGA / ISPM tool(s) is your firm currently using or evaluating?

**Answer options.** SailPoint; Saviynt; Veza; ConductorOne; Lumos; Linx Security; Hydden; Silverfort; CyberArk; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** SailPoint and Saviynt are the table-stakes incumbents; the AI-native group (ConductorOne, Lumos, Linx) will skew toward "evaluating/pilot." Veza and Silverfort overlap [[data-access-governance]] — respondents may report them under either question, so the two surveys should be cross-referenced. CyberArk is PAM-first and may be reported here for the wrong reason; the CyberArk→Palo Alto deal (per seed) dates that option. Hydden is a visibility layer, not full IGA — niche.

## Open taxonomy questions

- Large overlap with [[data-access-governance]] (Veza, SailPoint, ConductorOne, Silverfort) — confirm the IGA-vs-DAG boundary stays clean for survey mapping.
- ISPM (posture) vs. IGA (lifecycle) could split as posture-only vendors (Hydden) differentiate.
