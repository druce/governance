---
type: overview
title: The Enterprise AI Governance & Security Stack — a hedge-fund CTO's map
status: stub
last_updated: 2026-06-28
---

# Overview — the AI governance & security layer cake

> **Stub** (Phase 0). Fleshed into the full thesis in Phase 4, with links into every
> category. This captures the spine from the seed layer-cake doc so the structure is legible
> now.

## The thesis

Standing up a *governed* enterprise AI platform isn't one purchase — it's a **stack**. Each
layer does one job, has a priority (do it Day-1 vs Day-2 vs optional), and a shortlist of
vendors competing for the slot. This wiki maps that stack for a **hedge-fund / asset-manager
CTO**: what each layer is for, when you actually need it, who fills it, who owns whom, and how
to tell neighbors apart.

## The layer cake (the spine)

Seven layers, top to bottom of the seed doc:

1. **Foundation** — identity, secrets, SIEM/SOC, EDR, network/SASE, SSPM, supply-chain,
   anti-deepfake. The security estate you (mostly) already own; extend it to AI.
2. **Data** — DSPM/classification, DLP, data-access governance. Know where sensitive data is,
   stop it walking out, right-size who can read it.
3. **AI model & prompt** — AI runtime security (firewall), AI gateway, LLM observability/eval,
   red-teaming/guardrails, AI access governance (CASB for AI), AI-SPM, agent security,
   authorization engines, MCP gateways, tool identity. The AI-specific control plane.
4. **Retrieval** — content sources, vector retrieval, **entitlement-aware RAG** (non-negotiable
   once you do RAG: the AI must never surface a doc the user couldn't already open).
5. **User experience** — the governed assistant people actually use (ChatGPT/Claude/Copilot
   Enterprise), third-party AI apps, enterprise browser / browser extension.
6. **Governance** — AI governance/model-risk platform, enterprise GRC, vendor risk, comms
   surveillance, ephemeral environments, policy-as-code.
7. **Policy / process** — trust-zone segmentation, risk tiers, promotion gates, HITL approvals,
   acceptable-use policy. Practices, not products.

## The three trust zones (red / yellow / green)

The organizing security idea. Segment where agents run so the dangerous combination never
lines up:

- **Red zone** — agents "YOLO" on the open Internet, **no** access to internal data.
- **Yellow zone** — agents reach the data warehouse but **cannot** reach the Internet to
  exfiltrate.
- **Green zone** — agents touch internal production systems, but only under extreme vetting,
  governance, and **no untrusted prompt input**.

## The lethal trifecta

From Simon Willison: three ingredients that are individually fine but catastrophic together —

1. **Untrusted input** (a prompt/content the attacker controls),
2. **Access to sensitive data**, and
3. **An egress path** to exfiltrate it.

Most of this stack exists to **break one leg** of that trifecta at each layer (input
inspection, data controls, egress control). Trust-zone segmentation is the architectural way
to guarantee the three never co-occur.

## Minimal vs full stack (to be expanded)

- **Minimal (small fund, public AI tools only):** identity + SASE you already own, an AI
  gateway, AI access governance / DLP for prompts, a governed enterprise assistant, AUP +
  risk tiers. _Filled out in Phase 4._
- **Full (RAG + agents in production):** add DSPM, entitlement-aware RAG, AI runtime security,
  observability, AI-SPM + agent authorization + MCP gateways, AI governance platform under SR
  11-7, comms surveillance. _Filled out in Phase 4._

## Map into the wiki

See [taxonomy.md](../taxonomy.md) for the canonical 42-category map and [[index]] for the
content catalog. Category and vendor pages link back here.
