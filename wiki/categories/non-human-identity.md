---
title: Non-Human / Agent Identity Governance
type: category
name: Non-Human / Agent Identity Governance
slug: non-human-identity
category: non-human-identity
layer: foundation
survey_question: Non-Human Identity / Agent Identity Governance
adoption_tier: day-2
trigger: agents and workloads hold their own credentials and call tools
maturity_stage_required: null
category_maturity: growth
adjacent: [identity-access, secrets-management, tool-identity-integration, identity-governance]
incumbent_coverage: []
vendor_count: 12
maps_to_seed_doc: (folded into Identity & Access + Tool Identity)
maps_to_seed_csv: Non-Human Identity / Agent Identity Governance
last_verified: 2026-06-28
---

## Business objective

Most identities in a modern enterprise are not people — they are service accounts, API keys, OAuth tokens, CI/CD jobs, workload identities, and now AI agents. Non-human identity (NHI) governance discovers all of these, gives them real, least-privilege identities, and ideally issues short-lived, secrets-less credentials so a workload authenticates by *what it is* rather than by a long-lived key sitting in a config file.

If the human IdP is the bouncer at the door, NHI is the same discipline applied to the machines and bots — knowing which one is which, what it is allowed to touch, and being able to cut it off.

## When you need it

Day-2 for most funds, but it moves toward Day-1 the moment agents start acting autonomously or you have sprawl of service accounts and tokens (almost everyone does). The trigger is agentic AI: an agent that can authenticate to internal systems is a non-human identity with standing access, and ungoverned agent/service-account credentials are a fast-growing breach path. A small fund with few agents can defer; a shop deploying agents against production systems should treat this as near-term.

## Security role

A preventive control on access to sensitive data and on how far data can flow out. NHI decides what a workload or agent is allowed to authenticate to (which systems, which data) and — via short-lived, scoped credentials — bounds the blast radius of a compromised agent or stolen credential, limiting what it can reach or exfiltrate. Lives at the boundary of the yellow and green zones, where agents hold real credentials.

## Vendors

Dedicated NHI / agent-identity platforms (the survey shortlist):

- [cyberark](../vendors/cyberark.md) — PAM incumbent extending into NHI and secrets-less workload/agent identity; broadest enterprise footprint.
- [astrix-security](../vendors/astrix-security.md) — NHI discovery and governance for app-to-app connections, tokens, and OAuth grants.
- [token-security](../vendors/token-security.md) — NHI security and governance platform focused on machine-identity sprawl.
- [aembit](../vendors/aembit.md) — workload identity and access management; issues short-lived, policy-based credentials (secrets-less workload auth).
- [oasis-security](../vendors/oasis-security.md) — NHI lifecycle management and discovery/governance.
- [natoma](../vendors/natoma.md) — agent identity and access governance (also relevant to MCP/tool access).
- [entro-security](../vendors/entro-security.md) — NHI and secrets security; discovery of non-human identities and exposed secrets. Acquired by [sailpoint](../vendors/sailpoint.md) (closed 2026-06-29) — the IGA incumbent buying into this category.
- [clutch-security](../vendors/clutch-security.md) — NHI security platform.
- [keycard](../vendors/keycard.md) — runtime authorization built for agents: short-lived, task-scoped credentials that narrow at each delegation hop via OAuth token exchange, with Cedar policy-as-code. Founded 2025; $38M raised. Cross-listed to [tool-identity-integration](tool-identity-integration.md) and [authorization-engine](authorization-engine.md). (added 2026-10-16)

Identity/governance platforms with NHI capabilities (cross-listed):

- [silverfort](../vendors/silverfort.md) — identity security across human and non-human accounts; service-account discovery and MFA.
- [linx-security](../vendors/linx-security.md) — AI-native IGA that explicitly covers NHI.
- [descope](../vendors/descope.md) / [stytch](../vendors/stytch.md) — agent/app auth (primary fit is tool-identity), relevant for issuing agent identities.

## Consolidation / M&A dynamics

- CyberArk — per seed, acquired by Palo Alto Networks (per seed; unverified — to confirm in research).
- Astrix Security — per seed, acquired by Cisco (per seed; unverified — to confirm in research).
- Entro Security — acquired by [sailpoint](../vendors/sailpoint.md) (announced 2026-06-18, closed 2026-06-29; ~$200M reported) for its Agentic Fabric agent-identity platform. Verified against SailPoint's press release.

NHI is an active acquisition target: the platform players (Palo Alto, Cisco, now SailPoint) are buying the discovery/governance startups to bolt NHI onto their identity and SASE stacks — three of the eight shortlist vendors are now acquired or pending. Expect this list to keep consolidating.

## Adjacent categories

- [identity-access](identity-access.md) — the human-side IdP; NHI is the same discipline for machines and agents.
- [secrets-management](secrets-management.md) — the vault for the credentials NHI governs; the two overlap heavily (Entro, CyberArk span both).
- [identity-governance](identity-governance.md) — joiner/mover/leaver and access certs, increasingly extended to non-human accounts.
- [tool-identity-integration](tool-identity-integration.md) — how agents authenticate to SaaS tools; consumes NHI.
- [mcp-gateway](mcp-gateway.md) — brokers which tools agents reach; pairs with agent identity.

## Survey

**Question.** Which non-human / agent identity governance tool(s) is your firm currently using or evaluating?

**Answer options.** CyberArk; Astrix Security; Token Security; Aembit; Oasis Security; Natoma; Entro Security (SailPoint); Clutch Security; Keycard; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** This is an emerging, crowded category — most respondents will cluster in "Interested/Considering," and many will not yet distinguish vendors clearly. CyberArk is the incumbent anchor and overlaps PAM/secrets, which may inflate its "in production" count for the wrong reason (existing PAM, not new NHI). The CyberArk→Palo Alto, Astrix→Cisco, and Entro→SailPoint (closed 2026-06-29) deals date those options. Consider asking separately about service-account/secrets sprawl vs. autonomous-agent identity — buyers conflate them.

## Open taxonomy questions

- Heavy overlap with [secrets-management](secrets-management.md) (Entro, CyberArk) and [identity-governance](identity-governance.md) (Silverfort, Linx) — where to draw NHI's boundary.
- Agent identity vs. workload identity may deserve splitting as agentic deployments mature.
