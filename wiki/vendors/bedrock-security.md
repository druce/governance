---
type: vendor
name: Bedrock Security
slug: bedrock-security
categories: [dspm]
layer: data
aliases: [Bedrock Data]
website: "https://www.bedrock.security"
founded: 2021
hq: Menlo Park, California, USA
ownership: independent
ownership_detail: VC-backed private; $25M Series A led by Greylock (2025-11). No M&A.
ownership_confidence: high
funding_total: ~$35M (disclosed)
last_funding: Series A $25M (2025-11-19, Greylock Partners)
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, data-security, ai-data-governance]
---

# Bedrock Security

> Now operating as **Bedrock Data** (rebrand from Bedrock Security). Primary category: [dspm](../categories/dspm.md).

**One-liner** — An AI-native data security posture management (DSPM) platform that discovers, classifies, and governs sensitive enterprise data in place using a "Metadata Lake," without moving data outside the customer boundary.

## What it does
Bedrock continuously discovers and classifies sensitive data across cloud, SaaS, on-prem, and AI environments, then scores and helps remediate data-security posture (over-exposed data, stale data, access risk). Its differentiator is a patented **Metadata Lake** that autonomously catalogs data *in place* — it reads metadata/context rather than copying the underlying data out, which keeps regulated data inside the customer's trust boundary. The pitch is "operationalizing a data security program": not just visibility, but driving down exposure and improving access governance, increasingly framed around safe AI/RAG adoption.

## Where it sits in the stack
Data layer — [dspm](../categories/dspm.md). Lethal-trifecta role: protects the **sensitive-data** leg by finding and reducing where sensitive data lives and who/what can reach it (including AI agents and copilots). Lives in the data trust zone feeding AI systems; adjacent to [dlp](../categories/dlp.md) and [data-access-governance](../categories/data-access-governance.md).

## Deployment & architecture
SaaS control plane with agentless, metadata-based scanning across private cloud, IaaS, PaaS, SaaS, and AI environments; data stays in place. Aimed at integrating into a broader data-security/governance program rather than acting as an inline proxy.

## Positioning & differentiators
Competes in the crowded DSPM field against [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [normalyze](normalyze.md), [concentric-ai](concentric-ai.md), [symmetry-systems](symmetry-systems.md), and [wiz](wiz.md)'s DSPM. Its angle is the "Metadata Lake" / data-stays-in-place architecture and AI-native classification, positioned for the AI-data-governance moment. Founder/CEO Bruno Kurtic co-founded Sumo Logic, which shapes the data-platform-at-scale narrative. Note marketing language ("industry-first," "frictionless") is vendor framing.

## Ownership, funding & M&A
Independent, VC-backed. $10M seed (March 2024, Greylock) and a $25M Series A announced 2025-11-19, led by Greylock Partners with Mangusta Capital, Mantis Venture Capital, and Pier 88 Investment Partners. No seed M&A flag; none found. Ownership confidence high (recent primary funding announcement).

## CTO / hedge-fund lens
DSPM is **Day-1** for a fund standing up AI on internal data — you must know where MNPI/PII/material data sits before pointing a copilot or RAG pipeline at it. Bedrock is a credible newer entrant; for a hedge fund the practical question is whether to buy a focused DSPM or use DSPM bundled into a platform already owned ([microsoft-purview](microsoft-purview.md), [wiz](wiz.md), [rubrik](rubrik.md)). The data-in-place architecture is attractive for regulated shops wary of exporting sensitive data to a scanner. Early-stage vendor risk applies (small, ~Series A).

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [symmetry-systems](symmetry-systems.md), [normalyze](normalyze.md), [concentric-ai](concentric-ai.md), [securiti](securiti.md), [microsoft-purview](microsoft-purview.md), [wiz](wiz.md).

## Open questions / to verify
- Exact total funding and full cap table (only seed + Series A confirmed; total ~$35M is disclosed-rounds sum).
- Confirm all three co-founders and current exec roster post-rebrand.
- Real-world classification accuracy / scale vs. Cyera/Sentra (independent benchmarks).

## Sources
- [Bedrock Data Announces $25 Million Series A](https://www.businesswire.com/news/home/20251119811935/en/) — fetched 2026-06-28 — supports: Series A amount/date/lead, HQ, CEO, product/Metadata Lake; confidence: high.
- [Bedrock Data Series A (Yahoo Finance mirror)](https://finance.yahoo.com/news/bedrock-data-announces-25-million-150000042.html) — fetched 2026-06-28 — supports: same; confidence: high.
- Earlier coverage (seed $10M, March 2024, Greylock; founders/founded 2021) via BusinessWire/Crunchbase — confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (Greylock seed + $25M Series A Nov 2025), rebrand to "Bedrock Data," Menlo Park HQ, founded 2021, DSPM/Metadata-Lake product. No M&A. Set ownership_confidence high.
