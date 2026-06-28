---
title: Netskope
type: vendor
name: Netskope
slug: netskope
categories: [network-security-sase, dlp, dspm, ai-access-governance]
layer: foundation
aliases: [NTSK, Netskope One]
website: "https://www.netskope.com"
founded: 2012
hq: Santa Clara, California, USA
ownership: public
ownership_detail: "IPO 2025-09-18, NASDAQ: NTSK; priced $19/share, raised ~$908M, ~$8.6B debut market cap. Verified 2026-06-28"
ownership_confidence: high
funding_total: "~$908M IPO proceeds (Sep 2025); previously VC-backed, ~$7.5B private valuation (2021)"
last_funding: "IPO September 2025 (NASDAQ: NTSK)"
deployment: [saas, inline-proxy, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress, sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [sase, sse, casb, dlp, dspm, shadow-ai, inline-proxy]
---

# Netskope

> Cloud-native SSE/SASE platform (Netskope One) built around inline CASB/DLP, now
> positioned as "AI-era" security with shadow-AI discovery and prompt data protection.

**One-liner** — Netskope is the SSE/SASE vendor whose roots are in inline CASB and
data-loss prevention, giving it strong visibility into cloud and AI app usage and the
sensitive data flowing into them; it IPO'd on Nasdaq in September 2025.

**Categories** — [network-security-sase](../categories/network-security-sase.md) (primary), [dlp](../categories/dlp.md), [dspm](../categories/dspm.md), [ai-access-governance](../categories/ai-access-governance.md)

## What it does
Netskope One is a unified, cloud-delivered platform combining secure web gateway,
CASB (inline + API), DLP, ZTNA private access, and data security posture features. Its
historical strength is granular understanding of cloud apps and the data moving through
them, which it extends to AI: discovering shadow AI apps, applying allow/block/coach
policies per user, and running inline DLP on prompts to stop sensitive data leaving in
ChatGPT-style interactions. It markets DSPM-style data discovery/classification alongside.

## Where it sits in the stack
Foundation-layer [network-security-sase](../categories/network-security-sase.md), with [dlp](../categories/dlp.md), [dspm](../categories/dspm.md), and
[ai-access-governance](../categories/ai-access-governance.md) roles served from the same platform. On the lethal trifecta it
covers the **egress** leg (where data can flow / blocking unsanctioned AI) and the
**sensitive-data** leg (inline + API DLP, data classification). Perimeter/data-control,
not a model-prompt guardrail.

## Deployment & architecture
SaaS cloud proxy with inline (steering via client agent, tunnels, reverse proxy) plus
out-of-band API scanning of sanctioned SaaS. Known for deep app/instance awareness
("cloud confidence index") and inline DLP. AI controls (vendor-stated): shadow-AI app
discovery, user/group access policies, prompt DLP, plus DSPM data classification.
Integrations: IdP/SSO, SIEM/SOC, and SaaS APIs.

## Positioning & differentiators
Closest peer to [zscaler](zscaler.md); Netskope is generally seen as more CASB/DLP/data-centric
(its origin), Zscaler as more secure-web-gateway/proxy-scale-centric — though both now
converge on full SSE/SASE plus AI access. Differs from pure [dspm](../categories/dspm.md) tools by bundling
data posture into an inline enforcement platform. Other neighbors: [palo-alto-networks](palo-alto-networks.md),
[cisco](cisco.md), [cato-networks](cato-networks.md), [forcepoint](forcepoint.md). Against dedicated AI-runtime guardrail
vendors, its AI governance is access/data-flow control, not deep prompt-injection defense.

## Ownership, funding & M&A
**Public company, NASDAQ: NTSK.** IPO **September 18, 2025**: priced at $19.00/share
(top of range), ~47.8M shares, raising ~$908M; opened at $23 and debuted around an
$8.6–8.8B market cap. Founded 2012, Santa Clara, CA. Previously venture-backed (private
valuation ~$7.5B in 2021). IPO disclosures showed ~$707M ARR (July 2025) and continuing
net losses (~$170M over six months). IPO verified against IPO-tracker and press sources
2026-06-28. (The seed had ownership: independent / no M&A flag — updated to public.)

## CTO / hedge-fund lens
Day-1 if you want an SSE/SASE layer with especially strong CASB/DLP and data-classification
for controlling cloud and AI app usage; the data-centric heritage makes it attractive where
preventing sensitive data egress (into AI prompts, unsanctioned SaaS) is the priority. Like
[zscaler](zscaler.md), it's an enterprise-scale platform — powerful but heavier than a 50-person fund
typically needs; smaller shops may prefer a lighter SSE plus a focused DLP/browser control.
No SR 11-7 / model-risk validation role; governs access to and data flow around AI.

## Competitors / alternatives
[zscaler](zscaler.md), [palo-alto-networks](palo-alto-networks.md), [cisco](cisco.md), [cato-networks](cato-networks.md), [forcepoint](forcepoint.md).

## Open questions / to verify
- Independent benchmarking of AI-prompt DLP and DSPM classification accuracy.
- Post-IPO financial trajectory / path to profitability (as of mid-2026).
- Depth of DSPM vs dedicated [dspm](../categories/dspm.md) specialists.

## Sources
- [Netskope prices IPO at $19 (NTSK) — IPOScoop](https://www.iposcoop.com/the-ipo-buzz-netskope-ntsk-prices-ipo-at-19-top-of-range/) — fetched 2026-06-28 — supports: IPO date/price/shares/raise/ticker NTSK; confidence: high.
- [Netskope IPO debut — CNBC](https://www.cnbc.com/2025/09/18/netskope-ipo-stock-nasdaq-ntsk.html) — fetched 2026-06-28 (search snippet) — supports: ~$8.6B market cap, founded 2012, Santa Clara HQ, Netskope One platform; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; VERIFIED Sept 2025 IPO (NASDAQ: NTSK, $19/share, ~$908M raised, ~$8.6B debut); set ownership: public (high); founded 2012, Santa Clara; documented CASB/DLP/DSPM/AI-access positioning. Source cached.
