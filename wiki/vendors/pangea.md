---
type: vendor
name: Pangea
slug: pangea
categories: [ai-red-teaming, ai-runtime-security]
layer: model-prompt
aliases: [Pangea Cyber, Pangea AI Guardrail Platform]
website: "https://pangea.cloud"
founded: 2021
hq: Palo Alto, California, USA
ownership: acquired
ownership_detail: "Acquired by CrowdStrike — announced 2025-09-16 at Fal.Con 2025, completed ~Sept 2025; reported ~$260M. Now part of CrowdStrike's AI Detection and Response (AIDR)."
ownership_confidence: high
funding_total: ~$51M (pre-acquisition)
last_funding: "$26M Series B (Nov 2022, led by GV; Decibel, Okta Ventures)"
deployment: [api, sdk, saas]
target_customer: enterprise / developers building AI apps
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 3
last_updated: 2026-06-28
tags: [ai-guardrails, prompt-injection, aidr, crowdstrike]
---

# Pangea

> Primary category: [ai-red-teaming](../categories/ai-red-teaming.md) (AI guardrails). Also [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [crowdstrike](crowdstrike.md)** (2025).

**One-liner** — A developer-first "AI guardrail" platform — prompt-injection blocking, AI DLP, and policy guardrails delivered as APIs/SDK — now the prompt-layer core of [crowdstrike](crowdstrike.md)'s AI Detection and Response (AIDR).

## What it does
Pangea provides a set of composable **AI security guardrails** that developers drop into AI applications or AI gateways: prompt-injection detection/blocking, sensitive-data redaction (AI DLP), malicious-content and PII filters, and policy enforcement on prompts and responses. It also protects workforce AI use (visibility + guardrails on how employees use AI). The pitch is "ship secure AI apps fast" via a few lines of code rather than standing up a separate inline appliance.

(Pangea began life in 2021 as a broader developer-first security-services API platform — auth, audit logging, secure-by-design building blocks — and pivoted to AI guardrails as that market emerged.)

## Where it sits in the stack
Model/prompt layer. It breaks the **untrusted-input** (prompt injection) and **egress/sensitive-data** legs of the lethal trifecta, sitting in the yellow (AI application) trust zone. Functionally it overlaps [ai-runtime-security](../categories/ai-runtime-security.md) (AI firewall) and [ai-red-teaming](../categories/ai-red-teaming.md)/guardrails; it is more an embeddable guardrail toolkit than a standalone inline proxy.

## Deployment & architecture
API/SDK-first, cloud-delivered. Guardrails are invoked from application code or fronted by an AI gateway. Vendor claims prompt-injection blocking at ~99% efficacy and sub-30ms latency (marketing — unverified). Post-acquisition, capabilities are being folded into [crowdstrike](crowdstrike.md) Falcon as AIDR.

## Positioning & differentiators
- Developer-/API-first guardrails vs. inline-proxy AI firewalls like [witnessai](witnessai.md) or [prisma-airs](prisma-airs.md).
- Founders Oliver Friedrichs and Sourabh Satish previously built Phantom Cyber (SOAR, acquired by Splunk 2018) — a security-operations pedigree that fits CrowdStrike's SOC focus.
- Nearest neighbors: [lakera](lakera.md), [prompt-security](prompt-security.md), [hiddenlayer](hiddenlayer.md), [enkrypt-ai](enkrypt-ai.md), [pillar-security](pillar-security.md), [aim-security](aim-security.md) in the guardrails/AI-runtime space.

## Ownership, funding & M&A
**Seed flag "acq by CrowdStrike" — CONFIRMED.** CrowdStrike announced the acquisition on 2025-09-16 at Fal.Con 2025 and announced completion later that month (~2025-09-26). Reported deal value ~$260M (BankInfoSecurity; not officially disclosed). Pre-acquisition Pangea was independent, ~$51M raised, including a $26M Series B (Nov 2022) led by GV with Decibel and Okta Ventures. Confidence: high on the acquisition; medium on exact price/close date (press-reported).

## CTO / hedge-fund lens
Day-2. Relevant only if you are *building* AI applications and want embeddable guardrails, or if you're a CrowdStrike shop adopting AIDR. A fund that only *consumes* SaaS AI assistants would get more from an [ai-access-governance](../categories/ai-access-governance.md) CASB-for-AI tool than from a developer guardrail SDK. As a now-CrowdStrike product, evaluate it as part of the Falcon platform rather than a standalone purchase.

## Competitors / alternatives
[lakera](lakera.md), [prompt-security](prompt-security.md) (now [sentinelone](sentinelone.md)), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [enkrypt-ai](enkrypt-ai.md), [witnessai](witnessai.md).

## Open questions / to verify
- Exact close date and final price (press-reported ~$260M).
- Whether Pangea remains available as a standalone product or only inside Falcon AIDR going forward.

## Sources
- [CrowdStrike to Acquire Pangea to Secure Every Layer of Enterprise AI](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-pangea-to-secure-every-layer-of-enterprise-ai/) — fetched 2026-06-28 — supports: acquisition (2025-09-16), AIDR, Pangea capabilities; confidence: high
- [CrowdStrike Buys Pangea for $260M (BankInfoSecurity)](https://www.bankinfosecurity.com/crowdstrike-buys-pangea-for-260m-to-guard-enterprise-ai-use-a-29480) — fetched 2026-06-28 — supports: ~$260M value; confidence: med
- [Pangea Cyber Closes $26M Series B (PR Newswire)](https://www.prnewswire.com/news-releases/pangea-cyber-closes-26m-series-b-from-gv-decibel-and-okta-ventures-for-developer-first-security-framework-to-deliver-secure-apps-faster-301689531.html) — fetched 2026-06-28 — supports: founded 2021, HQ Palo Alto, founders, $26M Series B; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by CrowdStrike (announced 2025-09-16 at Fal.Con, ~$260M, completed ~Sept 2025) — raised ownership_confidence to high. Established Pangea founded 2021, HQ Palo Alto, founders ex-Phantom Cyber, ~$51M raised. Added `ai-runtime-security` as secondary category (guardrails overlap). Set hedge_fund_fit medium.
