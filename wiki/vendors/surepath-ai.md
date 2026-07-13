---
title: SurePath AI
type: vendor
name: SurePath AI
slug: surepath-ai
aka: []
primary_category: ai-access-governance
also_listed_in: []
website: https://www.surepath.ai
founded: 2023
hq: Denver, Colorado, USA
ownership_state: acquired-pending
owner: F5
ownership_note: Acquisition by [f5](f5.md) announced 2026-06-22 as part of the F5 AI Security Platform launch; terms undisclosed; close date not yet confirmed
acquisition: {announced: 2026-06-22, closed: null, price: null}
funding_total: $6.3M (pre-acquisition)
last_funding: $5.2M seed announced 2024-11-14 (Uncork Capital lead, Operator Collective)
market_position: null
deployment_model: [saas]
form_factor: [inline-proxy, platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: mid-to-large enterprise
last_verified: 2026-07-13
verify_after: 2026-10-01
tags: [acquired, shadow-ai, ai-discovery, ai-access-governance]
---

# SurePath AI

> **Researched 2026-07-13.** Primary category: [ai-access-governance](../categories/ai-access-governance.md). **Acquisition by [f5](f5.md) announced 2026-06-22** — close not yet confirmed; re-verify after 2026-10-01.

**One-liner** — A network-based shadow-AI discovery and workforce-GenAI governance platform (find every AI tool in use, classify intent, enforce inline policy) that F5 is folding into its new AI Security Platform.

## What it does
SurePath AI governs how employees use generative AI — the tools you build, adopt, or buy, including the ones nobody approved. Its distinguishing mechanism is **network-based discovery**: deployment via network redirects and out-of-band analysis rather than per-application integrations, so it sees sanctioned and unsanctioned AI use alike. On top of discovery it layers **intent classification** (what the user is trying to do, not just which domain they hit), inline risk mitigation (detects and redacts sensitive data in prompts, role-based access controls, policy-driven guardrails), audit trails of GenAI conversations, and a branded **enterprise GenAI portal** that gives employees a sanctioned front door to public and private models. F5 also credits it with tracing agent tool calls and MCP server connections — extending the visibility layer from human chat use to agentic workflows.

## Where it sits in the stack
Primary [ai-access-governance](../categories/ai-access-governance.md) (CASB-for-AI / shadow-AI): it governs the AI your people reach for, not the AI apps you build (that's [ai-runtime-security](../categories/ai-runtime-security.md)). Layer: model-prompt. It is exactly the category's "velvet rope" pattern — discovery of unsanctioned use plus intent-aware inline policy on what data flows to which model — with the added twist of a sanctioned-portal carrot alongside the enforcement stick.

## Deployment & architecture
Cloud SaaS (admin console at admin.surepath.ai) with enforcement via network redirects; discovery analysis runs out-of-band. The no-per-app-integration approach is the selling point versus API-integrated rivals: faster coverage of the long tail of AI-enabled SaaS, at the cost of the deeper in-app context an API integration can see. Whether prompt/conversation data leaves the customer tenancy (retention, training use) is unverified.

## Positioning & differentiators
- **Network-based, integration-free discovery** — coverage of shadow AI without waiting on connectors; F5 calls it a pioneer of network-based AI discovery.
- **Intent classification** — policy keyed to what the user is doing, not just the destination domain; same intent-aware pattern as [witnessai](witnessai.md).
- **Enable, not block** — the enterprise GenAI portal + request enrichment aim to convert shadow users into governed users, closer in spirit to [nudge-security](nudge-security.md) than to a pure blocker.
- **Agent/MCP visibility** (per F5) — traces agent tool calls and MCP server connections, a forward-looking angle most shadow-AI peers lack.

Nearest neighbors: [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [lanai](lanai.md), [wald-ai](wald-ai.md), [portal26](portal26.md), [nudge-security](nudge-security.md).

## Ownership, funding & M&A
Founded **2023**, HQ **Denver, Colorado**; founders Casey Bleeker (CEO) and Randy Birdsall. Raised a **$5.2M seed** (announced 2024-11-14, led by Uncork Capital with Operator Collective; **$6.3M total**). **F5 announced its acquisition of SurePath AI on 2026-06-22**, simultaneously with the launch of the **F5 AI Security Platform**, where SurePath becomes the discovery/visibility layer feeding F5's guardrails and red-team products (the ex-[calypsoai](calypsoai.md) assets). Terms undisclosed; the press release does not state a closing date, so status is **acquired-pending** until completion is confirmed. Verified against F5's own press release. Confidence: high on the announcement, open on the close.

## CTO / hedge-fund lens
Shadow-AI governance is a Day-1 concern for a fund (MNPI in consumer chatbots), and SurePath's integration-free network deployment suits a lean IT team. But the F5 acquisition changes the evaluation: expect it to be packaged as the visibility layer of the F5 AI Security Platform rather than sold standalone indefinitely. Natural fit if you're already an F5 shop or want discovery + guardrails + red-team from one vendor; if not, the independent specialists ([harmonic-security](harmonic-security.md), [witnessai](witnessai.md), [aurascape](aurascape.md)) or your SASE vendor's AI-guard module are the comparators. Site claims finance-sector customers (unnamed) — fs_traction: claimed, not verified.

## Competitors / alternatives
[witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [nudge-security](nudge-security.md), [lanai](lanai.md), [cyberhaven](cyberhaven.md), [wald-ai](wald-ai.md), [portal26](portal26.md), [acuvity](acuvity.md) (the closest analogue — also discovery-led, also platform-acquired in 2026, by Proofpoint), [zscaler](zscaler.md) (AI Guard), [netskope](netskope.md) (Netskope One).

## Open questions / to verify
- **Acquisition close date** — announced 2026-06-22; no completion notice found as of 2026-07-13. Re-check after 2026-10-01.
- Deal price/terms (undisclosed at announcement).
- Whether SurePath remains purchasable standalone or is absorbed into F5 AI Security Platform SKUs; brand survival.
- Data handling: does prompt/conversation capture leave the customer tenancy; retention and training-use policy.
- Depth of MCP/agent tracing (F5 marketing claim — no independent corroboration found).
- Certifications (SOC 2 etc.) and named FS customers.

## Sources
- [F5 launches AI Security Platform (F5 press release)](https://www.f5.com/company/news/press-releases/f5-ai-security-platform-control-enterprise-risk) — fetched 2026-07-13 — supports: acquisition announced 2026-06-22, no close date/terms, network-based discovery + intent classification + MCP tracing description; confidence: high. Cached: `raw/sources/2026-07-13--surepath-ai--f5-acquisition-pr.md`
- [SurePath AI homepage](https://www.surepath.ai/) — fetched 2026-07-13 — supports: product capabilities, GenAI portal, target sectors, SaaS deployment; confidence: med (vendor marketing). Cached: `raw/sources/2026-07-13--surepath-ai--homepage.md`
- [SurePath AI announces over $5M in seed funding (PRNewswire)](https://www.prnewswire.com/news-releases/surepath-ai-announces-over-5-million-in-seed-funding-to-secure-genai-adoption-in-the-enterprise-302304040.html) — fetched 2026-07-13 — supports: $5.2M seed 2024-11-14, Uncork/Operator Collective, $6.3M total, Denver HQ, founded 2023, founders; confidence: med (company release, factual details). Cached: `raw/sources/2026-07-13--surepath-ai--seed-funding-pr.md`

## History
- [2026-07-13] Page created via wiki-create (user-requested addition, not in seeds) and researched same day: categorized ai-access-governance; F5 acquisition announced 2026-06-22 flagged acquired-pending with verify_after 2026-10-01.
