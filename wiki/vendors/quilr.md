---
title: Quilr
type: vendor
name: Quilr
slug: quilr
aka: [Quilr AI]
primary_category: ai-spm
also_listed_in: [ai-access-governance, mcp-gateway]
website: https://www.quilr.ai
founded: 2023
hq: Austin, Texas, USA (some profiles list San Francisco — unconfirmed)
ownership_state: independent
owner: null
ownership_note: Seed-stage; ~$3–4M led by Crew Capital (2025)
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$3–4M
last_funding: Seed (2025-04)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: gateway
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise (securing AI adoption / human-related breach prevention)
last_verified: 2026-06-28
verify_after: null
tags: [ai-spm, shadow-ai, guardrails, seed-stage, agentic, mcp-gateway]
sources:
  - {claim: "Quilr markets an MCP Gateway placed in front of MCP servers: per-agent tool scoping, identity verification on every agent-to-MCP call, audited tool-call logs", url: "https://quilr.ai/solutions/mcp-tooling", date: 2026-10-23, confidence: low}
---

# Quilr

> Primary category: [ai-spm](../categories/ai-spm.md). Also spans [ai-access-governance](../categories/ai-access-governance.md) and [mcp-gateway](../categories/mcp-gateway.md).

**One-liner** — An early-stage agentic-AI security startup that discovers shadow AI, applies adaptive guardrails to prompts and data, and provides posture management over AI usage and autonomous agents.

## What it does
Quilr aims to stop "human-related" and AI-related security breaches by sitting between employees/agents and AI tools. It does **shadow-AI discovery** (which AI apps/agents are in use), applies **adaptive guardrails** on prompts and responses (data-leak prevention, prompt-injection defense, regulated-data protection), and provides **AI security posture management** across prompts, shadow AI, and autonomous agents. Branded as an agentic "service-as-software" platform.

## Where it sits in the stack
Straddles [ai-spm](../categories/ai-spm.md) (visibility/posture over AI usage and agents) and [ai-access-governance](../categories/ai-access-governance.md) (CASB-for-AI / shadow-AI control of what employees feed to which tools). Layer: model/prompt. At a lightweight level it screens untrusted input (prompt injection), guards sensitive data in prompts, and limits risky outbound flows to unsanctioned AI. Lives at the employee↔AI and agent↔tool boundary.

## Deployment & architecture
SaaS with guardrail enforcement on the AI interaction path (API/inline guardrails; the exact browser-extension vs proxy vs API mechanism is not clearly documented publicly). ~70 employees per third-party profiles. Treat architecture specifics as unverified.

**MCP Gateway (added 2026-10-23).** Quilr now markets a **QuilrAI MCP Gateway**, which is the basis for the [mcp-gateway](../categories/mcp-gateway.md) cross-list. Per its product page, you "drop the gateway in front of your MCP servers" and it claims 500+ supported servers. Each agent gets a policy-defined subset of each server's tools, configured in Quilr's "Guardian" (e.g., GitHub limited to approved repos, filesystem limited to the project directory). "Every agent-to-MCP call goes through the QuilrAI gateway with identity verification." Each call is logged with agent identity, tool name, redacted parameters and response, in searchable, exportable logs with configurable retention. A companion MCP scanner checks community MCP packages at install and on update. A 2026-10 CTO-survey respondent wrote in "Quilr MCP Gateway." This is **vendor marketing only**. The auth mechanisms and IdPs, the deployment model (SaaS vs self-hosted), and latency on the MCP path are not documented.

## Positioning & differentiators
A **seed-stage** entrant in a crowded shadow-AI / AI-SPM field, leaning on its founder/advisor security pedigree (angels include Tanuj Gulati, ex-Securonix CTO/founder, and Sam Kassoumeh, SecurityScorecard co-founder/COO). Differs from larger, better-funded neighbors mostly by maturity. Nearest neighbors: [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [wald-ai](wald-ai.md), [lanai](lanai.md), [nudge-security](nudge-security.md), and [reco](reco.md) on the access-governance/shadow-AI side; [noma-security](noma-security.md) and [zenity](zenity.md) on the heavier AI-SPM/agent side.

## Ownership, funding & M&A
Independent, seed-stage. Founder: Vidit Arora. **~$3–4M seed (April 2025) led by Crew Capital**, with Sprout & Oak and angels (Tanuj Gulati, Sam Kassoumeh). No M&A; no seed acquisition flag. Ownership confidence: high (clearly independent), though firmographics are thin.

> Contradiction (soft): founding year listed as 2023 (startuphub) vs 2024 (Tracxn); HQ listed as Austin, TX (Tracxn/Crunchbase) vs San Francisco (startuphub). Non-blocking — recorded both, dated 2026-06-28.

## CTO / hedge-fund lens
**Day-2**, and for most hedge funds **not yet** — at seed stage with ~$3–4M raised, Quilr is an early bet, not a procurement-ready control. The job it does (shadow-AI discovery + DLP-style guardrails on AI usage) is real and arguably Day-1, but a regulated fund would more likely buy that capability from a more established [ai-access-governance](../categories/ai-access-governance.md) vendor or get it bundled in [netskope](netskope.md)/[zscaler](zscaler.md) SSE. Worth watching, not yet a core stack item.

## Competitors / alternatives
[harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [wald-ai](wald-ai.md), [lanai](lanai.md), [nudge-security](nudge-security.md), [reco](reco.md), [noma-security](noma-security.md), [zenity](zenity.md).

## Open questions / to verify
- Founding year (2023 vs 2024) and HQ (Austin vs SF).
- Deployment mechanism — browser extension, inline proxy, or API guardrails?
- Real customer traction vs marketing; total funding (sources say $3M and $4M).
- MCP Gateway: deployment model, supported auth/IdPs, GA status, and whether it is a separate SKU from the AI-usage guardrails.

## Sources
- [Quilr — $4M Raised (StartupHub.ai)](https://www.startuphub.ai/startups/quilr) — fetched 2026-06-28 — supports: funding, HQ (SF variant), headcount, product focus; confidence: medium (aggregator).
- [Quilr Unveils Agentic AI Service-as-Software Platform (BusinessWire)](https://www.businesswire.com/news/home/20250417432711/en/Quilr-Unveils-Agentic-AI-Service-as-Software-Platform-to-Prevent-Human-Related-Security-Breaches) — fetched 2026-06-28 (search snapshot; direct fetch timed out) — supports: launch, product framing, seed date; confidence: medium.
- [QuilrAI — MCP Gateway / "Give your agents tools"](https://quilr.ai/solutions/mcp-tooling) — fetched 2026-10-23 — supports: MCP gateway in front of MCP servers, Guardian tool scoping, identity verification, audited tool calls, MCP package scanner; confidence: low (vendor marketing). Cached: `raw/sources/2026-10-23--quilr--mcp-gateway.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent seed-stage (~$3–4M, Crew Capital, 2025), founder Vidit Arora, shadow-AI + guardrails + AI-SPM scope. Flagged soft contradictions on founding year and HQ. Set ownership_confidence high; hedge_fund_fit low (early stage).
- [2026-10-23] Cross-listed to mcp-gateway (mcp_support: gateway) on the evidence of Quilr's MCP Gateway product page; prompted by a 2026-10 CTO-survey write-in ("Quilr MCP Gateway"). Only the MCP claim was re-verified; last_verified left unchanged.
