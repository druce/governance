---
type: vendor
name: AWS Secrets Manager
slug: aws-secrets-manager
categories: [secrets-management]
layer: foundation
aliases: [Secrets Manager]
website: https://aws.amazon.com/secrets-manager/
founded: 2018
hq: Seattle, WA
ownership: public
ownership_detail: First-party AWS service. Amazon.com, Inc. (NASDAQ: AMZN).
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise (any AWS customer)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, rotation, iam, kms, aws, first-party-cloud]
---

# AWS Secrets Manager

> **Researched 2026-06-28 (light — well-known first-party cloud service).** Primary category: [[secrets-management]].

**One-liner** — AWS's official wording: it "helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles" — the default secrets store if you run on AWS.

## What it does
Replaces hard-coded credentials with a runtime API call: your app asks Secrets Manager for the secret when it needs it, so credentials never live in source code or config. Its signature feature is **built-in automatic rotation** (via Lambda) — including native rotation for RDS/Aurora and other databases — so you can move from long-lived to short-lived secrets without redeploying apps. Access is governed by IAM policies; secrets are encrypted with AWS KMS; all access is auditable via CloudTrail. (AWS positions IAM for AWS credentials, KMS for encryption keys, and ACM for certificates — Secrets Manager is for application/DB secrets.)

## Where it sits in the stack
Foundation layer, [[secrets-management]] — the AWS-native building block. Tightly coupled to IAM (identity), KMS (encryption), and CloudTrail (audit). Lethal-trifecta role: none directly; it is plumbing that keeps secrets out of code, agents, and repos, lowering the chance an AI pipeline leaks a long-lived credential.

## Deployment & architecture
Fully managed, multi-tenant service within AWS, accessed via API/SDK/CLI. IAM resource policies for fine-grained access; KMS for encryption; Lambda rotation functions; native integrations across AWS data services. Note a common cost nuance: it bills per secret per month plus per API call (cheaper, no-rotation alternative for static config is SSM Parameter Store).

## Positioning & differentiators
The default on AWS, especially where automatic DB-credential rotation matters. Versus [[hashicorp-vault]] it is simpler and managed but AWS-bound and less capable for multi-cloud / dynamic secrets / advanced policy. Direct analogue of [[azure-key-vault]] (+ KMS) and [[gcp-secret-manager]]. Versus developer SaaS ([[doppler]], [[infisical]], [[1password]]) it is infra-centric, not developer-workflow-centric.

## Ownership, funding & M&A
First-party AWS service, launched 2018. Owner: Amazon.com, Inc. (public, NASDAQ: AMZN). No M&A question. Confidence high.

## CTO / hedge-fund lens
Day-1 if you run anything on AWS. The automatic rotation story is the standout for regulated shops (rotating DB creds without downtime supports audit and reduces standing-secret risk). For a fund whose stack lives in AWS, this is the natural secrets manager. Not a model-risk (SR 11-7) tool, but secret hygiene is table-stakes for any AI deployment.

## Competitors / alternatives
[[azure-key-vault]], [[gcp-secret-manager]], [[hashicorp-vault]], [[conjur]] (CyberArk), [[1password]], [[doppler]], [[infisical]].

## Open questions / to verify
- None material — first-party, well-documented.

## Sources
- [What is AWS Secrets Manager? (AWS docs)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) — fetched 2026-06-28 — supports: official description, rotation, IAM/KMS/CloudTrail model; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed first-party AWS service, ownership public (AMZN), official one-liner, rotation/IAM/KMS model. ownership set public, confidence high.
