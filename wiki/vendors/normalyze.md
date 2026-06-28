---
type: vendor
name: Normalyze
slug: normalyze
categories: [dspm]
layer: data
aliases: []
website: https://normalyze.ai
founded: 2020
hq: San Francisco, USA
ownership: acquired
ownership_detail: "Acquired by Proofpoint; announced 2024-10-29, expected close Nov 2024. Terms undisclosed. (Proofpoint is itself Thoma Bravo-owned.)"
ownership_confidence: high
funding_total: ~$26.6M
last_funding: Series A $22.2M (2022-06, Battery Ventures + Lightspeed)
deployment: [saas, api]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, data-security, proofpoint, thoma-bravo]
---

# Normalyze

> **One-liner** — A DSPM startup that discovers and classifies sensitive data across cloud/SaaS/on-prem and puts a dollar value on the risk; acquired by Proofpoint to add data-posture to its human-centric security platform.

**Categories** — [[dspm]]

## What it does
Normalyze is **Data Security Posture Management**: it scans data stores across SaaS, PaaS, public/multi-cloud, on-prem and hybrid, discovers and classifies sensitive data, maps who/what can access it, and surfaces the riskiest exposures. Its differentiator was **in-place scanning** (no copying data out) and **quantified, dollar-value risk** scoring to prioritize remediation. The job: know where regulated/sensitive data is and whether it is over-exposed — including to AI tools and RAG pipelines.

## Where it sits in the stack
Data layer, [[dspm]]. Lethal-trifecta leg: **sensitive-data** — find and reduce sensitive-data exposure before AI systems can reach it. Posture/visibility, not an inline runtime control. Adjacent to [[dlp]] (Proofpoint's core) and [[data-access-governance]].

## Deployment & architecture
SaaS console with agentless, in-place scanning of connected data stores via cloud APIs/roles. Integrates with cloud providers and security tooling. Post-acquisition it is being folded into the Proofpoint platform alongside Proofpoint DLP.

## Positioning & differentiators
Known for in-place scanning and quantified risk ("data risk in dollars"). Nearest neighbors: [[cyera]], [[sentra]], [[bigid]], [[securiti]], [[concentric-ai]], [[bedrock-security]], and [[wiz]] (DSPM-as-CNAPP-module). As part of Proofpoint, the pitch shifts from standalone DSPM to "DSPM + DLP + human-centric security" in one platform.

## Ownership, funding & M&A
**Verified (acquirer matches seed).** Acquired by **Proofpoint**; announced **2024-10-29**, expected to close **November 2024**; **financial terms not disclosed**. Note the chain of ownership: **Proofpoint is itself owned by Thoma Bravo** (taken private 2021), so Normalyze is now effectively a Thoma Bravo-portfolio asset under Proofpoint. Founded 2020 (San Francisco); co-founders Amer Deeba (CEO, ex-Qualys) and Ravi Ithal (CTO, ex-Netskope/Palo Alto); ~$26.6M raised (Series A $22.2M, June 2022, Battery Ventures + Lightspeed). Ownership confidence **high** on the acquirer; **deal terms remain undisclosed**.

## CTO / hedge-fund lens
**Day-1 if you handle regulated/sensitive data and especially if doing RAG** (you must know where sensitive data sits before exposing it to AI). For an existing Proofpoint customer, Normalyze's value is consolidation — DSPM under the same vendor as email security/DLP. For others, evaluate it against the data-first specialists rather than as a standalone going forward, since the brand is being absorbed.

## Competitors / alternatives
[[cyera]], [[sentra]], [[bigid]], [[securiti]], [[concentric-ai]], [[bedrock-security]], [[wiz]], [[microsoft-purview]].

## Open questions / to verify
- Independent confirmation of the actual close (press treated it as completed by Dec 2024; a standalone "completion" PR was not located).
- Deal price (undisclosed).
- Whether the Normalyze brand survives or is fully merged into Proofpoint's platform naming.

## Sources
- [Proofpoint Signs Definitive Agreement to Acquire Normalyze](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-signs-definitive-agreement-acquire-normalyze) — fetched 2026-06-28 — supports: acquirer Proofpoint, date 2024-10-29, expected close Nov 2024, DSPM positioning; confidence: high
- [Proofpoint to Acquire Normalyze (SecurityWeek)](https://www.securityweek.com/proofpoint-to-acquire-data-security-posture-management-firm-normalyze/) — fetched 2026-06-28 — supports: DSPM, in-place scanning, undisclosed terms; confidence: high
- [Normalyze — Crunchbase/Tracxn profiles](https://www.crunchbase.com/organization/normalyze) — fetched 2026-06-28 — supports: founded 2020, founders, ~$26.6M funding, HQ; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Proofpoint acquisition (announced 2024-10-29, expected close Nov 2024, terms undisclosed), raised ownership_confidence low→high; noted Proofpoint→Thoma Bravo ownership chain; filled founding/HQ/funding. Open: independent close confirmation.
