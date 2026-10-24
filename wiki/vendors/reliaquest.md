---
title: ReliaQuest
type: vendor
name: ReliaQuest
slug: reliaquest
aka: [GreyMatter, ReliaQuest GreyMatter, Digital Shadows]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: https://www.reliaquest.com/
founded: 2007
hq: Tampa, FL, USA
ownership_state: independent
owner: null
ownership_note: Private, growth-equity backed. >$500M round at a $3.4B valuation announced 2025-03-31, led by EQT Growth with KKR and FTV Capital; ARR >$300M, growing >30% and profitable (per EQT). CFO publicly discussing IPO readiness (July 2026); no IPO filing found as of 2026-10-23.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: '>$500M growth round at $3.4B valuation, announced 2025-03-31 (EQT Growth lead; KKR, FTV Capital, Ten Eleven, Finback)'
market_position: {ai-soc-analysts: challenger, siem-soc: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: platform subscription (vendor advertises "one predictable price"; figures not public)
fs_traction: unverified
target_customer: mid-market to large enterprise with an existing security tool estate
last_verified: 2026-10-23
verify_after: 2027-04-23
tags: [ai-soc, security-operations, mdr-adjacent, siem-less, growth-equity, ipo-candidate]
sources:
  - {claim: ">$500M round at $3.4B valuation led by EQT Growth with KKR and FTV; ARR >$300M, >30% growth, profitable; 1,000+ customers, 1,200 staff, six operating centers", url: "https://eqtgroup.com/news/eqt-leads-funding-round-exceeding-usd-500-million-in-reliaquest-a-leader-in-ai-powered-security-operations-2025-03-31", date: 2026-10-23, confidence: high}
  - {claim: "GreyMatter marketed as 'The Agentic AI Security Operations Platform' with SIEM-less / Detect at Source options and a security data pipeline", url: "https://www.reliaquest.com/platform/", date: 2026-10-23, confidence: medium}
  - {claim: "ReliaQuest positions itself as 'not an MSSP' and GreyMatter as 'your team, partnered with an agentic AI security operations platform'", url: "https://reliaquest.com/cyber-knowledge/reliaquest-vs-co-management", date: 2026-10-23, confidence: medium}
  - {claim: "Founded 2007 by Brian Murphy in Tampa; acquired Digital Shadows (2022, $160M) and EclecticIQ assets (2023)", url: "https://en.wikipedia.org/wiki/ReliaQuest", date: 2026-10-23, confidence: medium}
---

# ReliaQuest

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A Tampa-based security-operations company whose GreyMatter platform sits on top of the tools you already own (SIEM, EDR, cloud, identity) and runs triage, investigation and containment with AI agents. You buy it as a subscription to an outcome, so it sits somewhere between an AI SOC product and a managed SOC.

**What it does** — GreyMatter connects to 200+ security tools (EQT's figure) and works across them. Detection can run on your SIEM, or skip it: "Detect at Source" and a security data pipeline let you detect without centralising every log, which ReliaQuest sells as a way to cut SIEM spend. AI agents ("GreyMatter Agentic Teammates") handle alert triage, investigation and response, and the platform also does SOAR-style automation, phishing triage, exposure management and digital-risk/dark-web monitoring. The digital-risk piece comes from the 2022 Digital Shadows acquisition, and the threat-intel work from the EclecticIQ assets bought in 2023.

**Managed service vs. software: be clear what you're buying.** This is the main thing to pin down in procurement.
- **Today's marketing says it's a platform.** ReliaQuest says it is "not an MSSP" and calls GreyMatter "your team, partnered with an agentic AI security operations platform." It describes co-management as "human-led" and in the past.
- **History and buyers say it's a service.** In 2023 Gartner Peer Insights reviewers made ReliaQuest a *Customers' Choice for Managed Detection and Response*, which is a service category. It has 1,200 staff across six "global operating centers," and buyers have long described it as a co-managed SOC. The survey comment "expensive but good" fits a services-heavy subscription better than a software licence.
- **Practical reading:** you do not run GreyMatter yourself the way you run [microsoft-sentinel](microsoft-sentinel.md) or [dropzone-ai](dropzone-ai.md). ReliaQuest runs the platform and some share of the work, and AI agents now do more of it. How much is done by ReliaQuest people versus agents versus your own team **is not stated in primary material** and goes into the contract. Get named responsibilities, response SLAs, and what happens out of hours.

**Naming / provenance** — Founded 2007 by CEO Brian Murphy in Tampa, Florida. Per Wikipedia (secondary), Murphy bootstrapped it for about nine years before FTV Capital invested in 2016. GreyMatter is the platform brand. Digital Shadows (acquired 2022, $160M) is folded in.

**Ownership & viability** — `independent`, privately held and growth-equity backed. On **2025-03-31** EQT announced a round of **more than $500M at a $3.4B valuation**, led by EQT Growth with existing investors KKR and FTV Capital. EQT says ARR has passed **$300M**, is growing more than 30% a year, and the business is **operating profitably**, with 1,000+ customers. That is one of the stronger financial profiles in either neighbouring category. In a July 2026 interview the CFO talked about IPO readiness, but **no IPO filing was found as of 2026-10-23**. The likely exit is an IPO or a sale to a platform vendor. For customers, a sale is the bigger risk: the precedent is [zscaler](zscaler.md) buying the MDR provider Red Canary in 2025.

**Positioning & differentiators** —
- **Works on top of your stack, no rip-and-replace.** The 200+ integrations and the multi-SIEM / SIEM-less detection mean it suits a firm with [splunk](splunk.md), [microsoft-sentinel](microsoft-sentinel.md) or [crowdstrike](crowdstrike.md) already deployed. MDR vendors that require their own agent or SIEM do not fit that firm as well.
- **More scale and maturity than the AI SOC startups.** Peers in [ai-soc-analysts](../categories/ai-soc-analysts.md) ([dropzone-ai](dropzone-ai.md), [prophet-security](prophet-security.md), [7ai](7ai.md), [radiant-security](radiant-security.md)) are 2023-vintage software. ReliaQuest has about 18 years of SOC operations and $300M+ ARR. The flip side is that it is also the most service-like of them.
- **Can reduce SIEM spend.** Detect-at-source and pipeline features let a firm cut what it sends to an expensive SIEM. This is vendor-stated. Test it against your own volumes.
- **Analyst recognition is vendor-cited.** ReliaQuest claims Leader in the IDC MarketScape for Standalone AI SOC Platforms (2026) and Visionary in Gartner's 2026 MQ for Cyberthreat Intelligence Technologies. Neither is an MDR or SIEM Magic Quadrant placement. Not independently checked.

**Who should choose them / anti-fit** — Fits a **mid-size to large firm with a real tool estate and a thin SOC** that wants 24/7 detection and response without hiring a full team, and that values keeping its existing SIEM/EDR. **Anti-fit:**
- A small fund with a single-vendor stack: Microsoft E5, or [crowdstrike](crowdstrike.md) with Falcon Complete, likely covers the need for less money ("expensive" was the one survey comment).
- A firm with its own detection-engineering team that wants pure software to drive itself. Look at the AI-SOC software vendors instead.

**Known weaknesses / gotchas** — Survey write-in (2026-10): *"Reliaquest - expensive but good"*, with 2 respondents in production. Pricing is not public. The split between platform and people is ambiguous (see above). The analyst recognition on its site is vendor-curated. A future IPO or acquisition could change pricing and roadmap.

**Deployment & data handling** — SaaS. GreyMatter connects to customer tools by API. Where alert and telemetry data is stored, retention, and residency options are **unverified**. Assume security telemetry, including user and endpoint context, is processed in ReliaQuest's cloud.

**Integrations & partnerships** — 200+ security tool integrations (EQT); multi-SIEM and multicloud. Moved to a partner-first channel model in 2023 (vendor release, secondary). MCP support unverified.

**Compliance & FS traction** — **Unverified.** No named hedge-fund or asset-manager references found. The survey shows two production deployments among Oct-2026 respondents, who are mostly hedge funds and PE.

**Commercial** — Platform subscription, marketed as "One Predictable Price". Figures not public; survey feedback suggests premium.

## Open questions

- Who does the work: ReliaQuest analysts, AI agents, or the customer's team? Get a named RACI and SLAs.
- Data residency, retention and training-use terms for telemetry processed by GreyMatter's AI.
- Certifications (SOC 2 Type II, ISO 27001), not checked.
- IPO or sale status: recheck by 2027-04-23.
- Whether the Gartner MDR Customers' Choice (2023) has been renewed, and how Gartner now categorises it (MDR vs AI SOC).

## Sources

- [EQT leads funding round exceeding USD 500 million in ReliaQuest (2025-03-31)](https://eqtgroup.com/news/eqt-leads-funding-round-exceeding-usd-500-million-in-reliaquest-a-leader-in-ai-powered-security-operations-2025-03-31) — fetched 2026-10-23 — supports: round size, valuation, investors, ARR, profitability, customer/staff counts; confidence: high
- [ReliaQuest GreyMatter platform page](https://www.reliaquest.com/platform/) — fetched 2026-10-23 — supports: agentic platform positioning, SIEM-less / Detect at Source, pricing message, vendor-cited IDC/Gartner recognitions; confidence: medium (marketing)
- [GreyMatter competitive-differentiation FAQ](https://reliaquest.com/resources/greymatter-faq/competitive-differentiation-and-validation-faq/) — fetched 2026-10-23 — supports: "not an MSSP"; confidence: medium (marketing)
- [ReliaQuest vs co-management](https://reliaquest.com/cyber-knowledge/reliaquest-vs-co-management) — fetched 2026-10-23 — supports: hybrid "your team + platform" framing; confidence: medium (marketing)
- [ReliaQuest — Wikipedia](https://en.wikipedia.org/wiki/ReliaQuest) — fetched 2026-10-23 — supports: founding 2007, Tampa, Digital Shadows $160M (2022), EclecticIQ (2023); confidence: medium
- [ReliaQuest named Customers' Choice by Gartner for MDR services (BusinessWire, 2023-08-09)](https://www.businesswire.com/news/home/20230809299906/en/ReliaQuest-named-Customers-Choice-by-Gartner-for-Managed-Detection-and-Response-MDR-services) — title only (fetch blocked) — supports: MDR-service categorisation by Gartner Peer Insights; confidence: medium
- Cached: `raw/sources/2026-10-23--reliaquest--eqt-funding-and-platform.md`

## History

- [2026-10-23] Page created and researched. Added because of Oct-2026 CTO survey write-ins under AI SOC (2 in production, 1 recommended, comment "expensive but good"). Primary set to ai-soc-analysts (respondents' placement + vendor's agentic-platform positioning), with siem-soc cross-list for SIEM-less detection.
