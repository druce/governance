---
type: category
name: Agent Security (runtime)
slug: agent-runtime-security
layer: model-prompt
priority: day-2
trifecta_role: untrusted-input, egress (guards agent actions at runtime); yellow/green zone
maps_to_seed_doc: (folded into AI-SPM / Agent Governance)
maps_to_seed_csv: Agent Security
vendor_count: 6
status: drafted
last_updated: 2026-06-28
---

# Agent Security (runtime)

## Business objective

Agent runtime security **protects agentic applications while they run** — as the agent
reads a tool result, decides on an action, and calls an API. Where a plain LLM chat
takes a prompt and returns text, an agent *takes actions in the world* (queries
databases, hits SaaS APIs, runs code, spends money), so a poisoned tool output or an
injected instruction can become real damage. This layer watches the agent's behaviour in
real time and stops the dangerous step: the rogue tool call, the exfiltration attempt,
the action outside policy.

Think of it as the runtime guard that sits **around the agent loop** — inspecting not
just the user's prompt (that's [[ai-runtime-security]]) but the agent's *plans, tool
calls, and intermediate results*, where prompt-injection actually lands in an agentic
system.

## When you need it

Day-2 — it becomes relevant **once you run agents that take consequential actions**, not
just chatbots that answer questions. A fund piloting a research copilot that only reads
doesn't need it; a fund letting agents execute trades-adjacent workflows, touch
production systems, or act on untrusted web/email content does. It pairs naturally with
[[hitl-approvals]] (human sign-off on high-stakes actions) and [[trust-zone-segmentation]]
(keep agents out of the green zone unless heavily vetted). Buy it when "what could this
agent do if it were tricked?" stops having a comfortable answer.

## Lethal-trifecta role

This is the layer that **breaks the chain at the agent's action boundary**. It targets
**untrusted input** (prompt injection arriving via tool outputs, documents, web content)
and **egress** (blocking the exfiltration or unauthorized action the injection tries to
trigger). It's most at home in the **yellow and green zones**, where agents have data or
production access and the worry is an injected instruction turning that access into a
breach. It complements, rather than replaces, zone segmentation: segmentation makes the
trifecta hard to assemble; runtime agent security catches the case where it assembles
anyway.

## Vendors

- [[zenity]] — security and governance for agents and low-code/copilot platforms; runtime detection of risky agent behaviour. Cross-listed to [[ai-spm]].
- [[lasso-security]] — AI/agent security plus shadow-AI and DLP; common shortlist for agent + LLM-app protection. Cross-listed to [[ai-runtime-security]] and [[dlp]].
- [[operant-ai]] — runtime protection for agentic apps and APIs (in-cluster/runtime defense angle).
- [[apex-security]] — enterprise agent security (per seed, acq. by Tenable — unverified).
- [[straiker]] — runtime security for AI agents and applications.
- [[noma-security]] — AI/ML and agent security spanning discovery and runtime; primary in [[ai-spm]], cross-listed here.

## Consolidation / M&A dynamics

Early and consolidating. Per seed flag (**unverified — to confirm in research**): Apex
Security acq. by Tenable, an example of a larger exposure-management vendor buying into
agent security. Expect the same platform gravity as [[ai-spm]]: cloud-security, EDR, and
AI-firewall vendors absorbing standalone agent-runtime players. Several vendors here also
sell AI-SPM, so the category may not survive long as a clean standalone purchase.

## Adjacent categories

- [[ai-spm]] — the discovery/posture sibling; AI-SPM inventories agents, this layer guards them at runtime. Largest overlap in the model/prompt layer (Zenity, Noma span both).
- [[ai-runtime-security]] — the AI firewall for prompts/responses; agent-runtime extends the same idea to tool calls and multi-step agent loops.
- [[mcp-gateway]] — controls *which tools* an agent can reach; agent-runtime watches *how the agent behaves* once it has them. Complementary chokepoints.
- [[authorization-engine]] — decides if a given agent action is allowed; agent-runtime can call into authz or enforce policy itself.
- [[hitl-approvals]] / [[trust-zone-segmentation]] — process controls this layer backstops.

## Survey

**Question.** Which agent (runtime) security tools is your organization using or
evaluating to protect agentic applications as they act? *(Select all that apply and
indicate stage.)*

**Answer options.** Zenity · Lasso Security · Operant AI · Apex Security · Straiker ·
Noma · Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- Young category — expect **low production adoption** and lots of "Interested/Considering"; the signal is intent, not deployment.
- **Heavy overlap with [[ai-spm]]:** Zenity and Noma appear on both lists. If you ask both questions, a short scope line ("runtime *protection* of agents, not just inventory") reduces double-counting.
- Lasso also appears under [[ai-runtime-security]] and shadow-AI; respondents may file it wherever they first met it.
- "Other" likely captures Prisma AIRS and AI-firewall vendors that pitch agent protection as a feature.

## Open taxonomy questions

- **This is the other half of the ai-spm overlap, and the messiest seam in the layer.** The seed *doc* has no separate row — agent security is folded into "AI-SPM / Agent Governance"; only the *CSV* breaks "Agent Security" out as its own survey question. We keep it separate (see Q1 in taxonomy-gaps.md) to preserve the survey cut and because runtime enforcement is genuinely a different job from posture/inventory — but the vendor lists bleed together (Zenity, Noma, Lasso). Working rule: **agent-runtime-security = enforcement at the agent's action boundary; [[ai-spm]] = visibility/posture over the AI estate.**
- Open question for the final taxonomy pass: if essentially every vendor here also ships AI-SPM (and vice versa), should the two merge into one "Agent Security / AI-SPM" category with sub-segments, matching the seed doc's single row? Kept split for now to serve survey design.
- Overlap with [[mcp-gateway]] and [[authorization-engine]] (the "stop the bad action" job is shared across three layers) — see those pages' open questions.
