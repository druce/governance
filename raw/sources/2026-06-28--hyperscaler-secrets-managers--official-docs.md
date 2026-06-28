# Hyperscaler first-party secrets managers — official docs

- URLs:
  - Azure Key Vault: https://learn.microsoft.com/en-us/azure/key-vault/general/overview
  - AWS Secrets Manager: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
  - GCP Secret Manager: https://cloud.google.com/secret-manager/docs/overview
- Fetched: 2026-06-28
- Good for: official one-liners + ownership (first-party cloud services). Ownership = the hyperscaler; all public companies.

## Azure Key Vault (Microsoft)
Official: "Azure Key Vault is a secure secrets store, providing management for secrets, keys, and certificates, all backed by Hardware Security Modules." Three jobs: Secrets Management (tokens, passwords, certs, API keys), Key Management (encryption keys), Certificate Management (TLS/SSL). Two tiers: Standard (FIPS 140 L1 software) and Premium (HSM-backed, FIPS 140-3 L3 Marvell LiquidSecurity HSMs). Auth via Microsoft Entra ID; authz via Azure RBAC or vault access policy. Microsoft cannot see/extract your data. Owner: Microsoft (public, NASDAQ: MSFT).

## AWS Secrets Manager (Amazon)
Official: "AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles." Removes hard-coded credentials; runtime retrieval; built-in automatic rotation via Lambda; IAM-based access control; CloudTrail audit; KMS encryption. (For AWS creds use IAM, for encryption keys use KMS, for certs use ACM.) Owner: Amazon / AWS (public, NASDAQ: AMZN).

## GCP Secret Manager (Google)
Stores API keys, passwords, certificates, and other sensitive data as secrets with versioning. IAM-integrated access control, audit logging via Cloud Audit Logs, CMEK, rotation schedules + Pub/Sub notifications. Regional or automatic replication. Owner: Google / Alphabet (public, NASDAQ: GOOGL).

All three are commodity, first-party building blocks: default choice if you're already in that cloud; ownership is the parent hyperscaler; no M&A question.
