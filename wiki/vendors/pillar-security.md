---
type: vendor
name: Pillar Security
slug: pillar-security
categories: [ai-runtime-security, ai-spm]
layer: model-prompt
aliases: []
website: "https://www.pillar.security"
founded: 2023
hq: Tel Aviv, Israel (US presence in Miami)
ownership: independent
ownership_detail: Independent, VC-backed; $9M seed led by Shield Capital announced 2025-04-16. No M&A.
ownership_confidence: high
funding_total: ~$9M
last_funding: Seed, $9M, 2025-04-16
deployment: [saas, api, sdk]
target_customer: enterprise (AI builders / dev teams in regulated and mid-market+ orgs)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ai-security, israel, runtime-guardrails, ai-spm, red-teaming, agent-security]
---

# Pillar Security

> Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). Also [ai-spm](../categories/ai-spm.md).

**One-liner** — An Israeli startup selling an end-to-end platform that discovers an
organization's AI assets and agents, red-teams them, and then wraps them in adaptive
runtime guardrails (an AI firewall) against prompt injection, data leakage, and tool abuse.

**Categories** — [ai-runtime-security](../categories/ai-runtime-security.md), [ai-spm](../categories/ai-spm.md)

## What it does

Pillar pitches one platform spanning the AI application lifecycle, with three connected jobs:

- **Discovery / inventory (AI-SPM):** automatically maps AI assets — models, datasets,
  prompts, notebooks, frameworks, MCP servers, tools, and agents — including shadow AI and
  unapproved coding agents. Flags which agents touch sensitive data (PII, code repos,
  production DBs) and what each agent is permitted to do.
- **Red teaming:** simulates attacks against discovered AI surfaces. Pillar markets a
  "RedGraph" approach that uses environmental context to map exploitable surfaces and
  simulate multi-turn attacks, tool hijacking, and lateral movement across an agent ecosystem.
- **Runtime guardrails (AI firewall):** adaptive input/output guardrails calibrated per
  application/agent that block prompt injection (direct and indirect), jailbreaks, PII/PCI
  leakage, secret exposure, and toxic/inappropriate content in real time. Pillar emphasizes
  behavioral-deviation detection (flagging when an agent strays from its defined business
  purpose) and taint analysis that traces PII/secrets from source to destination, rather
  than only static rule matching.

The selling idea is that findings flow between the three: red-teaming and production
telemetry feed the guardrails, which "continuously evolve." (Capability claims here are
vendor marketing; the gateway integration below is independently documented.)

## Where it sits in the stack

Primary home is [ai-runtime-security](../categories/ai-runtime-security.md) (the AI-firewall layer, `model-prompt`), with a
strong second foot in [ai-spm](../categories/ai-spm.md) (discovery/posture, `governance`-adjacent). Because it
also red-teams models, it overlaps the [ai-red-teaming](../categories/ai-red-teaming.md) category, and its agent-behavior
monitoring overlaps [agent-runtime-security](../categories/agent-runtime-security.md).

Lethal-trifecta role: Pillar is one of the few single vendors that touches all three legs —
it inspects **untrusted input** (prompt-injection / jailbreak detection on the way in),
guards **sensitive data** (PII/PCI/secret detection and taint tracing), and constrains
**egress** (blocking leakage and out-of-purpose tool/agent actions on the way out). It is
relevant to the yellow (model/agent) zone where untrusted content meets privileged tools.

## Deployment & architecture

SaaS control plane. The runtime guardrail is consumed primarily as an **API** — Pillar
exposes a guardrail API that AI gateways call on each request. It is natively integrated
into [litellm](litellm.md)/LiteLLM Proxy (via the Generic Guardrail API, `api_base
https://api.pillar.security/api/v1/integrations/litellm`, with `pre_call` / `post_call` /
`during_call` modes) and into the TrueFoundry AI Gateway, so customers can turn protection
on with a config change rather than re-architecting traffic. SDK / code-side hooks support
the build-time discovery and red-teaming. It is *not* its own inline TLS-intercepting
network proxy — it rides on top of an existing [ai-gateway](../categories/ai-gateway.md). Integrations span code
repos, AI/ML and data platforms, MCP servers (connection mapping + allowlisting), and
audit/compliance logging; it also appears in the Wiz integration marketplace.

## Positioning & differentiators

Pillar's pitch is **breadth across the lifecycle in one product** — discover, test, then
protect — versus point tools that do only one. Against nearest neighbors:

- vs [lakera](lakera.md), [prompt-security](prompt-security.md), [enkrypt-ai](enkrypt-ai.md) — these center on the runtime guardrail
  / prompt-firewall; Pillar bundles that with discovery (AI-SPM) and red-teaming.
- vs [splxai](splxai.md) — SplxAI leans red-teaming/testing-first; Pillar offers red-teaming plus
  production runtime in one.
- vs [prisma-airs](prisma-airs.md) and [cisco-ai-defense](cisco-ai-defense.md) — platform-scale incumbents (Palo Alto, Cisco)
  with broader security portfolios and channel; Pillar is a focused startup competing on
  depth in AI-native, agent-aware protection.
- vs [witnessai](witnessai.md) — WitnessAI is more about employee/shadow-AI access governance (CASB-for-AI);
  Pillar targets the teams *building* AI apps/agents.
- vs [hiddenlayer](hiddenlayer.md) — HiddenLayer's heritage is model/ML-supply-chain security (model
  scanning, MLDR); Pillar is more application/agent-runtime and prompt-centric.
- vs [pangea](pangea.md) — Pangea sells composable AI-security API building blocks; Pillar sells a
  more opinionated, integrated platform.

Differentiators it stresses: agent-centric behavioral monitoring (deviation from intended
purpose), taint tracing of sensitive data, and a feedback loop from red-teaming + telemetry
(claims ~50M+ AI application interactions of threat intel) into adaptive guardrails.

## Ownership, funding & M&A

Independent, VC-backed. Founded 2023 by Dor Sarig (CEO; ex–Israeli MoD, Perimeter81,
Cymulate) and Ziv Karliner (CTO). Raised a **$9M seed** announced **2025-04-16**, led by
**Shield Capital**, with **Golden Ventures**, **Ground Up Ventures**, and strategic angels.
HQ Tel Aviv, with a US footprint in Miami. **No M&A** — not acquired, no acquisitions
(no seed M&A flag). Ownership confidence: high (primary press release + multiple
independent press).

## CTO / hedge-fund lens

This is a **Day-1** control *if you are building or running your own AI applications/agents*
(internal copilots over fund data, RAG assistants, agentic workflows) — it provides the
prompt-injection / data-leak / egress guardrail you cannot safely launch without, plus an
inventory of what AI you actually have. For a fund that only *consumes* SaaS AI
(ChatGPT/Copilot) and isn't building, a CASB-for-AI like [witnessai](witnessai.md) or a gateway-native
guardrail may matter more, and Pillar is closer to Day-2/optional. SR 11-7 / model-risk
relevance is indirect: its red-teaming evidence and runtime logs can feed model-risk and
audit, but it is a security tool, not a governance/attestation platform like
[ai-governance-platform](../categories/ai-governance-platform.md) vendors. Fit: medium for a hedge fund — high if you have an
in-house AI build team, lower if you don't. Caveat: small, early-stage (seed) vendor —
weigh vendor-risk and roadmap maturity against incumbents.

## Competitors / alternatives

[lakera](lakera.md), [prompt-security](prompt-security.md), [enkrypt-ai](enkrypt-ai.md), [splxai](splxai.md), [prisma-airs](prisma-airs.md),
[cisco-ai-defense](cisco-ai-defense.md), [witnessai](witnessai.md), [hiddenlayer](hiddenlayer.md), [pangea](pangea.md), [calypsoai](calypsoai.md), [trojai](trojai.md),
[aim-security](aim-security.md)

## Open questions / to verify
- Exact pricing / packaging (per-app, per-request, platform) — not public.
- How much of the runtime is genuinely model-agnostic vs gateway-dependent.
- Customer count / production references — limited public evidence (seed-stage).
- Whether HQ is best described as Tel Aviv or dual Tel Aviv/Miami; both appear in sources.
- Any funding since the 2025-04 seed.

## Sources
- [Pillar Security Raises $9M to Help Enterprises Build and Run Secure AI Software (GlobeNewswire)](https://www.globenewswire.com/news-release/2025/04/16/3062627/0/en/Pillar-Security-Raises-9M-to-Help-Enterprises-Build-and-Run-Secure-AI-Software.html) — fetched 2026-06-28 — supports: $9M seed, 2025-04-16, Shield Capital + Golden/Ground Up, founders, Tel Aviv HQ, product scope; confidence: high
- [Pillar Security Platform page](https://www.pillar.security/platform) — fetched 2026-06-28 — supports: discovery/AI-SPM, RedGraph red-teaming, runtime guardrails, agent/MCP focus (vendor marketing); confidence: med
- [Pillar Security guardrail integration (LiteLLM proxy docs)](https://docs.litellm.ai/docs/proxy/guardrails/pillar_security) — fetched 2026-06-28 — supports: API guardrail deployment behind AI gateway, scan categories (prompt injection, jailbreak, PII/PCI, secrets), pre/post/during-call modes; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023 (Sarig/Karliner), Tel Aviv HQ (+Miami), independent with $9M seed led by Shield Capital (2025-04-16, no M&A), API/SaaS/SDK deployment as a gateway-integrated guardrail (LiteLLM/TrueFoundry), trifecta coverage on all three legs, hedge_fund_fit medium. Filled frontmatter and all body sections; cached 3 sources.
