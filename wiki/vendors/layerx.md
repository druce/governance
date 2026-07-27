---
title: LayerX
type: vendor
name: LayerX
slug: layerx
aka: [LayerX Security, Akamai Workforce Protector]
primary_category: browser-security-extension
also_listed_in: []
website: https://layerxsecurity.com
founded: 2022
hq: Tel Aviv, Israel
ownership_state: acquired-closed
owner: Akamai Technologies
ownership_note: 'Acquired by Akamai Technologies (NASDAQ: AKAM) — announced 2026-05-14, closed 2026-07-02 for ~US$205M, per Akamai''s own completion press release. Price is acquirer-stated and unaudited: no 8-K was filed (below Akamai''s significance threshold) and the deal closed two days after Q2 quarter-end, so the audited purchase-price allocation should first appear in the Q3 2026 10-Q (~Nov 2026). Brand is mid-transition: layerxsecurity.com is still live and LayerX-branded with an acquisition banner, while on akamai.com the product is already "Akamai Workforce Protector (Formerly LayerX)"'
acquisition: {announced: 2026-05-14, closed: 2026-07-02, price: ~US$205M (acquirer-stated; unaudited — no SEC PPA until Q3 2026 10-Q)}
funding_total: $45M
last_funding: Series A extension (April 2025), total raised $45M
market_position: null
deployment_model: [saas]
form_factor: [browser-extension, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / Fortune 500
last_verified: 2026-07-27
verify_after: 2026-11-30
tags: [acquired, akamai, browser-security, shadow-ai, last-mile-dlp, secure-enterprise-browser]
sources:
  - {claim: "Akamai completed the acquisition of LayerX on 2026-07-02; deal valued at approximately US$205M, initially announced 2026-05-14", url: "https://www.akamai.com/newsroom/press-release/akamai-completes-acquisition-of-secure-enterprise-browser-provider-layerx", date: 2026-07-27, confidence: high}
  - {claim: "The LayerX product is sold on akamai.com as 'Akamai Workforce Protector (Formerly LayerX)' — browser extension plus management console, positioned as an interaction-security layer", url: "https://www.akamai.com/products/akamai-workforce-protector", date: 2026-07-27, confidence: high}
  - {claim: "layerxsecurity.com is live (200, no redirect) and still LayerX-branded, carrying the banner 'Akamai acquires LayerX, delivering end-to-end security and real-time AI usage control'", url: "https://layerxsecurity.com/", date: 2026-07-27, confidence: high}
  - {claim: "No Akamai 8-K was filed for the LayerX completion and the Q2 2026 10-Q was not yet filed as of 2026-07-27, so no audited purchase-price allocation exists yet", url: "https://data.sec.gov/submissions/CIK0001086222.json", date: 2026-07-27, confidence: high}
---

# LayerX

> **Researched 2026-06-28; re-verified 2026-07-27.** Agentless browser-security platform delivered as a lightweight extension on the user's existing browser — last-mile DLP, shadow-AI/SaaS control, and access governance without an enterprise browser or full SSE stack. **Acquired by Akamai Technologies (NASDAQ: AKAM) — closed 2026-07-02** for ~US$205M. No longer an independent vendor: on akamai.com the product is already **"Akamai Workforce Protector (Formerly LayerX)"**, though layerxsecurity.com still loads under the LayerX name.

**One-liner** — A browser extension that turns Chrome/Edge/Safari/Firefox into an enterprise-controlled endpoint, so security teams can see and govern what employees paste into GenAI tools and SaaS apps.

## What it does

LayerX installs as a lightweight extension on the browsers employees already use. From inside the browser it gets visibility into web sessions, SaaS apps, and AI tools, and enforces last-mile guardrails: blocking or redacting sensitive data pasted into ChatGPT/Copilot, detecting shadow SaaS and shadow AI, stopping malicious or risky extensions, and adding access/identity controls and anti-phishing. The pitch is to get most of the value of a secure enterprise browser or an SSE deployment without forcing users onto a new browser or routing all traffic through a proxy.

## Where it sits in the stack

Primary category: [browser-security-extension](../categories/browser-security-extension.md) (layer: `ux`). It operates at the last mile — the point where a human interacts with web apps and LLMs. In lethal-trifecta terms it mainly addresses **egress** (data leaving to AI/SaaS) and **sensitive-data** exposure (what gets pasted/uploaded); shadow-AI discovery is its headline use case. It lives in the user/endpoint trust zone rather than at a network or model gateway.

## Deployment & architecture

Agentless from the endpoint's perspective: no OS agent, no separate browser — just a browser extension, plus a management console (SaaS). This is its core differentiator versus enterprise-browser vendors (which replace the browser) and SSE/proxy vendors (which reroute traffic). Integrations reported: works across Chrome, Edge, Safari, Firefox; positions against SSE and enterprise-browser stacks. (IdP/SIEM integration details not deeply verified here — see open questions.)

## Brand status (as of 2026-07-27)

Mid-transition, and the two halves point in different directions — worth stating precisely because it determines what you actually buy and from whom:

- **layerxsecurity.com is live** (200, no redirect), still LayerX-branded, still calling the product the "LayerX Interaction Security Platform." The only Akamai content is a banner: *"Akamai acquires LayerX, delivering end-to-end security and real-time AI usage control."*
- **On akamai.com the successor name is already in use.** The product page is titled **"Akamai Workforce Protector (Formerly LayerX)"**, and a Gartner Peer Insights listing exists under that name.

So unlike several other 2025–26 absorptions in this space where the acquired brand simply persists, Akamai has already picked and shipped a replacement name. Treat "LayerX" as the legacy name and **Akamai Workforce Protector** as what will be on the quote; expect layerxsecurity.com to fold into akamai.com, and the "formerly LayerX" parenthetical to be temporary.

## Positioning & differentiators

Known for the "agentless, last-mile guardrails" angle: cover GenAI data leakage and shadow AI with a low-friction extension instead of a heavier control point. Akamai keeps that framing and pushes it further, marketing the product as an **"interaction security"** layer — governing prompts, responses, agent actions, and data exchanges across AI, SaaS, web, and desktop apps, on managed *and* unmanaged devices — rather than as network access or file control.

The technical differentiation (extension-based, no browser swap, no traffic reroute) survives the deal intact. What does *not* survive is the independent-best-of-breed argument: LayerX now sits inside Akamai's Zero Trust line alongside its segmentation (Guardicore lineage), ZTNA, and DNS-security products, and is sold as the browser-side endpoint of that platform. That puts it in the same 2025–26 platform-absorption wave as [prisma-airs](prisma-airs.md) (Palo Alto), [cisco-ai-defense](cisco-ai-defense.md), [calypsoai](calypsoai.md) (F5), [aim-security](aim-security.md) (Cato), [lakera](lakera.md) (Check Point) and [prompt-security](prompt-security.md) (SentinelOne) — AI-usage control is being bought as a feature of a security platform, not sold as a category. Nearest neighbors:
- [island](island.md) and enterprise browsers — replace the browser entirely; LayerX keeps the user's browser. Island is still independent, which is now also a *neutrality* difference, not just an architectural one.
- [chrome-enterprise](chrome-enterprise.md) — native browser management/DLP from Google; LayerX is browser-agnostic and AI-risk-focused. Both are now platform-owned, so the comparison is Akamai's stack versus Google's rather than startup versus incumbent.
- [menlo-security](menlo-security.md) — remote browser isolation / proxy model; LayerX is extension-based, not isolation. Still independent.
- [grip-security](grip-security.md) — SaaS/shadow-AI discovery and identity governance, but Grip is identity-centric rather than an in-browser enforcement extension. Still independent.

## Ownership, funding & M&A

- Founded 2022 in Tel Aviv by Or Eshed (CEO) and David Weisbrot/Vaisbrud (CTO).
- Raised ~$45M total (Series A $26M in May 2024, extended via subsequent rounds to $45M) from Glilot Capital Partners, Dell Technologies Capital, and Jump Capital (led the extension).
- **M&A (verified, closed):** Akamai Technologies (NASDAQ: AKAM) announced intent to acquire LayerX on **2026-05-14** and **completed the acquisition on 2026-07-02** — Q3 2026 guidance met on the first business days of the quarter. Value ~**US$205M**, per Akamai's own completion press release; the announcement release qualified this as "after giving effect to expected purchase price adjustments." Announcement-era guidance, not repeated at close: LayerX ARR ~$10M at year end, ~$0.12 of FY2026 non-GAAP EPS dilution. The seed registry carried no M&A flag — this acquisition surfaced during research. Confidence: high (acquirer primary source, both ends of the deal).
- **On the price figure:** ~$205M is acquirer-stated and **unaudited**. Akamai filed no 8-K for the completion (a ~$205M deal is below its significant-acquisition threshold), and since the deal closed two days after Q2 quarter-end, the Q2 2026 10-Q can only carry it as a subsequent event. The audited purchase-price allocation — goodwill, intangibles, and the useful lives assigned to the LayerX trademark, which is the tell for how long the brand survives — should first appear in the **Q3 2026 10-Q, expected around November 2026**. That is what `verify_after` is set to.

## CTO / hedge-fund lens

Priority: **optional**. This is a last-mile control, not a Day-1 essential for a 50-person fund — but it is one of the lower-friction ways to get shadow-AI/GenAI-egress visibility without standing up an SSE or swapping browsers. For a hedge fund worried about analysts pasting MNPI, positions, or client data into public LLMs, an extension-based guardrail is still an easy pilot; the technology didn't change on 2026-07-02.

What changed is the commercial picture, and it cuts both ways:

- **You now contract with Akamai, not a Series-A startup.** Ask for the quote under the product's current name (Akamai Workforce Protector) so you're not comparing against stale LayerX pricing, and ask explicitly whether it is still sold standalone or only bundled with Akamai's Zero Trust / ZTNA / segmentation line — a ~$205M tuck-in bought to complete a platform is usually headed for the bundle.
- **Counterparty risk arguably fell.** A $10M-ARR startup selling a browser extension into regulated buyers was a real vendor-viability question; a cash purchase by a profitable NASDAQ company with an existing enterprise-security channel is not. If Akamai is already in your stack (CDN, WAF, ZTNA), procurement and vendor-diligence overhead drops sharply.
- **Diligence artifacts reset.** Any SOC 2 / pen-test / DPA you were handed as LayerX paperwork needs re-requesting under Akamai's entity, and the sub-processor list will change. Same for the "where does my data go" answer — the console is Akamai-operated now.

No direct SR 11-7 / model-risk role; this is a data-egress and usage-control tool, not a model-governance tool.

## Competitors / alternatives

[island](island.md) · [chrome-enterprise](chrome-enterprise.md) · [menlo-security](menlo-security.md) · [grip-security](grip-security.md)

## Open questions / to verify

- Exact funding-round chronology ($26M Series A → $37M → $45M) and dates; sources are slightly inconsistent on round labeling.
- Co-founder name spelling: "David Weisbrot" (press) vs "David Vaisbrud" (Akamai release).
- Depth of IdP / SIEM / MCP / DSPM integrations — not verified in this pass.
- **Standalone availability and pricing under Akamai** — whether Akamai Workforce Protector is still sold on its own or only inside a Zero Trust bundle. Not disclosed in either press release.
- **Audited price and intangible useful lives** — re-check Akamai's Q3 2026 10-Q (~Nov 2026) against the acquirer-stated ~$205M; the trademark's assigned life is the best available signal for how long the LayerX name lasts.
- **Domain/brand endgame** — when layerxsecurity.com redirects to akamai.com, and whether the slug and survey option should move to `akamai-workforce-protector` at that point. Held at `layerx` for now under this sweep's rename rule (see history).

## Sources

- [Akamai Completes Acquisition of Secure Enterprise Browser Provider LayerX](https://www.akamai.com/newsroom/press-release/akamai-completes-acquisition-of-secure-enterprise-browser-provider-layerx) — fetched 2026-07-27 — supports: close date 2026-07-02, ~US$205M value, 2026-05-14 announcement, fit with Akamai's Zero Trust platform (segmentation, ZTNA, DNS security); confidence: high (primary, acquirer).
- [Akamai Workforce Protector (Formerly LayerX) — product page](https://www.akamai.com/products/akamai-workforce-protector) — fetched 2026-07-27 — supports: product rebrand, "interaction security" positioning, capability list (shadow-AI/SaaS discovery, GenAI/web/SaaS DLP, malicious-extension protection, managed + unmanaged devices); confidence: high (primary, but vendor marketing for the claims about efficacy).
- [Akamai EDGAR submissions index (CIK 0001086222)](https://data.sec.gov/submissions/CIK0001086222.json) — checked 2026-07-27 — supports: no 8-K filed for the completion, last 10-Q on file is Q1 2026 (filed 2026-05-08), Q2 2026 10-Q not yet filed — hence no audited purchase-price allocation yet; confidence: high (primary).
- [LayerX homepage](https://layerxsecurity.com/) — checked 2026-07-27 — supports: domain live (200, no redirect), still LayerX-branded, acquisition banner text; confidence: high.
- [Akamai Technologies Announces Intent to Acquire LayerX](https://www.akamai.com/newsroom/press-release/akamai-technologies-announces-intent-to-acquire-layerx-advancing-its-workforce-security-strategy-with-ai-usage-control) — fetched 2026-06-28 — supports: acquirer, ~$205M price, 2026-05-14 announcement, Q3 2026 close, ~$10M ARR, founders; confidence: high (primary).
- [LayerX Security Extends Series A Funding to $37M](https://layerxsecurity.com/blog/layerx-security-extends-series-a-funding-to-37m-to-power-next-gen-enterprise-browser-security-challenges-sse-solutions-and-enterprise-browsers/) — fetched 2026-06-28 — supports: product scope (last-mile DLP, shadow AI, GenAI leakage), browser-extension deployment, investors, positioning vs SSE/enterprise browsers; confidence: med (vendor marketing).
- [Akamai acquires Israeli AI browser security startup LayerX for $205 million (Calcalist)](https://www.calcalistech.com/ctechnews/article/byinuqxkme) — fetched 2026-06-28 — supports: founded 2022, founders, Tel Aviv HQ, $45M total funding, acquisition; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022 (Tel Aviv; Or Eshed & David Weisbrot), ~$45M raised (Glilot, Dell Tech Capital, Jump Capital), agentless browser-extension model for last-mile DLP / shadow-AI control. Verified pending Akamai acquisition (~$205M, announced 2026-05-14, close Q3 2026) — surfaced in research, no prior seed flag; set ownership=acquired, confidence high.
- [2026-07-27] **Akamai acquisition closed 2026-07-02** for ~US$205M, per Akamai's own completion press release — `acquired-pending` → `acquired-closed`, close date and price filled in. Price is acquirer-stated and unaudited: no 8-K was filed (below Akamai's significance threshold) and the close landed two days after Q2 quarter-end, so the audited purchase-price allocation is not expected before the Q3 2026 10-Q (~Nov 2026); `verify_after` set to 2026-11-30 for that. Product is already rebranded **Akamai Workforce Protector (Formerly LayerX)** on akamai.com and positioned as an "interaction security" layer inside Akamai's Zero Trust line, but layerxsecurity.com remains live and LayerX-branded with an acquisition banner — brand recorded as mid-transition, `website` and slug held at LayerX under this sweep's rename rule (rename only once the old brand is actually retiring), with an open question to revisit when the domain redirects. Rewrote positioning (now grouped with the 2025–26 platform-absorption wave), competitor notes (flagged which neighbors are still independent), and the CTO lens (contracting with Akamai, bundle risk, lower counterparty risk, diligence artifacts reset).
