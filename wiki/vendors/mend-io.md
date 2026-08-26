---
title: Mend.io
type: vendor
name: Mend.io
slug: mend-io
aka: [WhiteSource, Mend]
primary_category: software-supply-chain
also_listed_in: []
website: https://www.mend.io/
founded: 2011
hq: Givatayim, Israel
ownership_state: independent
owner: null
ownership_note: Privately held, VC-backed. ~$121M raised in total; $75M Series D announced April 2021. No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$121M
last_funding: Series D $75M, 2021-04
market_position: {software-supply-chain: challenger}
deployment_model: [saas, self-hosted]
form_factor: [platform, sdk, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: null
tags: [appsec, sca, auto-remediation, ai-code-security, rebrand]
sources:
  - {claim: "WhiteSource rebranded to Mend.io in May 2022 and launched the Mend Application Security Platform with automated remediation", url: "https://www.mend.io/blog/whitesource-is-now-mend/", date: 2026-08-26, confidence: high}
  - {claim: "~$121M total funding; $75M Series D April 2021; HQ Givatayim, Israel; privately held VC-backed", url: "https://pitchbook.com/profiles/company/57623-23", date: 2026-08-26, confidence: medium}
---

# Mend.io

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — Software composition analysis with a remediation-first pitch: rather than handing you a vulnerability list, Mend opens the dependency-upgrade pull request itself — and has extended the same model to AI-generated code and embedded AI components.

**What it does** — Core product is **SCA** over open-source dependencies, plus SAST and container scanning. The differentiator the company leans on is **automated remediation**: Mend Renovate (the widely used open-source dependency-update bot, which Mend maintains) and auto-generated fix PRs, so the output is a merge request rather than a ticket. Since 2024 it has pushed into **AI security** — scanning AI-generated code, inventorying AI models and AI components pulled into applications, and flagging risk in that supply chain specifically.

**Naming / provenance** — Founded 2011 in Israel as **WhiteSource**; rebranded to **Mend.io** in May 2022 alongside the platform relaunch. Much older comparison content still says WhiteSource. The `.io` is part of the brand.

**Ownership & viability** — `independent`, VC-backed, roughly **$121M raised**, with a **$75M Series D in April 2021**. No round found since — five years without a raise in a consolidating category is a signal worth weighing. No acquisition found as of 2026-08-26; in a market where [black-duck](black-duck.md), [checkmarx](checkmarx.md) and [veracode](veracode.md) are all PE-held and [snyk](snyk.md) is far larger, Mend is a plausible acquisition target rather than a consolidator.

**Positioning & differentiators** —
- **Renovate ownership.** Mend maintains the dependency-update bot that a very large number of engineering teams already run for free. That is genuine distribution and a credible remediation story no competitor has an equivalent of.
- **Fix-first framing.** Positioned against [snyk](snyk.md)'s find-first framing, though Snyk also opens fix PRs — the gap is narrower in practice than the marketing suggests.
- **AI-component inventory.** Overlaps [ai-spm](../categories/ai-spm.md) from the code side: what models and AI SDKs are actually compiled into our applications.
- **Mid-market price point.** Generally cheaper than [black-duck](black-duck.md) or [checkmarx](checkmarx.md); thinner on licence-compliance depth than Black Duck.

**Who should choose them / anti-fit** — Fits a firm that already runs Renovate and wants the commercial layer on top, or one that wants SCA with the remediation loop closed and does not need heavyweight licence compliance. **Anti-fit:** a firm needing binary scanning of third-party software ([veracode](veracode.md)), deep licence diligence ([black-duck](black-duck.md)), or the broadest enterprise AST coverage ([checkmarx](checkmarx.md)).

**Known weaknesses / gotchas** — Smaller than the incumbents, with correspondingly thinner enterprise support and integration breadth. Funding age (2021) versus a consolidating market is the main viability question. The rebrand still causes research confusion.

**Deployment & data handling** — SaaS and self-hosted both offered. Data-handling specifics for the SaaS path — whether source is transmitted, retention, training use — are **unverified**.

**Integrations & partnerships** — SCM and CI/CD integration is the core surface (Renovate operates directly on repositories). Detail and MCP support unverified.

**Compliance & FS traction** — Unverified; no named FS references confirmed.

**Commercial** — Not public. Subscription, typically per developer or per repository.

## Open questions

- Any funding, acquisition, or ownership change since the 2021 Series D — the most important open item on this page.
- Whether source code leaves the tenancy under Mend SaaS; retention and training-use terms.
- Certifications held; FS customer references.
- How the AI-component inventory compares to dedicated [ai-spm](../categories/ai-spm.md) tools.
- Renovate's licensing/commercial boundary — what stays free.

## Sources

- [WhiteSource Is Now Mend (Mend.io blog)](https://www.mend.io/blog/whitesource-is-now-mend/) — fetched 2026-08-26 — supports: rebrand date, positioning; confidence: high (primary, vendor)
- [Mend.io company profile (PitchBook)](https://pitchbook.com/profiles/company/57623-23) — fetched 2026-08-26 — supports: funding total, Series D, HQ, ownership; confidence: medium
- Cached: `raw/sources/2026-08-26--mend-io--rebrand-and-funding.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier A, score 8).
