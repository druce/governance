---
title: Crogl
type: vendor
name: Crogl
slug: crogl
aka: []
primary_category: ai-soc-analysts
also_listed_in: []
website: https://www.crogl.com/
founded: null
hq: Albuquerque, NM, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; $30M total across two rounds — a $5M seed co-led by Tola Capital and Firestreak Ventures (with S3 Ventures and AV8 Ventures) and a $25M Series A led by Menlo Ventures announced 2025-03-06. Tim Tully of Menlo joined the board.
acquisition: {announced: null, closed: null, price: null}
funding_total: $30M
last_funding: Series A $25M led by Menlo Ventures, 2025-03-06
market_position: {ai-soc-analysts: ai-native-disruptor}
deployment_model: [saas]
form_factor: [platform, agent]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: null
tags: [ai-soc, alert-triage, knowledge-engine, agentic]
sources:
  - {claim: "$25M Series A led by Menlo Ventures announced 2025-03-06, following a $5M seed co-led by Tola Capital and Firestreak Ventures with S3 Ventures and AV8 Ventures; $30M total. Founders Monzy Merza (CEO, ex-Splunk/Databricks/Sandia) and David Dorsey (CTO)", url: "https://www.globenewswire.com/news-release/2025/03/06/3038257/0/en/founded-by-cybersecurity-researchers-and-practitioners-crogl-launches-with-its-breakthrough-knowledge-engine-to-combat-cyber-risk-and-announces-25-million-in-series-a-funding-led-b.html", date: 2026-08-26, confidence: high}
  - {claim: "Knowledge engine framing; early customers resolving thousands of daily alerts", url: "https://siliconangle.com/2025/03/06/crogl-raises-25m-launches-knowledge-engine-scale-enterprise-security/", date: 2026-08-26, confidence: medium}
---

# Crogl

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md).

**One-liner** — An AI SOC analyst built around a "knowledge engine": rather than scripting playbooks, it learns how a given SOC actually investigates and reproduces that reasoning across the daily alert volume.

**What it does** — Ingests the alert stream from existing detection tooling and investigates autonomously — pulling context from the surrounding estate, forming and testing hypotheses, and producing a verdict with its reasoning trail rather than an enriched alert handed back to a human. The differentiating framing is the **knowledge engine**: the system's model of the environment and of how this particular team investigates, accumulated over time, rather than a library of vendor-authored playbooks. The pitch is scale — early customers described as resolving thousands of daily alerts and freeing hundreds of analyst hours.

**Naming / provenance** — Launched publicly **2025-03-06**. Founded by **Monzy Merza** (CEO), previously at Splunk, Databricks and Sandia National Laboratory, and **David Dorsey** (CTO). Based in Albuquerque, NM — unusual for the category and worth noting only because it makes the company easy to confuse with nothing else.

**Ownership & viability** — `independent`, VC-backed. **$30M total**: a $5M seed co-led by Tola Capital and Firestreak Ventures, then a **$25M Series A led by Menlo Ventures** announced 2025-03-06, with **Tim Tully** (formerly Splunk CTO) joining the board. Early-stage. In a category with at least nine credible competitors on this wiki alone, consolidation is near-certain and most entrants will not survive as independents.

**Positioning & differentiators** —
- **Founder credibility is the strongest signal.** Merza ran security markets at Splunk and Databricks; Tully was Splunk's CTO. This is a team that has seen the alert-volume problem from the data-platform side, which is where it actually originates.
- **Learned investigation vs authored playbooks.** The claim against [torq](torq.md) and classic SOAR — and against playbook-driven AI SOC entrants — is that the knowledge is derived from the environment rather than written down in advance.
- **Not a SIEM.** Unlike [artemis-security](artemis-security.md), Crogl does not bundle a data layer; it sits on top of whatever detection stack exists.
- **Everything above is company-published.** No independent evaluation of investigation quality was found, which is true of essentially every vendor in this category.

**Who should choose them / anti-fit** — Fits a firm with a **real alert volume and a SOC too small to work it** — but only one comfortable running an early-stage vendor inside the detection workflow. **Anti-fit:** an alternative manager with a modest alert volume and an MDR provider; the honest comparison there is "does our MDR do this?", not "which AI SOC vendor?". Also anti-fit for any firm whose vendor-diligence floor excludes Series-A companies.

**Known weaknesses / gotchas** — Early-stage across the board: small customer count, no independent benchmarks, no certifications confirmed. The category itself is unproven — autonomous investigation quality is very hard to evaluate in a POC, and the failure mode (a confidently wrong verdict that closes a real incident) is severe. Ask specifically how it handles the alerts it gets wrong.

**Deployment & data handling** — SaaS. **Unverified** and important: an AI SOC analyst reads security telemetry, which is among the most sensitive data a firm holds. Where inference runs, what is retained, and whether customer data trains shared models are the three questions to ask.

**Integrations & partnerships** — Connects to existing SIEM/EDR/detection tooling; specific list unverified. MCP support unverified.

**Compliance & FS traction** — **Unverified.** No named customers or certifications confirmed.

**Commercial** — Not public.

## Open questions

- Where inference runs; retention; whether customer telemetry trains shared models.
- Named customers and any independent evaluation of investigation accuracy.
- Certifications held (SOC 2 at minimum).
- Any funding since the March 2025 Series A.
- How it handles and surfaces low-confidence verdicts.

## Sources

- [Crogl launches with knowledge engine and $25M Series A (GlobeNewswire, 2025-03-06)](https://www.globenewswire.com/news-release/2025/03/06/3038257/0/en/founded-by-cybersecurity-researchers-and-practitioners-crogl-launches-with-its-breakthrough-knowledge-engine-to-combat-cyber-risk-and-announces-25-million-in-series-a-funding-led-b.html) — fetched 2026-08-26 — supports: funding, investors, founders; confidence: high
- [Crogl raises $25M and launches knowledge engine (SiliconANGLE)](https://siliconangle.com/2025/03/06/crogl-raises-25m-launches-knowledge-engine-scale-enterprise-security/) — fetched 2026-08-26 — supports: product framing, early traction claims; confidence: medium
- Cached: `raw/sources/2026-08-26--crogl--launch-and-series-a.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
