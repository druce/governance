---
title: DNSFilter
type: vendor
name: DNSFilter
slug: dnsfilter
aka: [DNS Filter]
primary_category: network-security-sase
also_listed_in: []
website: https://www.dnsfilter.com/
founded: 2015
hq: Washington, DC, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; nearly $62M raised, including two rounds led by Insight Partners — a $30M Series A (July 2021) and a $15M Series A extension (August 2023). No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$62M
last_funding: Series A extension $15M from Insight Partners, 2023-08
market_position: {network-security-sase: niche-specialist}
deployment_model: [saas]
form_factor: [agent, api]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: smb to mid-market (heavy MSP channel)
last_verified: 2026-08-26
verify_after: null
tags: [protective-dns, dns-filtering, content-filtering, msp, lightweight]
sources:
  - {claim: "Nearly $62M raised including two Insight Partners-led rounds; $15M Series A extension announced August 2023", url: "https://www.dnsfilter.com/newsroom/dnsfilter-raises-another-15-million-in-series-a-extension-from-insight-partners", date: 2026-08-26, confidence: high}
  - {claim: "$30M Series A led by Insight Partners, July 2021; protects 27M+ end users across ~30,000 organisations; AI scanning of billions of domains daily", url: "https://www.insightpartners.com/ideas/dnsfilter-raises-30m-in-funding-to-fight-growing-number-of-dns-based-security-threats/", date: 2026-08-26, confidence: medium}
  - {claim: "June 2026 expansion of the MSP Partner Program", url: "https://www.businesswire.com/news/home/20260630616164/en/DNSFilter-Launches-New-MSP-Partner-Program-Turning-Security-Squeeze-Into-a-Growth-Opportunity-for-its-Partners", date: 2026-08-26, confidence: high}
---

# DNSFilter

> Primary category: [network-security-sase](../categories/network-security-sase.md). **Scope caveat:** this is protective DNS, not an SSE — see below.

**One-liner** — AI-driven protective DNS and content filtering: blocks resolution of malicious and policy-violating domains before a connection is made, deployed in minutes with no proxy and no TLS interception.

**What it does** — Sits at the DNS layer. Every domain lookup from a device or network is resolved through DNSFilter, which classifies the domain in real time — the company's pitch is proprietary AI scanning billions of domains daily to catch newly-registered malicious, phishing and malware infrastructure faster than list-based feeds — and either resolves or blocks it. Also does category-based content filtering (the traditional web-filtering use case) and reporting.

**Why it appears in an AI-governance list.** DNS blocking is the **cheapest possible control on shadow AI**: it can stop resolution of unsanctioned AI services outright for the whole estate in an afternoon. What it cannot do is anything finer than that — see the caveat below.

**Naming / provenance** — Founded 2015, headquartered in Washington, DC. Single brand.

**Ownership & viability** — `independent`, VC-backed, **~$62M raised** with two rounds led by **Insight Partners**: a **$30M Series A (July 2021)** and a **$15M extension (August 2023)**. Reports 150+ employees and claims protection of 27M+ end users across roughly 30,000 organisations, largely via a substantial MSP channel — expanded again with a new partner programme in **June 2026**. No round since 2023; the MSP channel gives it a durable revenue base but caps enterprise ambition.

**Positioning & differentiators** —
- **Deploys in minutes.** Point DNS at DNSFilter and it works. Nothing else in this category is remotely as fast to stand up.
- **No TLS interception.** For a firm unwilling to decrypt traffic, DNS-layer blocking is the control that requires no man-in-the-middle. That is also its ceiling.
- **MSP-first distribution.** Most of its base arrives through managed service providers — relevant to a small manager whose IT is outsourced, since the MSP may already resell it.
- **Competes with Cisco Umbrella, not Zscaler.** The honest comparison set is Cisco Umbrella, Cloudflare Gateway's DNS tier, and Quad9 — not the SSE platforms.

**Who should choose them / anti-fit** — Fits a **small firm or an MSP-managed shop** wanting a fast, cheap, blunt control over malicious domains and unsanctioned services, or a larger firm wanting DNS as one layer among several. **Anti-fit:** any firm that believes DNS filtering constitutes AI-traffic governance. It does not.

**Known weaknesses / gotchas — read this before listing it as an SSE.** DNS filtering is **all-or-nothing per domain**. It can block `chatgpt.com` entirely; it cannot allow the sanctioned enterprise tenant while blocking the consumer one, cannot inspect prompt content, cannot apply DLP, and cannot distinguish an approved use from a prohibited one on the same domain — because it never sees the payload. It is also trivially bypassed by DNS-over-HTTPS, a VPN, or a hardcoded resolver unless separately blocked. Filing it alongside [zscaler](zscaler.md) and [netskope](netskope.md) in a survey question risks respondents reporting it as equivalent coverage when it is a much weaker control.

**Deployment & data handling** — SaaS resolver, with a roaming client agent for off-network devices. **DNS query data does leave the tenancy** — that is inherent to the model, and query logs are a sensitive dataset (they reveal every service a firm touches). Retention terms and residency are **unverified** and worth asking about.

**Integrations & partnerships** — Directory integration for per-user policy, SIEM log export, RMM/PSA tooling for the MSP channel. Detail unverified.

**Compliance & FS traction** — **Unverified.** Base skews SMB and MSP-served; no financial-services references confirmed.

**Commercial** — Per-seat subscription with published tiers; among the cheapest controls in this wiki.

## Open questions

- DNS query-log retention, residency and secondary use — the main data-handling question.
- Whether any funding has occurred since the 2023 extension.
- Certifications held.
- How it handles DoH/DoT bypass in practice.
- Whether it should be cross-listed to a shadow-AI/discovery category rather than sitting beside full SSE platforms.

## Sources

- [DNSFilter Raises Another $15 Million in Series A Extension from Insight Partners (DNSFilter)](https://www.dnsfilter.com/newsroom/dnsfilter-raises-another-15-million-in-series-a-extension-from-insight-partners) — fetched 2026-08-26 — supports: funding total and round; confidence: high (primary)
- [DNSFilter Raises $30M (Insight Partners)](https://www.insightpartners.com/ideas/dnsfilter-raises-30m-in-funding-to-fight-growing-number-of-dns-based-security-threats/) — fetched 2026-08-26 — supports: Series A, scale claims; confidence: medium
- [DNSFilter Launches New MSP Partner Program (BusinessWire, 2026-06-30)](https://www.businesswire.com/news/home/20260630616164/en/DNSFilter-Launches-New-MSP-Partner-Program-Turning-Security-Squeeze-Into-a-Growth-Opportunity-for-its-Partners) — fetched 2026-08-26 — supports: MSP channel emphasis, currency; confidence: high
- Cached: `raw/sources/2026-08-26--dnsfilter--funding-and-scope.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
