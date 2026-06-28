---
type: vendor
name: Apex Security
slug: apex-security
categories: [agent-runtime-security]
layer: model-prompt
aliases: [Apex, Apex AI Security]
website: "https://www.apexsec.com"
founded: 2023
hq: Tel Aviv, Israel
ownership: acquired
ownership_detail: "Acquired by Tenable (NASDAQ: TENB) — announced 2025-05-29 (>$105M reported), expected close Q2 2025; integrated into Tenable One exposure management (H2 2025)"
ownership_confidence: high
funding_total: ~$25M (pre-acquisition; seed + Series A)
last_funding: "Series A (backers incl. Sam Altman, Sequoia Capital, Index Ventures)"
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [acquired, ai-spm, shadow-ai, agent-security, exposure-management]
---

# Apex Security

> **Researched 2026-06-28.** Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). **Acquired by Tenable** (announced 2025-05-29).

**One-liner** — An AI-attack-surface / AI-governance startup (discover ungoverned AI, enforce policy, govern agents) bought by exposure-management vendor Tenable and folded into Tenable One.

## What it does
Apex secures the AI attack surface: it discovers **ungoverned / shadow AI** (apps, AI-generated code, AI identities), enforces policy on AI usage, and controls exposure across both the AI tools an organization *uses* and the AI systems it *builds* — including governance/runtime control of AI agents. The pitch is visibility + control over everything AI in the enterprise, mapped into a security/exposure view.

## Where it sits in the stack
Primary [agent-runtime-security](../categories/agent-runtime-security.md) (runtime governance of agentic AI) with strong overlap into [ai-spm](../categories/ai-spm.md) (AI discovery/posture) and [ai-access-governance](../categories/ai-access-governance.md) (shadow AI). Layer: model-prompt. Lethal-trifecta role: as a governance/visibility + policy layer it touches all three legs indirectly — flagging risky **untrusted-input** exposure, **sensitive-data** handling, and AI **egress**. Post-acquisition it becomes the AI lens of Tenable's exposure-management view.

## Deployment & architecture
SaaS / API-based discovery and policy enforcement across the AI estate (used tools + built systems). Following close, capabilities are delivered as part of **Tenable One**, Tenable's unified exposure-management platform — adding AI visibility, context and control alongside vuln/asset exposure data. Integrations: the enterprise SaaS/AI estate, IdP, Tenable One.

## Positioning & differentiators
Apex's angle was breadth across "AI you use and AI you build" framed as **exposure management** rather than a single inline firewall — which is exactly why an exposure-management leader (Tenable) acquired it to extend Tenable One into AI. Notable for a marquee investor list. Nearest neighbors: [zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md), [noma-security](noma-security.md), [quilr](quilr.md), [reco](reco.md), [nudge-security](nudge-security.md).

## Ownership, funding & M&A
Founded **2023** by Matan Derman (CEO) and Tomer Avni (CPO); Israeli startup (HQ Tel Aviv). Backed by a high-profile group — **Sam Altman**, Clem Delangue (Hugging Face), **Sequoia Capital**, **Index Ventures** (~$25M raised across seed + Series A; exact total not itemized in sources). **Acquired by Tenable** (NASDAQ: TENB) — announced **2025-05-29**; deal value not officially disclosed, Calcalist reported **>$105M**; expected to **close in Q2 2025**, with integrated capabilities in Tenable One in **H2 2025**. Verified against Tenable's own press release and corroborating press; confirms the seed flag ("acq by Tenable"). **Confidence: high.**

## CTO / hedge-fund lens
Day-2 (AI posture/governance is something you layer on after baseline controls). Relevant mainly if you are a **Tenable shop** doing exposure management and want AI assets in the same risk picture — shadow-AI discovery + agent governance has real value for a fund worried about ungoverned AI usage. Mild SR 11-7 relevance (AI inventory/governance supports model-risk documentation). Standalone Apex is no longer the buying unit; evaluate via Tenable One.

## Competitors / alternatives
[zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md), [noma-security](noma-security.md), [quilr](quilr.md), [reco](reco.md), [nudge-security](nudge-security.md), [wiz](wiz.md).

## Open questions / to verify
- Confirm the deal **closed** (announced 2025-05-29, expected Q2 2025) — verify completion date.
- Precise total funding (sources cite the investor list; ~$25M approximate).
- Whether the Apex brand persists or is fully absorbed into Tenable One.

## Sources
- [Tenable Announces Intent to Acquire Apex Security (Tenable press release)](https://www.tenable.com/press-releases/tenable-announces-intent-to-acquire-apex-security-to-expand-exposure-management-across-the-ai-attack-surface) — fetched 2026-06-28 — supports: 2025-05-29 announce, Apex capabilities, founders, founding 2023, investor list, Tenable One integration, Q2 2025 close; confidence: high
- [Tenable acquires Sam Altman-backed Apex for over $105 million (Calcalist)](https://www.calcalistech.com/ctechnews/article/6wcqhdv35) — fetched 2026-06-28 — supports: >$105M reported value; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by Tenable** (announced 2025-05-29, >$105M reported, into Tenable One H2 2025). Seed flag verified. Filled founding (2023), Tel Aviv HQ, founders, investor list (Altman/Sequoia/Index), AI-exposure-management positioning. Confidence high.
</content>
