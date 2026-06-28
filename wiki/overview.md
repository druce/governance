---
type: overview
title: The Enterprise AI Governance & Security Stack — a hedge-fund CTO's map
status: drafted
last_updated: 2026-06-28
---

# Overview — the AI governance & security layer cake

The thesis: standing up a *governed* enterprise AI platform isn't one purchase — it's a **stack**.
Each layer does one job, has a priority (Day-1 / Day-2 / optional), and a shortlist of vendors
competing for the slot. This wiki maps that stack for a **hedge-fund / asset-manager CTO**: what
each layer is for, when you actually need it, who fills it, who owns whom, and how to tell neighbors
apart. It also doubles as scaffolding for a CTO usage/evaluation **survey** (see [[survey-blueprint]]).

If you read nothing else, read [[day-1-for-a-50-person-fund]] — the opinionated minimum.

## The three organizing ideas

### 1. The layer cake (the spine)
Seven layers, top to bottom. Each links to its categories:

1. **Foundation** — [[identity-access]], [[non-human-identity]], [[identity-governance]],
   [[secrets-management]], [[siem-soc]], [[ai-soc-analysts]], [[edr-xdr]],
   [[network-security-sase]], [[sspm]], [[software-supply-chain]], [[anti-deepfake]].
   *The security estate you mostly already own; extend it to AI.*
2. **Data** — [[dspm]], [[dlp]], [[data-access-governance]]. *Know where sensitive data is, stop it
   walking out, right-size who can read it.*
3. **AI model & prompt** — [[ai-runtime-security]], [[ai-gateway]], [[llm-observability]],
   [[ai-red-teaming]], [[ai-access-governance]], [[ai-spm]], [[agent-runtime-security]],
   [[authorization-engine]], [[mcp-gateway]], [[tool-identity-integration]]. *The AI-specific
   control plane — the heart of this wiki.*
4. **Retrieval** — [[content-sources]], [[vector-retrieval]], [[entitlement-aware-rag]].
   *Once you do RAG, the AI must never surface a doc the user couldn't already open.*
5. **User experience** — [[enterprise-ai-assistant]], [[third-party-ai-apps]], [[enterprise-browser]],
   [[browser-security-extension]]. *The governed tools people actually use.*
6. **Governance** — [[ai-governance-platform]], [[enterprise-grc]], [[vendor-risk]],
   [[comms-surveillance]], [[ephemeral-environments]], [[policy-as-code]]. *Prove and manage AI risk
   to regulators and allocators.*
7. **Policy / process** — [[trust-zone-segmentation]], [[risk-tiers]], [[promotion-gates]],
   [[hitl-approvals]], [[acceptable-use-policies]]. *Practices, not products.*

Full canonical map: [taxonomy.md](../taxonomy.md) (42 categories). Catalog: [[index]].

### 2. The three trust zones (red / yellow / green)
Segment where agents run so the dangerous combination never lines up:
- **Red zone** — agents "YOLO" on the open Internet, **no** access to internal data.
- **Yellow zone** — agents reach the data warehouse but **cannot** reach the Internet to exfiltrate.
- **Green zone** — agents touch internal production systems, but only under extreme vetting and
  governance, and **no untrusted prompt input**.

[[trust-zone-segmentation]] is the architectural control that makes the next idea impossible by
construction. [[ephemeral-environments]] are how you implement disposable, zone-scoped compute.

### 3. The lethal trifecta
From [Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): three ingredients
that are individually fine but catastrophic together —
1. **Untrusted input** (a prompt/content an attacker controls),
2. **Access to sensitive data**, and
3. **An egress path** to exfiltrate it.

Most of this stack exists to **break one leg** at each layer:
- **Untrusted input** → [[ai-runtime-security]], [[ai-red-teaming]], [[anti-deepfake]].
- **Sensitive data** → [[dspm]], [[data-access-governance]], [[entitlement-aware-rag]],
  [[non-human-identity]].
- **Egress** → [[dlp]], [[ai-gateway]], [[ai-access-governance]], [[network-security-sase]],
  [[mcp-gateway]].
Trust-zone segmentation guarantees the three never co-occur.

## What's actually Day-1 vs Day-2
- **Day-1 (before go-live):** identity/SASE you already own; a governed [[enterprise-ai-assistant]];
  an [[ai-gateway]]; [[ai-access-governance]]/[[dlp]] for prompts; [[acceptable-use-policies]] +
  [[risk-tiers]] + [[trust-zone-segmentation]]; and, if doing RAG, [[entitlement-aware-rag]] +
  [[dspm]]/[[data-access-governance]] hygiene.
- **Day-2 (when agents proliferate/act):** [[ai-spm]], [[agent-runtime-security]],
  [[authorization-engine]], [[mcp-gateway]], [[tool-identity-integration]], [[ai-soc-analysts]],
  full [[ai-red-teaming]]; and an [[ai-governance-platform]] (Day-1 under SR 11-7).
Detailed: [[day-1-for-a-50-person-fund]].

## Consolidation: the map is moving under you
2025–26 saw a wave of M&A — **much of the AI-runtime/guardrail field is now inside platforms**
(Palo Alto, Cisco, CrowdStrike, SentinelOne, F5, Zscaler, Check Point, Cato). If you already run one
of those, you may get an AI-firewall/guardrail capability as a module — check before buying
standalone. Full, dated, verified detail: [[ai-security-m-and-a-map]].

## How to navigate this wiki
- **Categories** — one page per layer slot: what it's for, when you need it, vendors, survey scaffold.
- **Vendors** — one page per company (multi-category tagged), with ownership/funding/M&A verified
  and dated, and a hedge-fund lens.
- **Comparisons** — filed-back answers: [[ai-gateways-head-to-head]], [[runtime-ai-firewalls]],
  [[entitlement-aware-rag-options]], [[ai-security-m-and-a-map]], [[day-1-for-a-50-person-fund]],
  [[survey-blueprint]].
- Start at [[index]] for the full catalog.
