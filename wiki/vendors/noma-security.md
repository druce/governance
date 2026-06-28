---
type: vendor
name: Noma Security
slug: noma-security
categories: [ai-spm, agent-runtime-security]
layer: model-prompt
aliases: [Noma]
website: https://noma.security
founded: 2023
hq: Tel Aviv, Israel (R&D); New York, USA (operations)
ownership: independent
ownership_detail: VC-backed; $100M Series B led by Evolution Equity Partners (2025-07)
ownership_confidence: high
funding_total: ~$132M
last_funding: Series B $100M (2025-07)
deployment: [saas, api, self-hosted]
target_customer: enterprise / regulated (Fortune 500; financial services, life sciences, retail, tech)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [ai-spm, agent-security, runtime, red-teaming]
---

# Noma Security

> Primary category: [[ai-spm]]. Also spans [[agent-runtime-security]].

**One-liner** — An end-to-end AI and agent security platform that discovers your AI/agent estate, scores its posture, red-teams it, and protects it at runtime.

## What it does
Noma sits across the AI lifecycle. It continuously **discovers** AI assets — models, datasets, notebooks, pipelines, and increasingly AI agents — across cloud accounts, code repos, and ML/AI development platforms; builds an inventory and **posture** view (AI-SPM); runs **AI red teaming** to find prompt-injection and jailbreak weaknesses before deployment; and provides **runtime protection** for live AI agents and applications (guardrails on inputs/outputs and agent actions). The pitch is one platform instead of stitching a posture tool, a red-team tool, and a runtime firewall together.

## Where it sits in the stack
Primarily [[ai-spm]] (inventory + posture + governance of AI assets), extending into [[agent-runtime-security]] for live agent protection. Layer: model/prompt. On the lethal trifecta it touches all three legs — it inspects **untrusted input** (prompt-injection detection), watches **sensitive data** moving through AI/agent flows, and can constrain **egress**/tool actions. Lives mostly in the yellow/green zones around enterprise AI workloads.

## Deployment & architecture
SaaS control plane with API/agent-based connectors into cloud (AWS/Azure/GCP), code repositories, and AI dev platforms (e.g. Databricks — note Databricks Ventures is an investor). Runtime protection inserts guardrails into the application/agent path. Integrates with the AI development toolchain it discovers; SIEM/SOC export is the usual pattern for posture/runtime findings.

## Positioning & differentiators
Known for being one of the louder "end-to-end agentic AI security" plays — combining discovery + posture + red teaming + runtime in a single platform, where many neighbors do only one slice. Closest neighbor is [[zenity]], which similarly spans AI-SPM and agent runtime but came up through copilot/low-code security; Noma came up through the ML/AI data-and-pipeline posture angle. Other adjacents: [[reco]] and [[nudge-security]] (lighter AI-SPM/shadow-AI), [[prisma-airs]] and [[straiker]] (runtime-leaning), and AI red-teaming specialists like [[hiddenlayer]].

## Ownership, funding & M&A
Independent, VC-backed. Founded 2023 by Niv Braun (CEO) and Alon Tron; emerged from stealth November 2024. Series A (Oct 2024) led by Ballistic Ventures; **$100M Series B (July 2025) led by Evolution Equity Partners** with Ballistic, Glilot Capital, Cyber Club London, Databricks Ventures, and SVCI — bringing total funding to roughly $132M. No M&A; no seed acquisition flag. Ownership confidence: high (independent). (One PR render listed "founded 2024"; multiple profiles + the stealth timeline support 2023 — medium confidence on the exact year.)

## CTO / hedge-fund lens
**Day-2.** This is a consolidation buy once you already have AI/agents in production and want a single pane for "what AI do we have, how exposed is it, and is anything being attacked right now." Noma explicitly courts financial-services buyers, so the regulated-shop framing (SR 11-7 model inventory, evidence for model-risk review) is part of the story — though Noma is a security posture tool, not a model-risk/governance platform like [[credo-ai]]. For a hedge fund: relevant if you're building/hosting your own agents at scale; overkill if your AI footprint is a couple of SaaS assistants behind an [[ai-gateway]].

## Competitors / alternatives
[[zenity]], [[reco]], [[nudge-security]], [[prisma-airs]], [[straiker]], [[operant-ai]], [[hiddenlayer]], [[cranium]].

## Open questions / to verify
- Exact founding year (2023 vs 2024).
- Runtime enforcement mechanics — inline proxy vs in-app SDK vs sidecar — not pinned down from public sources.
- Real depth of agent-runtime protection vs AI-SPM (marketing blends them).

## Sources
- [Noma Security Raises $100M (PRNewswire)](https://www.prnewswire.com/news-releases/noma-security-raises-100m-to-drive-adoption-of-ai-agent-security-302518641.html) — fetched 2026-06-28 — supports: Series B $100M, lead investor, founders, HQ, product scope, customers; confidence: high (vendor-issued release).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/VC-backed, $100M Series B (2025-07, Evolution Equity), founders Braun/Tron, Tel Aviv+NY, AI-SPM + agent-runtime scope. Set ownership_confidence high. No M&A.
