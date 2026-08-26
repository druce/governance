---
title: Fortinet
type: vendor
name: Fortinet
slug: fortinet
aka: [FortiGate, FortiSASE, FortiOS]
primary_category: network-security-sase
also_listed_in: [edr-xdr, siem-soc]
website: https://www.fortinet.com/
founded: 2000
hq: Sunnyvale, CA, USA
ownership_state: public
owner: null
ownership_note: NASDAQ:FTNT. Q2 2026 revenue $2,047.9M with net income $606.3M; FY2026 guidance $8.02–8.18B revenue.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {network-security-sase: legacy-incumbent}
deployment_model: [saas, on-prem, hybrid]
form_factor: [inline-proxy, platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise and mid-market
last_verified: 2026-08-26
verify_after: null
tags: [sase, sse, firewall, sd-wan, ngfw, incumbent, public]
sources:
  - {claim: "Q2 2026 revenue $2,047.9M, net income $606.3M; FY2026 guidance $8.020–8.180B revenue, $9.35–9.55B billings", url: "https://investor.fortinet.com/news-releases/news-release-details/fortinet-reports-strong-second-quarter-2026-financial-results", date: 2026-08-26, confidence: high}
  - {claim: "Launched FortiGate 1200G with FortiSASE Outpost, FortiSOC AI SOC platform and expanded FortiEndpoint; AI collaborations announced with Intel, Anthropic, OpenAI and NVIDIA", url: "https://www.globenewswire.com/news-release/2026/07/29/3335555/0/en/Fortinet-Reports-Strong-Second-Quarter-2026-Financial-Results.html", date: 2026-08-26, confidence: high}
---

# Fortinet

> Primary category: [network-security-sase](../categories/network-security-sase.md). Also listed in [edr-xdr](../categories/edr-xdr.md) and [siem-soc](../categories/siem-soc.md).

**One-liner** — The appliance-rooted network-security incumbent: FortiGate firewalls, FortiOS and custom ASICs extended into a SASE/SSE service — the vendor most likely to already own the egress path at a mid-size firm that never bought a cloud-first SSE.

**What it does** — Fortinet's centre of gravity is the **FortiGate next-generation firewall**, running **FortiOS** on purpose-built **FortiASIC** silicon. Everything else attaches to that: SD-WAN, **FortiSASE** (the cloud-delivered secure service edge — SWG, CASB, ZTNA, and the TLS inspection that makes any of it work), FortiEndpoint (EDR), FortiSOC/FortiSIEM (security operations), and a long tail of Forti-branded products. The strategic pitch it makes against [zscaler](zscaler.md) and [netskope](netskope.md) is the "SASE Firewall": one operating system and one policy model spanning the on-prem appliance and the cloud edge, rather than a cloud-only service bolted alongside whatever firewall you already run.

**Why it matters to an AI-governance stack.** Fortinet's relevance here is almost entirely about **egress**. Traffic to ChatGPT, Claude, Copilot and every unsanctioned AI SaaS leaves through this box. Whether the firm can see, classify, and control that traffic — and whether it terminates TLS to do so — is decided by whatever sits on this path. Fortinet is not an AI-security vendor; it is where AI-related egress control gets enforced by default in a large number of mid-size financial firms, which is why its absence from this wiki was a genuine gap. 2026 product motion adds an explicit AI layer: **FortiSOC**, an AI SOC platform (see [ai-soc-analysts](../categories/ai-soc-analysts.md)), and announced AI collaborations with Intel, **Anthropic**, **OpenAI** and NVIDIA.

**Naming / provenance** — Founded 2000 in Sunnyvale by brothers Ken and Michael Xie. IPO 2009 (NASDAQ: **FTNT**). Product naming is uniformly `Forti-` prefixed, which is consistent but makes the portfolio hard to navigate.

**Ownership & viability** — `public`, NASDAQ-listed, and financially strong: **Q2 2026 revenue of $2,047.9M with net income of $606.3M**, and FY2026 guidance of **$8.02–8.18B** revenue on $9.35–9.55B billings. No viability question. The relevant risk is architectural lock-in, not solvency.

**Positioning & differentiators** —
- **Price-performance from custom silicon.** The FortiASIC story is real and is why Fortinet wins on throughput-per-dollar against software-only firewalls — the reason it dominates mid-market and branch deployments.
- **Single-OS convergence.** One policy model across appliance and cloud edge is a genuine operational advantage over stitching [zscaler](zscaler.md) onto an incumbent firewall — and a genuine lock-in mechanism.
- **Breadth over depth.** Fortinet sells nearly every security category. Individual products are rarely the category leader; the bundle economics usually win. FortiEndpoint against [crowdstrike](crowdstrike.md) is the clearest example.
- **Appliance heritage cuts both ways.** [zscaler](zscaler.md) and [netskope](netskope.md) were built cloud-first for a remote workforce; Fortinet arrived there from the datacentre. For a firm with real offices, trading floors and colo footprints — most alternative managers — that heritage is an advantage, not a liability.

**Who should choose them / anti-fit** — Fits a firm with **physical sites, colo/datacentre presence and cost sensitivity**, that wants one vendor across firewall, SD-WAN and SSE. **Anti-fit:** a fully remote, cloud-only firm with no datacentre — the appliance economics are wasted and a cloud-native SSE is cleaner; and any firm deliberately avoiding single-vendor concentration in the security stack.

**Known weaknesses / gotchas** — Best-of-breed depth is weaker than specialists in most individual categories. FortiOS has a **significant history of exploited vulnerabilities in internet-facing management interfaces**, repeatedly appearing in CISA's Known Exploited Vulnerabilities catalog — patch discipline on FortiGate is not optional, and this is the single most important operational caveat on this page. Licensing across the Forti- portfolio is complex.

**Deployment & data handling** — On-prem appliances, virtual appliances, and cloud-delivered FortiSASE; hybrid is the intended shape. For FortiSASE, where inspected traffic is decrypted and what is logged/retained is **unverified** and is the diligence question that matters — TLS inspection of AI traffic means the vendor's cloud sees prompt content.

**Integrations & partnerships** — Fortinet Security Fabric is the internal integration model; broad third-party ecosystem. 2026 AI partnerships with Intel, Anthropic, OpenAI, NVIDIA announced. MCP support unverified.

**Compliance & FS traction** — **Unverified** here in specifics, though Fortinet is widely deployed across financial services. Certifications (FIPS, Common Criteria on appliances) are claimed by product line; not confirmed here.

**Commercial** — Public list pricing exists for hardware; enterprise licensing is negotiated. Generally positioned below [palo-alto-networks](palo-alto-networks.md) on price.

## Open questions

- FortiSASE data handling: where TLS termination occurs, what prompt content is logged, retention, and regional residency options.
- What the Anthropic/OpenAI collaborations actually deliver in product terms.
- FortiSOC's AI-SOC capability versus the dedicated vendors in [ai-soc-analysts](../categories/ai-soc-analysts.md).
- Whether FortiSASE does meaningful AI-application classification (distinguishing sanctioned from shadow AI) or only generic URL/SaaS categorisation.
- Named FS references at hedge-fund scale.

## Sources

- [Fortinet Reports Strong Second Quarter 2026 Financial Results (Fortinet IR)](https://investor.fortinet.com/news-releases/news-release-details/fortinet-reports-strong-second-quarter-2026-financial-results) — fetched 2026-08-26 — supports: Q2 2026 revenue and net income, FY2026 guidance; confidence: high (primary)
- [Q2 2026 results (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/07/29/3335555/0/en/Fortinet-Reports-Strong-Second-Quarter-2026-Financial-Results.html) — fetched 2026-08-26 — supports: FortiSASE Outpost, FortiSOC, AI partnerships; confidence: high
- Cached: `raw/sources/2026-08-26--fortinet--q2-2026-results-and-ai-products.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier B, score 7, flagged there as "a genuine category gap"); promoted to inclusion because Fortinet frequently owns the egress path at mid-size financial firms.
