---
title: SplxAI
type: vendor
name: SplxAI
slug: splxai
aka: [SPLX, SPLX AI, SplxAI Inc.]
primary_category: ai-red-teaming
also_listed_in: [ai-runtime-security]
website: https://splx.ai
founded: 2023
hq: Dover, Delaware, US (Croatian engineering roots; NYC US presence)
ownership_state: acquired-closed
owner: Zscaler
ownership_note: 'Acquired by Zscaler (NASDAQ: ZS); closed 2025-10-31 for $40.6M cash, publicly announced 2025-11-03 as an already-completed deal. Close date and price per Zscaler Form 10-Q for the quarter ended 2025-10-31 (Note 6). SPLX brand and splx.ai retained.'
acquisition: {announced: 2025-11-03, closed: 2025-10-31, price: '$40.6M cash (Zscaler 10-Q, Q1 FY2026)'}
funding_total: ~$7M (pre-acquisition)
last_funding: $7M seed, 2025-03-26 (led by LAUNCHub Ventures)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise (regulated + AI-building orgs)
last_verified: 2026-07-27
verify_after: null
tags: [ai-red-teaming, ai-runtime-security, prompt-injection, agentic-ai, zscaler, acquired]
sources:
  - {claim: acquisition-close, url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/zs-20251031.htm", date: 2025-11-25, confidence: high}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/zs-20251031.htm", date: 2025-11-25, confidence: high}
  - {claim: acquisition-announced, url: "https://www.zscaler.com/press/zscaler-secures-enterprise-ai-lifecycle-acquisition-innovative-ai-security-pioneer-splx", date: 2025-11-03, confidence: high}
---

# SplxAI

> **Researched 2026-06-28; re-verified 2026-07-27 against Zscaler's SEC filings.** Now **SPLX, a Zscaler company** — acquired by [zscaler](zscaler.md), **closed 2025-10-31 for $40.6M cash**, publicly announced three days later on 2025-11-03. `splx.ai` is still live (HTTP 200, no redirect) under the SPLX brand and banners "SPLX is now part of Zscaler"; Probe still ships as a named product. Primary category: [ai-red-teaming](../categories/ai-red-teaming.md); also [ai-runtime-security](../categories/ai-runtime-security.md). **No longer an independent company** — shop for this inside a Zscaler platform conversation.

**One-liner** — Automated, continuous AI red-teaming ("Probe") plus runtime guardrails and prompt-hardening for conversational and agentic AI apps — now owned by Zscaler.

## What it does

SplxAI attacks your own AI applications before adversaries do. Its flagship product, **Probe**, runs thousands of automated adversarial simulations (the company cites 5,000+ attack scenarios) against chatbots, copilots, RAG pipelines, and agentic workflows — probing for prompt injection, jailbreaks, data leakage, hallucinations, toxic output, and off-topic/PII exposure across text, image, and voice. It then triages findings and recommends remediations (including **prompt hardening** — automatically tightening system prompts). Beyond pre-deployment testing, SPLX added **runtime guardrails** plus AI asset discovery and governance/compliance reporting, pushing it from a point red-teaming tool toward a fuller AI-security lifecycle platform. The team also open-sourced **Agentic Radar**, a static-analysis tool that maps dependencies in agentic workflows to surface missing controls.

The pitch is economic as much as technical: automated red-teaming is positioned as far cheaper and more repeatable than manual pentests (the company claims manual evaluation is ~5x more expensive — a vendor marketing figure).

## Where it sits in the stack

- Primary: [ai-red-teaming](../categories/ai-red-teaming.md) (model/prompt layer) — the proactive, pre-deployment leg: find weaknesses in your AI app before go-live and on every change.
- Secondary: [ai-runtime-security](../categories/ai-runtime-security.md) (AI firewall) — runtime guardrails/threat inspection that block malicious prompts and unsafe responses in production.

**Risk coverage.** Red-teaming is overwhelmingly about **untrusted input** — stress-testing how the app handles hostile prompts/content. The runtime guardrails extend coverage toward **sensitive-data** exposure and **exfiltration** (blocking data leakage and unsafe tool/response paths). Net: it spans input screening, data protection and outbound controls, but its center of gravity is untrusted-input/prompt-injection. Trust zone: wherever LLM-facing apps live (typically yellow/green app tiers).

## Deployment & architecture

- **SaaS** platform with **API** access, so Probe scans can be wired into CI/CD and dev workflows (test the app on every release).
- Runtime guardrails operate as an inline inspection/guardrail layer for production traffic (threat inspection + prompt hardening).
- Connects to the AI apps/agents under test; post-acquisition the roadmap is integration into the **Zscaler Zero Trust Exchange** (AI asset discovery → red teaming → runtime guardrails → governance, "development through deployment").
- Open-source adjunct: Agentic Radar (static analysis of agent workflows).

## Positioning & differentiators

SplxAI is known for **automated, continuous** red-teaming (not a one-off manual engagement) with a research-driven, continually-updated attack database and multi-modal coverage (text/image/voice). Founders and team came out of AI red-teaming at Cisco, Zscaler, and Wiz, with CTF wins (Wiz, Black Hat) as credibility.

**Positioning has changed: this is now a platform feature, not a standalone bet.** Since 2025-10-31 SPLX is a Zscaler product line, so the honest comparison is no longer "SPLX vs other red-teaming startups" but "Zscaler's AI-security stack vs the other SSE/platform stacks." That reframes almost every row below: the pure-plays are now the *independent* alternatives to a captive Zscaler capability, and the incumbent-owned tools are the true head-to-head competitors.

Versus neighbors:
- [mindgard](mindgard.md) — closest pure-play automated AI red-teaming peer (research/academia roots); both target offensive testing of AI apps. **Now one of the few remaining independent options** in this niche if you don't want to buy into a platform.
- [promptfoo](promptfoo.md) — open-source/developer-first eval + red-teaming (acq. by OpenAI); SPLX is the enterprise SaaS, governance-flavored counterpart. Both are now incumbent-owned.
- [enkrypt-ai](enkrypt-ai.md) — overlapping red-team + guardrails combo; both straddle testing and runtime.
- [lakera](lakera.md) — strong on runtime prompt-injection guardrails (and red-teaming via Gandalf heritage); Lakera is more runtime-firewall-first, SPLX more red-team-first. Now Check Point-owned, making this a **Zscaler vs Check Point** comparison rather than a startup bake-off.
- [pillar-security](pillar-security.md) — runtime + posture for AI apps; overlaps on the runtime side.
- [hiddenlayer](hiddenlayer.md) — model-centric security (model scanning + detection-response) and red-teaming; different emphasis (model artifacts vs app behavior).
- [prisma-airs](prisma-airs.md), [witnessai](witnessai.md) — runtime AI firewall / access-governance incumbents; SPLX's guardrails compete at the edges but its differentiator is the offensive testing side. Prisma AIRS is the direct **Palo Alto vs Zscaler** platform rival.

The Zscaler acquisition mirrors the broader consolidation: network/SSE incumbents buying AI-security capability to bolt onto existing inline enforcement points. The AI red-teaming category has now been almost entirely absorbed this way — Lakera→Check Point, promptfoo→OpenAI, CalypsoAI→F5, SPLX→Zscaler — which means the practical selection question for a buyer is increasingly *which platform vendor you already run*, not which red-teaming engine tests best. The $40.6M price tag is worth noting for what it signals: a small tuck-in acqui-hire-plus-technology deal (about a third of the consideration was retention equity), not a category-defining purchase, so expect SPLX to show up as a Zscaler feature rather than a preserved standalone franchise.

## Ownership, funding & M&A

- **Funding (pre-acquisition):** $7M seed, announced 2025-03-26, **led by LAUNCHub Ventures**, with Rain Capital, Inovo, Runtime Ventures, DNV Ventures, and South Central Ventures. Brief's "led by LAUNCHub" — **confirmed**. No separate later priced round found before acquisition.
- **M&A — CONFIRMED, dates and price corrected 2026-07-27.** Acquired by **Zscaler (NASDAQ: ZS)**. **Closed 2025-10-31**; **publicly announced 2025-11-03**. Price: **$40.6M total cash purchase consideration**, plus $16.6M grant-date fair value of restricted shares to retained SPLX employees (service-conditioned, so expensed post-combination rather than counted as purchase price) and 50,180 deferred shares for key-employee re-vesting. Source: Zscaler's **Form 10-Q for the quarter ended 2025-10-31** (filed 2025-11-25), Note 6 *Business Combinations*: "On October 31, 2025, we acquired all the equity of SPLXAI Inc." Ownership confidence: **high**.
- **The deal closed before it was announced.** Zscaler's 2025-11-03 press release says it "today announced it *has acquired*" SPLX — it publicised a transaction that had already completed on the last day of Zscaler's fiscal Q1. There was no publicly-announced signing date and never a pending window, which is why `announced` post-dates `closed` in the frontmatter. That ordering is deliberate and correct.
- **Price correction.** This page previously said the SPLX price was "not separately disclosed" and folded it into the **$692.0M** aggregate. That aggregate is real but covers **two** deals that closed in the same quarter — Red Canary (closed **2025-08-01**, the much larger component) and SPLX. The 10-Q does break SPLX out separately, at $40.6M.
- The research brief assumed "independent"; that is now outdated (soft/scope, not a hard contradiction — the brief predates or missed the deal). Ownership reset to **subsidiary (Zscaler)**.

> Note: founding year — the seed announcement says **founded 2023**; SiliconANGLE says the product "launched August 2024." Read as entity formed 2023, product GA mid-2024. Soft, non-blocking.

## CTO / hedge-fund lens

**Day-2, low direct fit for most hedge funds.** SplxAI/Probe is a tool you need when you are *building and shipping your own* LLM/agent applications and want to test them adversarially — a developer/AppSec capability. A typical 50-person fund consuming ChatGPT Enterprise or Copilot does not red-team its own models and gets little from this. It becomes relevant only if the fund builds customer- or analyst-facing AI agents that handle sensitive data, in which case automated red-teaming + runtime guardrails are a sensible Day-2 control once the basics (access governance, DLP, an AI gateway) are in place.

Model-risk angle: the governance/compliance reporting can feed an SR 11-7-style model-risk file (evidence of adversarial testing), but SplxAI is a testing tool, not a governance platform — pair it with an [ai-governance-platform](../categories/ai-governance-platform.md) vendor for that.

Practical note: because it is now part of **Zscaler** (closed 2025-10-31), shops that already run Zscaler SSE may get this capability as a platform add-on rather than a standalone buy. As of 2026-07-27 SPLX still sells under its own brand with its own Probe login, so a standalone evaluation is still possible — but at a $40.6M tuck-in price, roughly a third of it retention equity, this was bought as technology and a team to fold into the Zero Trust Exchange, not as a franchise to preserve. Budget on the assumption it becomes a Zscaler SKU, and if you are *not* a Zscaler shop, weigh [mindgard](mindgard.md) (the remaining independent) or whichever platform you have already standardised on.

## Competitors / alternatives

[mindgard](mindgard.md), [enkrypt-ai](enkrypt-ai.md), [lakera](lakera.md), [pillar-security](pillar-security.md), [promptfoo](promptfoo.md), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [witnessai](witnessai.md)

## Open questions / to verify

- ~~SPLX-specific acquisition price~~ — **RESOLVED 2026-07-27**: $40.6M cash, per Zscaler's 10-Q Note 6.
- ~~Exact close date within Zscaler Q1 FY2026~~ — **RESOLVED 2026-07-27**: 2025-10-31.
- Whether Probe/runtime guardrails remain available as a standalone product, or only via the Zscaler Zero Trust Exchange, and any pricing/packaging changes post-integration. As of 2026-07-27 `splx.ai` still markets Probe under the SPLX brand with its own login at `probe.splx.ai`, which suggests standalone availability survives for now — but that is inference from the marketing site, not a confirmed Zscaler packaging statement.
- Precise founded month vs product GA.
- CTO co-founder Ante Gojsalić — confirm current role post-acquisition.

## Sources

- [Zscaler Form 10-Q, quarter ended 2025-10-31](https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/zs-20251031.htm) (filed 2025-11-25), Note 6 *Business Combinations* — fetched 2026-07-27 — supports: **close date 2025-10-31**, **SPLX-specific price $40.6M cash**, $16.6M retention RSUs, 50,180 deferred shares, $13.0M developed technology / $1.1M customer relationships; also separates Red Canary (closed 2025-08-01) from SPLX within the $692.0M Q1 FY2026 aggregate; confidence: high. Cached: `raw/sources/2026-07-27--splxai--zscaler-10q-close-date-price.md`
- [Zscaler press: acquisition of SPLX](https://www.zscaler.com/press/zscaler-secures-enterprise-ai-lifecycle-acquisition-innovative-ai-security-pioneer-splx) — fetched 2026-06-28, re-checked 2026-07-27 — supports: public announcement date 2025-11-03, phrased "has acquired" (already-closed deal, no closing-conditions language, no terms disclosed), products/scope; confidence: high
- [SplxAI blog: $7M seed round](https://splx.ai/blog/splxai-closes-7m-seed-funding-round-to-help-organizations-secure-agentic-ai-systems) — fetched 2026-06-28 — supports: $7M seed led by LAUNCHub + investors, founded 2023, Delaware HQ, Probe/runtime; confidence: high
- [SiliconANGLE: SplxAI $7M / automated red teaming](https://siliconangle.com/2025/03/26/splxai-gets-7m-try-block-prompt-injection-attacks-ai-agents-automated-red-teaming/) — fetched 2026-06-28 — supports: Probe mechanics, SaaS+API deployment, founders ex-Cisco/Zscaler/Wiz, customers (KPMG, Infobip, Glean), Agentic Radar; confidence: med
- [Vestbee: Croatian SplxAI closes $7M seed](https://www.vestbee.com/insights/articles/croatian-splx-ai-closes-7-m-seed-round) — fetched 2026-06-28 — supports: Croatian roots, founders Kamber/Gojsalić, seed details; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established $7M seed (2025-03-26, led by LAUNCHub Ventures + Rain/Inovo/Runtime/DNV/South Central), founded 2023 (Croatian roots, Delaware/NYC US), Probe automated red-teaming + runtime guardrails (SaaS/API). CONFIRMED acquisition by Zscaler (announced 2025-11-03, closed Q1 FY2026; bundled $692M with Red Canary, SPLX portion undisclosed) — ownership changed from independent→subsidiary, confidence high. Set hedge_fund_fit low (build-your-own-AI tool). Cached 4 sources.
- [2026-07-27] URL audit + M&A re-verification against primary SEC filings. `splx.ai` live (HTTP 200, no redirect), title "SPLX | End-to-End Security for AI", banner "SPLX is now part of Zscaler" — brand and Probe product retained, so `website` unchanged. **Corrected two frontmatter errors** found by checking Zscaler's Form 10-Q for the quarter ended 2025-10-31 (Note 6): (1) `closed` was 2025-11-03, a duplicate of the announcement date with no supporting source — the real close date is **2025-10-31**, three days *before* the public announcement, because Zscaler announced an already-completed deal; (2) `price` was null and the body claimed the SPLX figure was "not separately disclosed" inside the $692.0M Red Canary + SPLX aggregate — the 10-Q does break it out, at **$40.6M cash** (plus $16.6M service-conditioned retention RSUs and 50,180 deferred shares). `ownership_state: acquired-closed` confirmed correct and now genuinely sourced. Rewrote competitive positioning for a platform-owned product (category now almost fully consolidated: Lakera→Check Point, promptfoo→OpenAI, CalypsoAI→F5, SPLX→Zscaler; mindgard remains independent). Cached 1 new source.
