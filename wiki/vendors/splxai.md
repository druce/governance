---
type: vendor
name: SplxAI
slug: splxai
categories: [ai-red-teaming, ai-runtime-security]
layer: model-prompt
aliases: [SPLX, SPLX AI, SplxAI Inc.]
website: https://splx.ai
founded: 2023
hq: Dover, Delaware, US (Croatian engineering roots; NYC US presence)
ownership: subsidiary
ownership_detail: "Acquired by Zscaler (NASDAQ: ZS); announced 2025-11-03, closed Zscaler Q1 FY2026 (bundled with Red Canary, aggregate $692M; SPLX portion not separately disclosed)"
ownership_confidence: high
funding_total: ~$7M (pre-acquisition)
last_funding: "$7M seed, 2025-03-26 (led by LAUNCHub Ventures)"
deployment: [saas, api]
target_customer: enterprise (regulated + AI-building orgs)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [ai-red-teaming, ai-runtime-security, prompt-injection, agentic-ai, zscaler]
---

# SplxAI

> Now **SPLX, a Zscaler company.** Acquired by [[zscaler]] — announced 2025-11-03, closed in Zscaler's Q1 FY2026. Primary category: [[ai-red-teaming]]; also [[ai-runtime-security]].

**One-liner** — Automated, continuous AI red-teaming ("Probe") plus runtime guardrails and prompt-hardening for conversational and agentic AI apps — now owned by Zscaler.

## What it does

SplxAI attacks your own AI applications before adversaries do. Its flagship product, **Probe**, runs thousands of automated adversarial simulations (the company cites 5,000+ attack scenarios) against chatbots, copilots, RAG pipelines, and agentic workflows — probing for prompt injection, jailbreaks, data leakage, hallucinations, toxic output, and off-topic/PII exposure across text, image, and voice. It then triages findings and recommends remediations (including **prompt hardening** — automatically tightening system prompts). Beyond pre-deployment testing, SPLX added **runtime guardrails** plus AI asset discovery and governance/compliance reporting, pushing it from a point red-teaming tool toward a fuller AI-security lifecycle platform. The team also open-sourced **Agentic Radar**, a static-analysis tool that maps dependencies in agentic workflows to surface missing controls.

The pitch is economic as much as technical: automated red-teaming is positioned as far cheaper and more repeatable than manual pentests (the company claims manual evaluation is ~5x more expensive — a vendor marketing figure).

## Where it sits in the stack

- Primary: [[ai-red-teaming]] (model/prompt layer) — the proactive, pre-deployment leg: find weaknesses in your AI app before go-live and on every change.
- Secondary: [[ai-runtime-security]] (AI firewall) — runtime guardrails/threat inspection that block malicious prompts and unsafe responses in production.

**Lethal-trifecta role.** Red-teaming is overwhelmingly about the **untrusted-input** leg — stress-testing how the app handles hostile prompts/content. The runtime guardrails extend coverage toward **sensitive-data** exposure and **egress** (blocking data leakage and unsafe tool/response paths). Net: it touches all three legs, but its center of gravity is untrusted-input/prompt-injection. Trust zone: wherever LLM-facing apps live (typically yellow/green app tiers).

## Deployment & architecture

- **SaaS** platform with **API** access, so Probe scans can be wired into CI/CD and dev workflows (test the app on every release).
- Runtime guardrails operate as an inline inspection/guardrail layer for production traffic (threat inspection + prompt hardening).
- Connects to the AI apps/agents under test; post-acquisition the roadmap is integration into the **Zscaler Zero Trust Exchange** (AI asset discovery → red teaming → runtime guardrails → governance, "development through deployment").
- Open-source adjunct: Agentic Radar (static analysis of agent workflows).

## Positioning & differentiators

SplxAI is known for **automated, continuous** red-teaming (not a one-off manual engagement) with a research-driven, continually-updated attack database and multi-modal coverage (text/image/voice). Founders and team came out of AI red-teaming at Cisco, Zscaler, and Wiz, with CTF wins (Wiz, Black Hat) as credibility.

Versus neighbors:
- [[mindgard]] — closest pure-play automated AI red-teaming peer (research/academia roots); both target offensive testing of AI apps.
- [[promptfoo]] — open-source/developer-first eval + red-teaming (acq. by OpenAI); SplxAI is the enterprise SaaS, governance-flavored counterpart.
- [[enkrypt-ai]] — overlapping red-team + guardrails combo; both straddle testing and runtime.
- [[lakera]] — strong on runtime prompt-injection guardrails (and red-teaming via Gandalf heritage); Lakera is more runtime-firewall-first, SplxAI more red-team-first.
- [[pillar-security]] — runtime + posture for AI apps; overlaps on the runtime side.
- [[hiddenlayer]] — model-centric security (model scanning + detection-response) and red-teaming; different emphasis (model artifacts vs app behavior).
- [[prisma-airs]], [[witnessai]] — runtime AI firewall / access-governance incumbents; SplxAI's guardrails compete at the edges but its differentiator is the offensive testing side.

The Zscaler acquisition mirrors the broader consolidation: network/SSE incumbents buying AI-security capability to bolt onto existing inline enforcement points.

## Ownership, funding & M&A

- **Funding (pre-acquisition):** $7M seed, announced 2025-03-26, **led by LAUNCHub Ventures**, with Rain Capital, Inovo, Runtime Ventures, DNV Ventures, and South Central Ventures. Brief's "led by LAUNCHub" — **confirmed**. No separate later priced round found before acquisition.
- **M&A — CONFIRMED:** Acquired by **Zscaler (NASDAQ: ZS)**. Announced **2025-11-03** (Zscaler press release + SPLX blog). **Closed** during Zscaler's **Q1 fiscal 2026**; Zscaler disclosed Red Canary + SPLXAI together for an aggregate $692.0M — the SPLX-specific price is **not separately disclosed** (Red Canary was the much larger component). Ownership confidence: **high**.
- The research brief assumed "independent"; that is now outdated (soft/scope, not a hard contradiction — the brief predates or missed the deal). Ownership reset to **subsidiary (Zscaler)**.

> Note: founding year — the seed announcement says **founded 2023**; SiliconANGLE says the product "launched August 2024." Read as entity formed 2023, product GA mid-2024. Soft, non-blocking.

## CTO / hedge-fund lens

**Day-2, low direct fit for most hedge funds.** SplxAI/Probe is a tool you need when you are *building and shipping your own* LLM/agent applications and want to test them adversarially — a developer/AppSec capability. A typical 50-person fund consuming ChatGPT Enterprise or Copilot does not red-team its own models and gets little from this. It becomes relevant only if the fund builds customer- or analyst-facing AI agents that handle sensitive data, in which case automated red-teaming + runtime guardrails are a sensible Day-2 control once the basics (access governance, DLP, an AI gateway) are in place.

Model-risk angle: the governance/compliance reporting can feed an SR 11-7-style model-risk file (evidence of adversarial testing), but SplxAI is a testing tool, not a governance platform — pair it with an [[ai-governance-platform]] vendor for that.

Practical note: because it is now part of **Zscaler**, shops that already run Zscaler SSE may eventually get this capability as a platform add-on rather than a standalone buy — worth tracking how the standalone product and pricing survive integration.

## Competitors / alternatives

[[mindgard]], [[enkrypt-ai]], [[lakera]], [[pillar-security]], [[promptfoo]], [[hiddenlayer]], [[prisma-airs]], [[witnessai]]

## Open questions / to verify

- SPLX-specific acquisition price (bundled with Red Canary at $692M aggregate; not broken out).
- Whether Probe/runtime guardrails remain available as a standalone product, or only via the Zscaler Zero Trust Exchange, and any pricing/packaging changes post-integration.
- Exact close date within Zscaler Q1 FY2026; precise founded month vs product GA.
- CTO co-founder Ante Gojsalić — confirm current role post-acquisition.

## Sources

- [Zscaler press: acquisition of SPLX](https://www.zscaler.com/press/zscaler-secures-enterprise-ai-lifecycle-acquisition-innovative-ai-security-pioneer-splx) — fetched 2026-06-28 — supports: Zscaler acquired SPLX, announced 2025-11-03, products/scope; confidence: high
- [SplxAI blog: $7M seed round](https://splx.ai/blog/splxai-closes-7m-seed-funding-round-to-help-organizations-secure-agentic-ai-systems) — fetched 2026-06-28 — supports: $7M seed led by LAUNCHub + investors, founded 2023, Delaware HQ, Probe/runtime; confidence: high
- [SiliconANGLE: SplxAI $7M / automated red teaming](https://siliconangle.com/2025/03/26/splxai-gets-7m-try-block-prompt-injection-attacks-ai-agents-automated-red-teaming/) — fetched 2026-06-28 — supports: Probe mechanics, SaaS+API deployment, founders ex-Cisco/Zscaler/Wiz, customers (KPMG, Infobip, Glean), Agentic Radar; confidence: med
- [Vestbee: Croatian SplxAI closes $7M seed](https://www.vestbee.com/insights/articles/croatian-splx-ai-closes-7-m-seed-round) — fetched 2026-06-28 — supports: Croatian roots, founders Kamber/Gojsalić, seed details; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established $7M seed (2025-03-26, led by LAUNCHub Ventures + Rain/Inovo/Runtime/DNV/South Central), founded 2023 (Croatian roots, Delaware/NYC US), Probe automated red-teaming + runtime guardrails (SaaS/API). CONFIRMED acquisition by Zscaler (announced 2025-11-03, closed Q1 FY2026; bundled $692M with Red Canary, SPLX portion undisclosed) — ownership changed from independent→subsidiary, confidence high. Set hedge_fund_fit low (build-your-own-AI tool). Cached 4 sources.
