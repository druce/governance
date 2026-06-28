---
title: Clutch Security
type: vendor
name: Clutch Security
slug: clutch-security
categories: [non-human-identity]
layer: foundation
aliases: []
website: "https://www.clutch.security"
founded: 2023
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: "VC-backed; no acquisition found as of 2026-06-28"
ownership_confidence: high
funding_total: "$28.5M"
last_funding: "Series A, January 2025 ($20M, led by SignalFire)"
deployment: [saas, api]
target_customer: enterprise / regulated (banking, financial services, insurance)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [non-human-identity, secrets, nhi, zero-trust, agentic]
---

# Clutch Security

> **One-liner** — A non-human identity security platform that discovers, secures, and applies Zero Trust lifecycle controls to every API key, secret, service account, token, and AI agent across an environment.

**Categories** — [non-human-identity](../categories/non-human-identity.md) (primary)

## What it does
Clutch secures the credentials and machine identities that power cloud infrastructure, CI/CD pipelines, and AI systems — API keys, secrets, service accounts, tokens, certificates. It discovers and inventories NHIs, assesses posture/risk, applies Zero Trust verification, and provides threat detection and response, plus AI-agent guardrails and shadow-AI discovery. Its differentiating philosophy is replacing periodic secret *rotation* with real-time dynamic controls and ephemeral identities ("Zero Trust for NHIs").

## Where it sits in the stack
Foundation layer, [non-human-identity](../categories/non-human-identity.md). Overlaps with [secrets-management](../categories/secrets-management.md) but positions as a security/governance layer over secrets rather than a vault. Lethal-trifecta role: constrains the **egress / action** leg (what a machine identity or agent can reach and do) and protects the **sensitive-data** leg by finding and locking down over-privileged or exposed credentials.

## Deployment & architecture
SaaS, cloud-agnostic — connects "to wherever your Identities, Agents, and Secrets live" via API/read integrations across cloud, CI/CD, and SaaS. Emphasis on ephemeral, dynamically-issued identities over static long-lived secrets.

## Positioning & differentiators
Clutch's hook is the Zero Trust / ephemeral-identity framing — moving past rotation toward short-lived, dynamically-verified credentials — plus explicit AI-agent guardrails. Nearest neighbors are [entro-security](entro-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), and [astrix-security](astrix-security.md). Versus [entro-security](entro-security.md) (secrets-lifecycle / vaulting + rotation), Clutch leans into Zero Trust verification and ephemeral identities; versus MCP-native brokers like [natoma](natoma.md) it governs the identity/secret rather than the MCP tool call. Targets BFSI and tech.

## Ownership, funding & M&A
- **Independent, VC-backed.** Founded October 2023; HQ Tel Aviv, Israel. Co-founder/CEO Ofir Har-Chen (co-founders Sagi Haas and Tal Kimhi).
- **Funding:** $20M Series A (announced January 2025, led by SignalFire; with Lightspeed Venture Partners and Merlin Ventures), bringing **total funding to $28.5M**.
- **M&A:** No acquisition flag in the seed and none found as of 2026-06-28 — remains independent (high confidence on independence).

## CTO / hedge-fund lens
Day-2. Most relevant for a fund with significant cloud/CI-CD footprint and growing agentic-AI use that wants to move off static, long-lived service-account keys toward Zero Trust/ephemeral credentials. Clutch explicitly targets banking/financial services/insurance, so the messaging maps to a regulated buyer; the AI-agent guardrail angle is forward-looking but newer. No direct SR 11-7 role; supports access-control and operational-risk posture. For a small fund on managed cloud secret managers it is optional until NHI sprawl and agent credentials become a real exposure.

## Competitors / alternatives
[entro-security](entro-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), [astrix-security](astrix-security.md), [silverfort](silverfort.md); vaults: [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md); agent/MCP governance: [natoma](natoma.md).

## Open questions / to verify
- Customer count / production references (only sector targeting found).
- Maturity and scope of the AI-agent guardrail capabilities vs. core NHI product.
- Any funding since the January 2025 Series A.

## Sources
- [Clutch Security Raises $20M Series A](https://www.clutch.security/blog/clutch-security-20M-series-a) — fetched 2026-06-28 — supports: $20M Series A (SignalFire), $28.5M total, founder, product scope, target sectors; confidence: med (vendor blog)
- Web search (TechCrunch, SecurityWeek, Calcalist) — fetched 2026-06-28 — supports: founded Oct 2023, Tel Aviv HQ, $28.5M total, co-founders; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded Oct 2023, Tel Aviv HQ, CEO Ofir Har-Chen, $28.5M total funding ($20M Series A Jan 2025, SignalFire). No M&A — confirmed independent (high confidence). Zero Trust / ephemeral NHI positioning with AI-agent guardrails; hedge_fund_fit medium.
