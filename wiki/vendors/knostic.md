---
type: vendor
name: Knostic
slug: knostic
categories: [entitlement-aware-rag, enterprise-ai-assistant]
layer: retrieval
aliases: []
website: https://www.knostic.ai
founded: 2023
hq: Herndon, Virginia, US (R&D in Tel Aviv, Israel)
ownership: independent
ownership_detail: VC-backed, independent as of 2026-06-28; no M&A flagged or found.
ownership_confidence: high
funding_total: ~$19.3M
last_funding: $5M RSAC Innovation Sandbox Top-10 finalist investment (2025-04); $11M Series A (2025-03)
deployment: [saas, api]
target_customer: enterprise / regulated (energy, finance, healthcare, pharma, government)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 5
last_updated: 2026-06-28
tags: [need-to-know, copilot-security, oversharing, llm-access-control]
---

# Knostic

> Primary category: [entitlement-aware-rag](../categories/entitlement-aware-rag.md). Also: [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md).

**One-liner** — A "need-to-know" access-control and oversharing-detection layer that sits *above* document ACLs to stop enterprise AI assistants (Microsoft 365 Copilot, Glean, Gemini) from surfacing answers a user can technically reach but has no business seeing.

## What it does

Enterprise AI assistants answer questions by retrieving and synthesizing from everything the asking user is *permitted* to open. In most M365 tenants those permissions are far looser than anyone realizes — years of over-shared SharePoint sites, inherited folder access, "share with everyone" links. A human rarely stumbles across the over-permissioned HR spreadsheet; Copilot will read it, infer from it, and hand the answer to anyone who asks ("what's the VP of Sales' bonus?", "what M&A targets are we looking at?"). Knostic's founders frame it as: *LLMs can't keep a secret.*

Knostic adds a **knowledge-level / need-to-know policy layer** on top of raw ACLs. It works in three moves:

1. **Discover/simulate** — it probes the assistant the way an employee would (simulated queries) to surface oversharing exposure paths *before* they become incidents.
2. **Policy** — enforces need-to-know boundaries keyed to a user's role, independent of the underlying permission system ("if you need to know, you know; if you don't, you don't").
3. **Remediate/audit** — pinpoints the precise permission or label issues to fix and produces an audit trail of who could see what and why.

Its central argument: **mirroring document ACLs is not enough**, because the ACLs themselves are too loose. Need-to-know is a separate, higher policy layer than file permissions.

## Where it sits in the stack

Primary category [entitlement-aware-rag](../categories/entitlement-aware-rag.md) (retrieval layer); also relevant to [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) governance. Lethal-trifecta role: it addresses the **sensitive-data** leg — it does not break untrusted input or egress, it narrows *what private knowledge the model is allowed to surface* to a given user. Trust zone: the green/yellow boundary inside the enterprise, governing internal knowledge exposure rather than external exfiltration.

## Deployment & architecture

- SaaS, integrated read-only/advisory. It analyzes oversharing exposure and **hands findings to the enforcement plane rather than enforcing inline** — e.g. "Purview Manages Data Access, Knostic Manages AI Exposure," delivering "Copilot risk insights in days, not months, pinpointing precise permission or labeling issues for [Purview](microsoft-purview.md) to act on."
- Detection is AI-native (simulating inference/reconstruction risk) rather than simple content scanning, because "LLMs don't just retrieve data — they infer and reconstruct hidden insights."
- Integrations: Microsoft 365 Copilot, [glean](glean.md), Google Gemini; Microsoft [Purview](microsoft-purview.md) for remediation. Also markets shadow-AI discovery, prompt-injection and MCP-server risk checks.
- *To verify:* exact API surface (Graph scope, whether it reads production traffic vs only simulates), and whether any runtime/inline enforcement exists vs advisory-only. Vendor pages do not specify.

## Positioning & differentiators

Knostic's wedge is the **gap between ACL-mirroring and need-to-know**. Contrast the neighbors:

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

**Day-1 if you are deploying Microsoft 365 Copilot (or Glean) on a tenant with legacy SharePoint sprawl** — which describes most funds. The oversharing risk is concrete and embarrassing for an asset manager: comp, P&L, deal pipeline, LP data, and MNPI can all be synthesized out of over-shared documents by a tool every employee suddenly has. Knostic targets exactly the "we turned on Copilot and now anyone can ask about bonuses" failure mode.

Caveats for a smaller shop: it is an *added* control on top of Copilot + Purview, advisory rather than an inline guardrail, so value depends on having someone to action its findings. A 50-person fund that hasn't deployed Copilot tenant-wide may get most of the benefit from a Purview/SharePoint permissions cleanup first; Knostic earns its keep once Copilot/Glean is live at scale and you need continuous oversharing assurance. Limited direct SR 11-7 / model-risk angle — this is data-exposure governance, not model validation, though it supports the broader AI-use audit story.

## Competitors / alternatives

- [glean](glean.md) — permission-mirroring search/assistant (a target it secures, and a philosophical foil).
- [microsoft-graph](microsoft-graph.md) / native Copilot ACL enforcement.
- [microsoft-purview](microsoft-purview.md) — data labeling/DLP; complementary remediation plane.
- Broader [entitlement-aware-rag](../categories/entitlement-aware-rag.md) approaches.

## Open questions / to verify

- Exact deployment surface: Graph API scopes, read-only vs any inline enforcement, production-traffic monitoring vs simulation-only.
- Whether the $5M RSAC finalist money is structured as investment vs award, and confirmed cumulative total (~$19.3M is summed across rounds).
- Customer references / named deployments in financial services.

## Sources

- [Knostic Nabs $11 Million to Eliminate Enterprise AI Data Leaks (PRNewswire)](https://www.prnewswire.com/news-releases/knostic-nabs-11-million-to-eliminate-enterprise-ai-data-leaks-302392397.html) — fetched 2026-06-28 — supports: $11M Series A 2025-03-05, founders, founded 2023, HQ Herndon VA, need-to-know for Copilot/Glean; confidence: high.
- [About Knostic](https://www.knostic.ai/about-us) — fetched 2026-06-28 — supports: founders/roles, HQ, target verticals, product scope; confidence: med (vendor marketing).
- [Knostic Top-10 Finalist RSAC Innovation Sandbox — $5M](https://www.knostic.ai/blog/knostic-top-10-finalist-in-rsac-innovation-sandbox-contest-secures-additional-5-million-investment) — fetched 2026-06-28 — supports: $5M finalist investment Apr 2025, product covers Copilot/Glean/Gemini; confidence: med (vendor).
- [Stop Copilot Data Oversharing with Knostic & Purview (solution brief)](https://www.knostic.ai/copilot-data-oversharing-solution-brief) — fetched 2026-06-28 — supports: advisory/read-only model, Purview complementarity, inference-risk detection; confidence: med (vendor marketing).
- [Knostic Raises $3.3M for Enterprise GenAI Access Control (Dark Reading / corroborated)](https://www.darkreading.com/application-security/knostic-raises-3-3m-for-enterprise-genai-access-control) — fetched 2026-06-28 (403; via aggregated summaries) — supports: $3.3M pre-seed Apr 2024, early investors, founded 2023; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (high), founded 2023 by Gadi Evron + Sounil Yu, HQ Herndon VA + Tel Aviv (not NY), ~$19.3M funding ($3.3M pre-seed Apr 2024 / $11M Series A Mar 2025 / $5M RSAC finalist Apr 2025), advisory need-to-know layer for Copilot/Glean oversharing. No M&A. 5 sources cached. status→researched.
