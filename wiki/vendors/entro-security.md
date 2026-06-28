---
type: vendor
name: Entro Security
slug: entro-security
categories: [non-human-identity, secrets-management]
layer: foundation
aliases: []
website: "https://entro.security"
founded: 2022
hq: Boston, Massachusetts, USA (R&D Tel Aviv)
ownership: independent
ownership_detail: "VC-backed; no acquisition found as of 2026-06-28"
ownership_confidence: high
funding_total: "$24M"
last_funding: "Series A, June 2024 ($18M, led by Dell Technologies Capital)"
deployment: [saas, api]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [non-human-identity, secrets-management, nhi, agentic]
---

# Entro Security

> **One-liner** — An agentless SaaS platform that discovers, governs, and manages the full lifecycle of non-human identities and secrets (API keys, tokens, service accounts) across cloud, SaaS, and on-prem.

**Categories** — [non-human-identity](../categories/non-human-identity.md) (primary), [secrets-management](../categories/secrets-management.md)

## What it does
Entro inventories the machine identities and secrets scattered across an enterprise — API keys, OAuth tokens, certificates, service accounts — and manages them end to end: discovery, vaulting, automatic rotation, anomaly/threat detection, and decommissioning of idle or over-privileged identities. The pitch is that most organizations have thousands of unmanaged secrets with excessive permissions and no single owner; Entro maps them, scores risk, and provides real-time detection and response. It has since extended into securing AI/agent ("agentic") identities.

## Where it sits in the stack
Foundation layer. Primary home is [non-human-identity](../categories/non-human-identity.md) (the system of record and lifecycle for machine identities) with strong overlap into [secrets-management](../categories/secrets-management.md). Unlike a vault (which stores secrets), Entro focuses on *discovery, posture, and lifecycle governance* across the secrets that already exist in many vaults and platforms. Lethal-trifecta role: constrains the **egress / action** leg (limiting what credentials can reach) and protects **sensitive-data** by finding and rotating exposed or over-scoped secrets.

## Deployment & architecture
Agentless SaaS — connects via API/read access to cloud providers, SaaS apps, vaults, and source/CI systems rather than installing agents. Detection-and-response across on-prem, cloud, and SaaS. SOC2 and GDPR compliant per vendor.

## Positioning & differentiators
Entro is an NHI-and-secrets *governance* layer rather than a vault — it sits over existing secret stores (cloud secret managers, [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md)/Conjur) to give one inventory, risk posture, and automated rotation. Its nearest neighbors are [clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), and [astrix-security](astrix-security.md); vs. those it emphasizes the secrets-lifecycle (vaulting + rotation + decommissioning) angle. Differentiated from MCP-native agent brokers like [natoma](natoma.md) and [mintmcp](mintmcp.md), which govern the runtime tool call rather than the credential lifecycle.

## Ownership, funding & M&A
- **Independent, VC-backed.** Founded 2022 by Itzik Alvas (CEO) and Adam Cheriki (CTO), both Israeli IDF cyber-unit alumni. HQ Boston, MA, with R&D in Tel Aviv.
- **Funding:** $6M seed (May 2023) + $18M Series A (June 2024, led by Dell Technologies Capital) = **$24M total**.
- **M&A:** No acquisition flag in the seed and none found as of 2026-06-28 — remains independent (high confidence on independence; "couldn't find" rather than "doesn't exist").

## CTO / hedge-fund lens
Day-2. Most relevant once a fund has meaningful cloud/SaaS sprawl and is worried about ungoverned API keys and service-account credentials — a real audit and breach concern (NHI/secrets breaches rank high in IBM/Verizon data per vendor). For a small fund largely on managed cloud secret managers, this is optional until secrets sprawl becomes unmanageable. No direct SR 11-7 role, but supports access-control and operational-risk evidence. Boston HQ and Dell Capital backing are mild comfort signals for a regulated buyer.

## Competitors / alternatives
[clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), [astrix-security](astrix-security.md), [silverfort](silverfort.md); vaults: [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md), [azure-key-vault](azure-key-vault.md), [aws-secrets-manager](aws-secrets-manager.md).

## Open questions / to verify
- Current customer count / scale (only vendor-stated headcount growth found).
- Depth of agentic-AI identity capabilities vs. core NHI/secrets product.
- Any funding since the June 2024 Series A.

## Sources
- [Non-Human Identity Lifecycle Firm Entro Security Raises $18 Million](https://www.securityweek.com/non-human-identity-lifecycle-firm-entro-security-raises-18-million/) — fetched 2026-06-28 — supports: $18M Series A (Dell Tech Capital), $24M total, founders, founded, Boston HQ, product scope; confidence: high
- Web search (Crunchbase, Business Wire, Calcalist) — fetched 2026-06-28 — supports: $6M seed May 2023, founding details; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022, Boston HQ (R&D Tel Aviv), founders Alvas/Cheriki, $24M total funding ($6M seed 2023 + $18M Series A 2024, Dell Tech Capital). No M&A — confirmed independent (high confidence). Agentless SaaS NHI + secrets-lifecycle positioning; hedge_fund_fit medium.
