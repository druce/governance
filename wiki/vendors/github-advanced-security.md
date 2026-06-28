---
title: GitHub Advanced Security
type: vendor
name: GitHub Advanced Security
slug: github-advanced-security
categories: [software-supply-chain]
layer: foundation
aliases: [GHAS, GitHub Code Security, GitHub Secret Protection]
website: "https://github.com/security/advanced-security"
founded: 2008                       # GitHub, the parent product; GHAS launched later
hq: San Francisco, CA, USA
ownership: subsidiary
ownership_detail: Product of GitHub, a subsidiary of Microsoft (Microsoft acq. GitHub 2018-10, closed; announced 2018-06)
ownership_confidence: high
funding_total:                      # n/a — product within Microsoft/GitHub
last_funding:                       # n/a
deployment: [saas, self-hosted]     # GitHub.com SaaS + GitHub Enterprise Server (self-managed)
target_customer: enterprise / mid-market (GitHub Team & Enterprise orgs)
hedge_fund_fit: high
priority: day-2
trifecta_relevance: [none]          # supply-chain/code-security control; not a runtime AI-trifecta gate
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sast, secret-scanning, sca, code-scanning, codeql, copilot-autofix, devsecops]
---

# GitHub Advanced Security

> Primary category: [software-supply-chain](../categories/software-supply-chain.md) (foundation layer).

**One-liner** — Platform-native application/code security built into GitHub: SAST (CodeQL), secret scanning, and dependency review/Dependabot, now sold as two purchasable products (GitHub Code Security and GitHub Secret Protection).

**Categories** — [software-supply-chain](../categories/software-supply-chain.md)

## What it does
GitHub Advanced Security (GHAS) is the paid security layer that runs inside the GitHub source-control and CI/CD platform. It bundles the main classes of code-security scanning:

- **Code scanning / SAST** — static analysis powered by CodeQL (or third-party engines) to find vulnerabilities and coding errors in pull requests and on push.
- **Secret scanning + push protection** — detects exposed credentials, keys and tokens (including AI-powered detection of unstructured secrets) and can block commits that would leak them.
- **Dependency review + Dependabot** — surfaces vulnerable open-source dependencies, alerts on them, and opens automated update PRs (software composition analysis / SCA).
- **Copilot Autofix** — AI-generated remediation suggestions attached directly to code-scanning and secret alerts.

Because it lives in the repo and the CI pipeline, scanning happens where developers already work — findings appear as PR checks and in a security-overview dashboard rather than in a separate console.

## Where it sits in the stack
This is a [software-supply-chain](../categories/software-supply-chain.md) / foundation-layer control: it secures the code and dependencies that flow into everything else, before runtime. It does not address the lethal trifecta directly (it is not an inline prompt/egress gate), hence `trifecta_relevance: none`.

**AI-generated-code relevance:** when developers accept code from Copilot, Cursor, or Claude, that code lands in the same repos GHAS already scans. CodeQL/SAST and secret scanning catch insecure or credential-leaking AI output at the PR gate, and **Copilot Autofix** proposes fixes inline — so for shops on GitHub this is often the lowest-friction way to put a guardrail under AI-assisted development.

## Deployment & architecture
- **SaaS** on GitHub.com (Team and Enterprise Cloud orgs) and **self-hosted** on GitHub Enterprise Server.
- Runs as part of repo settings + GitHub Actions CI; results integrate with the GitHub security-overview dashboard, SARIF-compatible third-party scanners, code owners, and branch protection.
- Code and secret scanning are enabled by default on public repos; private-repo scanning requires purchasing the relevant product.

## Positioning & differentiators
GHAS's edge is that it is **platform-native**: nothing new to deploy, findings sit in the PR, and Copilot Autofix is tightly wired in. The tradeoff versus standalone scanners — [snyk](snyk.md), [semgrep](semgrep.md) — is breadth and depth of engine, policy flexibility, and multi-SCM coverage; dedicated tools often go deeper on SCA/SAST and work across GitHub, GitLab and Bitbucket alike. Its closest platform-native peer is [gitlab](gitlab.md) (GitLab Ultimate), which bundles a similar scanner set for teams on GitLab instead of GitHub.

**2025 repackaging (verify-worthy):** GitHub split GHAS into two separately purchasable products — **GitHub Secret Protection** ($19/active committer/mo) and **GitHub Code Security** ($30/active committer/mo) — announced 2025-03-04, available to Team-plan customers from 2025-04-01 via metered/pay-as-you-go billing. This lets teams buy secret scanning without paying for the full SAST/SCA suite, and extended these features below the Enterprise tier for the first time. The umbrella term "GitHub Advanced Security" still refers to the combined capability set.

## Ownership, funding & M&A
GHAS is a product, not a company. It is part of **GitHub**, which **Microsoft acquired** (announced 2018-06-04, closed 2018-10-26 for ~$7.5B in stock). Ownership: subsidiary (Microsoft → GitHub). Confidence: high (well-documented, primary).

## CTO / hedge-fund lens
- **Day-2 in general, Day-1 if you ship AI-generated code.** If your developers are already on GitHub and using Copilot/Cursor/Claude, turning on Code Security + Secret Protection is usually the path of least resistance for code-level guardrails — it is a **tier/product upgrade on tooling you already own, not a new vendor** to onboard, contract, and integrate.
- Granular per-committer metered pricing makes it easy to start with just secret scanning (cheap, high-value) and add SAST/SCA later.
- Relevant to SR 11-7-style model-risk hygiene only indirectly (it secures the code that builds AI systems; it is not a model-risk control itself).
- Fit is **high** for GitHub-centric shops; near-zero if you are standardized on GitLab or Bitbucket (use [gitlab](gitlab.md) Ultimate or [snyk](snyk.md)/[semgrep](semgrep.md) instead).

## Competitors / alternatives
[gitlab](gitlab.md) · [snyk](snyk.md) · [semgrep](semgrep.md)

## Open questions / to verify
- Exact current CodeQL language coverage and any 2026 pricing changes.
- Whether GHAS on GitHub Enterprise Server has feature parity with Cloud for the new product split.
- Copilot Autofix accuracy / false-positive data from independent sources (vendor claims are marketing).

## Sources
- [Introducing GitHub Secret Protection and GitHub Code Security — GitHub Changelog](https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/) — fetched 2026-06-28 — supports: 2025 repackaging into two purchasable products, features, pricing, dates; confidence: high (primary).
- [About GitHub Advanced Security — GitHub Docs](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) — fetched 2026-06-28 — supports: GHAS components (CodeQL SAST, secret scanning, Dependabot/dependency review, Copilot Autofix), Secret Protection vs Code Security packaging; confidence: high (primary).

## History
- [2026-06-28] Researched; established Microsoft/GitHub subsidiary ownership (high confidence), 2025 split into GitHub Secret Protection + GitHub Code Security, component features (CodeQL SAST, secret scanning, Dependabot, Copilot Autofix), SaaS + Enterprise Server deployment, Day-1-for-AI-code hedge-fund lens. status stub -> researched.
- [2026-06-28] Stub created from seed registry.
