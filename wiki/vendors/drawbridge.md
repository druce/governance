---
title: Drawbridge
type: vendor
name: Drawbridge
slug: drawbridge
aka: [Drawbridge Partners, DrawbridgeConnect, Drawbridge Cyber Risk Intelligence]
primary_category: vendor-risk
also_listed_in: [enterprise-grc]
website: "https://www.drawbridgeco.com"
founded: 2018
hq: null
ownership_state: pe-owned
owner: "Francisco Partners and Long Ridge Equity Partners (controlling holder undisclosed)"
ownership_note: "Long Ridge Equity Partners minority growth investment 2021-03; Francisco Partners strategic growth investment announced 2022-09-06 (closed 2022-09-01 per deal database), terms undisclosed; Long Ridge and leadership remain significant holders. No ownership change found through 2026-10-23."
acquisition: {announced: 2022-09-06, closed: null, price: null}
funding_total: null
last_funding: "Francisco Partners strategic growth investment, announced 2022-09-06 (terms undisclosed)"
market_position: {vendor-risk: niche-specialist, enterprise-grc: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: alternative investment managers (hedge funds, private equity) and PE portfolio companies; small-to-mid-sized firms without a large in-house security team
last_verified: 2026-10-23
verify_after: null
tags: [alternative-investments, managed-cyber-program, vendor-due-diligence, ddq, cyber-benchmarking, pen-testing, sec-cyber-rules, pe-portfolio-monitoring]
sources:
  - {claim: "Positioning as cybersecurity specialist for alternative investment firms combining technology and human expertise; Cyber Risk Intelligence platform modules; service lines incl. Vendor Risk Assessment and AI Risk Intelligence; 1,200+ firms", url: "https://www.drawbridgeco.com/", date: 2026-10-23, confidence: medium}
  - {claim: "Francisco Partners strategic growth investment; Long Ridge and leadership remain significant equity holders; 900+ funds (2022)", url: "https://www.businesswire.com/news/home/20220906006016/en/Drawbridge-Announces-Strategic-Growth-Investment-from-Francisco-Partners", date: 2026-10-23, confidence: medium}
  - {claim: "Next-gen cyber risk assessment (2024-08-22): benchmarking vs 1,000+ managers; Crosscheck DDQ validation", url: "https://www.opalesque.com/industry-updates/7469/drawbridge-releases-next-gen-cyber-risk-assessment-tool.html", date: 2026-10-23, confidence: medium}
  - {claim: "DrawbridgeConnect vendor due diligence workflow; Enfusion adoption (2020)", url: "https://mondovisione.com/news/drawbridge-partners-introduces-drawbridgeconnect-platform-2019813/", date: 2026-10-23, confidence: medium}
---

# Drawbridge

> Primary category: [vendor-risk](../categories/vendor-risk.md). Also listed in [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — A cybersecurity software-plus-services firm built only for hedge funds and private equity managers. It runs a fund's cyber programme (assessments, pen tests, policies, training, vendor due diligence) through a proprietary scoring and benchmarking platform and a team of advisors.

**What it does** — Drawbridge sells a **managed cybersecurity programme** for alternative investment managers, assembled from two parts. It is important to keep them apart.

*Software (the platform).* The **Cyber Risk Intelligence** platform (earlier branded **DrawbridgeConnect**) is the system of record for a firm's cyber programme. Modules listed on its site: Cyber Assessment, Cyber Analysis, **Peer Benchmarking** (against 1,200+ funds by its count), Cyber Scoring, Remediation Planning, Reporting, Regulatory Readiness, and, for PE sponsors, Portfolio Analytics and Portfolio Company Tracking. The earlier DrawbridgeConnect platform included a **vendor due-diligence workflow**: send questionnaires to third parties, track completion, keep vendor records in one place. Enfusion adopted it for exactly that in 2020. Whether that questionnaire workflow is still a distinct module in the current platform is unverified.

*Services (people).* Vulnerability scanning, penetration testing, cloud assessment, tabletop exercises, policy writing, security awareness training, cyber risk assessments, **Vendor Risk Assessment**, and a newer **AI Risk Intelligence** service. Delivery is advisor-led: the 2024 assessment release describes clients working through results "with a Drawbridge advisor". Its **Crosscheck** feature has advisors validate a manager's DDQ answers against Drawbridge scan results, shared documents and the manager's other DDQ responses.

So when a respondent says "Drawbridge for TPRM", they most likely mean **Drawbridge staff assessing the firm's vendors on its behalf, with the platform as the record**, not a self-service TPRM tool their team operates.

**Naming / provenance** — Founded 2018 (company says it has served the industry "since 2018"). Trades as Drawbridge; legal and LinkedIn name **Drawbridge Partners LLC**. Product branding has moved from **DrawbridgeConnect** (2019–2022 coverage) to **Cyber Risk Intelligence** (current site). Not to be confused with unrelated companies of the same name (e.g. an ad-tech cross-device identity firm); check the domain, drawbridgeco.com.

**Ownership & viability** — `pe-owned`. **Long Ridge Equity Partners** made a minority growth investment in **March 2021**. **Francisco Partners** made a "strategic growth investment" **announced 2022-09-06** (a deal database records it closing 2022-09-01), terms undisclosed, with Long Ridge and management remaining "significant equity holders". Which party holds control is not disclosed. No ownership change, funding or sale was found for 2023 through 2026-10-23. At four years into a Francisco Partners hold, a sale or recapitalisation would be unsurprising. A buyer could be another alt-industry IT/cyber provider (the managed-services firms that serve hedge funds) or a GRC platform. For clients the risk is service continuity and price, not software availability.

**Positioning & differentiators** —
- **Vertical, not horizontal.** Every peer in [vendor-risk](../categories/vendor-risk.md) ([processunity](processunity.md), [whistic](whistic.md), [venminder](venminder.md), [panorays](panorays.md)) sells to any industry. Drawbridge sells only to alternative managers. Its questionnaires, benchmarks and regulatory readiness are built around SEC exam expectations and **LP operational due diligence**. Its peer benchmark against 1,000+ managers is something no horizontal tool can offer.
- **Service-heavy where peers are software-heavy.** [venminder](venminder.md) is the closest horizontal analogue (it also sells analyst-completed vendor assessments). Drawbridge bundles that with the rest of the cyber programme (pen tests, training, policies) for a firm with no CISO.
- **Both sides of the DDQ.** Drawbridge helps managers *answer* allocator cyber DDQs (Crosscheck) as well as *issue* vendor due diligence. That is the same two-way problem [vendict](vendict.md) attacks with generative AI, solved here with advisors.
- **Versus outside-in ratings ([bitsight](bitsight.md), [securityscorecard](securityscorecard.md)):** different instrument. Drawbridge's scoring is assessment- and evidence-based for the manager itself, not an external attack-surface score of suppliers.

**Who should choose them / anti-fit** — Fits a **small or mid-sized hedge fund or PE manager (or PE sponsor overseeing portfolio companies)** that lacks an in-house security team and wants one specialist to run its cyber programme, vendor due diligence included, to the standard LPs and the SEC expect. The survey supports this: three respondents, all in production, under TPRM. **Anti-fit:** a firm with its own CISO and security team that wants a self-service TPRM platform to run itself (use a horizontal [vendor-risk](../categories/vendor-risk.md) tool or the TPRM module of its GRC suite), and any non-alternatives firm. It is also not continuous outside-in monitoring of a large supplier base, and not a replacement for an MSSP/MDR (Drawbridge says it is not an MSP or IT provider).

**Known weaknesses / gotchas** —
- **Category ambiguity.** Drawbridge is a cyber-programme provider, and vendor risk is one service line. Treating it as a like-for-like TPRM software comparison against ProcessUnity or Whistic will mislead survey analysis. Its survey answers measure "do you outsource vendor DD to a specialist", which differs from "which TPRM platform do you run".
- **Advisor dependency.** Quality depends on the assigned advisor and the firm's service tier. Ask who does the vendor assessments, at what depth, and on what turnaround.
- **Thin public evidence after 2024.** The most recent dated product announcement found is August 2024. Current platform modules come from the homepage only.
- **Vendor-reported metrics** ("1,200+ firms", "90% of clients improved their Cyber Score within 12 months") are marketing.

**Deployment & data handling** — SaaS platform plus remote and on-site services. Clients upload policies, DDQ responses, vendor documentation and scan results, and Drawbridge staff see them. That is a concentrated, sensitive dataset about the firm's security weaknesses and its vendors. Hosting location, retention, sub-processors, and how benchmark data is anonymised across 1,000+ peer funds are **unverified** and are standard diligence questions to ask.

**Integrations & partnerships** — None verified on this pass. A Cerby integration listing references Drawbridge (seen in search results, not checked). Historically sold alongside alt-industry fund-tech vendors (Enfusion was a client; Enfusion's old press URLs now redirect to cwan.com, Clearwater Analytics). MCP support unverified (not expected).

**Compliance & FS traction** — **FS traction claimed and structural**: the whole customer base is alternative investment managers (900+ funds claimed in 2022, 1,200+ claimed in 2026). Named clients in press: Enfusion (vendor DD, 2020) and Optima Partners (questionnaire distribution). Certifications held (SOC 2 Type II etc.) unverified. Regulatory angle: its Regulatory Readiness module and services map to SEC cyber expectations for registered advisers and to LP ODD questionnaires.

**Commercial** — Not public. Probably an annual programme or retainer fee with service tiers rather than per-seat software pricing (unverified).

## Open questions

- Is vendor due diligence currently a self-service platform module, an advisor-delivered service, or both? What is the depth of a "Vendor Risk Assessment"?
- Who controls the company (Francisco Partners vs Long Ridge), and has there been any recap or sale since 2022?
- HQ (the US phone number suggests Florida; unconfirmed) and headcount.
- SOC 2 Type II / ISO 27001 status; hosting and sub-processors; anonymisation of peer-benchmark data.
- Scope and substance of the "AI Risk Intelligence" service (AI vendor assessments? AI policy?).
- Pricing model and typical annual cost for a mid-sized fund.

## Sources

- [Drawbridge homepage (Drawbridge)](https://www.drawbridgeco.com/) — fetched 2026-10-23 — supports: positioning, platform modules, service lines, client-count claims; confidence: medium (vendor marketing)
- [Drawbridge Announces Strategic Growth Investment from Francisco Partners (Business Wire)](https://www.businesswire.com/news/home/20220906006016/en/Drawbridge-Announces-Strategic-Growth-Investment-from-Francisco-Partners) — headline and snippets via search 2026-10-23 (page returned 403) — supports: Francisco Partners investment, Long Ridge/management retained stakes, 900+ funds; confidence: medium
- [Drawbridge releases next-gen cyber risk assessment (Opalesque)](https://www.opalesque.com/industry-updates/7469/drawbridge-releases-next-gen-cyber-risk-assessment-tool.html) — fetched 2026-10-23 — supports: 2024 assessment suite, peer benchmarking, Crosscheck; confidence: medium (trade press reprint of release)
- [Drawbridge Partners introduces DrawbridgeConnect platform (Mondo Visione)](https://mondovisione.com/news/drawbridge-partners-introduces-drawbridgeconnect-platform-2019813/) — via search 2026-10-23 — supports: vendor DD questionnaire workflow; Enfusion adoption; confidence: medium
- Cached: `raw/sources/2026-10-23--drawbridge--homepage-platform-services.md`, `raw/sources/2026-10-23--drawbridge--ownership-and-history.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Triggered by three in-production write-ins under Third-Party Risk (TPRM) in the October 2026 CTO survey. Primary set to vendor-risk to match how respondents use it; enterprise-grc cross-listed because the platform functions as a lightweight cyber-programme/compliance system of record. Flagged as software plus managed service, not a self-service TPRM platform.
