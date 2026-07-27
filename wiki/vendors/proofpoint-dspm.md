---
title: Proofpoint DSPM
type: vendor
name: Proofpoint DSPM
slug: proofpoint-dspm
aka: [Normalyze]
primary_category: dspm
also_listed_in: []
website: https://www.proofpoint.com/us/products/data-security-posture-management
founded: 2020
hq: San Francisco, USA
ownership_state: acquired-closed
owner: Proofpoint
ownership_note: Normalyze acquired by Proofpoint; announced 2024-10-29, expected close Nov 2024. Terms undisclosed. Brand retired — normalyze.ai now redirects to Proofpoint; sold as Proofpoint DSPM. (Proofpoint is itself Thoma Bravo-owned.)
acquisition: {announced: 2024-10-29, closed: 2024-10-29, price: null}
funding_total: ~$26.6M
last_funding: Series A $22.2M (2022-06, Battery Ventures + Lightspeed)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated
last_verified: 2026-07-27
verify_after: null
tags: [dspm, data-security, proofpoint, thoma-bravo]
sources:
  - {claim: "Normalyze brand retired; normalyze.ai 301-redirects to Proofpoint; product now Proofpoint Data Security Posture Management", url: "https://www.proofpoint.com/us/normalyze-is-now-proofpoint", date: 2026-07-27, confidence: high}
---

# Proofpoint DSPM

> **One-liner** — Proofpoint's Data Security Posture Management product, built from the acquired DSPM startup **Normalyze**: discovers and classifies sensitive data across cloud/SaaS/on-prem and puts a dollar value on the risk.

**Categories** — [dspm](../categories/dspm.md)

## What it does
Proofpoint DSPM (formerly Normalyze) is **Data Security Posture Management**: it scans data stores across SaaS, PaaS, public/multi-cloud, on-prem and hybrid, discovers and classifies sensitive data, maps who/what can access it, and surfaces the riskiest exposures. Normalyze's differentiator was **in-place scanning** (no copying data out) and **quantified, dollar-value risk** scoring to prioritize remediation; Proofpoint pitches the combined product as protecting data "while prioritizing the reduction of human-centric risks." The job: know where regulated/sensitive data is and whether it is over-exposed — including to AI tools and RAG pipelines.

## Naming / provenance
Founded 2020 as **Normalyze**; acquired by Proofpoint (announced 2024-10-29). The standalone brand is **retired**: as of 2026-07-27, normalyze.ai 301-redirects to a "Normalyze is now Proofpoint" page and the product is sold as **Proofpoint Data Security Posture Management**. Page slugged by product (like [prisma-airs](prisma-airs.md)) because "Proofpoint" alone is ambiguous — Proofpoint also owns [acuvity](acuvity.md) (shadow-AI/agent visibility, acquired 2026-02) and its core email-security/DLP franchise.

## Where it sits in the stack
Data layer, [dspm](../categories/dspm.md). Risk focus: **sensitive data** — find and reduce sensitive-data exposure before AI systems can reach it. Posture/visibility, not an inline runtime control. Adjacent to [dlp](../categories/dlp.md) (Proofpoint's core) and [data-access-governance](../categories/data-access-governance.md).

## Deployment & architecture
SaaS console with agentless, in-place scanning of connected data stores via cloud APIs/roles. Integrates with cloud providers and security tooling. Now folded into the Proofpoint platform alongside Proofpoint DLP.

## Positioning & differentiators
Known for in-place scanning and quantified risk ("data risk in dollars"). Nearest neighbors: [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [bedrock-security](bedrock-security.md), and [wiz](wiz.md) (DSPM-as-CNAPP-module). The pitch is no longer standalone DSPM but "DSPM + DLP + human-centric security" in one Proofpoint platform.

## Ownership, funding & M&A
**Verified (acquirer matches seed).** Normalyze acquired by **Proofpoint**; announced **2024-10-29**, expected to close **November 2024**; **financial terms not disclosed**. Brand fully absorbed by 2026 (redirect verified 2026-07-27). Note the chain of ownership: **Proofpoint is itself owned by Thoma Bravo** (taken private 2021), so this is effectively a Thoma Bravo-portfolio asset under Proofpoint — Proofpoint's first data/AI-security buy, followed by [acuvity](acuvity.md) (2026-02). Founded 2020 (San Francisco); co-founders Amer Deeba (CEO, ex-Qualys) and Ravi Ithal (CTO, ex-Netskope/Palo Alto); ~$26.6M raised (Series A $22.2M, June 2022, Battery Ventures + Lightspeed). Ownership confidence **high** on the acquirer; **deal terms remain undisclosed**.

## CTO / hedge-fund lens
**Day-1 if you handle regulated/sensitive data and especially if doing RAG** (you must know where sensitive data sits before exposing it to AI). For an existing Proofpoint customer, the value is consolidation — DSPM under the same vendor as email security/DLP. For others, evaluate it against the data-first specialists ([cyera](cyera.md), [sentra](sentra.md)) as a Proofpoint platform module, not a standalone tool — the standalone product and brand are gone.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [bedrock-security](bedrock-security.md), [wiz](wiz.md), [microsoft-purview](microsoft-purview.md).

## Open questions / to verify
- Independent confirmation of the actual close (press treated it as completed by Dec 2024; a standalone "completion" PR was not located).
- Deal price (undisclosed).
- How Proofpoint DSPM is packaged/priced relative to the former standalone Normalyze offering.

## Sources
- [Normalyze is now Proofpoint (redirect target)](https://www.proofpoint.com/us/normalyze-is-now-proofpoint) — fetched 2026-07-27 — supports: brand retired, product renamed Proofpoint DSPM, positioning; confidence: high
- [Proofpoint DSPM product page](https://www.proofpoint.com/us/products/data-security-posture-management) — fetched 2026-07-27 — supports: current product name and scope; confidence: high
- [Proofpoint Signs Definitive Agreement to Acquire Normalyze](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-signs-definitive-agreement-acquire-normalyze) — fetched 2026-06-28 — supports: acquirer Proofpoint, date 2024-10-29, expected close Nov 2024, DSPM positioning; confidence: high
- [Proofpoint to Acquire Normalyze (SecurityWeek)](https://www.securityweek.com/proofpoint-to-acquire-data-security-posture-management-firm-normalyze/) — fetched 2026-06-28 — supports: DSPM, in-place scanning, undisclosed terms; confidence: high
- [Normalyze — Crunchbase/Tracxn profiles](https://www.crunchbase.com/organization/normalyze) — fetched 2026-06-28 — supports: founded 2020, founders, ~$26.6M funding, HQ; confidence: med
- Cached: `raw/sources/2026-07-27--proofpoint-dspm--normalyze-brand-retired.md`

## History
- [2026-06-28] Stub created from seed registry (as `normalyze`).
- [2026-06-28] Researched; verified Proofpoint acquisition (announced 2024-10-29, expected close Nov 2024, terms undisclosed), raised ownership_confidence low→high; noted Proofpoint→Thoma Bravo ownership chain; filled founding/HQ/funding. Open: independent close confirmation.
- [2026-07-27] Renamed page `normalyze` → `proofpoint-dspm` (user-flagged; verified normalyze.ai 301-redirects to Proofpoint and product is sold as Proofpoint DSPM). Brand-survival open question resolved: brand retired.
