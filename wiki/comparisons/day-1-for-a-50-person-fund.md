---
type: comparison
name: What's actually Day-1 for a ~50-person hedge fund
slug: day-1-for-a-50-person-fund
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 0
---

# What's actually Day-1 for a ~50-person hedge fund

The layer cake has ~40 rows. A 50-person fund does **not** buy 40 things. This page is the
opinionated minimum: what you genuinely need before letting staff and agents use AI on real data,
what you almost certainly **already own**, and what's safe to defer. Written for the CTO who has to
say "yes, we can use AI" without creating an MNPI-leak or a model-risk finding.

## The premise

A 50-person fund's reality: small IT/security team, heavy reliance on a Microsoft or Google estate,
mostly-SaaS, a few power users who want ChatGPT/Claude/Copilot and maybe some agents. The dominant
risks are **(1) MNPI/client data leaking into a public model**, **(2) the AI surfacing data someone
shouldn't see**, and **(3) a regulator/allocator asking "how do you govern this?"** Everything below
serves those three.

## Tier 0 — you (almost certainly) already own it; just extend to AI
These are not new purchases — confirm they cover AI and move on.
- [identity-access](../categories/identity-access.md) — Entra/Okta SSO + MFA. *Extend:* SSO every AI tool; no local logins.
- [edr-xdr](../categories/edr-xdr.md) + [network-security-sase](../categories/network-security-sase.md) — already deployed. *Extend:* the SASE layer ([zscaler](../vendors/zscaler.md),
  [netskope](../vendors/netskope.md), [palo-alto-networks](../vendors/palo-alto-networks.md), [cloudflare](../vendors/cloudflare.md)) can already see/limit traffic to AI sites —
  turn that on. This is your cheapest shadow-AI control.
- [siem-soc](../categories/siem-soc.md) — Sentinel/Splunk. *Extend:* ingest AI gateway + assistant audit logs.
- [enterprise-grc](../categories/enterprise-grc.md) + [vendor-risk](../categories/vendor-risk.md) — you have a TPRM process. *Extend:* run AI vendors through it.
- [comms-surveillance](../categories/comms-surveillance.md) — if you're under MAR/SEC/FINRA supervision you already capture e-comms;
  *extend* the archive to AI prompts/responses (a real, current gap — see the category page).

## Tier 1 — genuinely Day-1 *new* work for AI
The short list that actually needs attention before go-live:

| Need | Why | Realistic pick |
|---|---|---|
| **Governed assistant** | The thing people use; gives you logging/no-train/SSO | [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md): ChatGPT/Claude Enterprise or M365 Copilot |
| **AI gateway** | One audit log + egress chokepoint + spend control | [ai-gateway](../categories/ai-gateway.md): [litellm](../vendors/litellm.md) (OSS) or [portkey](../vendors/portkey.md); or your SASE/Cloudflare |
| **Shadow-AI / prompt DLP** | Stop MNPI pasted into public AI | [ai-access-governance](../categories/ai-access-governance.md) / [dlp](../categories/dlp.md): [witnessai](../vendors/witnessai.md), [cyberhaven](../vendors/cyberhaven.md), or SASE-native |
| **Entitlement-aware RAG** *(if doing RAG)* | AI must not surface forbidden docs | [entitlement-aware-rag](../categories/entitlement-aware-rag.md): Copilot+[microsoft-graph](../vendors/microsoft-graph.md) or [glean](../vendors/glean.md) |
| **Data hygiene** *(if doing RAG)* | Fix oversharing before RAG amplifies it | [dspm](../categories/dspm.md)/[data-access-governance](../categories/data-access-governance.md): [microsoft-purview](../vendors/microsoft-purview.md), [varonis](../vendors/varonis.md) |
| **AI runtime security** *(if building apps/agents)* | Block injection/leak inline | [ai-runtime-security](../categories/ai-runtime-security.md): bundle from your platform, or [hiddenlayer](../vendors/hiddenlayer.md)/[witnessai](../vendors/witnessai.md) |

## Tier 1 — process (cheap, do it now)
These cost little but matter most to allocators/regulators:
- [acceptable-use-policies](../categories/acceptable-use-policies.md) — the cheapest control there is. Write it, everyone signs.
- [risk-tiers](../categories/risk-tiers.md) — classify AI use cases by stakes so scrutiny matches risk.
- [trust-zone-segmentation](../categories/trust-zone-segmentation.md) — design red/yellow/green zones *now* so the [lethal trifecta](../overview.md)
  can never line up later, even if you don't build agents yet.
- [promotion-gates](../categories/promotion-gates.md) — a lightweight sign-off between "experiment" and "production."
- **Model-risk note:** if you're under **SR 11-7** (bank-affiliated) or expect allocator due diligence,
  an [ai-governance-platform](../categories/ai-governance-platform.md) / model inventory moves to Day-1; otherwise a spreadsheet inventory +
  your GRC is fine to start.

## Tier 2 — defer until you actually have agents / scale
Don't buy these on Day 1: [ai-spm](../categories/ai-spm.md), [agent-runtime-security](../categories/agent-runtime-security.md), [authorization-engine](../categories/authorization-engine.md),
[mcp-gateway](../categories/mcp-gateway.md), [tool-identity-integration](../categories/tool-identity-integration.md), [non-human-identity](../categories/non-human-identity.md), [ai-soc-analysts](../categories/ai-soc-analysts.md),
[llm-observability](../categories/llm-observability.md) (lightweight from launch, but not a big spend), full [ai-red-teaming](../categories/ai-red-teaming.md). These
become real when agents proliferate and act — "Day-2 when agents act," per the seed.

## The 6-line answer
If the CTO wants one paragraph: **Turn on SSO + SASE AI-traffic controls you already own; pick one
governed enterprise assistant; put an AI gateway in front of model calls for logging + egress
control; add a prompt-DLP/shadow-AI control; if you do RAG, fix data permissions and use
entitlement-aware retrieval; write an AUP and risk tiers; design trust zones. Defer the whole
agent-security stack until you actually run agents.**

## Minimal vs full stack
- **Minimal (public AI tools only, no RAG/agents):** Tier 0 extensions + governed assistant + AI
  gateway + shadow-AI/prompt-DLP + AUP/risk-tiers. ~4 new line items.
- **Full (RAG + agents in production):** add DSPM/data-access hygiene, entitlement-aware RAG, AI
  runtime security, observability, then the Tier-2 agent stack, and an AI governance platform under
  SR 11-7. See [overview](../overview.md) for the whole map.

## History
- [2026-06-28] Created in Phase 4 as the flagship CTO-facing synthesis.
