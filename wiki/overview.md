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
apart. It also doubles as scaffolding for a CTO usage/evaluation **survey** (see [survey-blueprint](comparisons/survey-blueprint.md)).

If you read nothing else, read [day-1-for-a-50-person-fund](comparisons/day-1-for-a-50-person-fund.md) — the opinionated minimum.

## The three organizing ideas

### 1. The layer cake (the spine)
Seven layers, top to bottom. Each links to its categories:

1. **Foundation** — [identity-access](categories/identity-access.md), [non-human-identity](categories/non-human-identity.md), [identity-governance](categories/identity-governance.md),
   [secrets-management](categories/secrets-management.md), [siem-soc](categories/siem-soc.md), [ai-soc-analysts](categories/ai-soc-analysts.md), [edr-xdr](categories/edr-xdr.md),
   [network-security-sase](categories/network-security-sase.md), [sspm](categories/sspm.md), [software-supply-chain](categories/software-supply-chain.md), [anti-deepfake](categories/anti-deepfake.md).
   *The security estate you mostly already own; extend it to AI.*
2. **Data** — [dspm](categories/dspm.md), [dlp](categories/dlp.md), [data-access-governance](categories/data-access-governance.md). *Know where sensitive data is, stop it
   walking out, right-size who can read it.*
3. **AI model & prompt** — [ai-runtime-security](categories/ai-runtime-security.md), [ai-gateway](categories/ai-gateway.md), [llm-observability](categories/llm-observability.md),
   [ai-red-teaming](categories/ai-red-teaming.md), [ai-access-governance](categories/ai-access-governance.md), [ai-spm](categories/ai-spm.md), [agent-runtime-security](categories/agent-runtime-security.md),
   [authorization-engine](categories/authorization-engine.md), [mcp-gateway](categories/mcp-gateway.md), [tool-identity-integration](categories/tool-identity-integration.md). *The AI-specific
   control plane — the heart of this wiki.*
4. **Retrieval** — [content-sources](categories/content-sources.md), [vector-retrieval](categories/vector-retrieval.md), [entitlement-aware-rag](categories/entitlement-aware-rag.md).
   *Once you do RAG, the AI must never surface a doc the user couldn't already open.*
5. **User experience** — [enterprise-ai-assistant](categories/enterprise-ai-assistant.md), [third-party-ai-apps](categories/third-party-ai-apps.md), [enterprise-browser](categories/enterprise-browser.md),
   [browser-security-extension](categories/browser-security-extension.md). *The governed tools people actually use.*
6. **Governance** — [ai-governance-platform](categories/ai-governance-platform.md), [enterprise-grc](categories/enterprise-grc.md), [vendor-risk](categories/vendor-risk.md),
   [comms-surveillance](categories/comms-surveillance.md), [ephemeral-environments](categories/ephemeral-environments.md), [policy-as-code](categories/policy-as-code.md). *Prove and manage AI risk
   to regulators and allocators.*
7. **Policy / process** — [trust-zone-segmentation](categories/trust-zone-segmentation.md), [risk-tiers](categories/risk-tiers.md), [promotion-gates](categories/promotion-gates.md),
   [hitl-approvals](categories/hitl-approvals.md), [acceptable-use-policies](categories/acceptable-use-policies.md). *Practices, not products.*

Full canonical map: [taxonomy.md](../taxonomy.md) (42 categories). Catalog: [index](../index.md).

### 2. The three trust zones (red / yellow / green)
Segment where agents run so the dangerous combination never lines up:
- **Red zone** — agents "YOLO" on the open Internet, **no** access to internal data.
- **Yellow zone** — agents reach the data warehouse but **cannot** reach the Internet to exfiltrate.
- **Green zone** — agents touch internal production systems, but only under extreme vetting and
  governance, and **no untrusted prompt input**.

[trust-zone-segmentation](categories/trust-zone-segmentation.md) is the architectural control that makes the next idea impossible by
construction. [ephemeral-environments](categories/ephemeral-environments.md) are how you implement disposable, zone-scoped compute.

### 3. The lethal trifecta
From [Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): three ingredients
that are individually fine but catastrophic together —
1. **Untrusted input** (a prompt/content an attacker controls),
2. **Access to sensitive data**, and
3. **An egress path** to exfiltrate it.

Most of this stack exists to **break one leg** at each layer:
- **Untrusted input** → [ai-runtime-security](categories/ai-runtime-security.md), [ai-red-teaming](categories/ai-red-teaming.md), [anti-deepfake](categories/anti-deepfake.md).
- **Sensitive data** → [dspm](categories/dspm.md), [data-access-governance](categories/data-access-governance.md), [entitlement-aware-rag](categories/entitlement-aware-rag.md),
  [non-human-identity](categories/non-human-identity.md).
- **Egress** → [dlp](categories/dlp.md), [ai-gateway](categories/ai-gateway.md), [ai-access-governance](categories/ai-access-governance.md), [network-security-sase](categories/network-security-sase.md),
  [mcp-gateway](categories/mcp-gateway.md).
Trust-zone segmentation guarantees the three never co-occur.

## What's actually Day-1 vs Day-2
- **Day-1 (before go-live):** identity/SASE you already own; a governed [enterprise-ai-assistant](categories/enterprise-ai-assistant.md);
  an [ai-gateway](categories/ai-gateway.md); [ai-access-governance](categories/ai-access-governance.md)/[dlp](categories/dlp.md) for prompts; [acceptable-use-policies](categories/acceptable-use-policies.md) +
  [risk-tiers](categories/risk-tiers.md) + [trust-zone-segmentation](categories/trust-zone-segmentation.md); and, if doing RAG, [entitlement-aware-rag](categories/entitlement-aware-rag.md) +
  [dspm](categories/dspm.md)/[data-access-governance](categories/data-access-governance.md) hygiene.
- **Day-2 (when agents proliferate/act):** [ai-spm](categories/ai-spm.md), [agent-runtime-security](categories/agent-runtime-security.md),
  [authorization-engine](categories/authorization-engine.md), [mcp-gateway](categories/mcp-gateway.md), [tool-identity-integration](categories/tool-identity-integration.md), [ai-soc-analysts](categories/ai-soc-analysts.md),
  full [ai-red-teaming](categories/ai-red-teaming.md); and an [ai-governance-platform](categories/ai-governance-platform.md) (Day-1 under SR 11-7).
Detailed: [day-1-for-a-50-person-fund](comparisons/day-1-for-a-50-person-fund.md).

## Consolidation: the map is moving under you
2025–26 saw a wave of M&A — **much of the AI-runtime/guardrail field is now inside platforms**
(Palo Alto, Cisco, CrowdStrike, SentinelOne, F5, Zscaler, Check Point, Cato). If you already run one
of those, you may get an AI-firewall/guardrail capability as a module — check before buying
standalone. Full, dated, verified detail: [ai-security-m-and-a-map](comparisons/ai-security-m-and-a-map.md).

## How to navigate this wiki
- **Categories** — one page per layer slot: what it's for, when you need it, vendors, survey scaffold.
- **Vendors** — one page per company (multi-category tagged), with ownership/funding/M&A verified
  and dated, and a hedge-fund lens.
- **Comparisons** — filed-back answers: [ai-gateways-head-to-head](comparisons/ai-gateways-head-to-head.md), [runtime-ai-firewalls](comparisons/runtime-ai-firewalls.md),
  [entitlement-aware-rag-options](comparisons/entitlement-aware-rag-options.md), [ai-security-m-and-a-map](comparisons/ai-security-m-and-a-map.md), [day-1-for-a-50-person-fund](comparisons/day-1-for-a-50-person-fund.md),
  [survey-blueprint](comparisons/survey-blueprint.md).
- Start at [index](../index.md) for the full catalog.
