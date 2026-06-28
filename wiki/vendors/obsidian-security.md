---
type: vendor
name: Obsidian Security
slug: obsidian-security
categories: [sspm]
layer: foundation
aliases: []
website: https://www.obsidiansecurity.com
founded: 2017
hq: Newport Beach, California, USA
ownership: independent
ownership_detail: "Venture-backed, independent as of 2026-06-28; no acquisition found. Series C ($90M) led by Menlo Ventures, Norwest, IVP, April 2022."
ownership_confidence: high
funding_total: ~$119.5M (vendor figure at Series C)
last_funding: "Series C $90M led by Menlo Ventures / Norwest / IVP (2022-04-14)"
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [sspm, saas-security, itdr, identity-threat-detection]
---

# Obsidian Security

> Primary category: [sspm](../categories/sspm.md).

**One-liner** — A SaaS security platform that pairs posture management (SSPM) with identity threat detection and response — i.e. it both hardens SaaS configurations and watches for active account compromise and privilege abuse inside apps like M365, Salesforce, Workday, and ServiceNow.

**Categories** — [sspm](../categories/sspm.md)

## What it does
Obsidian connects via API to an organization's SaaS apps and builds a model of users, privileges, OAuth integrations, and configuration state. Beyond static posture (SSPM), its differentiator is **detection**: it baselines normal SaaS activity and alerts on threats — compromised accounts, session hijacking, privilege escalation, suspicious third-party/AI app behavior — bringing a SOC/threat-detection lens to the SaaS layer. It also covers data-exposure reduction and excessive-privilege cleanup. More recently it markets AI threat/risk management (governing AI app and agent usage touching SaaS).

## Where it sits in the stack
Sits in [sspm](../categories/sspm.md) (foundation layer), straddling SSPM and identity threat detection & response (ITDR). Trifecta-wise it primarily addresses the **sensitive-data** leg (limiting exposure and catching data-theft via compromised SaaS accounts). The detection/ITDR angle makes it more of a runtime-aware SaaS control than pure config hygiene.

## Deployment & architecture
SaaS-delivered; integrates with target apps via their APIs/OAuth (not an inline proxy or endpoint agent for core function). Streams detections to SIEM/SOC and integrates with IdP for identity context. Designed to feed a security operations workflow, not just a posture dashboard.

## Positioning & differentiators
Best known for bringing threat detection (its founders came from Carbon Black and Cylance) to SaaS, not just posture scoring — that ITDR emphasis is the main thing separating it from config-first SSPM peers. Nearest neighbors: [appomni](appomni.md) (posture/data-access depth, enterprise SSPM), [valence-security](valence-security.md) (remediation + AI security), [adaptive-shield](adaptive-shield.md) (CrowdStrike), [grip-security](grip-security.md) (SaaS/identity discovery), [wing-security](wing-security.md), [reco](reco.md), [nudge-security](nudge-security.md), [docontrol](docontrol.md).

## Ownership, funding & M&A
Independent, venture-backed. Founded 2017 by Glenn Chisholm, Ben Johnson, and Matt Wolff (alumni of Carbon Black and Cylance); HQ in Newport Beach, California. Raised a $90M Series C led by Menlo Ventures with Norwest Venture Partners and IVP (announced 2022-04-14), bringing vendor-cited total to ~$119.5M. No acquisition of Obsidian found as of 2026-06-28 — `ownership_confidence: high` that it remains independent.

## CTO / hedge-fund lens
**Day-2.** Relevant once a fund has a SOC function (in-house or MSSP) that can act on SaaS detections — Obsidian's value is as much in the alerting/response as in posture. Fit is **medium**: a small fund without security-operations capacity may not exploit the ITDR strength and could get baseline posture more cheaply elsewhere; a larger, SaaS-heavy, regulated shop wanting active detection of SaaS account compromise gets more from it than from a config-only SSPM. Supports access-review and incident-evidence needs; not directly an SR 11-7 model-risk control.

## Competitors / alternatives
[appomni](appomni.md), [valence-security](valence-security.md), [adaptive-shield](adaptive-shield.md), [grip-security](grip-security.md), [wing-security](wing-security.md), [reco](reco.md), [nudge-security](nudge-security.md), [docontrol](docontrol.md)

## Open questions / to verify
- Whether any funding round has closed since the 2022 Series C; current total.
- Depth/maturity of the newer AI threat/risk-management features vs. peers.

## Sources
- [Obsidian Security Raises $90 Million Series C Round (vendor press release)](https://www.obsidiansecurity.com/news/obsidian-security-raises-90-million-series-c-round) — fetched 2026-06-28 — supports: Series C $90M, Menlo/Norwest/IVP leads, ~$119.5M total, founded 2017, founders, SSPM + identity threat detection scope; confidence: high (primary, vendor tone).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (no acquisition), founded 2017 by Chisholm/Johnson/Wolff, Newport Beach HQ, $90M Series C led by Menlo Ventures (2022), ~$119.5M total; established SSPM + identity-threat-detection positioning. Set ownership_confidence high, status researched.
