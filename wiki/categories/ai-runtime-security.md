---
type: category
name: AI Runtime Security (AI Firewall)
slug: ai-runtime-security
layer: model-prompt
priority: day-1
trifecta_role: untrusted-input / egress
maps_to_seed_doc: AI Runtime Security (AI Firewall)
maps_to_seed_csv: AI Runtime Security / AI Firewall
vendor_count: 14
status: drafted
last_updated: 2026-06-28
---

# AI Runtime Security (AI Firewall)

## Business objective

The metal detector for prompts and responses. An AI firewall sits in the live
request/response path of an LLM application and inspects traffic for AI-specific
attacks the network firewall and SASE stack can't see: prompt injection,
jailbreaks, model denial-of-service, and sensitive-data leakage in model output.
It is AI-specific inspection layered *on top of* the foundation-layer
[network-security-sase](network-security-sase.md) and [dlp](dlp.md) controls — those see packets and files; an
AI firewall understands prompts, system instructions, tool calls, and model
responses.

The job is real-time enforcement: block the malicious prompt before it reaches the
model, and block (or redact) the unsafe or leaky response before it reaches the
user or the next tool in an agent chain.

## When you need it

Day-1 once you put any LLM application in front of users or data. The moment a
model can read untrusted input (a customer email, a web page, a document) and also
touch sensitive data or take actions, you need something inspecting that path. For
a hedge-fund CTO: if you are only running a governed [enterprise-ai-assistant](enterprise-ai-assistant.md)
where the vendor already enforces guardrails, this can lag slightly; the instant
you build your own RAG app, agent, or copilot on top of an API, an AI firewall
becomes Day-1. Distinct from [ai-access-governance](ai-access-governance.md), which governs *employees
using* third-party AI — runtime security protects *the AI apps you build and run*.

## Lethal-trifecta role

Breaks two legs at the choke point. On the inbound side it neutralizes **untrusted
input** (prompt-injection / jailbreak detection); on the outbound side it controls
**egress** (blocking sensitive-data leakage and unsafe responses). It lives at the
boundary between the red/yellow zone (where untrusted prompts arrive) and the
data/tooling the model can reach — the enforcement point that keeps the three legs
from lining up. It is detection-and-block, not just observation.

## Vendors

**Dedicated AI firewall / runtime platforms**
- [prisma-airs](../vendors/prisma-airs.md) — Palo Alto's AI runtime security (incl. former Protect AI capabilities); the incumbent-platform play, tied to the broader Prisma/Cortex stack.
- [hiddenlayer](../vendors/hiddenlayer.md) — model-scanning heritage; runtime detection plus red-teaming (cross-listed in [ai-red-teaming](ai-red-teaming.md)).
- [witnessai](../vendors/witnessai.md) — inline inspection of prompts/responses; bridges into [ai-access-governance](ai-access-governance.md) (its primary slot).
- [pillar-security](../vendors/pillar-security.md) — full-lifecycle AI security, runtime guardrails plus posture.
- [cisco-ai-defense](../vendors/cisco-ai-defense.md) — Cisco's runtime AI defense, built on the former Robust Intelligence tech.
- [robust-intelligence](../vendors/robust-intelligence.md) — the acquired company now inside Cisco AI Defense (may merge into that page).
- [aim-security](../vendors/aim-security.md) — enterprise AI security/guardrails platform.
- [enkrypt-ai](../vendors/enkrypt-ai.md) — guardrails plus red-teaming (cross-listed in [ai-red-teaming](ai-red-teaming.md)).
- [calypsoai](../vendors/calypsoai.md) — runtime inference security and control.
- [lakera](../vendors/lakera.md) — prompt-injection/guardrail detection with a strong research profile (cross-listed in [ai-red-teaming](ai-red-teaming.md)).
- [trojai](../vendors/trojai.md) — model and runtime security, scanning plus runtime defense.
- [splxai](../vendors/splxai.md) — red-teaming-first vendor that also offers runtime guardrails (primary in [ai-red-teaming](ai-red-teaming.md)).

**Runtime guardrails inside a DLP/data-security lineage**
- [prompt-security](../vendors/prompt-security.md) — prompt/response inspection and AI DLP (cross-listed in [dlp](dlp.md) and [ai-access-governance](ai-access-governance.md)).
- [lasso-security](../vendors/lasso-security.md) — runtime LLM/agent protection (cross-listed in [dlp](dlp.md) and [agent-runtime-security](agent-runtime-security.md)).

## Consolidation / M&A dynamics

This is one of the most actively rolled-up categories. Per seed flags (unverified —
to confirm in research): Prisma AIRS is part of Palo Alto Networks and is said to
incorporate the former Protect AI; CalypsoAI flagged as acquired by [f5](../vendors/f5.md); Lakera
flagged as acquired by Check Point; Aim Security flagged as acquired by
[cato-networks](../vendors/cato-networks.md); Prompt Security flagged as acquired by [sentinelone](../vendors/sentinelone.md); Cisco AI
Defense is the productized former Robust Intelligence. Net effect: platform
security vendors (Palo Alto, Cisco, F5, Check Point, SentinelOne, Cato) are
absorbing the AI-firewall startups, so several "independent" survey options now sit
inside a larger suite.

## Adjacent categories

- [ai-gateway](ai-gateway.md) — the gateway is the traffic-routing choke point; the firewall is the inspection logic. They are frequently sold or bundled together (gateway + inline guardrails).
- [ai-access-governance](ai-access-governance.md) — governs employees' use of external AI; runtime security protects internally built AI. Several vendors (WitnessAI, Prompt Security, Lasso) straddle both.
- [ai-red-teaming](ai-red-teaming.md) — offline/pre-prod testing that finds the weaknesses the runtime firewall must block; many vendors do both (HiddenLayer, Lakera, SplxAI, Enkrypt).
- [network-security-sase](network-security-sase.md) / [dlp](dlp.md) — the foundation-layer controls this layer sits on top of.
- [agent-runtime-security](agent-runtime-security.md) — extends runtime protection from single-model calls to multi-step agent behavior.

## Survey

**Question:** Which AI runtime security / AI firewall products are you using or
evaluating to protect AI applications at runtime (prompt-injection, jailbreak, and
output-leakage defense)?

**Answer options:** Prisma AIRS (Palo Alto), HiddenLayer, WitnessAI, Pillar
Security, Cisco AI Defense (former Robust Intelligence), Aim Security, Enkrypt AI,
CalypsoAI, Lakera, TrojAI, SplxAI, Prompt Security, Lasso Security, Other (Please
Specify).

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:**
- Table-stakes / most-recognized: Prisma AIRS, HiddenLayer, Cisco AI Defense, WitnessAI.
- Heavy overlap with [ai-red-teaming](ai-red-teaming.md) (HiddenLayer, Lakera, SplxAI, Enkrypt) and [ai-access-governance](ai-access-governance.md) (WitnessAI, Prompt Security, Lasso) — respondents may not distinguish "firewall" from "red-team" from "shadow-AI." Consider a clarifying lead-in defining runtime/inline.
- M&A dates several options: if confirmed, CalypsoAI→F5, Lakera→Check Point, Aim→Cato, Prompt Security→SentinelOne. Respondents may know the product under either name; consider showing both.
- Robust Intelligence should appear as "Cisco AI Defense (former Robust Intelligence)" to avoid double-counting.

## Open taxonomy questions

- Where does the line sit between AI runtime security (protecting the app) and [agent-runtime-security](agent-runtime-security.md) (protecting multi-step agents)? As agents proliferate the two may merge.
- Should `robust-intelligence` collapse into [cisco-ai-defense](../vendors/cisco-ai-defense.md) once the acquisition and rebrand are confirmed?
- Gateway-vs-firewall: when a vendor ships both inline guardrails and routing (Prisma AIRS, F5), which category is primary? Currently split by emphasis.
