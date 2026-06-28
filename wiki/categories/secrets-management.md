---
title: Secrets Manager
type: category
name: Secrets Manager
slug: secrets-management
layer: foundation
priority: day-1
trifecta_role: sensitive-data (protects the credentials that unlock sensitive systems and data)
maps_to_seed_doc: Secrets Manager
maps_to_seed_csv: Secrets Manager
vendor_count: 8
status: drafted
last_updated: 2026-06-28
---

## Business objective

A secrets manager is the locked drawer for passwords, API keys, database credentials, and certificates. It stores them centrally, controls who/what can read them, rotates them without breaking production, and gives an audit trail — so credentials never end up hardcoded in a repo, baked into a container image, or pasted into an agent's config.

The seed metaphor is exactly right: the locked drawer, with a record of who opened it. In the agent era this matters more, not less — every agent and workload that needs to authenticate somewhere needs a credential, and those credentials should be vaulted, scoped, and short-lived rather than long-lived secrets floating around.

## When you need it

Day-1, required. Any firm running code, cloud infrastructure, or AI agents has secrets to manage; the only question is whether they are vaulted or scattered. For most shops the slot is already filled by the cloud-native option that ships with their platform (Key Vault on Azure, Secrets Manager on AWS, Secret Manager on GCP). The AI-era upgrade is rotation discipline and making sure agents pull short-lived secrets from the vault rather than holding standing keys.

## Lethal-trifecta role

The sensitive-data leg, at its root. Secrets are the keys to sensitive data and systems; a leaked credential is often the first domino in an exfiltration chain. Vaulting + rotation + scoping shrinks that exposure. Lives across all zones — anything that authenticates needs the drawer.

## Vendors

Cloud-native (usually already owned, bundled with the platform):

- [azure-key-vault](../vendors/azure-key-vault.md) — Microsoft's managed secrets/key store; default for Azure/M365 shops.
- [aws-secrets-manager](../vendors/aws-secrets-manager.md) — AWS-native secrets store with built-in rotation.
- [gcp-secret-manager](../vendors/gcp-secret-manager.md) — Google Cloud's managed secrets store.

Platform / enterprise:

- [hashicorp-vault](../vendors/hashicorp-vault.md) — the cross-cloud incumbent; broad secrets, dynamic secrets, and encryption-as-a-service (per seed, acquired by IBM).
- [conjur](../vendors/conjur.md) — CyberArk Conjur; secrets management for apps/DevOps, tied to the CyberArk PAM estate.

Developer-friendly / modern:

- [1password](../vendors/1password.md) — secrets management extending from the password-manager franchise into developer/infrastructure secrets.
- [doppler](../vendors/doppler.md) — developer-centric secrets platform (SecretOps) with environment syncing.
- [infisical](../vendors/infisical.md) — open-source-rooted secrets management platform.

Cross-listed (secrets sit adjacent to NHI): [cyberark](../vendors/cyberark.md), [entro-security](../vendors/entro-security.md).

## Consolidation / M&A dynamics

- HashiCorp Vault — per seed, acquired by IBM (per seed; unverified — to confirm in research).
- CyberArk Conjur — part of CyberArk, which per seed was acquired by Palo Alto Networks (per seed; unverified — to confirm in research).

The independents are consolidating into platform owners (IBM, Palo Alto), while the cloud providers' bundled offerings keep most enterprises from buying a third-party tool at all. The developer-friendly tier (1Password/Doppler/Infisical) competes on DX rather than enterprise governance.

## Adjacent categories

- [non-human-identity](non-human-identity.md) — NHI governs *which workload/agent* gets a credential; secrets management stores and rotates the credential itself. Heavy overlap (Entro, CyberArk span both).
- [identity-access](identity-access.md) — human/agent identity; complementary to machine credentials.
- [policy-as-code](policy-as-code.md) — Vault pairs with policy tooling; HashiCorp spans both.
- [ephemeral-environments](ephemeral-environments.md) — short-lived environments pull short-lived secrets.

## Survey

**Question.** Which secrets manager(s) is your firm currently using or evaluating?

**Answer options.** Azure Key Vault; HashiCorp Vault; AWS Secrets Manager; GCP Secret Manager; CyberArk Conjur; 1Password; Doppler; Infisical; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Cloud-native options (Key Vault, AWS, GCP) are table-stakes and will dominate; most firms use whatever ships with their cloud, so expect multi-select with a clear primary. The seed bundled "1Password / Doppler / Infisical" as one option — split here, but they serve a similar developer-secrets niche and may confuse respondents who lump them. HashiCorp→IBM and Conjur/CyberArk→Palo Alto (per seed) date those options. Ask whether secrets rotation is actually automated — ownership ≠ good hygiene.

## Open taxonomy questions

- Overlap with [non-human-identity](non-human-identity.md) is significant — Entro and CyberArk straddle both; confirm where vaulting ends and NHI governance begins.
- Whether to treat cloud-native and dedicated/enterprise secrets managers as one survey question or split them.
