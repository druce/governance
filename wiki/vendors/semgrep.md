---
type: vendor
name: Semgrep
slug: semgrep
categories: [software-supply-chain]
layer: foundation
aliases: [r2c]
website: "https://semgrep.dev"
founded: 2017
hq: San Francisco, California, USA
ownership: independent
ownership_detail: Private, venture-backed. Total funding ~$193M; last round $100M Series D (Feb 2025, led by Menlo Ventures). Originally named r2c.
ownership_confidence: high
funding_total: ~$193M
last_funding: Series D, $100M, February 2025 (Menlo Ventures)
deployment: [saas, self-hosted, sdk]
target_customer: developer / AppSec teams, startups to enterprise; strong open-source adoption
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sast, sca, secrets-detection, appsec, open-source]
---

# Semgrep

> Primary category: [software-supply-chain](../categories/software-supply-chain.md). Formerly **r2c**.

**One-liner** — Fast, customizable static analysis (SAST) with a popular open-source engine, extended into a commercial platform covering dependencies (SCA) and secrets — known for low-noise, rule-driven scanning that developers actually run.

## What it does

Semgrep ("semantic grep") matches code patterns with lightweight, human-readable rules across 30+ languages. The platform has three commercial pillars:
- **Semgrep Code (SAST)** — first-party code analysis with custom rules and AI-assisted false-positive triage.
- **Semgrep Supply Chain (SCA)** — third-party dependency vulnerability scanning with reachability analysis to suppress unreachable-CVE noise.
- **Semgrep Secrets** — API key / credential leak detection.
The **Semgrep OSS** engine (released end of 2020) is free and widely used; it drives bottom-up developer adoption.

## Where it sits in the stack

[software-supply-chain](../categories/software-supply-chain.md), foundation layer. Relevance to **AI-generated code**: LLM-authored code is effectively **untrusted input** — Semgrep's custom rules can encode org-specific guardrails (banned APIs, insecure patterns, missing authz checks) that catch the kinds of mistakes AI assistants reproduce at scale, and its SCA leg flags vulnerable dependencies the model may pull in. Reachability helps keep the AI-amplified volume of findings actionable.

## Deployment & architecture

Open-source CLI engine (run locally or in CI). Commercial SaaS platform (self-hosted option available) with Git integrations (GitHub/GitLab/Bitbucket), PR/MR comments, CI/CD plugins, IDE feedback, and an API. Pricing is per-contributor/month (~$40 Code & Supply Chain, ~$20 Secrets) with a free tier under ~10 contributors — a notably developer- and SMB-friendly model.

## Positioning & differentiators

Best known for **customizable, low-false-positive SAST** and its open-source engine — the easiest of the [software-supply-chain](../categories/software-supply-chain.md) tools to tailor with your own rules. Versus [snyk](snyk.md): narrower than Snyk's full suite (less container/IaC depth) but lighter, cheaper, and more transparent/hackable; strong where teams want to write their own policy-as-code checks. Versus [socket](socket.md): Semgrep SCA is CVE/known-vuln + reachability oriented, whereas Socket targets *malicious* packages — complementary. Versus [endor-labs](endor-labs.md): both emphasize reachability/SCA, but Semgrep leads with SAST and OSS adoption while Endor leads with dependency/reachability depth. Versus [aikido-security](aikido-security.md): Aikido bundles many scanners for SMBs; Semgrep is more of a best-of-breed SAST engine.

## Ownership, funding & M&A

Independent, private, venture-backed. Founded 2017 as **r2c** by Isaac Evans (CEO), Drew Dennison (CTO), and Luke O'Malley (CPO); HQ San Francisco. Total funding ~$193M; most recent round a **$100M Series D in February 2025 led by Menlo Ventures**, with existing investors Felicis, Harpoon, Lightspeed, Redpoint, and Sequoia participating. No acquisitions or M&A of note; no IPO. (ownership_confidence: high.)

## CTO / hedge-fund lens

**Day-2 baseline, Day-1 if your devs ship AI-generated code.** Semgrep is a strong fit for a fund's engineering team that wants policy-as-code: encode your own rules (no eval of untrusted data, required authz, banned crypto) and run them in CI against both human- and AI-written code. The free OSS engine plus per-contributor pricing makes it cost-effective for small teams (sub-50 eng), and self-hosting suits regulated/air-gapped environments. Often paired with [socket](socket.md) for malicious-package coverage. Model-risk relevance is light/indirect — it governs code quality/security, not model behavior or SR 11-7 model risk.

## Competitors / alternatives

[snyk](snyk.md), [socket](socket.md), [endor-labs](endor-labs.md), [aikido-security](aikido-security.md); GitHub Advanced Security / CodeQL (not yet a page).

## Open questions / to verify

- Current ARR / customer count (not established here).
- Depth of container/IaC coverage relative to [snyk](snyk.md) (Semgrep is primarily code + dependencies + secrets).

## Sources
- [Semgrep Business Breakdown & Founding Story — Contrary Research](https://research.contrary.com/company/semgrep) — fetched 2026-06-28 — supports: founded 2017 (r2c), founders, SF HQ, ~$193M total, Series D $100M Feb 2025 (Menlo), product modules, per-contributor pricing; confidence: high
- [Semgrep / r2c — Crunchbase + search synthesis](https://www.crunchbase.com/organization/r2c) — fetched 2026-06-28 — supports: r2c→Semgrep rename, Series D $100M Feb 2025 led by Menlo Ventures, OSS engine released end 2020; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/private VC-backed, founded 2017 as r2c (SF HQ), ~$193M raised, Series D $100M Feb 2025 (Menlo Ventures); SAST+SCA+Secrets with open-source engine; ownership_confidence high. hedge_fund_fit medium (Day-1 if shipping AI-generated code).
