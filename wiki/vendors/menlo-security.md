---
type: vendor
name: Menlo Security
slug: menlo-security
categories: [enterprise-browser]
layer: ux
aliases: [Menlo]
website: "https://www.menlosecurity.com"
founded: 2013
hq: Mountain View, California, USA
ownership: independent
ownership_detail: Private, VC/PE-backed (Vista Equity Partners, Neuberger Berman, General Catalyst, Amex Ventures, Ericsson Ventures, HSBC, JPMorgan Chase). Acquired Votiro (CDR/DLP) 2025-02-19.
ownership_confidence: high
funding_total: ~$260M (as of 2026-06-28)
last_funding: Series E, $100M, 2020 (led by Vista Equity Partners)
deployment: [saas, inline-proxy]
target_customer: enterprise / regulated / government
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [untrusted-input, egress, sensitive-data]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [enterprise-browser, remote-browser-isolation, rbi, browser-security, dlp]
---

# Menlo Security

> **Primary category:** [enterprise-browser](../categories/enterprise-browser.md).

**One-liner** — A cloud security company best known for **remote browser isolation** (running web content in the cloud, away from the endpoint) that now packages those controls as a cloud-delivered **secure enterprise browser**.

## What it does
Menlo's original and core technology is **Remote Browser Isolation (RBI)**: web pages and email links execute in a disposable container in Menlo's cloud, and only a safe visual/rendered stream reaches the user's device — so malware, malicious scripts, and drive-by exploits never touch the endpoint. On top of that cloud isolation platform, Menlo added (Feb 2024) a **Secure Enterprise Browser** offering that delivers browser-level governance — DLP, copy/paste and upload controls, access policy, and visibility — without requiring a separate endpoint browser install or agent, because the heavy lifting happens in the cloud. With the 2025 Votiro acquisition it also folds in Content Disarm & Reconstruction (CDR) and file/data security.

## Where it sits in the stack
**UX layer**, in [enterprise-browser](../categories/enterprise-browser.md) (and conceptually overlapping [browser-security-extension](../categories/browser-security-extension.md) / web-isolation tooling). For the lethal trifecta its strongest leg is **untrusted-input**: isolation neutralizes malicious web/email content before it reaches the user (the classic "render it somewhere disposable" defense). With its enterprise-browser DLP it also addresses **egress** (blocking data leaving via the browser) and **sensitive-data** handling (CDR/DLP via Votiro). It sits at the boundary between the open internet (red zone) and the user/endpoint.

## Deployment & architecture
Cloud-delivered SaaS with an **inline/cloud-isolation proxy** model: traffic is routed through Menlo's cloud where browsing is isolated and policy is applied. The enterprise-browser capability is positioned as working **without endpoint software** (it can deliver controls to the browser the user already has, via the cloud), which contrasts with [island](island.md)'s installed-browser approach. Integrations: IdP/SSO, SWG/SASE deployments, SIEM/SOC logging, email security, and (post-Votiro) file/data inspection across browser, email, collaboration, and APIs.

## Positioning & differentiators
Menlo is the established **isolation-first** vendor in this space, with a long enterprise/government track record (it claims 1,000+ enterprises/agencies, 8 of the 10 largest global financial institutions, and many Fortune 500 — vendor-reported). Versus neighbors:
- **[island](island.md)** and **[prisma-access-browser](prisma-access-browser.md)** ship a managed local Chromium browser; Menlo leans on **cloud isolation** and can secure the user's existing browser without a new install.
- **[layerx](layerx.md)** and other [browser-security-extension](../categories/browser-security-extension.md) vendors add controls via extension; Menlo's isolation puts a network/cloud air-gap between user and content.
- **[seraphic](seraphic.md)** (now CrowdStrike) and **[red-access](red-access.md)** are lighter, browser-agnostic plays.
- **[chrome-enterprise](chrome-enterprise.md)** / **[microsoft-edge-business](microsoft-edge-business.md)** are the native, lower-cost baselines.

Differentiation: isolation pedigree (strong against web/email-borne threats and zero-days) plus the data-security depth added by Votiro. Trade-off vs. installed enterprise browsers is granularity of in-browser control and user-experience consistency.

## Ownership, funding & M&A
Independent and private. Founded **2013** (Mountain View, CA) by Amir Ben-Efraim (CEO), Adam Fong, and Ganesh Srinivasan. ~**$260M raised total**; last major round a $100M Series E in 2020 led by **Vista Equity Partners** (other backers: Neuberger Berman, General Catalyst, American Express Ventures, Ericsson Ventures, HSBC, JPMorgan Chase). Vendor said it exceeded $100M ARR (Oct 2024) and expected to be cash-flow positive in 2025.

**M&A:** Menlo **acquired Votiro** (data/file security — CDR and DLP) on **2025-02-19** (terms not disclosed) — confirmed via Menlo's own press release. The brief asked to check a possible **Menlo/Seraphic** deal: that did **not** happen — **Seraphic Security was acquired by CrowdStrike** (~$400M, 2025), a separate transaction. No Menlo/Seraphic relationship found, so no contradiction.

## CTO / hedge-fund lens
Enterprise browser / isolation is **priority: optional**. Menlo fits a fund that wants strong protection against **web- and email-borne threats** (phishing, malicious links, drive-bys) with minimal endpoint footprint, especially if it already runs a SWG/SASE and wants to add isolation without standardizing everyone on a new browser. Its financial-sector and government customer base is a credibility point for regulated buyers. The egress/DLP and CDR pieces help with leakage and malicious-file concerns; the AI-governance angle (blocking/logging paste or upload into public AI tools) is available via the enterprise-browser controls but is not Menlo's headline strength. No direct SR 11-7 / model-risk role — this is threat-isolation and data-control tooling. Main objections: cost/complexity of an isolation layer, and latency/UX of cloud-rendered browsing for some workflows.

## Competitors / alternatives
[island](island.md), [prisma-access-browser](prisma-access-browser.md), [seraphic](seraphic.md), [red-access](red-access.md), [layerx](layerx.md), [chrome-enterprise](chrome-enterprise.md), [microsoft-edge-business](microsoft-edge-business.md).

## Open questions / to verify
- How the cloud-isolation "secure enterprise browser" compares in control granularity to an installed browser like [island](island.md) for real-world DLP.
- Integration depth and roadmap for Votiro CDR/DLP across the platform post-acquisition.
- Current ARR/financials and any IPO timing (CEO has publicly floated IPO ambitions); latency profile for trading/latency-sensitive apps.

## Sources
- [Menlo Security Acquires Votiro to Deliver AI-driven Data Security](https://www.menlosecurity.com/press-releases/menlo-acquires-votiro) — fetched 2026-06-28 — supports: Votiro acquisition 2025-02-19, HQ, CEO, backers; confidence: high (vendor press)
- [Menlo Security Exceeds $100M ARR, Delivers Secure Enterprise Browser Market Leadership](https://www.menlosecurity.com/press-releases/menlo-security-exceeds-100m-arr-delivers-secure-enterprise-browser-market-leadership) — fetched 2026-06-28 — supports: ~$260M total funding, investors, ARR, RBI + secure enterprise browser products, customer base; confidence: high for funding/ownership, medium for vendor-reported metrics

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Menlo Security is an independent, private cloud-security vendor (founded 2013, Mountain View), known for remote browser isolation with a cloud-delivered secure enterprise browser; ~$260M raised, last round $100M Series E (2020, Vista Equity). Confirmed M&A: acquired Votiro (2025-02-19). Checked Menlo/Seraphic per brief — Seraphic was acquired by CrowdStrike, NOT Menlo; no contradiction. Ownership independent, confidence high. hedge_fund_fit medium.
