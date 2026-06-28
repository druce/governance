---
type: vendor
name: Socket
slug: socket
categories: [software-supply-chain]
layer: foundation
aliases: [Socket.dev]
website: "https://socket.dev"
founded: 2020
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Private, venture-backed. Total funding ~$65M; last round $40M Series B (Oct 2024, led by Abstract Ventures, with Elad Gil and a16z).
ownership_confidence: high
funding_total: ~$65M
last_funding: Series B, $40M, October 2024 (Abstract Ventures, Elad Gil, a16z)
deployment: [saas, api]
target_customer: engineering orgs with heavy open-source / npm + PyPI use; startups to enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [malicious-packages, npm, pypi, supply-chain-attacks, typosquatting, sca]
---

# Socket

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — Supply-chain security that catches *malicious* open-source packages — backdoors, typosquats, install-script abuse, obfuscated code — before they land in your codebase, rather than just flagging known CVEs.

## What it does

Socket inspects the actual behavior and metadata of open-source packages (npm, PyPI, and other ecosystems) to detect **active threats**: malware, hidden backdoors, typo-squatted package names, suspicious install scripts, credential/token exfiltration, and risky permission changes between versions. This is a different job from CVE-based scanning: Socket is built for the **novel, malicious-package attack** — the npm/PyPI compromises that don't have a CVE yet. It claims to block 100+ supply-chain attacks per week and is frequently the **first public discloser** of major npm campaigns (e.g. the 2025 "Shai-Hulud" worm, the "Qix" maintainer phishing compromise, and "SANDWORM_MODE"), several later echoed by CISA.

## Where it sits in the stack

[software-supply-chain](../categories/software-supply-chain.md), foundation layer. Relevance to **AI-generated code**: this is exactly the **untrusted-input** vector that AI coding assistants amplify. LLMs hallucinate plausible-but-nonexistent package names ("slopsquatting"), which attackers pre-register with malware; LLMs also confidently suggest installing obscure packages. Socket's behavioral, malicious-package focus is the control aimed at that threat — complementary to CVE scanners like [snyk](snyk.md) and [semgrep](semgrep.md), which would not flag a brand-new malicious package.

## Deployment & architecture

SaaS. Primary surface is a **GitHub App** that posts pull-request comments/alerts when a dependency change introduces risk, plus a **CLI** (`socket`) for local/CI use and an API. Also offers IDE feedback and registry/firewall-style controls to block bad packages at install time. Lightweight to adopt — no need to instrument the whole codebase; it gates dependency changes.

## Positioning & differentiators

The category leader for **malicious-package / active-supply-chain-attack detection**, distinct from the known-CVE SCA done by [snyk](snyk.md), [semgrep](semgrep.md), and [endor-labs](endor-labs.md). Where those answer "does this dependency have a published vulnerability?", Socket answers "is this dependency *trying to attack me*?" Founder/CEO Feross Aboukhadijeh is a well-known open-source author (WebTorrent, StandardJS), which underpins its credibility and ecosystem reach. Best used **alongside** a CVE scanner, not instead of one. Versus [aikido-security](aikido-security.md) (which bundles many scanner types for SMBs), Socket is the specialist on the malicious-package leg.

## Ownership, funding & M&A

Independent, private, venture-backed. Founded ~2020; HQ San Francisco; founder/CEO Feross Aboukhadijeh. Total funding ~$65M; most recent round a **$40M Series B in October 2024**, led by Abstract Ventures with participation from Elad Gil, Andreessen Horowitz (a16z), and angels including Bret Taylor. No M&A; no IPO. Reported scale: 7,500+ organizations and 300,000+ GitHub repos protected. (ownership_confidence: high. Founding year ~2020 is approximate — not confirmed against an incorporation record here.)

## CTO / hedge-fund lens

**Day-2 baseline, Day-1 if your devs ship AI-generated code** — and arguably the single highest-leverage add precisely because AI assistants increase the odds of pulling in a hallucinated or malicious package. It is cheap to deploy (a GitHub App on your repos) and low-friction, so even a small fund (sub-50 eng) can adopt it. The recommended posture is **Socket for malicious packages + [snyk](snyk.md) or [semgrep](semgrep.md) for known CVEs and SAST** — they cover different halves of the supply-chain problem. Model-risk relevance is light/indirect: it doesn't touch SR 11-7 model governance, but it directly mitigates a fast-growing AI-coding-era attack surface.

## Competitors / alternatives

[snyk](snyk.md), [semgrep](semgrep.md), [endor-labs](endor-labs.md), [aikido-security](aikido-security.md); GitHub Dependabot (CVE-only, different scope; not yet a page).

## Open questions / to verify

- Exact incorporation/founding year (using ~2020; not confirmed against a primary registration record).
- Whether the "firewall"/install-time blocking is GA across all supported ecosystems vs. detection-only in some.

## Sources
- [Socket secures $40M Series B — Socket blog](https://socket.dev/blog/series-b) — fetched 2026-06-28 — supports: $40M Series B Oct 2024 (Abstract Ventures, Elad Gil, a16z), $65M total, Feross Aboukhadijeh CEO, SF HQ, malicious-package detection, GitHub App/CLI, 7,500+ orgs; confidence: high (vendor primary)
- [Widespread Supply Chain Compromise Impacting npm — CISA + Socket disclosures](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) — fetched 2026-06-28 — supports: Socket as first-responder/discloser of major 2025 npm attacks (Shai-Hulud, Qix, SANDWORM_MODE); confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/private VC-backed, founded ~2020 (SF HQ, CEO Feross Aboukhadijeh), ~$65M raised, Series B $40M Oct 2024 (Abstract Ventures/Elad Gil/a16z); specialist in malicious open-source package detection (npm/PyPI), distinct from CVE scanners; ownership_confidence high. hedge_fund_fit medium (Day-1 if shipping AI-generated code — directly mitigates slopsquatting).
