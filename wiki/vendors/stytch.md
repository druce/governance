---
title: Stytch
type: vendor
name: Stytch
slug: stytch
aka: [Stytch Inc]
primary_category: tool-identity-integration
also_listed_in: [non-human-identity]
website: https://stytch.com
founded: 2020
hq: San Francisco, California, USA
ownership_state: acquired-closed
owner: Twilio
ownership_note: 'Acquired by Twilio (NYSE: TWLO). Definitive agreement announced 2025-10-30 (per Twilio Q3 2025 Form 10-Q); closed 2025-11-14 for $104.1M cash, or $58.5M net of cash acquired (per Twilio FY2025 Form 10-K, Note 11 — Twilio''s blog said terms undisclosed). Now a Twilio subsidiary; Stytch brand and stytch.com retained.'
acquisition: {announced: 2025-10-30, closed: 2025-11-14, price: '$104.1M cash ($58.5M net of cash acquired; Twilio FY2025 10-K)'}
funding_total: ~$126M–$146M pre-acquisition (aggregators; not vendor-confirmed). Disclosed rounds = $120M ($30M Series A + $90M Series B).
last_funding: Series B, $90M, 2021-11 (led by Coatue; $1B valuation) — last priced round before Twilio acquisition
market_position: null
deployment_model: [saas]
form_factor: [api, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: developers / B2B SaaS builders; startups through enterprise (developer-first CIAM)
last_verified: 2026-07-27
verify_after: null
tags: [authentication, ciam, oauth, mcp, agent-identity, non-human-identity, device-fingerprinting, twilio, acquired]
sources:
  - {claim: acquisition-announced, url: "https://www.sec.gov/Archives/edgar/data/1447669/000144766925000151/twlo-20250930.htm", date: 2025-10-31, confidence: high}
  - {claim: acquisition-close, url: "https://www.sec.gov/Archives/edgar/data/1447669/000144766926000021/twlo-20251231.htm", date: 2026-07-27, confidence: high}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1447669/000144766926000021/twlo-20251231.htm", date: 2026-07-27, confidence: high}
---

# Stytch

> **Researched 2026-06-28; re-verified 2026-07-27 against Twilio's SEC filings.** Developer-first authentication/CIAM platform (passwordless, MFA, device-fingerprinting fraud) that pivoted hard into AI-agent identity — turning your app into an OAuth provider for agents and MCP servers. **Acquired by Twilio (NYSE: TWLO): announced 2025-10-30, closed 2025-11-14 for $104.1M cash** ($58.5M net of cash acquired). `stytch.com` is still live (HTTP 200, no redirect), still Stytch-branded, and banners "Stytch has joined Twilio to build the intelligent identity layer for the internet." **No longer an independent company.**

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

Stytch is known as a **developer-first, API-first auth** alternative to hosted CIAM, and in 2025 it moved early and aggressively on **agent/MCP authentication**, branding itself an "identity platform for AI agents."

**Since 2025-11-14 this is a platform-vendor conversation, not a startup one.** Stytch is now a Twilio product line, so evaluate it the way you would any Twilio component: bundled commercially with Twilio's communications/verification stack (Verify, Lookup), roadmap set by Twilio's platform priorities, and procurement/MSA likely running through Twilio rather than a standalone startup contract. The upside is counterparty durability — a startup-risk discount that no longer applies. The downside is the usual acquired-product risks: pricing repackaging into platform bundles, and a real question of investment level given the modest purchase price. The independent-vendor differentiation below is therefore historical framing; today the sharper question is Twilio-vs-alternative-platform.

Versus nearest neighbors:

- [descope](descope.md) — the closest comparison: also a developer-centric CIAM that has leaned hard into agentic/non-human identity and MCP auth. **Descope is now the main remaining independent option in this niche**, which matters if you specifically want a vendor whose roadmap is not subordinate to a larger platform. Stytch differentiates on its device-fingerprinting fraud heritage and (now) Twilio's communications/reputation data.
- [workos](workos.md) — more focused on **enterprise-readiness features** (SSO/SCIM/directory sync) that B2B SaaS bolt on to sell upmarket; overlapping but more "enterprise plumbing," less fraud/consumer-auth and (historically) less agent-fraud tooling.
- [okta](okta.md) (Auth0) — the incumbent identity/CIAM platform; broader and more enterprise, with its own agent-identity initiatives. Stytch positions as lighter-weight and more developer-native.
- [cyberark](cyberark.md) — comes at non-human/agent identity from the enterprise secrets/privileged-access side, governing workloads centrally, rather than embedding OAuth into an app a developer ships.

## Ownership, funding & M&A

**Acquired by Twilio (NYSE: TWLO).** Definitive agreement announced **2025-10-30**, alongside Twilio's Q3 2025 results; deal **closed 2025-11-14**. Both dates are confirmed in Twilio's own SEC filings, not just its blog: the Q3 2025 **Form 10-Q** (filed 2025-10-31) states "On October 30, 2025, we entered into a definitive agreement to acquire Stytch, Inc. … We expect the transaction to close in the fourth quarter of 2025," and the FY2025 **Form 10-K** (Note 11, Business Combinations) states "On November 14, 2025, the Company acquired all outstanding shares of Stytch, Inc."

**Price: $104.1M in cash, or $58.5M net of cash acquired.** Twilio's press announcement called terms undisclosed, but the 10-K discloses the full preliminary purchase-price allocation: $45.6M of the price was Stytch's own balance-sheet cash, $11.8M was identifiable intangibles (developed technology $9.9M over a 5-year life; customer relationships $2.0M over 4 years), and **$48.5M was goodwill**.

That price is worth reading carefully. **$104.1M gross is below the ~$120M Stytch raised in disclosed primary rounds**, and roughly a tenth of its $1B Series B valuation from 2021. With effective enterprise value near **$58.5M** and only ~$11.8M booked as identifiable technology and customer intangibles, this looks like a soft landing / talent-and-tech tuck-in rather than a premium strategic exit — a signal that the developer-CIAM market did not support a standalone $1B outcome, and a fair diligence question about how much runway the product line gets inside Twilio.

Twilio's stated rationale is augmenting its platform with modern auth and **AI-agent authentication/verification**, pairing Stytch's identity stack with Twilio's communications and phone/identity reputation data — the "intelligent identity layer" framing now on stytch.com. Post-close, Twilio Inc. is the parent and data controller while Stytch, Inc. continues as the day-to-day data processor; the Stytch brand, domain, and product names (Connected Apps, IsAgent, Device Fingerprinting) all persist as of 2026-07-27.

Pre-acquisition funding: **$30M Series A** (2021, led by Thrive Capital) and a **$90M Series B** (2021-11, led by Coatue) at a **$1B valuation** = $120M in disclosed rounds; aggregators (Crunchbase/Tracxn) list cumulative funding around **$126M–$146M**, which is not vendor-confirmed. Founded **2020 in San Francisco** by **Reed McGinley-Stempel** (CEO, ex-Plaid) and **Julianna Lamb** (CTO); some sources also list **Mark Cunningham** as a co-founder.

## CTO / hedge-fund lens

**Day-2 at most, and for most funds: not a buy at all.** Stytch is developer infrastructure you embed when **you are building an application** (or an MCP server / agent-facing API) and need to authenticate users and grant agents scoped access. A hedge fund that is a **consumer** of AI tools — running ChatGPT/Claude Enterprise, governing staff usage, doing entitlement-aware RAG — does not buy Stytch; that's why `hedge_fund_fit: low`.

It becomes relevant only if the fund **builds its own customer- or agent-facing software** (e.g. an investor portal, an internal agentic app exposed via MCP) and wants delegated, revocable, least-privilege agent access rather than handing agents broad credentials. In that narrow case its Connected Apps / MCP-auth model is a sensible control on the agent-authorization boundary. No direct SR 11-7 / model-risk relevance.

Weigh the **Twilio acquisition** in both directions. It removes startup-viability risk — you are now contracting with a public company already common in fund tech stacks for SMS/voice, which simplifies vendor due diligence and may let you add Stytch under an existing Twilio MSA. But the **$104.1M price (below money raised, ~$58.5M net of cash, only $11.8M of identifiable intangibles)** says Twilio bought this cheaply, so ask pointed questions about committed roadmap, standalone product survival, and repricing at renewal before you build a dependency on Connected Apps or IsAgent. If you want an independent vendor in this slot, [descope](descope.md) is the comparable that has not been acquired.

## Competitors / alternatives

[descope](descope.md), [workos](workos.md), [okta](okta.md), [cyberark](cyberark.md), [composio](composio.md), [arcade](arcade.md), [stackone](stackone.md)

## Open questions / to verify

- Vendor-confirmed cumulative funding (aggregators disagree: $126M vs $146M; disclosed rounds total $120M).
- Confirm Mark Cunningham as co-founder from a primary source (press names McGinley-Stempel and Lamb consistently; Cunningham appears in aggregator profiles).
- Post-acquisition product status: as of 2026-07-27 the Stytch brand, domain, and product names all persist, but whether Connected Apps / IsAgent stay standalone or fold into Twilio's identity offering — and any pricing/packaging changes into Twilio bundles — is still open. Re-check at the next Twilio product event.
- Independent (non-marketing) validation of device-fingerprinting / agent-detection accuracy.

## Sources

- [Twilio Form 10-K, FY2025 (Note 11, Business Combinations)](https://www.sec.gov/Archives/edgar/data/1447669/000144766926000021/twlo-20251231.htm) — fetched 2026-07-27 — supports: **close date 2025-11-14**, **purchase price $104.1M cash / $58.5M net of cash acquired**, purchase-price allocation (goodwill $48.5M, intangibles $11.8M, cash acquired $45.6M); confidence: high (acquirer SEC filing). Cached: `raw/sources/2026-07-27--stytch--twilio-sec-filings.md`.
- [Twilio Form 10-Q, Q3 2025 (filed 2025-10-31)](https://www.sec.gov/Archives/edgar/data/1447669/000144766925000151/twlo-20250930.htm) — fetched 2026-07-27 — supports: **announced date 2025-10-30** ("On October 30, 2025, we entered into a definitive agreement to acquire Stytch, Inc."), and that the deal was still pending as of that filing (announced ≠ closed); confidence: high (acquirer SEC filing).
- [Twilio Acquires Stytch, an Identity Platform for AI Agents](https://www.twilio.com/en-us/blog/company/news/twilio-to-acquire-stytch) — fetched 2026-06-28 — supports: acquisition by Twilio, announced 2025-10-30 / completed 2025-11-14, agent-identity rationale; note this source says terms were **undisclosed** — the price came from the 10-K; confidence: high (acquirer primary).
- [Stytch changelog: A new chapter begins — Stytch joins Twilio (2025-11-14)](https://changelog.stytch.com/announcements/2025-11-14-a-new-chapter-begins-stytch-joins-twilio) — fetched 2026-07-27 — supports: close confirmed by the target on 2025-11-14 ("Twilio's acquisition of Stytch is now final"), Twilio Inc. as parent/data controller with Stytch, Inc. as day-to-day processor; confidence: high (target primary).
- [Stytch raises $90M Series B at $1B valuation (TechCrunch)](https://techcrunch.com/2021/11/18/stytch-api-passwordless-unicorn/) — fetched 2026-06-28 — supports: $90M Series B 2021-11 (Coatue), $30M Series A, $1B valuation, SF HQ, API-first passwordless product, developer target; confidence: high.
- [Stytch Agent Ready / AI agents & Connected Apps docs](https://stytch.com/ai-agent-ready) — fetched 2026-06-28 — supports: Connected Apps OAuth/OIDC for agents, MCP-native auth, scoped/revocable tokens, consent, agent fraud/rate-limiting, SDK+API deployment; confidence: med (vendor).
- [Introducing IsAgent (Stytch blog)](https://stytch.com/blog/introducing-is-agent/) — fetched 2026-06-28 — supports: IsAgent (2025-08-01) agent detection via UA+TLS fingerprints, "client hint not a security guarantee," Device Fingerprinting for fraud; confidence: med (vendor).
- Founders/founding year (2020; McGinley-Stempel, Lamb, Cunningham) and ~$126M–$146M cumulative funding: Crunchbase/Tracxn aggregators (not cached) — confidence: low/med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2020 (San Francisco), founders Reed McGinley-Stempel (CEO) & Julianna Lamb (CTO) (+ Mark Cunningham per aggregators), developer-first CIAM with $90M Series B (2021, Coatue, $1B valuation). **Corrected ownership from `independent` to `acquired`: Twilio acquired Stytch, announced 2025-10-30, completed 2025-11-14 (terms undisclosed), confirmed via Twilio's primary announcement — confidence high.** Documented the agent-identity angle (Connected Apps OAuth-for-agents, MCP-native auth, IsAgent/device-fingerprinting). Positioned vs [descope](descope.md)/[workos](workos.md)/[okta](okta.md)/[cyberark](cyberark.md); set hedge_fund_fit low (developer infra, not a CTO buy). status: researched, confidence medium. 4 sources cached.
- [2026-07-27] Re-verified the Twilio acquisition against **primary SEC filings** during the URL-audit sweep. **Both previously recorded dates were correct** — announced 2025-10-30 (Twilio Q3 2025 Form 10-Q: "On October 30, 2025, we entered into a definitive agreement to acquire Stytch, Inc."), closed 2025-11-14 (Twilio FY2025 Form 10-K, Note 11). No date-transposition and no fabricated-close-date bug on this page; the dates were distinct, plausible, and genuinely sourced. **Added the previously-null price: $104.1M cash, $58.5M net of cash acquired**, with the full purchase-price allocation (goodwill $48.5M, identifiable intangibles $11.8M, cash acquired $45.6M) — Twilio's blog called terms undisclosed, but the 10-K discloses them. Noted the analytically important point that $104.1M is **below Stytch's ~$120M in disclosed primary funding** and ~1/10th of its 2021 $1B valuation, i.e. a soft-landing exit, and worked that into the positioning and CTO-lens sections. Confirmed stytch.com is live (200, no redirect), still Stytch-branded, bannering "Stytch has joined Twilio." Rewrote competitive positioning to treat this as a platform-vendor conversation and flagged [descope](descope.md) as the remaining independent comparable. last_verified → 2026-07-27; added frontmatter `sources:` entries. 1 new source cached.
