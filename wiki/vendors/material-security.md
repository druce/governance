---
type: vendor
name: Material Security
slug: material-security
categories: [browser-security-extension]
layer: ux
aliases: [Material]
website: "https://material.security"
founded: 2017
hq: Redwood City, California, USA
ownership: independent
ownership_detail: "Independent, VC-backed. Series C May 2022 led by Founders Fund at $1.1B valuation; no M&A found as of 2026-06-28."
ownership_confidence: high
funding_total: ~$166M
last_funding: Series C, $100M, May 2022 ($1.1B valuation)
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [sensitive-data, untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [email-security, cloud-workspace-security, microsoft-365, google-workspace, data-security, posture-management]
---

# Material Security

> Detection-and-response platform for cloud workspaces (Microsoft 365 and Google Workspace) — email security, data security, account/identity protection, and posture management. Primarily an EMAIL/WORKSPACE security company, not a browser extension.

**One-liner** — "Zero Trust" security for your email and cloud workspace: it sits on top of Microsoft 365 / Google Workspace via API to catch malicious email, lock down sensitive content, and contain account takeover.

## What it does

Material Security protects the cloud workspace — primarily the mailbox and the files attached to it. It connects to Microsoft 365 or Google Workspace through provider APIs (no inline mail-flow rerouting, no browser agent) and provides four things: **email security** (detect/remediate phishing and sophisticated email threats that slip past native controls), **data security** (find and protect sensitive content sitting in mailboxes and files — its original "encrypt old sensitive email so a breached inbox isn't a data dump" idea), **identity threat detection** (harden accounts, contain the blast radius of a compromised account), and **posture management** (catch and auto-remediate config drift). It also ships an OAuth Remediation Agent to shut down malicious OAuth apps and surface shadow IT / unsanctioned AI app usage.

## Where it sits in the stack

Tagged here under [browser-security-extension](../categories/browser-security-extension.md) (layer: `ux`) **but this is a category-fit stretch** — Material is email/cloud-workspace security, delivered by API, with no browser extension. In lethal-trifecta terms its strongest legs are **untrusted-input** (malicious inbound email as the attack vector) and **sensitive-data** (protecting content at rest in the workspace). Its shadow-AI relevance is indirect: OAuth/third-party app visibility can surface unsanctioned AI apps connected to the workspace, not in-browser GenAI usage. It lives in the SaaS/workspace trust zone, not the endpoint/browser.

## Deployment & architecture

SaaS control plane with **API-based** integration into Microsoft 365 and Google Workspace; single-tenant architecture per customer. No inline proxy, no MX-record/mail-gateway rerouting, no endpoint agent, and — importantly for this category — **no browser extension**. Integrates at the workspace/identity layer (OAuth app governance, account hardening).

## Positioning & differentiators

Known for the original insight that a breached mailbox is a data-exfiltration goldmine, so it selectively protects/redacts sensitive historical email and content rather than only blocking inbound threats. It competes with cloud email security / ICES vendors (Abnormal Security, Proofpoint, Mimecast) and with Google/Microsoft native controls, more than with browser-security vendors. It is **not** a close neighbor of [island](island.md), [chrome-enterprise](chrome-enterprise.md), [grip-security](grip-security.md), or [menlo-security](menlo-security.md) — those are endpoint/browser controls, whereas Material is a workspace API platform. (Email-security peers are not yet pages in this wiki — see open questions.)

## Ownership, funding & M&A

- Founded 2017 in Redwood City, CA by former Dropbox engineers (CEO Ryan Noon) after the 2016 election email hacks.
- ~$166M raised total. Series C: $100M in May 2022, led by Founders Fund (Trae Stephens), with Andreessen Horowitz, Elad Gil, and individual investors; $1.1B post-money valuation (unicorn).
- **M&A:** none found as of 2026-06-28. Independent and VC-backed. Seed registry carried no M&A flag; research confirmed no acquisition. ownership=independent, confidence high.

## CTO / hedge-fund lens

Priority: **optional** (and arguably mis-filed under browser security — see below). For a hedge fund on Microsoft 365 or Google Workspace, Material is a credible *email/workspace* security layer: it adds detection/response and data protection on top of native Microsoft/Google controls. That's a real Day-2 consideration — but as an *email-security* decision, not a *browser-security* one. If a CTO is shopping the browser-security-extension category (last-mile GenAI/DLP via the browser), Material does not fill that slot; [layerx](layerx.md), [island](island.md), or [chrome-enterprise](chrome-enterprise.md) do. No direct SR 11-7 / model-risk role. Note its customer list skews to tech (OpenAI, Anthropic, Reddit, Figma), not finance — fit for a regulated fund is plausible but unverified.

## Competitors / alternatives

Within its real category (cloud email/workspace security): Abnormal Security, Proofpoint, Mimecast, plus Microsoft/Google native controls (none are wiki pages yet). Within the tagged browser category it is not a true substitute for [layerx](layerx.md) / [island](island.md) / [chrome-enterprise](chrome-enterprise.md).

## Open questions / to verify

- **Category fit:** Material is primarily email/cloud-workspace security with no browser extension. `browser-security-extension` is likely the wrong primary category; an email/workspace-security category would fit better. Kept per instruction; flagged for taxonomy review.
- Any funding after the May 2022 Series C? Nothing found; last verified round is 2022 — confirm there's been no down-round/flat extension since.
- Whether to add email/cloud-workspace-security peers (Abnormal, Proofpoint, Mimecast) as pages so Material can be re-homed.
- Regulated-/financial-sector references (current customer evidence skews to tech companies).

## Sources

- [Material Security — homepage / product](https://material.security/) — fetched 2026-06-28 — supports: cloud-workspace (M365 + Google Workspace) scope, four capability areas, API deployment, no browser extension, customer names; confidence: high (primary).
- [Announcing Our Series C — Material Security](https://material.security/resources/announcing-our-series-c) — fetched 2026-06-28 — supports: $100M Series C, $1.1B valuation, Founders Fund lead, May 2022; confidence: high (primary).
- [Material Security Reaches $1.1 Billion Valuation (BusinessWire)](https://www.businesswire.com/news/home/20220511005584/en/Material-Security-Reaches-1.1-Billion-Valuation-for-%E2%80%98Zero-Trust%E2%80%99-Security-on-Microsoft-and-Google-Email) — fetched 2026-06-28 — supports: founded 2017, Redwood City HQ, ~$166M total, investors, "Zero Trust" email positioning; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2017 (Redwood City; ex-Dropbox, CEO Ryan Noon), ~$166M raised, Series C $100M May 2022 led by Founders Fund at $1.1B valuation, independent (no M&A). Confirmed primary identity is email / cloud-workspace security (M365 + Google Workspace) via API with NO browser extension — flagged browser-security-extension category as a likely mis-fit in Open questions; kept category per instruction.
