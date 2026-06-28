---
type: vendor
name: Cranium
slug: cranium
categories: [ai-spm, ai-governance-platform]
layer: model-prompt
aliases: [Cranium AI]
website: "https://cranium.ai"
founded: 2023
hq: Short Hills, New Jersey, USA
ownership: independent
ownership_detail: KPMG Studio spinout (first KPMG tech spinout); VC-backed. ACQUIRER of Aiceberg (2026-05-21), not acquired.
ownership_confidence: high
funding_total: ~$32M
last_funding: Series A $25M (2023-10)
deployment: [saas, api]
target_customer: enterprise / regulated (security, compliance, third-party AI trust)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [ai-spm, ai-governance, compliance, supply-chain, kpmg]
---

# Cranium

> Primary category: [ai-spm](../categories/ai-spm.md). Also spans [ai-governance-platform](../categories/ai-governance-platform.md).

**One-liner** — An enterprise AI security + governance platform that inventories your AI/ML systems, assesses their risk and compliance posture, and documents trust for internal and third-party AI.

## What it does
Cranium helps an organization **map, monitor, and manage** its AI/ML estate against adversarial threats "without interrupting how teams train, test, and deploy." It builds an AI inventory, runs security-risk and exposure assessments, and ties findings to compliance frameworks (NIST AI RMF, EU AI Act, etc.). A distinctive piece is **AI Cards** / third-party AI trust — documenting and exchanging the security posture of AI systems with customers and across the supply chain. So it straddles posture (AI-SPM) and governance/compliance evidence.

## Where it sits in the stack
Primary [ai-spm](../categories/ai-spm.md) (discover + assess + monitor AI assets), with heavy overlap into [ai-governance-platform](../categories/ai-governance-platform.md) (compliance mapping, model documentation, third-party AI trust). Layer: model/prompt, reaching up into the governance layer. Lethal-trifecta role is indirect — it reduces exposure by finding weak/untrusted AI surfaces and risky data handling, rather than blocking traffic inline. More a posture/governance tool than a runtime control.

## Deployment & architecture
SaaS platform with API connectors to discover and assess AI/ML systems across the enterprise; produces reports, AI Cards, and compliance artifacts. Not an inline proxy or runtime firewall in its core form — though the 2026 Aiceberg acquisition adds agentic-AI runtime/risk capabilities (see below).

## Positioning & differentiators
Known for the **KPMG pedigree** (incubated in KPMG Studio; KPMG is investor and go-to-market channel) and for the **AI-trust / AI Cards / supply-chain** angle — quantifying and sharing third-party AI risk, which fits TPRM and audit workflows more than a pure security tool. Differs from posture-plus-runtime players like [noma-security](noma-security.md) and [zenity](zenity.md) (more runtime/agent focus) and from governance-first platforms like [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), and [ibm-watsonx-governance](ibm-watsonx-governance.md) (policy/model-risk first). Cranium tries to bridge security posture and governance evidence in one place.

## Ownership, funding & M&A
Independent, VC-backed. Founded 2023 by Jonathan Dambrot (CEO), Daniel Christman, Felix Knoll, and Paul Spicer; the **first technology spinout from KPMG Studio**. **Series A $25M (Oct 2023) led by Titanium Ventures** with KPMG LLP and SYN Ventures; ~$32M total.

**M&A (verified):** On **2026-05-21 Cranium acquired Aiceberg**, an agentic-AI security and risk-management company, to extend toward end-to-end coverage including AI agents. **Cranium is the acquirer and remains independent** — not itself acquired. (No "Cranium acquired" flag existed in the seed; confirmed direction against the BusinessWire release.) Ownership confidence: high.

## CTO / hedge-fund lens
**Day-2**, and skews toward the **governance/compliance** buyer rather than the SOC. If your driver is SR 11-7 model-risk evidence, EU AI Act / NIST AI RMF documentation, and third-party AI vendor risk (which AI is in your supply chain and is it trustworthy), Cranium's AI-Cards/trust framing is its strongest hedge-fund hook. If your driver is blocking prompt injection at runtime, look at runtime players instead. Mid-to-large regulated shops get the most out of it.

## Competitors / alternatives
[noma-security](noma-security.md), [zenity](zenity.md), [reco](reco.md), [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), [modelop](modelop.md), [ibm-watsonx-governance](ibm-watsonx-governance.md), [onetrust](onetrust.md).

## Open questions / to verify
- What Aiceberg adds in practice (agent runtime vs risk scoring) and how it changes deployment.
- Whether Cranium offers any inline/runtime enforcement post-acquisition or stays posture/governance-only.
- Current total funding after 2023 (any undisclosed rounds before the Aiceberg deal).

## Sources
- [Cranium Raises $25M Series A (cranium.ai)](https://cranium.ai/resources/press-release/cranium-series-a-funding-to-secure-ai/) — fetched 2026-06-28 — supports: founding, KPMG Studio spinout, Series A $25M/Titanium Ventures, HQ, product; confidence: high (vendor release).
- [Cranium AI Acquires Aiceberg (BusinessWire)](https://www.businesswire.com/news/home/20260521627247/en/Cranium-AI-Acquires-Aiceberg-to-Strengthen-its-End-to-End-AI-Security-Governance-and-Agentic-AI-Platform) — fetched 2026-06-28 (search snapshot; direct fetch timed out) — supports: Cranium acquired Aiceberg 2026-05-21, agentic AI; confidence: medium.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent KPMG Studio spinout (2023), Series A $25M (2023-10, Titanium Ventures), Short Hills NJ. Verified Cranium is the ACQUIRER of Aiceberg (2026-05-21), not acquired. Set ownership_confidence high.
