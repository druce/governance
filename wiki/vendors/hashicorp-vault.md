---
title: HashiCorp Vault
type: vendor
name: HashiCorp Vault
slug: hashicorp-vault
aka: [Vault, HCP Vault]
primary_category: secrets-management
also_listed_in: [policy-as-code]
website: https://www.hashicorp.com/products/vault
founded: 2012
hq: San Francisco, USA
ownership_state: acquired-closed
owner: IBM
ownership_note: HashiCorp acquired by IBM for $6.4B ($35/share); announced 2024-04-24, closed 2025-02-27. Vault is the secrets-management product within IBM.
acquisition: {announced: 2024-04-24, closed: 2025-02-27, price: null}
funding_total: 'n/a (was public, Nasdaq: HCP, before IBM)'
last_funding: IPO Dec 2021
market_position: null
deployment_model: [self-hosted, saas, on-prem]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated / platform & DevOps teams
last_verified: 2026-06-28
verify_after: null
tags: [secrets-management, vault, pki, encryption, ibm, hashicorp]
---

# HashiCorp Vault

> **One-liner** — The de facto open-source-rooted secrets manager: central vault for API keys, DB creds, certificates and encryption keys, with dynamic short-lived secrets — now an IBM company.

**Categories** — [secrets-management](../categories/secrets-management.md) (primary), [policy-as-code](../categories/policy-as-code.md)

## What it does
Vault stores and brokers secrets (API keys, database credentials, tokens, certificates) and provides encryption-as-a-service, dynamic secrets (generated on demand, auto-expiring), secret leasing/rotation, and PKI/certificate issuance. The point is to get long-lived credentials out of code, config files and CI logs, and to give every human/workload identity-scoped, audited, time-bound access to secrets. Critical plumbing for any AI/agent system that needs to hold credentials without hard-coding them.

## Where it sits in the stack
Foundation layer, [secrets-management](../categories/secrets-management.md). Lethal-trifecta leg: **sensitive-data** — it controls the credentials that gate access to sensitive systems, shrinking blast radius via short-lived secrets. Adjacent to [policy-as-code](../categories/policy-as-code.md) via sibling product **HashiCorp Sentinel** (see [hashicorp-sentinel](hashicorp-sentinel.md)) and to non-human identity ([non-human-identity](../categories/non-human-identity.md)) for workload/agent auth.

## Deployment & architecture
Self-managed (open source + Enterprise) or managed **HCP Vault** SaaS. API-driven; integrates with cloud KMS, Kubernetes, IdPs, databases, PKI, and CI/CD. Auth via multiple methods (cloud IAM, OIDC, AppRole, Kubernetes service accounts) — relevant for giving agents/workloads secretless or short-lived access.

## Positioning & differentiators
The category reference point, known for the open-source core, dynamic secrets and broad ecosystem. Nearest neighbors: cloud-native managers [azure-key-vault](azure-key-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [gcp-secret-manager](gcp-secret-manager.md) (simpler, locked to one cloud), [conjur](conjur.md) (CyberArk), and developer-secrets tools [1password](1password.md), [doppler](doppler.md), [infisical](infisical.md). Vault's edge is multi-cloud neutrality + dynamic secrets; its cost is operational complexity to run well.

## Ownership, funding & M&A
**Verified.** HashiCorp was **acquired by IBM** for **$35.00/share, $6.4B enterprise value** — announced **2024-04-24**, **closed 2025-02-27** after ~10 months of regulatory review (US FTC and UK CMA both cleared). HashiCorp was previously public (Nasdaq: HCP, IPO Dec 2021); founded 2012 by Mitchell Hashimoto and Armon Dadgar; HQ San Francisco. Vault is now IBM's secrets-management product line. Ownership confidence **high**.

## CTO / hedge-fund lens
**Day-1.** A secrets manager is table-stakes before any AI/agent work touches credentials; Vault is the vendor-neutral default if you span multiple clouds or want dynamic secrets. For a smaller fund mostly on one cloud, the native manager ([azure-key-vault](azure-key-vault.md) etc.) may be enough and lower-effort. IBM ownership generally adds enterprise support/continuity but watch licensing changes (HashiCorp moved the core from MPL to the BSL/Business Source License in 2023). Relevant to model-risk/audit as the system of record for credential access.

## Competitors / alternatives
[azure-key-vault](azure-key-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [gcp-secret-manager](gcp-secret-manager.md), [conjur](conjur.md), [cyberark](cyberark.md), [1password](1password.md), [doppler](doppler.md), [infisical](infisical.md).

## Open questions / to verify
- Post-IBM roadmap/licensing for Vault OSS vs Enterprise vs HCP.
- Degree of integration with IBM/Red Hat identity and the CyberArk-style NHI space.

## Sources
- [IBM to Acquire HashiCorp (IBM newsroom)](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) — fetched 2026-06-28 — supports: $6.4B/$35 share, product list incl. Vault; confidence: high
- [IBM closes $6.4B HashiCorp acquisition (TechCrunch)](https://techcrunch.com/2025/02/27/ibm-closes-6-4b-hashicorp-acquisition/) — fetched 2026-06-28 — supports: close date 2025-02-27, regulatory review; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified IBM acquisition ($6.4B, closed 2025-02-27), set ownership subsidiary, confidence low→high; filled founding/HQ/product detail. Noted Sentinel sibling for policy-as-code.
