---
title: Symmetry Systems
type: vendor
name: Symmetry Systems
slug: symmetry-systems
aka: []
primary_category: dspm
also_listed_in: [data-access-governance]
website: https://www.symmetry-systems.com
founded: 2021
hq: San Jose, California, USA
ownership_state: acquired-pending
owner: Zscaler
ownership_note: 'Zscaler (NASDAQ: ZS) signed a definitive agreement 2026-05-19, announced 2026-05-21; $175.0M total consideration (cash + restricted shares subject to future employment services) per Zscaler''s Form 10-Q for the quarter ended 2026-04-30, Note 17, which states the deal is "expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions" (Zscaler FY ends 2026-07-31). No completion 8-K, press release, or other filing confirms close as of 2026-07-27 — treated as pending, not closed. Prior: VC-backed, $17.7M inside round 2023 (ForgePoint + Prefix).'
acquisition: {announced: 2026-05-21, closed: null, price: '$175.0M (cash + restricted shares)'}
funding_total: ~$33M (approx; disclosed rounds)
last_funding: $17.7M inside round (2023-08-09, ForgePoint Capital + Prefix Capital)
market_position: null
deployment_model: [saas, self-hosted, on-prem]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated
last_verified: 2026-07-27
verify_after: 2026-09-15
tags: [dspm, data-access-governance, identity-graph, darpa, zscaler, acquired-pending]
sources:
  - {claim: acquisition-pending, url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368326000096/zs-20260430.htm", date: 2026-05-26, confidence: high}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368326000096/zs-20260430.htm", date: 2026-05-26, confidence: high}
  - {claim: acquisition-announced, url: "https://ir.zscaler.com/news-releases/news-release-details/zscaler-acquire-symmetry-systems-combining-zero-trust-and-access", date: 2026-05-21, confidence: high}
---

# Symmetry Systems

> **Re-verified 2026-07-27 against Zscaler's SEC filings.** Data+AI security posture platform that fuses the data estate with the full identity graph. **Under a signed definitive agreement to be acquired by [zscaler](zscaler.md) for $175.0M — signed 2026-05-19, announced 2026-05-21, close NOT yet confirmed** (Zscaler's 10-Q says "expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions"; Zscaler's FY ends 2026-07-31). Still an independent company on paper as of 2026-07-27, and symmetry-systems.com is still live on its own domain. Primary category: [dspm](../categories/dspm.md); also [data-access-governance](../categories/data-access-governance.md).

**One-liner** — A DSPM platform that maps sensitive data to *who can reach it* — humans, service accounts, AI agents, third parties — and can automatically remediate over-permissioned or misconfigured access.

## What it does
Symmetry discovers and classifies sensitive data across clouds, SaaS, on-prem, legacy, and air-gapped stores, then joins that data map to a complete **identity graph** so you see not just what is exposed but exactly which identity could reach it and what they could do. **DataGuard** delivers the DSPM/data-access-governance view; **DataEnforce** acts on it — auto-remediating misconfigurations, revoking excess permissions, and enforcing policy without requiring a separate DLP or PAM tool. Increasingly positioned around exposure at the intersection of data and *agentic* identities.

## Where it sits in the stack
Data layer — primary [dspm](../categories/dspm.md), secondary [data-access-governance](../categories/data-access-governance.md). It controls access to sensitive data — reducing blast radius by knowing and shrinking who/what can reach it, including AI agents. Adjacent to [dlp](../categories/dlp.md) and identity tooling ([veza](veza.md), [sailpoint](sailpoint.md)).

## Deployment & architecture
Flexible deployment — managed SaaS, customer-hosted, cloud, on-prem, legacy, and air-gapped — which is unusual in DSPM and matters for regulated/isolated environments. Builds an identity-to-data graph rather than only tagging data at rest. Included as a Representative Vendor in the 2025 Gartner Market Guide for DSPM.

## Positioning & differentiators
Differentiator is the **identity-graph fusion** (data + identities + actions) and the active-remediation angle (DataEnforce), plus broad deployment reach including air-gapped. Origin: DARPA-funded research at UT Austin. Competes with [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [bedrock-security](bedrock-security.md), [proofpoint-dspm](proofpoint-dspm.md), [concentric-ai](concentric-ai.md), and [varonis](varonis.md) on the access-aware DSPM edge. Smaller/quieter than the best-funded DSPM players, so vendor-scale risk applies.

## Ownership, funding & M&A
- **M&A — SIGNED BUT PENDING, corrected 2026-07-27.** [zscaler](zscaler.md) (NASDAQ: ZS) **entered into a definitive agreement on 2026-05-19** to acquire Symmetry Systems, Inc., publicly announced **2026-05-21**. **Total consideration $175.0M**, "consisting of cash and restricted shares subject to future employment services." Source: Zscaler's **Form 10-Q for the quarter ended 2026-04-30** (filed 2026-05-26), **Note 17 *Subsequent Event***, which states the transaction "is **expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions**." Zscaler's fiscal year ends 2026-07-31, so the expected close window runs through 2026-07-31.
- **Not closed as of 2026-07-27.** No Item 2.01 completion 8-K, no "Zscaler completes acquisition" press release, and no other filing confirms close: EDGAR full-text search for "Symmetry" against Zscaler's CIK returns only the 10-Q and the same-day earnings 8-K, and Zscaler has filed nothing but Forms 4 and 144 since 2026-05-26. Every public headline still reads "to acquire" / "announces intent to acquire," and Symmetry's own 2026-05-21 post ("A New Chapter for Symmetry Systems: Joining Forces with Zscaler") refers in its forward-looking-statements section to "the **proposed** acquisition." symmetry-systems.com remains live on its own domain with a "Zscaler **to acquire** Symmetry Systems" banner — no redirect to zscaler.com. Ownership state is therefore **`acquired-pending`**, not closed. Re-verify after Zscaler's FY2026 Form 10-K (FY ended 2026-07-31; the FY2025 edition was filed 2025-09-11) — hence `verify_after: 2026-09-15`.
- **Price was previously recorded as undisclosed.** The press release gave no terms, but the 10-Q discloses $175.0M. For scale: that is more than 4x what Zscaler paid for [splxai](splxai.md) ($40.6M cash, closed 2025-10-31), so Symmetry is a materially bigger bet than the SPLX tuck-in — though still small next to Red Canary.
- **Prior funding:** ~$15M Series A (2022) + $17.7M inside round (2023-08-09, ForgePoint + Prefix, W11, TSG) — ~$33M total (approximate). At $175.0M this is roughly a 5x return on invested capital, a respectable but not spectacular outcome for a DSPM player.
- The seed had no M&A flag and an earlier research pass wrongly recorded it as independent; corrected 2026-06-28 via the Zscaler/Symmetry primary announcements, then corrected again 2026-07-27 from `acquired-closed` to `acquired-pending`. See [ai-security-m-and-a-map](../comparisons/ai-security-m-and-a-map.md).

### Two Zscaler deals, one platform story
Zscaler is assembling an AI-security stack by acquisition, and this page and [splxai](splxai.md) are two pieces of the same build-out — but they are at **different stages**, which matters for how you shop them:

| | [splxai](splxai.md) (SPLX) | Symmetry Systems |
|---|---|---|
| Status | **Closed** 2025-10-31 | **Pending** — signed 2026-05-19 |
| Price | $40.6M cash | $175.0M (cash + restricted shares) |
| Brings | AI red-teaming + runtime guardrails | Data Access Graph (data↔identity mapping) |
| Layer | Model/prompt | Data |

The two are complementary rather than overlapping: SPLX tests and guards what an AI *application* does with prompts and responses, while Symmetry maps what data an *identity or agent* can actually reach. Stitched into the Zero Trust Exchange alongside Red Canary (SecOps), the intended story is discover data and identities (Symmetry) → govern agent access inline (Zscaler's existing enforcement points) → test and guard the apps (SPLX). That is a coherent architecture on paper, but as of 2026-07-27 it is roadmap: the Symmetry deal has not even closed, and no shipped product yet fuses the Access Graph with Zscaler's inline enforcement. Treat integration claims as forward-looking until Zscaler ships and documents them.

## CTO / hedge-fund lens
DSPM is **Day-1** for AI on internal data; Symmetry's identity-aware cut is appealing where the real question is "which account or agent could exfiltrate this." The flexible/air-gapped deployment suits funds unwilling to send sensitive data to a cloud scanner. Indirect SR 11-7 relevance (governs data feeding models). Weigh its smaller scale against bigger DSPM vendors; good shortlist candidate where identity-to-data lineage and on-prem/air-gapped coverage are priorities.

**Buy-side caveat as of 2026-07-27: this is a company mid-transaction.** The Zscaler deal is signed at $175.0M but not closed, with the expected close window running through 2026-07-31. If you are evaluating Symmetry now you are effectively evaluating a future Zscaler SKU: expect roadmap and packaging to be re-cut around the Zero Trust Exchange, and expect the air-gapped/on-prem deployment flexibility — the differentiator most relevant to funds unwilling to ship data to a cloud scanner — to be the thing most at risk, since it fits awkwardly with a cloud-delivered SSE platform. If you already run Zscaler, wait for close and negotiate it into the platform deal. If you do not, get contractual commitments on standalone availability and deployment modes before signing, or shortlist [cyera](cyera.md)/[sentra](sentra.md)/[varonis](varonis.md) instead.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [bedrock-security](bedrock-security.md), [proofpoint-dspm](proofpoint-dspm.md), [concentric-ai](concentric-ai.md), [varonis](varonis.md), [microsoft-purview](microsoft-purview.md), [wiz](wiz.md).

## Open questions / to verify
- ~~Acquisition price~~ — **RESOLVED 2026-07-27**: $175.0M total consideration, per Zscaler's 10-Q Note 17.
- **Did the Zscaler deal actually close by 2026-07-31 (end of Zscaler FY2026)?** Unconfirmed as of 2026-07-27. Check Zscaler's FY2026 Form 10-K (expect ~2026-09-11) or an Item 2.01 8-K. This is the single most important open item on the page — `verify_after: 2026-09-15`.
- Whether DataGuard/DataEnforce survive as standalone products post-close, and whether the on-prem/air-gapped deployment options are retained under Zscaler.
- Precise total funding and any round since the 2023 inside round.
- Current customer scale / traction relative to Cyera/Sentra.
- How much of DataEnforce auto-remediation customers actually run in enforce (vs. observe) mode.

## Sources
- [Zscaler Form 10-Q, quarter ended 2026-04-30](https://www.sec.gov/Archives/edgar/data/1713683/000171368326000096/zs-20260430.htm) (filed 2026-05-26), Note 17 *Subsequent Event* — fetched 2026-07-27 — supports: **definitive agreement signed 2026-05-19**, **$175.0M total consideration** (cash + restricted shares subject to future employment services), and **deal NOT closed** ("expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions"); confidence: high. Cached: `raw/sources/2026-07-27--symmetry-systems--zscaler-10q-pending-175m.md`
- [Zscaler press: Zscaler to Acquire Symmetry Systems](https://ir.zscaler.com/news-releases/news-release-details/zscaler-acquire-symmetry-systems-combining-zero-trust-and-access) — fetched 2026-06-28, re-checked 2026-07-27 — supports: public announcement date 2026-05-21, "**to acquire**" (pending) framing, Access Graph / AI-agent rationale, no terms disclosed; confidence: high
- [Symmetry Systems: A New Chapter — Joining Forces with Zscaler](https://www.symmetry-systems.com/news/zscaler-acquires-symmetry/) — fetched 2026-07-27 — supports: vendor-side announcement 2026-05-21; forward-looking-statements section refers to "the **proposed** acquisition," corroborating pending status; confidence: med (vendor)
- [Symmetry Systems Closes $17.7M (Symmetry newsroom)](https://www.symmetry-systems.com/news/symmetry-systems-closes-17-7-million-to-scale-its-ai-powered-data-security-platform/) — fetched 2026-06-28 — supports: $17.7M round, investors, date, product (DataGuard/DataEnforce), deployment; confidence: high.
- [Symmetry Systems Raises $17.7M (SecurityWeek)](https://www.securityweek.com/symmetry-systems-raises-17-7m-for-data-security-posture-management-platform/) — fetched 2026-06-28 — supports: round + DSPM positioning, DARPA/UT Austin origin; confidence: med.
- [Symmetry Systems — About](https://www.symmetry-systems.com/about/) — fetched 2026-06-28 — supports: HQ San Jose, identity-graph positioning; confidence: med (vendor).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (private), San Jose, DARPA/UT-Austin origin, ~$33M raised incl. $17.7M (2023). Product = DataGuard (DSPM) + DataEnforce (remediation), identity-graph differentiator. No M&A. Set ownership_confidence high.

- [2026-06-28] CORRECTION (lint cross-check): ownership independent→acquired. Zscaler acquisition confirmed (announced 2026-05-21); earlier research missed it. Source cached.
- [2026-07-27] URL audit + M&A re-verification against primary SEC filings. **CORRECTION: `ownership_state` acquired-closed → acquired-pending.** The 2026-06-28 pass recorded `closed: 2026-05-21` — a duplicate of the announcement date with no supporting citation, inferred from the cached note's "close expected shortly after announcement." Zscaler's Form 10-Q for the quarter ended 2026-04-30 (filed 2026-05-26), Note 17 *Subsequent Event*, is explicit that this deal was **signed but not closed**: definitive agreement 2026-05-19, "expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions" (Zscaler FY ends 2026-07-31). Confirmed no close as of today: no Item 2.01 8-K (EDGAR FTS for "Symmetry" on CIK 0001713683 returns only the 10-Q + the same-day earnings 8-K; nothing but Forms 4/144 filed since 2026-05-26), no completion press release, symmetry-systems.com still live on its own domain with a "Zscaler **to acquire**" banner. Set `closed: null`, `verify_after: 2026-09-15` (post-FY2026 10-K). **Also resolved the price**, previously "terms undisclosed": **$175.0M** total consideration (cash + restricted shares subject to future employment services) per the same note — ~4x the $40.6M Zscaler paid for [splxai](splxai.md). Added a Zscaler two-deal comparison (SPLX closed/model-layer vs Symmetry pending/data-layer) and a mid-transaction buy-side caveat. Same defect pattern as [natoma](natoma.md): announced date copied into the closed field, turning a pending deal into a closed one. Cached 1 new source.
