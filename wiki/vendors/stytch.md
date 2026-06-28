---
title: Stytch
type: vendor
name: Stytch
slug: stytch
categories: [tool-identity-integration, non-human-identity]
layer: model-prompt
aliases: [Stytch Inc]
website: "https://stytch.com"
founded: 2020
hq: San Francisco, California, USA
ownership: acquired
ownership_detail: Acquired by Twilio; definitive agreement announced 2025-10-30, deal completed 2025-11-14 (terms undisclosed). Now a Twilio subsidiary / product line.
ownership_confidence: high
funding_total: ~$126M–$146M pre-acquisition (aggregators; not vendor-confirmed). Disclosed rounds = $120M ($30M Series A + $90M Series B).
last_funding: Series B, $90M, 2021-11 (led by Coatue; $1B valuation) — last priced round before Twilio acquisition
deployment: [saas, api, sdk]
target_customer: developers / B2B SaaS builders; startups through enterprise (developer-first CIAM)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [untrusted-input, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [authentication, ciam, oauth, mcp, agent-identity, non-human-identity, device-fingerprinting]
---

# Stytch

> Developer-first authentication/CIAM platform (passwordless, MFA, device-fingerprinting fraud) that has pivoted hard into AI-agent identity — turning your app into an OAuth provider for agents and MCP servers. Acquired by Twilio in Nov 2025.

**One-liner** — An API-first authentication and fraud platform for developers that now also does AI-agent identity: letting your app issue scoped, revocable OAuth tokens to agents and MCP servers, and detecting agentic traffic.

**Categories** — [tool-identity-integration](../categories/tool-identity-integration.md), [non-human-identity](../categories/non-human-identity.md)

## What it does

Stytch started as a developer-focused **CIAM** (customer identity and access management) platform: API-first, passwordless auth (email/SMS magic links, one-time passcodes, social sign-in, WebAuthn/passkeys, biometrics), session management, MFA, and a fraud/abuse layer built on **device fingerprinting**. The pitch was that auth should be embeddable building blocks for developers rather than a hosted "widget."

Since 2025 its center of gravity has shifted to **identity for AI agents**. Two pieces matter for this wiki:

- **Connected Apps** — turns the customer's own application into an OAuth 2.0 / OIDC authorization server, so AI agents and MCP servers can be granted **scoped, auditable, revocable** access to user data. It handles the full token lifecycle (issue/validate/refresh/revoke), consent screens, and human-in-the-loop / IT-admin approval, with the principle that an agent "inherits only the permissions the user already has." This is the **non-human-identity** angle: delegated, least-privilege access for agents acting on a user's behalf.
- **IsAgent / agent fraud detection** — IsAgent (launched 2025-08-01) is a lightweight front-end component that flags AI-agent and programmatic traffic (via User-Agent + TLS fingerprints, plus optional cryptographic self-identification) so sites can route agents to a tailored experience. Stytch is explicit that IsAgent is a "client hint, not a security guarantee"; for actual abuse prevention it points to its backend **Device Fingerprinting** product (intelligent rate limiting against scraping, prompt-injection-driven abuse, and compute abuse).

## Where it sits in the stack

Primary category: [tool-identity-integration](../categories/tool-identity-integration.md) (the agent→app/SaaS authentication-and-connector slot in the model/prompt layer); secondary: [non-human-identity](../categories/non-human-identity.md). Stytch is **infrastructure a developer embeds**, not a control a CTO buys off-the-shelf to govern their own AI usage — that distinction matters for the hedge-fund lens below.

Lethal-trifecta role: it mainly helps on the **egress** leg (scoped, revocable tokens bound what an agent can read/write through your app, instead of handing it a user's full session) and partly on **untrusted-input** (IsAgent/fingerprinting + rate limiting filter malicious automated traffic, including prompt-injection-driven abuse). It does not classify or stop sensitive-data content itself. In trust-zone terms it governs the **authorization boundary** between an agent and a first-party application.

## Deployment & architecture

- **API + SDKs** — REST/JS/backend SDKs plus pre-built UI components; "headless" option for full control. No inline proxy; it sits in the app's auth/authorization path.
- **MCP-native** — native support for the Model Context Protocol with dynamic client registration, so remote MCP servers (connecting Claude, ChatGPT, etc.) get OAuth out of the box; deployment guides for Cloudflare Workers and Vercel edge.
- **OAuth/OIDC authorization server** — Connected Apps; Authorization Code Flow with PKCE for first-party apps, third-party integrations, and CLI tools.
- **Fraud layer** — Device Fingerprinting backend + IsAgent front-end component; intelligent rate limiting.
- Key integrations: standard IdPs/social providers, MCP clients, and (post-acquisition) Twilio's communications/identity reputation data.

## Positioning & differentiators

Stytch is known as a **developer-first, API-first auth** alternative to hosted CIAM, and in 2025 it moved early and aggressively on **agent/MCP authentication**, branding itself an "identity platform for AI agents." Versus nearest neighbors:

- [descope](descope.md) — the closest comparison: also a developer-centric CIAM that has leaned hard into agentic/non-human identity and MCP auth. Stytch differentiates on its device-fingerprinting fraud heritage and (now) Twilio's reputation data.
- [workos](workos.md) — more focused on **enterprise-readiness features** (SSO/SCIM/directory sync) that B2B SaaS bolt on to sell upmarket; overlapping but more "enterprise plumbing," less fraud/consumer-auth and (historically) less agent-fraud tooling.
- [okta](okta.md) (Auth0) — the incumbent identity/CIAM platform; broader and more enterprise, with its own agent-identity initiatives. Stytch positions as lighter-weight and more developer-native.
- [cyberark](cyberark.md) — comes at non-human/agent identity from the enterprise secrets/privileged-access side, governing workloads centrally, rather than embedding OAuth into an app a developer ships.

## Ownership, funding & M&A

**Acquired by Twilio.** Definitive agreement announced **2025-10-30** (alongside Twilio's Q3 2025 results); deal **completed 2025-11-14**. Terms were **not disclosed**. Twilio's stated rationale is augmenting its platform with modern auth and **AI-agent authentication/verification**, pairing Stytch's identity stack with Twilio's communications/reputation data. Confirmed against Twilio's own announcement and Stytch's changelog → `ownership: acquired`, confidence **high**.

Pre-acquisition funding: **$30M Series A** (2021, led by Thrive Capital) and a **$90M Series B** (2021-11, led by Coatue) at a **$1B valuation** = $120M in disclosed rounds; aggregators (Crunchbase/Tracxn) list cumulative funding around **$126M–$146M**, which is not vendor-confirmed. Founded **2020 in San Francisco** by **Reed McGinley-Stempel** (CEO, ex-Plaid) and **Julianna Lamb** (CTO); some sources also list **Mark Cunningham** as a co-founder.

## CTO / hedge-fund lens

**Day-2 at most, and for most funds: not a buy at all.** Stytch is developer infrastructure you embed when **you are building an application** (or an MCP server / agent-facing API) and need to authenticate users and grant agents scoped access. A hedge fund that is a **consumer** of AI tools — running ChatGPT/Claude Enterprise, governing staff usage, doing entitlement-aware RAG — does not buy Stytch; that's why `hedge_fund_fit: low`.

It becomes relevant only if the fund **builds its own customer- or agent-facing software** (e.g. an investor portal, an internal agentic app exposed via MCP) and wants delegated, revocable, least-privilege agent access rather than handing agents broad credentials. In that narrow case its Connected Apps / MCP-auth model is a sensible control on the agent-authorization boundary. No direct SR 11-7 / model-risk relevance. Also weigh the **Twilio acquisition**: roadmap and pricing now sit inside a larger platform — a diligence point, not necessarily a negative.

## Competitors / alternatives

[descope](descope.md), [workos](workos.md), [okta](okta.md), [cyberark](cyberark.md), [composio](composio.md), [arcade](arcade.md), [stackone](stackone.md)

## Open questions / to verify

- Vendor-confirmed cumulative funding (aggregators disagree: $126M vs $146M; disclosed rounds total $120M).
- Confirm Mark Cunningham as co-founder from a primary source (press names McGinley-Stempel and Lamb consistently; Cunningham appears in aggregator profiles).
- Post-acquisition product status: will Connected Apps / IsAgent persist standalone or fold into Twilio's identity offering, and any pricing/availability changes.
- Independent (non-marketing) validation of device-fingerprinting / agent-detection accuracy.

## Sources

- [Twilio Acquires Stytch, an Identity Platform for AI Agents](https://www.twilio.com/en-us/blog/company/news/twilio-to-acquire-stytch) — fetched 2026-06-28 — supports: acquisition by Twilio, announced 2025-10-30 / completed 2025-11-14, terms undisclosed, agent-identity rationale; confidence: high (acquirer primary).
- [Stytch raises $90M Series B at $1B valuation (TechCrunch)](https://techcrunch.com/2021/11/18/stytch-api-passwordless-unicorn/) — fetched 2026-06-28 — supports: $90M Series B 2021-11 (Coatue), $30M Series A, $1B valuation, SF HQ, API-first passwordless product, developer target; confidence: high.
- [Stytch Agent Ready / AI agents & Connected Apps docs](https://stytch.com/ai-agent-ready) — fetched 2026-06-28 — supports: Connected Apps OAuth/OIDC for agents, MCP-native auth, scoped/revocable tokens, consent, agent fraud/rate-limiting, SDK+API deployment; confidence: med (vendor).
- [Introducing IsAgent (Stytch blog)](https://stytch.com/blog/introducing-is-agent/) — fetched 2026-06-28 — supports: IsAgent (2025-08-01) agent detection via UA+TLS fingerprints, "client hint not a security guarantee," Device Fingerprinting for fraud; confidence: med (vendor).
- Founders/founding year (2020; McGinley-Stempel, Lamb, Cunningham) and ~$126M–$146M cumulative funding: Crunchbase/Tracxn aggregators (not cached) — confidence: low/med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2020 (San Francisco), founders Reed McGinley-Stempel (CEO) & Julianna Lamb (CTO) (+ Mark Cunningham per aggregators), developer-first CIAM with $90M Series B (2021, Coatue, $1B valuation). **Corrected ownership from `independent` to `acquired`: Twilio acquired Stytch, announced 2025-10-30, completed 2025-11-14 (terms undisclosed), confirmed via Twilio's primary announcement — confidence high.** Documented the agent-identity angle (Connected Apps OAuth-for-agents, MCP-native auth, IsAgent/device-fingerprinting). Positioned vs [descope](descope.md)/[workos](workos.md)/[okta](okta.md)/[cyberark](cyberark.md); set hedge_fund_fit low (developer infra, not a CTO buy). status: researched, confidence medium. 4 sources cached.
