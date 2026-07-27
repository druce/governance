---
title: Prisma Browser (Palo Alto/Talon)
type: vendor
name: Prisma Browser (Palo Alto/Talon)
slug: prisma-access-browser
aka: [Prisma Access Browser, Talon, Talon Cyber Security, Talon Enterprise Browser]
primary_category: enterprise-browser
also_listed_in: []
website: https://www.paloaltonetworks.com/sase/prisma-browser
founded: 2021
hq: 'Santa Clara, California, USA (Palo Alto Networks); Talon origin: Tel Aviv, Israel'
ownership_state: acquired-closed
owner: Palo Alto Networks
ownership_note: Former Talon Cyber Security, acquired by Palo Alto Networks (closed 2023-12-28, reported ~$625M); rebranded Prisma Access Browser within the Prisma SASE portfolio.
acquisition: {announced: 2023-12-28, closed: 2023-12-28, price: null}
funding_total: n/a (PANW product; Talon raised ~$143M pre-acquisition)
last_funding: acquired by Palo Alto Networks 2023-12-28
market_position: null
deployment_model: [saas]
form_factor: [agent, browser-extension]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [enterprise-browser, sase, talon, palo-alto, byod]
---

# Prisma Browser (Palo Alto/Talon)

> Primary category: [enterprise-browser](../categories/enterprise-browser.md). Palo Alto Networks' Chromium-based secure enterprise browser, formerly Talon. Marketed as **Prisma Browser** as of 2026-07-27 (previously **Prisma Access Browser**; the longer name still appears in PANW datasheets).

**One-liner** — A managed, Chromium-based enterprise browser (the former Talon) that delivers security controls — DLP, isolation, last-mile inspection — at the browser layer, especially for unmanaged/BYOD and contractor devices, integrated into Palo Alto Networks' Prisma SASE.

**What it does** — Prisma Browser turns the browser into a control point: it enforces data-loss controls (copy/paste, download, screenshot, watermarking), protects against phishing, web-based attacks and malicious extensions, and gives security teams visibility into web/SaaS usage without needing to manage the underlying device. For AI specifically, browser-layer controls are a pragmatic way to govern shadow-AI use (paste limits into chatbots, blocking risky GenAI sites) on devices the org doesn't own.

**Where it sits in the stack** — UX layer, [enterprise-browser](../categories/enterprise-browser.md). It addresses the **sensitive-data** leg (DLP at the point of use) and **egress** leg (what data can leave into web apps / GenAI tools) of the lethal trifecta. Complements [network-security-sase](../categories/network-security-sase.md) (the same Prisma Access fabric) and overlaps with [browser-security-extension](../categories/browser-security-extension.md) approaches.

**Deployment & architecture** — SaaS-managed Chromium browser installed on managed and unmanaged endpoints; part of the Prisma SASE portfolio so policy and visibility flow into the broader PANW console. Was offered complimentary to qualified Prisma SASE customers at acquisition time. As of 2026-07-27 PANW markets three form factors — the dedicated desktop browser, an extension for existing consumer browsers, and a mobile app — which narrows the gap with the [browser-security-extension](../categories/browser-security-extension.md) approach.

**Positioning & differentiators** — Palo Alto's answer to the enterprise-browser category, leaning on SASE integration as the differentiator (consistent policy across network and browser). Nearest neighbors: [island](island.md) (the category pioneer), [menlo-security](menlo-security.md), [seraphic](seraphic.md), [red-access](red-access.md), plus the platform browsers [chrome-enterprise](chrome-enterprise.md) and [microsoft-edge-business](microsoft-edge-business.md); lighter-weight alternatives are [browser-security-extension](../categories/browser-security-extension.md) vendors like [layerx](layerx.md) and [material-security](material-security.md).

**Ownership, funding & M&A** — **Former Talon Cyber Security** (founded 2021, Tel Aviv; raised ~$143M). **Acquired by [palo-alto-networks](palo-alto-networks.md) — VERIFIED:** intent announced Nov 2023, acquisition **closed 2023-12-28** (reported ~$625M); rebranded Prisma Access Browser, since shortened to Prisma Browser. Confirmed against PANW's own closing press release. The seed flag "former Talon (PANW)" is **confirmed.** Corrected the stub's `ownership: independent` to `subsidiary`.

**CTO / hedge-fund lens** — Optional in the taxonomy, but a strong fit for funds with significant contractor/BYOD or third-party-manager access who need DLP and GenAI controls without full MDM. If you're already a Prisma SASE customer the marginal cost is low. Standalone, weigh against [island](island.md) and against just deploying a [browser-security-extension](../categories/browser-security-extension.md) on existing Chrome.

**Competitors / alternatives** — [island](island.md), [menlo-security](menlo-security.md), [seraphic](seraphic.md), [red-access](red-access.md), [chrome-enterprise](chrome-enterprise.md), [microsoft-edge-business](microsoft-edge-business.md), [layerx](layerx.md).

**Open questions / to verify**
- Exact reported acquisition price (~$625M is press-reported, not PANW-disclosed).
- Current feature parity / GenAI-specific controls vs. dedicated [ai-access-governance](../categories/ai-access-governance.md) tools.
- **Slug flag (not acted on):** the page slug remains `prisma-access-browser` while PANW's marketing name is now `Prisma Browser`. Left as-is to avoid breaking inbound links and the survey-v2.csv wiki URL; revisit if "Prisma Access Browser" disappears from PANW collateral entirely.

**Sources**
- [PANW Closes Talon Cyber Security Acquisition](https://www.paloaltonetworks.com/company/press/2023/palo-alto-networks--closes-talon-cyber-security-acquisition-and-will-offer-complimentary-enterprise-browser-to-qualified-sase-ai-customers) — fetched 2026-06-28 — supports: Talon -> Prisma Access Browser, close 2023-12-28, capabilities; confidence: high
- [Secure Browser | Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser) — fetched 2026-07-27 — supports: current product name "Prisma Browser", live product URL, three form factors (desktop browser, extension, mobile app); confidence: high (vendor marketing)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed flag "former Talon (PANW)" — Talon Cyber Security acquired by Palo Alto Networks, closed 2023-12-28 (reported ~$625M), rebranded Prisma Access Browser, against PANW closing press release. Established Talon founded 2021 (Tel Aviv). Corrected ownership independent->subsidiary, confidence low->high.
- [2026-07-27] URL fix: `paloaltonetworks.com/sase/access-browser` returns hard 404; live page is `paloaltonetworks.com/sase/prisma-browser` (HTTP 200). **Naming simplification, not a rebrand or change of owner** — same company, same ex-Talon product lineage, PANW now markets it as "Prisma Browser" (the longer "Prisma Access Browser" persists in datasheets, kept in `aka`). Updated title/name, website, `form_factor: [agent, browser-extension]` (PANW now ships desktop browser + extension + mobile app). Slug left unchanged; flagged in open questions.
