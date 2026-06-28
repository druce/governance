---
title: Identity & Access (IdP/SSO)
type: category
name: Identity & Access (IdP/SSO)
slug: identity-access
layer: foundation
priority: day-1
trifecta_role: sensitive-data (foundational enabler; least-privilege gates who/what reaches sensitive systems across all three legs)
maps_to_seed_doc: Identity & Access
maps_to_seed_csv: General Identity
vendor_count: 5
status: drafted
last_updated: 2026-06-28
---

## Business objective

This is the front door. An identity provider (IdP) gives every human — and, increasingly, every agent and workload — a single verified identity, single sign-on (SSO), multi-factor authentication, and role-based access control (RBAC). The seed doc's metaphor: the bouncer at the door who verifies who (or which agent) you are and hands out least-privilege badges.

Everything else in the stack leans on this. DLP, data-access governance, AI access governance, and trust-zone enforcement all assume there is a reliable answer to "who is this?" If identity is weak or fragmented, every downstream control inherits that weakness.

## When you need it

Day-1, non-negotiable. No hedge fund stands up a governed AI platform without an IdP already in place — in practice it is usually the oldest piece of the security stack. For most shops this slot is already filled (commonly Microsoft Entra ID, because it ships with M365). The AI-era question is not "do we have an IdP" but "is SSO/MFA actually enforced everywhere, and can it issue and govern identities for agents and service accounts, not just people?"

## Lethal-trifecta role

Cross-cutting rather than a single leg. Identity does not by itself break untrusted-input, sensitive-data, or egress — but it is the substrate that makes zone enforcement possible. You cannot keep an agent out of the green zone, or scope it to read-only data, if you cannot first prove which identity is making the request. It is foundational to all three legs and lives across every trust zone.

## Vendors

Core enterprise IdPs (the survey shortlist):

- [microsoft-entra](../vendors/microsoft-entra.md) — Microsoft Entra ID; default for M365 shops, bundled, broad reach into the Microsoft estate.
- [okta](../vendors/okta.md) — independent identity platform; strong in heterogeneous/multi-cloud environments and as a neutral SSO hub.
- [ping-identity](../vendors/ping-identity.md) — enterprise IdP, strong in regulated/large-enterprise and CIAM use cases (now under Thoma Bravo).
- [forgerock](../vendors/forgerock.md) — enterprise identity platform; per seed, acquired into the Ping/Thoma Bravo orbit (unverified — to confirm in research).

Adjacent / agent-era identity:

- [workos](../vendors/workos.md) — developer-focused auth and SSO; primary fit is tool/agent identity, listed here as it overlaps the IdP slot for app builders.

## Consolidation / M&A dynamics

- ForgeRock — per seed, acquired by Thoma Bravo and folded toward Ping Identity (per seed; unverified — to confirm in research).
- Ping Identity — taken private by Thoma Bravo (per seed; unverified — to confirm in research).

The macro story: the standalone-IdP field has thinned via private-equity roll-ups, leaving Entra (Microsoft) and Okta as the two independents most funds actually weigh, with Ping/ForgeRock consolidated behind them.

## Adjacent categories

- [non-human-identity](non-human-identity.md) — extends the same "real identity" idea to workloads and agents; the agent-era growth edge of this layer.
- [identity-governance](identity-governance.md) — sits on top of the IdP to decide who *should* have access (joiner/mover/leaver, access certifications).
- [secrets-management](secrets-management.md) — handles machine credentials/API keys; complements human/agent identity.
- [tool-identity-integration](tool-identity-integration.md) — how agents authenticate to downstream SaaS tools; WorkOS/Descope/Stytch live here.

## Survey

**Question.** Which identity provider(s) / SSO platform(s) is your firm currently using or evaluating for human and agent access?

**Answer options.** Microsoft Entra ID; Okta; Ping Identity; ForgeRock; WorkOS; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Entra and Okta are table-stakes and will dominate "in production" responses; most respondents already own one, so framing should emphasize *primary* IdP and whether agent/workload identity is in scope. Ping and ForgeRock now overlap (same PE owner) — list both but expect confusion; consider a note. WorkOS is niche (developer/app-builder) and may belong better under tool-identity; include only if surveying teams that build their own AI apps.

## Open taxonomy questions

- Where does the human-IdP slot end and [non-human-identity](non-human-identity.md) begin as agents get first-class identities? The two may converge.
- WorkOS is cross-listed; decide whether it appears in this survey question or only under [tool-identity-integration](tool-identity-integration.md).
