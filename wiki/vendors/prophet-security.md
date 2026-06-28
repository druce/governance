---
type: vendor
name: Prophet Security
slug: prophet-security
categories: [ai-soc-analysts]
layer: foundation
aliases: []
website: https://www.prophetsecurity.ai
founded: 2023
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: VC-backed; $30M Series A led by Accel (2025-07), plus strategic investments from Amex Ventures and Citi Ventures.
ownership_confidence: high
funding_total: ~$41M
last_funding: Series A $30M (2025-07, Accel)
deployment: [saas, api]
target_customer: enterprise SOC teams (also mid-market)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [agentic-soc, ai-soc, alert-triage]
---

# Prophet Security

**One-liner** — An agentic "AI SOC analyst" that autonomously triages and investigates security alerts and writes up findings in plain language, so human analysts stop drowning in Tier-1 noise.

**What it does** — Prophet's Agentic AI SOC Platform connects to your existing detection stack (SIEM, EDR, cloud, identity) and, when an alert fires, autonomously gathers evidence, builds an investigation, correlates across systems, and delivers a verdict with reasoning a human can audit. It ships three components: the **AI SOC Analyst** (alert investigation), an **AI Threat Hunter** (proactive pattern-finding), and an **AI Detection Advisor** (tunes detection coverage / reduces false positives from telemetry). The pitch is reducing mean-time-to-respond and analyst burnout, not replacing the SIEM.

**Where it sits in the stack** — [ai-soc-analysts](../categories/ai-soc-analysts.md) in the Foundation layer; it sits on top of [siem-soc](../categories/siem-soc.md) and [edr-xdr](../categories/edr-xdr.md) as an automation/decision layer. This is a SOC-operations tool, not an AI-application control: it does **not** break a leg of the lethal trifecta (trifecta_relevance: none). It lives in the green/trusted operations zone alongside your other security tooling.

**Deployment & architecture** — SaaS, integrates via API into SIEM/EDR/cloud/identity sources. No inline data-path role; it reads telemetry and writes investigations back. Fast to stand up (read-only integrations).

**Positioning & differentiators** — Founded by Kamal Shah (CEO) and Vibhav Sreekanti (CTO), both from StackRox (acquired by Red Hat), which lends cloud-native security credibility. Differentiates on autonomous, plain-language investigations plus the detection-tuning feedback loop. Nearest neighbors: [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md), [7ai](7ai.md), [simbian](simbian.md), and the hyperautomation-rooted [torq](torq.md); incumbents' built-in equivalents include CrowdStrike Charlotte AI and Palo Alto Cortex.

**Ownership, funding & M&A** — Independent, VC-backed. $30M Series A led by Accel (announced 2025-07-29), with Bain Capital Ventures; subsequent strategic investments from Amex Ventures and Citi Ventures bring reported total to ~$41M. No M&A. No seed acquisition flag to verify. Confidence high on independence, medium on the exact total.

**CTO / hedge-fund lens** — **Day-2.** This only makes sense once you already run a SIEM/EDR and have enough alert volume to justify automating triage. For a 50-person fund it is usually overkill unless you have a real SOC or MSSP relationship; mid-to-large asset managers with an in-house security team are the better fit. No direct SR 11-7 / model-risk angle — it's a security-ops efficiency play, though note you are introducing an LLM-driven agent into your investigation workflow (model-risk and data-handling diligence on the vendor applies).

**Competitors / alternatives** — [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md), [7ai](7ai.md), [simbian](simbian.md), [torq](torq.md).

**Open questions / to verify** — Exact total funding and valuation; on-prem/self-hosted option for regulated data; how customer telemetry is used for model training/retention.

## Sources
- [Prophet Security Raises $30M Series A Led by Accel](https://www.prophetsecurity.ai/blog/prophet-security-raises-30-million-series-a-led-by-accel) — fetched 2026-06-28 — supports: Series A amount/lead, product components, founders; confidence: med (vendor blog).
- [Prophet Security accelerates Agentic AI SOC with Amex/Citi Ventures (PRNewswire)](https://www.prnewswire.com/news-releases/prophet-security-accelerates-the-agentic-ai-soc-movement-with-strategic-investments-from-amex-ventures-and-citi-ventures-302696588.html) — fetched 2026-06-28 — supports: strategic investors, ~$41M total; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2023 founding, SF HQ, founders ex-StackRox, $30M Series A (Accel) + Amex/Citi strategic = ~$41M total, independent. Set ownership_confidence high. trifecta=none (SOC-ops tool). hedge_fund_fit=medium (Day-2).
