---
title: D3 Security
type: vendor
name: D3 Security
slug: d3-security
aka: [D3, Morpheus, Smart SOAR]
primary_category: ai-soc-analysts
also_listed_in: [siem-soc]
website: https://d3security.com/
founded: 2002
hq: Vancouver, BC, Canada
ownership_state: independent
owner: null
ownership_note: Privately held; no disclosed institutional funding rounds found as of 2026-08-26. Long-established SOAR vendor that self-funded through the SOAR era.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {ai-soc-analysts: challenger}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise and MSSP
last_verified: 2026-08-26
verify_after: null
tags: [soar, ai-soc, agentic, mssp, self-hostable]
sources:
  - {claim: "Morpheus is an agentic SOC platform built from scratch over two years by a team of 60; claims investigation of up to 95% of alerts in under 2 minutes at L2+ depth across 800+ self-healing integrations; 'Unified Intelligence Model' with a purpose-built cybersecurity LLM producing one audit trail per incident", url: "https://d3security.com/", date: 2026-08-26, confidence: low}
  - {claim: "D3 Security unveiled Morpheus, its AI-powered autonomous SOC", url: "https://www.msspalert.com/news/d3-security-unveils-morpheus-its-ai-powered-autonomous-soc", date: 2026-08-26, confidence: medium}
---

# D3 Security

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [siem-soc](../categories/siem-soc.md).

**One-liner** — A long-established SOAR vendor that rebuilt itself as an agentic SOC platform (Morpheus) — the incumbent-turned-AI-native case in a category otherwise made of 2023-vintage startups.

**What it does** — Two generations of product in one company. The original **Smart SOAR** is classic security orchestration, automation and response: codified playbooks, case management, and a very large integration library. **Morpheus**, the current flagship, is the agentic rewrite: rather than executing predefined steps, it runs the investigation to a verdict and drafts the remediation. D3's stated architecture is a **Unified Intelligence Model** — one purpose-built security LLM carrying the whole investigation in a single reasoning context, producing one audit trail per incident rather than a chain of separate tool calls.

**Naming / provenance** — Founded 2002 in Vancouver — by two decades the oldest company in this category. Expect three names in the wild: D3 Security (company), Smart SOAR (legacy product), Morpheus (current).

**Ownership & viability** — `independent`, privately held, with **no disclosed institutional funding rounds found**. That is unusual and cuts both ways: a company that reached this scale without venture money has no investor-driven exit clock and is probably profitable, but it also has no public financial evidence to diligence and less capital to outspend the funded entrants. Note that the "team of 60 over two years" figure for Morpheus is the company's own.

**Positioning & differentiators** —
- **Integration depth is the real moat.** 800+ integrations accumulated over two decades of SOAR work, described as self-healing. The AI-native startups in this category are building that library from zero, and integration breadth is what actually determines whether an autonomous investigation can reach the evidence it needs.
- **Both halves of the job.** Investigation *and* execution. Several competitors investigate and hand back a verdict; D3 retains the SOAR execution engine underneath, so it can act.
- **Self-hosted and on-prem are available** — rare in this category and directly relevant to a firm unwilling to route security telemetry to a vendor cloud.
- **Strong MSSP channel**, which matters if your provider already runs it.
- **Marketing is aggressive.** Its site publishes competitive comparison pages targeting Splunk SOAR and CrowdStrike Charlotte AI by name, and the "95% of alerts in under 2 minutes" figure is self-reported. Treat as claims.

**Who should choose them / anti-fit** — Fits a firm that **already has SOAR ambitions and a wide tool estate**, or one that needs the platform self-hosted. Also fits where an MSSP already runs it. **Anti-fit:** a small manager with modest alert volume that has no SOC to automate — the honest answer there is MDR, not a SOAR platform. Also anti-fit if you want a purely SaaS, zero-maintenance product.

**Known weaknesses / gotchas** — SOAR's historical failure mode is playbook maintenance burden; D3's argument is that Morpheus removes it, which is exactly the claim to test in a POC rather than accept. No disclosed funding means limited public financial visibility. No independent evaluation of Morpheus's investigation quality was found.

**Deployment & data handling** — SaaS, self-hosted and on-prem. Where the "purpose-built cybersecurity LLM" runs under each deployment — and in particular whether the self-hosted option includes local inference or still calls out — is **unverified and is the key question** for a firm choosing self-hosting for data-control reasons.

**Integrations & partnerships** — 800+ claimed integrations across SIEM, EDR, identity, ticketing and cloud; the largest library of any vendor in this category. MCP support unverified.

**Compliance & FS traction** — **Unverified.** No named financial-services references confirmed; certifications not confirmed.

**Commercial** — Not public. Markets itself explicitly on price against Splunk SOAR.

## Open questions

- **Does the self-hosted deployment run inference locally, or call an external model?** Decisive for the data-control use case.
- Company financials/ownership — is it genuinely bootstrapped?
- Independent evaluation of Morpheus investigation accuracy.
- Certifications held; named FS customers.
- Migration path and cost from Smart SOAR to Morpheus for existing customers.

## Sources

- [Morpheus by D3 Security (vendor site)](https://d3security.com/) — fetched 2026-08-26 — supports: architecture, integration count, performance claims; confidence: low (vendor marketing)
- [D3 Security Unveils Morpheus, its AI-Powered Autonomous SOC (MSSP Alert)](https://www.msspalert.com/news/d3-security-unveils-morpheus-its-ai-powered-autonomous-soc) — fetched 2026-08-26 — supports: product launch, positioning; confidence: medium
- Cached: `raw/sources/2026-08-26--d3-security--morpheus-agentic-soc.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
