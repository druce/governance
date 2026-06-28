---
type: vendor
name: Aurascape
slug: aurascape
categories: [ai-access-governance, ai-runtime-security]
layer: model-prompt
aliases: ["AI Activity Control"]
website: "https://aurascape.ai"
founded: 2024
hq: Santa Clara, CA, USA
ownership: independent
ownership_detail: "VC-backed, independent as of 2026-06. No M&A found."
ownership_confidence: high
funding_total: "$62.8M (reported total across seed + Series A)"
last_funding: "Series A — $50M — 2025-04 (co-led by Mayfield Fund + Menlo Ventures)"
deployment: [saas, inline-proxy, browser]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress, untrusted-input]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [shadow-ai, ai-dlp, ai-visibility, prevention-first]
---

# Aurascape

> Researched 2026-06-28. Primary category: [ai-access-governance](../categories/ai-access-governance.md); also [ai-runtime-security](../categories/ai-runtime-security.md).

**One-liner** — An AI-native security platform that gives enterprises visibility into and control over every employee/app interaction with AI tools (sanctioned and shadow), with prevention-first data protection across text, code, image, audio, and video.

## What it does

Aurascape watches how people and applications in an organization actually use AI — public chatbots, embedded AI features, copilots, and agentic tools — and enforces policy on those interactions in real time. It decodes prompt/response traffic across what it markets as 1,500+ AI applications, classifies the content (including non-text modalities), and can block or remediate risky actions such as sensitive data being pasted into a public model. The core jobs: discover **shadow AI**, prevent data leakage to AI services, and apply granular guardrails without simply blocking all AI use. Marketing frames this as "AI Activity Control" and "prevention-first."

## Where it sits in the stack

- Primary: [ai-access-governance](../categories/ai-access-governance.md) — it governs who can use which AI tools and what data may flow to them, the classic shadow-AI discovery + access-control job. Layer: **model-prompt**.
- Secondary: [ai-runtime-security](../categories/ai-runtime-security.md) — because it inspects and can block prompt/response traffic inline, it overlaps with the AI-firewall/guardrail category.
- **Lethal-trifecta role:** mainly **sensitive-data** exposure and **egress** control (stopping confidential data from leaving to external AI services); to a lesser degree **untrusted-input** screening on responses. It is fundamentally an egress/DLP-for-AI control sitting at the boundary between the corporate (green/yellow) zone and external AI services (red zone).

## Deployment & architecture

Hybrid, per the lead investor's description:
- **Cloud-native inline proxy** for network-level monitoring of AI traffic.
- **Endpoint agent** for device-level visibility (catches browser plugins, local tools, traffic that bypasses the network path).
- Coverage spans LLMs, embedded AI, and shadow-AI tools; multimodal classification (text, code, image, audio, video).
- Integrations noted: Microsoft Copilot monitoring. Broader SIEM/IdP/DSPM integration not yet confirmed from primary sources.

This proxy-plus-agent model is closer to a SASE/SSE data-protection architecture than a pure API-based guardrail — unsurprising given the founders' Zscaler/Palo Alto/Netskope background.

## Positioning & differentiators

Aurascape positions as **AI-native and prevention-first**, arguing that legacy firewalls, regex DLP, and SASE tools can't parse the probabilistic, multimodal nature of AI traffic. Claimed differentiators (vendor/investor, treat as marketing): breadth of app coverage (1,500+), multimodal detection, low false positives, and 14 patents filed (2 approved as of the Menlo post).

Versus neighbors:
- vs [witnessai](witnessai.md) — both do AI access governance/observability with inline enforcement; close competitor.
- vs [harmonic-security](harmonic-security.md) and [wald-ai](wald-ai.md) — overlap on preventing sensitive-data leakage to GenAI; Harmonic leans browser/data-centric.
- vs [prompt-security](prompt-security.md) — Prompt leans toward runtime prompt-injection/guardrail firewalling; Aurascape leans access-governance + DLP.
- vs [lanai](lanai.md) — both target shadow-AI discovery; Lanai is more endpoint/edge-discovery focused.
- vs [cyberhaven](cyberhaven.md) — Cyberhaven is data-lineage DLP extending into AI; Aurascape is AI-first.
- vs [nudge-security](nudge-security.md) and [reco](reco.md) — those lean SaaS-posture/identity discovery; Aurascape is deeper on inline AI-traffic control.

## Ownership, funding & M&A

- **Independent, VC-backed.** No acquisition found; confidence high that it is independent as of 2026-06.
- **Founded 2024**, Santa Clara, CA. Launched from ~1 year of stealth on **2025-04-08**.
- **Seed:** $12.8M, August 2024, led by Mayfield Fund (with Celesta Capital, StepStone Group, AISpace, and Mark McLaughlin participating) — per aggregator/press, medium confidence.
- **Series A:** $50M, April 2025, co-led by **Mayfield Fund** and **Menlo Ventures**; strategic investors include former Palo Alto Networks CEO Mark McLaughlin, former Symantec CEO Greg Clark, Walden International's Lip-Bu Tan, and former Zscaler CSO Manoj Apte.
- **Reported total funding: ~$62.8M.** Note: the launch PR headlines "$50M" (the Series A); the $62.8M figure is the seed + Series A total per press/aggregators.
- **Founders:** Moinul Khan (CEO; ex-Zscaler SSE/data-protection lead, ex-Palo Alto Networks, ex-Netskope), Patrick Xu (CTO). Additional co-founders (Viswesh, Liang Li) per aggregators — lower confidence on exact roles. Team drawn from Palo Alto Networks, Zscaler, Netskope, Google, Amazon.

## CTO / hedge-fund lens

This is a **Day-1-relevant** control for any firm where employees are already using AI tools (i.e., everyone): it answers "what AI are my people using and what data is going to it?" For a hedge fund, the strongest fit is the egress/DLP angle — preventing MNPI, positions, or client data from leaking into public models — plus an audit trail of AI usage that supports governance and exam readiness. SR 11-7 model-risk relevance is indirect: Aurascape governs *usage and data flow*, not model validation, so it complements rather than satisfies model-risk programs.

Caveats for a smaller shop: it's an early-stage (2024) company with a proxy + endpoint-agent footprint, which is heavier to deploy than a pure-API guardrail and competes in a crowded field. Reference customers, pricing, and SOC 2/compliance posture are not yet established here and should be diligenced. Fit rated **medium** pending that.

## Competitors / alternatives

[witnessai](witnessai.md) · [harmonic-security](harmonic-security.md) · [wald-ai](wald-ai.md) · [prompt-security](prompt-security.md) · [lanai](lanai.md) · [nudge-security](nudge-security.md) · [reco](reco.md) · [cyberhaven](cyberhaven.md)

## Open questions / to verify

- Exact total funding: reconcile "$50M" (PR headline) vs "$62.8M" (reported total). Seed round amount/date needs a primary source.
- Full co-founder roster and roles (Patrick Xu / Viswesh / Liang Li currently aggregator-sourced).
- Integration depth: SIEM/SOAR, IdP/SSO, DSPM, MCP support — not confirmed from primary sources.
- Compliance posture (SOC 2, ISO), pricing model, and named reference customers.
- Real-world false-positive rate and deployment friction of the inline-proxy + agent model.

## Sources

- [Aurascape Launches from Stealth with $50M in Funding (official PR / Aurascape.ai mirror)](https://aurascape.ai/resources/news/aurascape-launches-from-stealth-with-50m-in-funding-and-an-ai-native-security-platform-to-enable-businesses-to-innovate-fearles/) — fetched 2026-06-28 — supports: founded 2024, Santa Clara HQ, $50M Series A Apr 2025, investors, product; confidence: high (vendor/marketing for product claims)
- [Investing in Aurascape — Menlo Ventures perspective](https://menlovc.com/perspective/investing-in-aurascape-building-the-security-stack-for-the-ai-era/) — fetched 2026-06-28 — supports: hybrid inline-proxy + endpoint-agent deployment, 1,500+ apps, multimodal, founder pedigree, patents; confidence: medium (lead investor, promotional)
- [Aurascape Banks Hefty $50 Million to Mitigate 'Shadow AI' Risks — SecurityWeek](https://www.securityweek.com/aurascape-banks-hefty-50-million-to-mitigate-shadow-ai-risks/) — fetched 2026-06-28 — supports: independent confirmation of funding/investors, shadow-AI product framing; confidence: high
- [Aurascape launches with $50M in funding — SiliconANGLE](https://siliconangle.com/2025/04/08/aurascape-launches-50m-funding-bring-security-observability-ai-apps/) — fetched 2026-06-28 — supports: $62.8M total / $12.8M seed Aug 2024, CEO Moinul Khan background; confidence: medium (press, partly aggregator-derived)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2024 (Santa Clara, CA), launched from stealth Apr 2025, $50M Series A (Mayfield + Menlo) + $12.8M seed (~$62.8M reported total), independent (no M&A) at high confidence, CEO Moinul Khan (ex-Zscaler/PAN/Netskope). Added [ai-runtime-security](../categories/ai-runtime-security.md) as secondary category given inline prompt/response enforcement. 4 sources cached.
