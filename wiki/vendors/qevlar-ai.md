---
title: Qevlar AI
type: vendor
name: Qevlar AI
slug: qevlar-ai
aka: [Qevlar]
primary_category: ai-soc-analysts
also_listed_in: []
website: https://www.qevlar.com/
founded: 2023
hq: Paris, France
ownership_state: independent
owner: null
ownership_note: VC-backed. $30M (€25.8M) Series A announced 2026-03-10, co-led by Partech and Forgepoint Capital International with EQT Ventures participating. Follows a €9.1M round in April 2025 led by EQT Ventures and Forgepoint (total commitments then €12.8M).
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$45M equivalent (€12.8M pre-Series A + $30M Series A)
last_funding: Series A $30M co-led by Partech and Forgepoint Capital International, 2026-03-10
market_position: {ai-soc-analysts: ai-native-disruptor}
deployment_model: [saas]
form_factor: [platform, agent]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise and MSSP
last_verified: 2026-08-26
verify_after: null
tags: [ai-soc, agentic, alert-investigation, vulnerability-operations, european]
sources:
  - {claim: "$30M raised 2026-03-10, co-led by Partech and Forgepoint Capital International with EQT Ventures participating; founded 2023; customers include Mercedes-Benz, Sodexo, Orange Cyberdefense, ECI and Atos; reported 10x reduction in investigation time to ~3 minutes", url: "https://www.businesswire.com/news/home/20260310058427/en/Qevlar-AI-Raises-$30M-to-Shift-Security-Operations-From-Alert-Firefighting-to-Organization-Level-Security-Insights", date: 2026-08-26, confidence: high}
  - {claim: "April 2025 round of €9.1M led by EQT Ventures and Forgepoint Capital International brought total commitments to €12.8M", url: "https://www.eu-startups.com/2026/03/paris-based-qevlar-ai-raises-e25-8-million-to-automate-security-operations-centre-investigations-with-agentic-ai/", date: 2026-08-26, confidence: medium}
  - {claim: "May 2026: AI agents unifying SOC and vulnerability operations", url: "https://www.businesswire.com/news/home/20260521075567/en/Qevlar-Introduces-AI-Agents-Unifying-SOC-and-Vulnerability-Operations-as-Exploitation-Windows-Collapse", date: 2026-08-26, confidence: high}
---

# Qevlar AI

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md).

**One-liner** — An agentic AI SOC platform that autonomously enriches, correlates and investigates security alerts to a verdict — the best-funded and most enterprise-referenced of the European entrants, and now extending the same agents into vulnerability operations.

**What it does** — Takes the alert stream and runs the investigation without a human in the loop: enriching signals from surrounding systems, correlating across sources, and producing an investigation conclusion. The company's headline claim is a **10x reduction in investigation time, down to roughly three minutes**, reported by Fortune 500 customers and MSSPs. The **2026 product direction is convergence**: in May 2026 it introduced agents unifying **SOC and vulnerability operations**, on the argument that as the window between disclosure and exploitation collapses, deciding which vulnerabilities matter is the same reasoning problem as deciding which alerts matter. That is a genuinely distinct bet from the pure alert-triage framing of [dropzone-ai](dropzone-ai.md), [prophet-security](prophet-security.md) or [crogl](crogl.md).

**Naming / provenance** — Founded **2023** in Paris. Single brand; appears as both "Qevlar" and "Qevlar AI".

**Ownership & viability** — `independent`, VC-backed and well capitalised for its age. A **€9.1M round in April 2025** led by **EQT Ventures** and **Forgepoint Capital International** (total commitments then €12.8M), followed by a **$30M (€25.8M) round announced 2026-03-10** co-led by **Partech** and **Forgepoint**, with EQT Ventures following on. Existing investors doubling down inside twelve months is a positive signal. Still an early-stage company in a crowded category that will consolidate.

**Positioning & differentiators** —
- **The customer list is unusually strong for the stage** — **Mercedes-Benz** and **Sodexo** as enterprises, and **Orange Cyberdefense, ECI and Atos** as MSSPs. In a category where almost every vendor's evidence is a self-published metric, named large-enterprise and MSSP logos are the most useful signal available.
- **MSSP distribution.** Selling through Orange Cyberdefense and Atos gets the product into European enterprises without a direct sales motion — and means a European manager may encounter it through a provider rather than a procurement.
- **SOC + vulnerability convergence** is a real differentiator versus the alert-triage-only field.
- **European, but less explicitly sovereignty-positioned than [sekoia](sekoia.md).** Paris-based with European investors; whether it offers EU-only data handling is unverified below.

**Who should choose them / anti-fit** — Fits a firm with **genuine alert volume and a European MSSP relationship**, or one wanting SOC triage and vulnerability prioritisation from the same system. **Anti-fit:** a small manager whose entire security operation is outsourced and whose alert volume does not justify a platform — and any firm unwilling to let an autonomous system close investigations.

**Known weaknesses / gotchas** — Founded 2023; short track record. All performance figures are company-reported with no independent evaluation found. The category's core risk applies fully here: an autonomous investigation that confidently reaches the wrong verdict on a real incident is worse than no automation, and this is very difficult to assess in a short POC. Ask how low-confidence cases are surfaced and escalated.

**Deployment & data handling** — SaaS. **Unverified and material**: where inference runs, whether EU-only processing is available, retention of investigated telemetry, and whether customer data trains shared models. Given the European customer base these should all have clear answers — get them in writing.

**Integrations & partnerships** — Ingests from existing SIEM/EDR/detection stacks; MSSP partnerships with Orange Cyberdefense, ECI and Atos. Specific integration list unverified. MCP support unverified.

**Compliance & FS traction** — **Unverified.** Named customers are automotive, food services and MSSPs; no financial-services references confirmed. Certifications not confirmed.

**Commercial** — Not public. Often reached through an MSSP.

## Open questions

- EU-only data processing availability; where inference runs; training use of customer telemetry.
- Certifications held (SOC 2, ISO 27001).
- Any financial-services customers.
- Independent evaluation of investigation accuracy, and the false-verdict rate.
- How the vulnerability-operations agents overlap with an existing VM tool such as [rapid7](rapid7.md).

## Sources

- [Qevlar AI Raises $30M (BusinessWire, 2026-03-10)](https://www.businesswire.com/news/home/20260310058427/en/Qevlar-AI-Raises-$30M-to-Shift-Security-Operations-From-Alert-Firefighting-to-Organization-Level-Security-Insights) — fetched 2026-08-26 — supports: round, investors, customers, performance claims; confidence: high (primary)
- [Paris-based Qevlar AI raises €25.8 million (EU-Startups)](https://www.eu-startups.com/2026/03/paris-based-qevlar-ai-raises-e25-8-million-to-automate-security-operations-centre-investigations-with-agentic-ai/) — fetched 2026-08-26 — supports: earlier round, founding year; confidence: medium
- [Qevlar Introduces AI Agents Unifying SOC and Vulnerability Operations (BusinessWire, 2026-05-21)](https://www.businesswire.com/news/home/20260521075567/en/Qevlar-Introduces-AI-Agents-Unifying-SOC-and-Vulnerability-Operations-as-Exploitation-Windows-Collapse) — fetched 2026-08-26 — supports: 2026 product direction; confidence: high
- Cached: `raw/sources/2026-08-26--qevlar-ai--funding-and-product-direction.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
