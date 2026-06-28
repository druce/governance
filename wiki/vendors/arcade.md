---
type: vendor
name: Arcade.dev
slug: arcade
categories: [mcp-gateway, tool-identity-integration]
layer: model-prompt
aliases: [Arcade AI, ArcadeAI]
website: "https://www.arcade.dev"
founded: 2024
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: VC-backed startup; $72M raised across seed + Series A. No M&A.
ownership_confidence: high
funding_total: $72M
last_funding: Series A — $60M — 2026-06 (led by SYN Ventures)
deployment: [saas, self-hosted, on-prem, sdk, api]
target_customer: enterprise (incl. regulated — banks, pharma, industrials)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [egress, sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [agent-tool-calling, oauth, mcp, tool-auth, agent-identity]
---

# Arcade.dev

**One-liner** — Infrastructure that lets AI agents call real tools (Gmail, Slack, GitHub, Salesforce…) on behalf of a *specific authenticated user*, handling the OAuth/token plumbing so the agent acts with that user's permissions instead of a god-mode service account.

## What it does

Arcade is an authenticated tool-calling / "secure action layer" for AI agents. The hard part of giving an agent the ability to *do* things (send an email, post to Slack, open a GitHub issue) isn't the model call — it's auth: the agent needs a valid OAuth token scoped to the right user with the right permissions, and you don't want the model or the client to ever see those secrets.

Arcade solves that. It ships thousands of pre-built tools (toolkits for Gmail, Google Workspace, Microsoft 365, Slack, GitHub, Salesforce, HubSpot, Stripe, Zoom, etc.) plus an SDK to build custom ones. Each tool declares the OAuth scopes it needs (e.g. `Gmail.SendEmail` → `gmail.send`). When an agent calls a tool, the **Arcade Engine** checks whether the calling user has already authorized those scopes; if not, it triggers the OAuth 2.0 consent flow with the provider, stores the resulting token, and on every subsequent call **injects the token into the tool execution at runtime — the LLM and the client never see the secret**. Tokens are remembered until revoked, and Arcade keeps an audit trail of which agent did what, for whom, on which resource.

The pitch (their words): "Agents fail because nobody can prove that this agent, on behalf of this user, can perform this action on this resource." Arcade's job is to make that provable.

## Where it sits in the stack

- **Primary category:** [tool-identity-integration](../categories/tool-identity-integration.md) — Arcade is fundamentally about *non-human / delegated identity*: binding an agent's tool call to an authenticated end-user's OAuth grant and scopes. (Frontmatter keeps `mcp-gateway` first for registry continuity, but the substance is tool-identity; see History.)
- **Secondary:** [mcp-gateway](../categories/mcp-gateway.md) — Arcade authored the MCP authorization spec (a marketing/credibility claim it says Anthropic adopted) and hosts/serves MCP tools to clients like Cursor, Claude Desktop and VS Code, so it functions as an MCP runtime/gateway too.
- **Layer:** model-prompt (it mediates what the model is allowed to *invoke*).
- **Lethal-trifecta role:** controls the **egress** leg (the agent can only take actions it's been explicitly, user-scoped authorized to take) and guards **sensitive-data** access (tokens are scoped and never exposed to the model). It does *not* inspect untrusted input — pair it with a prompt-injection / runtime-security layer for that.
- **Trust zone:** sits at the boundary between the agent (yellow/untrusted reasoning) and external SaaS systems (where the real data and side effects live).

## Deployment & architecture

- **Models:** managed SaaS (Arcade Cloud) **and** self-hosted — deployable in your own cloud (AWS/Azure/GCP), VPC, on-prem, or fully air-gapped. The air-gapped/self-host option is the relevant one for a regulated buyer.
- **Core component:** the **Arcade Engine**, which coordinates OAuth flows, stores/refreshes tokens, enforces scopes, and executes tool calls. Tokens are injected server-side at call time.
- **Auth mechanisms:** OAuth 2.0, API keys, and user tokens; scope-based permissioning per tool. Integrates with existing IdPs (Okta, Microsoft Entra, SailPoint per the Series A release).
- **Integrations / frameworks:** LangChain, OpenAI Agents SDK, Google ADK, CrewAI, AG2, Vercel AI SDK, Spring AI; MCP servers for IDE/agent clients. Python-first SDK (`arcade-mcp`), open-source tool framework on GitHub (github.com/ArcadeAI).

## Positioning & differentiators

Arcade's distinctive angle is **per-user delegated authorization at the moment of action**, not just a catalog of tool connectors. Compared with neighbors:

- vs [composio](composio.md) and [stackone](stackone.md) — these are also "many pre-built tool integrations for agents" platforms; Composio overlaps most directly. Arcade leans harder on the auth/identity story and self-host/air-gap for regulated shops.
- vs [descope](descope.md), [stytch](stytch.md), [workos](workos.md) — these are auth/CIAM vendors that have added agent/MCP auth primitives; they give you the OAuth/token machinery but you assemble the tools. Arcade bundles the token machinery *with* a large pre-built tool library and execution runtime. WorkOS itself published an explainer on Arcade, framing it as an LLM tool-calling platform.
- vs [mintmcp](mintmcp.md), [obot](obot.md), [agentgateway](agentgateway.md), [natoma](natoma.md) — these are MCP-gateway / MCP-management plays (hosting, proxying, governing MCP servers). Arcade competes on the MCP-runtime side but its center of gravity is authorized *execution*, not just gatewaying traffic.

The "thousands of pre-built tools" (8,000+ tool count cited at Series A) and "authored the MCP auth spec" are vendor/marketing claims — credible but not independently audited here.

## Ownership, funding & M&A

- **Independent, VC-backed.** No acquisition.
- **Founded:** February 2024, San Francisco.
- **Founders:** Alex Salazar (CEO), Sam Partee (CTO, ex-Redis).
- **Seed:** $12M, March 2025 — led by Laude Ventures; strategic angels incl. Andy Konwinski (Perplexity co-founder) and Pete Sonsini (NEA).
- **Series A:** $60M, June 2026 — led by SYN Ventures, with strategic investment from Morgan Stanley and Wipro; Jay Leek (SYN) joined the board.
- **Total:** $72M. Ownership confidence: **high** (dated primary funding releases + vendor blog).

## CTO / hedge-fund lens

- **Day-2.** You need this only once you're moving agents from read-only/RAG into *taking actions* in real systems (sending mail, updating CRM, touching repos). Before that, it's premature.
- **When it earns its place:** when you want agents to act *as a specific employee* with that person's existing entitlements, and you need an audit trail proving "this agent did X for user Y" — exactly the control story a regulated/compliance-sensitive shop wants before letting an agent write anywhere. The self-host/air-gapped option and IdP integration (Okta/Entra) matter here; SaaS-only token custody for Gmail/GitHub would be a harder sell internally.
- **Posture fit:** medium for a hedge fund. Compelling *if* you're building internal agents that act across SaaS; less relevant if your AI use stays at chat/RAG/coding-assistant level. The Morgan Stanley strategic investment and named bank/pharma deployments suggest it's being taken seriously by regulated buyers, but verify references yourself — these are the vendor's claims.
- Not a model-risk / SR 11-7 tool; it's an access-control and accountability layer.

## Competitors / alternatives

[composio](composio.md), [stackone](stackone.md), [descope](descope.md), [stytch](stytch.md), [workos](workos.md), [mintmcp](mintmcp.md), [obot](obot.md), [agentgateway](agentgateway.md), [natoma](natoma.md)

## Open questions / to verify

- Independent confirmation of the "8,000+ tools" and "authored the MCP auth spec adopted by Anthropic" claims (currently vendor-stated).
- Real-world token-custody model for SaaS deployment — where tokens are stored, encryption, tenant isolation (matters for a fund's security review).
- Named regulated-customer references (banks/pharma) are vendor claims, unverified.
- Pricing model (not researched).
- Exact split of open-source (`arcade-mcp`) vs proprietary Engine functionality.

## Sources
- [Arcade: The MCP Runtime for Production AI Agents (home)](https://www.arcade.dev/) — fetched 2026-06-28 — supports: positioning as secure action layer / MCP runtime; confidence: med (marketing).
- [About Arcade — docs](https://docs.arcade.dev/en/get-started/about-arcade) — fetched 2026-06-28 — supports: OAuth/scopes auth model, Engine, runtime token injection, frameworks, integrations, MCP support; confidence: high (primary docs).
- [Arcade.dev Raises $60M Series A (blog)](https://www.arcade.dev/blog/arcade-series-a/) — fetched 2026-06-28 — supports: $60M Series A, SYN Ventures lead, Morgan Stanley/Wipro, $72M total, deployment, IdP integrations, customer claims; confidence: high (primary).
- [Arcade Raises $60M (BusinessWire, 2026-06-15)](https://www.businesswire.com/news/home/20260615229631/en/Arcade-Raises-$60M-to-Become-the-Secure-Action-Layer-Behind-Every-Production-AI-Agent) — fetched 2026-06-28 — supports: Series A details, founders, HQ; confidence: high.
- [Arcade.dev Scores $12M Seed (BusinessWire, 2025-03-18)](https://www.businesswire.com/news/home/20250318815130/en/Arcade.dev-Scores-$12M-to-Solve-the-Biggest-Security-Problem-with-AI-Agents) — fetched 2026-06-28 — supports: seed $12M, founders, founding date; confidence: high.
- [What is Arcade.dev? An LLM tool calling platform — WorkOS](https://workos.com/blog/what-is-arcade-dev-an-llm-tool-calling-platform) — fetched 2026-06-28 — supports: third-party framing of Arcade as LLM tool-calling platform; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed startup (founded Feb 2024, SF; founders Alex Salazar / Sam Partee), $72M total funding ($12M seed Mar-2025 Laude Ventures, $60M Series A Jun-2026 SYN Ventures + Morgan Stanley/Wipro) — ownership_confidence raised to high. Confirmed product = authenticated per-user tool-calling via OAuth scopes with runtime token injection; SaaS + self-host/air-gap; MCP runtime + tool-identity. Categories kept as [mcp-gateway, tool-identity-integration] but argued primary substance is tool-identity (noted in body). trifecta = egress + sensitive-data. hedge_fund_fit = medium. Cached 3 source files.
