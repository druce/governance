---
title: Sekoia.io
type: vendor
name: Sekoia.io
slug: sekoia
aka: [SEKOIA.IO, Sekoia]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: https://www.sekoia.io/
founded: 2016
hq: Paris / Bretagne, France
ownership_state: independent
owner: null
ownership_note: VC-backed, European. €60M raised in total since founding. €26M Series B announced 2025-04-09 from Revaia with UNEXO, plus existing investors Bright Pixel Capital, Omnes Capital and Bpifrance.
acquisition: {announced: null, closed: null, price: null}
funding_total: €60M
last_funding: Series B €26M led by Revaia, 2025-04-09
market_position: {ai-soc-analysts: challenger}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market to enterprise, heavy MSSP channel
last_verified: 2026-08-26
verify_after: null
tags: [xdr, siem, threat-intelligence, european, eu-sovereignty, mssp]
sources:
  - {claim: "€26M Series B announced 2025-04-09 from Revaia with UNEXO and existing investors Bright Pixel Capital, Omnes Capital and Bpifrance; brings total to €60M since founding", url: "https://www.sekoia.io/en/presse/sekoia-io-secures-e26-million-in-series-b-to-democratize-cyber-operations-with-ai-and-cyber-intelligence/", date: 2026-08-26, confidence: high}
  - {claim: "Operations in four European countries, 100+ employees, ~50 MSSP partners; clients include EDF, Vinci, SNCF, Mirakl, Marlink and the French Ministry of Armed Forces; launched the Open XDR Platform in late 2021", url: "https://techfundingnews.com/paris-based-sekoia-io-scoops-e26m-to-scale-ai-powered-threat-detection-and-cyber-intelligence/", date: 2026-08-26, confidence: medium}
---

# Sekoia.io

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A European AI-native SOC platform pairing detection and response with its own threat-intelligence production — the sovereignty option for a firm that will not put security telemetry in a US-owned cloud.

**What it does** — A unified SOC platform combining **XDR** (detection and response across endpoint, network, cloud and identity telemetry) with a **continuously produced threat-intelligence feed** that Sekoia generates in-house rather than licensing. The company's positioning is that detection content and intelligence should come from the same place, so detections are driven by tracked adversary infrastructure rather than generic rules. It launched an **Open XDR Platform** in late 2021 as a multi-vendor offering, and now describes its ambition as the leading **AI-native security platform for managed SOCs** — the MSSP channel is central, with roughly fifty partners.

**Naming / provenance** — Founded 2016 in France; the brand is `Sekoia.io` including the TLD. Not related to the Sequoia venture firm despite the phonetic collision — a real search hazard.

**Ownership & viability** — `independent`, European VC-backed, **€60M raised since founding**. The **€26M Series B closed 2025-04-09**, led by **Revaia** with UNEXO and existing backers including **Bpifrance** — the French state investment bank, which is a meaningful signal about the company's sovereignty positioning and its likely persistence. 100+ employees across four European countries. Named clients are substantial and public-sector-weighted: **EDF, Vinci, SNCF, Mirakl, Marlink, and the French Ministry of Armed Forces**.

**Positioning & differentiators** —
- **European data sovereignty is the actual differentiator**, and it is a real one. Every other vendor in [ai-soc-analysts](../categories/ai-soc-analysts.md) on this wiki is US-owned. For a manager with EU-regulated entities, DORA obligations, or a policy against US CLOUD Act exposure for security telemetry, Sekoia is the option that exists.
- **First-party threat intelligence.** Most detection vendors license intelligence; Sekoia produces it. Whether that materially improves detection is unverified, but it is a structural difference.
- **MSSP-first.** A large share of consumption is through partners — so the practical question for many buyers is whether their provider runs it.
- **Smaller than the US field.** €60M against competitors with several times that; expect thinner integration coverage and less product breadth than [crowdstrike](crowdstrike.md) or [palo-alto-networks](palo-alto-networks.md).

**Who should choose them / anti-fit** — Fits a firm with **European entities and a sovereignty or DORA-driven requirement** on where security telemetry rests, particularly one served by a European MSSP. **Anti-fit:** a US-only manager with no sovereignty constraint — the US field is deeper and the reference base more familiar. Also anti-fit for a firm needing the widest possible third-party integration coverage.

**Known weaknesses / gotchas** — Limited US presence and reference base; support-hours and account-coverage questions are real for a US buyer. Named customers are heavily French and public-sector, so financial-services fit is unproven from public evidence. The company markets itself both as XDR and as an AI SOC platform, and the boundary between those claims and the MSSP's own work is worth pinning down in a specific deal.

**Deployment & data handling** — SaaS. **Telemetry leaves the tenancy**, but the sovereignty pitch is about *where it lands*. Confirm the actual hosting region, legal entity and sub-processor list in writing — that is the entire reason to consider this vendor, and it is the one thing not to take on trust.

**Integrations & partnerships** — Open XDR approach with multi-vendor telemetry ingestion; ~50 MSSP partners including Orange Cyberdefense-scale providers. Specific integration list unverified. MCP support unverified.

**Compliance & FS traction** — **Unverified for financial services.** Public-sector and large-enterprise French references are strong; no FS names confirmed. French/EU certifications (e.g. ANSSI qualification) are plausible but **not confirmed here** — worth checking, as they would be the strongest evidence for the sovereignty case.

**Commercial** — Not public. Often consumed through an MSSP rather than bought directly.

## Open questions

- **Hosting region, legal entity and sub-processors** — the decisive diligence item.
- Any ANSSI qualification or EU-specific certification held.
- Financial-services customers; any hedge-fund or asset-manager references.
- US support coverage and account management.
- How much of the "AI-native SOC" capability is Sekoia's product versus the MSSP's operation.

## Sources

- [Sekoia.io Secures €26 Million in Series B (Sekoia.io)](https://www.sekoia.io/en/presse/sekoia-io-secures-e26-million-in-series-b-to-democratize-cyber-operations-with-ai-and-cyber-intelligence/) — fetched 2026-08-26 — supports: round size, date, investors, total raised; confidence: high (primary)
- [Paris-based Sekoia.io scoops €26M (Tech Funding News)](https://techfundingnews.com/paris-based-sekoia-io-scoops-e26m-to-scale-ai-powered-threat-detection-and-cyber-intelligence/) — fetched 2026-08-26 — supports: headcount, geography, MSSP partners, named clients, Open XDR; confidence: medium
- Cached: `raw/sources/2026-08-26--sekoia--series-b-and-european-positioning.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
