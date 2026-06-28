---
type: vendor
name: NeMo Guardrails (NVIDIA)
slug: nemo-guardrails
categories: [ai-red-teaming]
layer: model-prompt
aliases: [NVIDIA NeMo Guardrails, Colang]
website: "https://github.com/NVIDIA-NeMo/Guardrails"
founded: 2023
hq: Santa Clara, CA (NVIDIA)
ownership: public
ownership_detail: "Open-source project (Apache 2.0) maintained by NVIDIA (NASDAQ: NVDA); not a standalone company"
ownership_confidence: high
funding_total: n/a (NVIDIA-funded OSS project)
last_funding: n/a
deployment: [self-hosted, sdk]
target_customer: AI developers / enterprises (esp. NVIDIA AI stack users)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [ai-red-teaming, guardrails, open-source, nvidia, colang]
---

# NeMo Guardrails (NVIDIA)

> NVIDIA's open-source toolkit for adding programmable guardrails ("rails") to
> LLM-based conversational apps — define dialogue flows and safety checks in Colang.

**One-liner** — An open-source Python toolkit from NVIDIA that wraps an LLM with
configurable input, dialog, retrieval, execution, and output rails.

**Categories** — [ai-red-teaming](../categories/ai-red-teaming.md)

## What it does
NeMo Guardrails sits between the user and the LLM and enforces programmable rules. It
provides five rail types: **input rails** (filter/transform user input — jailbreak and
prompt-injection checks), **dialog rails** (constrain conversation flow), **retrieval
rails** (guard RAG context), **execution rails** (govern tool/function calls), and
**output rails** (moderate/block the model's response — toxicity, hallucination, PII).
Rules are authored in **Colang**, a Python-like dialogue-modeling language. It can
self-check with an LLM and pairs with NVIDIA's NeMo Guard / Aegis content-safety
models.

## Where it sits in the stack
[ai-red-teaming](../categories/ai-red-teaming.md) / guardrails in the model/prompt layer, overlapping
[ai-runtime-security](../categories/ai-runtime-security.md). Lethal-trifecta role: **untrusted-input** (input/jailbreak
rails) and **sensitive-data** (output moderation/PII rails); execution rails also
touch the tool-call surface relevant to [mcp-gateway](../categories/mcp-gateway.md) / agent control. It is an
in-app library, not a network proxy.

## Deployment & architecture
Self-hosted open-source Python package (SDK) under Apache 2.0; runs in-process or as a
server in front of model calls. Integrates with OpenAI, Llama, Falcon and others, and
with LangChain. Part of the broader NVIDIA NeMo / NIM microservices ecosystem, so it
slots naturally into NVIDIA-hosted inference stacks. Latest release 0.22.0 (May 2026).

## Positioning & differentiators
The other reference **open-source guardrails framework** alongside [guardrails-ai](guardrails-ai.md);
the two interoperate. NeMo Guardrails is distinguished by **Colang** and its
dialog-flow modeling (strong for scripted conversational control) and by tight
coupling to NVIDIA's model/microservice stack. [guardrails-ai](guardrails-ai.md) leans toward a
validator marketplace. Commercial managed alternatives: [lakera](lakera.md), [prompt-security](prompt-security.md),
[pillar-security](pillar-security.md), [prisma-airs](prisma-airs.md).

## Ownership, funding & M&A
**Not an independent company** — it is an open-source project owned and maintained by
**NVIDIA (NASDAQ: NVDA)**, released October 2023, Apache 2.0. Ownership corrected from
the stub's default `independent` to `public` (part of NVIDIA). No funding rounds (it is
NVIDIA-funded OSS). Confidence high.

## CTO / hedge-fund lens
Day-2, developer-facing, and free. Relevant only if your team is **building LLM/RAG
apps in code** and wants programmable rails — especially if you already run on NVIDIA
infrastructure. For a fund consuming off-the-shelf assistants it is not an operated
control. As open source it carries no license cost but does carry build/maintain
effort; most funds will instead buy guardrails inside an [ai-runtime-security](../categories/ai-runtime-security.md)
product. Useful as documented output/PII controls for an SR 11-7 model-risk story if
you self-build.

## Competitors / alternatives
[guardrails-ai](guardrails-ai.md), [lakera](lakera.md), [prompt-security](prompt-security.md), [pillar-security](pillar-security.md),
[prisma-airs](prisma-airs.md), [enkrypt-ai](enkrypt-ai.md).

## Open questions / to verify
- Relationship/packaging with commercial NeMo microservices and NIM (paid vs. free line).
- Real-world latency/overhead of running rails inline in production.

## Sources
- [NVIDIA-NeMo/Guardrails — GitHub](https://github.com/NVIDIA-NeMo/Guardrails) — fetched 2026-06-28 — supports: what it is, Apache 2.0, NVIDIA maintainer, rail types, Colang, version 0.22.0; confidence: high (primary repo).
- [NeMo Guardrails docs](https://docs.nvidia.com/nemo/guardrails/home) — fetched 2026-06-28 — supports: rail types, integrations, safety features; confidence: high (primary docs).
- [NeMo Guardrails (arXiv 2310.10501)](https://arxiv.org/abs/2310.10501) — fetched 2026-06-28 — supports: toolkit design, programmable rails; confidence: high (primary paper).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established this is an NVIDIA-owned open-source project (Apache 2.0, 2023), not a standalone company. Corrected ownership independent→public (NVIDIA), confidence high; hedge_fund_fit low.
