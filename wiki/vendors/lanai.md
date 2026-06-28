---
title: Lanai
type: vendor
name: Lanai
slug: lanai
categories: [ai-access-governance]
layer: model-prompt
aliases: [Lanai AI, Lanai Software, withlanai]
website: "https://www.withlanai.com/"
founded:                            # not confirmed; stealth until 2025-01; ~2023-2024 inferred
hq: San Francisco, California, USA
ownership: independent
ownership_detail: VC-backed startup; no acquisition. Seed round led by Juxtapose (2025-01-23).
ownership_confidence: high
funding_total: ~$10M (seed)
last_funding: Seed, $10M, 2025-01-23
deployment: [endpoint-agent, saas]
target_customer: enterprise (Fortune 500; SaaS, fintech, healthcare, restaurant tech)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [shadow-ai, ai-observability, edge-detection, dlp-adjacent]
---

# Lanai

> Researched 2026-06-28. Primary category: [ai-access-governance](../categories/ai-access-governance.md). Confidently identified as the SF-based enterprise shadow-AI / AI-observability startup (withlanai.com, founders Lexi Reese + Steve Herrod) — not the Hawaiian island or unrelated software.

**One-liner** — An endpoint-based "AI observability" platform that discovers and governs all the AI tools employees actually use (including shadow AI), running prompt/response detection on the device so sensitive data and risky workflows are caught without routing traffic to the cloud.

**What it does** — Lanai installs a lightweight detection model on employee laptops/browsers that watches how people use AI assistants and agents — sanctioned tools, personal ChatGPT accounts, coding assistants (Cursor, etc.), and autonomous agents alike. Instead of just logging that someone visited `chatgpt.com`, it analyzes the *prompt + data pattern* on-device to flag when sensitive information (trade secrets, regulated data) is being pasted into third-party AI, and to map which AI workflows are in use across the org. By its April 2026 GA, Lanai had broadened this into an "AI @ Work Operating System" that also measures the *business impact* of each AI workflow (adoption, value, "scale-or-cut" decisions) via a queryable "AI graph" connected to systems like Salesforce, GitHub, and Zendesk over MCP. Positioning has drifted from pure security/shadow-AI (launch) toward "AI accountability / value measurement" — so it now straddles security and FinOps/enablement.

**Where it sits in the stack** — Primary: [ai-access-governance](../categories/ai-access-governance.md) at the **model-prompt** layer. It addresses two legs of the lethal trifecta: **sensitive-data** access (detecting confidential data going into prompts) and **egress** (data leaving to third-party AI services). It does not break the untrusted-input leg. Trust zones: it operates at the **green→red boundary**, i.e. the moment an employee on a managed endpoint sends data out to an untrusted external AI service. Functionally it is a shadow-AI-discovery + AI-aware DLP control that lives on the endpoint rather than the network or an inline proxy.

**Deployment & architecture** — Endpoint/edge agent: detection models run **directly on the device** (laptop/browser), with the vendor's explicit claim that "traffic [does not leave] the device perimeter." Deploys in under 24 hours via standard **MDM and SSO**; integrates with existing data-management tools. Detection is dynamic (no static allow/deny lists) and pattern-based — the vendor says it analyzes purpose/impact of interactions rather than reading and storing individual prompts (a privacy-positioning claim; treat as vendor-stated). The newer AI-graph layer is SaaS and pulls business-system context via MCP.

**Positioning & differentiators** — Lanai's distinguishing bet is **on-device detection** plus **workflow-level value measurement**, which is unusual in this crowd:
- vs [witnessai](witnessai.md) — WitnessAI is an inline/proxy "AI firewall" enforcing policy on traffic; Lanai is an endpoint observer that emphasizes not routing traffic centrally.
- vs [harmonic-security](harmonic-security.md) — Harmonic is browser/endpoint AI-DLP focused on stopping sensitive data in prompts; closest neighbor, but Lanai layers on portfolio/impact analytics ("Datadog of AI").
- vs [aurascape](aurascape.md) — Aurascape is network/proxy AI-activity visibility and control; Lanai is device-resident.
- vs [nudge-security](nudge-security.md) — Nudge discovers SaaS/AI accounts via email/OAuth signals and nudges users; Lanai inspects actual prompt/data patterns on the endpoint.
- vs [wald-ai](wald-ai.md) — Wald is a gateway/redaction proxy for safe AI use; Lanai avoids the proxy model.
- vs [reco](reco.md) — Reco is SaaS-posture/identity-centric discovery; Lanai is prompt-level and enablement-oriented.

The recurring theme: most peers sit inline (proxy/gateway) or in the IdP/SaaS-graph; Lanai is endpoint-resident and increasingly framed as enablement/ROI tooling, not just a guardrail.

**Ownership, funding & M&A** — Independent, VC-backed. Emerged from stealth **2025-01-23** with a **$10M seed** round **led by Juxtapose**, with Lux Capital, F7 Ventures, and BAG (Black Angel Group) participating; BenchStrength also later listed as a backer. No acquisition or M&A found — **independent (confidence: high)**. Founders: **Lexi Reese** (CEO; ex-COO Gusto, ex-Google) and **Dr. Steve Herrod** (co-founder; ex-VMware CTO, Juxtapose partner). Other leaders: Rajesh Raman (CTO, ex-Google/Meta/Splunk), Mohit Mehta (CPO, ex-Splunk/Nvidia). HQ: **San Francisco**.

> Contradiction (soft): seed size reported as **$10M** across Business Wire, Crunchbase, FinSMEs, citybiz (2025-01-23) vs a single unconfirmed "$11.5M" AI-generated search summary. Using $10M; $11.5M unverified — flagged 2026-06-28.

**CTO / hedge-fund lens** — Day-1-relevant problem (shadow AI on employee endpoints is exactly the data-leak vector a fund worries about), but Lanai is an **early-stage, enterprise-targeted** vendor whose published customers are Fortune 500. For a 50-person fund, the endpoint-agent + MDM/SSO model is operationally light, and "detect data going into third-party AI without an inline proxy" maps cleanly to model-risk/data-confidentiality concerns. Cautions: young company (seed-stage, GA only April 2026), unproven at small-shop scale, and the privacy claim ("we don't read prompts") and the on-device-only data claim should be validated in a POC. The pivot toward AI-ROI/enablement analytics may or may not match a security-led buyer's priorities. **Fit: medium** — promising for the shadow-AI-discovery job, but verify maturity and references.

**Competitors / alternatives** — [harmonic-security](harmonic-security.md), [witnessai](witnessai.md), [aurascape](aurascape.md), [nudge-security](nudge-security.md), [wald-ai](wald-ai.md), [reco](reco.md).

## Open questions / to verify
- Exact founding year (stealth until Jan 2025; ~2023–2024 inferred, not confirmed by a primary source).
- Reconcile seed size: $10M (corroborated) vs $11.5M (single unconfirmed summary) — possible later extension.
- Validate the on-device-only / "no traffic leaves the device" and "don't read individual prompts" claims technically (currently vendor-stated marketing).
- Enforcement depth: does Lanai *block/redact* in real time, or primarily observe + alert? Coverage of agentic/MCP traffic vs human prompts.
- Pricing and minimum deployment size; any sub-enterprise / mid-market offering.

## Sources
- [Lanai's edge-based observability agents aim to seek out and shut down shadow AI](https://siliconangle.com/2025/09/10/lanais-edge-based-observability-agents-aim-shut-shadow-ai/) — SiliconANGLE — fetched 2026-06-28 — supports: product mechanics (on-device detection), founders, differentiation, shadow-AI thesis; confidence: med (trade press; customer-result figures are vendor-provided/marketing).
- [Lanai launches AI @ Work Operating System…](https://www.prnewswire.com/news-releases/lanai-launches-ai--work-operating-system-to-help-enterprises-close-the-ai-accountability-gap-302743892.html) — Lanai via PR Newswire (MARKETING) — fetched 2026-06-28 — supports: GA date 2026-04-16, HQ San Francisco, investors, leadership, MCP/AI-graph, MDM+SSO deployment, target customers; confidence: med (vendor release).
- [About Lanai / company page](https://www.withlanai.com/company) — Lanai (MARKETING) — fetched 2026-06-28 — supports: self-description ("Enterprise AI Accountability Company"), AI @ Work OS + Token Tuner products, leadership bios; confidence: med.
- [Lanai emerges from stealth with $10M seed (launch)](https://www.businesswire.com/news/home/20250123017577/en/Silicon-Valley-Veterans-Launch-Lanai-The-Enterprise-AI-Navigation-System) — Business Wire (vendor launch) + corroborated by Crunchbase funding-round (2025-01-23) and FinSMEs — search-level 2026-06-28 — supports: $10M seed, Juxtapose-led, Lux/F7/BAG, founders Reese & Herrod, stealth-exit date; confidence: high on round, med on founding year.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed this is the SF enterprise shadow-AI / AI-observability startup (withlanai.com; founders Lexi Reese & Steve Herrod). Established: independent VC-backed (high confidence), $10M seed led by Juxtapose 2025-01-23 (no M&A), HQ San Francisco, endpoint/edge on-device detection deploying via MDM/SSO, GA of "AI @ Work OS" 2026-04-16. Cached 4 sources. Flagged soft contradiction on seed size ($10M vs unconfirmed $11.5M); founding year inferred ~2024, unverified.
