---
type: vendor
name: 1Password
slug: 1password
categories: [secrets-management]
layer: foundation
aliases: [AgileBits, 1Password Extended Access Management]
website: https://1password.com/
founded: 2005
hq: Toronto, Canada
ownership: independent
ownership_detail: Private, VC-backed (legal entity AgileBits Inc.). ~$920M raised; Series C $620M at $6.8B valuation (Jan 2022). Acquirer of Apono (2026-06-15, reported $250M-$300M).
ownership_confidence: high
funding_total: ~$920M
last_funding: Series C, $620M, 2022-01 (at $6.8B valuation)
deployment: [saas, sdk, api]
target_customer: enterprise / mid-market / SMB
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, password-manager, extended-access-management, device-trust, acquirer]
---

# 1Password

> **Researched 2026-06-28.** Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — The password manager that grew into an enterprise "Extended Access Management" platform — vaulting human credentials, passkeys, and developer secrets, and (post-Apono) governing just-in-time access for people, machines, and AI agents.

## What it does
1Password started as a consumer/business password manager (the AgileBits product) and is now pitched to enterprises as **Extended Access Management**: securing the credentials, passkeys, SSH keys, and developer secrets that flow through unmanaged apps and devices that traditional IAM/MDM doesn't cover. For engineering teams it offers a **Secrets Automation / Developer** product — a vault plus CLI, SDKs, and CI/CD integrations to inject secrets at runtime instead of hard-coding them — which is why it sits in [secrets-management](../categories/secrets-management.md). With the 2026 Apono acquisition it is moving toward just-in-time, auto-revoked access governance and a "Credential Broker" that releases short-lived credentials on demand.

## Where it sits in the stack
Foundation layer, [secrets-management](../categories/secrets-management.md), with adjacencies into device-trust / access management (Kolide) and now privileged/just-in-time access (Apono). Lethal-trifecta leg: **sensitive-data** — its job is to keep credentials out of code, browsers, prompts, and repos. Complements the IdP ([microsoft-entra](microsoft-entra.md), [okta](okta.md)) rather than replacing it.

## Deployment & architecture
SaaS, end-to-end (zero-knowledge) encrypted vaults, with the famous secret-key + master-password model. For developers: CLI, SDKs, Connect/Service Accounts, and integrations with CI/CD and cloud. Device-trust checks via the former Kolide product. The forthcoming **1Password Credential Broker** (private beta) brokers short-lived credentials, beginning with GitHub Actions workload identity.

## Positioning & differentiators
Best known for human credential management and ease of use, then for "managing the unmanaged" (devices/apps outside MDM/SSO). In pure machine/CI secrets it overlaps with [doppler](doppler.md) and [infisical](infisical.md) but is less developer-infra-native than they are; its strength is the human + device + secret bundle. The Apono deal pushes it toward access governance / NHI territory adjacent to [cyberark](cyberark.md) and [silverfort](silverfort.md).

## Ownership, funding & M&A
Independent and private. Founded 2005 (legal entity AgileBits Inc.), HQ Toronto. ~$920M raised; the $620M Series C (Jan 2022) was at a $6.8B valuation, led by ICONIQ Growth — the largest venture round by a Canadian company at the time. 2024 revenue ~$318M ARR.
**Acquirer**, not acquired:
- **Apono** — just-in-time/privileged access governance for humans, machines, and AI agents — announced **2026-06-15**, reported $250M-$300M (Calcalist; other sources >$200M). Confirmed via 1Password press + Busin​essWire.
- Earlier: **Kolide** (device trust, Feb 2024), **Trelica** (SaaS access management, UK), **Passage** (passkeys, 2022).
Confidence high.

## CTO / hedge-fund lens
Day-1 as a **human** credential/password manager — many funds already run it, and it is an easy, well-regarded baseline. As a **machine/CI secrets manager** it is optional: if your workloads live in one cloud, the native manager ([aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md), [gcp-secret-manager](gcp-secret-manager.md)) is usually the simpler choice; 1Password shines when you want one tool spanning humans, devices, and some developer secrets. Watch the Apono integration — JIT access for AI agents is genuinely relevant to agentic deployments. Not a model-risk (SR 11-7) tool.

## Competitors / alternatives
[doppler](doppler.md), [infisical](infisical.md), [azure-key-vault](azure-key-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [gcp-secret-manager](gcp-secret-manager.md), [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md) (for the access-governance direction).

## Open questions / to verify
- Apono integration timeline and how "Credential Broker" maps onto existing Secrets Automation.
- Current valuation/ARR (latest public figure is the 2022 $6.8B round + ~$318M 2024 ARR).

## Sources
- [1Password Unlocks $620M Round, $6.8B Valuation (Crunchbase News)](https://news.crunchbase.com/venture/1password-620m-round-cybersecurity-investor/) — fetched 2026-06-28 — supports: funding, valuation, founding/HQ, B2B direction; confidence: high.
- [1Password Acquires Apono (1Password press)](https://1password.com/press/2026/june/1password-acquires-apono) — fetched 2026-06-28 — supports: Apono acquisition, JIT access / agent governance, Credential Broker; confidence: high.
- [1Password Acquires Apono in Reported $250M-$300M Deal (SecurityWeek)](https://www.securityweek.com/1password-acquires-apono-in-reported-250m-300m-deal/) — fetched 2026-06-28 — supports: reported deal value; confidence: med (price reported, not officially disclosed).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent/private (AgileBits), founded 2005 Toronto, ~$920M raised / $6.8B (2022). Established it is an ACQUIRER — Apono (2026-06-15, reported $250M-$300M), plus Kolide/Trelica/Passage. Set ownership independent, trifecta=sensitive-data, confidence high.
