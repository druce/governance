---
type: vendor
name: Grip Security
slug: grip-security
categories: [sspm, browser-security-extension, ai-access-governance]
layer: foundation
aliases: []
website: "https://www.grip.security"
founded: 2021
hq: Tel Aviv, Israel (US office Boston, MA)
ownership: independent
ownership_detail: VC-backed independent; no acquisition found as of 2026-06-28.
ownership_confidence: medium
funding_total: ~$76M (per aggregators)
last_funding: Series B $41M, led by Third Point Ventures (with YL Ventures, Intel Capital, The Syndicate Group)
deployment: [saas, api, browser]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sspm, shadow-ai, identity, saas-security]
---

# Grip Security

> Identity-centric SaaS security: discovers every SaaS and AI app your people actually use (incl. shadow IT / shadow AI), scores the risk, and remediates at the identity layer — with a browser extension to extend control to the last mile.

**One-liner** — An identity-first SaaS Security Posture Management (SSPM) platform that finds all the SaaS and AI apps employees sign up for and helps you govern access and clean up the sprawl.

## What it does

Grip discovers the full inventory of SaaS and AI applications in use across an organization — including unsanctioned "shadow SaaS" and embedded/standalone "shadow AI" tools — by analyzing identity and authentication signals rather than only scanning configurations of a few known apps. It then evaluates each app's risk, surfaces misconfigurations in sanctioned apps, and drives remediation through automated workflows: revoking risky OAuth grants, rotating passwords, and offboarding shadow apps when users leave. Grip pitches this as moving past "posture visibility" into "governance" — i.e., enforcing controls, not just reporting drift (vendor framing; marketing).

The job for a buyer: get an accurate, continuously updated map of every SaaS/AI app touching corporate identities and data, and a way to act on the risky ones.

## Where it sits in the stack

Primary category [sspm](../categories/sspm.md); also [browser-security-extension](../categories/browser-security-extension.md) (its endpoint/browser agent extends discovery and control to the user) and [ai-access-governance](../categories/ai-access-governance.md) (shadow-AI discovery and OAuth governance). Layer: foundation.

Lethal-trifecta role: mainly **sensitive-data** and **egress** — it limits which third-party SaaS/AI apps can reach corporate data and where OAuth-granted access can send it. It is not an inline prompt/content firewall; it governs the access plane, not model I/O.

## Deployment & architecture

SaaS control plane fed by API integrations to IdP (SSO/OAuth logs), email, and SaaS apps, plus an optional **browser extension** that observes and controls app usage at the user. Agentless on the SaaS side; the browser component is the endpoint piece. Integrates with identity providers and security tooling for enforcement and offboarding workflows.

## Positioning & differentiators

Known for **identity-based discovery** — using authentication/identity events to find apps that config-scanning SSPMs miss, especially long-tail shadow SaaS and shadow AI. Grip explicitly contrasts itself with config-posture-centric peers like [appomni](appomni.md) (Grip marketing: "Posture identifies risk. Governance controls it"). Versus [nudge-security](nudge-security.md) (also OAuth/identity-driven discovery and offboarding) the lines blur; versus [valence-security](valence-security.md) and [wing-security](wing-security.md) it leans more on identity signals and the browser last mile. Differentiator claims are vendor marketing pending independent validation.

## Ownership, funding & M&A

Independent, VC-backed. Founded 2021; HQ Tel Aviv with a Boston, MA US office. Total funding ~$76M per aggregators; most recent disclosed round a $41M Series B led by Third Point Ventures (with YL Ventures, Intel Capital, The Syndicate Group). No acquisition found as of 2026-06-28. CEO: Lior Yaari. Funding/founding figures are from aggregators (medium confidence); HQ confirmed via Grip's own press release.

## CTO / hedge-fund lens

**Day-2.** SSPM secures SaaS apps a fund already runs; you reach for it once you have meaningful SaaS sprawl and an SSO estate to instrument. The increasingly compelling reason for a fund to look now is **shadow-AI discovery**: finding which AI tools staff have connected to email, file stores, and code, and revoking risky OAuth scopes. No direct SR 11-7 / model-risk role. Fit is **medium** — valuable for a 100+ person shop with broad SaaS use; lighter funds may get most of the benefit from their IdP plus a narrower shadow-AI tool. The browser extension is a deployment consideration (endpoint rollout).

## Competitors / alternatives

[appomni](appomni.md), [obsidian-security](obsidian-security.md), [valence-security](valence-security.md), [wing-security](wing-security.md), [docontrol](docontrol.md), [reco](reco.md), [nudge-security](nudge-security.md).

## Open questions / to verify

- Exact funding history (seed/Series A amounts/dates) and current total — aggregator-sourced.
- Depth/maturity of the browser extension vs. core API discovery.
- Independent validation of identity-discovery coverage claims vs. config-based SSPMs.

## Sources

- [Grip Security Launches Industry's Only Identity-Centric SSPM (press release)](https://www.grip.security/press-release/grip-security-launches-saas-security-posture-management-sspm-solution) — fetched 2026-06-28 — supports: SSPM capabilities, identity-centric positioning, HQ Boston+Tel Aviv, launch Feb 2025; confidence: med (vendor marketing).
- [Grip Security — Crunchbase / StartupHub aggregator profile](https://www.crunchbase.com/organization/grip-security) — fetched 2026-06-28 — supports: founded 2021, ~$76M total, $41M Series B (Third Point Ventures); confidence: med (aggregator).
- [Grip vs AppOmni (vendor page)](https://www.grip.security/grip-vs-appomni) — fetched 2026-06-28 — supports: identity-discovery and shadow-AI positioning vs config-posture peers; confidence: low (vendor marketing).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (Tel Aviv, founded 2021, ~$76M total, $41M Series B led by Third Point Ventures), identity-centric SSPM + browser extension + shadow-AI discovery; no acquisition found. Set ownership independent (medium), hedge_fund_fit medium, status researched.
