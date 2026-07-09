---
title: Knostic
type: vendor
name: Knostic
slug: knostic
aka: []
primary_category: agent-runtime-security
also_listed_in: [entitlement-aware-rag, ai-access-governance, enterprise-ai-assistant]
website: https://www.knostic.ai
founded: 2023
hq: Herndon, Virginia, US (R&D in Tel Aviv, Israel)
ownership_state: independent
owner: null
ownership_note: VC-backed, independent as of 2026-06-28; no M&A flagged or found.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$19.3M
last_funding: $5M RSAC Innovation Sandbox Top-10 finalist investment (2025-04); $11M Series A (2025-03)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated (energy, finance, healthcare, pharma, government)
last_verified: 2026-07-09
verify_after: null
tags: [agent-security, coding-agents, mcp, need-to-know, copilot-security, oversharing, llm-access-control]
---

# Knostic

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md) (recategorized 2026-07-09; was [entitlement-aware-rag](../categories/entitlement-aware-rag.md)). Also: [entitlement-aware-rag](../categories/entitlement-aware-rag.md), [ai-access-governance](../categories/ai-access-governance.md), [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md).

**One-liner** — An agentic-AI security platform ("Security Across the Agentic Lifecycle"): Kirin secures AI agents, coding assistants, and MCP servers at runtime (least-privilege, anomaly detection, prompt-injection blocking), with supply-chain reputation (AgentMesh) and shadow-AI discovery alongside its original "need-to-know" oversharing control for enterprise AI assistants.

> **Repositioning note (2026-07-09):** Knostic launched (2023–2025) as a need-to-know /
> Copilot-oversharing control and was filed under entitlement-aware RAG. As of mid-2026 its
> website leads with **agentic security** — Kirin (agents/coding tools/MCP), AgentMesh
> (supply-chain reputation, VirusTotal partnership 2026-06), Shadow AI Spotlight, OpenAnt —
> and CSA's Agentic AI Security Innovator Market Map places it in Governance, Observability,
> and Supply Chain Integrity. The knowledge-security product still exists; this is a
> re-lead/expansion, not a product replacement. Primary category moved accordingly.

## What it does

**Agentic security (current lead, 2026).** Kirin is the flagship: it secures AI agents and
AI coding tools — in-house, SaaS, and MCP-driven agents, plus IDE extensions, rules, and
skills — by enforcing least-privilege policies on what data and APIs an agent can reach,
continuously observing agent activity for anomalies, blocking prompt-injection / malicious
instructions before they trigger actions, authenticating agents via OAuth, and keeping an
audit log. The pitch is that coding agents "act fast and can make destructive mistakes"
(the `rm -rf` failure mode) and that extensions/MCP servers are an ungoverned supply
chain. Companion products: **AgentMesh** (supply-chain reputation engine for agent
artifacts such as VS Code .VSIX extensions; feeds VirusTotal's Crowdsourced AI as of
2026-06), **Shadow AI Spotlight** (unsanctioned AI tool discovery), and **OpenAnt** (LLM
vulnerability discovery via semantic analysis). All capability claims are vendor
marketing, unverified independently.

**Knowledge security (original product, still offered).** Enterprise AI assistants answer questions by retrieving and synthesizing from everything the asking user is *permitted* to open. In most M365 tenants those permissions are far looser than anyone realizes — years of over-shared SharePoint sites, inherited folder access, "share with everyone" links. A human rarely stumbles across the over-permissioned HR spreadsheet; Copilot will read it, infer from it, and hand the answer to anyone who asks ("what's the VP of Sales' bonus?", "what M&A targets are we looking at?"). Knostic's founders frame it as: *LLMs can't keep a secret.*

Knostic adds a **knowledge-level / need-to-know policy layer** on top of raw ACLs. It works in three moves:

1. **Discover/simulate** — it probes the assistant the way an employee would (simulated queries) to surface oversharing exposure paths *before* they become incidents.
2. **Policy** — enforces need-to-know boundaries keyed to a user's role, independent of the underlying permission system ("if you need to know, you know; if you don't, you don't").
3. **Remediate/audit** — pinpoints the precise permission or label issues to fix and produces an audit trail of who could see what and why.

Its central argument: **mirroring document ACLs is not enough**, because the ACLs themselves are too loose. Need-to-know is a separate, higher policy layer than file permissions.

## Where it sits in the stack

Primary category [agent-runtime-security](../categories/agent-runtime-security.md): Kirin operates at the agent's action boundary — screening injected instructions arriving via tool results and blocking the unsafe action or data reach they attempt — which is exactly this category's job. Cross-listed to [entitlement-aware-rag](../categories/entitlement-aware-rag.md) for the original knowledge-security product (which controls access to sensitive data only: it narrows *what private knowledge the model may surface* to a given user, at the green/yellow boundary, without screening input or controlling egress), to [ai-access-governance](../categories/ai-access-governance.md) for Shadow AI Spotlight, and to [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) governance where buyers encounter the Copilot-oversharing use case.

## Deployment & architecture

- SaaS, integrated read-only/advisory. It analyzes oversharing exposure and **hands findings to the enforcement plane rather than enforcing inline** — e.g. "Purview Manages Data Access, Knostic Manages AI Exposure," delivering "Copilot risk insights in days, not months, pinpointing precise permission or labeling issues for [Purview](microsoft-purview.md) to act on."
- Detection is AI-native (simulating inference/reconstruction risk) rather than simple content scanning, because "LLMs don't just retrieve data — they infer and reconstruct hidden insights."
- Integrations: Microsoft 365 Copilot, [glean](glean.md), Google Gemini; Microsoft [Purview](microsoft-purview.md) for remediation. Also markets shadow-AI discovery, prompt-injection and MCP-server risk checks.
- *To verify:* exact API surface (Graph scope, whether it reads production traffic vs only simulates), and whether any runtime/inline enforcement exists vs advisory-only. Vendor pages do not specify.

## Positioning & differentiators

**In agent security**, Knostic's angle vs. the category shortlist ([zenity](zenity.md), [lasso-security](lasso-security.md), [operant-ai](operant-ai.md), [apex-security](apex-security.md), [straiker](straiker.md)) is the **AI coding tool / developer-environment wedge**: IDE extensions, MCP servers, rules and skills as a supply chain (AgentMesh reputation scoring, VirusTotal integration), plus runtime least-privilege for the agents themselves. CSA's Agentic AI Security Innovator Market Map (2026) slots it under Governance, Observability, and Supply Chain Integrity. Whether it can cover general enterprise agent runtimes as deeply as the agent-runtime incumbents is unproven.

**In knowledge security**, the original wedge is the **gap between ACL-mirroring and need-to-know**. Contrast the neighbors:

- [microsoft-graph](microsoft-graph.md) / native Copilot — enforces the *raw* SharePoint/Graph ACLs. Knostic's whole pitch is that those ACLs are themselves over-permissioned, so faithful ACL enforcement still overshares.
- [glean](glean.md) — permission-mirroring enterprise search; same critique: mirroring loose permissions faithfully still leaks.
- [microsoft-purview](microsoft-purview.md) — labels and DLP on the data plane; Knostic positions as complementary, feeding Purview the AI-specific exposure findings it can't see on its own.

Differentiator claims (vendor marketing): "world's first need-to-know access controls for LLMs"; the discover-by-simulation approach; recognition sweep (RSA Launch Pad 2024 + Black Hat Startup Spotlight 2024 winner; RSAC 2025 Innovation Sandbox Top-10 finalist).

## Ownership, funding & M&A

- **Independent, VC-backed** (high confidence). No acquisition flagged in the seed and none found.
- Founded **2023** by **Gadi Evron** (CEO; serial security entrepreneur, ex-Citibank/PwC) and **Sounil Yu** (CTO; creator of the Cyber Defense Matrix, ex-Bank of America Chief Security Scientist).
- HQ **Herndon, Virginia**, with R&D in **Tel Aviv, Israel**. (Seed/brief guess of "New York" not confirmed — primary release lists Herndon, VA.)
- Funding (~$19.3M total): **$3.3M pre-seed** (Apr 2024, Shield Capital / Pitango First / DNX / Seedcamp + angels); **$11M Series A** (Mar 5 2025, led by Bright Pixel Capital, with SVCI, DNX, Seedcamp, angels Kevin Mahaffey and Gerhard Eschelbeck); **$5M** RSAC 2025 Innovation Sandbox Top-10 finalist investment (Apr 2025). Note the Series A release stated ~$14.3M cumulative *before* the RSAC $5M.

## CTO / hedge-fund lens

Two distinct value propositions now. The agentic products (Kirin/AgentMesh) matter **once developers use AI coding agents and MCP servers** — increasingly true even at small funds — and compete for the same budget as the agent-runtime shortlist; they are young and unproven in production. The knowledge-security product remains **Day-1 if you are deploying Microsoft 365 Copilot (or Glean) on a tenant with legacy SharePoint sprawl** — which describes most funds. The oversharing risk is concrete and embarrassing for an asset manager: comp, P&L, deal pipeline, LP data, and MNPI can all be synthesized out of over-shared documents by a tool every employee suddenly has. Knostic targets exactly the "we turned on Copilot and now anyone can ask about bonuses" failure mode.

Caveats for a smaller shop: it is an *added* control on top of Copilot + Purview, advisory rather than an inline guardrail, so value depends on having someone to action its findings. A 50-person fund that hasn't deployed Copilot tenant-wide may get most of the benefit from a Purview/SharePoint permissions cleanup first; Knostic earns its keep once Copilot/Glean is live at scale and you need continuous oversharing assurance. Limited direct SR 11-7 / model-risk angle — this is data-exposure governance, not model validation, though it supports the broader AI-use audit story.

## Competitors / alternatives

Agent security: [zenity](zenity.md), [lasso-security](lasso-security.md), [operant-ai](operant-ai.md), [apex-security](apex-security.md), [straiker](straiker.md), [noma-security](noma-security.md).

Knowledge security:

- [glean](glean.md) — permission-mirroring search/assistant (a target it secures, and a philosophical foil).
- [microsoft-graph](microsoft-graph.md) / native Copilot ACL enforcement.
- [microsoft-purview](microsoft-purview.md) — data labeling/DLP; complementary remediation plane.
- Broader [entitlement-aware-rag](../categories/entitlement-aware-rag.md) approaches.

## Open questions / to verify

- How Kirin enforces at runtime (inline proxy? IDE plugin? endpoint agent?) and whether the agentic products have production customers — all claims are vendor pages so far.
- Revenue/product mix between the knowledge-security platform and the agentic line; whether need-to-know remains actively developed.
- Any funding since the RSAC $5M (Apr 2025) to bankroll the agentic expansion.
- Exact deployment surface: Graph API scopes, read-only vs any inline enforcement, production-traffic monitoring vs simulation-only.
- Whether the $5M RSAC finalist money is structured as investment vs award, and confirmed cumulative total (~$19.3M is summed across rounds).
- Customer references / named deployments in financial services.

## Sources

- [Knostic Nabs $11 Million to Eliminate Enterprise AI Data Leaks (PRNewswire)](https://www.prnewswire.com/news-releases/knostic-nabs-11-million-to-eliminate-enterprise-ai-data-leaks-302392397.html) — fetched 2026-06-28 — supports: $11M Series A 2025-03-05, founders, founded 2023, HQ Herndon VA, need-to-know for Copilot/Glean; confidence: high.
- [About Knostic](https://www.knostic.ai/about-us) — fetched 2026-06-28 — supports: founders/roles, HQ, target verticals, product scope; confidence: med (vendor marketing).
- [Knostic Top-10 Finalist RSAC Innovation Sandbox — $5M](https://www.knostic.ai/blog/knostic-top-10-finalist-in-rsac-innovation-sandbox-contest-secures-additional-5-million-investment) — fetched 2026-06-28 — supports: $5M finalist investment Apr 2025, product covers Copilot/Glean/Gemini; confidence: med (vendor).
- [Stop Copilot Data Oversharing with Knostic & Purview (solution brief)](https://www.knostic.ai/copilot-data-oversharing-solution-brief) — fetched 2026-06-28 — supports: advisory/read-only model, Purview complementarity, inference-risk detection; confidence: med (vendor marketing).
- [Knostic Raises $3.3M for Enterprise GenAI Access Control (Dark Reading / corroborated)](https://www.darkreading.com/application-security/knostic-raises-3-3m-for-enterprise-genai-access-control) — fetched 2026-06-28 (403; via aggregated summaries) — supports: $3.3M pre-seed Apr 2024, early investors, founded 2023; confidence: med.
- [Knostic homepage](https://www.knostic.ai/) + [AI Agent Security Solution](https://www.knostic.ai/ai-agent-security-solution) — fetched 2026-07-09 — supports: "Security Across the Agentic Lifecycle" lead positioning, Kirin/AgentMesh/Shadow AI Spotlight/OpenAnt lineup, knowledge platform still offered; confidence: med (vendor marketing); cached `raw/sources/2026-07-09--knostic--agentic-repositioning.md`
- [CSA Agentic AI Security Innovator Market Map placement (Knostic blog)](https://www.knostic.ai/blog/knostic-featured-across-three-categories-in-csas-agentic-ai-security-innovator-market-map) and [VirusTotal Crowdsourced AI += Knostic](https://blog.virustotal.com/2026/06/crowdsourced-ai-knostic.html) — fetched 2026-07-09 — supports: third-party agentic-security recognition (CSA: Governance/Observability/Supply Chain Integrity), AgentMesh × VirusTotal (2026-06); confidence: med-high (VirusTotal is independent)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (high), founded 2023 by Gadi Evron + Sounil Yu, HQ Herndon VA + Tel Aviv (not NY), ~$19.3M funding ($3.3M pre-seed Apr 2024 / $11M Series A Mar 2025 / $5M RSAC finalist Apr 2025), advisory need-to-know layer for Copilot/Glean oversharing. No M&A. 5 sources cached. status→researched.
- [2026-07-09] Recategorized (user flag verified): website now leads with agentic security — Kirin (agents/coding tools/MCP runtime protection), AgentMesh (supply-chain reputation; VirusTotal 2026-06), Shadow AI Spotlight, OpenAnt; CSA agentic-AI market map placement. Knowledge-security product still offered. primary_category entitlement-aware-rag → agent-runtime-security; cross-listed entitlement-aware-rag + ai-access-governance + enterprise-ai-assistant. Cached 1 source file.
