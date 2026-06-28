---
type: vendor
name: GCP Secret Manager
slug: gcp-secret-manager
categories: [secrets-management]
layer: foundation
aliases: [Google Cloud Secret Manager, Secret Manager]
website: https://cloud.google.com/secret-manager
founded: 2020
hq: Mountain View, CA
ownership: public
ownership_detail: First-party Google Cloud service. Alphabet Inc. / Google LLC (NASDAQ: GOOGL).
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise (any Google Cloud customer)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, iam, cmek, rotation, google-cloud, first-party-cloud]
---

# GCP Secret Manager

> **Researched 2026-06-28 (light — well-known first-party cloud service).** Primary category: [[secrets-management]].

**One-liner** — Google Cloud's managed service for storing API keys, passwords, certificates, and other sensitive data as versioned secrets, with IAM-based access control — the default vault if you run on Google Cloud.

## What it does
Central place to store secrets as named objects with immutable, versioned payloads, so apps fetch them at runtime instead of embedding them in code or config. Access is governed by Google Cloud IAM at the project or per-secret level; every access is logged via Cloud Audit Logs; secrets can be encrypted with customer-managed keys (CMEK). It supports rotation schedules with Pub/Sub notifications and regional or automatic (multi-region) replication. Workloads authenticate via Google Cloud service accounts / Workload Identity, avoiding a bootstrap secret.

## Where it sits in the stack
Foundation layer, [[secrets-management]] — the Google-Cloud-native building block, the counterpart of Cloud IAM (identity) and Cloud KMS (encryption). Lethal-trifecta role: none directly; it is plumbing that keeps long-lived credentials out of code, prompts, and repos.

## Deployment & architecture
Fully managed, multi-tenant service within Google Cloud, accessed via API/SDK/CLI/Terraform. IAM for access; Cloud KMS/CMEK for encryption; Cloud Audit Logs for audit; Pub/Sub for rotation events. Versioning with explicit enable/disable/destroy of versions. (Note: rotation here means scheduled notifications/automation hooks rather than the fully-managed DB-credential rotation AWS offers out of the box.)

## Positioning & differentiators
The default on Google Cloud: minimal setup, native IAM/Workload Identity, simple versioning. Direct analogue of [[azure-key-vault]] and [[aws-secrets-manager]] (+ KMS) on the other clouds. Versus [[hashicorp-vault]] it is simpler and managed but GCP-bound and lighter on dynamic secrets / advanced policy. Versus developer SaaS ([[doppler]], [[infisical]], [[1password]]) it is infra-centric, not developer-workflow-centric.

## Ownership, funding & M&A
First-party Google Cloud service, GA since 2020. Owner: Google LLC / Alphabet Inc. (public, NASDAQ: GOOGL). No M&A question. Confidence high.

## CTO / hedge-fund lens
Day-1 if you run anything on Google Cloud. For a fund whose workloads sit in GCP (or who use Vertex AI / Gemini), this is the natural secrets manager — IAM-integrated, audited, cheap. Not a model-risk (SR 11-7) tool, but secret hygiene is table-stakes for any AI deployment. Most funds will pick whichever of the three hyperscaler managers matches their primary cloud rather than run a separate tool.

## Competitors / alternatives
[[azure-key-vault]], [[aws-secrets-manager]], [[hashicorp-vault]], [[conjur]] (CyberArk), [[1password]], [[doppler]], [[infisical]].

## Open questions / to verify
- None material — first-party, well-documented.

## Sources
- [Secret Manager overview (Google Cloud docs)](https://cloud.google.com/secret-manager/docs/overview) — fetched 2026-06-28 — supports: what it stores, IAM/CMEK/audit/rotation/versioning model; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed first-party Google Cloud service, ownership public (GOOGL), one-liner, IAM/CMEK/versioning/rotation model. ownership set public, confidence high.
