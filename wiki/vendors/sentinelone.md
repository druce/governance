---
type: vendor
name: SentinelOne
slug: sentinelone
categories: [edr-xdr, ai-runtime-security, ai-spm]
layer: foundation
aliases: [Singularity, SentinelOne Inc.]
website: https://www.sentinelone.com
founded: 2013
hq: Mountain View, California, USA
ownership: public
ownership_detail: "Public — NYSE: S (IPO June 2021). Acquirer: Prompt Security (GenAI runtime/DLP, announced 2025-08-05, ~$250M) and Observo AI (data pipeline)."
ownership_confidence: high
funding_total: n/a (public)
last_funding: IPO June 2021 (NYSE: S)
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 3
last_updated: 2026-06-28
tags: [edr, xdr, singularity, purple-ai, ai-security, genai]
---

# SentinelOne

> Primary category: [edr-xdr](../categories/edr-xdr.md). Also [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-spm](../categories/ai-spm.md) (via the Prompt Security acquisition).

**One-liner** — The main publicly traded EDR/XDR challenger to [crowdstrike](crowdstrike.md) and [microsoft-defender](microsoft-defender.md), whose Singularity platform now extends into GenAI security after acquiring [prompt-security](prompt-security.md).

## What it does
SentinelOne's Singularity is an autonomous, AI-driven endpoint/extended detection and response platform ([edr-xdr](../categories/edr-xdr.md)), spanning endpoint, cloud, identity, and data/SIEM (via the Scalyr acquisition), with **Purple AI** as its agentic SOC analyst. In 2025 it moved into AI security by acquiring **Prompt Security**, adding GenAI runtime protection — shadow-AI discovery, prompt-injection defense, and data-leakage prevention across browsers, desktop apps, and APIs — which maps to [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-spm](../categories/ai-spm.md).

## Where it sits in the stack
Foundation layer for its core ([edr-xdr](../categories/edr-xdr.md), with SIEM/[siem-soc](../categories/siem-soc.md) and agentic SOC adjacency). With Prompt Security folded in, it reaches the model/prompt layer ([ai-runtime-security](../categories/ai-runtime-security.md), [ai-spm](../categories/ai-spm.md), [ai-access-governance](../categories/ai-access-governance.md)), addressing the **untrusted-input** (prompt injection) and **egress/sensitive-data** legs of the lethal trifecta. Spans green (managed endpoints) into yellow (AI app usage) trust zones.

## Deployment & architecture
SaaS control plane with a single autonomous endpoint agent; API-first. Prompt Security's protection runs across browser, desktop, and API channels — relevant for governing workforce GenAI use without an inline network proxy. Integrates with SIEM/SOC, IdP, and cloud platforms.

## Positioning & differentiators
- Positions as the autonomous/AI-native EDR alternative to [crowdstrike](crowdstrike.md); usually the #2 considered in EDR bake-offs alongside [microsoft-defender](microsoft-defender.md).
- Its AI-security M&A mirrors CrowdStrike's almost beat-for-beat: SentinelOne bought [prompt-security](prompt-security.md) (GenAI runtime) the way CrowdStrike bought [pangea](pangea.md).
- For the AI-security overlap, nearest neighbors are [prompt-security](prompt-security.md) (now itself), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md).

## Ownership, funding & M&A
Public company, NYSE: S, IPO June 2021; HQ Mountain View, CA; founded 2013 (Tomer Weingarten et al.). The seed flagged "acq Prompt Security" — **CONFIRMED**: announced 2025-08-05, combination of cash and stock, reported ~$250M (Calcalist; not officially disclosed), expected to close in fiscal Q3 FY2026 (SentinelOne later announced completion). Same announcement also covered the **Observo AI** (data pipeline) acquisition. See [prompt-security](prompt-security.md). Confidence: high on the deal; medium on price.

## CTO / hedge-fund lens
Day-1 foundational as an EDR/XDR option — the leading independent alternative if you don't want CrowdStrike or Defender. The GenAI-security additions (Prompt Security, Purple AI) are a Day-2 consolidation benefit attractive to existing SentinelOne shops wanting AI runtime guardrails from their EDR vendor. Not an SR 11-7/model-risk governance tool; it's security infrastructure. Fits enterprise and mid-market.

## Competitors / alternatives
[crowdstrike](crowdstrike.md), [microsoft-defender](microsoft-defender.md), [palo-alto-networks](palo-alto-networks.md) (Cortex), [cisco](cisco.md). AI-security overlap: [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [pangea](pangea.md).

## Open questions / to verify
- Final Prompt Security purchase price (press-reported ~$250M) and confirmed close date.
- How Prompt Security's standalone product is packaged within Singularity going forward.

## Sources
- [SentinelOne to Acquire Prompt Security to Advance GenAI Security](https://www.sentinelone.com/press/sentinelone-to-acquire-prompt-security-to-advance-genai-security/) — fetched 2026-06-28 — supports: Prompt Security acquisition (2025-08-05), GenAI runtime rationale, fiscal Q3 close; confidence: high
- [SentinelOne buys Prompt for $250M (Calcalist)](https://www.calcalistech.com/ctechnews/article/im5ma59bu) — fetched 2026-06-28 — supports: ~$250M deal value; confidence: med
- [SentinelOne IR / corporate facts](https://investors.sentinelone.com/) — fetched 2026-06-28 — supports: public (NYSE: S), founded 2013, HQ Mountain View; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed SentinelOne is public (NYSE: S, IPO 2021, founded 2013, Mountain View) and is the ACQUIRER — fixed ownership from `acquired` to `public`. CONFIRMED Prompt Security acquisition (announced 2025-08-05, ~$250M, close fiscal Q3 FY2026); noted Observo AI acquisition. Filled founding/HQ/deployment; set hedge_fund_fit high.
