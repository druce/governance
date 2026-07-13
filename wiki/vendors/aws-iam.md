---
title: AWS IAM / Identity Center
type: vendor
name: AWS IAM / Identity Center
slug: aws-iam
aka: [AWS Identity and Access Management, AWS IAM Identity Center, AWS SSO]
primary_category: identity-access
also_listed_in: []
website: https://aws.amazon.com/iam/
founded: null
hq: Seattle, Washington, USA
ownership_state: public
owner: Amazon (AWS)
ownership_note: 'Product of Amazon Web Services (Amazon, NASDAQ: AMZN)'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: null
last_verified: 2026-07-13
verify_after: null
tags: [idp, iam, sso, aws, cloud-iam]
---

# AWS IAM / Identity Center

> Stub scaffolded from survey-v2.csv row (General Identity, listed as "AWS"). Unverified — fill via wiki-research.

**One-liner** — AWS's native identity layer: IAM for cloud-resource permissions (users, roles, policies) plus IAM Identity Center (ex-AWS SSO) for workforce single sign-on into AWS accounts and apps.

**What it does** — TBD: IAM governs programmatic/console access to AWS resources via roles and policies; IAM Identity Center adds workforce SSO across multiple AWS accounts and SAML apps. It is cloud IAM more than a general-purpose corporate IdP — most shops federate it *from* an IdP ([microsoft-entra](microsoft-entra.md), [okta](okta.md)) rather than use it as the front door.

**Naming / provenance** — CSV row says just "AWS"; scoped here to IAM + IAM Identity Center as the identity shopping unit (parallel to [aws-secrets-manager](aws-secrets-manager.md) for the secrets slot).

**Ownership & viability** — Product of Amazon Web Services (Amazon, public). No standalone viability question.

**Positioning & differentiators** — TBD: default and unavoidable for AWS-resource access; IAM roles are also the de facto identity for AWS-hosted workloads/agents, which touches [non-human-identity](../categories/non-human-identity.md).

**Who should choose them / anti-fit** — TBD: every AWS shop uses IAM by definition; the survey question is whether anyone treats it as their *primary* workforce IdP.

**Known weaknesses / gotchas** — TBD.

**Deployment & data handling** — SaaS (AWS control plane); details TBD.

**Integrations & partnerships** — TBD: SAML/OIDC federation, external IdP integration, agent/workload roles.

**Compliance & FS traction** — TBD (AWS itself carries the usual attestations; specifics unverified here).

**Commercial** — TBD: IAM and Identity Center are no-additional-charge AWS features.

## Open questions

- Everything above marked TBD is unverified — fill via wiki-research, never guess.
- Survey-design: is "AWS" as a General Identity option measuring cloud IAM usage (near-universal for AWS shops) or primary-IdP choice (rare)? Consider clarifying the option label.

## Sources

<!-- - [title](url) — fetched YYYY-MM-DD — supports: <claim>; confidence: high/med/low -->

## History

- [2026-07-13] Page scaffolded from survey-v2.csv row (added by human, no page existed) via wiki-create; scoped "AWS" to IAM / IAM Identity Center.
