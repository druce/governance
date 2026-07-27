---
title: Teleskope
type: vendor
name: Teleskope
slug: teleskope
aka: []
primary_category: dspm
also_listed_in: [dlp]
website: https://www.teleskope.ai
founded: 2022
hq: New York City, New York, USA
ownership_state: independent
owner: null
ownership_note: Independent; $25M Series A announced 2025-10-31 (M13 lead)
acquisition: {announced: null, closed: null, price: null}
funding_total: $32.2M
last_funding: $25M Series A announced 2025-10-31 (M13 lead; Primary Venture Partners, Lerer Hippeau)
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [platform, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: [SOC 2]
pricing_model: null
fs_traction: claimed
target_customer: mid-to-large enterprise
last_verified: 2026-07-13
verify_after: null
tags: [dspm, data-security, automated-remediation, independent]
---

# Teleskope

> **Researched 2026-07-13.** Primary category: [dspm](../categories/dspm.md). Independent, Series A.

**One-liner** — An "agentic data security" DSPM that doesn't stop at finding and classifying sensitive data — it autonomously remediates (block, quarantine, redact, delete), with AI-era coverage that includes stopping sensitive data reaching external LLMs.

## What it does
Teleskope discovers and classifies sensitive data across cloud, SaaS, and hybrid environments using contextual classification (pitched against generic pattern matching; claims 40,000 bytes/sec at 99.3% accuracy), converts policy into targeted actions based on risk profile, and then **enforces natively** — block, quarantine, redact, notify, delete — rather than filing findings for a human queue. Its 2026-06 "Data Reasoning Layer" launch packages that classification + decision-making + automated remediation loop. AI-specific coverage spans Notion, Claude, OpenAI, Gemini, Slack, and Copilot, including preventing sensitive-data exposure to external LLMs.

## Where it sits in the stack
Primary [dspm](../categories/dspm.md) (data layer): find and classify sensitive data before AI touches it. Cross-listed in [dlp](../categories/dlp.md) because the native remediation/redaction and block-data-to-external-LLM enforcement crosses into the data-in-motion control the DLP page covers. The differentiating claim is precisely that it collapses the DSPM→DLP handoff: posture findings become automated enforcement in the same product.

## Deployment & architecture
Notably flexible for the category: **air-gapped, single-tenant SaaS, or Teleskope-managed** deployments — the air-gapped/self-hosted option matters for firms that won't let a scanner exfiltrate metadata. SOC 2 attested (site also claims an ISO certification, number unstated).

## Positioning & differentiators
- **Remediation-native** — acts (redact/quarantine/delete) instead of only reporting; the "operates like a human security team" agentic pitch.
- **AI-era scope** — classification and enforcement extend to GenAI tools and external-LLM egress, not just data stores.
- **Deployment flexibility** — air-gapped option is rare among cloud-native DSPM peers.

Nearest neighbors: [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [concentric-ai](concentric-ai.md), [bedrock-security](bedrock-security.md), [proofpoint-dspm](proofpoint-dspm.md) (ex-Normalyze), [wiz](wiz.md) (DSPM-as-module).

## Ownership, funding & M&A
**Independent.** Founded **2022** by **Elizabeth Nammour** (CEO; ex-Airbnb security engineer), HQ **New York City**. Funding: $2.2M pre-seed (2023-07, Lerer Hippeau), ~$7M seed (Primary Venture Partners), **$25M Series A led by M13** (PR 2025-10-31), **$32.2M total**. No M&A activity found. Named customers include Ramp, LegalZoom, Alloy, EarnIn, GoFundMe, Stitch Fix, Notion, Petco, The Atlantic — fintech names (Ramp, Alloy, EarnIn) ground the `fs_traction: claimed` tag, though no asset-manager/hedge-fund customer is named.

## CTO / hedge-fund lens
Day-1 category (you must know where sensitive data sits before RAG/AI touches it), and the automated-remediation angle suits a small security team that can't work a findings backlog. Freshly funded and independent — the flip side is acquisition risk in a consolidating category (Normalyze→Proofpoint, Securiti→Veeam, Symmetry→Zscaler all went to platforms). Evaluate against Cyera/Sentra on classification quality and against your appetite for autonomous remediation actions in production data stores.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [concentric-ai](concentric-ai.md), [bedrock-security](bedrock-security.md), [securiti](securiti.md), [proofpoint-dspm](proofpoint-dspm.md), [wiz](wiz.md), [microsoft-purview](microsoft-purview.md).

## Open questions / to verify
- Which ISO certification (27001?) — site says "ISO" without a number.
- Data handling in the SaaS deployment (does content/metadata leave the tenancy).
- Pricing model and band.
- Accuracy/throughput claims (40k bytes/sec, 99.3%) are vendor-stated — no independent corroboration found.
- Any FS/asset-manager customers beyond fintech.

## Sources
- [Teleskope homepage](https://www.teleskope.ai/) — fetched 2026-07-13 — supports: capabilities, deployment models (air-gapped/single-tenant SaaS/managed), AI tool coverage, customers, SOC 2; confidence: med (vendor marketing). Cached: `raw/sources/2026-07-13--teleskope--homepage.md`
- [Teleskope raises $25M (AlleyWatch, 2026-01)](https://www.alleywatch.com/2026/01/teleskope-agentic-data-security-platform-remediation-automation-dspm-elizabeth-nammour/) — fetched 2026-07-13 — supports: $25M Series A (M13), $32.2M total, founder background, customers; confidence: med-high (founder interview; corroborated by BusinessWire PR 2025-10-31). Cached: `raw/sources/2026-07-13--teleskope--series-a-alleywatch.md`

## History
- [2026-07-13] Page created via wiki-create + researched: surfaced while triaging Google-suggested SurePath competitors (user request); real category fit is dspm, not shadow-AI. Independent, $32.2M raised.
