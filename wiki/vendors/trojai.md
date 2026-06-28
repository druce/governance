---
type: vendor
name: TrojAI
slug: trojai
categories: [ai-runtime-security, ai-red-teaming]
layer: model-prompt
aliases: [Troj.AI]
website: "https://troj.ai"
founded: 2019
hq: Saint John, New Brunswick, Canada (Boston office)
ownership: acquired
ownership_detail: "acq. by A10 Networks (NYSE: ATEN) — announced 2026-06-15; terms undisclosed; becomes A10's AI-security software arm (primary: A10 press release / BusinessWire)"
ownership_confidence: high
funding_total: ~$9.65M (pre-acquisition, disclosed)
last_funding: "Seed $5.75M, Apr 2024 (Flying Fish Partners, Build Ventures, Techstars Ventures)"
deployment: [api, self-hosted, saas]
target_customer: enterprise; MSSPs; sovereign / regulated buyers
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [ai-firewall, red-teaming, m-and-a, canada]
---

# TrojAI

> **One-liner** — AI-security platform pairing build-time red teaming (TrojAI Detect) with runtime threat protection (TrojAI Defend); acquired by network-security vendor A10 Networks in June 2026.

**Categories** — [ai-runtime-security](../categories/ai-runtime-security.md), [ai-red-teaming](../categories/ai-red-teaming.md)

## What it does
TrojAI secures enterprise AI across two layers. **TrojAI Detect** is automated **red teaming** — it probes models, applications, and agents for vulnerabilities at build time (jailbreaks, prompt injection, data leakage, harmful output), increasingly with *agent-led* multi-turn attack chains, and maps findings to OWASP / MITRE ATLAS / NIST. **TrojAI Defend** is a **runtime AI firewall** — inline inspection of prompts/responses to block prompt injection, sensitive-data leakage, and policy violations in production, including for AI coding agents (Claude Code, Codex). A newer *Agent Runtime Intelligence* capability (private preview as of early 2026) captures full agent execution traces for deeper runtime visibility.

## Where it sits in the stack
Spans [ai-runtime-security](../categories/ai-runtime-security.md) (Defend, the inline firewall — its primary slot) and [ai-red-teaming](../categories/ai-red-teaming.md) (Detect, build-time testing). In lethal-trifecta terms it addresses **untrusted-input** (catching prompt-injection/jailbreaks both pre-prod and inline) and **sensitive-data** (blocking data leakage in responses). It lives at the model/prompt boundary between users/apps and the model, and is meant to sit in the yellow zone in front of model calls.

## Deployment & architecture
API-based runtime inspection (Defend) that can be inserted in front of model endpoints / via an AI gateway; red-teaming (Detect) runs against model and app endpoints. Supports self-hosted / data-sovereign deployment — a point A10 emphasizes ("sovereign AI security"). Findings map to OWASP/MITRE/NIST; targets SIEM/SOC workflows and MSSP delivery. Post-acquisition, pairs with A10's hardware-based AI firewall appliances.

## Positioning & differentiators
One of the few players covering **both** build-time red teaming and runtime defense in one platform (vs. red-team-only [mindgard](mindgard.md)/[splxai](splxai.md) or runtime-leaning [prompt-security](prompt-security.md)). Differentiators: agent-led/multi-turn red teaming, coding-agent runtime protection, and a sovereignty/self-hosted posture attractive to regulated and non-US buyers and MSSPs. Canada-rooted with Boston go-to-market. Nearest neighbors: [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [enkrypt-ai](enkrypt-ai.md).

## Ownership, funding & M&A
**No seed M&A flag, but a recent acquisition CONFIRMED.** **A10 Networks (NYSE: ATEN)** announced it **acquired TrojAI on 2026-06-15** (primary: A10 press release + BusinessWire; corroborated by StockTitan/Investing.com). Terms undisclosed; A10 expects no material FY2026 financial impact. Rationale: combine A10's hardware AI firewall with TrojAI's software red teaming + runtime protection for "sovereign AI security." Founded 2019 (incorporated 2020) by **James Stewart (CTO)** and **Stephen Goddard**; CEO since 2024 is **Lee Weiner** (ex-Rapid7). HQ Saint John, New Brunswick, Canada, with a Boston office. Pre-acquisition funding ~$9.65M disclosed (incl. $5.75M seed Apr 2024 — Flying Fish Partners, Build Ventures, Techstars Ventures; plus NBIF). `ownership_confidence: high`.

## CTO / hedge-fund lens
**Day-1 for the runtime-firewall job** if you expose LLMs/agents to users or untrusted content; the red-teaming half is a strong Day-2 assurance layer feeding [promotion-gates](../categories/promotion-gates.md). SR 11-7 / model-risk angle: Detect produces framework-mapped test evidence useful for model validation; Defend gives an enforcement + logging control. The A10 acquisition is a double-edged consideration for a hedge fund: it adds a public-company parent and appliance integration (good for procurement stability and on-prem/sovereign needs), but the product is now part of a networking vendor's roadmap, so watch for repositioning. Self-hosted/sovereign deployment is a plus for funds wary of routing prompts through a vendor cloud. Fit **medium** — credible, but smaller and less proven at scale than [prisma-airs](prisma-airs.md) or [hiddenlayer](hiddenlayer.md); the new owner changes the buying calculus.

## Competitors / alternatives
[hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [splxai](splxai.md), [prompt-security](prompt-security.md).

## Open questions / to verify
- Acquisition close date and integration/rebrand under A10 (only the 2026-06-15 announcement was public as of 2026-06-28).
- Whether TrojAI Defend will be bundled with A10's firewall appliances vs. sold standalone.
- Exact post-acquisition pricing and whether the standalone SaaS continues.

## Sources
- [A10 Networks Acquires TrojAI Inc., Expanding AI Roadmap](https://www.a10networks.com/news/press-releases/a10-networks-acquires-trojai-inc-expanding-ai-roadmap/) — fetched 2026-06-28 — supports: acquisition 2026-06-15, rationale, two product layers; confidence: high
- [BusinessWire: A10 Networks Acquires TrojAI](https://www.businesswire.com/news/home/20260615349365/en/A10-Networks-Acquires-TrojAI-Inc.-Expanding-AI-Roadmap) — fetched 2026-06-28 — supports: acquisition, public-company parent; confidence: high
- [TrojAI extends platform — agent-led red teaming, runtime intelligence, coding-agent protection](https://www.prnewswire.com/news-releases/trojai-extends-enterprise-ai-security-with-agent-led-red-teaming-runtime-intelligence-and-coding-agent-protection-302716692.html) — fetched 2026-06-28 — supports: product capabilities; confidence: med (vendor)
- (cached: `raw/sources/2026-06-28--trojai--a10-acquisition.md`)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; ownership changed independent → **acquired** (A10 Networks, announced 2026-06-15, terms undisclosed) — NOT in seed flags; set ownership_confidence high. Established founding 2019 (Stewart/Goddard), CEO Lee Weiner, HQ Saint John NB, ~$9.65M raised pre-deal. Documented Detect (red team) + Defend (runtime) split. hedge_fund_fit = medium.
