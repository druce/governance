---
type: vendor
name: Wiz
slug: wiz
categories: [dspm, ai-spm]
layer: data
aliases: []
website: https://www.wiz.io
founded: 2020
hq: New York City, USA (R&D Tel Aviv, Israel)
ownership: acquired
ownership_detail: "Acquired by Google (Alphabet) for $32B all-cash; announced 2025-03, closed 2026-03-11. Joins Google Cloud, keeps brand."
ownership_confidence: high
funding_total: ~$1.9B (pre-acquisition)
last_funding: Series E $1B (2024-05) at ~$12B valuation
deployment: [saas, api]
target_customer: enterprise / cloud-native / regulated
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [cnapp, cspm, dspm, ai-spm, cloud-security, google]
---

# Wiz

> **One-liner** — The agentless cloud security platform (CNAPP) that maps risk across your cloud estate; now a Google company, with a DSPM and AI-SPM module relevant to AI data and model exposure.

**Categories** — [dspm](../categories/dspm.md) (primary), [ai-spm](../categories/ai-spm.md)

## What it does
Wiz scans cloud environments (AWS, Azure, GCP, Oracle, Kubernetes) agentlessly and builds a graph of resources, identities, vulnerabilities, exposures and data, then correlates them into prioritized "attack paths." Its core is CNAPP (cloud-native application protection), but the relevant modules here are **Wiz DSPM** (discovers and classifies sensitive data across cloud stores and flags toxic combinations of exposure + access) and **Wiz AI-SPM** (inventories AI services, models, training data and pipelines, and finds misconfigurations/exposures in them). The pitch is one connected graph rather than a stack of point tools.

## Where it sits in the stack
Primarily the **data** layer ([dspm](../categories/dspm.md)) with an [ai-spm](../categories/ai-spm.md) extension at the model/prompt layer. Lethal-trifecta leg: **sensitive-data** — it tells you where regulated/sensitive data lives in cloud and whether AI services can reach it. It is posture/visibility (find and prioritize), not an inline runtime control; it does not sit in the prompt path the way an [ai-runtime-security](../categories/ai-runtime-security.md) firewall does.

## Deployment & architecture
SaaS console; connects to cloud accounts via agentless API scanning (read-only roles) with optional lightweight sensors for runtime. Integrates with SIEM/SOC ([siem-soc](../categories/siem-soc.md)), ticketing, CI/CD and IdP. Not an inline proxy.

## Positioning & differentiators
Known for fast agentless deployment, the security graph, and attack-path prioritization that reduced alert noise versus legacy CSPM. Nearest neighbors in DSPM: [cyera](cyera.md), [sentra](sentra.md), [normalyze](normalyze.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md) — most of those are data-first specialists, whereas Wiz comes at data from a broad cloud-security posture angle (DSPM as a module of CNAPP). For AI-SPM it overlaps [noma-security](noma-security.md), [prisma-airs](prisma-airs.md).

## Ownership, funding & M&A
**Verified.** Acquired by **Google (Alphabet)** for **$32B all-cash** — Google's largest-ever acquisition. Announced March 2025; **closed 2026-03-11** after a long regulatory path (US DOJ clearance Oct 2025; EU + Australia Feb 2026; Singapore + Japan Mar 2026). Wiz joins Google Cloud but keeps its brand and multi-cloud support. Founded January 2020 by the ex-Adallom team (Assaf Rappaport et al.); raised ~$1.9B pre-deal (Series E $1B, May 2024, ~$12B valuation); crossed $1B ARR in 2025. Ownership confidence **high**.

## CTO / hedge-fund lens
**Day-1 if you run meaningful workloads in public cloud**; less central for a shop that is mostly SaaS-only. For a fund, the draw is one tool for cloud misconfig + data exposure + (increasingly) AI asset posture, which maps to data-protection and model-risk diligence. Watch the Google ownership: neutral-multi-cloud messaging is the stated commitment, but a Google-owned control plane may be a governance question for some shops. Pricing is enterprise-tier.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [normalyze](normalyze.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [bedrock-security](bedrock-security.md) (DSPM); [noma-security](noma-security.md), [prisma-airs](prisma-airs.md) (AI-SPM); [microsoft-purview](microsoft-purview.md) (data security in Microsoft estates).

## Open questions / to verify
- Exact total funding figure (sources range ~$1.9B); confirm against Crunchbase/filings.
- How Wiz DSPM/AI-SPM roadmap and pricing change under Google Cloud post-close.

## Sources
- [Google wraps up $32B acquisition of Wiz](https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/) — fetched 2026-06-28 — supports: acquirer, $32B, close date 2026-03-11, regulatory path, integration; confidence: high
- [Wiz, Inc. — Wikipedia](https://en.wikipedia.org/wiki/Wiz,_Inc.) — fetched 2026-06-28 — supports: founding 2020, founders, funding rounds, HQ; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Google acquisition ($32B all-cash, closed 2026-03-11), raised ownership_confidence low→high; filled founding/HQ/funding, DSPM + AI-SPM positioning.
