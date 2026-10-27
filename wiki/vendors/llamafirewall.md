---
title: LlamaFirewall (Meta)
type: vendor
name: LlamaFirewall (Meta)
slug: llamafirewall
aka: [Meta LlamaFirewall, PromptGuard 2, Prompt Guard 2, AlignmentCheck, CodeShield, PurpleLlama]
primary_category: agent-runtime-security
also_listed_in: [ai-runtime-security, ai-red-teaming]
website: https://meta-llama.github.io/PurpleLlama/LlamaFirewall/
founded: 2025
hq: Menlo Park, CA (Meta)
ownership_state: oss-vendor-backed
owner: "Meta Platforms (NASDAQ: META)"
ownership_note: 'Open-source framework (MIT) published by Meta inside its PurpleLlama repo; announced 2025-04-29. Not a company. The PromptGuard 2 models it uses are under Meta''s Llama community licence and gated on Hugging Face. Last PyPI release 1.0.3 on 2025-05-29; 2026 commits are housekeeping only.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (Meta-funded OSS project)
last_funding: n/a
market_position: {agent-runtime-security: niche-specialist, ai-runtime-security: niche-specialist, ai-red-teaming: niche-specialist}
deployment_model: [self-hosted]
form_factor: [sdk]
data_leaves_tenancy: partial
integrations: [openai-agents-sdk, langchain, langgraph, huggingface, together-ai, semgrep]
mcp_support: none
certifications: []
pricing_model: OSS (free)
fs_traction: unverified
target_customer: engineering teams building their own LLM agents who want an in-process, self-hosted guardrail layer
last_verified: 2026-10-26
verify_after: null
tags: [open-source, meta, guardrails, prompt-injection, agents, code-security]
sources:
  - {claim: launch-date-components, url: "https://thehackernews.com/2025/04/meta-launches-llamafirewall-framework.html", date: 2025-04-30, confidence: high}
  - {claim: paper-benchmarks-production-use, url: "https://arxiv.org/abs/2505.03574", date: 2025-05-06, confidence: high}
  - {claim: readme-license-setup, url: "https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall", date: 2026-10-26, confidence: high}
  - {claim: release-cadence, url: "https://pypi.org/project/llamafirewall/", date: 2026-10-26, confidence: high}
  - {claim: limitations, url: "https://www.infoq.com/news/2025/05/llamafirewall-agent-protection", date: 2025-05-13, confidence: medium}
---

# LlamaFirewall (Meta)

> **One-liner** — Meta's open-source (MIT) Python guardrail framework for **LLM agents**.
> It chains three scanners:
>
> - **PromptGuard 2**, a small prompt-injection/jailbreak classifier
> - **AlignmentCheck**, an LLM that audits the agent's reasoning for goal hijacking
> - **CodeShield**, static analysis of code the agent writes
>
> You call it from your own agent code; it is not a product or a proxy.

**Categories** — [agent-runtime-security](../categories/agent-runtime-security.md)
(primary), [ai-runtime-security](../categories/ai-runtime-security.md),
[ai-red-teaming](../categories/ai-red-teaming.md) (guardrails half)

## What it does

LlamaFirewall is a policy layer that runs a set of **scanners** at different points
in an agent's loop and returns allow or block with a score:

- **PromptGuard 2** — a fine-tuned BERT-style classifier, in 86M and 22M parameter
  variants, that flags direct prompt injection and jailbreak text. It runs on user input
  and on untrusted content the agent reads, such as web pages and tool results. It is
  fast and runs locally.
- **AlignmentCheck** — an *experimental* chain-of-thought auditor. A separate LLM reads
  the agent's trace (user goal, then the agent's reasoning and actions) and flags when
  the agent's behaviour has drifted from what the user asked. This is the signature of
  indirect prompt injection or goal hijacking. Meta's results used Llama 4 Maverick or
  Llama 3.3 70B as the judge.
- **CodeShield** — Semgrep and regex rules across 8 languages that scan LLM-generated code
  for insecure patterns before it is committed or executed.
- **Regex and custom scanners** — your own patterns or simple LLM-prompt checks.

You call `scan()` per message or `scan_replay()` over a whole trace. Meta ships demos
wiring it into the OpenAI Agents SDK guardrail hook and a LangChain/LangGraph agent.

## Agent-security role: the lethal trifecta

LlamaFirewall works on the **untrusted-input** leg. PromptGuard screens content
entering the context, and AlignmentCheck tries to catch the *effect* of injected
instructions: an agent that starts doing something the user didn't ask for, such as
reading secrets or calling an exfiltration tool. That can cut the chain before the
**egress** step. It does **not** control what data the agent can reach, what tools it
holds or where it can send data. Those are jobs for authorization, MCP gateways and
sandboxing ([nvidia-openshell](nvidia-openshell.md),
[mcp-gateway](../categories/mcp-gateway.md),
[authorization-engine](../categories/authorization-engine.md)). Treat it as a detection
layer inside the agent, not a containment boundary. Because it is a probabilistic
detector, Meta's own benchmark still shows residual attack success.

## Deployment & data handling

- Python library (`pip install llamafirewall`, Python 3.10+). It runs in-process in
  your agent. Self-hosted only, no SaaS and no proxy.
- Guard models download from Hugging Face. PromptGuard 2 is a **gated** model under
  Meta's Llama community licence, so you need an HF account and must accept the licence.
- **AlignmentCheck's documented setup calls a hosted LLM through Together AI**
  (`TOGETHER_API_KEY`). In that default, agent traces, which may hold sensitive data,
  leave your tenancy. Pointing it at a self-hosted Llama is architecturally possible;
  the paper treats the judge model as configurable, but the README documents only
  Together. Hence `data_leaves_tenancy: partial`. PromptGuard and CodeShield run locally.
- Inline and synchronous. PromptGuard adds small latency. AlignmentCheck adds a full
  large-LLM call per check and lists "reduced latency" as future work.

## Positioning & differentiators

- **Agent-specific, not just prompt filtering.** [nemo-guardrails](nemo-guardrails.md)
  and [guardrails-ai](guardrails-ai.md) focus on chat I/O rails and validators.
  LlamaFirewall's distinctive piece is AlignmentCheck, which audits the agent's reasoning
  trajectory against user intent. CodeShield also targets coding agents specifically.
- **vs commercial agent runtime security** ([zenity](zenity.md),
  [lasso-security](lasso-security.md), [straiker](straiker.md),
  [operant-ai](operant-ai.md)): those bring discovery, a policy console, SIEM export and
  coverage of third-party agent platforms. LlamaFirewall is a free component for agents
  *you* write, with no management plane.
- **vs commercial AI firewalls** ([lakera](lakera.md), [prisma-airs](prisma-airs.md),
  [hiddenlayer](hiddenlayer.md)): PromptGuard 2 is a credible free prompt-injection
  classifier. The commercial products add continuously updated threat models, hosted
  low-latency inference and support.
- **Benchmark claim (Meta's own numbers on AgentDojo):** attack success fell from 17.6%
  to 1.75% with PromptGuard 2 plus AlignmentCheck. Task utility fell from 47.7% to 42.7%.
  These figures are not independently reproduced.

**Position labels:** *niche-specialist* in all three categories: a reference-grade OSS
toolkit from a model lab, used by teams that build their own agents, not a market
product with a support or management plane.

## Who should choose them / anti-fit

- **Choose** if you build agents in Python, especially coding agents or agents that read
  web or email content, and want a free in-process layer. Use PromptGuard on untrusted
  inputs and CodeShield on generated code. Pilot AlignmentCheck with a self-hosted judge
  model. It also works as a reference design when evaluating commercial agent-security
  vendors.
- **Anti-fit:**
  - Firms consuming SaaS agents (Copilot, ChatGPT agents). There is nothing to hook
    into.
  - Buyers who need a supported product, dashboards, SIEM integration or policy
    management.
  - Anyone who cannot send agent traces to Together AI and lacks the GPU capacity to
    self-host a 70B-class judge model.
  - Shops that need active maintenance and fast threat-model updates.

## Known weaknesses / gotchas

- **Maintenance cadence:** the last PyPI release was **1.0.3 on 2025-05-29**. Commits
  touching LlamaFirewall in 2026 (Jun–Aug) are type-checking and lint housekeeping, not
  features. Treat it as a published research artifact with light upkeep, not an evolving
  product. Steward risk sits with Meta's priorities.
- **AlignmentCheck is labelled experimental** by Meta. It is costly (an LLM call per
  check), and small judge models hurt agent utility significantly per the paper.
- **CodeShield is not comprehensive.** Meta reports 96% precision and 79% recall and says
  it may miss context-dependent vulnerabilities.
- **Licensing split:** the framework is MIT, but the PromptGuard 2 weights are under the
  Llama community licence and gated. Legal should review that licence, not just MIT.
- **Default data path:** AlignmentCheck setup sends traces to Together AI (see above).

## Ownership & viability

A Meta Platforms (NASDAQ: META) open-source project, part of the **PurpleLlama** AI
security tooling repo alongside Llama Guard and CyberSecEval. Announced
**2025-04-29**, together with an updated Llama Guard, CyberSecEval 4 and the "Llama for
Defenders" programme. PyPI 1.0.0 was published the same day. Paper: arXiv 2505.03574
(v1 2025-05-06, 19 Meta authors), which states LlamaFirewall "is utilized in production at
Meta". No funding or M&A applies. No 2026 product news found as of 2026-10-26.

## Integrations & partnerships

- Demos: OpenAI Agents SDK (guardrail hook), LangChain/LangGraph agent.
- Dependencies: Hugging Face (model download), Together AI (AlignmentCheck default),
  Semgrep rules (CodeShield).
- MCP: no MCP-specific support documented. You could scan tool results yourself.
- No marketplace listings, commercial partners or support channels. GitHub issues on
  PurpleLlama only.

## Compliance & FS traction

None. It is a library. No named external production adopters or FS users found.

## Commercial

Free. MIT framework; Llama community licence on the PromptGuard models. Hidden costs are
the judge-model inference for AlignmentCheck (Together AI usage or your own GPUs) and
engineering integration time.

## CTO / hedge-fund lens

**Day-2, and only if you build agents in-house.** For a fund with a small platform team
writing research or ops agents, PromptGuard 2 on every untrusted input is a sensible,
cheap default. Commercial guardrail vendors often benchmark against it, which makes it a
useful baseline. AlignmentCheck is the interesting idea but is experimental, slow and,
by default, ships traces off-tenancy. Do not rely on it as your control for agents that
touch MNPI or can move data. Put hard limits on tool access and egress first; detection
layers like this sit on top.

## Open questions / to verify

- Whether Meta still actively develops LlamaFirewall (no release since 2025-05-29), or
  whether a successor exists in Llama Stack or a newer PurpleLlama component.
- Supported judge-model backends for AlignmentCheck beyond Together AI (self-hosted vLLM,
  Bedrock and so on), per current code.
- Independent benchmarks of PromptGuard 2 and AlignmentCheck versus commercial detectors.
- Any external production adopters, in FS or otherwise.

## Sources

- [The Hacker News: Meta launches LlamaFirewall framework](https://thehackernews.com/2025/04/meta-launches-llamafirewall-framework.html) — fetched 2026-10-26 (published 2025-04-30) — supports: announcement 2025-04-29, components, companion releases; confidence: high
- [arXiv 2505.03574: LlamaFirewall paper](https://arxiv.org/abs/2505.03574) — fetched 2026-10-26 — supports: design, AgentDojo numbers, production use at Meta, AlignmentCheck experimental, judge models; confidence: high (vendor-authored)
- [LlamaFirewall README + LICENSE (PurpleLlama)](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) — fetched 2026-10-26 — supports: scanners, MIT, HF gated models, Together API key, OpenAI Agents/LangChain demos; confidence: high
- [PyPI: llamafirewall](https://pypi.org/project/llamafirewall/) (JSON API) — fetched 2026-10-26 — supports: release history, last release 1.0.3 on 2025-05-29; confidence: high
- [InfoQ: LlamaFirewall agent protection](https://www.infoq.com/news/2025/05/llamafirewall-agent-protection) — fetched 2026-10-26 (published 2025-05-13) — supports: CodeShield precision/recall and limitations, future work; confidence: medium
- Cached: `raw/sources/2026-10-26--llamafirewall--readme-pypi-license.md`, `raw/sources/2026-10-26--llamafirewall--paper-launch-coverage.md`

## History

- [2026-10-26] Page created (product slug `llamafirewall`; there is no Meta company page
  in the wiki). Verified the April 2025 launch (2025-04-29), MIT licence, components and
  the stale release cadence. Primary agent-runtime-security (AlignmentCheck audits agent
  trajectories), cross-listed ai-runtime-security (PromptGuard as a prompt-injection
  filter) and ai-red-teaming (guardrails half). Cached 2 sources.
