---
title: GitHub Advanced Security
type: vendor
name: GitHub Advanced Security
slug: github-advanced-security
aka: [GHAS, GitHub Code Security, GitHub Secret Protection, CodeQL]
primary_category: software-supply-chain
also_listed_in: []
website: https://github.com/security/advanced-security
founded: 2008
hq: San Francisco, CA, USA
ownership_state: acquired-closed
owner: Microsoft
ownership_note: 'Product of GitHub, a wholly-owned subsidiary of Microsoft (NASDAQ: MSFT) — announced 2018-06-04, closed 2018-10-25, $7.5B in Microsoft stock (inclusive of $1.3B cash for vested GitHub equity awards and an indemnity escrow); $6,924M allocated as purchase price under ASC 805.'
acquisition: {announced: 2018-06-04, closed: 2018-10-25, price: '$7.5B in Microsoft stock ($6,924M purchase price allocated; Microsoft FY2019 10-K Note 8)'}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas, self-hosted]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / mid-market (GitHub Team & Enterprise orgs)
last_verified: 2026-07-27
verify_after: null
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
This is a [software-supply-chain](../categories/software-supply-chain.md) / foundation-layer control: it secures the code and dependencies that flow into everything else, before runtime. It is not an inline prompt/egress control.

**AI-generated-code relevance:** when developers accept code from Copilot, Cursor, or Claude, that code lands in the same repos GHAS already scans. CodeQL/SAST and secret scanning catch insecure or credential-leaking AI output at the PR gate, and **Copilot Autofix** proposes fixes inline — so for shops on GitHub this is often the lowest-friction way to put a guardrail under AI-assisted development.

## Deployment & architecture
- **SaaS** on GitHub.com (Team and Enterprise Cloud orgs) and **self-hosted** on GitHub Enterprise Server.
- Runs as part of repo settings + GitHub Actions CI; results integrate with the GitHub security-overview dashboard, SARIF-compatible third-party scanners, code owners, and branch protection.
- Code and secret scanning are enabled by default on public repos; private-repo scanning requires purchasing the relevant product.

## Positioning & differentiators
GHAS's edge is that it is **platform-native**: nothing new to deploy, findings sit in the PR, and Copilot Autofix is tightly wired in. The tradeoff versus standalone scanners — [snyk](snyk.md), [semgrep](semgrep.md) — is breadth and depth of engine, policy flexibility, and multi-SCM coverage; dedicated tools often go deeper on SCA/SAST and work across GitHub, GitLab and Bitbucket alike. Its closest platform-native peer is [gitlab](gitlab.md) (GitLab Ultimate), which bundles a similar scanner set for teams on GitLab instead of GitHub.

**2025 repackaging (verify-worthy):** GitHub split GHAS into two separately purchasable products — **GitHub Secret Protection** ($19/active committer/mo) and **GitHub Code Security** ($30/active committer/mo) — announced 2025-03-04, available to Team-plan customers from 2025-04-01 via metered/pay-as-you-go billing. This lets teams buy secret scanning without paying for the full SAST/SCA suite, and extended these features below the Enterprise tier for the first time. The umbrella term "GitHub Advanced Security" still refers to the combined capability set.

## Ownership, funding & M&A
GHAS is a product, not a company. It is part of **GitHub**, which **Microsoft acquired** — announced **2018-06-04** (Form 8-K, Item 8.01, same-day press release: "Microsoft will acquire GitHub for $7.5 billion in Microsoft stock ... subject to customary closing conditions and completion of regulatory review") and closed **2018-10-25** (Microsoft FY2019 10-K, Note 8). Ownership: subsidiary (Microsoft → GitHub). Confidence: high (primary SEC filings).

Two details worth carrying: the headline $7.5B was all-stock **except** a $1.3B cash component covering vested GitHub equity awards and an indemnity escrow, and the amount actually allocated in purchase accounting was **$6,924M** (goodwill $5,497M, intangibles $1,267M, assigned to Intelligent Cloud) — the ~$600M difference was recognized separately as post-combination compensation expense.

> Date trap: most secondary coverage dates the close to 2018-10-26, but that is the day *completion was announced* (both the Microsoft blog post and Nat Friedman's GitHub post are dated 10-26 and neither states a closing date). Microsoft's SEC filings say **October 25, 2018**, twice and consistently.

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
- [Microsoft Form 10-K, FY2019](https://www.sec.gov/Archives/edgar/data/789019/000156459019027952/msft-10k_20190630.htm), Note 8 *Business Combinations* — fetched 2026-07-27 — supports: **close date 2018-10-25**, $7.5B stock transaction inclusive of $1.3B cash, $6,924M purchase price allocated, goodwill $5,497M / intangibles $1,267M, Intelligent Cloud segment; confidence: high (primary, audited). Cached: `raw/sources/2026-07-27--github-advanced-security--microsoft-github-deal-dates.md`
- [Microsoft Form 8-K (2018-06-04)](https://www.sec.gov/Archives/edgar/data/789019/000119312518182975/d600091d8k.htm) + [press-release exhibit 99.1](https://www.sec.gov/Archives/edgar/data/789019/000119312518182975/d600091dex991.htm) — fetched 2026-07-27 — supports: **announce date 2018-06-04**, $7.5B in Microsoft stock, and explicit pending language ("subject to customary closing conditions and completion of regulatory review"); confidence: high (primary)
- [Microsoft FY2019 Q2 Form 10-Q (quarter ended 2018-12-31)](https://www.sec.gov/Archives/edgar/data/789019/000156459019001392/msft-10q_20181231.htm), Note 7 — fetched 2026-07-27 — supports: contemporaneous corroboration of the 2018-10-25 close date; confidence: high (primary)

## History
- [2026-06-28] Researched; established Microsoft/GitHub subsidiary ownership (high confidence), 2025 split into GitHub Secret Protection + GitHub Code Security, component features (CodeQL SAST, secret scanning, Dependabot, Copilot Autofix), SaaS + Enterprise Server deployment, Day-1-for-AI-code hedge-fund lens. status stub -> researched.
- [2026-06-28] Stub created from seed registry.
- [2026-07-27] Date-sanity sweep — **fixed transposed acquisition dates**. Frontmatter read `{announced: 2018-10-01, closed: 2018-06-01}`, i.e. the deal closed four months *before* it was announced — impossible, and contradicted by the page's own `ownership_note`, which had the direction right but only month precision. Verified against Microsoft's SEC filings: Form 8-K dated 2018-06-04 announces the definitive agreement with explicit pending language, and the FY2019 10-K (Note 8) plus FY2019 Q2 10-Q (Note 7) both state the acquisition closed **2018-10-25**. Corrected to `{announced: 2018-06-04, closed: 2018-10-25}` and filled the null `price` ($7.5B in stock; $6,924M allocated purchase price). Added a note on the common 10-25 vs 10-26 confusion — 10-26 is the day completion was *announced*, not the closing date. Cached 1 new source.
