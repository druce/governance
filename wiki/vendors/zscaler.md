---
title: Zscaler
type: vendor
name: Zscaler
slug: zscaler
aka: [ZS, Zero Trust Exchange]
primary_category: network-security-sase
also_listed_in: [ai-access-governance, dlp, ai-red-teaming, ai-runtime-security]
website: https://www.zscaler.com
founded: 2007
hq: San Jose, California, USA
ownership_state: public
owner: null
ownership_note: 'Public company, NASDAQ: ZS (IPO 2018); confirmed via vendor press releases 2026-06-28'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (public)
last_funding: 'IPO March 2018 (NASDAQ: ZS)'
market_position: {dlp: platform-module, ai-red-teaming: platform-module, ai-runtime-security: platform-module}
deployment_model: [saas]
form_factor: [inline-proxy, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-10-23
verify_after: null
tags: [sase, sse, zero-trust, cloud-proxy, shadow-ai, inline-dlp, mdr, red-canary, splx, ai-guard]
sources:
  - {claim: "FY2026 10-K Note 6: Red Canary acquired 2025-08-01 for $651.4M cash (+$20.2M restricted stock); SPLX 2025-10-31 $40.6M cash; SquareX 2026-02-05 $112.8M cash; Symmetry Systems 2026-05-27 $152.9M cash (+$16.9M restricted stock)", url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368326000157/zs-20260731.htm", date: 2026-10-23, confidence: high}
  - {claim: "FY2026 10-K business section: DLP across web, endpoint, email and AI; Secure AI Apps continuously red teams AI apps and guards against prompt injection at runtime; MDR service and Agentic SOC", url: "https://www.sec.gov/Archives/edgar/data/1713683/000171368326000157/zs-20260731.htm", date: 2026-10-23, confidence: high}
  - {claim: "Definitive agreement to acquire Red Canary (MDR) announced 2025-05-27, expected close August 2025", url: "https://www.zscaler.com/press/zscaler-accelerate-innovation-ai-powered-security-operations-acquisition-red-canary", date: 2026-10-23, confidence: high}
  - {claim: "Red Canary acquisition completed 2025-08-01; initially a separate business unit", url: "https://www.zscaler.com/press/zscaler-completes-acquisition-red-canary-accelerate-innovations-agentic-ai-driven-security", date: 2026-10-23, confidence: high}
  - {claim: "Zscaler AI Guard is an API guardrail (pre-/post-call prompt and response scanning by policy ID) integrated by LiteLLM, Portkey and TrueFoundry", url: "https://docs.litellm.ai/docs/proxy/guardrails/zscaler_ai_guard", date: 2026-10-23, confidence: medium}
---

# Zscaler

> Cloud-delivered security platform (SSE/SASE) that proxies user traffic through its
> Zero Trust Exchange; now extended to discover and govern enterprise AI use.

**One-liner** — Zscaler is the large public SSE/SASE vendor whose cloud proxy already
sits between your users and the internet, and which now uses that position to find
shadow AI, control who can use which AI apps, and block sensitive data going into prompts.

**Categories** — [network-security-sase](../categories/network-security-sase.md) (primary), [ai-access-governance](../categories/ai-access-governance.md)

## What it does
Zscaler runs a global cloud proxy (the "Zero Trust Exchange") that inspects user and
branch traffic instead of backhauling it to a corporate firewall. Core products are
ZIA (secure web/internet access), ZPA (zero-trust private app access), and a data
protection (DLP/CASB) suite. Because nearly all egress already passes through Zscaler,
it can layer AI controls on top without new inline plumbing: discovering which AI apps
employees use, coaching/allowing/blocking access by user or group, and applying inline
DLP to prompts.

## Where it sits in the stack
Foundation-layer network control under [network-security-sase](../categories/network-security-sase.md), with an
[ai-access-governance](../categories/ai-access-governance.md) role as a secondary use of the same proxy. It primarily
controls outbound data flows (governing where data can go, blocking unsanctioned AI
destinations) and prevents sensitive-data leakage (inline DLP on prompts). It is the
green/yellow-zone perimeter, not a model-layer guardrail.

## Deployment & architecture
SaaS-delivered cloud proxy; traffic forwarded via agent (Zscaler Client Connector),
GRE/IPsec tunnels, or PAC files. Inline inspection (incl. TLS) is the architecture, plus
out-of-band API scanning for SaaS. AI access security features (per vendor material,
2026): shadow-AI app discovery/classification, user-based allow/block/coach policies,
inline DLP with 100+ dictionaries (PII, PCI, PHI, source code), prompt content
moderation, and optional browser isolation. Integrations with SIEM/SOC, IdP, and major
AI providers. In Jan 2026 Zscaler announced an "AI Security Suite" (AI Asset Management,
Secure Access to AI, Secure AI Infrastructure/Apps incl. red teaming). The SPLX
acquisition that feeds it had closed earlier, on 2025-10-31 (see Ownership below;
corrected 2026-10-23 from an earlier "announced Jan 2026" reading).

## Cross-category roles (added 2026-10-23)
Survey respondents placed Zscaler in three more categories. Each is supported by Zscaler's
FY2026 Form 10-K (filed 2026-09-03):
- **[dlp](../categories/dlp.md).** Zscaler's Data Loss Prevention "enables enterprises to
  alert on and/or block the transmission or sharing of sensitive data" across "web DLP,
  endpoint DLP, email DLP and DLP for AI systems". It also blocks USB/print on endpoints, and
  "DLP policies also protect interactions with AI applications, safeguarding user prompts."
  Inline DLP on the proxy is the core of it. Endpoint and email DLP are later additions. For
  a Zscaler shop it is often the default DLP. Classification depth, EDM and case workflow
  against dedicated DLP vendors were not evaluated.
- **[ai-red-teaming](../categories/ai-red-teaming.md)** and **[ai-runtime-security](../categories/ai-runtime-security.md).**
  "Secure AI Apps and Infrastructure ... continuously red teams AI applications and models
  throughout the development pipeline" and "at runtime ... guards AI applications and models
  against prompt injection, data leakage, abuse". The red-teaming engine comes from
  [splxai](splxai.md). **Zscaler AI Guard** (the product respondents wrote in under "AI
  Red-Teaming / Guardrails") is the runtime piece. It is an API guardrail that scans
  prompts before the model call and responses after it, against a policy ID. Third-party AI
  gateways (LiteLLM, Portkey, TrueFoundry) integrate it as a guardrail provider. The same
  "AI Guard" brand also covers user-side AI access control ("AI Guard for Users", see
  [ai-access-governance](../categories/ai-access-governance.md)), so the naming is ambiguous.
  Ask which AI Guard SKU is being quoted. Zscaler is a platform module in both categories,
  not a specialist.
- **Security operations: Red Canary MDR.** Zscaler now sells a **Managed Detection and
  Response** service and an **Agentic SOC** product (10-K) built on the Red Canary
  acquisition. This makes Zscaler an MDR provider. Not cross-listed: there is no MDR
  category, and the Agentic SOC product was not researched against
  [ai-soc-analysts](../categories/ai-soc-analysts.md) peers this pass.

## Positioning & differentiators
Known for scale and an installed inline footprint: if a shop already routes egress
through Zscaler, turning on AI discovery/DLP is incremental rather than a new deployment.
Differs from API-first CASB/DSPM tools by being inline-first. Nearest neighbors:
[netskope](netskope.md) (closest SSE/SASE competitor, also pushing AI controls), [palo-alto-networks](palo-alto-networks.md)
(Prisma Access / Prisma AIRS), [cisco](cisco.md), [cato-networks](cato-networks.md), [forcepoint](forcepoint.md). Versus
dedicated AI-runtime/guardrail vendors, Zscaler's AI governance is a perimeter overlay,
not deep model-prompt inspection.

## Ownership, funding & M&A
Public company, **NASDAQ: ZS** (IPO March 2018); HQ San Jose, California; founded 2007 by
Jay Chaudhry. Confirmed public status via vendor/IR press releases (as of 2026-06-28).
No ownership ambiguity. **Acquisition ledger** (Zscaler FY2026 Form 10-K, Note 6, filed
2026-09-03):
- **Red Canary** (MDR): definitive agreement announced **2025-05-27**, **closed 2025-08-01**
  for **$651.4M cash** plus $20.2M restricted stock. Trade press reported ~$675M at signing,
  which matches the headline figure before adjustments. Red Canary initially runs as a
  separate business unit ("Red Canary, a Zscaler company"). It is the Red Canary that
  survey respondents wrote in under SIEM.
- **[splxai](splxai.md)** (AI red teaming): closed **2025-10-31**, **$40.6M cash** plus $16.6M
  restricted stock, publicly announced 2025-11-03.
- **SquareX** (browser security): closed **2026-02-05**, **$112.8M cash** plus $37.4M
  restricted stock.
- **[symmetry-systems](symmetry-systems.md)** (DSPM): the 10-K states Zscaler "acquired all
  outstanding equity" on **2026-05-27** for **$152.9M cash** plus $16.9M restricted stock.
  So the deal **has closed**. The symmetry-systems page (last verified 2026-07-27) still
  shows it as pending and needs updating.

## CTO / hedge-fund lens
Day-1 if you want a single cloud-delivered egress/secure-access layer for a distributed
or remote workforce; the AI-governance features are then a low-friction Day-1.5 add-on for
controlling ChatGPT-style shadow AI and stopping data leakage into prompts. For a small
fund this is a heavyweight enterprise platform — capable but priced and scoped for larger
estates; a 50-person shop may get most of the AI-access value from a lighter SSE or a
browser/DLP point tool. No direct SR 11-7 / model-risk function; it governs *access to* AI,
not model validation.

## Competitors / alternatives
[netskope](netskope.md), [palo-alto-networks](palo-alto-networks.md), [cisco](cisco.md), [cato-networks](cato-networks.md), [forcepoint](forcepoint.md).

## Open questions / to verify
- Independent (non-marketing) validation of AI-access DLP efficacy and prompt inspection depth.
- How SPLX (red teaming) and AI Guard (runtime) are packaged and priced together, and which "AI Guard" SKU covers what.
- Whether Red Canary MDR stays a separate business unit or becomes "Zscaler MDR". Are non-Zscaler customers still supported?
- Depth of Zscaler endpoint and email DLP vs. its inline proxy DLP.
- Exact pricing/packaging of the AI Security Suite vs base ZIA/data-protection licenses.

## Sources
- [Zscaler — AI Access Security (product) + "Secure Enterprise AI Adoption" press](https://www.zscaler.com/products-and-solutions/ai-access-security) — fetched 2026-06-28 — supports: AI access governance/shadow-AI/inline-DLP features, inline proxy deployment, NASDAQ: ZS, San Jose HQ; confidence: med (marketing).

- [Zscaler Form 10-K, FY ended 2026-07-31 (filed 2026-09-03)](https://www.sec.gov/Archives/edgar/data/1713683/000171368326000157/zs-20260731.htm) — fetched 2026-10-23 — supports: Red Canary/SPLX/SquareX/Symmetry close dates and consideration; DLP, Secure AI Apps (red teaming + runtime guarding), MDR and Agentic SOC product descriptions; confidence: high. Cached: `raw/sources/2026-10-23--zscaler--fy2026-10k-acquisitions-and-products.md`
- [Zscaler to acquire Red Canary (2025-05-27)](https://www.zscaler.com/press/zscaler-accelerate-innovation-ai-powered-security-operations-acquisition-red-canary) and [Zscaler completes Red Canary acquisition (2025-08-01)](https://www.zscaler.com/press/zscaler-completes-acquisition-red-canary-accelerate-innovations-agentic-ai-driven-security) — fetched 2026-10-23 — supports: announced/closed dates, MDR description, separate business unit; confidence: high. Cached: `raw/sources/2026-10-23--zscaler--red-canary-announce-and-close.md`
- [LiteLLM docs — Zscaler AI Guard guardrail](https://docs.litellm.ai/docs/proxy/guardrails/zscaler_ai_guard) and [Zscaler AI Guard product page](https://www.zscaler.com/products-and-solutions/ai-guardrails) — fetched 2026-10-23 — supports: AI Guard as API guardrail (pre/post call), "AI Guard for Users/Apps" naming; confidence: medium. Cached: `raw/sources/2026-10-23--zscaler--ai-guard-product-and-integrations.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed public (NASDAQ: ZS, IPO 2018), HQ San Jose, founded 2007; documented AI access governance / shadow-AI / inline-DLP positioning; set ownership: public (high). One vendor source cached (marketing).
- [2026-10-23] Cross-listed in dlp, ai-red-teaming and ai-runtime-security from Zscaler's FY2026 10-K product descriptions plus AI Guard integration docs, after Oct-2026 CTO survey write-ins ("Zscaler" under DLP; "Zscaler AI Guard" under AI Red-Teaming/Guardrails). Verified **Red Canary** acquisition (announced 2025-05-27, closed 2025-08-01, $651.4M cash). Corrected the SPLX timing (closed 2025-10-31, not announced Jan 2026). Added SquareX (closed 2026-02-05) and found that **Symmetry Systems closed 2026-05-27** per the 10-K, so the symmetry-systems page is stale. Set market_position labels. Not cross-listed to an MDR/SOC category (none exists for MDR, and Agentic SOC was not researched).
