---
title: GitLab (Ultimate)
type: vendor
name: GitLab (Ultimate)
slug: gitlab
categories: [software-supply-chain]
layer: foundation
aliases: [GitLab Ultimate, GitLab Inc., GTLB]
website: "https://about.gitlab.com"
founded: 2014
hq: San Francisco, CA, USA (all-remote company)
ownership: public
ownership_detail: "Public, NASDAQ: GTLB (IPO 2021-10-14). Datadog acquisition reported/rumored (Reuters 2024-07; renewed buzz Oct 2025) but UNCONFIRMED — no definitive agreement as of 2026-06-28."
ownership_confidence: high
funding_total:                      # n/a — public; IPO at ~$10B valuation (2021)
last_funding: "IPO 2021-10-14 (NASDAQ: GTLB), ~$10B valuation"
deployment: [saas, self-hosted, on-prem]   # GitLab.com SaaS + self-managed (Dedicated/self-hosted)
target_customer: enterprise / mid-market (DevSecOps platform buyers)
hedge_fund_fit: high
priority: day-2
trifecta_relevance: [none]          # supply-chain/code-security control; not a runtime AI-trifecta gate
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sast, dast, sca, secret-detection, container-scanning, license-compliance, devsecops]
---

# GitLab (Ultimate)

> Primary category: [software-supply-chain](../categories/software-supply-chain.md) (foundation layer).

**One-liner** — The DevSecOps platform whose top tier, **GitLab Ultimate**, bundles platform-native application security — SAST, DAST, dependency scanning, secret detection, container scanning, and license compliance — directly into the SCM and CI/CD pipeline.

**Categories** — [software-supply-chain](../categories/software-supply-chain.md)

## What it does
GitLab is an end-to-end software-development platform (source control, CI/CD, issue tracking, registry). Its security scanning is gated behind the **Ultimate** tier and runs as pipeline jobs:

- **SAST** — static analysis of source for vulnerabilities.
- **DAST** — dynamic testing of running applications.
- **Dependency scanning** — SCA over open-source dependencies.
- **Secret detection** — finds committed credentials/keys/tokens.
- **Container scanning** — vulnerabilities in built container images.
- **License compliance** — flags disallowed open-source licenses.

Findings surface in the merge-request UI and in a security dashboard, so review happens where developers already work rather than in a separate console.

## Where it sits in the stack
A [software-supply-chain](../categories/software-supply-chain.md) / foundation-layer control: it secures code, dependencies and container images before runtime. It is not an inline prompt/egress gate, so `trifecta_relevance: none`.

**AI-generated-code relevance:** code accepted from Copilot, Cursor, or Claude lands in the same GitLab repos and pipelines. Ultimate's SAST/SCA/secret detection inspect that code at the merge-request gate — for GitLab-standardized shops this is usually the least-friction way to put a guardrail under AI-assisted development (the scanners are already in the CI).

## Deployment & architecture
- **SaaS** on GitLab.com, **GitLab Dedicated** (single-tenant SaaS), and **self-managed** (self-hosted / on-prem) installs.
- Security scanners run as GitLab CI pipeline jobs; results integrate with merge requests, the security dashboard, compliance frameworks, and the container registry.
- All-remote company; product spans the full DevSecOps lifecycle in one platform.

## Positioning & differentiators
GitLab's pitch is the **single integrated platform**: SCM + CI/CD + security in one tool, versus stitching together point products. Its scanner suite is **platform-native** — the direct analog to [github-advanced-security](github-advanced-security.md) but for teams on GitLab. The tradeoff versus standalone scanners — [snyk](snyk.md), [semgrep](semgrep.md) — is engine depth, policy flexibility and cross-SCM reach; dedicated tools often go deeper on SAST/SCA and run across multiple platforms, whereas GitLab's security is most compelling when you have already committed to GitLab as your DevOps platform.

## Ownership, funding & M&A
GitLab Inc. is an **independent public company** (NASDAQ: **GTLB**), founded 2014 by Dmytro Zaporozhets and Sytse "Sid" Sijbrandij, IPO'd 2021-10-14 at roughly a $10B valuation; HQ San Francisco, all-remote. Ownership (public): high confidence.

**M&A status — verified UNCONFIRMED.** Acquisition interest has been reported repeatedly: Reuters (2024-07) reported GitLab was exploring a sale with Datadog as an interested party; renewed buzz in October 2025 cited a possible Datadog offer near $60/share (GTLB rose ~10%). Neither company has confirmed, and analysts (e.g. Wolfe Research) have publicly doubted the deal will close. No definitive merger agreement or SEC 8-K announcing an acquisition was located as of 2026-06-28. Treat the Datadog deal as rumor, not fact; ownership remains **public**.

## CTO / hedge-fund lens
- **Day-2 in general, Day-1 if you ship AI-generated code.** If your developers are on GitLab and using Copilot/Cursor/Claude, enabling Ultimate's scanners is typically the path of least resistance for code-level guardrails — a **tier upgrade on a platform you already run, not a new vendor** to procure and integrate.
- Watch the pricing model: security is bundled into the **Ultimate** tier, so adopting it can mean a platform-wide seat upgrade rather than a metered add-on (contrast with [github-advanced-security](github-advanced-security.md)'s per-committer product split).
- Indirectly relevant to SR 11-7-style hygiene (it secures the code that builds AI systems; not a model-risk control itself).
- **Keep the Datadog acquisition rumor on the radar** for vendor-concentration/continuity diligence, but do not treat it as decided.
- Fit is **high** for GitLab-centric shops; low if you are standardized on GitHub (use [github-advanced-security](github-advanced-security.md)) or want a cross-SCM scanner ([snyk](snyk.md), [semgrep](semgrep.md)).

## Competitors / alternatives
[github-advanced-security](github-advanced-security.md) · [snyk](snyk.md) · [semgrep](semgrep.md)

## Open questions / to verify
- Resolution of the Datadog acquisition rumor (watch for an 8-K / definitive agreement).
- Current Ultimate per-seat pricing and any 2026 changes.
- Depth/parity of GitLab's AI-assisted remediation (GitLab Duo) versus GitHub Copilot Autofix — independent benchmarks (vendor claims are marketing).

## Sources
- [GitLab Inc. — Wikipedia](https://en.wikipedia.org/wiki/GitLab_Inc.) — fetched 2026-06-28 — supports: founding (2014, Zaporozhets & Sijbrandij), all-remote HQ, IPO 2021-10-14 NASDAQ GTLB ~$10B, public ownership, Datadog sale rumor origin; confidence: high.
- [GitLab users cautiously optimistic on Datadog DevSecOps deal — TechTarget](https://www.techtarget.com/searchITOperations/news/366596593/GitLab-users-cautiously-optimistic-on-Datadog-DevSecOps-deal) — fetched 2026-06-28 — supports: Datadog acquisition is rumored/exploratory and unconfirmed, no definitive agreement; confidence: medium (secondary, corroborated).

## History
- [2026-06-28] Researched; established public ownership (NASDAQ: GTLB, IPO 2021-10-14), 2014 founding, all-remote SF HQ, GitLab Ultimate security suite (SAST/DAST/dependency/secret/container/license), SaaS+self-managed deployment, Day-1-for-AI-code lens. Verified Datadog acquisition as UNCONFIRMED rumor (no definitive agreement as of 2026-06-28); ownership kept public. status stub -> researched.
- [2026-06-28] Stub created from seed registry.
