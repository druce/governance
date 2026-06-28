---
title: Enkrypt AI
type: vendor
name: Enkrypt AI
slug: enkrypt-ai
categories: [ai-runtime-security, ai-red-teaming]
layer: model-prompt
aliases: [Enkrypt, Sentry]
website: "https://www.enkryptai.com/"
founded: 2022
hq: Boston, MA, USA
ownership: independent
ownership_detail: VC-backed independent; no M&A. Seed round Feb 2024 led by Boldcap.
ownership_confidence: high
funding_total: $2.35M (disclosed seed; later/larger Series A unconfirmed)
last_funding: Seed, $2.35M, 2024-02 (led by Boldcap)
deployment: [saas, api, sdk, inline-proxy]
target_customer: enterprise / regulated (finance, healthcare)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [llm-security, red-teaming, guardrails, ai-firewall, agent-security, mcp]
---

# Enkrypt AI

> Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). Also [ai-red-teaming](../categories/ai-red-teaming.md).

**One-liner** — A full-lifecycle LLM/agent security startup that pairs automated red-teaming (find the holes) with runtime guardrails (an AI firewall that blocks them), wrapped in compliance/risk reporting mapped to frameworks like the EU AI Act and NIST.

## What it does

Enkrypt AI sells the "test-then-protect" loop for generative AI. On the **red-teaming** side it runs automated adversarial attacks against models, apps, and agents to surface prompt injection, jailbreaks, data leakage, hallucination, bias, and (in its published research) CBRN and agent-misuse risks. On the **runtime** side, its guardrails / "Sentry" control layer sits between users and the model and inspects and blocks unsafe inputs and outputs and policy violations in real time. A distinguishing pitch is **policy-to-rule automation**: it converts human-readable compliance policies into enforced guardrail rules, plus continuous risk reporting and audit evidence. The company also publishes an "LLM Safety Leaderboard" benchmarking 200+ models, which doubles as marketing and as model-selection input.

Recent product expansion is heavily **agentic**: Agent Red Teaming, Agent Guardrails, an Agent Policy Engine, an MCP Scanner (scan MCP servers for risk), and an MCP Gateway. It was named a Gartner Cool Vendor in AI Security (2025, per the vendor).

## Where it sits in the stack

Primary home is [ai-runtime-security](../categories/ai-runtime-security.md) (the AI firewall / runtime guardrail layer, model-prompt layer, Day-1 if you put GenAI in front of users or data). Its testing side belongs to [ai-red-teaming](../categories/ai-red-teaming.md), and its MCP/agent tooling reaches into [mcp-gateway](../categories/mcp-gateway.md) and agent security territory.

Lethal-trifecta role: the runtime guardrail is one of the few controls that touches **all three legs** — it screens **untrusted input** (prompt-injection/jailbreak detection), watches for **sensitive-data** exposure in prompts/outputs (PII/leakage filtering), and can block unsafe **egress** (tool calls / outbound content). Trust zones: it lives at the boundary between the untrusted user/web zone and the model.

## Deployment & architecture

SaaS platform consumed via **API and SDK**, with the guardrail deployable as an **inline control layer / proxy** between application and model so it can inspect traffic in real time. Integration surface emphasizes **MCP** (scanner + gateway for agent tool access) and multi-model coverage (guardrails sit in front of many model providers). Compliance reporting maps detections to EU AI Act / NIST. (SIEM/IdP/DSPM integration depth not confirmed from primary sources — see open questions.)

## Positioning & differentiators

Enkrypt's angle is **breadth across the lifecycle** — red-teaming, runtime guardrails, and compliance reporting in one place — versus point players. Compared to neighbors:

- vs [lakera](lakera.md) and [prompt-security](prompt-security.md) — Enkrypt leans harder into the red-teaming + compliance-reporting story, not just inline guardrails.
- vs [splxai](splxai.md), [mindgard](mindgard.md), [promptfoo](promptfoo.md) — those are more red-teaming/eval-first; Enkrypt also ships the production firewall.
- vs [pillar-security](pillar-security.md), [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [prisma-airs](prisma-airs.md), [calypsoai](calypsoai.md) — these overlap on runtime/AI-firewall; Enkrypt is a smaller, independent, research-forward startup rather than a platform or acquirer.
- Known for visible research output (CBRN red-teaming study, guardrail-bypass reports on Azure/AWS/Meta, agent risk taxonomy) and the LLM Safety Leaderboard.

## Ownership, funding & M&A

Independent, VC-backed. Confirmed **$2.35M seed (Feb 2024), led by Boldcap**, with Berkeley SkyDeck, Kubera VC, Arka VC, Veredas Partners, and Builders Fund. **No M&A** — not acquired, has not acquired anyone (no seed flag; nothing found).

> The research brief hinted at a "~$8M Series A (2025, led by Boldcap)" and "MIT origins." Neither was confirmable against primary sources as of 2026-06-28: the only publicly disclosed round is the seed, and the founders are **Yale PhDs** (Sahil Agarwal, CEO; Prashanth Harshangi, CTO), not MIT. Some third-party aggregators cite a larger Series A figure but without a primary announcement. Treated as **unconfirmed**, not asserted. (soft mismatch, non-blocking.)

## CTO / hedge-fund lens

The runtime-guardrail function is **Day-1** for any fund putting an LLM or agent in front of users or sensitive data; the red-teaming and compliance-reporting functions are **Day-2** maturity but become Day-1 under a model-risk regime. For an asset manager, the **compliance-mapping and audit-evidence** angle (EU AI Act / NIST, and by extension SR 11-7-style model-risk documentation) is the most differentiated reason to look here — it turns guardrail enforcement into auditable evidence. Caveat: Enkrypt is an **early-stage, small independent** vendor, so vendor-risk/longevity diligence matters more than with a Palo Alto ([prisma-airs](prisma-airs.md)) or Cisco. Fit: **medium** — attractive capability set and compliance framing, tempered by startup maturity and the fact that larger platforms now bundle similar guardrails.

## Competitors / alternatives

[lakera](lakera.md), [splxai](splxai.md), [pillar-security](pillar-security.md), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [witnessai](witnessai.md), [mindgard](mindgard.md), [promptfoo](promptfoo.md), [calypsoai](calypsoai.md), [prompt-security](prompt-security.md).

## Open questions / to verify

- Series A: amount, date, lead — could not confirm a 2025 Series A; only the $2.35M seed is documented. Re-check for a later announcement.
- "MIT origins" appears incorrect (founders are Yale PhDs) — confirm/retire this alias note.
- Depth of enterprise integrations (SIEM/SOC, IdP, DSPM) beyond MCP and model providers.
- Whether guardrails run self-hosted/on-prem for regulated buyers, or SaaS-only.

## Sources

- [Enkrypt AI homepage](https://www.enkryptai.com/) — fetched 2026-06-28 — supports: product portfolio (Agent Guardrails/Red Teaming/Policy Engine, MCP Scanner/Gateway), SaaS+API+SDK deployment, EU AI Act/NIST mapping, Gartner Cool Vendor 2025; confidence: med (vendor marketing).
- [Enkrypt AI vendor profile — IT-Harvest](https://guardiansofthemachineage.com/vendors/enkrypt-ai/) — fetched 2026-06-28 — supports: founded 2022, Boston HQ, Yale-PhD founders, $2.35M seed (Boldcap), Sentry inline control-layer description; confidence: med.
- [Enkrypt AI secures $2.35M — Tech Startups](https://techstartups.com/2024/02/27/enkrypt-ai-secures-2-35m-in-funding-to-build-visibility-and-security-infrastructure-for-generative-ai/) — fetched 2026-06-28 — supports: seed amount/date/investors, founders, founding year, HQ, Sentry product; confidence: high (for the seed round).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022, Boston HQ, Yale-PhD founders (Sahil Agarwal/Prashanth Harshangi), independent with confirmed $2.35M seed (Feb 2024, led by Boldcap). Could NOT confirm the brief's ~$8M 2025 Series A or "MIT origins" — flagged as unconfirmed (soft). Set deployment saas/api/sdk/inline-proxy, trifecta all three legs, hedge_fund_fit medium. Cached 3 sources. status: researched.
