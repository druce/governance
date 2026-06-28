---
type: vendor
name: Lasso Security
slug: lasso-security
categories: [dlp, ai-runtime-security, agent-runtime-security, ai-access-governance]
layer: data
aliases: [Lasso]
website: https://www.lasso.security
founded: 2023
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: Independent, VC-backed. $6M seed led by Entrée Capital (Samsung Next) announced 2023-11-20; later SAFE/round activity reported by aggregators but post-seed totals unverified.
ownership_confidence: high
funding_total: "$6M seed verified; later rounds reported (~$28M cited by aggregators) but unverified"
last_funding: Seed $6M (2023-11-20); later rounds reported 2024-2025 (unverified)
deployment: [saas, inline-proxy, api, sdk]
target_customer: enterprise / mid-market (AI-adopting orgs, AppSec + dev teams)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [genai-security, llm-security, mcp, shadow-ai, israel]
---

# Lasso Security

> Primary category: [[dlp]]. Spans [[ai-runtime-security]], [[agent-runtime-security]], and [[ai-access-governance]].

**One-liner** — An Israeli end-to-end GenAI security platform that watches every LLM and
agent touchpoint (employee chatbots, built apps, MCP tools) to stop sensitive-data leakage,
prompt injection, and shadow-AI sprawl in real time.

## What it does

Lasso protects the full lifecycle of LLM/GenAI use inside an enterprise. It does three jobs
that the wiki splits across categories:

- **Shadow-AI discovery** — its Discover module maps the AI models, agents, and apps in use
  across the org, including unapproved ("shadow") tools employees adopt on their own.
- **Context-based data protection / DLP** — inspects prompts and model responses for
  sensitive-data disclosure and policy violations, and can block before data egresses to an
  LLM.
- **Runtime guardrails** — detection models (trained on a large, frequently-updated corpus
  of prompt-injection and jailbreak attempts) screen inputs and outputs for prompt
  injection, jailbreaks, malicious code generation, model/data exfiltration.
- **Agent / MCP security** — an open-source MCP Gateway plus an "Intent Security Framework"
  that baselines what an agent should do, which tools it should call, and what data it
  should touch, then flags deviations.

The pitch to a CTO: one platform to see and govern both *human* AI use (employees pasting
into ChatGPT) and *built* AI (your own LLM apps and agents), rather than buying a separate
shadow-AI tool, an AI firewall, and an agent-security tool.

## Where it sits in the stack

Primary home is [[dlp]] (Data layer) because the headline job is keeping sensitive data out
of prompts and responses. But Lasso is genuinely cross-layer:

- [[ai-runtime-security]] (Model/Prompt layer) — inline guardrails / AI-firewall function.
- [[agent-runtime-security]] — MCP Gateway + intent baselining for agentic apps.
- [[ai-access-governance]] — shadow-AI discovery and employee-AI control via browser extension.

**Lethal-trifecta role:** addresses all three legs — screens **untrusted input** (prompt
injection/jailbreak detection), guards **sensitive data** (DLP on prompts/responses), and
controls **egress** (blocking leakage to external LLMs and via MCP tool calls). It lives at
the boundary between the green zone (internal data/agents) and the red zone (external models
and tools).

## Deployment & architecture

Multiple insertion points rather than a single chokepoint:

- **Browser extension** — "Lasso for Employees," to see and control AI use in the browser
  (shadow-AI, employee chatbot guardrails).
- **Inline / reverse proxy + API gateway + SDK** — "Lasso for Applications," to wrap your
  own LLM apps; enforce policy inline at the proxy, API, or AI-gateway layer.
- **Open-source MCP Gateway** — a proxy/orchestrator for Model Context Protocol traffic
  (on GitHub, Smithery, MCP Servers), for agentic workflows.
- **SaaS** control plane with dashboards/observability.

Integrations include AI gateways — e.g. Lasso ships as a guardrail in [[portkey]]'s gateway.
Vendor performance claims (marketing): sub-50ms decisions, 99.8% detection accuracy.

## Positioning & differentiators

- **Breadth** is the story: most neighbors pick one lane (pure DLP, pure AI firewall, pure
  shadow-AI). Lasso spans employee AI + built AI + agents/MCP under one platform.
- **MCP/agent focus early** — it shipped an open-source MCP security gateway (Apr 2025) and
  markets an agent "Intent Security Framework," positioning it toward agentic deployments,
  not just chatbot DLP.
- **Origin in LLM threat research** — leans on a large prompt-injection/jailbreak dataset as
  the basis for its detection models.

Nearest neighbors: [[prompt-security]] (very similar end-to-end GenAI scope; acquired by
SentinelOne), [[witnessai]] (runtime + AI access governance), [[harmonic-security]] and
[[cyberhaven]] (shadow-AI / DLP for AI), [[nightfall-ai]] and [[mind]] (data-centric DLP),
[[pillar-security]] and [[hiddenlayer]] (AI runtime), [[zenity]] (agent runtime).

## Ownership, funding & M&A

- **Independent**, VC-backed. **No M&A** — Lasso has not been acquired (and the seed
  registry carried no acquisition flag). Confidence: high that it remains independent.
- **Seed: $6M, announced 2023-11-20**, led by **Entrée Capital** with **Samsung Next**
  (verified, vendor + SecurityWeek). Confidence high.
- **Later funding:** aggregators (Crunchbase/PitchBook/Tracxn) report additional SAFE/round
  activity in 2024-2025 (e.g. a ~$10M SAFE in mid-2025 reportedly including CyberArk
  Ventures and Singtel Innov8, and a Series A reported late 2025; ~$28M total cited). These
  are **not confirmed against a primary source** and figures conflict between aggregators —
  treat post-seed totals as unverified.

## CTO / hedge-fund lens

- **Day-1-ish, but as a consolidation play.** A fund's Day-1 AI controls are "stop staff
  leaking data into ChatGPT" (shadow-AI + DLP) and "guardrail any internal LLM app." Lasso
  covers both, plus agent/MCP for when you go agentic (Day-2). For a small fund that wants
  one vendor instead of three, that breadth is attractive.
- **Model-risk / SR 11-7:** Lasso is a control/monitoring layer, not a model-governance
  platform — it helps with the data-leakage and prompt-abuse side, not model validation or
  documentation. Pair with an [[ai-governance-platform]] for SR 11-7 obligations.
- **Fit:** medium. Strong for a shop standing up employee AI + a few internal LLM/agent
  apps and wanting a single pane. Less compelling if you already own DLP via
  [[netskope]]/[[microsoft-purview]] or an AI firewall via [[prisma-airs]]. Early-stage
  vendor — diligence the roadmap, support, and SOC 2 posture.

## Competitors / alternatives

[[prompt-security]], [[witnessai]], [[harmonic-security]], [[cyberhaven]], [[nightfall-ai]],
[[mind]], [[pillar-security]], [[hiddenlayer]], [[prisma-airs]], [[zenity]].

## Open questions / to verify

- Post-seed funding: confirm the 2024-2025 round(s), exact amounts, investors, and total
  raised against a primary source (current data is aggregator-only and conflicting).
- Confirm the four co-founders (Elad Schulman CEO; Lior Ziv, Ophir Dror, Yuval Abadi per
  press) — names not all in vendor primary docs.
- Customer base / scale and compliance certifications (SOC 2, ISO) — not established.

## Sources

- [Lasso Security Emerges from Stealth With $6M Seed Funding (vendor)](https://www.lasso.security/resources/lasso-security-funding-announcement-2023) — fetched 2026-06-28 — supports: founded 2023, Tel Aviv HQ, $6M seed (Entrée Capital, Samsung Next, 2023-11-20), product scope; confidence: high.
- [LLM Security Startup Lasso Emerges From Stealth Mode (SecurityWeek)](https://www.securityweek.com/llm-security-startup-lasso-emerges-from-stealth-mode/) — fetched 2026-06-28 — supports: independent corroboration of founding/HQ/seed and GenAI-security scope; confidence: high.
- [Lasso Launches First Open-Source Security Gateway for MCP (vendor)](https://www.lasso.security/resources/lasso-releases-first-open-source-security-gateway-for-mcp) — fetched 2026-06-28 — supports: MCP/agent runtime security, open-source proxy deployment (2025-04-15); confidence: high.
- [Lasso platform / deployment overview (vendor + aggregated)](https://www.lasso.security/) — fetched 2026-06-28 — supports: deployment modes (browser extension, SDK, reverse proxy, API gateway), Discover/Guardrails/Intent modules, Portkey integration; performance claims are marketing; later-funding figures unverified; confidence: medium.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founding (2023), HQ (Tel Aviv), independent ownership, $6M seed (Entrée Capital/Samsung Next, 2023-11-20, verified). Confirmed cross-layer scope (DLP + AI runtime + agent/MCP + shadow-AI) and deployment (browser extension, inline/reverse proxy, API gateway, SDK, open-source MCP Gateway). No M&A. Post-seed funding reported by aggregators but left unverified. Set status: researched; sources_count 4.
