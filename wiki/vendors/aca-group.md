---
title: ACA Group
type: vendor
name: ACA Group
slug: aca-group
aka: [ACA, ACA Global, ACA Compliance Group, ComplianceAlpha, ACA Aponix, ACA Foreside]
primary_category: comms-surveillance
also_listed_in: [enterprise-grc]
website: https://www.acaglobal.com
founded: null
hq: New York, NY, USA
ownership_state: pe-owned
owner: Genstar Capital
ownership_note: 'PE-owned. Genstar Capital agreed on 2021-11-17 to take a controlling interest in ACA (from Starr Investment Holdings) and combine it with Genstar-backed Foreside Financial Group; the merger completed 2022-05-31, with Genstar the lead investor. Terms undisclosed. Since then ACA has made bolt-ons: Global Trading Analytics (2025-04-14) and FX Transparency (2026-03-10). New CEO Trey Loughran was appointed 2026-06-01. No sale or recap found as of 2026-10-23.'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {comms-surveillance: challenger, enterprise-grc: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: 'true'
integrations: [email, Microsoft Teams, Zoom, Slack, Bloomberg, WhatsApp, SMS, social media, voice/video, website archiving, "85+ capture connectors (vendor-stated)"]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: verified
target_customer: SEC/FCA-regulated investment managers — hedge funds, private markets (PE, private credit, real estate, VC), asset managers/RIAs, broker-dealers, investment companies, wealth managers
last_verified: 2026-10-23
verify_after: 2027-04-23
tags: [comms-surveillance, regtech, compliance-advisory, managed-services, sec, fca, 17a-4, worm, personal-trading, market-abuse, alternative-investments, pe-owned]
sources:
  - {claim: "Genstar to acquire controlling interest in ACA from Starr and combine with Foreside; Genstar majority owner", url: "https://www.acaglobal.com/insights/aca-group-and-foreside-join-forces", date: 2021-11-17, confidence: high}
  - {claim: "ACA/Foreside merger completed; Genstar lead investor", url: "https://www.businesswire.com/news/home/20220531005150/en/ACA-Group-and-Foreside-Complete-Merger-Combined-Firm-Will-Be-Known-As-ACA", date: 2022-05-31, confidence: medium}
  - {claim: "advisory + managed services + technology model; client types; offices; service lines", url: "https://www.acaglobal.com/about-us", date: 2026-10-23, confidence: medium}
  - {claim: "6,350+ clients firm-wide; product list", url: "https://www.acaglobal.com/", date: 2026-10-23, confidence: low}
  - {claim: "eComms capture/archive/surveillance scope, 17a-4 WORM, 85+ connectors, AWS, US/EU/APAC residency, AI features", url: "https://www.acaglobal.com/ecomms-surveillance-software", date: 2026-10-23, confidence: low}
  - {claim: "ComplianceAlpha eComms surveillance expansion: relationship forensics, ML/NLP, integrated archive", url: "https://www.acaglobal.com/insights/aca-group-expands-electronic-communications-surveillance-capabilities-compliancealpha-platform/", date: 2022-10-04, confidence: high}
---

# ACA Group

> Primary category: [comms-surveillance](../categories/comms-surveillance.md). Also listed in [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — The compliance consultancy that much of the alternative-investment
industry already uses, which also sells a compliance software suite (**ComplianceAlpha**).
The suite includes e-comms capture, archive and surveillance, so for many hedge funds
"ACA" is the surveillance vendor because ACA is already the compliance vendor.

## Consultancy or software? Both — be precise

ACA describes itself as "the only end-to-end governance, risk, and compliance provider
that combines expert advisory and powerful technology." In practice it sells three
different things, and a survey answer of "ACA" could mean any of them:

1. **Advisory.** Compliance consulting (founded by former regulators, 20+ years),
   mock exams, ACA Foreside (fund distribution / regulatory), performance and GIPS,
   AML, ACA Aponix cybersecurity and risk (pen testing, third-party risk advisory), and
   an "AI Risk and Governance" advisory service.
2. **Managed services.** Outsourced compliance operations, reporting/filing, and
   "surveillance and monitoring" run by ACA staff.
3. **Technology.** The ComplianceAlpha RegTech suite: Compliance Management (calendar,
   workflows, risk and policy management), Marketing and Financial Promotion Review,
   **eComms Capture, Archive and Surveillance**, Employee Compliance (personal
   trading, certifications, conflicts), Market Abuse (trade) Surveillance, Transaction
   Cost Analysis, Control Room, eLearning, AML/sanctions screening, Ethos (ESG), a
   research-compliance product for expert-network call oversight, and Vantage for
   Cyber.

The survey write-in placed ACA under Communications Surveillance (1 in production),
which is the **software** (ComplianceAlpha eComms). It may also be partly the
**managed service** if ACA staff do the alert review.

## What the e-comms product does

Per ACA's product page (vendor marketing, 2026-10-23):

- **Capture**: email; Teams, Zoom, Slack; Bloomberg; social; WhatsApp and SMS;
  voice/video; website archiving. ACA states "85+ pre-integrated connectors."
- **Archive**: "WORM-compliant storage that satisfies SEC 17a-4." This is vendor-stated.
- **Surveillance**: a policy-based lexicon/scenario engine, NLP, and "relationship
  forensics," which scores how closely employees know each other or outside contacts.
  It was added in 2022. On top sits an AI layer ("Encore AI" / AI Insights) for
  summaries, entities, sentiment and risk with the triggering language highlighted,
  plus echo suppression to cut repeat alerts. ACA says explicitly that AI "does not
  replace" human reviewers.
- **Case management** for investigations and escalation.

Like [hadrius](hadrius.md) and [greenboard](greenboard.md), ACA does **both capture/
archival and surveillance**, the two halves the category page separates. It also
pairs comms with **trade surveillance** and personal-trading oversight in the same
suite, which puts it closer to [steeleye](steeleye.md) than to a pure comms tool.

**Gap to note:** as of 2026-10-23, ACA's e-comms materials do **not** list ChatGPT,
Claude or Microsoft Copilot conversations as a capture channel. A dedicated search
found nothing either. Hadrius already treats AI-assistant conversations as a
supervised channel. If employees use enterprise AI assistants for business, ask ACA
directly how those records are captured.

## Where it sits in the stack

- [comms-surveillance](../categories/comms-surveillance.md) (governance layer). It is a
  **detective** control: it reviews after the fact and blocks nothing. Stopping data
  from leaving via a prompt is [dlp](../categories/dlp.md) /
  [ai-access-governance](../categories/ai-access-governance.md).
- [enterprise-grc](../categories/enterprise-grc.md), on the evidence of ComplianceAlpha's
  Compliance Management module (compliance calendar, testing workflows, risk and policy
  management). This is an FS-compliance-program GRC, not an enterprise IT-risk GRC like
  [archer](archer.md) or [servicenow](servicenow.md).
- **Not cross-listed to [vendor-risk](../categories/vendor-risk.md).** ACA's third-party
  risk offering is **consulting** ("Our consultants help firms establish TPRM policies,
  conduct vendor risk assessments, perform due diligence reviews"), with some portal
  tooling. It is not a vendor-risk rating and monitoring platform like
  [securityscorecard](securityscorecard.md) or [bitsight](bitsight.md).
- **Not cross-listed to [ai-governance-platform](../categories/ai-governance-platform.md).**
  "AI Risk and Governance" is listed under Advisory, not Technology. It is a consulting
  service, not a model-inventory product.

## Positioning & differentiators

- **Distribution is the moat.** ACA is already the outsourced compliance adviser,
  mock-exam provider or cyber assessor for a large share of hedge funds and PE firms
  (6,350+ clients firm-wide, vendor-stated). Buying surveillance from the same firm
  means one contract, one relationship, and staff who know your compliance manual.
- vs [hadrius](hadrius.md) / [greenboard](greenboard.md) — those are AI-native startups
  aimed at the same US adviser buyer, with similar module maps. They are faster
  shipping (Hadrius already captures Claude/ChatGPT conversations) but have far less
  institutional history and no consulting arm.
- vs [behavox](behavox.md) / [nice-actimize](nice-actimize.md) — those are
  enterprise conduct-surveillance engines for banks and large managers. ACA is sized
  for the mid-market alternative manager and wraps the software with advisory.
- vs [steeleye](steeleye.md) — both combine comms and trade surveillance. SteelEye is a
  data-platform product company with an EU/UK MAR lens. ACA is a services-led firm with
  US SEC and UK FCA coverage.
- vs Smarsh / Global Relay (no wiki pages) — those are archive-first incumbents. ACA's
  archive is one module of a broader compliance suite.

`market_position`: **challenger** in comms-surveillance (an established provider in the
alternative-asset segment, but not the archive incumbent). **niche-specialist** in
enterprise-grc (an FS-compliance-program tool, not general GRC).

## Who should choose them / anti-fit

**Good fit:** a hedge fund, PE or private-credit manager (tens to a few hundred staff)
that already uses ACA for compliance consulting or mock exams and wants comms and
personal-trading surveillance from the same firm, possibly with ACA staff doing
first-level review.

**Anti-fit:** firms wanting a best-of-breed, AI-native surveillance engine with
AI-assistant capture today; tier-1 banks needing enterprise conduct-surveillance scale;
firms that want their compliance adviser and their surveillance tooling independent of
each other; anyone needing self-hosted or in-tenant deployment.

## Known weaknesses / gotchas

- **Adviser and tool vendor in one.** If ACA both runs your surveillance and advises on
  (or mock-examines) your compliance program, decide whether that concentration is
  acceptable, and keep the evidence trail clear for examiners.
- **AI-assistant conversations not documented as a channel** (2026-10-23). See above.
- **Marketing figures are unverified.** The product page itself renders stat counters
  as "0+" and gives two different risk-scenario counts (20+ vs 150+). Rely on the body
  text and ask for specifics.
- **PE ownership since 2022.** Genstar has held ACA for about four and a half years,
  which is within a typical hold period, so a future sale or recapitalization is
  plausible. None was found as of 2026-10-23. A sale would not usually disrupt
  contracts, but it can change pricing and the roadmap.

## Deployment & data handling

Multi-tenant **SaaS** on a "cloud-first AWS architecture," with data-residency options
in the **US, EU and APAC** (vendor-stated). Data leaves your tenancy by design, because
that is what an archive is. Which LLM providers sit behind the AI Insights layer, and
whether customer communications are used to train models, is **unverified**. Get this
in writing.

## Integrations & partnerships

Capture connectors for email, Teams, Zoom, Slack, Bloomberg, WhatsApp/SMS, social and
voice (85+ claimed). Trade-data feeds from "over 5,000 brokerage institutions" for
personal-trading surveillance (vendor). No MCP/AI-assistant integrations documented.

## Compliance & FS traction

FS is the whole business. Client types on ACA's site include hedge funds, private
markets, asset managers, broker-dealers and wealth managers, and there is a named
hedge-fund testimonial (RA Capital Management's Director of Compliance). It won "Best
e-Comms Surveillance Solution" at the Capital Markets Technology Awards APAC 2025.
`fs_traction: verified`: the client base is overwhelmingly FS and this survey has an
in-production respondent. Security certifications for the platform (SOC 2 etc.) were
not found on the pages reviewed. Ask for them.

## Commercial

Not public. Typically sold as annual subscriptions per module, often bundled with
advisory or managed-service retainers. Band unknown.

## Competitors / alternatives

[hadrius](hadrius.md) · [greenboard](greenboard.md) · [steeleye](steeleye.md) ·
[behavox](behavox.md) · [shield](shield.md) · [theta-lake](theta-lake.md) ·
[nice-actimize](nice-actimize.md) · [microsoft-purview](microsoft-purview.md)

## Open questions

- AI-assistant capture (ChatGPT Enterprise / Claude Enterprise compliance APIs,
  Microsoft Copilot interactions): supported, roadmap, or not?
- Which LLMs power AI Insights; data retention and training-use terms.
- Platform certifications (SOC 2 Type II, ISO 27001).
- Founding year: the site says "more than 20 years" without a year. Left `null`.
- Whether surveillance alert review can be outsourced to ACA staff as a defined
  service. The managed-services menu lists "Surveillance and Monitoring" generically.
- Pricing bands.

## Sources

- [ACA Group and Foreside to Join Forces (ACA)](https://www.acaglobal.com/insights/aca-group-and-foreside-join-forces) — fetched 2026-10-23 — supports: 2021-11-17 agreement, Genstar controlling interest from Starr, Genstar majority owner; confidence: high
- [ACA Group and Foreside Complete Merger (BusinessWire)](https://www.businesswire.com/news/home/20220531005150/en/ACA-Group-and-Foreside-Complete-Merger-Combined-Firm-Will-Be-Known-As-ACA) — search snapshot 2026-10-23 (direct fetch 403) — supports: completion 2022-05-31, Genstar lead investor; confidence: medium
- [ACA — About us](https://www.acaglobal.com/about-us) — fetched 2026-10-23 — supports: advisory/managed-services/technology model, client types, offices, service lines; confidence: medium (vendor)
- [ACA — homepage](https://www.acaglobal.com/) — fetched 2026-10-23 — supports: 6,350+ clients, product list; confidence: low (vendor)
- [ACA — eComms Capture, Archive & Surveillance](https://www.acaglobal.com/ecomms-surveillance-software) — fetched 2026-10-23 — supports: channels, 17a-4 WORM claim, 85+ connectors, AWS, residency, AI features, RA Capital testimonial; confidence: low (vendor marketing)
- [ACA Expands eComms Surveillance in ComplianceAlpha (ACA, 2022-10-04)](https://www.acaglobal.com/insights/aca-group-expands-electronic-communications-surveillance-capabilities-compliancealpha-platform/) — fetched 2026-10-23 — supports: relationship forensics, ML/NLP, integrated archive; confidence: high
- [ACA — Cybersecurity, privacy & risk advisory](https://www.acaglobal.com/advisory/cybersecurity-privacy-risk/) — fetched 2026-10-23 — supports: TPRM delivered as consulting; confidence: medium
- Cached: `raw/sources/2026-10-23--aca-group--ecomms-and-company.md`, `raw/sources/2026-10-23--aca-group--genstar-ownership.md`

## History

- [2026-10-23] Page created and researched in one pass from a 2026-10 CTO-survey write-in
  ("ACA", 1 in production under Communications Surveillance). Established PE ownership
  (Genstar, announced 2021-11-17, merger completed 2022-05-31), the hybrid
  advisory/managed-services/technology model, and ComplianceAlpha eComms scope.
  Cross-listed enterprise-grc (Compliance Management module). Considered and rejected
  vendor-risk (TPRM is consulting, not a ratings platform) and ai-governance-platform
  (advisory only). Flagged the absence of documented AI-assistant capture.
