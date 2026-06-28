---
type: vendor
name: WitnessAI
slug: witnessai
categories: [ai-access-governance, ai-runtime-security]
layer: model-prompt
aliases: [Witness AI]
website: https://witness.ai
founded: 2023
hq: Mountain View, California (US)
ownership: independent
ownership_detail: "Independent, VC-backed; $86.5M raised across Series A+B; no acquisition as of 2026-06-28"
ownership_confidence: high
funding_total: $86.5M
last_funding: "Series B $58M, 2026-01-13 (Sound Ventures lead)"
deployment: [inline-proxy, saas, self-hosted, api]
target_customer: enterprise; regulated
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [ai-access-governance, ai-firewall, shadow-ai, agentic-control, independent]
---

# WitnessAI

> **One-liner** — Inline "AI enablement" platform that gives security teams visibility, identity-aware access governance, and runtime guardrails over how employees and agents use AI.

**Categories** — [ai-access-governance](../categories/ai-access-governance.md), [ai-runtime-security](../categories/ai-runtime-security.md)

## What it does
WitnessAI sits **inline between users/apps and AI services** and does three jobs (the "Observe / Govern / Protect" split): **Observe** — discover and audit which AI apps and models employees use, with per-interaction visibility and risk scoring (a CASB-for-AI / shadow-AI view); **Govern** — apply **identity-aware access policy** (who can use which AI tools for what, with redaction/blocking by role and data type); **Protect** — runtime guardrails that block prompt injection, multi-turn attacks, toxic output, and sensitive-data leakage. Its newer **Agentic Control** extends the same model to AI agents and MCP — tracking which agents and MCP servers/tools are active and what an agent is doing on a user's behalf.

## Where it sits in the stack
Primary slot is [ai-access-governance](../categories/ai-access-governance.md) (CASB-for-AI / shadow-AI control — the access-governance and visibility job), with a strong secondary in [ai-runtime-security](../categories/ai-runtime-security.md) (the inline Protect guardrails). Because it's an inline chokepoint on AI traffic, it touches all three lethal-trifecta legs: **untrusted-input** (prompt-injection/jailbreak blocking), **sensitive-data** (redaction/DLP on prompts), and **egress** (governing which AI destinations data can flow to). It's a yellow-zone enforcement point in front of model and agent calls.

## Deployment & architecture
**Inline** — proxy/gateway-style interception of AI traffic (browser/network/API paths) with policy enforcement and logging. Emphasizes an **enterprise-first, single-tenant architecture** for data sovereignty and compliance, with hybrid-cloud and edge deployment. Identity integration (IdP/SSO) drives the per-user policy; logs feed SIEM/SOC. Agentic Control adds MCP-server and tool visibility for agent governance.

## Positioning & differentiators
Known for the **"AI enablement, not blocking"** framing — letting employees use AI under guardrails rather than banning tools. Differentiators: identity-aware governance (ties policy to user identity, not just network), single-tenant/sovereign deployment, and an early push into **agentic + MCP governance**. Founder/CEO **Rick Caccia** (ex-Palo Alto, Exabeam, Google marketing leadership) gives it strong enterprise-security GTM credibility. Nearest neighbors on access governance: [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [cyberhaven](cyberhaven.md), [zscaler](zscaler.md)/[netskope](netskope.md) AI modules; on runtime: [prisma-airs](prisma-airs.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [cisco-ai-defense](cisco-ai-defense.md).

## Ownership, funding & M&A
**No seed M&A flag; confirmed independent.** Founded **2023** by **Rick Caccia (co-founder & CEO)** and **Gil Spencer**; HQ **Mountain View, CA**. Raised **$27.5M Series A (May 2024)** led by **GV (Google Ventures)** and **Ballistic Ventures** (which incubated it), then a **$58M Series B announced 2026-01-13** led by **Sound Ventures** (early OpenAI/Anthropic/SentinelOne investor) with Fin Capital, Qualcomm Ventures, Samsung Ventures, and Forgepoint Capital — **$86.5M total**. **Independent** as of 2026-06-28; the Series B is growth capital for global expansion and agent security. `ownership_confidence: high`.

## CTO / hedge-fund lens
**Day-1 for a hedge fund** — the shadow-AI visibility + identity-aware access governance job is exactly what a fund needs first when employees start pasting data into ChatGPT/Claude: see what's being used, stop MNPI/PII from leaking into prompts, and enforce role-based rules. Single-tenant/sovereign deployment is attractive for a fund unwilling to route prompts through a shared multi-tenant cloud. SR 11-7 angle is indirect (it's a usage-control, not a model-validation tool), but the audit trail of AI interactions supports acceptable-use enforcement and surveillance/compliance needs ([comms-surveillance](../categories/comms-surveillance.md) adjacency). Fit **high** for the access-governance job; if you also want deep model-supply-chain or build-time red teaming, pair with [hiddenlayer](hiddenlayer.md) / [promptfoo](promptfoo.md). Main caution: inline interception adds a latency/availability dependency and overlaps with SSE/CASB ([zscaler](zscaler.md), [netskope](netskope.md)) you may already own.

## Competitors / alternatives
[harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [cyberhaven](cyberhaven.md), [prompt-security](prompt-security.md), [prisma-airs](prisma-airs.md), [lakera](lakera.md), [zscaler](zscaler.md), [netskope](netskope.md), [wald-ai](wald-ai.md).

## Open questions / to verify
- Exact inline insertion modes (forward proxy vs. browser vs. API gateway) and supported AI destinations.
- Whether the single-tenant architecture is customer-cloud, vendor-managed, or both.
- Real-world latency/availability impact of inline enforcement at scale.

## Sources
- [WitnessAI Raises $58 Million for Global Expansion and Announces New Ways to Secure AI Agents](https://witness.ai/resources/witnessai-raises-58-million-for-global-expansion-and-announces-new-ways-to-secure-ai-agents/) — fetched 2026-06-28 — supports: $58M Series B 2026-01-13, $86.5M total, HQ, product/agentic control, deployment; confidence: high
- [Axios: WitnessAI nabs $58M](https://www.axios.com/2026/01/13/witnessai-funding-enterprise-ai) — fetched 2026-06-28 — supports: Series B, independence, investors; confidence: high
- [TechCrunch: WitnessAI is building guardrails for generative AI models](https://techcrunch.com/2024/05/21/witnessai-is-building-guardrails-for-generative-ai-models/) — fetched 2026-06-28 — supports: founders, founding 2023, Series A, product framing; confidence: high
- (cached: `raw/sources/2026-06-28--witnessai--series-b-58m.md`)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED **independent**, set ownership_confidence high. Established founding 2023 (Caccia/Spencer; Mountain View), $27.5M Series A (May 2024, GV/Ballistic) + $58M Series B (2026-01-13, Sound Ventures) = $86.5M total. Documented Observe/Govern/Protect + Agentic Control; inline architecture. hedge_fund_fit raised to high.
