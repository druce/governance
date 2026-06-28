---
type: vendor
name: LayerX
slug: layerx
categories: [browser-security-extension]
layer: ux
aliases: [LayerX Security]
website: "https://layerxsecurity.com"
founded: 2022
hq: Tel Aviv, Israel
ownership: acquired
ownership_detail: "Akamai Technologies announced intent to acquire for ~$205M cash (2026-05-14); close expected Q3 2026. Independent VC-backed until then."
ownership_confidence: high
funding_total: $45M
last_funding: Series A extension (April 2025), total raised $45M
deployment: [saas, browser-extension, api]
target_customer: enterprise / Fortune 500
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [egress, sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [browser-security, shadow-ai, last-mile-dlp, secure-enterprise-browser]
---

# LayerX

> Agentless browser-security platform delivered as a lightweight extension on the user's existing browser — last-mile DLP, shadow-AI/SaaS control, and access governance without an enterprise browser or full SSE stack. Being acquired by Akamai (announced 2026-05).

**One-liner** — A browser extension that turns Chrome/Edge/Safari/Firefox into an enterprise-controlled endpoint, so security teams can see and govern what employees paste into GenAI tools and SaaS apps.

## What it does

LayerX installs as a lightweight extension on the browsers employees already use. From inside the browser it gets visibility into web sessions, SaaS apps, and AI tools, and enforces last-mile guardrails: blocking or redacting sensitive data pasted into ChatGPT/Copilot, detecting shadow SaaS and shadow AI, stopping malicious or risky extensions, and adding access/identity controls and anti-phishing. The pitch is to get most of the value of a secure enterprise browser or an SSE deployment without forcing users onto a new browser or routing all traffic through a proxy.

## Where it sits in the stack

Primary category: [browser-security-extension](../categories/browser-security-extension.md) (layer: `ux`). It operates at the last mile — the point where a human interacts with web apps and LLMs. In lethal-trifecta terms it mainly addresses **egress** (data leaving to AI/SaaS) and **sensitive-data** exposure (what gets pasted/uploaded); shadow-AI discovery is its headline use case. It lives in the user/endpoint trust zone rather than at a network or model gateway.

## Deployment & architecture

Agentless from the endpoint's perspective: no OS agent, no separate browser — just a browser extension, plus a management console (SaaS). This is its core differentiator versus enterprise-browser vendors (which replace the browser) and SSE/proxy vendors (which reroute traffic). Integrations reported: works across Chrome, Edge, Safari, Firefox; positions against SSE and enterprise-browser stacks. (IdP/SIEM integration details not deeply verified here — see open questions.)

## Positioning & differentiators

Known for the "agentless, last-mile guardrails" angle: cover GenAI data leakage and shadow AI with a low-friction extension instead of a heavier control point. Nearest neighbors:
- [island](island.md) and enterprise browsers — replace the browser entirely; LayerX keeps the user's browser.
- [chrome-enterprise](chrome-enterprise.md) — native browser management/DLP from Google; LayerX is browser-agnostic and AI-risk-focused.
- [menlo-security](menlo-security.md) — remote browser isolation / proxy model; LayerX is extension-based, not isolation.
- [grip-security](grip-security.md) — SaaS/shadow-AI discovery and identity governance, but Grip is identity-centric rather than an in-browser enforcement extension.

## Ownership, funding & M&A

- Founded 2022 in Tel Aviv by Or Eshed (CEO) and David Weisbrot/Vaisbrud (CTO).
- Raised ~$45M total (Series A $26M in May 2024, extended via subsequent rounds to $45M) from Glilot Capital Partners, Dell Technologies Capital, and Jump Capital (led the extension).
- **M&A (verified):** Akamai Technologies announced intent to acquire LayerX for ~$205M cash on 2026-05-14; close expected Q3 2026. LayerX ARR cited at ~$10M; deal expected to dilute Akamai non-GAAP EPS ~$0.12 for FY2026. Confirmed against Akamai's own press release and Israeli tech press. The seed registry carried no M&A flag — this acquisition surfaced during research. Confidence: high (deal announced, not yet closed as of fetch date).

## CTO / hedge-fund lens

Priority: **optional**. This is a last-mile control, not a Day-1 essential for a 50-person fund — but it is one of the lower-friction ways to get shadow-AI/GenAI-egress visibility without standing up an SSE or swapping browsers. For a hedge fund worried about analysts pasting MNPI, positions, or client data into public LLMs, an extension-based guardrail is an easy pilot. Watch the Akamai acquisition: post-close, expect it to be folded into Akamai's Zero Trust / workforce-security line, which changes pricing, packaging, and roadmap. No direct SR 11-7 / model-risk role; this is a data-egress and usage-control tool, not a model-governance tool.

## Competitors / alternatives

[island](island.md) · [chrome-enterprise](chrome-enterprise.md) · [menlo-security](menlo-security.md) · [grip-security](grip-security.md)

## Open questions / to verify

- Exact funding-round chronology ($26M Series A → $37M → $45M) and dates; sources are slightly inconsistent on round labeling.
- Co-founder name spelling: "David Weisbrot" (press) vs "David Vaisbrud" (Akamai release).
- Depth of IdP / SIEM / MCP / DSPM integrations — not verified in this pass.
- Post-acquisition product direction and standalone availability once the Akamai deal closes (Q3 2026).

## Sources

- [Akamai Technologies Announces Intent to Acquire LayerX](https://www.akamai.com/newsroom/press-release/akamai-technologies-announces-intent-to-acquire-layerx-advancing-its-workforce-security-strategy-with-ai-usage-control) — fetched 2026-06-28 — supports: acquirer, ~$205M price, 2026-05-14 announcement, Q3 2026 close, ~$10M ARR, founders; confidence: high (primary).
- [LayerX Security Extends Series A Funding to $37M](https://layerxsecurity.com/blog/layerx-security-extends-series-a-funding-to-37m-to-power-next-gen-enterprise-browser-security-challenges-sse-solutions-and-enterprise-browsers/) — fetched 2026-06-28 — supports: product scope (last-mile DLP, shadow AI, GenAI leakage), browser-extension deployment, investors, positioning vs SSE/enterprise browsers; confidence: med (vendor marketing).
- [Akamai acquires Israeli AI browser security startup LayerX for $205 million (Calcalist)](https://www.calcalistech.com/ctechnews/article/byinuqxkme) — fetched 2026-06-28 — supports: founded 2022, founders, Tel Aviv HQ, $45M total funding, acquisition; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022 (Tel Aviv; Or Eshed & David Weisbrot), ~$45M raised (Glilot, Dell Tech Capital, Jump Capital), agentless browser-extension model for last-mile DLP / shadow-AI control. Verified pending Akamai acquisition (~$205M, announced 2026-05-14, close Q3 2026) — surfaced in research, no prior seed flag; set ownership=acquired, confidence high.
