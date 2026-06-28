---
title: Aim Security
type: vendor
name: Aim Security
slug: aim-security
categories: [ai-runtime-security, ai-spm]
layer: model-prompt
aliases: [Aim, Aim Labs]
website: "https://www.aim.security"
founded: 2022
hq: Tel Aviv, Israel
ownership: acquired
ownership_detail: "Acquired by [cato-networks](cato-networks.md) — announced 2025-09-03 (~$350M reported), Cato's first acquisition; being integrated into Cato SASE Cloud"
ownership_confidence: high
funding_total: ~$28M (Series A; pre-acquisition)
last_funding: "$10M Series A extension / ~$18M Series A (YL Ventures, Canaan Partners)"
deployment: [saas, api, inline-proxy]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [acquired, ai-firewall, shadow-ai, ai-spm, unit-8200]
---

# Aim Security

> **Researched 2026-06-28.** Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [cato-networks](cato-networks.md)** (announced 2025-09-03).

**One-liner** — An enterprise AI-security pure-play (AI firewall + shadow-AI control + AI-SPM) bought by SASE vendor [cato-networks](cato-networks.md) in its first-ever acquisition.

## What it does
Aim secures enterprise AI across three jobs: (1) **securing employee use of public AI apps** — shadow-AI discovery and policy (CASB-for-AI / [ai-access-governance](../categories/ai-access-governance.md)); (2) **protecting private AI apps and agents** via an inline **AI Firewall** that screens prompts/responses for prompt injection, data leakage and abuse ([ai-runtime-security](../categories/ai-runtime-security.md)); and (3) **securing the AI development lifecycle** via AI Security Posture Management — discovering and governing the AI assets an org builds ([ai-spm](../categories/ai-spm.md)). It targeted Fortune 500 / Global 2000 buyers. Aim's research team is also known publicly for AI vulnerability discovery (e.g., "EchoLeak"-class agent/Copilot exploits).

## Where it sits in the stack
Primary [ai-runtime-security](../categories/ai-runtime-security.md) (the AI firewall) with a secondary [ai-spm](../categories/ai-spm.md) tag (posture management); also overlaps [ai-access-governance](../categories/ai-access-governance.md) (shadow AI). Layer: model-prompt. Lethal-trifecta role: covers all three legs — **untrusted input** (prompt-injection defense), **sensitive data** (DLP on AI traffic), **egress** (governing what leaves to public AI). Sits at the green↔red boundary.

## Deployment & architecture
SaaS with API and inline deployment in front of AI apps/agents; post-acquisition it is being integrated natively into the [cato-networks](cato-networks.md) SASE Cloud, so AI controls ride Cato's inline backbone alongside SD-WAN/SSE rather than as a standalone proxy. Integrations: IdP, SIEM, the enterprise's AI gateways and SaaS estate.

## Positioning & differentiators
Aim covered the full enterprise-AI-security span (shadow AI + runtime firewall + AI-SPM) in one product rather than picking a single slice — that breadth is part of why a SASE vendor bought it to instantly fill its AI-security line. Founded by [[Unit 8200]] veterans, backed by [[YL Ventures]] and Canaan Partners. Nearest neighbors: [witnessai](witnessai.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md), [prisma-airs](prisma-airs.md), [harmonic-security](harmonic-security.md), [zenity](zenity.md).

## Ownership, funding & M&A
Founded **2022** (HQ **Tel Aviv**, US presence in New York) by Unit 8200 veterans (Matan Getz, CEO; Adir Gruss, CTO). VC-backed by YL Ventures and Canaan Partners (~$28M raised across seed + Series A pre-acquisition; exact total not itemized in sources — noted as unknown-precise). **Acquired by [cato-networks](cato-networks.md)** — announced **2025-09-03**; value not officially disclosed, press reports ~$350M. This is Cato's first acquisition. Verified against Cato's press release and corroborating press; confirms the seed flag ("acq by Cato"). **Confidence: high.**

## CTO / hedge-fund lens
Day-1 control type (AI firewall + shadow-AI), but as an absorbed product you'd now evaluate it as part of the [cato-networks](cato-networks.md) SASE platform. Most relevant to Cato customers or shops choosing SASE who want AI security native. Indirect SR 11-7 relevance (control point, plus AI-asset inventory from AI-SPM has mild model-governance value). Fits enterprises consolidating on SASE; standalone-Aim is no longer the buying unit.

## Competitors / alternatives
[witnessai](witnessai.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [harmonic-security](harmonic-security.md), [zenity](zenity.md).

## Open questions / to verify
- Precise total funding (sources cite YL Ventures/Canaan backing; figure ~$28M approximate).
- Official deal value (press ~$350M; not disclosed by Cato).
- Whether the Aim brand survives inside Cato or is fully absorbed.

## Sources
- [Cato Networks Acquires Aim Security… (Cato press release)](https://www.catonetworks.com/news/cato-acquires-aim-security-to-extend-sase-leadership-and-secure-enterprise-ai-transformation/) — fetched 2026-06-28 — supports: acquirer, 2025-09-03, Aim's three capabilities, founding 2022, YL/Canaan backing; confidence: high
- [Cato Networks acquires AI security startup Aim Security (CyberScoop)](https://cyberscoop.com/cato-networks-acquires-ai-security-startup-aim-security/) — fetched 2026-06-28 — supports: ~$350M reported value, Unit 8200 founders; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by [cato-networks](cato-networks.md)** (announced 2025-09-03, ~$350M reported, Cato's first acquisition). Seed flag verified. Filled founding (2022), Tel Aviv HQ, YL/Canaan backing, three-part product. Confidence raised to high.
</content>
