---
title: Bedrock Data
type: vendor
name: Bedrock Data
slug: bedrock-data
aka: [Bedrock Security, Bedrock Labs]
primary_category: dspm
also_listed_in: []
website: https://bedrockdata.ai/
founded: 2021
hq: Menlo Park, California, USA
ownership_state: independent
owner: null
ownership_note: VC-backed private; $25M Series A led by Greylock (2025-11). No M&A. Renamed Bedrock Security → Bedrock Data 2025-08-05 (brand change only; legal entity remains Bedrock Labs, Inc.).
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$35M (disclosed)
last_funding: Series A $25M (2025-11-19, Greylock Partners)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / mid-market
last_verified: 2026-07-27
verify_after: null
tags: [dspm, data-security, ai-data-governance]
---

# Bedrock Data

> **Formerly Bedrock Security** — renamed to **Bedrock Data** on 2025-08-05 (brand change
> only; same company, same CEO, same Menlo Park HQ, legal entity Bedrock Labs, Inc.).
> `bedrock.security` 301-redirects to `bedrockdata.ai`. Page slug renamed
> `bedrock-security` → `bedrock-data` on 2026-07-27 to follow the current company name.
> Primary category: [dspm](../categories/dspm.md).

**One-liner** — An AI-native data security posture management (DSPM) platform that discovers, classifies, and governs sensitive enterprise data in place using a "Metadata Lake," without moving data outside the customer boundary.

## What it does
Bedrock continuously discovers and classifies sensitive data across cloud, SaaS, on-prem, and AI environments, then scores and helps remediate data-security posture (over-exposed data, stale data, access risk). Its differentiator is a patented **Metadata Lake** that autonomously catalogs data *in place* — it reads metadata/context rather than copying the underlying data out, which keeps regulated data inside the customer's trust boundary. The pitch is "operationalizing a data security program": not just visibility, but driving down exposure and improving access governance, increasingly framed around safe AI/RAG adoption.

## Where it sits in the stack
Data layer — [dspm](../categories/dspm.md). It controls access to sensitive data by finding and reducing where that data lives and who/what can reach it (including AI agents and copilots). Lives in the data trust zone feeding AI systems; adjacent to [dlp](../categories/dlp.md) and [data-access-governance](../categories/data-access-governance.md).

## Deployment & architecture
SaaS control plane with agentless, metadata-based scanning across private cloud, IaaS, PaaS, SaaS, and AI environments; data stays in place. Aimed at integrating into a broader data-security/governance program rather than acting as an inline proxy.

## Positioning & differentiators
Competes in the crowded DSPM field against [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [proofpoint](proofpoint.md), [concentric-ai](concentric-ai.md), [symmetry-systems](symmetry-systems.md), and [wiz](wiz.md)'s DSPM. Its angle is the "Metadata Lake" / data-stays-in-place architecture and AI-native classification, positioned for the AI-data-governance moment. Founder/CEO Bruno Kurtic co-founded Sumo Logic, which shapes the data-platform-at-scale narrative. Note marketing language ("industry-first," "frictionless") is vendor framing.

## Ownership, funding & M&A
Independent, VC-backed. $10M seed (March 2024, Greylock) and a $25M Series A announced 2025-11-19, led by Greylock Partners with Mangusta Capital, Mantis Venture Capital, and Pier 88 Investment Partners. No seed M&A flag; none found. Ownership confidence high (recent primary funding announcement).

**Naming.** The company launched as **Bedrock Security** and **renamed to Bedrock Data on 2025-08-05** ("Bedrock Security Rebrands as Bedrock Data to Advance Data Governance, Security and Management in the AI Era"). This is a brand change, not an ownership event: the legal entity remains **Bedrock Labs, Inc.** (d/b/a Bedrock Data), Bruno Kurtic stayed CEO/co-founder across both names, the HQ is still Menlo Park, and the Metadata Lake product line carried straight over — the vendor even rehosts its old Bedrock Security press releases on the bedrockdata.ai newsroom. The rename widened the pitch from security-only to data governance + security + management for the AI era; the current site leads with "Beyond DSPM." Verified 2026-07-27.

> Do not confuse this company with an **unrelated** "Bedrock Data" at **bedrockdata.com** — a Boston-area, .406 Ventures-backed SaaS data-integration vendor (product: **Fusion**, syncing Salesforce/NetSuite/Marketo/HubSpot data), active at least 2016–2018. Different domain (`.com` vs `.ai`), different product, different investors. Its current status is unverified.

## CTO / hedge-fund lens
DSPM is **Day-1** for a fund standing up AI on internal data — you must know where MNPI/PII/material data sits before pointing a copilot or RAG pipeline at it. Bedrock is a credible newer entrant; for a hedge fund the practical question is whether to buy a focused DSPM or use DSPM bundled into a platform already owned ([microsoft-purview](microsoft-purview.md), [wiz](wiz.md), [rubrik](rubrik.md)). The data-in-place architecture is attractive for regulated shops wary of exporting sensitive data to a scanner. Early-stage vendor risk applies (small, ~Series A).

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [symmetry-systems](symmetry-systems.md), [proofpoint](proofpoint.md), [concentric-ai](concentric-ai.md), [securiti](securiti.md), [microsoft-purview](microsoft-purview.md), [wiz](wiz.md).

## Open questions / to verify
- Exact total funding and full cap table (only seed + Series A confirmed; total ~$35M is disclosed-rounds sum).
- Confirm all three co-founders and current exec roster post-rebrand (only CEO/co-founder Bruno Kurtic is confirmed by name).
- Current status of the unrelated `bedrockdata.com` (Fusion) company — no evidence found either way.
- Real-world classification accuracy / scale vs. Cyera/Sentra (independent benchmarks).

## Sources
- [Bedrock Rebrands to Advance Data Governance and AI-Ready Security](https://bedrockdata.ai/news/bedrock-security-rebrands-as-bedrock-data) — fetched 2026-07-27 — supports: rename direction Bedrock Security → Bedrock Data, date 2025-08-05, legal entity Bedrock Labs Inc., Menlo Park HQ, Bruno Kurtic CEO/co-founder; confidence: high (first-party).
- [Bedrock Security Rebrands as Bedrock Data (BusinessWire)](https://www.businesswire.com/news/home/20250805421801/en/Bedrock-Security-Rebrands-as-Bedrock-Data-to-Advance-Data-Governance-Security-and-Management-in-the-AI-Era) — 2026-07-27 — supports: same, wire copy with both names in one headline; confidence: high.
- [Bedrock Security Names Co-Founder Bruno Kurtic as CEO](https://www.businesswire.com/news/home/20240723928182/en/Bedrock-Security-Names-Co-Founder-Bruno-Kurtic-as-New-Chief-Executive-Officer) — 2026-07-27 — supports: CEO continuity across the old brand (same-entity check); confidence: high.
- [Bedrock Data Announces $25 Million Series A](https://www.businesswire.com/news/home/20251119811935/en/) — fetched 2026-06-28 — supports: Series A amount/date/lead, HQ, CEO, product/Metadata Lake; confidence: high.
- [Bedrock Data Series A (Yahoo Finance mirror)](https://finance.yahoo.com/news/bedrock-data-announces-25-million-150000042.html) — fetched 2026-06-28 — supports: same; confidence: high.
- Earlier coverage (seed $10M, March 2024, Greylock; founders/founded 2021) via BusinessWire/Crunchbase — confidence: med.
- Cached: `raw/sources/2026-07-27--bedrock-security--rebrand-to-bedrock-data.md`.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (Greylock seed + $25M Series A Nov 2025), rebrand to "Bedrock Data," Menlo Park HQ, founded 2021, DSPM/Metadata-Lake product. No M&A. Set ownership_confidence high.
- [2026-07-27] **Naming direction corrected.** URL audit found `bedrock.security` 301-redirecting to `bedrockdata.ai`, raising the question of which name is current. Verified against the vendor's own 2025-08-05 rebrand release: **Bedrock Security is the FORMER name, Bedrock Data is the CURRENT name** — the previous frontmatter had it backwards (`name: Bedrock Security`, `aka: [Bedrock Data]`) even though the body already said otherwise. Fixed: `title`/`name` → Bedrock Data, `aka` → [Bedrock Security, Bedrock Labs], `website` → bedrockdata.ai. Same-entity confirmed via CEO (Bruno Kurtic), HQ (Menlo Park), Metadata Lake product, and migrated press archive — not a domain squat. Added a disambiguation note for the unrelated bedrockdata.com/Fusion company. Slug rename to `bedrock-data` flagged, not executed.
- [2026-07-27] **Slug renamed** `bedrock-security` → `bedrock-data` (user-confirmed), following the `conductorone → c1` and `normalyze → proofpoint-dspm` precedents; inbound links, `survey-v2.csv` Wiki URL, and `index.md` updated. `aka` retains Bedrock Security.
