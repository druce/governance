---
title: Veracode
type: vendor
name: Veracode
slug: veracode
aka: []
primary_category: software-supply-chain
also_listed_in: []
website: https://www.veracode.com/
founded: 2006
hq: Burlington, MA, USA
ownership_state: pe-owned
owner: TA Associates
ownership_note: TA Associates took a majority position in May 2022 at a ~$2.5B valuation (from Thoma Bravo, which had bought Veracode from Broadcom/CA in 2018). Brian Roche became CEO in April 2024, succeeding Sam King.
acquisition: {announced: 2022-03, closed: 2022-05, price: ~$2.5B valuation}
funding_total: null
last_funding: null
market_position: {software-supply-chain: legacy-incumbent}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: null
tags: [appsec, sast, dast, sca, incumbent, pe-owned]
sources:
  - {claim: "TA Associates acquired a majority stake in Veracode in May 2022 at a $2.5B valuation", url: "https://fintech.global/2022/03/16/ta-associates-acquires-majority-stake-in-app-security-platform-veracode/", date: 2026-08-26, confidence: medium}
  - {claim: "Veracode acquired Phylum's technology (Jan 2025) for malicious-package detection in open source", url: "https://www.veracode.com/blog/innovating-secure-software-supply-chains-veracode-acquires-phylum/", date: 2026-08-26, confidence: high}
  - {claim: "Brian Roche promoted to CEO April 2024; Veracode acquired Longbow Security (2024)", url: "https://www.bankinfosecurity.com/veracode-promotes-brian-roche-to-ceo-buys-longbow-security-a-24767", date: 2026-08-26, confidence: high}
---

# Veracode

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — The other AppSec incumbent: a SaaS-first application-security platform (SAST, DAST, SCA, container, IaC) with a two-decade compliance-scanning heritage, now bolting on malicious-package detection and risk correlation.

**What it does** — Veracode runs the full battery of application security tests as a service: static analysis, dynamic analysis against running apps, software composition analysis on open-source dependencies, container and IaC scanning, plus manual penetration testing as a paid add-on. Its historical differentiator was **binary static analysis** — scanning compiled artifacts rather than requiring source — which made it the tool of choice for assessing third-party and vendor-supplied software. Recent direction is set by three tuck-ins: **Crashtest Security** (DAST), **Longbow Security** (2024 — cloud/app risk discovery and correlation, i.e. ASPM), and **Phylum** (Jan 2025 — detection of deliberately malicious packages in open-source registries, not just vulnerable ones).

**Naming / provenance** — Founded 2006 in Burlington, MA. Owned by CA Technologies (2017) via the Veracode/CA deal, passed to Broadcom with the CA acquisition, sold to **Thoma Bravo** in 2018, then majority-sold to **TA Associates** in 2022. Brian Roche succeeded Sam King as CEO in April 2024.

**Ownership & viability** — `pe-owned`, **TA Associates** majority since May 2022 at a reported **~$2.5B** valuation. Three PE owners in eight years is a lot of turnover; each transition has come with a strategy reset. Financially stable and shipping, but this is a mature-market asset being managed for cash and multiple expansion, not a growth story. Expect incremental product work and continued tuck-ins rather than reinvention.

**Positioning & differentiators** —
- **Binary/compiled-artifact scanning.** Still the cleanest way to assess software you did not write and cannot get source for — genuinely useful in third-party due diligence, and something [snyk](snyk.md) and [semgrep](semgrep.md) do not do.
- **Compliance-report shape.** Veracode's output has long been formatted for the "prove to a counterparty that this app was tested" use case (its Verified programme). That is an audit artifact, not a developer workflow.
- **Phylum for malicious packages.** Puts it in direct competition with [socket](socket.md) on the *deliberately hostile dependency* problem, which is a different threat from the *known-CVE dependency* problem [snyk](snyk.md) and [black-duck](black-duck.md) solve.
- **Weaker developer experience.** The consistent criticism versus [snyk](snyk.md), [semgrep](semgrep.md) and [aikido-security](aikido-security.md).

**Who should choose them / anti-fit** — Fits a firm that needs **third-party software assessed without source access**, or one whose counterparties/regulators want a named independent AppSec attestation. **Anti-fit:** a developer-led team optimising for inline feedback and low friction — Veracode's centre of gravity is the security team's report, not the pull request.

**Known weaknesses / gotchas** — Developer experience and scan latency are the standing complaints. Serial PE ownership means roadmap discontinuity. SaaS-only, with limited self-hosted options — a constraint for firms that will not send code or binaries out.

**Deployment & data handling** — SaaS. Code or compiled binaries are uploaded to Veracode for analysis, so **artifacts do leave the tenancy by design**. Exact retention, isolation, and training-use terms are **unverified** and should be diligenced before any proprietary trading code is submitted.

**Integrations & partnerships** — CI/CD and IDE plugins, SCM, ticketing. Detailed list and MCP/agent support unverified.

**Compliance & FS traction** — Long financial-services history claimed; **not independently verified here**. Certifications held unverified.

**Commercial** — Not public. Enterprise subscription, historically priced per application scanned — a model that penalises microservice estates.

## Open questions

- Retention, isolation, and training-use terms for uploaded source/binaries.
- Certifications actually held (SOC 2, ISO 27001, FedRAMP).
- Named FS customers; whether per-application pricing is still the default.
- Whether Phylum's malicious-package feed is competitive with [socket](socket.md)'s in coverage and latency.
- TA Associates hold period — exit timing.

## Sources

- [TA Associates acquires majority stake in Veracode (FinTech Global)](https://fintech.global/2022/03/16/ta-associates-acquires-majority-stake-in-app-security-platform-veracode/) — fetched 2026-08-26 — supports: ownership, valuation; confidence: medium
- [Veracode acquires Phylum technology (Veracode blog)](https://www.veracode.com/blog/innovating-secure-software-supply-chains-veracode-acquires-phylum/) — fetched 2026-08-26 — supports: Phylum acquisition and rationale; confidence: high (primary, vendor)
- [Veracode Promotes Brian Roche to CEO, Buys Longbow Security (BankInfoSecurity)](https://www.bankinfosecurity.com/veracode-promotes-brian-roche-to-ceo-buys-longbow-security-a-24767) — fetched 2026-08-26 — supports: CEO change, Longbow; confidence: high
- Cached: `raw/sources/2026-08-26--veracode--ownership-and-acquisitions.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier A, score 9).
