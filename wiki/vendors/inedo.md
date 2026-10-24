---
title: Inedo
type: vendor
name: Inedo
slug: inedo
aka: [Inedo ProGet, ProGet]
primary_category: software-supply-chain
also_listed_in: []
website: "https://inedo.com/proget"
founded: 2007
hq: Berea, Ohio, USA
ownership_state: independent
owner: null
ownership_note: "Private; no outside funding or acquisition found (low-medium confidence, directory and wiki-mirror sources). CEO Alex Papadimoulis. Checked 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {software-supply-chain: niche-specialist}
deployment_model: [self-hosted]
form_factor: [platform]
data_leaves_tenancy: "false"
integrations: [nuget, npm, pypi, maven, docker, ci-servers, active-directory, ldap]
mcp_support: unverified
certifications: []
pricing_model: "Per-server annual licence incl. support: Free; Basic $2,395/yr; Enterprise $11,995/yr (new-licence prices effective 2024-08-01)"
fs_traction: unverified
target_customer: small-to-mid-size engineering teams (Windows/.NET-heavy shops especially) that want a self-hosted private package registry with built-in SCA
last_verified: 2026-10-24
verify_after: null
tags: [package-repository, artifact-repository, sca, sbom, cyclonedx, license-compliance, self-hosted, survey-write-in-2026-10]
sources:
  - {claim: "SCA: scans packages and Docker images against NVD + Inedo DB; risk categories; license detection and blocking; build re-analysis (marketing)", url: "https://inedo.com/proget/software-composition-analysis", date: 2026-10-24, confidence: medium}
  - {claim: "SBOM in OWASP CycloneDX; import/export; generated at build/CI time; EO 14028 framing (marketing)", url: "https://inedo.com/proget/software-bill-of-materials", date: 2026-10-24, confidence: medium}
  - {claim: "Edition restrictions: Free has no vulnerability assessments/SBOM/policies/blocking; Basic partial; Enterprise full incl. container scanning and HA", url: "https://docs.inedo.com/docs/proget/administration/license", date: 2026-10-24, confidence: high}
  - {claim: "Basic $2,395/yr, Enterprise $11,995/yr from 2024-08-01; per-server licensing", url: "https://blog.inedo.com/inedo/proget-pricing-changes-2024", date: 2024-08-01, confidence: medium}
  - {claim: "Founded 2007, Berea Ohio; BuildMaster 2010, ProGet 2012, Otter 2016", url: "https://en.wikipedia.org/wiki/ProGet", date: 2026-10-24, confidence: low-medium}
---

# Inedo

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — Inedo makes **ProGet**, a self-hosted private package and container registry (NuGet, npm, PyPI, Maven, Docker and others) that proxies and caches public open-source registries. Paid editions add built-in vulnerability scanning, licence policy and SBOM management. It is a lighter, cheaper alternative to [jfrog](jfrog.md) Artifactory or [sonatype](sonatype.md) Nexus.

**What it does** — ProGet sits between your developers and build servers and the public registries. Every third-party package is pulled through ProGet's feeds, so you have one place to cache, approve and block what enters your builds. **Does it genuinely claim supply-chain security? Yes**, through its software composition analysis (SCA) features (vendor claims, checked 2026-10-24):
- **Vulnerability scanning** of third-party packages and Docker images against the NVD and Inedo's own vulnerability database. Each finding is scored against a configurable risk profile into categories that say whether to monitor, remediate or contain it. Packages can be blocked automatically by CVE score or by your team's manual assessment.
- **Licence policy.** It detects each package's licence, shows which applications use which licences, and blocks unwanted ones (Inedo's example is GPL-3) at registry or feed level.
- **SBOMs** in OWASP **CycloneDX**: generated at build/CI time, importable and exportable through the UI and API, framed around US Executive Order 14028. ProGet re-analyses builds and projects already in production when new vulnerabilities or unwanted licences appear, and raises issues for the team.
- **Bypass detection.** It flags packages that were pulled straight from the internet rather than through ProGet.

No **malicious-package detection** is claimed on the pages reviewed. That separates it from [socket](socket.md), and from [sonatype](sonatype.md)'s repository firewall, which markets malware blocking. SPDX is not mentioned.

**Edition gating matters.** Per Inedo's licence documentation, **ProGet Free has none of the security features**: no vulnerability assessments, no SBOM generation, no compliance policies, no blocking. **Basic** adds project vulnerability identification, build SBOMs and blocking, but only one shared policy, three rule exceptions and global (not per-project) assessments. **Enterprise** adds container vulnerability scanning, full per-project policies, advanced compliance, and high availability (clustering, multi-site replication). A firm running Free has a package cache, not a supply-chain control.

**Naming / provenance** — Inedo was founded in 2007 in Berea, Ohio, as a custom-software firm before it shipped products: BuildMaster (release automation, 2010), **ProGet** (2012) and Otter (configuration management, 2016). It acquired NuGet Server in 2016 and has a Tokyo office (around 2017). CEO Alex Papadimoulis also runs the developer site The Daily WTF. These history details come from wiki mirrors and directories (low-medium confidence). Survey respondents name the product, "Inedo ProGet". The page is slugged by the company, per the default rule.

**Ownership & viability** — `independent`, private. No venture funding, PE investment or acquisition was found (checked 2026-10-24). It appears to be a small, long-running, self-funded company, though headcount and revenue were not found. Viability risk is **key-person and small-vendor risk** rather than burn rate. A plausible exit would be a sale to a DevOps or AppSec consolidator. Because ProGet is self-hosted and licensed per server, an existing install would keep running through any ownership change, but vulnerability-database updates would depend on the new owner.

**Positioning & differentiators** — `niche-specialist`: a small-vendor, self-hosted registry with security built in, used mostly by small and mid-size teams. It is not a broad AppSec platform.
- **Against [jfrog](jfrog.md) (Artifactory + Xray) and [sonatype](sonatype.md) (Nexus + Lifecycle/Firewall).** Same job, much lower price. Enterprise lists at $11,995 per server per year, and SCA is included rather than sold as a separate product (Inedo's own pitch against Sonatype Lifecycle). The cost is less depth: a smaller vulnerability-research team, no malware intelligence claimed, and a smaller ecosystem.
- **Against scanner-first SCA ([snyk](snyk.md), [mend-io](mend-io.md), [endor-labs](endor-labs.md), [github-advanced-security](github-advanced-security.md)).** ProGet enforces at the **point of ingestion** (the registry), so a blocked package never reaches a build. Scanners analyse your repos and offer reachability and fix advice that ProGet does not claim. Many shops run both kinds.
- **Against [chainguard](chainguard.md).** Chainguard replaces the upstream artifacts with hardened rebuilds; ProGet governs which upstream artifacts you let in. The two are complementary.

**Who should choose them / anti-fit** — Fits a **small or mid-size engineering team**, especially a Windows/.NET-heavy shop (ProGet's origin is NuGet), that wants a private, on-prem registry for its quant libraries and containers, plus basic vulnerability and licence gating, without Artifactory pricing. The **Basic or Enterprise** edition is required for that. **Anti-fit:** a firm that needs malicious-package detection or deep reachability analysis (pair it with or choose [socket](socket.md), [endor-labs](endor-labs.md) or [sonatype](sonatype.md)). Also a large multi-site enterprise that wants a heavily supported platform with broad partner integrations ([jfrog](jfrog.md)), and anyone who expects the Free edition to provide security.

**Known weaknesses / gotchas** —
- **Free ≠ secure.** Security features are paid-only. Ask a respondent which edition they run.
- **Only sees what flows through it.** A community-forum thread asking whether dependencies that bypass ProGet's proxy (for example, pulled direct from Maven Central) get scanned had no answer. ProGet can *flag* bypassed packages but cannot scan what it never saw. Enforce registry use at the network or CI level.
- **Metadata quality.** A forum user reported Python SBOM licence fields showing as "unknown". Licence detection is only as good as the package metadata.
- **Vulnerability source depth** (NVD plus Inedo's own database) is not independently benchmarked against Snyk, Sonatype or GitHub advisory coverage.
- **Thin hedge-fund evidence.** One survey respondent wrote it in (Software Supply Chain, 1, in production, 2026-10).

**Deployment & data handling** — **Self-hosted** (Windows and Linux/Docker installs are documented by Inedo but were not re-checked on this pass), with a high-availability cluster in Enterprise. Your packages, SBOMs and build data stay on your servers, so `data_leaves_tenancy: "false"` for content. ProGet necessarily makes outbound calls to public registries (through its connectors) and to fetch vulnerability data. What licence-check or telemetry traffic goes back to Inedo is **unverified**. Inline at package ingestion (proxy/feed), plus out-of-band re-analysis of builds.

**Integrations & partnerships** — Feed types include NuGet, npm, PyPI, Maven and Docker containers, among others (the full feed list was not re-checked on this pass). Integrates with CI servers for SBOM generation, and with Active Directory/LDAP in paid editions. MCP and agent support are unverified and not expected. No cloud-marketplace listing was checked.

**Compliance & FS traction** — Certifications are not applicable in the usual sense for self-hosted software and none were found. No named FS customers were found (the case-studies page was not reviewed). Survey evidence: 1 in-production write-in (2026-10).

**Commercial** — Annual per-server licence including support. Free (commercial use allowed, no security features), **Basic $2,395/yr**, **Enterprise $11,995/yr** (new-licence prices effective 2024-08-01; check the current pricing page).

## Open questions

- Headcount, revenue, and confirmation of no outside ownership.
- Exactly which vulnerability sources Inedo's database aggregates (OSV, GitHub Advisory Database?), and update cadence.
- Any malicious-package or typosquat detection on the roadmap.
- Outbound telemetry and licence-check traffic to Inedo.
- Named financial-services customers.

## Sources

- [ProGet Software Composition Analysis (Inedo)](https://inedo.com/proget/software-composition-analysis) — fetched 2026-10-24 — supports: vulnerability scanning, licence blocking, build re-analysis; confidence: medium (vendor marketing)
- [ProGet x SBOM (Inedo)](https://inedo.com/proget/software-bill-of-materials) — fetched 2026-10-24 — supports: CycloneDX SBOM, CI generation, EO 14028; confidence: medium (vendor marketing)
- [ProGet License Restrictions (Inedo docs)](https://docs.inedo.com/docs/proget/administration/license) — fetched 2026-10-24 — supports: edition gating of security features; confidence: high
- [ProGet pricing changes 2024 (Inedo blog)](https://blog.inedo.com/inedo/proget-pricing-changes-2024) — via search 2026-10-24 — supports: Basic/Enterprise prices from 2024-08-01; confidence: medium
- [ProGet (Wikipedia) and Inedo mirrors / Craft profile](https://en.wikipedia.org/wiki/ProGet) — via search 2026-10-24 — supports: founding 2007, Berea OH, product dates, CEO; confidence: low-medium
- [Inedo community forums](https://forums.inedo.com/) — via search 2026-10-24 — supports: proxy-bypass and licence-metadata caveats; confidence: low (user reports)
- Cached: `raw/sources/2026-10-24--inedo--proget-sca-sbom-editions.md`

## History

- [2026-10-24] Page created and researched. Added because of an October 2026 CTO survey write-in under AppSec / Software Supply Chain (Q53, "Inedo ProGet", 1 respondent, in production). Checked whether ProGet genuinely claims supply-chain security: yes (SCA vulnerability scanning, licence policy and blocking, CycloneDX SBOMs), though gated to the paid Basic and Enterprise editions. Primary software-supply-chain. Company slug `inedo`.
