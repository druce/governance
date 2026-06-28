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

The [ai-runtime-security](../categories/ai-runtime-security.md) layer is the **metal detector for prompts and responses** — it
inspects model traffic in real time to block prompt injection, jailbreaks, and data leakage. It's
the AI-specific inspection that sits *on top of* your [network-security-sase](../categories/network-security-sase.md) and bolts onto an
[ai-gateway](../categories/ai-gateway.md). For a hedge fund this is **Day-1** once you put any AI app or agent in front of
real data. This page compares the realistic shortlist; see each vendor page for sourced detail and
[ai-security-m-and-a-map](ai-security-m-and-a-map.md) for ownership.

## The big story: this category has been half-acquired

Of the dozen credible runtime players, **seven are now inside platforms** (2025–26):

| Vendor | Now owned by | Status |
|---|---|---|
| [prisma-airs](../vendors/prisma-airs.md) (incl. Protect AI) | [palo-alto-networks](../vendors/palo-alto-networks.md) | Closed |
| [cisco-ai-defense](../vendors/cisco-ai-defense.md) (Robust Intelligence) | [cisco](../vendors/cisco.md) | Closed |
| [prompt-security](../vendors/prompt-security.md) | [sentinelone](../vendors/sentinelone.md) | Closed |
| [calypsoai](../vendors/calypsoai.md) | [f5](../vendors/f5.md) | Closed (2025-10) |
| [aim-security](../vendors/aim-security.md) | [cato-networks](../vendors/cato-networks.md) | Announced |
| [lakera](../vendors/lakera.md) | Check Point | Announced (Q4 2025) |
| [splxai](../vendors/splxai.md) | [zscaler](../vendors/zscaler.md) | Closed (Q1 FY26) |

**Implication for a CTO:** if you already run PANW, Cisco, SentinelOne, F5, Zscaler, Cato, or Check
Point, you likely have (or soon will have) an AI firewall available as a module. Check before buying
a standalone. The remaining **independents** are the diligence-worthy pure-plays.

## At a glance

| Vendor | Core strength | Deploy | Ownership | Independent? |
|---|---|---|---|---|
| [prisma-airs](../vendors/prisma-airs.md) | Full platform: scan + posture + runtime + agent | Inline + API | Palo Alto | No |
| [hiddenlayer](../vendors/hiddenlayer.md) | Model scanning / MLDR / supply-chain + red team | SDK/API/scan | Independent ($50M A) | **Yes** |
| [witnessai](../vendors/witnessai.md) | Identity-aware inline guardrails + access governance | Inline proxy | Independent ($86.5M) | **Yes** |
| [pillar-security](../vendors/pillar-security.md) | End-to-end AI/agent security lifecycle | API/SDK | Independent | **Yes** |
| [cisco-ai-defense](../vendors/cisco-ai-defense.md) | Model validation + runtime, Cisco-integrated | Inline/network | Cisco | No |
| [lasso-security](../vendors/lasso-security.md) | LLM + agent/MCP traffic guardrails, DLP | API/proxy/gateway | Independent | **Yes** |
| [enkrypt-ai](../vendors/enkrypt-ai.md) | Red-team + guardrails (Yale-founded) | API/SDK | Independent (seed) | **Yes** |
| [calypsoai](../vendors/calypsoai.md) | Guardrails + red-team (now F5 AI Guardrails) | Inline/API | F5 | No |
| [lakera](../vendors/lakera.md) | Prompt-injection defense (Gandalf fame) | API | Check Point (pending) | No |
| [prompt-security](../vendors/prompt-security.md) | Prompt-layer DLP + runtime | Inline/proxy | SentinelOne | No |
| [trojai](../vendors/trojai.md) | Detect (red-team) + Defend (runtime firewall) | API/inline | A10 Networks (announced) | No |
| [splxai](../vendors/splxai.md) | AI red-team + runtime | API | Zscaler | No |

## How to tell the independents apart

- **[hiddenlayer](../vendors/hiddenlayer.md)** is the **model-centric** player: scan models for malware/backdoors, supply-chain
  provenance, MLDR (detection & response for models), plus red-teaming. Best if your risk is the
  *model artifact* and ML pipeline, not just the prompt stream.
- **[witnessai](../vendors/witnessai.md)** is the **identity-aware inline** player — it ties guardrails to *who* the user is
  and *what data* may flow to which model, overlapping [ai-access-governance](../categories/ai-access-governance.md). Best if your priority
  is governing employee/agent AI **usage** with policy, not just blocking attacks.
- **[lasso-security](../vendors/lasso-security.md)** spans LLM + **agent/MCP** traffic + DLP — the broadest "agent era" coverage of
  the independents; overlaps [agent-runtime-security](../categories/agent-runtime-security.md) and [dlp](../categories/dlp.md).
- **[pillar-security](../vendors/pillar-security.md)** pitches an end-to-end lifecycle (discover → test → protect) for AI/agent apps.
- **[enkrypt-ai](../vendors/enkrypt-ai.md)** leans red-team + guardrails; smallest/earliest (seed-stage) — diligence viability.

## Runtime vs red-teaming (don't conflate)

Several of these also appear in [ai-red-teaming](../categories/ai-red-teaming.md). The distinction:
- **Runtime firewall** = *inline, real-time* block of prompt-injection/leak in production.
- **Red-teaming** = *offline* attack simulation/eval to find weaknesses before production.
HiddenLayer, SplxAI, Lakera, Enkrypt, TrojAI, CalypsoAI do **both**; pure-runtime buyers should
separate "what blocks traffic now" from "what tests my app."

## CTO / hedge-fund lens
- **Day-1** if you deploy any internal-data-facing AI app or agent. If you only use a governed
  [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) (ChatGPT/Claude Enterprise) with no custom apps, the assistant's own
  controls + [ai-access-governance](../categories/ai-access-governance.md) may suffice initially — runtime firewall becomes urgent when
  you build.
- **Buy-vs-bundle:** lead with whatever your platform incumbent (PANW/Cisco/Zscaler/SentinelOne)
  already offers; bring in an independent ([hiddenlayer](../vendors/hiddenlayer.md), [witnessai](../vendors/witnessai.md)) when you need depth they
  lack (model scanning; identity-aware usage governance).
- **Trifecta:** this layer breaks **untrusted-input** (injection) and **egress** (response DLP) — two
  of three legs — at the model boundary.

## Survey-design notes
- Half the answer options are now platform modules — label them (e.g. "Lakera (Check Point)",
  "CalypsoAI (F5 AI Guardrails)", "Prompt Security (SentinelOne)"). See [ai-security-m-and-a-map](ai-security-m-and-a-map.md).
- Expect respondents to confuse runtime with red-teaming — consider splitting the question.

## Sources
Per-vendor sourcing on each linked page; M&A confirmations in [ai-security-m-and-a-map](ai-security-m-and-a-map.md).

## History
- [2026-06-28] Created from Phase 3 Wave 1–2 researched runtime/red-team vendor pages.
