---
title: Checkmarx
type: vendor
name: Checkmarx
slug: checkmarx
aka: [Checkmarx One, Checkmarx Ltd.]
primary_category: software-supply-chain
also_listed_in: []
website: https://checkmarx.com/
founded: 2006
hq: Ramat Gan, Israel (US HQ Paramus, NJ)
ownership_state: pe-owned
owner: Hellman & Friedman
ownership_note: H&F acquired Checkmarx from Insight Partners in an all-cash deal valued at $1.15B, completed 2020-04. TPG holds a minority stake alongside Insight. CEO Sandeep Johri since 2023 (succeeded founder Emmanuel Benzaquen).
acquisition: {announced: 2020-03, closed: 2020-04, price: $1.15B}
funding_total: null
last_funding: null
market_position: {software-supply-chain: leader}
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
tags: [appsec, sast, sca, aspm, incumbent, pe-owned]
sources:
  - {claim: "H&F completed acquisition of Checkmarx from Insight Partners, $1.15B all cash; TPG minority", url: "https://checkmarx.com/press-releases/hellman-friedman-completes-acquisition-of-checkmarx/", date: 2026-08-26, confidence: high}
  - {claim: "Checkmarx ASPM aggregates SAST, SCA, IaC, API, DAST, container and supply-chain signals into Checkmarx One; Tromzo reasoning engine folded in to power Checkmarx Assist agents from early 2026", url: "https://checkmarx.com/product/aspm/", date: 2026-08-26, confidence: medium}
---

# Checkmarx

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — The AppSec incumbent: an enterprise application-security platform (Checkmarx One) built around SAST, now bundling SCA, IaC, API, DAST, container and supply-chain scanning under a single ASPM posture lens.

**What it does** — Checkmarx made its name in **static application security testing (SAST)** and has spent the last five years assembling the rest of the AppSec stack around it. Checkmarx One is the unified platform; **Checkmarx ASPM** is the correlation layer that aggregates findings from all of those scanners into one risk-ranked view rather than eight separate alert queues. In late 2025 it absorbed **Tromzo**'s reasoning engine and engineering team, which powers the **Checkmarx Assist** agents shipping from early 2026 — the company's move toward autonomous triage and remediation.

**Naming / provenance** — Founded 2006 in Israel by Emmanuel Benzaquen and Maty Siman. Single brand throughout; the platform was renamed from "Checkmarx CxSAST/CxSCA" to **Checkmarx One** in 2022. Not to be confused with Checkmate or Checkmarx's own reseller-branded OEM deployments.

**Ownership & viability** — `pe-owned`. **Hellman & Friedman** acquired Checkmarx from **Insight Partners** in 2020 in an all-cash transaction valued at **$1.15B**; **TPG** took a minority stake alongside Insight. Sandeep Johri replaced founder Emmanuel Benzaquen as CEO in 2023. Six years into an H&F hold is late in a typical PE cycle — a sale or IPO is a live possibility, and the Tromzo tuck-in reads as pre-exit story-building. Not a viability risk; is an ownership-churn risk.

**Positioning & differentiators** —
- **SAST depth over breadth-first.** Where [snyk](snyk.md) and [aikido-security](aikido-security.md) won developers with fast, cheap, wide coverage, Checkmarx's pitch is the depth and low false-positive rate of its static engine on large legacy codebases — the C#/Java/COBOL-adjacent estate a bank or fund actually runs.
- **ASPM as the consolidation play.** Same strategic bet as [apiiro](apiiro.md) and [legit-security](legit-security.md), but made from the position of already owning the scanners rather than correlating someone else's.
- **Enterprise procurement fit.** On-prem/self-hosted deployment is a first-class option, not an afterthought — which matters where [snyk](snyk.md) and the SaaS-only AI-natives struggle.
- **Not AI-native.** AI-generated-code risk is a 2025-26 product bolt-on here, not the founding thesis it is at [endor-labs](endor-labs.md) or [socket](socket.md).

**Who should choose them / anti-fit** — Fits a firm with a **large, long-lived in-house codebase** and a security team that must satisfy auditors with a named commercial AST tool. Also fits where self-hosting is mandated. **Anti-fit:** a small quant team shipping mostly Python/notebooks and gluing together AI-generated services — the license cost and rollout weight are wrong for that shape; [semgrep](semgrep.md) or [aikido-security](aikido-security.md) fit better.

**Known weaknesses / gotchas** — Heavier to deploy and tune than the developer-first tools; historically criticised for scan times and false-positive volume on large repos (the exact axis the AI-native competitors attack). Pricing is enterprise-negotiated and opaque. Ownership churn risk per above.

**Deployment & data handling** — SaaS (Checkmarx One) and self-hosted/on-prem. Whether source code leaves the tenancy under the SaaS model, and retention/training-use terms, are **unverified** — this is the specific question a fund with proprietary trading code must ask before signing.

**Integrations & partnerships** — CI/CD (Jenkins, GitHub Actions, GitLab CI, Azure DevOps), SCM, IDE plugins, ticketing. Detailed integration list and MCP/agent-framework support unverified.

**Compliance & FS traction** — Long-standing financial-services install base is widely claimed but **not independently verified here**; no named FS references confirmed. Certifications held (vs. frameworks supported) unverified.

**Commercial** — Not public. Enterprise subscription, typically priced per developer or per application.

## Open questions

- Does source code leave the tenancy under Checkmarx One SaaS? Retention and training-use terms?
- Certifications actually held (SOC 2, ISO 27001, FedRAMP status).
- Named financial-services customers; hedge-fund-scale references.
- Current ARR / scale, and whether an H&F exit is in motion.
- MCP support and agent-framework hooks for the Checkmarx Assist agents.

## Sources

- [Hellman & Friedman Completes Acquisition of Checkmarx (Checkmarx press release)](https://checkmarx.com/press-releases/hellman-friedman-completes-acquisition-of-checkmarx/) — fetched 2026-08-26 — supports: ownership, price, TPG/Insight minority; confidence: high
- [Checkmarx ASPM product page](https://checkmarx.com/product/aspm/) — fetched 2026-08-26 — supports: platform scope, Tromzo/Checkmarx Assist; confidence: medium (vendor marketing)
- Cached: `raw/sources/2026-08-26--checkmarx--ownership-and-platform.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (`reports/competitor-scan-2026-08-25/candidates.md`, Tier A, score 10) — surfaced as a peer by four wiki vendors and confirmed as a genuine category gap.
