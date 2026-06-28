---
type: vendor
name: CrowdStrike
slug: crowdstrike
categories: [edr-xdr, siem-soc, ai-soc-analysts, ai-red-teaming]
layer: foundation
aliases: [Falcon, CrowdStrike Holdings]
website: https://www.crowdstrike.com
founded: 2011
hq: Austin, Texas, USA
ownership: public
ownership_detail: "Public — NASDAQ: CRWD (IPO 2019). Acquirer: Adaptive Shield (SSPM, closed ~Jan 2025) and Pangea (AI prompt-layer/AIDR, completed ~Sept 2025)."
ownership_confidence: high
funding_total: n/a (public)
last_funding: IPO June 2019 (NASDAQ: CRWD)
deployment: [saas, api]
target_customer: enterprise / mid-market / regulated
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 4
last_updated: 2026-06-28
tags: [edr, xdr, siem, soc, ai-security, falcon]
---

# CrowdStrike

> Primary category: [[edr-xdr]]. Also [[siem-soc]], [[ai-soc-analysts]], and (via Pangea) [[ai-red-teaming]] / AI runtime security.

**One-liner** — The dominant cloud-native endpoint protection (EDR/XDR) vendor, whose Falcon platform has expanded into SIEM, cloud, identity, an agentic SOC analyst (Charlotte AI), and — via the Pangea acquisition — AI prompt-layer security ("AI Detection and Response").

## What it does
CrowdStrike's Falcon is a single-agent, cloud-delivered security platform. Its core is best-in-class [[edr-xdr]] (endpoint/extended detection and response), but it now spans next-gen SIEM (Falcon LogScale, see [[crowdstrike-logscale]]), cloud security (CNAPP), identity threat detection, exposure management, and a SOC-automation layer. For a CTO, it is the "if you already own one security platform, it's probably this or [[microsoft-defender]]" incumbent.

In 2024–2025 CrowdStrike pushed hard into AI security on two fronts: **Charlotte AI**, an internally built agentic SOC analyst (see [[ai-soc-analysts]]), and the **Pangea** acquisition, which adds AI prompt-layer guardrails and what CrowdStrike brands as the industry's first complete **AI Detection and Response (AIDR)** — securing data, models, agents, identities, and AI interactions across the AI lifecycle.

## Where it sits in the stack
Foundation layer. Falcon is endpoint/identity/cloud telemetry and response ([[edr-xdr]], [[siem-soc]], [[ai-soc-analysts]]). With Pangea folded in, CrowdStrike also reaches into the model/prompt layer ([[ai-runtime-security]] / [[ai-red-teaming]]), addressing the **untrusted-input** (prompt injection) and **egress/sensitive-data** legs of the lethal trifecta at the AI interaction layer. It spans the green (managed endpoints) and is extending into the yellow (AI app) trust zones.

## Deployment & architecture
SaaS control plane with a lightweight single endpoint agent; API-first for integrations. Pangea's AI guardrails deploy via gateway or are embedded in applications with a few lines of code (API/SDK). Integrates with SIEM/SOC workflows natively (it *is* a SIEM via LogScale), IdP, and cloud providers.

## Positioning & differentiators
- Market-leading EDR/XDR brand; very broad single-agent platform consolidation play.
- Charlotte AI (agentic triage) competes with [[ai-soc-analysts]] pure-plays like [[prophet-security]], [[dropzone-ai]], [[radiant-security]].
- AIDR via Pangea positions it against [[sentinelone]] (which bought [[prompt-security]]), [[prisma-airs]] (Palo Alto), [[cisco-ai-defense]], and AI-runtime pure-plays ([[hiddenlayer]], [[witnessai]], [[lakera]]).
- Nearest neighbor is [[microsoft-defender]] (bundled-with-E5 economics) and [[sentinelone]] (challenger with a near-identical AI-security M&A playbook).

## Ownership, funding & M&A
Public company, NASDAQ: CRWD, IPO June 2019; HQ Austin, TX; founded 2011 (George Kurtz et al.). The seed flagged it as "acquirer (Pangea, Charlotte AI internal)" — **confirmed**:
- **Pangea** — acquisition announced 2025-09-16 at Fal.Con 2025; reported ~$260M; completed ~September 2025. Adds AI prompt-layer security / AIDR. (Confidence: high on the deal; medium on exact close date and price, which were press-reported not officially disclosed.)
- **Adaptive Shield** — announced 2024-11-06 at Fal.Con Europe; reported ~$300M; closed ~January 2025. Adds [[sspm]] / GenAI SaaS posture. (See [[adaptive-shield]].)
- **Charlotte AI** is internally built, not an acquisition — confirmed.
- Falcon LogScale comes from the earlier Humio acquisition (2021).

## CTO / hedge-fund lens
Day-1 foundational. Most funds of any size already run CrowdStrike or Defender for endpoint; it's table-stakes EDR. The AI-security additions (Charlotte AI, Pangea/AIDR) are a Day-2 consolidation convenience — attractive if you're already a Falcon shop and want AI guardrails from an incumbent rather than a pure-play. Not specifically an SR 11-7/model-risk tool; it's security infrastructure, not model governance. Fits enterprise and serious mid-market; arguably heavy for a very small fund that could lean on Defender bundled with M365.

## Competitors / alternatives
[[microsoft-defender]], [[sentinelone]], [[palo-alto-networks]] (Cortex), [[cisco]]. For the AI-security overlap: [[prompt-security]], [[prisma-airs]], [[cisco-ai-defense]], [[pangea]] (now part of CrowdStrike).

## Open questions / to verify
- Exact Pangea close date and final purchase price (press-reported ~$260M; not officially disclosed).
- How Pangea's standalone product survives vs. being absorbed into Falcon AIDR.

## Sources
- [CrowdStrike to Acquire Pangea to Secure Every Layer of Enterprise AI](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-pangea-to-secure-every-layer-of-enterprise-ai/) — fetched 2026-06-28 — supports: Pangea acquisition date (2025-09-16), AIDR rationale; confidence: high
- [CrowdStrike Buys Pangea for $260M (BankInfoSecurity)](https://www.bankinfosecurity.com/crowdstrike-buys-pangea-for-260m-to-guard-enterprise-ai-use-a-29480) — fetched 2026-06-28 — supports: ~$260M deal value; confidence: med
- [CrowdStrike and Adaptive Shield Unify Cloud and Identity with SaaS Protection](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-acquires-adaptive-shield-and-integrates-saas-protection/) — fetched 2026-06-28 — supports: Adaptive Shield acquisition (2024-11-06); confidence: high
- [CrowdStrike IR / corporate facts](https://ir.crowdstrike.com/) — fetched 2026-06-28 — supports: public (CRWD), founded 2011, HQ Austin; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed CrowdStrike is public (NASDAQ: CRWD, founded 2011, Austin TX) and is the ACQUIRER, not acquired — fixed ownership from `acquired` to `public`. Verified Pangea acquisition (announced 2025-09-16, ~$260M, completed ~Sept 2025) and Adaptive Shield (announced 2024-11-06, ~$300M, closed ~Jan 2025); Charlotte AI confirmed internally built. Filled founding/HQ/deployment; set hedge_fund_fit high.
