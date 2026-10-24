---
title: Adlumin (N-able)
type: vendor
name: Adlumin
slug: adlumin
aka: [N-able Adlumin, Adlumin Security Operations, Adlumin SecOps, Adlumin MDR, Adlumin XDR, "Adlumin, Inc."]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: https://www.n-able.com/products/adlumin
founded: null
hq: Washington, DC, USA (pre-acquisition, per 2024 coverage); now part of N-able (Burlington, MA)
ownership_state: acquired-closed
owner: "N-able, Inc. (NYSE: NABL)"
ownership_note: "N-able acquired Adlumin, Inc. by merger on 2024-11-20; announced the same day as completed. Adlumin is an indirect wholly owned subsidiary. adlumin.com now redirects to n-able.com. Adlumin had already been N-able's XDR/MDR partner."
acquisition: {announced: 2024-11-20, closed: 2024-11-20, price: "$98.7M cash at close (10-K; release says ~$100M before adjustments) + up to 1,570,762 N-able shares + $120M deferred cash ($52.5M / $67.5M at 1st / 2nd anniversaries) + up to $30M earn-out (2025-26)"}
funding_total: null
last_funding: null
market_position: {ai-soc-analysts: niche-specialist, siem-soc: niche-specialist}
deployment_model: [saas]
form_factor: [platform, agent]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: SMB and mid-market IT teams, and MSPs serving them
last_verified: 2026-10-24
verify_after: null
tags: [mdr, xdr, siem, managed-soc, msp-channel, survey-write-in, security-operations]
sources:
  - {claim: "N-able acquired Adlumin 2024-11-20; ~$100M cash at close, 1,570,762 shares, $120M deferred cash, up to $30M earn-out; Adlumin = Security Operations as a Service platform, self-run or fully managed; 'AI-powered engine' benefit", url: "https://www.thomabravo.com/press-releases/n-able-acquires-existing-strategic-partner-adlumin-adding-cloud-native-xdr-and-mdr-capabilities-to-its-end-to-end-security-and-it-management-platform", date: 2026-10-24, confidence: high}
  - {claim: "10-K: acquired Adlumin, Inc. on 2024-11-20; $98.7M cash at close; deferred installments; earn-out contingent consideration fair value $16.6M; 131 employees joined", url: "https://www.sec.gov/Archives/edgar/data/1834488/000183448825000053/nabl-20241231.htm", date: 2026-10-24, confidence: high}
  - {claim: "Current branding Adlumin Security Operations; MDR 'Experts managing your security toolset'; 'AI-powered XDR platform'; 'proprietary AI to automate 90% of investigation and remediation'; SMB / MSP target", url: "https://www.n-able.com/products/adlumin", date: 2026-10-24, confidence: medium}
  - {claim: "'Cloud-native SIEM that scales with your data'; 'Unmetered data ingest'", url: "https://www.n-able.com/products/adlumin/siem", date: 2026-10-24, confidence: medium}
---

# Adlumin (N-able)

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A cloud SIEM + XDR platform with an optional MDR service, owned by N-able (the RMM / IT-management vendor) since November 2024. You can run it yourself or have N-able's Adlumin team run it for you. It is aimed at small and mid-sized firms and the MSPs that serve them.

**What it does** — Adlumin calls itself a "Security Operations as a Service platform" and has two layers:
- *Software:* a **cloud-native SIEM** with "unmetered data ingest" (priced without per-GB metering), plus XDR detection across endpoint, identity (ITDR), UEBA, DNS, threat intel and SOAR automation. A June 2026 N-able release added detection of employees' "shadow AI" tool use across Adlumin and N-able's endpoint products.
- *Service:* **Adlumin MDR**, "Experts managing your security toolset", where Adlumin's SOC monitors and responds 24/7. Pen testing and incident response are add-ons.

The release says customers can run it "with their own internal team" or have it "fully managed". So it sits between a SIEM product and a managed SOC, depending on what you buy.

**What AI it claims (vendor marketing).** N-able describes "Adlumin's AI-powered XDR platform", says it uses "proprietary AI to automate 90% of investigation and remediation" (citing N-able's own 2026 State of the SOC report, methodology not given), and claims "AI-driven detection" that cuts dwell time "from weeks to hours". The 2024 acquisition release mentioned only "an AI-powered engine with data models that delivers rapid alerts". That reads like ML-based detection, not agentic investigation. **Not independently verified.** What the "90%" covers (alert closure? automated playbooks?) is unknown.

**Naming / provenance** — Adlumin, Inc. was a Washington, DC security-operations company (CEO Robert Johnston at acquisition). Founding year **unverified** (not checked). It is still sold under the Adlumin name ("Adlumin Security Operations" / "Adlumin SecOps") on n-able.com, and adlumin.com redirects there. Not to be confused with N-able's RMM products (N-central, N-sight), which are a different category.

**Slug choice** — Slugged `adlumin` (product), not `n-able` (company). Buyers and the survey respondent shop for and name "Adlumin". N-able's core business (RMM, backup) is outside this wiki's scope. The product brand survived the acquisition. If N-able's other products are ever added, an `n-able` page should link here.

**Ownership & viability** — `acquired-closed`. **N-able, Inc. (NYSE: NABL)** acquired Adlumin by merger on **2024-11-20**. The release, issued that day, says N-able "has acquired" it. No earlier signed-deal announcement was found, so announced = closed. Terms per the FY2024 10-K: **$98.7M cash at close** (the release says ~$100M before adjustments), **up to 1,570,762 N-able shares**, **$120M deferred cash** paid $52.5M and $67.5M on the first and second anniversaries, and **up to $30M earn-out** in 2025-26 (fair value $16.6M at acquisition). 131 employees joined N-able. Headline totals of ~$266M in some press combine all of those at face value. This is **acquired and invested**, not shelved: N-able now sells security operations as one of its three pillars and keeps adding features. The risk for customers is product direction set by an MSP-tooling company, plus N-able's own ownership. N-able is public, and its PE-sponsor history (Thoma Bravo, Silver Lake) was not re-checked here.

**Positioning & differentiators** —
- **SIEM + MDR in one, with flat-priced ingest.** Compared with [splunk](splunk.md) or [microsoft-sentinel](microsoft-sentinel.md), the pitch is predictable cost and a managed option for firms without a SOC.
- **Run it yourself or have it run for you.** Compared with pure MDRs ([blackpoint-cyber](blackpoint-cyber.md), [esentire](esentire.md)), you can operate the platform with your own team and add MDR later.
- **Inside the N-able stack.** It pairs with N-central / N-sight RMM, so it is natural for MSPs and IT teams already on N-able. Its closest channel peer is [blackpoint-cyber](blackpoint-cyber.md).
- **Not an AI-native SOC.** Compared with [dropzone-ai](dropzone-ai.md) or [7ai](7ai.md), the AI is a feature of a SIEM/MDR, not the product.

**Who should choose them / anti-fit** — Fits a **small to mid-sized fund** that wants a SIEM for compliance logging and 24/7 managed response from one vendor at predictable cost, especially if its IT provider already uses N-able. **Anti-fit:** a larger firm standardised on Microsoft E5 / [microsoft-sentinel](microsoft-sentinel.md) or [crowdstrike](crowdstrike.md), or one needing an enterprise SIEM with deep query, long retention and its own detection engineering.

**Known weaknesses / gotchas** — Survey write-in (2026-10): written into **Q46 SIEM/Logging** by **1 respondent, in production**. Earn-out and deferred payments ran through 2026, so watch for roadmap or packaging changes as integration completes. Log retention periods are not on the SIEM page. AI claims rest on the vendor's own report.

**Deployment & data handling** — SaaS (cloud-native SIEM) with collectors / endpoint agent. Logs and telemetry go to Adlumin/N-able's cloud (`data_leaves_tenancy: true`). Residency, retention, and training-use terms **unverified**. Out-of-band.

**Integrations & partnerships** — Described as vendor-agnostic, integrating with existing stacks. No integration list checked. N-able RMM integration implied by the bundling. MCP support unverified.

**Compliance & FS traction** — Site lists "Compliance Support" without naming frameworks. Certifications unverified. No named FS customers.

**Commercial** — Not public. Ingest is unmetered (vendor-stated), suggesting per-user/endpoint or platform pricing. Sold direct to IT teams and through MSPs.

## Open questions

- What the "AI automates 90% of investigation and remediation" claim measures; whether any LLM/agentic investigation exists.
- SIEM retention periods and data residency; certifications (SOC 2, ISO 27001).
- Adlumin founding year.
- Whether N-able plans to retire the Adlumin brand.
- N-able's own ownership and any strategic-review/sale activity (not checked).

## Sources

- [N-able acquires existing strategic partner Adlumin (2024-11-20, hosted by Thoma Bravo)](https://www.thomabravo.com/press-releases/n-able-acquires-existing-strategic-partner-adlumin-adding-cloud-native-xdr-and-mdr-capabilities-to-its-end-to-end-security-and-it-management-platform) — fetched 2026-10-24 — supports: deal date and terms, self-run vs managed model, AI-engine claim; confidence: high
- [N-able FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1834488/000183448825000053/nabl-20241231.htm) — fetched 2026-10-24 (MD&A and Item 5 read; Note 3 not reached) — supports: close date 2024-11-20, $98.7M cash at close, deferred and earn-out terms, 131 employees; confidence: high
- [N-able: Adlumin Security Operations](https://www.n-able.com/products/adlumin) — fetched 2026-10-24 — supports: current branding, MDR/XDR scope, AI marketing claims, SMB/MSP target; confidence: medium (marketing)
- [N-able: Adlumin SIEM](https://www.n-able.com/products/adlumin/siem) — fetched 2026-10-24 — supports: cloud-native SIEM, unmetered ingest; confidence: medium (marketing)
- Cached: `raw/sources/2026-10-24--adlumin--n-able-acquisition-and-product.md`

## History

- [2026-10-24] Page created and researched. Added because of an Oct-2026 CTO survey write-in under Q46 SIEM/Logging (1 respondent, in production). Slug `adlumin` (product brand that buyers name) rather than `n-able`. Primary ai-soc-analysts per the 2026-10 MDR-placement decision; siem-soc cross-list for its cloud SIEM.
