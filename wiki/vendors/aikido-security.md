---
type: vendor
name: Aikido Security
slug: aikido-security
categories: [software-supply-chain]
layer: foundation
aliases: [Aikido]
website: "https://www.aikido.dev"
founded: 2022
hq: Ghent, Belgium
ownership: independent
ownership_detail: "Independent, venture-backed private company; Series B Jan 2026 at $1B valuation (unicorn)"
ownership_confidence: high
funding_total: "~$84M total (pre-seed €2M Jan 2023; seed €5M Nov 2023; Series A $17M May 2024; Series B $60M Jan 2026)"
last_funding: "Series B $60M, Jan 2026, $1B valuation (led by DST Global; PSG Equity, Notion Capital, Singular)"
deployment: [saas, api]
target_customer: SMB / mid-market (developer-first)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [appsec, sca, sast, dev-first, consolidated-platform]
---

# Aikido Security

**One-liner** — A consolidated, developer-first "all-in-one" application-security platform (SCA, SAST, secrets, IaC, container, DAST, cloud) aimed at SMB/mid-market teams that want one cheap tool instead of a stack of point products.

**What it does** — Aikido bundles the AppSec tools a dev team would otherwise buy separately: **SCA** (open-source dependency / vulnerability scanning), **SAST** (static code analysis), **secrets detection**, **IaC** scanning, **container image** scanning, **DAST/surface monitoring**, and **cloud posture (CSPM)** — under one "no BS," low-noise interface. The pitch is consolidation and developer experience: fast onboarding, autotriage to cut false positives, and pricing/UX aimed at teams without a dedicated security org. 2025 acquisitions added "Aikido Attack" (automated penetration testing).

**Where it sits in the stack** — Touches the foundation layer of [software-supply-chain](../categories/software-supply-chain.md) via its SCA/dependency scanning, but spans more broadly into general AppSec. It scans what enters your codebase/builds — the *untrusted-input* leg of the lethal trifecta as applied to your own supply chain. **AI-generated-code relevance:** Aikido explicitly targets the world where development (including AI-assisted coding) accelerates and outpaces security review — the dev-first scanning catches vulnerable/hallucinated dependencies and insecure AI-generated code at the point of commit/PR. It is a scanner-and-monitor, not a blocking repository firewall like [sonatype](sonatype.md).

**Deployment & architecture** — SaaS-first with API/CI/CD and source-control (GitHub/GitLab/Bitbucket) integrations; connects to cloud accounts for CSPM. No binary repository of its own (unlike [jfrog](jfrog.md)/[sonatype](sonatype.md)) — it scans repos, pipelines, and cloud rather than acting as an artifact proxy. Self-service onboarding is a core differentiator.

**Positioning & differentiators** — Differentiator is **consolidation + price + developer experience** for smaller teams: one tool covering many AppSec domains, low false-positive noise, fast setup. Contrast with [snyk](snyk.md) (dev-first but more enterprise/expensive, deeper per-domain), [endor-labs](endor-labs.md) (reachability-focused SCA), and the repository-anchored incumbents [jfrog](jfrog.md) and [sonatype](sonatype.md) (artifact store + supply-chain firewall, enterprise-grade, heavier). Aikido competes by being the easy, affordable all-in-one rather than best-of-breed in any single domain.

**Ownership, funding & M&A** — **Independent, venture-backed private company.** Founded **2022** in **Ghent, Belgium** by Willem Delbare, Roeland Delrue, and Felix Garriau. Funding: pre-seed €2M (Jan 2023), seed €5M (Nov 2023), Series A $17M (May 2024, led by Singular), **Series B $60M (Jan 2026) at a $1B valuation** led by DST Global with PSG Equity, Notion Capital, and Singular — reportedly the fastest European cybersecurity company to reach unicorn status. Total raised ~$84M. No acquirer; Aikido is the acquirer (small 2025 tuck-ins, e.g. the "Attack" pen-testing capability). (ownership_confidence: high.)

**CTO / hedge-fund lens** — **Day-1 candidate specifically for a small/mid-size fund shipping AI-generated code** that wants one affordable tool to cover SCA + SAST + secrets + cloud without standing up an enterprise AppSec stack. The consolidation and self-service model fit a 50-person shop better than [jfrog](jfrog.md)/[sonatype](sonatype.md)'s heavier platforms. Caveats: it is a scanner, not a blocking repository firewall (no quarantine-at-proxy); depth in any single domain is lighter than a best-of-breed specialist; and it's a young (2022) company — diligence the roadmap and support for regulated use. Good "good-enough, cheap, fast" choice; revisit if the software estate grows enough to need repository-level controls.

**Competitors / alternatives** — [snyk](snyk.md) (closest dev-first peer), [endor-labs](endor-labs.md), [sonatype](sonatype.md), [jfrog](jfrog.md); GitHub Advanced Security at the low end.

## Open questions / to verify
- Exact name/terms of the 2025 acquisition(s) behind "Aikido Attack."
- Depth of AI-specific scanning (model/LLM-aware checks) vs general AppSec.
- Suitability/compliance posture (SOC 2, data residency) for a regulated fund.

## Sources
- [Aikido Security — Wikipedia](https://en.wikipedia.org/wiki/Aikido_Security) — fetched 2026-06-28 — supports: founded 2022 Ghent, founders, full funding history incl. Series B $60M Jan 2026 at $1B, product scope (SCA/SAST/cloud/runtime); confidence: medium (secondary)
- [Aikido Security Raises $60 Million Series B at $1 Billion Valuation (Yahoo Finance / Sifted)](https://finance.yahoo.com/news/aikido-security-raises-60-million-130000609.html) — fetched 2026-06-28 — supports: $60M Series B, $1B valuation, DST Global lead + PSG/Notion/Singular, fastest EU cyber unicorn, total >$80M; confidence: medium

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed status, founded 2022 Ghent (Delbare/Delrue/Garriau), ~$84M total funding incl. $60M Series B (Jan 2026, $1B unicorn, DST Global lead), consolidated dev-first AppSec/SCA scope. ownership_confidence high.
