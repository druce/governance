---
title: Blackpoint Cyber
type: vendor
name: Blackpoint Cyber
slug: blackpoint-cyber
aka: [Blackpoint, Blackpoint MDR, CompassOne, Blackpoint CompassOne, SNAP-Defense, Blackpoint AI]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: https://blackpointcyber.com/
founded: 2014
hq: null
ownership_state: independent
owner: null
ownership_note: "Private, growth-equity backed. $190M growth round led by Bain Capital Tech Opportunities with Accel (reported 2023-06-09). Founder Jon Murchison moved to Executive Chairman when Gagan Singh became CEO (2025-06-23). No sale or new round found through 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "$190M growth investment led by Bain Capital Tech Opportunities, Accel participating (reported 2023-06-09)"
market_position: {ai-soc-analysts: niche-specialist, siem-soc: platform-module}
deployment_model: [saas]
form_factor: [agent, platform]
data_leaves_tenancy: "true"
integrations: [Microsoft 365, Google Workspace, Cisco Duo]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: managed service providers (MSPs) and the small and mid-sized businesses they serve
last_verified: 2026-10-24
verify_after: null
tags: [mdr, managed-soc, msp-channel, survey-write-in, security-operations]
sources:
  - {claim: "MDR with 24/7 'human-led, AI-accelerated' SOC; 'AI-enhanced alerts'; Blackpoint AI tagline; CompassOne modules incl. SIEM (Logging & Compliance), ITDR; partner-first MSP model", url: "https://blackpointcyber.com/", date: 2026-10-24, confidence: medium}
  - {claim: "Gagan Singh appointed CEO, Jon Murchison Executive Chairman (2025-06-23); founded by former NSA experts; CompassOne 'Unified Security Posture and Response platform'", url: "https://blackpointcyber.com/media/blackpoint-cyber-appoints-gagan-singh-to-chief-executive-officer/", date: 2026-10-24, confidence: high}
  - {claim: "$190M growth round led by Bain Capital Tech Opportunities with Accel; founded 2014; MSP focus", url: "https://www.helpnetsecurity.com/2023/06/09/blackpoint-cyber-growth-investment/", date: 2026-10-24, confidence: medium}
---

# Blackpoint Cyber

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A managed detection and response (MDR) provider sold through managed service providers (MSPs). Its 24/7 SOC watches endpoints, Microsoft 365 / Google identities and cloud, and acts on threats itself. CompassOne, its platform, adds asset inventory, vulnerability and posture management, and a compliance-oriented SIEM.

**What it does** — Blackpoint sells a **managed service**, not software your team runs. The core is a 24/7 SOC that takes action on threats (isolating endpoints, locking compromised accounts) instead of only sending alerts. Its homepage claims it locks a Microsoft 365 account "every 30 minutes" on average (unsourced). Service lines: Endpoint MDR, Cloud MDR, Managed EDR, and Blackpoint ITDR for Microsoft 365, Google Workspace and Cisco Duo. **CompassOne** (launched 2025) is the platform around the service. Its modules are Security Posture Rating, Asset Inventory, Vulnerability Management, Cloud Posture, Application Control, a Tenant Administrator for MSPs that manage many clients, and **SIEM (Logging & Compliance)**. The SIEM is described as real-time event collection with automated mapping for compliance logging. That is why it is cross-listed in [siem-soc](../categories/siem-soc.md). It appears to be a logging module of the MDR platform, not a standalone SIEM competing with [splunk](splunk.md) or [microsoft-sentinel](microsoft-sentinel.md).

**What AI it claims (vendor marketing).** The site says the SOC is "human-led, AI-accelerated", the MDR has "AI-enhanced alerts for rapid threat detection and response", and it promotes "Blackpoint AI" with the tagline "AI that acts in seconds. Human expertise that built it." **No technical detail was found** on what the AI does: which models, which steps of triage or response are automated, or how much analyst review there is. Treat it as an MDR with some automation, not as an AI-SOC product in the sense of [dropzone-ai](dropzone-ai.md) or [prophet-security](prophet-security.md). It sits in [ai-soc-analysts](../categories/ai-soc-analysts.md) under the 2026-10 decision to put MDR providers there.

**Naming / provenance** — Founded 2014 by Jon Murchison, a former NSA computer operations expert. The company says it was founded by "former NSA cybersecurity experts". Earlier coverage calls its technology **SNAP-Defense**; current branding is Blackpoint MDR and CompassOne. HQ is **unverified**. Directories disagree between Ellicott City, Maryland and Denver, Colorado. The 2025 CEO release is datelined Denver, and a 2024 release called Denver its "second office".

**Ownership & viability** — `independent`, private and growth-equity backed. A **$190M growth investment** led by **Bain Capital Tech Opportunities**, with Accel, was reported **2023-06-09**. Existing backers Adelphi Capital Partners, Telecom Ventures, Pelican Ventures and WP Global Partners also took part. Directory totals of $201M to $214M disagree, so `funding_total` is left null. Leadership has changed: **Gagan Singh** (ex-McAfee, Norton, Avast) became CEO on **2025-06-23**, Murchison became Executive Chairman, and a new CFO was named in April 2026. The CEO release lists "M&A" in the remit. Three years after a Bain growth round, a sale to a larger security or MSP-tooling vendor is plausible. Precedents are [zscaler](zscaler.md) buying Red Canary and N-able buying Adlumin (see [adlumin](adlumin.md)). For an end customer the risk is that the MSP's service terms change.

**Positioning & differentiators** —
- **Channel-only, MSP-first.** Unlike [reliaquest](reliaquest.md) or [esentire](esentire.md), which sell to enterprises directly, Blackpoint is "partner-first". Most buyers get it through their outsourced IT provider. Its closest peers are Huntress, Arctic Wolf and N-able's [adlumin](adlumin.md) (no wiki pages for the first two).
- **Responds, not just alerts.** The pitch is that the SOC acts on its own: "outcomes, not just alerts". Every MDR says this, so check the response actions and authority in your contract.
- **A bundled posture stack.** CompassOne puts asset inventory, vulnerability management, cloud posture and a compliance SIEM in the same console. Small firms get one vendor. Larger firms will already own better tools for each piece.

**Who should choose them / anti-fit** — Fits a **small fund or family office whose IT is outsourced to an MSP** that already resells Blackpoint, and that wants 24/7 response coverage without hiring security staff. **Anti-fit:** a firm with its own security team and an enterprise SIEM. It will want direct vendor contracts, log retention it controls, and detection content it can tune, and Blackpoint's channel model and bundled SIEM are not built for that. It is also a poor fit if you need to buy direct rather than through an MSP (whether direct contracts exist is unverified).

**Known weaknesses / gotchas** — Survey write-in (2026-10): written into **Q46 SIEM/Logging** by **2 respondents, both in production**. That likely reflects its CompassOne SIEM / logging module or the MDR as a whole. AI claims are marketing with no detail. HQ, certifications and customer counts are not stated on primary pages. When you buy through an MSP, your contract and SLAs are with the MSP, not with Blackpoint.

**Deployment & data handling** — SaaS plus an endpoint agent (Managed EDR / application control), with API connections to M365, Google Workspace and Duo. Endpoint, identity and log telemetry is processed in Blackpoint's cloud and SOC (`data_leaves_tenancy: true`). Residency, retention, and whether telemetry is used for AI training are **unverified**. Out-of-band, so there is no inline latency.

**Integrations & partnerships** — M365, Google Workspace, Cisco Duo (ITDR). An Integrations module exists, but no full list was checked. MCP support unverified. Channel is MSPs.

**Compliance & FS traction** — A Trust Center is linked, but no certifications were named on the pages fetched. No named FS customers. The two production respondents (hedge-fund / PE-heavy sample) are the only FS evidence.

**Commercial** — Not public. Sold through MSP partners, who set end-customer pricing.

## Open questions

- What "Blackpoint AI" actually automates (triage? response? reporting?), and whether customer telemetry trains its models.
- SOC 2 / ISO 27001 status (Trust Center not reviewed).
- HQ (Maryland vs Denver) and current funding total.
- CompassOne SIEM retention periods, and whether it is sold standalone.
- Whether firms can contract directly, or only through an MSP.

## Sources

- [Blackpoint Cyber homepage](https://blackpointcyber.com/) — fetched 2026-10-24 — supports: MDR scope, AI marketing claims, CompassOne modules incl. SIEM, MSP channel; confidence: medium (marketing)
- [Blackpoint Cyber appoints Gagan Singh CEO (2025-06-23)](https://blackpointcyber.com/media/blackpoint-cyber-appoints-gagan-singh-to-chief-executive-officer/) — fetched 2026-10-24 — supports: leadership change, founding by former NSA experts, CompassOne description; confidence: high
- [Help Net Security: Blackpoint Cyber $190M growth investment (2023-06-09)](https://www.helpnetsecurity.com/2023/06/09/blackpoint-cyber-growth-investment/) — fetched 2026-10-24 — supports: round size, lead investors, founding 2014, MSP focus; confidence: medium
- Cached: `raw/sources/2026-10-24--blackpoint-cyber--site-funding-ceo.md`; earlier one-liner evidence in `raw/sources/2026-10-23--mdr-soc-writeins--one-liner-sources.md`

## History

- [2026-10-24] Page created and researched. Added because of Oct-2026 CTO survey write-ins under Q46 SIEM/Logging (2 respondents, both in production). Primary set to ai-soc-analysts per the 2026-10 decision placing MDR providers there; siem-soc cross-list for the CompassOne SIEM module.
