---
type: vendor
name: Azure Key Vault
slug: azure-key-vault
categories: [secrets-management]
layer: foundation
aliases: [Key Vault, Azure Managed HSM]
website: "https://azure.microsoft.com/products/key-vault"
founded: 2015
hq: Redmond, WA
ownership: public
ownership_detail: "First-party Microsoft Azure service. Microsoft Corporation (NASDAQ: MSFT)."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise (any Azure customer)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, hsm, kms, certificates, microsoft, first-party-cloud]
---

# Azure Key Vault

> **Researched 2026-06-28 (light — well-known first-party cloud service).** Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — Microsoft's official wording: "a secure secrets store, providing management for secrets, keys, and certificates, all backed by Hardware Security Modules" — the default vault if you run on Azure.

## What it does
One managed service covering three jobs: secrets management (tokens, passwords, connection strings, API keys), key management (creating/controlling encryption keys, e.g. for disk/database encryption), and certificate management (provision/renew TLS/SSL certs). Apps fetch secrets at runtime by URI instead of hard-coding them. Standard tier uses FIPS 140 Level 1 software crypto; Premium tier provides HSM-protected keys on FIPS 140-3 Level 3 HSMs. (A separate Managed HSM offering gives single-tenant, dedicated HSMs.)

## Where it sits in the stack
Foundation layer, [secrets-management](../categories/secrets-management.md) — the Azure-native building block. Authentication is via [microsoft-entra](microsoft-entra.md); authorization via Azure RBAC or vault access policies, and apps authenticate using Entra **managed identities** (no secret-zero problem). Lethal-trifecta role: none directly; it is plumbing that keeps credentials out of code and out of prompts/repos, reducing the chance an agent or RAG pipeline can leak a long-lived secret.

## Deployment & architecture
Fully managed, multi-tenant SaaS within Azure, accessed via REST API / SDKs / CLI. Native integration with managed identities, Azure services (Disk Encryption, SQL TDE/Always Encrypted, App Service), and logging to Azure Monitor / Event Hubs. Microsoft states it is designed so Microsoft cannot see or extract your data.

## Positioning & differentiators
The path of least resistance on Azure: zero infrastructure, deep Entra integration, per-app vault isolation. Versus [hashicorp-vault](hashicorp-vault.md) it is simpler but Azure-bound and less feature-rich for dynamic secrets / multi-cloud / fine-grained policy. Mirrors [aws-secrets-manager](aws-secrets-manager.md) + AWS KMS and [gcp-secret-manager](gcp-secret-manager.md) on the other clouds. Versus developer SaaS tools ([doppler](doppler.md), [infisical](infisical.md), [1password](1password.md)) it is cloud-infra-centric rather than developer-workflow-centric.

## Ownership, funding & M&A
First-party Microsoft service, GA since 2015. Owner: Microsoft Corporation (public, NASDAQ: MSFT). No M&A question. Confidence high.

## CTO / hedge-fund lens
Day-1 if you run anything on Azure — there is no reason to hand-roll secret storage. Cheap, audited (broad compliance coverage), and the natural counterpart to Entra-based identity. For a fund already standardized on Microsoft 365 / Entra, this is effectively the default secrets manager. Not a model-risk (SR 11-7) tool, but keeping secrets out of code/prompts is table-stakes hygiene for any AI deployment.

## Competitors / alternatives
[aws-secrets-manager](aws-secrets-manager.md), [gcp-secret-manager](gcp-secret-manager.md), [hashicorp-vault](hashicorp-vault.md), [conjur](conjur.md) (CyberArk), [1password](1password.md), [doppler](doppler.md), [infisical](infisical.md).

## Open questions / to verify
- None material — first-party, well-documented.

## Sources
- [Azure Key Vault Overview (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) — fetched 2026-06-28 — supports: official description, tiers/HSM, Entra/RBAC auth model; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed first-party Microsoft Azure service, ownership public (MSFT), official one-liner, Entra/managed-identity integration. ownership set public, confidence high.
