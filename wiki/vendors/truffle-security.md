---
title: Truffle Security
type: vendor
name: Truffle Security
slug: truffle-security
aka: [TruffleHog, TruffleHog Enterprise, TruffleHog Analyze, Truffle Security Co.]
primary_category: software-supply-chain
also_listed_in: []
website: https://trufflesecurity.com
founded: 2021
hq: San Francisco, California, USA
ownership_state: oss-vendor-backed
owner: null
ownership_note: "Private, VC-backed company that maintains open-source TruffleHog (AGPL-3.0; created 2016 by co-founder and CEO Dylan Ayrey). $25M Series B co-led by Intel Capital and a16z (2025-11-06); total raised over $40M. No acquisition found as of 2026-10-26."
acquisition: {announced: null, closed: null, price: null}
funding_total: "over $40M (company figure, 2025-11-06; one source itemises $14M Series A + $25M Series B)"
last_funding: "Series B, $25M, 2025-11-06 (Intel Capital and a16z)"
market_position: {software-supply-chain: oss-default}
deployment_model: [saas, hybrid]
form_factor: [platform, sdk]
data_leaves_tenancy: partial
integrations: [github, gitlab, bitbucket, slack, jira, confluence, s3, gcp, aws, docker, aws-marketplace]
mcp_support: none
certifications: []
pricing_model: "Open-source core is free (AGPL-3.0). TruffleHog Enterprise and Analyze are quote-based subscriptions; AWS Marketplace listing."
fs_traction: claimed
target_customer: security teams from mid-market to Fortune 1000; heavy open-source use by individual engineers and pentesters
last_verified: 2026-10-26
verify_after: null
tags: [secrets-scanning, secret-verification, open-source, agpl, nhi, leaked-credentials, appsec]
sources:
  - {claim: "$25M Series B, Intel Capital + a16z, total >$40M, founded 2021, SF; Enterprise and GCP Analyze", url: "https://www.securityweek.com/truffle-security-raises-25-million-for-secret-scanning-engine/", date: 2025-11-06, confidence: high}
  - {claim: "Dylan Ayrey co-founder/CEO, created TruffleHog 2016; revenue >2x; FS among customer verticals", url: "https://www.intelcapital.com/truffle-security-raises-25-million-series-b-to-expand-nhi-security/", date: 2025-11-06, confidence: medium}
  - {claim: "AGPL-3.0, ~28.7k stars, created 2016-12-31, release v3.99.7 2026-10-24", url: "https://github.com/trufflesecurity/trufflehog", date: 2026-10-26, confidence: high}
  - {claim: "800+ secret types with live verification; sources scanned; Analyze; named customers", url: "https://trufflesecurity.com/", date: 2026-10-26, confidence: medium}
  - {claim: "Truffle-hosted vs self-hosted scanners; in-memory processing, metadata-only to control plane", url: "https://docs.trufflesecurity.com/hosted-scanner-deployment", date: 2026-10-26, confidence: medium}
---

# Truffle Security

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner**: The company behind **TruffleHog**, the most widely used open-source secrets scanner. TruffleHog finds leaked credentials in code, git history, chat, tickets and cloud storage and **checks each one live against the issuing service** to tell you whether it still works. A commercial Enterprise edition adds continuous monitoring and remediation workflow.

**What it does**:
- **TruffleHog (open source, AGPL-3.0).** A CLI and library with 800+ detectors (vendor figure).
  - It scans git repositories including **full history and deleted or hidden content**, plus file systems, S3 and GCS buckets, Docker images, Slack, Jira, Confluence and more.
  - Its signature feature is **verification**: for most detectors it calls the provider's API to confirm a found key is live. That cuts false positives sharply and is why pentesters and red teams use it.
  - Very active: about 28.7k GitHub stars, with release v3.99.7 on 2026-10-24.
- **TruffleHog Enterprise.** A hosted dashboard with continuous scanning across connected sources, alerting, team management, and developer remediation workflows that **re-verify that a key was actually rotated** before closing the incident.
- **TruffleHog Analyze** (SaaS, GCP and AWS variants). Given a leaked key, it maps **what that identity can reach**: resources and permissions, without logging into the provider console. GCP Analyze launched with the November 2025 Series B. A third-party profile says AWS Analyze followed in August 2026; not confirmed from a primary source. Truffle markets this as non-human-identity (NHI) security.

**Naming / provenance**: **Dylan Ayrey** created open-source TruffleHog in **2016** (repo created 2016-12-31) and co-founded **Truffle Security Co.** in **2021** to commercialise it. He is CEO. The repository moved to the `trufflesecurity` GitHub organisation, and v3 was a full rewrite in Go. Slugged by company, with TruffleHog in `aka`, per the wiki's company-slug convention.

**Ownership & viability**: `oss-vendor-backed`. Truffle Security is a private, VC-backed company that maintains TruffleHog; the open-source project has no foundation. **$25M Series B co-led by Intel Capital and a16z**, announced **2025-11-06**, with Abstract, Lytical Ventures and security-industry angels. Total raised is "over $40M". Truffle claims revenue more than doubled in the year to November 2025 (vendor claim). Viability is reasonable for its size, but it is a much smaller company than [gitguardian](gitguardian.md).

**Acquisition-risk note:** a natural tuck-in for an AppSec platform, a code host, or an NHI or identity vendor buying detection. If acquired, the AGPL open-source code would survive as a fork-able baseline, though maintenance velocity could drop.

**Positioning & differentiators**: `oss-default` in software-supply-chain. TruffleHog is the default free secrets scanner many teams and security testers already run; the commercial layer is a smaller business on top.
- **Vs. [gitguardian](gitguardian.md):** the main commercial rival.
  - TruffleHog: open-source-first, live verification on most detectors, and permission analysis of a leaked key (Analyze).
  - GitGuardian: a more mature enterprise workflow, a distinct NHI inventory and governance product, AI-coding-agent hooks and an MCP server, and an on-prem or air-gapped option.
- **Vs. Gitleaks** (open source, MIT; no wiki page): Gitleaks is lighter and permissively licensed, with no verification. TruffleHog is heavier but verifies.
- **Vs. built-in scanning** ([github-advanced-security](github-advanced-security.md), [gitlab](gitlab.md)): native push protection is limited to that platform. TruffleHog scans across code hosts, chat, tickets and buckets.
- **Vs. NHI platforms** ([astrix-security](astrix-security.md), [entro-security](entro-security.md)): Analyze answers what a leaked key can reach. It is not an inventory or lifecycle-governance product, so it is **not cross-listed** to non-human-identity despite the NHI marketing.

**Who should choose them / anti-fit**: Fits a fund with in-house engineering or a security team that wants a **free, credible scanner today**: open-source TruffleHog in CI, pre-commit or periodic sweeps. Upgrade to Enterprise when you need continuous coverage of Slack, Jira, Confluence and S3, plus tracked rotation. Also fits incident response, where you need to know quickly which leaked keys are live and what they can touch. **Anti-fit:**
- Organisations whose legal team bars **AGPL** code from internal tooling. Running the CLI internally is generally not distribution, but some policies block AGPL outright; check with counsel.
- Buyers wanting governance of every machine identity, not only leaked ones.
- Buyers needing a fully air-gapped product with no vendor control plane.

**Known weaknesses / gotchas**:
- **Verification makes outbound calls.** Live-checking a key means the scanner authenticates to the provider with the leaked credential. That can trip alerts, appear in the provider's logs, and is undesirable in some regulated environments. It can be disabled.
- **AGPL-3.0 licence** for the open-source core (verified on GitHub 2026-10-26). Some third-party sites wrongly say MIT.
- **Small company.** About $40M raised against GitGuardian's ~$106M and the AppSec platforms. Expect a thinner enterprise-support bench.
- No AI-agent or MCP features found on its site as of 2026-10-26 (`mcp_support: none`, meaning none found).

**Deployment & data handling**: Open source runs wherever you run it, so nothing leaves your environment except verification calls. Enterprise uses a **Truffle-hosted SaaS control plane** with a choice of scanners:
- **Truffle-hosted scanners**, isolated per tenant in Truffle's infrastructure.
- **Self-hosted scanners** on Kubernetes or a VM, for sources not reachable from the internet or for data-residency needs.

Truffle's AWS Marketplace listing says secrets are processed **in memory** and only **detection metadata** goes back to the control plane (vendor claim). Hence `data_leaves_tenancy: partial`. Scanning is out-of-band, with no runtime latency.

**Integrations & partnerships**: GitHub, GitLab, Bitbucket, Slack, Jira, Confluence, S3, GCS and GCP logs, Docker, CI systems, AWS Marketplace. Investors include Intel Capital and a16z.

**Compliance & FS traction**: Truffle says customers span tech, retail and **financial services** at mid-market to Fortune 1000 scale. Named customers on its site are Optro, TextNow and Klaviyo; none are FS. Certifications are not stated on the homepage. Hedge-fund fit: **medium-high for the free open-source tool** (low cost, high value for any team with code); **medium for Enterprise**.

**Commercial**: Open source is free. Enterprise and Analyze are quote-based, with no public pricing; also sold through AWS Marketplace.

## Open questions

- SOC 2 / ISO 27001 status of TruffleHog Enterprise.
- Confirm AWS Analyze launch (August 2026, third-party) and whether Azure Analyze exists.
- Named FS customers; headcount.
- Whether Enterprise offers a fully self-hosted control plane (only scanners appear self-hostable).

## Sources

- [Truffle Security Raises $25 Million (SecurityWeek, 2025-11-06)](https://www.securityweek.com/truffle-security-raises-25-million-for-secret-scanning-engine/), fetched 2026-10-26. Supports: round, leads, total, HQ, 2021 founding, product lines. Confidence: high.
- [Truffle Security Series B (Intel Capital)](https://www.intelcapital.com/truffle-security-raises-25-million-series-b-to-expand-nhi-security/), search snapshot 2026-10-26. Supports: Dylan Ayrey as co-founder and CEO who created TruffleHog in 2016; revenue and customer claims. Confidence: medium.
- [trufflesecurity/trufflehog (GitHub API)](https://github.com/trufflesecurity/trufflehog), fetched 2026-10-26. Supports: AGPL-3.0, stars, repo creation date, latest release. Confidence: high.
- [Truffle Security homepage](https://trufflesecurity.com/), fetched 2026-10-26. Supports: 800+ detectors with verification, sources scanned, Analyze, named customers. Confidence: medium (vendor).
- [TruffleHog Enterprise docs: hosted and self-hosted scanners](https://docs.trufflesecurity.com/hosted-scanner-deployment), plus the AWS Marketplace listing, search snapshot 2026-10-26. Supports: deployment options, in-memory processing. Confidence: medium.
- Cached: `raw/sources/2026-10-26--truffle-security--funding-trufflehog.md`

## History

- [2026-10-26] Page created and researched in one pass. Slugged by company (`truffle-security`) with TruffleHog in `aka`. Primary software-supply-chain. Considered and rejected cross-listing to non-human-identity: Analyze maps a leaked key's permissions but there is no NHI inventory or lifecycle product. Set ownership to oss-vendor-backed (VC-backed company stewarding the AGPL project).
