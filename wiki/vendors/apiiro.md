---
type: vendor
name: Apiiro
slug: apiiro
categories: [software-supply-chain]
layer: foundation
aliases: []
website: https://apiiro.com
founded: 2019
hq: Tel Aviv, Israel (with New York, USA presence)
ownership: independent
ownership_detail: Venture-backed, independent as of 2026-06-28. $100M Series B (Nov 2022) led by General Catalyst.
ownership_confidence: high
funding_total: ~$135M
last_funding: Series B, $100M, 2022-11-03 (General Catalyst)
deployment: [saas, api]
target_customer: large enterprise (USAA, BlackRock, JPMorgan Chase, Shell cited)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [aspm, deep-code-analysis, risk-graph, sdlc, sbom]
---

# Apiiro

**One-liner** — A "deep code analysis" ASPM platform that builds a Risk Graph from design through runtime, so AppSec teams can see, prioritize, and auto-fix application risk across the whole SDLC — not just scanner findings.

**Categories** — [software-supply-chain](../categories/software-supply-chain.md) (primary)

## What it does
Apiiro is an **Application Security Posture Management (ASPM)** platform. Its core technology is **Deep Code Analysis (DCA)** feeding a **Risk Graph** that connects findings from code to runtime with context (who owns it, what data it touches, whether it's internet-facing). Distinctively, it starts at the **design phase** — analyzing feature requests/user stories to flag risky features before code is written — and runs through develop (code-to-runtime fixing, AutoFix agents) and deliver (SCM/CI-CD protection). It includes native scanners (secrets, open source, supply chain), an extended SBOM (XBOM), unified risk/vuln management across third-party scanners, and a policy/governance engine. Recent positioning leans "agentic" with automated remediation agents.

## Where it sits in the stack
[software-supply-chain](../categories/software-supply-chain.md) at the **foundation** layer, but Apiiro's scope is broader than pure SCA — it's an orchestration/posture layer *over* the SDLC. Trifecta role spans **untrusted input** (third-party + AI-generated code/dependencies entering the build) and **sensitive data** (the Risk Graph flags code paths touching sensitive data / PII). For AI-generated code, the relevance is its risk-graph context and design-phase analysis: it aims to govern the *materiality* of changes (including AI-authored ones) rather than just scan diffs.

## Deployment & architecture
SaaS, integrating via API into SCMs (GitHub/GitLab/Bitbucket/Azure DevOps), CI/CD, ticketing, and existing scanners whose output it normalizes into the Risk Graph. Not an inline runtime control — it's an analysis/posture plane over the dev pipeline.

## Positioning & differentiators
Apiiro's wedge is **deep code analysis + risk graph context and design-time risk detection**, versus tools that start from scanner findings. Against [legit-security](legit-security.md) — its closest ASPM neighbor — Apiiro markets deeper native code analysis and materiality/Risk-Graph context, while Legit historically emphasized SDLC/pipeline posture and code-to-cloud traceability (the two have converged). Against [endor-labs](endor-labs.md) it is broader-but-shallower on the specific dependency-reachability problem (Endor goes deeper on SCA reachability; Apiiro spans the whole SDLC). Versus [snyk](snyk.md) it is posture/orchestration-led rather than a developer-scanner suite; versus [semgrep](semgrep.md)/[socket](socket.md) it sits a layer up, consuming rather than being a single scanner. [aikido-security](aikido-security.md) competes at the SMB/all-in-one end.

## Ownership, funding & M&A
Independent, venture-backed. Founded 2019 by Idan Plotnik (CEO) and Yonatan Eldar; HQ Tel Aviv with New York presence. **$35M Series A** (2021) and a **$100M Series B** (2022-11-03, led by General Catalyst with Greylock and Kleiner Perkins); ~$135M total. No acquisition found; independent as of 2026-06-28. Confidence: high on funding/independence (primary press + vendor); founding year 2019 widely cited (one aggregator says 2018) — minor uncertainty noted.

## CTO / hedge-fund lens
**Day-1 if shipping AI-generated code at enterprise scale**; otherwise Day-2. Apiiro is built for *large* AppSec organizations with many repos, many scanners, and a need to prioritize across them — its customer logos (BlackRock, JPMorgan, USAA) are big regulated shops. A 50-person fund will likely find it heavier than needed and may prefer a focused tool ([endor-labs](endor-labs.md), [semgrep](semgrep.md), [aikido-security](aikido-security.md)). For a larger asset manager with a real internal dev org shipping AI-assisted code, the design-time risk and risk-graph prioritization map well to model-risk/change-governance expectations. `hedge_fund_fit: medium` — high for large in-house dev shops, low for small/buy-not-build funds.

## Competitors / alternatives
[legit-security](legit-security.md), [endor-labs](endor-labs.md), [snyk](snyk.md), [semgrep](semgrep.md), [socket](socket.md), [aikido-security](aikido-security.md)

## Open questions / to verify
- Founding year: 2019 (most sources) vs 2018 (one aggregator) — confirm against incorporation/primary.
- Any funding after the 2022 Series B (Series C?) — none confirmed as of 2026-06-28.
- Maturity/independence of the marketed "agentic" AutoFix agents vs roadmap.

## Sources
- [Apiiro pulls in $100M Series B (TechCrunch)](https://techcrunch.com/2022/11/03/applications-security-startup-apiiro-pulls-in-100m-series-b-from-a-list-investors/) — fetched 2026-06-28 — supports: Series B $100M/Nov 2022, General Catalyst/Greylock/Kleiner, CEO Idan Plotnik, $135M total, design-phase analysis; confidence: high
- [Apiiro vendor site](https://apiiro.com/) — fetched 2026-06-28 — supports: ASPM/Deep Code Analysis/Risk Graph/AutoFix positioning, enterprise customers; confidence: medium (marketing)
- [Apiiro — Crunchbase profile](https://www.crunchbase.com/organization/apiiro-ltd) — fetched 2026-06-28 — supports: ~$135M total funding, Tel Aviv/NY HQ, founders; confidence: medium (aggregator)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Tel Aviv/NY HQ, founded ~2019, ~$135M total ($100M Series B Nov 2022, General Catalyst), independent. Positioned as deep-code-analysis ASPM with Risk Graph. ownership_confidence raised to high.
