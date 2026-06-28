---
type: vendor
name: Legit Security
slug: legit-security
categories: [software-supply-chain]
layer: foundation
aliases: []
website: https://www.legitsecurity.com
founded: 2020
hq: Palo Alto, California, USA (R&D in Israel)
ownership: independent
ownership_detail: Venture-backed, independent as of 2026-06-28. No acquisition found in vendor news or press; $40M Series B (Sep 2023, CRV).
ownership_confidence: medium
funding_total: ~$70M (Series A $30M 2022 + Series B $40M 2023)
last_funding: Series B, $40M, 2023-09-20 (CRV)
deployment: [saas, api]
target_customer: enterprise / regulated (Google, NYSE, Kraft Heinz, AIG, Freddie Mac, Cboe cited)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [aspm, sdlc-security, secrets, sca, sast]
---

# Legit Security

**One-liner** — An AI-native ASPM platform that maps your whole SDLC — code, pipelines, secrets, dependencies — to give AppSec teams unified, prioritized visibility and remediation from code to cloud.

**Categories** — [software-supply-chain](../categories/software-supply-chain.md) (primary)

## What it does
Legit Security is an **Application Security Posture Management (ASPM)** platform. It discovers and inventories the software factory (repos, pipelines, build systems, scanners), then unifies findings — SAST, SCA, secrets detection, software supply chain security, code-change management — into prioritized, deduplicated remediation. It emphasizes **SDLC/pipeline security posture** and code-to-cloud traceability (knowing which code reached which deployment). In 2025 it added AI-native SCA and SAST capabilities aimed at AI-first development, plus AI-assisted remediation and an "AI Security Command Center" for governing AI usage in the SDLC.

## Where it sits in the stack
[software-supply-chain](../categories/software-supply-chain.md) at the **foundation** layer, as a posture/orchestration plane over the SDLC rather than a single scanner. Trifecta role is primarily **untrusted input** — third-party and AI-generated code/dependencies, plus pipeline-tampering and leaked secrets, are the input vectors it governs. AI-generated-code relevance: its 2025 AI-native SCA/SAST and AI-usage governance are pitched precisely at teams shipping AI-assisted code who need posture and policy over it.

## Deployment & architecture
SaaS, integrating via API into SCMs, CI/CD systems, build tooling, secrets stores, and third-party scanners whose results it normalizes. Not an inline runtime control; it sits over the development pipeline.

## Positioning & differentiators
Legit's heritage is **SDLC / pipeline security posture and software-factory discovery** — knowing every pipeline and build path and securing the route from code to cloud — which it has broadened into full ASPM with native code scanning. Its closest neighbor is [apiiro](apiiro.md); the practical split is Apiiro leading on deep code analysis / Risk-Graph materiality, Legit leading on SDLC/pipeline posture and factory visibility, though both now market the full ASPM stack and converge. Versus [endor-labs](endor-labs.md) it is broader and posture-led rather than reachability-SCA-deep. Versus point scanners [snyk](snyk.md), [semgrep](semgrep.md), [socket](socket.md) it sits a layer up, consuming and prioritizing their output. [aikido-security](aikido-security.md) competes at the smaller/all-in-one end.

## Ownership, funding & M&A
Independent, venture-backed. Founded ~2020 by Roni Fuchs (CEO), Liav Caspi (CTO) and Lior Barak (COO); out of stealth Feb 2022; HQ Palo Alto, CA with Israel R&D. **$30M Series A** (Feb 2022, Bessemer + TCV) and **$40M Series B** (2023-09-20, led by CRV with Cyberstarts, Bessemer, TCV); ~$70M total.

**M&A check (per task):** No acquisition or merger found. Legit Security's own news page shows no 2025/2026 acquisition; multiple targeted searches ("Legit Security acquired/acquires/acquisition") returned no acquirer press release. **Independent as of 2026-06-28.** `ownership_confidence: medium` — this is absence-of-evidence (corroborated by the vendor's own news page plus several negative searches), not a positive primary confirmation of continued independence; raise to high only with a current dated primary source.

## CTO / hedge-fund lens
**Day-1 if shipping AI-generated code with a real internal dev org**; otherwise Day-2. Legit fits regulated enterprises that need to *prove* control over their software factory — its customer list (NYSE, AIG, Freddie Mac, Cboe) skews finance/regulated, which matches an asset manager's audit/SR 11-7-style change-governance posture. The software-factory discovery and pipeline posture are valuable when you have many repos/pipelines and need one prioritized view. A small fund that ships little code will find a focused scanner ([endor-labs](endor-labs.md), [semgrep](semgrep.md), [aikido-security](aikido-security.md)) lighter. `hedge_fund_fit: medium` — high for larger regulated dev shops, low for buy-not-build funds.

## Competitors / alternatives
[apiiro](apiiro.md), [endor-labs](endor-labs.md), [snyk](snyk.md), [semgrep](semgrep.md), [socket](socket.md), [aikido-security](aikido-security.md)

## Open questions / to verify
- Founding year: sources vary 2020 vs 2021 — confirm against incorporation/primary.
- Any funding after the 2023 Series B (Series C?) — none confirmed as of 2026-06-28.
- Continued independence — re-verify against a current primary source before raising ownership_confidence.

## Sources
- [Legit Security Secures $40M Series B (PRNewswire)](https://www.prnewswire.com/news-releases/legit-security-secures-40-million-series-b-investment-led-by-crv-301932852.html) — fetched 2026-06-28 — supports: Series B $40M/Sep 2023/CRV, Series A $30M, Palo Alto HQ, founders, ASPM positioning; confidence: high
- [Legit Security — About Us](https://www.legitsecurity.com/about-us) — fetched 2026-06-28 — supports: ASPM capabilities, co-founders, enterprise customers, no acquisition mention; confidence: medium (vendor)
- [Legit Security — News (M&A check)](https://www.legitsecurity.com/news) — fetched 2026-06-28 — supports: no 2025/2026 acquisition announcement; 2025 AI-native SCA/SAST launch; IDC MarketScape ASPM Leader 2025; confidence: medium (vendor)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Palo Alto HQ (Israel R&D), founded ~2020, ~$70M total ($30M Series A 2022 / $40M Series B Sep 2023, CRV). M&A CHECK: no acquisition found across vendor news + multiple searches — independent as of 2026-06-28; ownership_confidence set to medium (absence-of-evidence). Positioned as AI-native SDLC-posture ASPM.
