---
title: Geordie AI
type: vendor
name: Geordie AI
slug: geordie-ai
aka: [Geordie, Geordie Beam]
primary_category: agent-runtime-security
also_listed_in: [ai-spm]
website: https://www.geordie.ai
founded: 2025
hq: London, United Kingdom (New York office)
ownership_state: independent
owner: null
ownership_note: 'VC-backed, independent. $30M Series A led by Balderton Capital (announced 2026-05-28), with Crosspoint Capital (new) and General Catalyst + Ten Eleven Ventures (follow-on); $36.5M raised in total including a $6.5M seed (2025-09). Post-money valuation reported at ~$180M (Fortune, corrected, from Companies House filings); another outlet reported $155M. No acquisition found as of 2026-10-23.'
acquisition: {announced: null, closed: null, price: null}
funding_total: $36.5M
last_funding: Series A, $30M, led by Balderton Capital (announced 2026-05-28)
market_position: {agent-runtime-security: ai-native-disruptor, ai-spm: ai-native-disruptor}
deployment_model: [saas]
form_factor: [platform, agent, api]
data_leaves_tenancy: 'true'
integrations: [Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Zed, Microsoft Copilot Studio, Amazon Bedrock, AWS DevOps Agent, n8n, LangChain, Dust, Gemini, Salesforce, MCP]
mcp_support: unverified
certifications: [SOC 2 Type II (vendor-stated), SOC 3 (vendor-stated), ISO 27001 (vendor-stated)]
pricing_model: null
fs_traction: claimed
target_customer: Enterprises with a growing estate of AI agents (coding agents, low-code/agent platforms, SaaS agents) and a security team that has to inventory and govern them
last_verified: 2026-10-23
verify_after: 2027-01-23
tags: [agent-security, ai-spm, agent-discovery, runtime-steering, coding-agents, rsac-innovation-sandbox, uk]
sources:
  - {claim: "Series A $30M led by Balderton; Crosspoint, General Catalyst, Ten Eleven; $36.5M total; London; founded early 2025", url: "https://www.securityweek.com/geordie-raises-30-million-for-ai-security-and-governance-platform/", date: 2026-05-28, confidence: high}
  - {claim: "Series A details, Balderton partner James Wise joins board", url: "https://tech.eu/2026/05/29/geordie-raises-30m-to-bring-security-and-governance-to-agentic-ai/", date: 2026-05-29, confidence: high}
  - {claim: "$6.5M seed 2025-09; ~$180M post-money (Companies House); 37 employees; founders; ~30 customer environments; AlphaSense, Owkin", url: "https://fortune.com/2026/05/28/geordie-security-governance-ai-agents/", date: 2026-05-28, confidence: medium}
  - {claim: "RSAC 2026 Innovation Sandbox winner ('Most Innovative Startup'), 2026-03-23; Beam released March 2026", url: "https://www.geordie.ai/resources/geordie-ai-named-most-innovative-startup-at-rsac-2026-innovation-sandbox/", date: 2026-03-23, confidence: high}
  - {claim: "product modules, platform coverage, Beam modes, certifications, customer logos", url: "https://www.geordie.ai/", date: 2026-10-23, confidence: low}
---

# Geordie AI

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). Also listed in [ai-spm](../categories/ai-spm.md).

**One-liner** — A London agent-security startup that finds every AI agent in the
enterprise (coding agents on laptops, Copilot Studio and Bedrock agents, SaaS agents),
maps what each one can reach, flags the risky ones, and — through its **Beam** module —
steers or blocks agent actions at runtime from inside the agent rather than from a
network gateway.

## What it does

Four modules, per the vendor (2026-10-23):

- **Discovery and posture.** Inventories agents across code, cloud, endpoints and SaaS
  and maps each one's configuration: permissions, tool and MCP connections, knowledge
  sources, system prompts, models and sub-tools, "updated continuously as they change."
  Named coverage includes coding agents (Claude Code, Codex, Cursor, GitHub Copilot,
  Zed), agent platforms (Copilot Studio, Amazon Bedrock, AWS DevOps Agent, n8n,
  LangChain, Dust, Gemini) and Salesforce.
- **Behavior and risk intelligence.** "A continuous, auditable record of every prompt,
  plan, response, and tool invocation," behavioral baselining and anomaly detection,
  with findings mapped to OWASP, NIST, ISO 42001, the EU AI Act and AIUC-1.
- **Cost intelligence.** Ties agent spend to the work it produced and flags waste.
- **Beam (remediation / runtime steering).** Released March 2026. Hooks into the agent
  itself — lifecycle hooks, plugins and MCP — and runs in four modes: *Monitor*
  (record only), *Guide* (inject context and an approved alternative path), *Confirm*
  (pause for a human) and *Enforce* (binding hooks so prohibited actions do not run).
  The vendor calls this "context engineering" and pitches it as "deterministic controls
  without gateway latency."

## Where it sits in the stack

Primary [agent-runtime-security](../categories/agent-runtime-security.md): Beam acts
inside the agent loop on plans and tool calls, which is the definition of that slot.
The discovery/posture half is squarely [ai-spm](../categories/ai-spm.md) — inventory
and risk scoring of the agent estate — hence the cross-list. This is the same
posture-plus-runtime shape as [zenity](zenity.md).

In lethal-trifecta terms, Geordie works mostly on the **sensitive-data** and **egress**
legs. Discovery shows which agents hold data access and outbound tools at the same
time, which is the dangerous combination. Beam can then stop or redirect the specific
tool call that would complete the chain. It does less on the **untrusted-input** leg.
It is not primarily a prompt-injection classifier sitting in front of the model. It
works on what the agent does next, not on what text arrives.

**Survey placement notes (2026-10 CTO survey):** respondents wrote Geordie in under
*AI Runtime Security / AI Firewall* and under *LLM Observability & Eval*.

- The **AI Runtime Security** placement is an understandable neighbor, but not a match.
  Geordie is not an inline prompt/response firewall, and the vendor explicitly
  positions Beam against gateway-style inspection. It is not cross-listed to
  [ai-runtime-security](../categories/ai-runtime-security.md).
- The **LLM Observability** placement is **largely a respondent misplacement**. Geordie
  does record prompts, plans and tool calls, and it does track cost. But that record
  exists for security audit and anomaly detection. It is not a developer
  tracing/evaluation platform like [langfuse](langfuse.md) or
  [langsmith](langsmith.md): there are no eval suites or prompt versioning. The
  agent-activity record is a real feature, so the confusion is reasonable, but it does
  not justify a cross-list.

## Positioning & differentiators

- vs [zenity](zenity.md) — the closest shape (posture + runtime for agents). Zenity
  came up through Microsoft low-code and copilot security and is deep on Copilot Studio
  and Power Platform. Geordie's public coverage list leads with **developer coding
  agents** (Claude Code, Cursor, Codex) as well as low-code platforms, and its runtime
  control lives in agent hooks rather than platform APIs.
- vs [noma-security](noma-security.md) — Noma came up via AI/ML pipeline posture and is
  far better funded. Geordie is the earlier-stage, agent-only bet.
- vs gateway-style runtime players ([prisma-airs](prisma-airs.md),
  [straiker](straiker.md), [lasso-security](lasso-security.md)) — those mostly inspect
  traffic in the request path. Geordie's Beam enforces at the agent itself, which
  avoids adding latency. The tradeoff is that coverage depends on which agent runtimes
  Geordie has hooks for.
- vs agent-identity players ([token-security](token-security.md)) — Token starts from
  the non-human-identity and credential side. Geordie starts from the agent's
  configuration and behavior. They are complementary more than competing.

`market_position: ai-native-disruptor` in both categories: a 2025-founded startup with
a strong external signal (RSAC 2026 Innovation Sandbox winner, Gartner Cool Vendor
2026 per the vendor) but ~37 staff and ~30 customer environments as of 2026-05.

## Who should choose them / anti-fit

**Good fit:** a firm whose engineers and quants already run coding agents (Claude Code,
Cursor, Codex) and whose business users are building Copilot Studio or Bedrock agents,
where the security team first needs an inventory of those agents, and then a way to put
"confirm before you push to prod / email externally / touch the PM book" checkpoints on
specific agent actions without re-architecting traffic.

**Anti-fit:** shops with little or no agent footprint; firms that need on-prem or
in-tenant deployment (none documented); buyers who want a single inline AI firewall
for chatbot prompt traffic (that is [ai-runtime-security](../categories/ai-runtime-security.md));
procurement teams that will not approve an 18-month-old vendor for a production
control.

## Known weaknesses / gotchas

- **Very young.** Founded early 2025, ~37 employees (Fortune, 2026-05). The reference
  base is thin, especially in regulated finance.
- **Growth figures are vendor claims.** "1,300% ARR growth" (first five months of 2026)
  and "50x ARR growth" (H1 2026) appear in vendor-sourced coverage with no base
  disclosed. Ignore them for diligence.
- **Valuation reports disagree.** ~$180M post-money (Fortune, corrected, from Companies
  House) vs $155M (another outlet). Soft discrepancy, recorded 2026-10-23. It is not
  material to a buyer.
- **Hook-based enforcement is only as good as the hook coverage.** An agent runtime
  without a Beam integration gets discovery and monitoring, not enforcement. Ask for
  the enforcement matrix by platform.
- **Acquisition risk is high.** Agent-security startups are being bought quickly
  (Palo Alto/Protect AI, Check Point/Lakera, SentinelOne/Prompt Security). A
  well-signaled 2025 startup is an obvious target, so get change-of-control terms.

## Deployment & data handling

SaaS (the login link resolves to an EU-region instance, which suggests regional
hosting; no self-hosted option documented). Discovery uses API connectors to
agent platforms plus endpoint/code-level collection for coding agents. **Prompt, plan,
response and tool-call records leave the tenancy** to build the audit trail, so treat
Geordie as a processor of sensitive prompt content. Retention, region choice, and
training-use terms are **unverified**. Beam runs in-process via hooks, so enforcement
does not add a network hop.

## Integrations & partnerships

Named coverage (vendor list): Claude Code, Codex, Cursor, GitHub Copilot, Zed, Copilot
Studio, Amazon Bedrock, AWS DevOps Agent, n8n, LangChain, Dust, Gemini, Salesforce,
and MCP connections. NVIDIA Inception member. SIEM/SOAR export targets and IdP
integrations are not documented publicly. `mcp_support` is left `unverified`: Geordie
discovers MCP connections and Beam can operate through MCP, but it is not an MCP
gateway in the [mcp-gateway](../categories/mcp-gateway.md) sense.

## Compliance & FS traction

Vendor-stated SOC 2 Type II, SOC 3, ISO 27001 and GDPR. Not independently verified.
Ask for the reports. Named customers lean toward financial data and fintech:
**AlphaSense** (per Fortune, "tens of thousands of agents"), **Fitch Group**,
**OakNorth** and **Allica Bank** (UK banks) appear among vendor logos, alongside EOG
Resources, Synthesia, The Telegraph and Owkin. `fs_traction: claimed`. These are logos,
not case studies, and none is a hedge fund or asset manager.

## Commercial

Not public. No pricing page found as of 2026-10-23.

## Competitors / alternatives

[zenity](zenity.md) · [noma-security](noma-security.md) · [straiker](straiker.md) ·
[operant-ai](operant-ai.md) · [lasso-security](lasso-security.md) ·
[prisma-airs](prisma-airs.md) · [token-security](token-security.md)

## Open questions

- Deployment detail: region choices, single-tenant option, data retention, sub-processors,
  training-use terms.
- Per-platform enforcement matrix: which agent runtimes Beam can actually *Enforce* on
  versus only monitor.
- SIEM/SOAR and IdP integrations.
- Pricing model (per agent, per seat, platform).
- Independent confirmation of SOC 2 / ISO 27001 reports.
- FS references beyond logos; any asset-manager deployments.
- RSAC's own release (rsaconference.com, 2026-isb-winner) and Balderton's release
  returned HTTP 403 on fetch. The win is corroborated by Geordie's release plus
  RSAC/Dark Reading search results, and the round by three independent outlets.

## Sources

- [Geordie raises $30 million for AI security and governance platform (SecurityWeek)](https://www.securityweek.com/geordie-raises-30-million-for-ai-security-and-governance-platform/) — fetched 2026-10-23 — supports: $30M Series A, Balderton lead, Crosspoint/General Catalyst/Ten Eleven, $36.5M total, London, founded early 2025, Beam; confidence: high
- [Geordie raises $30M to bring security and governance to agentic AI (tech.eu)](https://tech.eu/2026/05/29/geordie-raises-30m-to-bring-security-and-governance-to-agentic-ai/) — fetched 2026-10-23 — supports: round details, board seat; confidence: high
- [Fortune — Geordie security and governance for AI agents](https://fortune.com/2026/05/28/geordie-security-governance-ai-agents/) — fetched 2026-10-23 — supports: $6.5M seed (2025-09), ~$180M valuation, 37 staff, founders, ~30 customer environments, AlphaSense/Owkin; confidence: medium
- [Geordie AI named Most Innovative Startup at RSAC 2026 Innovation Sandbox (Geordie)](https://www.geordie.ai/resources/geordie-ai-named-most-innovative-startup-at-rsac-2026-innovation-sandbox/) — fetched 2026-10-23 — supports: RSAC ISB win 2026-03-23, founded 2025, founder backgrounds, Beam release March 2026, module list; confidence: high (corroborated by RSAC and Dark Reading search results)
- [Geordie AI homepage](https://www.geordie.ai/) — fetched 2026-10-23 — supports: coverage list, Beam modes, certifications, customer logos; confidence: low (vendor marketing)
- [Balderton — Geordie raises $30M](https://www.balderton.com/news/geordie-raises-30m-to-help-enterprises-securely-adopt-agentic-ai-at-scale/) — 403 on fetch 2026-10-23; title seen in search; confidence: n/a
- Cached: `raw/sources/2026-10-23--geordie-ai--series-a-funding.md`, `raw/sources/2026-10-23--geordie-ai--rsac-isb-and-product.md`

## History

- [2026-10-23] Page created and researched in one pass from 2026-10 CTO-survey write-ins
  (2 respondents in production; written in under LLM Observability and AI Runtime
  Security / AI Firewall). Verified RSAC 2026 Innovation Sandbox win (2026-03-23) and
  $30M Balderton-led Series A (2026-05-28). Primary set to agent-runtime-security
  (Beam acts in the agent loop), cross-listed ai-spm (discovery/posture). Did not
  cross-list ai-runtime-security (not an inline AI firewall) or llm-observability
  (security audit trail, not a dev tracing/eval platform — judged a respondent
  misplacement).
