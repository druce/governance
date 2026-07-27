---
title: Apex Security
type: vendor
name: Apex Security
slug: apex-security
aka: [Apex, Apex AI Security, Tenable One AI Exposure, Tenable AI Exposure]
primary_category: agent-runtime-security
also_listed_in: []
website: https://www.tenable.com/products/ai-exposure
founded: 2023
hq: Tel Aviv, Israel
ownership_state: acquired-closed
owner: Tenable
ownership_note: 'Acquired by Tenable (NASDAQ: TENB) — announced 2025-05-29, closed June 2025 (per Tenable 10-Q for Q2 2025); total consideration $47.8M. Brand fully retired: apexsec.com is dead (404 / parked domain-for-sale) and the technology now ships as Tenable One AI Exposure (GA 2026-01-27).'
acquisition: {announced: 2025-05-29, closed: 2025-06, price: $47.8M}
funding_total: ~$25M (pre-acquisition; seed + Series A)
last_funding: Series A (backers incl. Sam Altman, Sequoia Capital, Index Ventures)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [acquired, ai-spm, shadow-ai, agent-security, exposure-management]
sources:
  - {claim: "Acquisition closed June 2025; total consideration $47.8M ($47.7M cash net of $2.0M cash acquired + $0.1M replacement equity); Apex proprietary technology booked at $6.8M, goodwill $41.3M", url: "https://www.sec.gov/Archives/edgar/data/1660280/000166028025000090/tenb-20250630.htm", date: 2026-07-27, confidence: high}
  - {claim: "Apex brand retired; technology ships as Tenable One AI Exposure, GA announced 2026-01-27; apexsec.com dead (404 / parked domain-for-sale)", url: "https://www.tenable.com/products/ai-exposure", date: 2026-07-27, confidence: high}
---

# Apex Security

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). **Acquired by Tenable — closed June 2025.** The Apex brand is retired: apexsec.com no longer resolves, and the product now ships as **Tenable One AI Exposure** (GA 2026-01-27). This page is kept as the provenance record for the acquired technology; the buying unit is Tenable One.

**One-liner** — An AI-attack-surface / AI-governance startup (discover ungoverned AI, enforce policy, govern agents), acquired by exposure-management vendor Tenable in June 2025 and now sold as Tenable One AI Exposure.

## What it does
Apex secured the AI attack surface: it discovered **ungoverned / shadow AI** (apps, AI-generated code, AI identities), enforced policy on AI usage, and controlled exposure across both the AI tools an organization *uses* and the AI systems it *builds* — including governance/runtime control of AI agents. The pitch was visibility + control over everything AI in the enterprise, mapped into a security/exposure view.

As **Tenable One AI Exposure** the same capability set is now sold inside Tenable's exposure-management platform: discover AI platform usage across SaaS, cloud, APIs and agents; see who is using AI, with what intent, and what data is exchanged; find unsafe AI platform settings, agent configurations and third-party integrations; detect and block AI-specific attacks (direct and **indirect prompt injection**, jailbreaks) and contain risky or compromised agents. At GA (2026-01-27) coverage was scoped to **OpenAI ChatGPT Enterprise, Microsoft Copilot, Microsoft 365 Copilot and Studio Copilot**, with Google Gemini signalled as forthcoming — narrower than the "all AI platforms" framing of the acquisition-era messaging, and worth checking against your actual AI estate.

## Where it sits in the stack
Primary [agent-runtime-security](../categories/agent-runtime-security.md) (runtime governance of agentic AI) with strong overlap into [ai-spm](../categories/ai-spm.md) (AI discovery/posture) and [ai-access-governance](../categories/ai-access-governance.md) (shadow AI). Layer: model-prompt. Lethal-trifecta role: as a governance/visibility + policy layer it touches all three legs indirectly — flagging risky **untrusted-input** exposure, **sensitive-data** handling, and AI **egress**. Post-acquisition it is the AI lens of Tenable's exposure-management view — and the GA product does claim direct/indirect prompt-injection and jailbreak detection, not just posture reporting.

## Deployment & architecture
SaaS / API-based discovery and policy enforcement across the AI estate (used tools + built systems). Following close, capabilities ship as part of **Tenable One**, Tenable's unified exposure-management platform — adding AI visibility, context and control alongside vuln/asset exposure data. Tenable describes AI Exposure as **agentless** and deployable "in minutes" (SaaS-side API integrations against the AI platforms, not an inline proxy). There is no standalone Apex deployment left to buy. Integrations: the enterprise SaaS/AI estate, IdP, Tenable One.

## Positioning & differentiators
Apex's angle was breadth across "AI you use and AI you build" framed as **exposure management** rather than a single inline firewall — which is exactly why an exposure-management leader (Tenable) acquired it to extend Tenable One into AI. Notable for a marquee investor list. That thesis survived the integration: the differentiator today is **not** best-of-breed agent runtime enforcement but *co-location* — AI risk scored in the same exposure graph as vulns, cloud and identity, for shops already standardized on Tenable One. Against pure-plays in this category that is a consolidation play, not a depth play; the SaaS-platform-scoped GA coverage (ChatGPT Enterprise + Copilot family) is the practical limit. Nearest neighbors: [zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md), [noma-security](noma-security.md), [quilr](quilr.md), [reco](reco.md), [nudge-security](nudge-security.md).

## Ownership, funding & M&A
Founded **2023** by Matan Derman (CEO) and Tomer Avni (CPO); Israeli startup (HQ Tel Aviv). Backed by a high-profile group — **Sam Altman**, Clem Delangue (Hugging Face), **Sequoia Capital**, **Index Ventures** (~$25M raised across seed + Series A; exact total not itemized in sources). **Acquired by Tenable** (NASDAQ: TENB) — intent announced **2025-05-29**, deal **closed in June 2025**.

Close and price are confirmed from Tenable's **Form 10-Q for Q2 2025** (Note 6): Tenable acquired 100% of Apex Security, Inc.'s equity by share purchase agreement for **total consideration of $47.8M** — $47.7M cash net of $2.0M cash acquired, plus $0.1M fair value of replacement equity — allocated as $6.8M intangibles (Apex proprietary technology, 5-year life) and $41.3M goodwill. The 10-Q gives month precision only ("In June 2025"); Tenable filed no separate close 8-K, the deal being immaterial at that size.

> Contradiction (soft, resolved): Calcalist and follow-on trade press reported the deal at **">$105M"**; Tenable's 10-Q reports **$47.8M** total consideration. The SEC figure is authoritative for consideration transferred — the press number most likely folded in retention/incentive packages, which are compensation expense rather than purchase price under ASC 805. This page uses $47.8M. Resolved 2026-07-27.

**Confidence: high** (primary SEC filing).

## CTO / hedge-fund lens
Day-2 (AI posture/governance is something you layer on after baseline controls). Relevant mainly if you are a **Tenable shop** doing exposure management and want AI assets in the same risk picture — shadow-AI discovery + agent governance has real value for a fund worried about ungoverned AI usage. Mild SR 11-7 relevance (AI inventory/governance supports model-risk documentation). Standalone Apex is no longer the buying unit and there is no Apex contract, pricing or support path to evaluate: this is a **Tenable One module**, so it inherits Tenable commercials, renewal cycle and roadmap. If you are not already on Tenable One, adopting this means adopting the platform. Check the supported-platform list (ChatGPT Enterprise + Copilot family at GA) against what your firm actually runs before treating it as coverage — a Claude/Gemini/Bedrock-heavy shop was not in scope at GA.

## Competitors / alternatives
[zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md), [noma-security](noma-security.md), [quilr](quilr.md), [reco](reco.md), [nudge-security](nudge-security.md), [wiz](wiz.md).

## Open questions / to verify
- **Exact close date** — the 10-Q says only "In June 2025"; no day-level date is published in any primary source found. Left at month precision rather than guessed.
- Precise total funding (sources cite the investor list; ~$25M approximate).
- Whether AI Exposure is a separately-priced Tenable One module or bundled — Tenable does not publish pricing.
- Whether Google Gemini / Anthropic Claude / self-hosted-model coverage has shipped since GA (signalled as "forthcoming" at 2026-01-27).

## Sources
- [Tenable Announces Intent to Acquire Apex Security (Tenable press release)](https://www.tenable.com/press-releases/tenable-announces-intent-to-acquire-apex-security-to-expand-exposure-management-across-the-ai-attack-surface) — fetched 2026-06-28 — supports: 2025-05-29 announce, Apex capabilities, founders, founding 2023, investor list, Tenable One integration, Q2 2025 close; confidence: high
- [Tenable acquires Sam Altman-backed Apex for over $105 million (Calcalist)](https://www.calcalistech.com/ctechnews/article/6wcqhdv35) — fetched 2026-06-28 — supports: >$105M *reported* value; superseded by the 10-Q on price; confidence: low
- [Tenable Holdings, Inc. Form 10-Q, quarter ended 2025-06-30, Note 6 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1660280/000166028025000090/tenb-20250630.htm) — fetched 2026-07-27 — supports: **close in June 2025**, total consideration $47.8M, purchase price allocation; confidence: high
- [Tenable One AI Exposure product page](https://www.tenable.com/products/ai-exposure) — fetched 2026-07-27 — supports: live successor URL, product name, capabilities, supported AI platforms; confidence: high
- [Tenable Extends Exposure Management to AI Attack Surface (press release, 2026-01-27)](https://www.tenable.com/press-releases/tenable-extends-exposure-management-to-AI-attack-surface) — fetched 2026-07-27 — supports: GA of Tenable One AI Exposure on 2026-01-27; confidence: high
- [Introducing Tenable AI Exposure (Tenable blog, 2025-08-06)](https://www.tenable.com/blog/introducing-tenable-ai-exposure-stop-guessing-start-securing-your-ai-attack-surface) — fetched 2026-07-27 — supports: private-preview launch date, agentless architecture, prompt-injection/jailbreak detection; confidence: high
- Cached: [raw/sources/2026-07-27--apex-security--tenable-close-and-ai-exposure.md](../../raw/sources/2026-07-27--apex-security--tenable-close-and-ai-exposure.md)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by Tenable** (announced 2025-05-29, >$105M reported, into Tenable One H2 2025). Seed flag verified. Filled founding (2023), Tel Aviv HQ, founders, investor list (Altman/Sequoia/Index), AI-exposure-management positioning. Confidence high.
- [2026-07-27] URL audit found **apexsec.com dead** (404 on apex/www; audit also observed a 302 to a HugeDomains "for sale" parking page, $15,595) — the Apex domain has lapsed entirely. Re-researched: **acquisition CLOSED June 2025**, confirmed from Tenable's Q2 2025 Form 10-Q, at **$47.8M total consideration** — which *contradicts* the >$105M press figure carried since 2026-06-28; resolved in favor of the SEC filing (see M&A section). Product resurfaced as **Tenable One AI Exposure**: private preview 2025-08-06, **GA 2026-01-27**. `ownership_state` acquired-pending → **acquired-closed**; `website` → https://www.tenable.com/products/ai-exposure; `verify_after` cleared; aka + body updated for the rebrand.
</content>
