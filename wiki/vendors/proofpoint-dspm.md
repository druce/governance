---
title: Proofpoint DSPM
type: vendor
name: Proofpoint DSPM
slug: proofpoint-dspm
aka: [Normalyze]
primary_category: dspm
also_listed_in: [dlp]
website: https://www.proofpoint.com/us/products/data-security-posture-management
founded: 2020
hq: San Francisco, USA
ownership_state: acquired-closed
owner: Proofpoint
ownership_note: Normalyze acquired by Proofpoint; announced 2024-10-29, expected close Nov 2024. Terms undisclosed. Brand retired — normalyze.ai now redirects to Proofpoint; sold as Proofpoint DSPM. (Proofpoint is itself Thoma Bravo-owned.)
acquisition: {announced: 2024-10-29, closed: null, price: null}
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
last_verified: 2026-10-24
verify_after: null
tags: [dspm, data-security, proofpoint, thoma-bravo]
sources:
  - {claim: "Normalyze brand retired; normalyze.ai 301-redirects to Proofpoint; product now Proofpoint Data Security Posture Management", url: "https://www.proofpoint.com/us/normalyze-is-now-proofpoint", date: 2026-07-27, confidence: high}
  - {claim: "Proofpoint Enterprise DLP covers email, cloud apps, endpoints and AI tools; GenAI prompt/upload detection; single console (marketing)", url: "https://www.proofpoint.com/us/products/information-protection/enterprise-dlp", date: 2026-10-24, confidence: medium}
  - {claim: "DLP Transform cross-channel DLP (email, cloud, endpoint, web); GenAI allow/disallow by behavior, content, lineage; ChatGPT/Gemini browser extension expected end Q2 2024; Adaptive Email DLP (Tessian) GA", url: "https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-bolsters-information-protection-offering-cross-channel-dlp", date: 2024-05-01, confidence: high}
  - {claim: "Data Security Complete (DSPM + DLP + ITM + lineage) launched Q3 2025; AI Data Governance", url: "https://www.businesswire.com/news/home/20250923151333/en/Proofpoint-Secures-Collaboration-and-Data-in-the-Agentic-Workspace-with-Industry-First-Innovations", date: 2025-09-23, confidence: medium}
---

# Proofpoint DSPM

> **One-liner** — Proofpoint's Data Security Posture Management product, built from the acquired DSPM startup **Normalyze**: discovers and classifies sensitive data across cloud/SaaS/on-prem and puts a dollar value on the risk.

**Categories** — [dspm](../categories/dspm.md); also listed in [dlp](../categories/dlp.md) for Proofpoint Enterprise DLP (see below).

## What it does
Proofpoint DSPM (formerly Normalyze) is **Data Security Posture Management**: it scans data stores across SaaS, PaaS, public/multi-cloud, on-prem and hybrid, discovers and classifies sensitive data, maps who/what can access it, and surfaces the riskiest exposures. Normalyze's differentiator was **in-place scanning** (no copying data out) and **quantified, dollar-value risk** scoring to prioritize remediation; Proofpoint pitches the combined product as protecting data "while prioritizing the reduction of human-centric risks." The job: know where regulated/sensitive data is and whether it is over-exposed — including to AI tools and RAG pipelines.

## Naming / provenance
Founded 2020 as **Normalyze**; acquired by Proofpoint (announced 2024-10-29). The standalone brand is **retired**: as of 2026-07-27, normalyze.ai 301-redirects to a "Normalyze is now Proofpoint" page and the product is sold as **Proofpoint Data Security Posture Management**. Page slugged by product (like [prisma-airs](prisma-airs.md)) because "Proofpoint" alone is ambiguous — Proofpoint also owns [acuvity](acuvity.md) (shadow-AI/agent visibility, acquired 2026-02) and its core email-security/DLP franchise.

## Where it sits in the stack
Data layer, [dspm](../categories/dspm.md). Risk focus: **sensitive data** — find and reduce sensitive-data exposure before AI systems can reach it. Posture/visibility, not an inline runtime control. Adjacent to [dlp](../categories/dlp.md) (Proofpoint's core) and [data-access-governance](../categories/data-access-governance.md).

## Proofpoint Enterprise DLP (cross-listing to DLP)
*Added 2026-10-24, prompted by an October 2026 CTO survey write-in under DLP (Q52, "Proofpoint", 1 respondent, in production).* This page is the wiki's single Proofpoint data-security page, so Proofpoint's DLP product is recorded here rather than on a separate Proofpoint page.

**Proofpoint Enterprise DLP** is Proofpoint's core DLP product and is older than the DSPM. Per Proofpoint's product page (vendor marketing, checked 2026-10-24), it covers **email, cloud apps (Microsoft 365, including Teams, OneDrive and SharePoint), endpoints (USB transfers, web uploads, file-movement tracking) and AI tools**, with alerts triaged in a single console. Its **GenAI claim** (marketing; no mechanism detail on the page) is detection and control of sensitive data in GenAI prompts and uploads, including unsanctioned tools. The 2024-05-01 "DLP Transform" release described the approach in more detail: allow or disallow GenAI interactions based on user behaviour, content and data lineage rather than blocking the tools outright. That release also said a browser extension for text typed into ChatGPT and Gemini was "expected ... end of Q2 2024"; whether it shipped was not verified on this pass. Email DLP is the historical strength. **Adaptive Email DLP**, built on the acquired Tessian behavioural engine, went GA in 2024 and catches misdirected email and exfiltration by email. In September 2025 Proofpoint packaged DSPM, DLP, insider-threat management and data lineage together as **Data Security Complete** (launched Q3 2025), and announced **AI Data Governance** for sanctioned and unsanctioned AI use. Agent and MCP controls are sold separately (see [acuvity](acuvity.md)). **CTO lens:** a strong fit where Proofpoint already runs email security, since email DLP and the DSPM come under one vendor. Against [cyberhaven](cyberhaven.md) or [nightfall-ai](nightfall-ai.md), the GenAI prompt controls are unproven: ask in a POC whether prompt inspection depends on the browser extension, and how it treats desktop AI apps.

## Deployment & architecture
SaaS console with agentless, in-place scanning of connected data stores via cloud APIs/roles. Integrates with cloud providers and security tooling. Now folded into the Proofpoint platform alongside Proofpoint DLP.

## Positioning & differentiators
Known for in-place scanning and quantified risk ("data risk in dollars"). Nearest neighbors: [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [bedrock-data](bedrock-data.md), and [wiz](wiz.md) (DSPM-as-CNAPP-module). The pitch is no longer standalone DSPM but "DSPM + DLP + human-centric security" in one Proofpoint platform.

## Ownership, funding & M&A
**Verified (acquirer matches seed).** Normalyze acquired by **Proofpoint**; announced **2024-10-29**, expected to close **November 2024**; **financial terms not disclosed**. Brand fully absorbed by 2026 (redirect verified 2026-07-27). Note the chain of ownership: **Proofpoint is itself owned by Thoma Bravo** (taken private 2021), so this is effectively a Thoma Bravo-portfolio asset under Proofpoint — Proofpoint's first data/AI-security buy, followed by [acuvity](acuvity.md) (2026-02). Founded 2020 (San Francisco); co-founders Amer Deeba (CEO, ex-Qualys) and Ravi Ithal (CTO, ex-Netskope/Palo Alto); ~$26.6M raised (Series A $22.2M, June 2022, Battery Ventures + Lightspeed). Ownership confidence **high** on the acquirer; **deal terms remain undisclosed**.

## CTO / hedge-fund lens
**Day-1 if you handle regulated/sensitive data and especially if doing RAG** (you must know where sensitive data sits before exposing it to AI). For an existing Proofpoint customer, the value is consolidation — DSPM under the same vendor as email security/DLP. For others, evaluate it against the data-first specialists ([cyera](cyera.md), [sentra](sentra.md)) as a Proofpoint platform module, not a standalone tool — the standalone product and brand are gone.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [bedrock-data](bedrock-data.md), [wiz](wiz.md), [microsoft-purview](microsoft-purview.md).

## Open questions / to verify
- Independent confirmation of the actual close (press treated it as completed by Dec 2024; a standalone "completion" PR was not located).
- Deal price (undisclosed).
- How Proofpoint DSPM is packaged/priced relative to the former standalone Normalyze offering.
- Enterprise DLP: did the ChatGPT/Gemini browser extension (promised end Q2 2024) ship, and how does prompt inspection work for desktop AI apps? Is Enterprise DLP sold standalone or only inside Data Security Complete?

## Sources
- [Normalyze is now Proofpoint (redirect target)](https://www.proofpoint.com/us/normalyze-is-now-proofpoint) — fetched 2026-07-27 — supports: brand retired, product renamed Proofpoint DSPM, positioning; confidence: high
- [Proofpoint DSPM product page](https://www.proofpoint.com/us/products/data-security-posture-management) — fetched 2026-07-27 — supports: current product name and scope; confidence: high
- [Proofpoint Signs Definitive Agreement to Acquire Normalyze](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-signs-definitive-agreement-acquire-normalyze) — fetched 2026-06-28 — supports: acquirer Proofpoint, date 2024-10-29, expected close Nov 2024, DSPM positioning; confidence: high
- [Proofpoint to Acquire Normalyze (SecurityWeek)](https://www.securityweek.com/proofpoint-to-acquire-data-security-posture-management-firm-normalyze/) — fetched 2026-06-28 — supports: DSPM, in-place scanning, undisclosed terms; confidence: high
- [Normalyze — Crunchbase/Tracxn profiles](https://www.crunchbase.com/organization/normalyze) — fetched 2026-06-28 — supports: founded 2020, founders, ~$26.6M funding, HQ; confidence: med
- [Proofpoint Enterprise DLP product page](https://www.proofpoint.com/us/products/information-protection/enterprise-dlp) — fetched 2026-10-24 — supports: DLP channels, GenAI prompt/upload claims, single console; confidence: medium (vendor marketing)
- [Proofpoint Bolsters Information Protection Offering with Cross-Channel DLP (2024-05-01)](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-bolsters-information-protection-offering-cross-channel-dlp) — fetched 2026-10-24 — supports: DLP Transform channels, GenAI allow/disallow, browser-extension timing, Adaptive Email DLP GA; confidence: high (primary; capability claims vendor-stated)
- [Proofpoint Secures Collaboration and Data in the Agentic Workspace (Business Wire, 2025-09-23)](https://www.businesswire.com/news/home/20250923151333/en/Proofpoint-Secures-Collaboration-and-Data-in-the-Agentic-Workspace-with-Industry-First-Innovations) — via search 2026-10-24 — supports: Data Security Complete, AI Data Governance; confidence: medium
- Cached: `raw/sources/2026-07-27--proofpoint-dspm--normalyze-brand-retired.md`, `raw/sources/2026-10-24--proofpoint-dspm--enterprise-dlp.md`

## History
- [2026-06-28] Stub created from seed registry (as `normalyze`).
- [2026-06-28] Researched; verified Proofpoint acquisition (announced 2024-10-29, expected close Nov 2024, terms undisclosed), raised ownership_confidence low→high; noted Proofpoint→Thoma Bravo ownership chain; filled founding/HQ/funding. Open: independent close confirmation.
- [2026-07-27] Renamed page `normalyze` → `proofpoint-dspm` (user-flagged; verified normalyze.ai 301-redirects to Proofpoint and product is sold as Proofpoint DSPM). Brand-survival open question resolved: brand retired.
- [2026-10-24] Cross-listed to dlp and added a Proofpoint Enterprise DLP section (channels, GenAI prompt claims marked as marketing, Data Security Complete 2025), triggered by a 1-respondent in-production write-in under DLP in the October 2026 CTO survey. Kept as one Proofpoint data-security page rather than creating a duplicate Proofpoint vendor page.
- [2026-10-24] Set `acquisition.closed` to null: 2024-10-29 was the announcement date and no completion release has been found (ownership_state stays acquired-closed because the brand is fully absorbed).
