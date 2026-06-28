---
title: Infisical
type: vendor
name: Infisical
slug: infisical
categories: [secrets-management]
layer: foundation
aliases: []
website: "https://infisical.com/"
founded: 2022
hq: San Francisco, CA
ownership: independent
ownership_detail: Private, VC-backed (Y Combinator W23). $16M Series A led by Elad Gil (reported ~2025).
ownership_confidence: high
funding_total: ~$19M (incl. $16M Series A)
last_funding: Series A, $16M, ~2025 (led by Elad Gil)
deployment: [saas, self-hosted, api, sdk]
target_customer: mid-market / enterprise (developer/platform teams)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, open-source, self-hosted, developer-first, certificates, pam]
---

# Infisical

> **Researched 2026-06-28.** Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — The open-source, self-hostable secrets manager — an end-to-end-encrypted alternative to Doppler and cloud-only stores that also reaches into certificates and privileged access, increasingly pitched for AI agents.

## What it does
Infisical centralizes secrets, app config, and credentials and injects them into dev workflows, CI/CD pipelines, and cloud infrastructure instead of leaving them in `.env` files or code. It adds secrets versioning, point-in-time recovery, audit logging, and automatic rotation, and has expanded toward certificate management and privileged access management. The differentiator is the **open-source core** with a **self-hosted, end-to-end-encrypted** deployment option, for teams that don't want a third party holding their secrets.

## Where it sits in the stack
Foundation layer, [secrets-management](../categories/secrets-management.md), at the developer-workflow end. Lethal-trifecta leg: **sensitive-data** — keeps secrets out of code, repos, and prompts. Its newer secrets-for-agents framing makes it relevant to agentic/[non-human-identity](../categories/non-human-identity.md) deployments, though the core job is classic app/CI secrets.

## Deployment & architecture
Available as managed SaaS **or** self-hosted (the draw for regulated/air-gapped shops); web UI, CLI, SDKs, Kubernetes operator, and broad platform integrations. Large open-source footprint (tens of millions of downloads claimed; very active GitHub repo). End-to-end encryption.

## Positioning & differentiators
The open-source challenger to [doppler](doppler.md) (SaaS) and a lighter-weight alternative to [hashicorp-vault](hashicorp-vault.md) for teams that find Vault heavy. Versus the hyperscaler stores ([aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md), [gcp-secret-manager](gcp-secret-manager.md)) it is cloud-agnostic and self-hostable. Versus [1password](1password.md) it is purely developer/machine secrets (no human-password-manager/device-trust side). Self-hosting + OSS transparency are the key buying reasons.

## Ownership, funding & M&A
Independent, private, VC-backed. Founded 2022 by Vlad Matsiiako (CEO), Tony Dang, and Maidul Islam; HQ San Francisco; Y Combinator W23. $16M Series A led by Elad Gil (reported ~2025), with Y Combinator, Gradient, Dynamic Fund, and angels (Datadog CEO Olivier Pomel, Samsara CEO Sanjit Biswas). No M&A. Confidence high (founding/founders/round); exact Series A date approximate.

## CTO / hedge-fund lens
Day-1 *if* you want a cloud-agnostic or self-hosted secrets manager and value open-source auditability — the self-hosting option is the standout for a regulated fund that doesn't want secrets sitting in a third-party SaaS. If you're single-cloud, the native manager is usually simpler. Diligence: maturity of the self-hosted deployment you'll operate, support model, and whether the OSS vs paid feature split covers what you need. Not a model-risk (SR 11-7) tool.

## Competitors / alternatives
[doppler](doppler.md), [hashicorp-vault](hashicorp-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md), [gcp-secret-manager](gcp-secret-manager.md), [1password](1password.md), [conjur](conjur.md) (CyberArk).

## Open questions / to verify
- Exact Series A close date and total raised to date.
- OSS-vs-enterprise feature boundary (which controls require the paid tier).
- Production references / scale in financial services.

## Sources
- [Infisical (Y Combinator profile)](https://www.ycombinator.com/companies/infisical) — fetched 2026-06-28 — supports: founders, founding year, YC batch, open-source secrets/cert/PAM scope; confidence: high.
- [Open-Source Infisical Secures $16M Series A (CTOL)](https://www.ctol.digital/news/open-source-infisical-secures-16m-series-a-funding-enterprise-secrets-management/) — fetched 2026-06-28 (search snapshot; page 403 on direct fetch) — supports: $16M Series A, Elad Gil lead, investors; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent VC-backed (YC W23), founded 2022 SF by Matsiiako/Dang/Islam, $16M Series A led by Elad Gil. Open-source/self-hostable challenger to Doppler. Set ownership independent, trifecta=sensitive-data, confidence high.
