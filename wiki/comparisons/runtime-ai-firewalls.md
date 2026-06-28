---
type: comparison
name: Runtime AI Firewalls — comparison
slug: runtime-ai-firewalls
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 30
---

# Runtime AI firewalls (AI runtime security), compared

The [[ai-runtime-security]] layer is the **metal detector for prompts and responses** — it
inspects model traffic in real time to block prompt injection, jailbreaks, and data leakage. It's
the AI-specific inspection that sits *on top of* your [[network-security-sase]] and bolts onto an
[[ai-gateway]]. For a hedge fund this is **Day-1** once you put any AI app or agent in front of
real data. This page compares the realistic shortlist; see each vendor page for sourced detail and
[[ai-security-m-and-a-map]] for ownership.

## The big story: this category has been half-acquired

Of the dozen credible runtime players, **seven are now inside platforms** (2025–26):

| Vendor | Now owned by | Status |
|---|---|---|
| [[prisma-airs]] (incl. Protect AI) | [[palo-alto-networks]] | Closed |
| [[cisco-ai-defense]] (Robust Intelligence) | [[cisco]] | Closed |
| [[prompt-security]] | [[sentinelone]] | Closed |
| [[calypsoai]] | [[f5]] | Closed (2025-10) |
| [[aim-security]] | [[cato-networks]] | Announced |
| [[lakera]] | Check Point | Announced (Q4 2025) |
| [[splxai]] | [[zscaler]] | Closed (Q1 FY26) |

**Implication for a CTO:** if you already run PANW, Cisco, SentinelOne, F5, Zscaler, Cato, or Check
Point, you likely have (or soon will have) an AI firewall available as a module. Check before buying
a standalone. The remaining **independents** are the diligence-worthy pure-plays.

## At a glance

| Vendor | Core strength | Deploy | Ownership | Independent? |
|---|---|---|---|---|
| [[prisma-airs]] | Full platform: scan + posture + runtime + agent | Inline + API | Palo Alto | No |
| [[hiddenlayer]] | Model scanning / MLDR / supply-chain + red team | SDK/API/scan | Independent ($50M A) | **Yes** |
| [[witnessai]] | Identity-aware inline guardrails + access governance | Inline proxy | Independent ($86.5M) | **Yes** |
| [[pillar-security]] | End-to-end AI/agent security lifecycle | API/SDK | Independent | **Yes** |
| [[cisco-ai-defense]] | Model validation + runtime, Cisco-integrated | Inline/network | Cisco | No |
| [[lasso-security]] | LLM + agent/MCP traffic guardrails, DLP | API/proxy/gateway | Independent | **Yes** |
| [[enkrypt-ai]] | Red-team + guardrails (Yale-founded) | API/SDK | Independent (seed) | **Yes** |
| [[calypsoai]] | Guardrails + red-team (now F5 AI Guardrails) | Inline/API | F5 | No |
| [[lakera]] | Prompt-injection defense (Gandalf fame) | API | Check Point (pending) | No |
| [[prompt-security]] | Prompt-layer DLP + runtime | Inline/proxy | SentinelOne | No |
| [[trojai]] | Detect (red-team) + Defend (runtime firewall) | API/inline | A10 Networks (announced) | No |
| [[splxai]] | AI red-team + runtime | API | Zscaler | No |

## How to tell the independents apart

- **[[hiddenlayer]]** is the **model-centric** player: scan models for malware/backdoors, supply-chain
  provenance, MLDR (detection & response for models), plus red-teaming. Best if your risk is the
  *model artifact* and ML pipeline, not just the prompt stream.
- **[[witnessai]]** is the **identity-aware inline** player — it ties guardrails to *who* the user is
  and *what data* may flow to which model, overlapping [[ai-access-governance]]. Best if your priority
  is governing employee/agent AI **usage** with policy, not just blocking attacks.
- **[[lasso-security]]** spans LLM + **agent/MCP** traffic + DLP — the broadest "agent era" coverage of
  the independents; overlaps [[agent-runtime-security]] and [[dlp]].
- **[[pillar-security]]** pitches an end-to-end lifecycle (discover → test → protect) for AI/agent apps.
- **[[enkrypt-ai]]** leans red-team + guardrails; smallest/earliest (seed-stage) — diligence viability.

## Runtime vs red-teaming (don't conflate)

Several of these also appear in [[ai-red-teaming]]. The distinction:
- **Runtime firewall** = *inline, real-time* block of prompt-injection/leak in production.
- **Red-teaming** = *offline* attack simulation/eval to find weaknesses before production.
HiddenLayer, SplxAI, Lakera, Enkrypt, TrojAI, CalypsoAI do **both**; pure-runtime buyers should
separate "what blocks traffic now" from "what tests my app."

## CTO / hedge-fund lens
- **Day-1** if you deploy any internal-data-facing AI app or agent. If you only use a governed
  [[enterprise-ai-assistant]] (ChatGPT/Claude Enterprise) with no custom apps, the assistant's own
  controls + [[ai-access-governance]] may suffice initially — runtime firewall becomes urgent when
  you build.
- **Buy-vs-bundle:** lead with whatever your platform incumbent (PANW/Cisco/Zscaler/SentinelOne)
  already offers; bring in an independent ([[hiddenlayer]], [[witnessai]]) when you need depth they
  lack (model scanning; identity-aware usage governance).
- **Trifecta:** this layer breaks **untrusted-input** (injection) and **egress** (response DLP) — two
  of three legs — at the model boundary.

## Survey-design notes
- Half the answer options are now platform modules — label them (e.g. "Lakera (Check Point)",
  "CalypsoAI (F5 AI Guardrails)", "Prompt Security (SentinelOne)"). See [[ai-security-m-and-a-map]].
- Expect respondents to confuse runtime with red-teaming — consider splitting the question.

## Sources
Per-vendor sourcing on each linked page; M&A confirmations in [[ai-security-m-and-a-map]].

## History
- [2026-06-28] Created from Phase 3 Wave 1–2 researched runtime/red-team vendor pages.
