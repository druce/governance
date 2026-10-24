---
title: Bitwarden
type: vendor
name: Bitwarden
slug: bitwarden
aka: [Bitwarden Password Manager, Bitwarden Secrets Manager, Passwordless.dev, 8bit Solutions]
primary_category: secrets-management
also_listed_in: []
website: https://bitwarden.com/
founded: 2016
hq: Santa Barbara, California, USA
ownership_state: independent
owner: null
ownership_note: Private. $100M minority growth investment led by PSG with existing investor Battery Ventures (announced 2022-09-06); two PSG board seats. Not PE-controlled. No later round found as of 2026-10-23.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: $100M minority growth equity led by PSG, 2022-09
market_position: {secrets-management: challenger}
deployment_model: [saas, self-hosted]
form_factor: [platform, browser-extension, sdk, api]
data_leaves_tenancy: partial
integrations: [github-actions, gitlab-ci, jenkins, kubernetes, ansible, siem-export, scim, saml-sso]
mcp_support: server
certifications: [soc2-type2, soc3, iso27001, hipaa]
pricing_model: "Per-seat. Secrets Manager: Free (2 users), Teams $6/user/mo, Enterprise $12/user/mo (annual, USD; extra machine accounts $1 each). Password Manager business plans priced separately."
fs_traction: unverified
target_customer: smb to enterprise; developer and DevOps teams
last_verified: 2026-10-23
verify_after: null
tags: [password-manager, secrets-management, open-source, self-hosted, zero-knowledge, machine-accounts, mcp]
sources:
  - {claim: "$100M minority growth investment led by PSG, Battery Ventures participating, PSG's Tom Reardon and Govind Anand join board (2022-09)", url: "https://www.helpnetsecurity.com/2022/09/07/bitwarden-funding/", date: 2026-10-23, confidence: high}
  - {claim: "Founded 2016 by Kyle Spearrin; HQ Santa Barbara; CEO Michael Sullivan; 80,000+ businesses and 15M+ users; products Password Manager, Secrets Manager, Passwordless.dev, Authenticator", url: "https://bitwarden.com/about/", date: 2026-10-23, confidence: medium}
  - {claim: "Secrets Manager scope: projects, machine accounts for apps/pipelines/AI agents, CLI, SDKs, CI/CD and Kubernetes integrations, self-hosting on Enterprise, published pricing", url: "https://bitwarden.com/products/secrets-manager/", date: 2026-10-23, confidence: high}
  - {claim: "SOC 2 Type II, SOC 3, ISO 27001, HIPAA; not FedRAMP (pursuing); annual third-party code audits; cloud data in Azure US or EU; full stack self-hostable", url: "https://bitwarden.com/compliance/", date: 2026-10-23, confidence: medium}
  - {claim: "Local-first MCP server launched July 2025; Agent Access SDK announced Oct 2025 and described as alpha", url: "https://bitwarden.com/blog/bitwarden-mcp-server/", date: 2026-10-23, confidence: medium}
  - {claim: "@bitwarden/cli 2026.4.0 on npm was malicious for ~90 minutes on 2026-04-22; stole developer and cloud credentials; Bitwarden says vault data not at risk", url: "https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/", date: 2026-10-23, confidence: high}
---

# Bitwarden

> Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — The open-source password manager that has become the default "good, cheap, and self-hostable" choice for teams. It also sells a real machine-secrets product, Bitwarden Secrets Manager, so a single vendor can cover both staff passwords and application/CI secrets.

**What it does** — Two products on one zero-knowledge, end-to-end-encrypted vault. **Password Manager** handles human credentials, passkeys and shared vaults through browser extensions, desktop and mobile apps. **Secrets Manager** handles machine credentials. Secrets live in *projects*. *Machine accounts* are non-human identities for applications, pipelines and AI agents, and each one holds a token scoped to specific secrets. Delivery is through a CLI (`bws run` injects secrets into a process), SDKs in nine languages, and integrations with GitHub Actions, GitLab CI/CD, Jenkins, a Kubernetes Operator and Ansible. The line-up also includes **Passwordless.dev**, a FIDO2/WebAuthn toolkit for adding passkeys to your own apps, and a free Authenticator app. Of the three password-manager write-ins in this survey (Bitwarden, [lastpass](lastpass.md), [dashlane](dashlane.md)), Bitwarden is the only one with a dedicated machine-secrets product.

**Naming / provenance** — Founded 2016 by Kyle Spearrin, who is now Founder & Chief Innovation Officer. Bitwarden, Inc. is the parent of the original entity, 8bit Solutions LLC. Its own about page now lists Michael Sullivan as CEO. Michael Crandell was CEO at the 2022 round, and this page has not verified when the change happened.

**Ownership & viability** — `independent`. The only disclosed outside capital is a **$100M minority growth investment led by PSG**, with existing investor **Battery Ventures** participating. It was announced September 2022, and two PSG partners joined the board. No valuation was disclosed and no later round was found. The company claims **80,000+ businesses and 15M+ users**, which is vendor-reported. Viability looks sound. The acquisition-risk note: a minority-funded company four years past its last round is a plausible control-transaction candidate. Because the client code is open source and the full server stack can be self-hosted, customers would keep an exit path if an owner changed direction. That is a stronger continuity position than any closed-source competitor offers.

**Positioning & differentiators** —
- **Open source and fully self-hostable.** Clients and server are public, and the whole stack can run on your own infrastructure. Neither [1password](1password.md) nor [keeper](keeper.md) offers that. For a firm that does not want a third party holding its credential vault at all, Bitwarden is the most credible commercial option. The alternative is running [hashicorp-vault](hashicorp-vault.md), but Vault covers only machine secrets.
- **Price.** Published, low per-seat pricing. Secrets Manager Enterprise lists at $12/user/month, and a free tier allows 2 users. That is cheaper than [doppler](doppler.md) or [infisical](infisical.md) for small teams that already pay for Bitwarden seats.
- **Human and machine secrets from one vendor**, like [1password](1password.md) and [keeper](keeper.md). Secrets Manager is simpler than [hashicorp-vault](hashicorp-vault.md): it stores and injects static secrets and has no dynamic, short-lived credential engine. It is closer in shape to [doppler](doppler.md) or [infisical](infisical.md) than to Vault.
- **Early agent-credential work.** A local-first MCP server shipped in July 2025. An "Agent Access SDK" for just-in-time, human-approved credential release to AI agents followed in October 2025, but Bitwarden itself calls the SDK **alpha** and not for production data.

**Who should choose them / anti-fit** — Fits a **small-to-mid manager that wants one credential vendor for staff passwords and developer secrets at low cost**. It fits even better when the firm wants to self-host its vault for control or data-residency reasons. **Anti-fit:**
- A firm that needs **privileged session management, recording and vendor-access brokering**. Bitwarden is not a PAM product; look at [cyberark](cyberark.md), [beyondtrust](beyondtrust.md), [delinea](delinea.md) or [keeper](keeper.md).
- A platform team that needs **dynamic, short-lived database/cloud credentials** ([hashicorp-vault](hashicorp-vault.md), or the cloud-native stores such as [aws-secrets-manager](aws-secrets-manager.md) and [azure-key-vault](azure-key-vault.md)).
- Anyone who needs **FedRAMP**, which Bitwarden does not hold.

**Known weaknesses / gotchas** —
- **April 2026 supply-chain incident.** For about 90 minutes on 2026-04-22, `@bitwarden/cli` version 2026.4.0 on npm carried credential-stealing malware. It took npm and GitHub tokens, SSH keys and AWS/Azure/GCP credentials from developer machines and CI runners that installed it. Bitwarden says the vault was never at risk and only the npm channel was affected. Public accounts disagree on the root cause: Bitwarden tied it to the wider Checkmarx campaign, while JFrog and Socket pointed to a compromised GitHub Action. For a hedge fund this matters because the CLI is exactly what gets installed in CI pipelines. **Pin versions and verify CLI provenance**, and check whether any pipeline pulled that release.
- **Self-hosting moves the security burden to you.** Patching, backups and availability of a self-hosted vault become your team's job.
- **Secrets Manager is less mature** than the password manager and than dedicated secrets tools. It stores static secrets, with no secret generation or rotation engine verified here.

**Deployment & data handling** — Cloud SaaS, with vault data stored in Microsoft Azure in a **US or EU** region, or fully self-hosted. Self-hosting Secrets Manager requires the Enterprise plan. The vault is end-to-end encrypted: in the cloud, Bitwarden holds ciphertext but not the keys. `data_leaves_tenancy: partial` because the encrypted vault leaves your tenancy in the cloud model but not when self-hosted. Which metadata (item names, URLs, access logs) is visible to Bitwarden in the cloud model is **unverified**. Bitwarden says the MCP server runs locally on the user's machine and recommends a local, self-hosted LLM when using it. That advice matters: piping vault contents to a hosted model defeats the zero-knowledge design.

**Integrations & partnerships** — SSO (SAML/OIDC), SCIM and Directory Connector on Enterprise; event logs exportable to CSV or SIEM; CI/CD (GitHub Actions, GitLab, Jenkins), Kubernetes Operator, Ansible. MCP: a Bitwarden-published MCP server (`mcp_support: server`), extended in October 2025 to enterprise administration tasks.

**Compliance & FS traction** — Bitwarden's compliance page lists SOC 2 Type II, SOC 3 (public), ISO 27001, HIPAA (annual third-party audit), GDPR, CCPA and the EU-US Data Privacy Framework. It also lists annual third-party source-code audits and penetration tests, plus a HackerOne bug bounty. **No FedRAMP** (the page says Bitwarden is "pursuing" it). Five survey respondents (Oct 2026) report it in production, the joint-highest write-in count in this category alongside [lastpass](lastpass.md). No named financial-services customers were confirmed.

**Commercial** — Per-seat with published prices. Secrets Manager: Free (2 users, 3 projects, 3 machine accounts), Teams $6/user/month (20 machine accounts), Enterprise $12/user/month (50 machine accounts, SSO/SCIM, self-hosting). Extra machine accounts are $1 each, all billed annually in USD as of 2026-10-23. Password Manager business tiers are priced separately and were not re-verified here.

## Open questions

- When Michael Sullivan became CEO, and Michael Crandell's current role.
- Whether SOC 2 / ISO 27001 scope covers Secrets Manager and the cloud service only, or anything relevant to self-hosted deployments.
- What metadata is visible to Bitwarden in the cloud model.
- A published root-cause post-mortem for the April 2026 npm incident, and what CI/CD hardening followed.
- Whether Secrets Manager has gained secret rotation or dynamic-credential features.
- Status of the Agent Access SDK beyond alpha.
- Named FS customers; FedRAMP progress.

## Sources

- [Bitwarden raises $100M (Help Net Security)](https://www.helpnetsecurity.com/2022/09/07/bitwarden-funding/) — fetched 2026-10-23 — supports: funding, investors, board; confidence: high
- [About Bitwarden](https://bitwarden.com/about/) — fetched 2026-10-23 — supports: founding, HQ, CEO, customer counts, product line; confidence: medium (vendor)
- [Bitwarden Secrets Manager product page](https://bitwarden.com/products/secrets-manager/) — fetched 2026-10-23 — supports: product scope, integrations, pricing; confidence: high (primary)
- [Bitwarden compliance](https://bitwarden.com/compliance/) — fetched 2026-10-23 — supports: certifications, data residency, self-hosting; confidence: medium (vendor self-attestation)
- [Bitwarden MCP server blog](https://bitwarden.com/blog/bitwarden-mcp-server/) — fetched 2026-10-23 (search snippet) — supports: MCP server, Agent Access SDK alpha; confidence: medium
- [Bitwarden CLI npm package compromised (BleepingComputer)](https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/) — fetched 2026-10-23 — supports: April 2026 incident; confidence: high
- Cached: `raw/sources/2026-10-23--bitwarden--funding-products-compliance.md`, `raw/sources/2026-10-23--bitwarden--cli-npm-compromise-2026.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Added because 5 respondents to the Oct 2026 CTO survey wrote it in under Secrets Manager, all 5 in production.
