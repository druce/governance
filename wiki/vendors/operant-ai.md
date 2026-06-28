---
type: vendor
name: Operant AI
slug: operant-ai
categories: [agent-runtime-security]
layer: model-prompt
aliases: [Operant]
website: "https://www.operant.ai"
founded: 2020
hq: San Francisco, California, USA
ownership: independent
ownership_detail: VC-backed; ~$13.5M over 2 rounds (SineWave, Felicis, others)
ownership_confidence: high
funding_total: ~$13.5M
last_funding: undisclosed (Series A era)
deployment: [self-hosted, sdk, api]
target_customer: enterprise (Kubernetes / cloud-native AI builders)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [agent-runtime, kubernetes, cloud-native, mcp-gateway, owasp-llm]
---

# Operant AI

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md).

**One-liner** — A Kubernetes-native runtime defense platform that discovers, detects, and blocks threats against live AI apps, agents, and APIs in real time.

## What it does
Operant protects AI workloads where they actually run — in production, on Kubernetes. Its **3D Runtime Defense Suite** does three things in real time: **Discovery** (live blueprints of AI workloads, models, and APIs, including undocumented APIs and covert data flows to third-party model providers like OpenAI, Anthropic, Gemini, Cohere); **Detection** (runtime detection of OWASP LLM Top-10 threats — prompt injection, model theft, PII/secret/API-key leakage); and **Defense** (in-line blocking and redaction of sensitive data flows, quarantine of suspicious containers/models, rate- and token-limiting of AI endpoints). Add-ons include **AI Gatekeeper** (runtime protection for AI agents/apps across hybrid cloud) and an **MCP Gateway** (runtime defense for MCP-connected AI apps).

## Where it sits in the stack
Primary [agent-runtime-security](../categories/agent-runtime-security.md) — protection of live agentic/AI applications — with the runtime-firewall behavior of [ai-runtime-security](../categories/ai-runtime-security.md) and an [mcp-gateway](../categories/mcp-gateway.md) product. Layer: model/prompt, but enforced at the cloud-native infrastructure/runtime layer. It breaks all three lethal-trifecta legs inline: screens **untrusted input** (prompt injection), blocks **sensitive-data** leakage (PII/secrets redaction), and controls **egress** (third-party API/data-flow blocking, token limits). Sits in the runtime path of green/yellow-zone AI workloads.

## Deployment & architecture
**Self-hosted, Kubernetes / cloud-native.** Single-step install of a runtime agent (eBPF/sidecar-style) that observes and enforces inside the cluster — distinct from SaaS-control-plane posture tools. This makes it a fit for teams that run their own AI on K8s and want inline enforcement, not just a dashboard. Integrates around the cloud-native stack and third-party model APIs; the MCP Gateway secures agent↔tool (MCP) traffic.

## Positioning & differentiators
Known for being **runtime-first and infrastructure-native** — it lives in the Kubernetes data path and does inline blocking/redaction, where neighbors like [noma-security](noma-security.md), [zenity](zenity.md), and [cranium](cranium.md) lean on SaaS control planes and posture/governance. Closest comparators on the inline-enforcement axis are [prisma-airs](prisma-airs.md) and [straiker](straiker.md) (AI-firewall runtime) and, for tool/MCP traffic, dedicated [mcp-gateway](../categories/mcp-gateway.md) players. Its differentiator is the cloud-native deployment model and OWASP-LLM-runtime coverage rather than red-teaming or compliance.

## Ownership, funding & M&A
Independent, VC-backed. Founded 2020 by Vrajesh Bhavsar (CEO), Priyanka Tembey, and Ashley Roof; HQ San Francisco. ~$13.5M raised over two rounds from SineWave Ventures, Felicis, Alumni Ventures, Calm Ventures, Gaingels, and others. No M&A; no seed acquisition flag. Ownership confidence: high. (Funding figure from third-party profiles; no large disclosed round found — treat exact total as medium confidence.)

## CTO / hedge-fund lens
**Day-2**, and specifically for shops that **build and run their own AI/agent workloads on Kubernetes**. If your AI is self-hosted containers and microservices, Operant gives you inline runtime protection and data-flow control that a SaaS posture tool can't — and the MCP Gateway is timely if you're wiring agents to tools. If your AI footprint is SaaS assistants and API calls behind an [ai-gateway](../categories/ai-gateway.md), Operant's K8s-native model is a poor fit. Most hedge funds aren't running large self-hosted AI estates, so relevance is conditional on engineering posture.

## Competitors / alternatives
[prisma-airs](prisma-airs.md), [straiker](straiker.md), [zenity](zenity.md), [noma-security](noma-security.md), [lasso-security](lasso-security.md), [apex-security](apex-security.md).

## Open questions / to verify
- Exact funding total and latest round date (third-party figures only).
- Enforcement mechanism specifics (eBPF vs sidecar vs admission controller).
- Traction outside cloud-native-heavy engineering orgs.

## Sources
- [Operant AI Announces 3D Runtime Defense Suite (GlobeNewswire)](https://www.globenewswire.com/news-release/2024/11/12/2979274/0/en/Operant-AI-Announces-3D-Runtime-Defense-Suite-to-Secure-Live-AI-Workloads.html) — fetched 2026-06-28 — supports: product architecture, K8s-native, discovery/detection/defense, OWASP LLM; confidence: high (vendor release).
- [Operant AI profile (Tracxn) + AI Gatekeeper / MCP Gateway releases](https://tracxn.com/d/companies/operant-ai/__ei9GBSPqL_n7OUu-qQX8ay9wSRQWkT215htbu1Ey50M) — fetched 2026-06-28 — supports: founding 2020, founders, HQ, ~$13.5M funding; confidence: medium (aggregator + vendor releases).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent/VC-backed (~$13.5M), founded 2020 (Bhavsar/Tembey/Roof, San Francisco), Kubernetes-native runtime defense + AI Gatekeeper + MCP Gateway. Set ownership_confidence high; funding figure medium confidence.
