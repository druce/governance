---
title: VISO TRUST (Protecht)
type: vendor
name: VISO TRUST
slug: viso-trust
aka: [VISO Trust, Visotrust]
primary_category: vendor-risk
also_listed_in: [enterprise-grc]
website: "https://visotrust.com"
founded: null
hq: "United States (pre-acquisition); parent Protecht is Sydney, Australia-based"
ownership_state: acquired-closed
owner: Protecht
ownership_note: "Acquired by Protecht (Australian GRC vendor backed by PSG Equity, which invested US$280M in Protecht in 2025); announced as a completed acquisition on 2026-04-21 (Sydney dateline; Business Wire 2026-04-20 US time); sell-side advisor Bowen confirmed 'has been acquired' on 2026-04-28. Terms undisclosed. Brand retained as 'A Protecht Brand'. Pre-deal: ~$24M VC (Bain Capital Ventures, Work-Bench, Sierra Ventures, Lytical, Allstate Strategic Ventures, Cisco Investments, EnvisionX, Scale Asia)."
acquisition: {announced: 2026-04-21, closed: 2026-04-21, price: null}
funding_total: "~$24M (pre-acquisition)"
last_funding: "$7M round, 2024-11 (total $24M)"
market_position: {vendor-risk: ai-native-disruptor, enterprise-grc: platform-module}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: mid-market to enterprise security/GRC teams with small TPRM headcount
last_verified: 2026-10-23
verify_after: null
tags: [tprm, ai-native, artifact-based-assessment, soc2-report-analysis, fourth-party-risk, ai-vendor-risk, protecht]
sources:
  - {claim: "Protecht announces acquisition of VISO TRUST (Sydney, 2026-04-21); Protecht Australian GRC vendor; PSG Equity US$280M investment; co-founders remain; agentic AI to be integrated into Protecht platform", url: "https://www.protechtgroup.com/en-us/news/protecht-acquires-leading-ai-powered-risk-platform-viso-trust", date: 2026-10-23, confidence: high}
  - {claim: "VISO TRUST 'has been acquired by Protecht, a portfolio company of PSG' (Bowen, 2026-04-28); Bowen exclusive sell-side advisor", url: "https://boweninc.com/?p=11099", date: 2026-10-23, confidence: high}
  - {claim: "AI-powered TPRM across 3rd/4th/nth parties; evidence-backed assessment from SOC 2 / audit artifacts; 'A Protecht Brand'; Loews Corporation testimonial", url: "https://visotrust.com/", date: 2026-10-23, confidence: medium}
  - {claim: "$7M round Nov 2024 bringing total funding to $24M; investor list", url: "https://fintech.global/2024/11/22/viso-trust-raises-7m-to-enhance-ai-powered-third-party-risk-management/", date: 2026-10-23, confidence: medium}
---

# VISO TRUST (Protecht)

> Primary category: [vendor-risk](../categories/vendor-risk.md). Also listed in [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — AI-first third-party risk management. Instead of sending vendors long questionnaires, it ingests the evidence they already have (SOC 2 reports, pen-test letters, policies), uses AI to map it to controls, and produces an assessment in minutes. Since April 2026 it has been owned by the GRC vendor Protecht.

**What it does** — VISO TRUST's design choice is **artifact-first assessment**. A vendor uploads (or VISO collects) its existing assurance documents: SOC 2 Type II reports, ISO certificates, PCI attestations, pen-test summaries, policies. The platform's AI extracts control evidence, maps it to the buyer's framework, and flags gaps with traceable findings ("what failed, where it was found, what to do next"). Questionnaires become the exception, used only to fill gaps the evidence doesn't cover. The platform adds continuous monitoring of **fourth and nth parties**, reassessment triggers when something changes, and **AI risk assessments** for evaluating vendors' AI features.

**Naming / provenance** — Co-founders Paul Valente (CEO pre-deal; now Chief Customer Officer) and Russ Sherman (CTO). Founding year not confirmed on this pass. Written "VISO TRUST" (all caps) by the company. Post-acquisition it is marketed as "A Protecht Brand". The wiki title follows the "X (Acquirer)" convention.

**Ownership & viability** — `acquired-closed`. **Protecht**, a Sydney-based GRC (enterprise risk, compliance, operational resilience) vendor backed by **PSG Equity** (a US$280M investment in 2025), **announced the acquisition of VISO TRUST on 2026-04-21**. The release is worded as a completed deal. VISO's sell-side advisor Bowen confirmed on 2026-04-28 that VISO "has been acquired". No separate closing notice exists, so the close date is recorded as the announcement date, the same convention as other announced-as-completed deals in this wiki. Terms undisclosed. Before the deal VISO raised **~$24M** of VC, the last a **$7M round in November 2024** with Bain Capital Ventures, Work-Bench, Sierra Ventures, Cisco Investments and Allstate Strategic Ventures, among others. **Judgment: acquired and invested, so far.** Protecht says VISO's "agentic AI" will be integrated into its platform; both founders stayed; the brand and site remain live. The thing to watch is whether VISO stays sold standalone or becomes only a Protecht module.

**Positioning & differentiators** —
- **Evidence over self-attestation.** Questionnaire-centric platforms ([processunity](processunity.md), [venminder](venminder.md), [whistic](whistic.md)) are built around vendor-answered questions. VISO's premise is that the SOC 2 report the vendor already has is better evidence than its answers. [whistic](whistic.md)'s shared vendor-profile network attacks the same pain from a different angle.
- **AI-native, not AI-added.** The `ai-native-disruptor` label in vendor-risk is justified because the product was designed around AI document analysis from the start, unlike incumbents adding autofill features ([panorays](panorays.md)'s Smart Match). [vendict](vendict.md) is AI-native too, but works the *answering* side of questionnaires; VISO works the *assessing* side.
- **Now part of a GRC suite.** Under Protecht it becomes the TPRM component of a broader GRC platform, competing with suite TPRM modules from [onetrust](onetrust.md), [archer](archer.md) and [servicenow](servicenow.md). That is the `platform-module` label in enterprise-grc.
- **Versus outside-in ratings ([bitsight](bitsight.md), [securityscorecard](securityscorecard.md), [black-kite](black-kite.md)):** complementary. VISO assesses documented controls; ratings score external attack surface.

**Who should choose them / anti-fit** — Fits a firm with **many SaaS and service vendors and one or two people doing TPRM**, where reading SOC 2 reports is the bottleneck. That describes most hedge funds and PE managers, whose vendors (fund admins, market-data and SaaS providers) almost all have SOC 2 reports. Two survey respondents report it in production. Also a fit for a firm considering Protecht as its GRC platform. **Anti-fit:** a firm that wants its vendor DD fully outsourced to people ([drawbridge](drawbridge.md), [venminder](venminder.md)'s analyst service). Also a firm whose critical vendors are small and lack SOC 2-grade artifacts (less evidence to analyse), and a firm committed to a different GRC suite that may not want a component now owned by a competing suite.

**Known weaknesses / gotchas** —
- **AI-extracted findings need review.** A model summarising a 120-page SOC 2 report can miss carve-outs, complementary user-entity controls and qualified opinions. Test it in a pilot against reports your team has already read.
- **Ownership change is recent.** Roadmap, pricing and standalone availability under Protecht are untested. Ask about contract continuity and whether VISO will be bundled.
- **Survey placement.** One respondent placed VISO under "GRC / AI Governance" and another under TPRM. **The GRC placement is not a clear misplacement:** since April 2026 VISO is a brand of Protecht, a GRC suite, and it markets AI risk assessments of vendors. As a product, though, VISO itself is TPRM, so vendor-risk stays primary. The GRC answer most likely reflects the respondent buying it as part of a broader risk programme, or the "AI Governance" half of the combined question (assessing vendors' AI use).
- **Vendor-reported metrics** ("30-second" assessments, 90% faster reviews, 98% vendor response rate) are marketing.

**Deployment & data handling** — SaaS. Vendors' confidential assurance documents (SOC 2 reports are usually NDA-restricted) are uploaded to VISO and processed by its AI. Where that runs, which model providers are used, retention, training use, and whether hosting changes under Protecht (Australian parent, US product) are **unverified** and matter, because a manager may be contractually bound by its vendors' NDA terms on those reports.

**Integrations & partnerships** — Not verified on this pass. Protecht platform integration is announced (AI-driven assessments, GRC workflow agents, board analytics). MCP support unverified.

**Compliance & FS traction** — **Claimed**: the homepage shows a testimonial from Loews Corporation (a diversified holding company with insurance and financial interests) and a former backer in Allstate Strategic Ventures. Two hedge-fund/PE survey respondents report it in production (October 2026). No named asset-manager case study found. Certifications not confirmed. A TPRM vendor's own SOC 2 is the first thing to request.

**Commercial** — Not public. The vendor advertises "unlimited" vendors (suggesting platform rather than per-vendor pricing), but that is unverified, as is any change under Protecht.

## Open questions

- Founding year and pre-deal HQ city.
- Whether the deal had a separate legal close after the 2026-04-21 announcement.
- Will VISO remain sold standalone, or only within Protecht? Pricing changes post-acquisition?
- AI processing of NDA-restricted vendor reports: model providers, region, retention, training use.
- VISO's own certifications (SOC 2 Type II, ISO 27001).
- Named financial-services / asset-manager customers.

## Sources

- [Protecht Acquires Leading AI-powered Risk Platform VISO TRUST (Protecht)](https://www.protechtgroup.com/en-us/news/protecht-acquires-leading-ai-powered-risk-platform-viso-trust) — fetched 2026-10-23 — supports: acquisition announcement 2026-04-21, Protecht profile, PSG investment, founders retained, integration plan; confidence: high (primary, acquirer)
- [VISO TRUST Acquired by Protecht (Bowen)](https://boweninc.com/?p=11099) — fetched 2026-10-23 — supports: completion ("has been acquired"), Protecht as PSG portfolio company, sell-side advisor; confidence: high
- [VISO TRUST homepage (VISO TRUST)](https://visotrust.com/) — fetched 2026-10-23 — supports: product mechanism, 4th/nth-party monitoring, "A Protecht Brand", Loews testimonial; confidence: medium (vendor marketing)
- [VISO TRUST raises $7m (FinTech Global)](https://fintech.global/2024/11/22/viso-trust-raises-7m-to-enhance-ai-powered-third-party-risk-management/) — fetched 2026-10-23 — supports: Nov 2024 round, $24M total, investors; confidence: medium
- Cached: `raw/sources/2026-10-23--viso-trust--protecht-acquisition.md`, `raw/sources/2026-10-23--viso-trust--product-and-funding.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Triggered by two in-production write-ins (TPRM and GRC / AI Governance) in the October 2026 CTO survey. Research found the April 2026 Protecht acquisition, so the page is titled "VISO TRUST (Protecht)" per naming convention. Close date recorded as the announcement date (release worded as completed; Bowen confirmed 2026-04-28).
