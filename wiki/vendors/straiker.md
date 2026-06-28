---
type: vendor
name: Straiker
slug: straiker
categories: [agent-runtime-security, ai-runtime-security]
layer: model-prompt
aliases: [Straiker AI]
website: https://www.straiker.ai
founded: 2024
hq: Sunnyvale, California, USA
ownership: independent
ownership_detail: VC-backed; $21M Series A from Lightspeed & Bain Capital Ventures (2025-03)
ownership_confidence: high
funding_total: ~$21M
last_funding: Series A $21M (2025-03)
deployment: [saas, api]
target_customer: enterprise (finance, healthcare, tech, media, retail)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [agent-runtime, ai-runtime, red-teaming, ai-native, ex-palo-alto]
---

# Straiker

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). Also relevant to [ai-runtime-security](../categories/ai-runtime-security.md).

**One-liner** — An AI-native security platform that red-teams, protects at runtime, and discovers enterprise AI apps and autonomous agents across every layer of the AI stack.

## What it does
Straiker secures the full range of enterprise AI — from AI-native apps to agents — with three modules: **Ascend AI** (automated attack simulation / red teaming using AI-specific safety and security threat scenarios, for risk assessment and continuous testing); **Defend AI** (runtime protection with real-time threat detection and automated blocking across the layers of an AI application); and **Discover AI** (AI agent discovery, tool monitoring, and governance visibility at scale). It uses fine-tuned models to analyze intelligence across the whole stack — user, model, application, agents, identity, and data layers — rather than filtering at the prompt level alone.

## Where it sits in the stack
Spans [agent-runtime-security](../categories/agent-runtime-security.md) (runtime protection + discovery of agents) and [ai-runtime-security](../categories/ai-runtime-security.md) (AI-firewall-style inline detection/blocking), with a red-teaming function adjacent to [ai-red-teaming](../categories/ai-red-teaming.md). Layer: model/prompt. It works all three lethal-trifecta legs — simulates and blocks **untrusted input** attacks (prompt injection/jailbreaks), guards **sensitive data**, and constrains agent **actions/egress**. Combines pre-deployment testing with runtime defense in one platform.

## Deployment & architecture
SaaS / API-delivered, application- and agent-layer protection (not a Kubernetes-infra agent like [operant-ai](operant-ai.md)). Ascend AI runs automated adversarial tests against AI apps/agents; Defend AI provides inline runtime blocking. Exact integration points (gateway, SDK, proxy) aren't fully public — treat as medium confidence.

## Positioning & differentiators
Known for being **"AI-native"** — purpose-built fine-tuned detection models spanning the full AI stack — and for the **founder pedigree**: CEO Ankur Shah led Prisma Cloud at Palo Alto Networks, and co-founder Sreenath Kurupati is also ex-Palo Alto/Intel, which shaped the unified test-plus-protect positioning. Differs from posture/governance-first [noma-security](noma-security.md)/[zenity](zenity.md)/[cranium](cranium.md) by leading with runtime + red teaming, and from infra-native [operant-ai](operant-ai.md) by operating at the app/agent layer rather than in the Kubernetes data path. Closest neighbors: [prisma-airs](prisma-airs.md), [hiddenlayer](hiddenlayer.md), [straiker](straiker.md)'s red-teaming overlaps with [splxai](splxai.md) and [lakera](lakera.md).

## Ownership, funding & M&A
Independent, VC-backed. Founded 2024; emerged from stealth March 27, 2025 with a **$21M Series A from Lightspeed Venture Partners and Bain Capital Ventures**. Founders: Ankur Shah (CEO) and Sreenath Kurupati, both formerly of Palo Alto Networks. HQ Sunnyvale, CA. No M&A; no seed acquisition flag. Ownership confidence: high.

## CTO / hedge-fund lens
**Day-2.** Straiker is an early but credibly-led entrant; the combined "test before deploy + block at runtime" story is attractive if you're shipping internal AI apps/agents and want one vendor for both. For a hedge fund, the red-teaming (Ascend AI) maps cleanly onto pre-production model/agent validation that an SR 11-7 model-risk process would want, while Defend AI covers runtime. Given its 2024 founding and single Series A, treat it as an evaluate/pilot candidate rather than an incumbent control; larger shops may prefer the breadth of [prisma-airs](prisma-airs.md).

## Competitors / alternatives
[prisma-airs](prisma-airs.md), [hiddenlayer](hiddenlayer.md), [zenity](zenity.md), [noma-security](noma-security.md), [operant-ai](operant-ai.md), [splxai](splxai.md), [lakera](lakera.md).

## Open questions / to verify
- Deployment/integration mechanics (gateway vs SDK vs proxy) for Defend AI.
- Customer traction and any funding since the March 2025 Series A.
- How its runtime blocking compares head-to-head with established AI firewalls.

## Sources
- [Straiker Launches with $21M to Safeguard AI (straiker.ai)](https://www.straiker.ai/blog/straiker-launches-with-21-million-to-safeguard-ai) — fetched 2026-06-28 — supports: founding, founders, HQ, $21M Series A/investors, three-module product; confidence: high (vendor release).
- [AI Security Firm Straiker Emerges From Stealth With $21M (SecurityWeek)](https://www.securityweek.com/ai-security-firm-straiker-emerges-from-stealth-with-21m-in-funding/) — fetched 2026-06-28 — supports: stealth exit date, funding, leadership; confidence: high (reputable press).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/VC-backed, founded 2024, stealth exit 2025-03 with $21M Series A (Lightspeed, Bain Capital Ventures), ex-Palo Alto founders (Shah/Kurupati), Sunnyvale. Runtime + red-teaming + agent discovery scope; added ai-runtime-security as secondary category. Set ownership_confidence high.
