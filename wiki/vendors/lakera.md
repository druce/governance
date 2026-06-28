---
type: vendor
name: Lakera
slug: lakera
categories: [ai-runtime-security, ai-red-teaming]
layer: model-prompt
aliases: [Lakera AI, Lakera Guard]
website: "https://www.lakera.ai"
founded: 2021
hq: Zurich, Switzerland (and San Francisco, USA)
ownership: acquired
ownership_detail: "Acquired by Check Point Software (NASDAQ: CHKP) — announced 2025-09-16 (~$300M reported), expected close Q4 2025; to anchor Check Point's Global Center of Excellence for AI Security"
ownership_confidence: high
funding_total: ~$30M
last_funding: "$20M Series A — July 2024 (led by Atomico; Citi Ventures, Dropbox, redalpine)"
deployment: [saas, api, self-hosted]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [acquired, ai-firewall, prompt-injection, gandalf, red-teaming]
---

# Lakera

> **Researched 2026-06-28.** Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by Check Point Software** (announced 2025-09-16; expected close Q4 2025).

**One-liner** — An AI-native runtime-security pure-play (real-time prompt-injection / GenAI defense, of "Gandalf" fame) being acquired by Check Point to anchor its AI-security stack.

## What it does
Lakera protects LLMs, GenAI apps and autonomous/agentic systems at runtime. Its core product, **Lakera Guard**, screens inputs and outputs in real time against prompt injection, jailbreaks, data leakage, and model manipulation across multiple AI frameworks. Its threat intelligence is fed partly by **Gandalf**, a viral prompt-injection education game (>1M players; >50M data points) used even by Microsoft for security training. Lakera also does AI red teaming.

## Where it sits in the stack
Primary [ai-runtime-security](../categories/ai-runtime-security.md) (inline AI firewall / guardrails) with a secondary [ai-red-teaming](../categories/ai-red-teaming.md) tag. Layer: model-prompt. Lethal-trifecta role: strongest on **untrusted input** (it is the best-known prompt-injection defender) and **sensitive data** (output/data-leak screening). Sits at the green↔red boundary in front of model endpoints.

## Deployment & architecture
SaaS and self-hosted; primarily **API-based** (low-latency guardrail calls around model requests) plus SDK integration — model- and cloud-agnostic. On close, Lakera will combine with Check Point Infinity / GenAI Protect and form the foundation of Check Point's **Global Center of Excellence for AI Security**. Integrations: AI gateways, the app's LLM pipeline, SIEM.

## Positioning & differentiators
Lakera is the category's best-known **prompt-injection** specialist, with a research-and-community moat (Gandalf, an open prompt-injection dataset) and a lightweight API-first guardrail rather than a heavy inline proxy. Founders came from Google/Meta AI. Nearest neighbors: [prompt-security](prompt-security.md), [calypsoai](calypsoai.md), [witnessai](witnessai.md), [aim-security](aim-security.md), [prisma-airs](prisma-airs.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [hiddenlayer](hiddenlayer.md).

## Ownership, funding & M&A
Founded **2021** by David Haber (CEO), Dr. Mateo Rojas-Carulla and Dr. Matthias Kraft; dual HQ **Zurich + San Francisco**. Funding **~$30M total**, headlined by a **$20M Series A (July 2024)** led by Atomico (Citi Ventures, Dropbox, redalpine). **Acquired by Check Point Software** (NASDAQ: CHKP) — announced **2025-09-16**; deal value not disclosed, press reports ~$300M; expected to **close Q4 2025**. Verified against Check Point's own press release and corroborating press; confirms the seed flag ("acq by Check Point"). **Confidence: high** (note: at research date the close is announced/pending per the release — treat as agreed, closing Q4 2025).

## CTO / hedge-fund lens
Day-1 control type — a runtime AI firewall focused on prompt injection is a baseline control for any shop exposing LLMs to untrusted input. Lakera's API-first model suits teams that want guardrails in code without standing up an inline proxy. Indirect SR 11-7 relevance (control + red-team evidence). Post-acquisition, Check Point customers get it natively; standalone buyers should weigh whether it stays available outside the Check Point platform. Good fit for funds building their own LLM apps/agents.

## Competitors / alternatives
[prompt-security](prompt-security.md), [calypsoai](calypsoai.md), [witnessai](witnessai.md), [aim-security](aim-security.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [hiddenlayer](hiddenlayer.md).

## Open questions / to verify
- Confirm the deal **closed** (announced 2025-09-16, expected Q4 2025) — verify completion date when available.
- Official deal value (press ~$300M; not disclosed).
- Whether Lakera Guard remains available standalone post-integration.

## Sources
- [Check Point Acquires Lakera… (Check Point press release)](https://www.checkpoint.com/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/) — fetched 2026-06-28 — supports: 2025-09-16 announce, founders, founding 2021, Zurich/SF HQ, Center of Excellence integration, Q4 2025 close; confidence: high
- [Lakera raises $20M Series A (TechCrunch)](https://techcrunch.com/2024/07/24/lakera-which-protects-enterprises-from-llm-vulnerabilities-raises-20m/) — fetched 2026-06-28 — supports: $20M Series A, ~$30M total, Atomico lead, Gandalf; confidence: high
- [Check Point acquires Lakera in $300 million deal (Calcalist)](https://www.calcalistech.com/ctechnews/article/rj5bc1vige) — fetched 2026-06-28 — supports: ~$300M reported value; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by Check Point Software** (announced 2025-09-16, ~$300M reported, expected close Q4 2025). Seed flag verified. Filled founding (2021), Zurich/SF HQ, founders, ~$30M funding, Gandalf/prompt-injection positioning. Confidence high (close pending per release).
</content>
