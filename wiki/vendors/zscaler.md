---
type: vendor
name: Zscaler
slug: zscaler
categories: [network-security-sase, ai-access-governance]
layer: foundation
aliases: [ZS, Zero Trust Exchange]
website: https://www.zscaler.com
founded: 2007
hq: San Jose, California, USA
ownership: public
ownership_detail: "Public company, NASDAQ: ZS (IPO 2018); confirmed via vendor press releases 2026-06-28"
ownership_confidence: high
funding_total: n/a (public)
last_funding: "IPO March 2018 (NASDAQ: ZS)"
deployment: [saas, inline-proxy, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress, sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [sase, sse, zero-trust, cloud-proxy, shadow-ai, inline-dlp]
---

# Zscaler

> Cloud-delivered security platform (SSE/SASE) that proxies user traffic through its
> Zero Trust Exchange; now extended to discover and govern enterprise AI use.

**One-liner** — Zscaler is the large public SSE/SASE vendor whose cloud proxy already
sits between your users and the internet, and which now uses that position to find
shadow AI, control who can use which AI apps, and block sensitive data going into prompts.

**Categories** — [[network-security-sase]] (primary), [[ai-access-governance]]

## What it does
Zscaler runs a global cloud proxy (the "Zero Trust Exchange") that inspects user and
branch traffic instead of backhauling it to a corporate firewall. Core products are
ZIA (secure web/internet access), ZPA (zero-trust private app access), and a data
protection (DLP/CASB) suite. Because nearly all egress already passes through Zscaler,
it can layer AI controls on top without new inline plumbing: discovering which AI apps
employees use, coaching/allowing/blocking access by user or group, and applying inline
DLP to prompts.

## Where it sits in the stack
Foundation-layer network control under [[network-security-sase]], with an
[[ai-access-governance]] role as a secondary use of the same proxy. On the lethal
trifecta it primarily addresses the **egress** leg (controlling where data can flow,
blocking unsanctioned AI destinations) and the **sensitive-data** leg (inline DLP on
prompts). It is the green/yellow-zone perimeter, not a model-layer guardrail.

## Deployment & architecture
SaaS-delivered cloud proxy; traffic forwarded via agent (Zscaler Client Connector),
GRE/IPsec tunnels, or PAC files. Inline inspection (incl. TLS) is the architecture, plus
out-of-band API scanning for SaaS. AI access security features (per vendor material,
2026): shadow-AI app discovery/classification, user-based allow/block/coach policies,
inline DLP with 100+ dictionaries (PII, PCI, PHI, source code), prompt content
moderation, and optional browser isolation. Integrations with SIEM/SOC, IdP, and major
AI providers. In Jan 2026 Zscaler announced an "AI Security Suite" (AI Asset Management,
Secure Access to AI, Secure AI Infrastructure/Apps incl. red teaming) and the acquisition
of AI-security firm SPLX — both largely vendor-stated and not independently verified here.

## Positioning & differentiators
Known for scale and an installed inline footprint: if a shop already routes egress
through Zscaler, turning on AI discovery/DLP is incremental rather than a new deployment.
Differs from API-first CASB/DSPM tools by being inline-first. Nearest neighbors:
[[netskope]] (closest SSE/SASE competitor, also pushing AI controls), [[palo-alto-networks]]
(Prisma Access / Prisma AIRS), [[cisco]], [[cato-networks]], [[forcepoint]]. Versus
dedicated AI-runtime/guardrail vendors, Zscaler's AI governance is a perimeter overlay,
not deep model-prompt inspection.

## Ownership, funding & M&A
Public company, **NASDAQ: ZS** (IPO March 2018); HQ San Jose, California; founded 2007 by
Jay Chaudhry. Confirmed public status via vendor/IR press releases (as of 2026-06-28).
Continues to acquire (e.g. SPLX, AI security — vendor-announced Jan 2026; not deeply
verified). No ownership ambiguity.

## CTO / hedge-fund lens
Day-1 if you want a single cloud-delivered egress/secure-access layer for a distributed
or remote workforce; the AI-governance features are then a low-friction Day-1.5 add-on for
controlling ChatGPT-style shadow AI and stopping data leakage into prompts. For a small
fund this is a heavyweight enterprise platform — capable but priced and scoped for larger
estates; a 50-person shop may get most of the AI-access value from a lighter SSE or a
browser/DLP point tool. No direct SR 11-7 / model-risk function; it governs *access to* AI,
not model validation.

## Competitors / alternatives
[[netskope]], [[palo-alto-networks]], [[cisco]], [[cato-networks]], [[forcepoint]].

## Open questions / to verify
- Independent (non-marketing) validation of AI-access DLP efficacy and prompt inspection depth.
- Status/terms of the announced SPLX acquisition and how it integrates.
- Exact pricing/packaging of the AI Security Suite vs base ZIA/data-protection licenses.

## Sources
- [Zscaler — AI Access Security (product) + "Secure Enterprise AI Adoption" press](https://www.zscaler.com/products-and-solutions/ai-access-security) — fetched 2026-06-28 — supports: AI access governance/shadow-AI/inline-DLP features, inline proxy deployment, NASDAQ: ZS, San Jose HQ; confidence: med (marketing).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed public (NASDAQ: ZS, IPO 2018), HQ San Jose, founded 2007; documented AI access governance / shadow-AI / inline-DLP positioning; set ownership: public (high). One vendor source cached (marketing).
