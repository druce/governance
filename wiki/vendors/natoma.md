---
title: Natoma
type: vendor
name: Natoma
slug: natoma
aka: [Natoma Labs]
primary_category: non-human-identity
also_listed_in: [mcp-gateway]
website: https://natoma.ai
founded: 2024
hq: San Francisco, California, USA
ownership_state: acquired-pending
owner: Snowflake
ownership_note: "Snowflake (NYSE: SNOW) signed a definitive agreement 2026-05-24, announced 2026-05-27; ~$110.0M in stock + cash per Snowflake's 10-Q; expected to close June 2026 subject to closing conditions. No completion announcement or SEC filing confirms close as of 2026-07-27 — treated as pending, not closed."
acquisition: {announced: 2026-05-27, closed: null, price: "~$110.0M (stock + cash)"}
funding_total: $7M (seed)
last_funding: Seed, May 2025 (led by Index Ventures and Greylock)
market_position: null
deployment_model: [saas, self-hosted, on-prem]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated
last_verified: 2026-07-27
verify_after: 2026-09-15
tags: [mcp, ai-agents, non-human-identity, agentic]
---

# Natoma

> **One-liner** — An enterprise Model Context Protocol (MCP) governance gateway that gives AI agents identity-scoped, audited, policy-controlled access to enterprise tools and data — under a signed definitive agreement to be acquired by Snowflake (~$110M; announced 2026-05-27, close not yet confirmed).

**Categories** — [non-human-identity](../categories/non-human-identity.md) (primary), [mcp-gateway](../categories/mcp-gateway.md)

## What it does
Natoma sits between AI clients/agents and the enterprise systems they want to call (SaaS apps, databases, APIs, cloud, on-prem). It standardizes those connections through MCP, then layers identity, authorization, credential management, and audit on top so an agent acts with scoped, governed permissions rather than a broad static key. Marketing positions it as the "control and governance fabric" for agent-to-tool connections: a verified MCP server library, role/intent-based tool bundles ("Profiles"), attribute-based authorization, managed-or-BYO credentials, full audit trails, and shadow-AI discovery.

## Where it sits in the stack
Foundation layer, at the intersection of [non-human-identity](../categories/non-human-identity.md) (governing the agent's identity and entitlements) and [mcp-gateway](../categories/mcp-gateway.md) (the runtime broker for MCP tool calls). It primarily constrains **outbound actions** (what an agent is allowed to do and reach) and helps protect **sensitive data** by scoping tool/data access per identity and logging it. It does not itself inspect prompts for untrusted input — that's [ai-runtime-security](../categories/ai-runtime-security.md) territory.

## Deployment & architecture
Hybrid: cloud-hosted, VPC, on-premises, and desktop (for local tool access). Acts as a gateway/broker for MCP servers. Integrations called out: SIEM, EDR, MDM; identity-aware access controls; credential vaulting (managed or bring-your-own). SOC2 certified; GDPR/CCPA compliant per vendor.

## Positioning & differentiators
Natoma is an MCP-native entrant (founded 2024, as MCP itself was emerging) rather than a legacy NHI/secrets vendor extending into agents. Its pitch is governance *at the MCP layer* — a verified server registry plus identity-aware, attribute-based authorization on every tool call — which differentiates it from secrets-lifecycle players like [entro-security](entro-security.md) and [clutch-security](clutch-security.md) and from pure MCP brokers like [mintmcp](mintmcp.md), [obot](obot.md), or [arcade](arcade.md). Against [mcp-gateway](../categories/mcp-gateway.md) peers it leans harder on identity governance and shadow-AI discovery; against [non-human-identity](../categories/non-human-identity.md) peers it leans harder on the agent/MCP runtime.

## Ownership, funding & M&A
- **Independent funding:** $7M seed, May 2025, led by Index Ventures and Greylock. Founder/CEO Pratyus Patnaik (previously founded atSpoke, acquired by Okta in 2021; then senior director at Okta). Founding team drawn from Okta, Microsoft, Google, Salesforce.
- **M&A — announced, not confirmed closed:** Snowflake (NYSE: SNOW) **signed a definitive agreement on 2026-05-24** to acquire all outstanding capital stock of **Natoma Labs, Inc.**, announcing it publicly on **2026-05-27**. Snowflake's Form 10-Q for the quarter ended 2026-04-30 (filed 2026-05-29) discloses total stated consideration of **~$110.0 million**, primarily Snowflake common stock with the remainder in cash, with ~30% of the equity consideration subject to vesting conditions (accounted for as post-combination stock-based compensation — i.e. a meaningful retention package for the team). The 10-Q states the transaction "is expected to close in June 2026, subject to satisfaction of certain closing conditions," and tags the disclosure with XBRL's `srt:ScenarioForecastMember` — a forecast, not an actual.
- **Close status as of 2026-07-27: unconfirmed.** The expected June 2026 close window has elapsed with no public confirmation either way. Checked and found nothing: EDGAR full-text search returns no 8-K Item 2.01 (completion of acquisition); Snowflake's newsroom carries only the "Announces **Intent** to Acquire" release; natoma.ai is still live on its own domain, its banner reading "Natoma is joining forces with Snowflake" and its 2026-05-27 blog post still using the unchanged "has signed a definitive agreement to acquire" phrasing; and no trade-press report of consummation exists. Note the absence of a completion 8-K is weak evidence — at ~$110M this deal is very likely below Snowflake's Reg S-X significance threshold, so no such filing would be *required*. Per CLAUDE.md §7 ("Announced ≠ closed"), recorded as `acquired-pending`. The clean resolution is Snowflake's **Q2 FY2027 10-Q** (quarter ended 2026-07-31, normally filed late Aug / early Sept), where a closed deal would appear in purchase-price accounting rather than as a forecast subsequent event — hence `verify_after: 2026-09-15`.
- **Strategic intent:** Natoma is an **AI agent enablement / governed-access** vendor being folded into Snowflake's platform rather than run as a standalone security product. Its capabilities are slated to integrate with Snowflake Intelligence, Cortex Agents, and Cortex Code, giving Snowflake a natively integrated governance and identity layer for AI agents and MCP tool access.

## CTO / hedge-fund lens
Day-2 for most funds: relevant once you are actually deploying internal AI agents that call live enterprise systems and you need per-agent entitlements and an audit trail rather than shared API keys. The Snowflake acquisition matters two ways: (1) if you are a Snowflake shop, this likely becomes a native governance feature rather than a separate buy; (2) if you are not, Natoma's roadmap and standalone availability now carry integration-uncertainty risk. Because the deal is signed but not confirmed closed, treat any near-term procurement as transitional — diligence the post-close support and standalone-licensing commitments in writing rather than relying on current terms. No direct SR 11-7 / model-risk role, but the audit trail and access scoping support operational-risk and access-control evidence for agentic workflows.

## Competitors / alternatives
[mintmcp](mintmcp.md), [obot](obot.md), [arcade](arcade.md), [ibm-contextforge](ibm-contextforge.md), [pomerium](pomerium.md) (MCP gateways); [entro-security](entro-security.md), [clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md) (non-human / agent identity); [astrix-security](astrix-security.md).

## Open questions / to verify
- **Did the deal actually close?** Expected June 2026; unconfirmed as of 2026-07-27. Re-check Snowflake's Q2 FY2027 10-Q (quarter ended 2026-07-31) after 2026-09-15 for purchase accounting confirming a close date.
- Whether Natoma remains available standalone post-close, and whether it will continue selling to non-Snowflake customers.
- Hard numbers on customers/scale (only vendor-stated metrics found).

## Sources
- [Snowflake Inc. Form 10-Q, quarter ended 2026-04-30 (filed 2026-05-29), Note: Subsequent Events](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000030/snow-20260430.htm) — fetched 2026-07-27 — cached: `raw/sources/2026-07-27--natoma--snowflake-10q-subsequent-event.md` — supports: definitive agreement signed 2026-05-24, target entity Natoma Labs Inc., ~$110.0M consideration (stock + cash), ~30% equity subject to vesting, **expected to close June 2026 subject to closing conditions (i.e. NOT closed as of filing)**; confidence: high (primary SEC filing)
- [Snowflake Announces Intent to Acquire Natoma](https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-natoma-providing-secure-connectivity-for-the-agentic-enterprise/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: public announcement date 2026-05-27, what Natoma does, founder; note: this is the *intent* release — no completion release exists on Snowflake's newsroom as of 2026-07-27; confidence: high
- [Natoma is Joining Snowflake](https://natoma.ai/blog/natoma-snowflake) — fetched 2026-07-27 — supports: Natoma's own 2026-05-27 post still reads "Snowflake **has signed a definitive agreement to acquire** Natoma" (announcement, not completion, language); site live on its own domain; confidence: high
- [Natoma Platform](https://natoma.ai/platform) — fetched 2026-06-28 — supports: product/MCP features, deployment, integrations (vendor marketing); confidence: med
- Web search (Crunchbase, Index Ventures, press) — fetched 2026-06-28 — supports: founded 2024, HQ San Francisco, $7M seed May 2025 (Index/Greylock), CEO Pratyus Patnaik; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Snowflake acquisition (intent announced 2026-05-27, primary PR) — corrected ownership independent→acquired (high confidence); established founded 2024, HQ San Francisco, $7M seed (May 2025, Index/Greylock), CEO Pratyus Patnaik; MCP governance gateway / NHI positioning; hedge_fund_fit medium.
- [2026-07-27] **Status correction (contradiction resolved): `acquired-closed` → `acquired-pending`.** The page carried `acquisition.closed: 2026-05-27` — identical to the announced date — while its own body text said the deal was "subject to customary closing conditions; close date not stated." That close date was never sourced; it appears to have been set by duplicating the announcement date. Verified against Snowflake's Form 10-Q (filed 2026-05-29), which states the definitive agreement was signed 2026-05-24 for ~$110.0M and "is expected to close in June 2026, subject to satisfaction of certain closing conditions," tagged in XBRL as `srt:ScenarioForecastMember`. No completion evidence found as of 2026-07-27 (no 8-K Item 2.01 in EDGAR full-text search; no Snowflake completion press release; natoma.ai still live and still using "has signed a definitive agreement" language). Set `closed: null`, added price ~$110.0M (stock + cash), `verify_after: 2026-09-15` (Snowflake Q2 FY2027 10-Q should settle it). Also noted Natoma is an AI agent enablement/governed-access vendor being folded into the Snowflake platform (Snowflake Intelligence, Cortex Agents, Cortex Code).
