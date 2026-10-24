---
title: Soteria
type: vendor
name: Soteria
slug: soteria
aka: [Soteria LLC, Soteria Defense, Soteria Defense MDR, Soteria Defense Managed SIEM]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: "https://soteria.io"
founded: 2014
hq: "Charleston (North Charleston), SC"
ownership_state: independent
owner: null
ownership_note: "Private, founder-led (co-founders include Paul Ihme and Glenn Starkman); aggregator reports ~$5.5M raised across 3 early rounds (one $2.5M entry 2018-04), investors not named. No acquisition found as of 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$5.5M (aggregator, unverified)"
last_funding: null
market_position: {ai-soc-analysts: niche-specialist, siem-soc: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "true"
integrations: [Panther, Microsoft Defender, SentinelOne, LimaCharlie, Microsoft 365]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: small and mid-sized businesses (including financial-services and capital-markets firms) without an in-house SOC that want 24x7 MDR, managed SIEM and incident response from one provider
last_verified: 2026-10-24
verify_after: null
tags: [mdr, managed-siem, incident-response, vciso, brand-protection, panther, nsa-alumni, survey-write-in]
sources:
  - {claim: "Charleston SC, founded 2014; Soteria Defense MDR, Domain Watch, Soteria Inspect (M365); Templum vCISO client; co-founder Glenn Starkman; no AI mention on homepage", url: "https://soteria.io/", date: 2026-10-24, confidence: low}
  - {claim: "Thomas Murray partnership to offer Soteria Defense MDR and Domain Watch; MDR on Defender/SentinelOne/LimaCharlie; 24/7 DART; managed SIEM on Panther with AI-powered detection-as-code", url: "https://cyber.thomasmurray.com/insights/thomas-murray-announces-strategic-partnership-soteria", date: 2025-11-18, confidence: medium}
  - {claim: "Panther strategic partnership for MDR line; Soteria Defense Managed SIEM; co-founder Paul Ihme", url: "https://www.businesswire.com/news/home/20240813816055/en/Soteria-and-Panther-Enter-into-Strategic-Partnership-to-Defend-Clients-from-Cyber-Threats", date: 2024-08-13, confidence: medium}
  - {claim: "11-50 employees, headcount down ~6% YoY; ~$5.5M over 3 rounds; former NSA staff; cites SEC/FINRA/NYDFS/GLBA", url: "https://simplify.jobs/c/Soteria", date: 2026-10-24, confidence: low}
---

# Soteria

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A small Charleston, SC managed-security provider founded by former NSA staff. It sells 24x7 managed detection and response (**Soteria Defense MDR**), a **managed SIEM built on Panther**, incident response, vCISO and pen-testing services to firms without their own SOC.

**Survey placement and identification** — Written in once in the October 2026 CTO survey under Q46 "SIEM / Logging" (1 respondent, **not in production**). The respondent gave the name only, no domain; the survey owner **confirmed on 2026-10-24 that it is soteria.io**, the Charleston MDR. It sells a managed SIEM, which fits the SIEM question. It cites SEC, FINRA, NYDFS and GLBA requirements, names a capital-markets client (Templum), and is distributed by Thomas Murray, a risk firm serving financial institutions. Following the wiki's rule that MDR providers are filed under [ai-soc-analysts](../categories/ai-soc-analysts.md), that is the primary category, with [siem-soc](../categories/siem-soc.md) cross-listed for the managed SIEM. Note that Soteria's own homepage does not market AI. The only AI language is Panther's "AI-powered detection-as-code", which belongs to the SIEM it runs. Treat it as a **human-led MDR**, not an agentic-SOC product.

**What it does** —
- **Soteria Defense MDR:** "a fully managed endpoint and cloud telemetry solution". It runs on the client's EDR (Microsoft Defender, SentinelOne, LimaCharlie) and covers endpoints, cloud platforms and identity providers, with 24x7 monitoring and response by its Detection and Response Team (DART).
- **Soteria Defense Managed SIEM:** Panther SIEM (partnership announced 2024-08-13) operated by Soteria. The client gets Panther's detection-as-code platform while Soteria does the triage and tuning.
- **Domain Watch:** lookalike-domain and brand-impersonation monitoring with takedowns. **Soteria Inspect:** Microsoft 365 risk assessment ("200+ points of inspection").
- **Services:** penetration testing and red teaming, digital forensics and incident response, vCISO and strategic advisory (e.g. three years as vCISO for Templum).

**Naming / provenance** — Founded 2014. Brand family "Soteria Defense" (MDR, Managed SIEM). Co-founders named in sources: Paul Ihme and Glenn Starkman. Not to be confused with unrelated companies called Soteria (e.g. Soteria Insurance, UK).

**Ownership & viability** — `independent`, private. An aggregator reports about $5.5M raised across three early rounds (investors unnamed) and 11–50 staff, with headcount down about 6% year on year (treat as approximate). This is a small MDR in a consolidating market. Larger MDRs ([reliaquest](reliaquest.md), Arctic Wolf, eSentire) and AI-SOC platforms are squeezing boutique providers, so an acqui-hire or roll-up into a regional MSSP is plausible. For clients, the risk is analyst continuity and contract terms. Because it runs on the client's own EDR and on Panther, switching away is relatively easy.

**Positioning & differentiators** —
- **Bring-your-own-EDR, Panther-based.** Many MDRs force their own agent or SIEM. Soteria operates on Defender, SentinelOne or LimaCharlie and on Panther, so the detection stack belongs to the client.
- **Boutique versus platform MDRs.** Compared with [reliaquest](reliaquest.md) (GreyMatter agentic platform at scale) or AI-SOC products such as [dropzone-ai](dropzone-ai.md) and [prophet-security](prophet-security.md), Soteria is people-first and small. That means more direct access to senior staff, but no proprietary AI triage layer.
- **One provider across the incident lifecycle.** It offers MDR, IR and forensics, vCISO, and brand protection together, which suits a firm that wants a single security partner.

**Who should choose them / anti-fit** — Fits a **small or mid-sized fund or financial firm with no SOC** that already owns Defender or SentinelOne, wants a managed SIEM without staffing it, and values a boutique relationship. **Anti-fit:** firms wanting an AI-SOC tool to augment their own analysts, large or multi-region firms needing a big follow-the-sun SOC, and firms that want a SIEM platform to run themselves (buy Panther, [microsoft-sentinel](microsoft-sentinel.md) or similar directly).

**Known weaknesses / gotchas** —
- **"AI SOC" placement is by wiki policy, not vendor claim.** No AI triage or agentic capability is claimed by Soteria itself.
- **Small and shrinking headcount** (aggregator data). That makes analyst depth and 24x7 staffing questions worth asking.
- **Thin independent evidence.** Sources are vendor and partner releases and an aggregator profile.

**Deployment & data handling** — Managed service on cloud SIEM (Panther SaaS) plus the client's EDR consoles. Security telemetry, which includes user, endpoint and identity logs, flows to Panther and is accessed by Soteria analysts. Panther's hosting model (SaaS vs customer-cloud) for Soteria clients, data residency, retention and Soteria's own access controls are **unverified**. Ask about these.

**Integrations & partnerships** — Panther (SIEM, 2024-08-13). EDRs Microsoft Defender, SentinelOne ([sentinelone](sentinelone.md)), LimaCharlie. Microsoft 365. Channel partner Thomas Murray (2025-11-18) resells Soteria Defense MDR and Domain Watch. MCP unverified (not expected).

**Compliance & FS traction** — **FS traction claimed:** the aggregator profile cites SEC, FINRA, NYDFS and GLBA requirements. The named client Templum is a capital-markets infrastructure provider (vCISO engagement). The Thomas Murray channel serves financial institutions. Soteria's own SOC 2 status is not stated (a Trust Center is linked, content not retrieved).

**Commercial** — Not public. Likely a per-endpoint or per-data-volume MDR/managed-SIEM subscription (unverified).

## Open questions

- Confirm with the respondent that "Soteria" means soteria.io.
- Soteria's SOC 2 / certifications; SOC location(s) and whether 24x7 is in-house or follow-the-sun.
- Any AI or automation in its own triage workflow beyond Panther's features.
- Investors, current headcount, pricing.

## Sources

- [Soteria homepage](https://soteria.io/): fetched 2026-10-24. Supports: services, location, Templum client, co-founder. Confidence: low (vendor marketing).
- [Thomas Murray announces strategic partnership with Soteria](https://cyber.thomasmurray.com/insights/thomas-murray-announces-strategic-partnership-soteria): dated 2025-11-18, fetched 2026-10-24. Confidence: medium.
- [Soteria and Panther enter into strategic partnership (Business Wire)](https://www.businesswire.com/news/home/20240813816055/en/Soteria-and-Panther-Enter-into-Strategic-Partnership-to-Defend-Clients-from-Cyber-Threats): dated 2024-08-13, via search snippets 2026-10-24 (page 403). Confidence: medium.
- [Simplify company profile](https://simplify.jobs/c/Soteria): fetched 2026-10-24. Supports: headcount, funding, regulatory focus. Confidence: low (aggregator).
- Cached: `raw/sources/2026-10-24--soteria--homepage-partnerships.md`

## History

- [2026-10-24] Page created and researched. Triggered by one not-in-production write-in under Q46 "SIEM / Logging" in the October 2026 CTO survey (name only, no domain). Identified as soteria.io (Charleston MDR, managed SIEM on Panther). Identification is probable, not confirmed. Primary set to ai-soc-analysts per the user's MDR-placement decision, with siem-soc cross-listed. Noted that the vendor itself makes no AI claims.
- [2026-10-24] Identification confirmed by the survey owner (soteria.io); removed the "probable" caveats.
