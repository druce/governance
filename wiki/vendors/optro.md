---
title: Optro
type: vendor
name: Optro
slug: optro
aka: [AuditBoard, SOXHUB]
primary_category: enterprise-grc
also_listed_in: []
website: https://optro.ai/
founded: 2014
hq: Cerritos, California, USA
ownership_state: pe-owned
owner: Hg
ownership_note: Acquired by Hg (private equity) for >$3B — announced 2024-05-23, completed 2024. Rebranded AuditBoard → Optro 2026-03-09; ownership unchanged.
acquisition: {announced: 2024-05-23, closed: null, price: null}
funding_total: Series B (2018, Battery Ventures) prior to PE buyout
last_funding: Acquired by Hg, >$3B, 2024
market_position: null
deployment_model: [saas]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [grc, audit, risk-management, compliance, esg, ai-governance]
sources:
  - {claim: "AuditBoard renamed to Optro, announced 2026-03-09; new domain optro.ai", url: "https://www.prnewswire.com/news-releases/meet-optro-auditboard-unveils-new-identity-as-ai-transforms-grc-302707325.html", date: 2026-07-27, confidence: high}
  - {claim: "FairNow (AI governance) acquired fall 2025; CEO Raul Villar Jr.", url: "https://www.accountingtoday.com/news/auditboard-now-styles-itself-optro", date: 2026-07-27, confidence: high}
---

# Optro

> Primary category: [enterprise-grc](../categories/enterprise-grc.md).
> Formerly **AuditBoard** (2017–2026) and SOXHUB before that.

**One-liner** — A cloud audit-and-risk platform that grew from internal audit into a broad connected-risk (GRC + ESG) suite; PE-owned by Hg; rebranded from AuditBoard to Optro in March 2026 with an AI-forward "agentic GRC" pitch.

**What it does** — Started in internal audit / SOX (as SOXHUB, then AuditBoard) and expanded into a "connected risk" platform: audit management, risk management, compliance (SOX, IT compliance), third-party risk, business continuity, ESG reporting, and — since the fall-2025 FairNow acquisition — a dedicated AI-governance module. Strong traction with internal-audit and finance teams; claims more than half the Fortune 500.

**Where it sits in the stack** — [enterprise-grc](../categories/enterprise-grc.md), governance layer. System of record for audit/risk/compliance, not a runtime data control or inline prompt/egress control. The FairNow module hosts AI-governance and model-risk attestations, overlapping [ai-governance-platform](../categories/ai-governance-platform.md).

**Deployment & architecture** — SaaS. Integrates with ERP/finance systems, IT and security tooling; questionnaire and evidence-collection automation; the 2026 rebrand pitch is "agentic systems of action" — AI agents for autonomous control testing and risk surfacing (marketing framing; depth unverified).

**Positioning & differentiators** — Known for an audit-first heritage and usability, which differentiates it from risk-first incumbents [archer](archer.md) / [servicenow](servicenow.md) and no-code challengers [logicgate](logicgate.md) / [onspring](onspring.md). Strongest where internal audit drives the buy. **Naming caution for survey design:** the Optro name is only months old (March 2026) — most practitioners still know it as AuditBoard, so surveys should show "Optro (formerly AuditBoard)".

**Ownership, funding & M&A** — `pe-owned`. Acquired by **Hg** (software-focused PE) for over $3 billion — announced 2024-05-23, completed in 2024. **Renamed Optro on 2026-03-09** (announced at the IIA Great Audit Minds conference); ownership unchanged. New CEO **Raul Villar Jr.** (ex-Paycor) named July 2025. Acquired **FairNow**, an AI-governance platform, in fall 2025. Founded 2014; HQ Cerritos, CA; ~$200M ARR by late 2023. (high confidence)

**CTO / hedge-fund lens** — Day-1 GRC, particularly for funds where internal audit / SOX-style controls drive the requirement. Good fit for a fund with a real internal-audit function; for a small fund whose need is purely AI governance, a lighter or AI-specific tool may suffice — though the FairNow module now gives it a direct AI-governance answer.

**Competitors / alternatives** — [servicenow](servicenow.md), [archer](archer.md), [logicgate](logicgate.md), [onspring](onspring.md), [onetrust](onetrust.md).

**Open questions / to verify** — Depth of the FairNow-based AI-governance module vs. dedicated [ai-governance-platform](../categories/ai-governance-platform.md) tools; whether the "agentic" testing features are shipping or roadmap.

## Sources
- [Meet Optro: AuditBoard unveils new identity (PR Newswire)](https://www.prnewswire.com/news-releases/meet-optro-auditboard-unveils-new-identity-as-ai-transforms-grc-302707325.html) — fetched 2026-07-27 — supports: rename announced 2026-03-09, optro.ai domain, positioning; confidence: high
- [AuditBoard now styles itself Optro (Accounting Today)](https://www.accountingtoday.com/news/auditboard-now-styles-itself-optro) — fetched 2026-07-27 — supports: FairNow acquisition (fall 2025), CEO Raul Villar Jr., SOXHUB→AuditBoard 2017 history, independent corroboration; confidence: high
- [AuditBoard agrees to be acquired by Hg](https://hgcapital.com/insights/auditboard-agrees-to-be-acquired-by-hg) — fetched 2026-06-28 — supports: Hg acquisition >$3B, date, founded 2014, $200M ARR, scope; confidence: high
- [Hg acquires AuditBoard for $3B (SecurityWeek)](https://www.securityweek.com/private-equity-firm-hg-acquires-auditboard-for-3-billion/) — fetched 2026-06-28 — supports: deal value, independent corroboration; confidence: high
- Cached: `raw/sources/2026-07-27--optro--rebrand-announcement.md`

## History
- [2026-06-28] Stub created from seed registry (as `auditboard`).
- [2026-06-28] Researched; CONFIRMED seed flag — acquired by Hg PE for >$3B (2024); ownership independent→acquired; confidence high.
- [2026-07-27] Renamed page `auditboard` → `optro` after verified 2026-03-09 rebrand (user-flagged; confirmed against press release). Added FairNow acquisition, new CEO, optro.ai domain.
