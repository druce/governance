---
title: Rapid7
type: vendor
name: Rapid7
slug: rapid7
aka: [InsightIDR, InsightVM, Nexpose, Metasploit, Command Platform]
primary_category: siem-soc
also_listed_in: []
website: https://www.rapid7.com/
founded: 2000
hq: Boston, MA, USA
ownership_state: public
owner: null
ownership_note: NASDAQ:RPD. Activist Jana Partners disclosed a stake in June 2024 and pushed for a sale, working with Cannae Holdings; by March 2025 Rapid7 was reported close to a settlement adding three directors. FY2026 revenue guidance $836–842M. No sale announced as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {siem-soc: legacy-incumbent}
deployment_model: [saas, hybrid]
form_factor: [platform, agent]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market to enterprise
last_verified: 2026-08-26
verify_after: 2027-02-26
tags: [siem, vulnerability-management, mdr, soar, public, activist-pressure]
sources:
  - {claim: "Jana Partners took a significant position in June 2024 and may urge a sale; working with Cannae Holdings to team with a PE firm", url: "https://www.cnbc.com/2024/06/29/two-paths-for-jana-to-bolster-shareholder-value-at-rapid7.html", date: 2026-08-26, confidence: medium}
  - {claim: "By March 2025 Rapid7 was close to a settlement with Jana adding three new directors to the eight-member board; FY revenue guidance $836–842M", url: "https://www.thedeal.com/activism/jana-agitates-for-ma-at-rapid7/", date: 2026-08-26, confidence: medium}
---

# Rapid7

> Primary category: [siem-soc](../categories/siem-soc.md).

**One-liner** — A mid-market security-operations incumbent bundling vulnerability management (InsightVM), SIEM (InsightIDR) and managed detection and response on one platform — under sustained activist pressure to sell itself.

**What it does** — Three businesses that Rapid7 sells as one Command Platform. **InsightVM** (from Nexpose) is vulnerability management and is the historical core and cash engine. **InsightIDR** is the SIEM/XDR: log collection, detection rules, UEBA and investigation. **Rapid7 MDR** is the managed service layered on top, which is how a large share of its mid-market base actually consumes the product. It also stewards **Metasploit**, the open-source exploitation framework — a genuine asset for brand and recruiting more than for revenue.

**Naming / provenance** — Founded 2000 in Boston; IPO 2015 (NASDAQ: **RPD**). Product naming has churned — Nexpose → InsightVM, and the "Insight" platform is being rebranded to the **Command Platform** — so documentation and comparison content use several generations of names at once.

**Ownership & viability** — `public`, but **this is the section that matters**. In **June 2024** activist **Jana Partners** disclosed a significant stake and pushed for a sale, working with **Cannae Holdings** with the intent of teaming Cannae with a private-equity buyer. By **March 2025** Rapid7 was reported close to a **settlement adding three directors** to its eight-member board. FY2026 revenue guidance is **$836–842M** — a real business, but growing slowly in a market where growth is the whole valuation story, which is precisely why the activist is there. **No sale has been announced as of 2026-08-26.** A buyer at this level of pressure is a live possibility, and PE ownership of an incumbent security platform reliably means price increases and roadmap narrowing. `verify_after: 2027-02-26`.

**Positioning & differentiators** —
- **Bundle economics for the mid-market.** The genuine pitch: one vendor for VM + SIEM + MDR at a price a firm without a dedicated SOC can absorb. Buying [splunk](splunk.md) or [microsoft-sentinel](microsoft-sentinel.md) plus a separate VM tool plus a separate MDR provider costs more and takes more people.
- **MDR is the real product for most buyers.** Many customers are buying an outsourced SOC with tooling attached, not a SIEM they operate.
- **Weaker than the leaders on each individual axis.** InsightIDR is not competitive with [microsoft-sentinel](microsoft-sentinel.md) or [splunk](splunk.md) on scale or detection engineering depth; InsightVM faces Tenable and Qualys.
- **AI story is thin here.** Rapid7 has AI-assisted features, but nothing comparable to the agentic-SOC positions of [crowdstrike](crowdstrike.md) (Charlotte AI) or the dedicated vendors in [ai-soc-analysts](../categories/ai-soc-analysts.md). For an AI-governance stack, Rapid7 is baseline SecOps, not an AI capability.

**Who should choose them / anti-fit** — Fits a **mid-size firm with a small or no security team** that wants vulnerability management, log-based detection and a managed service from one vendor at a predictable price — a very common alternative-manager shape. **Anti-fit:** a firm already deep in Microsoft E5 (Sentinel + Defender is largely paid for) or one with a real detection-engineering team that will outgrow InsightIDR. Also anti-fit for anyone who cannot tolerate ownership uncertainty over a multi-year contract.

**Known weaknesses / gotchas** — Activist/sale overhang per above is the headline. Slow growth relative to the category. Product-naming churn makes evaluation confusing. Rapid7 also disclosed a breach of its own environment via the 2023 Progress/MOVEit-era wave and has had customer-facing incidents; standard diligence applies.

**Deployment & data handling** — SaaS platform with on-prem collectors; hybrid. **Log and vulnerability data leaves the tenancy** to Rapid7's cloud by design. Residency options and retention are **unverified**.

**Integrations & partnerships** — Broad connector and API surface; SOAR (InsightConnect) for workflow. MCP support unverified.

**Compliance & FS traction** — **Unverified.** Broad mid-market base including financial services is presumed; no named references confirmed.

**Commercial** — Public company with published packaging; pricing negotiated. Generally positioned below Splunk on cost.

## Open questions

- **Sale/take-private status** — the dominant item; recheck by 2027-02-26.
- Data residency options for log storage.
- Whether the Command Platform rebrand carries real consolidation or is naming only.
- Certifications held (FedRAMP status).
- Named FS customers at hedge-fund scale.

## Sources

- [Activist Jana has a stake in Rapid7 (CNBC, 2024-06-29)](https://www.cnbc.com/2024/06/29/two-paths-for-jana-to-bolster-shareholder-value-at-rapid7.html) — fetched 2026-08-26 — supports: activist stake, sale pressure, Cannae; confidence: medium
- [Jana Agitates for M&A at Rapid7 (The Deal)](https://www.thedeal.com/activism/jana-agitates-for-ma-at-rapid7/) — fetched 2026-08-26 — supports: settlement, board seats, revenue guidance; confidence: medium
- Cached: `raw/sources/2026-08-26--rapid7--activist-pressure-and-platform.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
