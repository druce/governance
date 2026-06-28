---
type: vendor
name: Zenity
slug: zenity
categories: [agent-runtime-security, ai-spm]
layer: model-prompt
aliases: [Zenity.io]
website: https://zenity.io
founded: 2021
hq: Tel Aviv-Yafo, Israel
ownership: independent
ownership_detail: VC-backed; $38M Series B co-led by Third Point Ventures & DTCP (2024-10); M12, Intel Capital, Vertex
ownership_confidence: high
funding_total: ~$55M+
last_funding: Series B $38M (2024-10)
deployment: [saas, api]
target_customer: enterprise / regulated (Fortune 500; financial services, tech, manufacturing, energy, pharma)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [agent-security, ai-spm, copilots, low-code, red-teaming]
---

# Zenity

> Primary category: [[agent-runtime-security]]. Also spans [[ai-spm]].

**One-liner** — An end-to-end security and governance platform for AI agents, enterprise copilots, and low-code/no-code apps — giving security teams visibility into and control over what agents can do.

## What it does
Zenity discovers and inventories the sprawl of AI agents, copilots, and low-code/no-code automations across an enterprise (it cites large enterprises averaging ~80,000 of them), assesses their risk and misconfigurations, and governs/protects their behavior at runtime. It made its name finding that a large share of copilots and low-code apps ship with security vulnerabilities, and on offensive research showing how agents can be hijacked (prompt injection, "living off AI," AgentFlayer). The product combines **AI-SPM** (discovery + posture for agents/copilots) with **agent runtime** protection and governance.

## Where it sits in the stack
Primary [[agent-runtime-security]] (runtime visibility + control over agent behavior), with deep overlap into [[ai-spm]] (inventory + posture of the agent/copilot estate). Layer: model/prompt. It addresses all three lethal-trifecta legs for agents — detects **untrusted input** (prompt injection into copilots/agents), watches **sensitive data** agents can reach, and constrains agent **actions/egress**. The Zenity/Noma pair is the canonical example of the **AI-SPM ↔ agent-runtime overlap** in this taxonomy.

## Deployment & architecture
SaaS control plane with API integrations into the agent/copilot platforms it secures — Microsoft Copilot Studio / Power Platform, Salesforce, ServiceNow, OpenAI/Anthropic-based agents, and other low-code/agent ecosystems — plus connectors for posture scanning and runtime monitoring of agent activity. Findings export to SIEM/SOC. Strong Microsoft alignment (M12 is an investor; CEO is ex-Microsoft).

## Positioning & differentiators
Known as an early, research-forward leader in **AI agent and copilot security** — CTO Michael Bargury's offensive research (Black Hat / DEF CON talks on copilot and agent exploitation) is core to the brand. Differs from [[noma-security]] (which came up via ML/data-pipeline AI-SPM) by its origin in **low-code/copilot** security and its runtime-governance emphasis. Differs from runtime AI-firewall players like [[prisma-airs]], [[straiker]], and [[operant-ai]] by focusing on the agent/copilot control plane (what agents are configured to do and access) rather than just inline prompt/response filtering.

## Ownership, funding & M&A
Independent, VC-backed. Founded 2021 by Ben Kliger (CEO, ex-Microsoft cloud workload protection product leader) and Michael Bargury (CTO). **$38M Series B (Oct 29, 2024) co-led by Third Point Ventures and DTCP**, with Microsoft's M12, Intel Capital, and Vertex Ventures; total raised over $55M. No M&A; no seed acquisition flag. Ownership confidence: high.

## CTO / hedge-fund lens
**Day-2**, becoming Day-1 fast for shops deploying Microsoft Copilot / Copilot Studio, Power Platform, or other low-code agents at scale — exactly the "citizen developer builds an agent that can touch sensitive data" risk. For a hedge fund running M365 Copilot or building internal agents, Zenity is one of the more relevant agent-security names; it gives the SOC an inventory and guardrails over agent behavior, useful for both security and SR 11-7-style model/agent oversight. Less relevant if you have essentially no agent/copilot footprint.

## Competitors / alternatives
[[noma-security]], [[straiker]], [[operant-ai]], [[lasso-security]], [[prisma-airs]], [[reco]], [[apex-security]].

## Open questions / to verify
- Runtime enforcement depth — does it block agent actions inline, or mostly detect + govern via the platform APIs?
- Coverage beyond the Microsoft/low-code ecosystem for code-built agents.
- Any funding since the Oct 2024 Series B.

## Sources
- [Zenity Raises $38M Series B (zenity.io newsroom)](https://zenity.io/company-overview/newsroom/company-news/zenity-raises-38m-series-b-funding-round-to-secure-agentic-ai) — fetched 2026-06-28 — supports: founders, HQ, Series B $38M/date/investors, total funding, product scope, customers; confidence: high (vendor release).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/VC-backed, founded 2021 (Kliger/Bargury, Tel Aviv), $38M Series B (2024-10, Third Point & DTCP), $55M+ total. Confirmed agent-runtime + AI-SPM dual scope (the canonical AI-SPM/agent-runtime overlap with Noma). Set ownership_confidence high.
