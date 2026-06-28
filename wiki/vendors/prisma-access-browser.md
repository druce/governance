---
type: vendor
name: Prisma Access Browser (Palo Alto/Talon)
slug: prisma-access-browser
categories: [enterprise-browser]
layer: ux
aliases: [Talon, Talon Cyber Security, Talon Enterprise Browser]
website: https://www.paloaltonetworks.com/sase/access-browser
founded: 2021
hq: Santa Clara, California, USA (Palo Alto Networks); Talon origin: Tel Aviv, Israel
ownership: subsidiary
ownership_detail: "Former Talon Cyber Security, acquired by Palo Alto Networks (closed 2023-12-28, reported ~$625M); rebranded Prisma Access Browser within the Prisma SASE portfolio."
ownership_confidence: high
funding_total: n/a (PANW product; Talon raised ~$143M pre-acquisition)
last_funding: acquired by Palo Alto Networks 2023-12-28
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [enterprise-browser, sase, talon, palo-alto, byod]
---

# Prisma Access Browser (Palo Alto/Talon)

> Primary category: [[enterprise-browser]]. Palo Alto Networks' Chromium-based secure enterprise browser, formerly Talon.

**One-liner** — A managed, Chromium-based enterprise browser (the former Talon) that delivers security controls — DLP, isolation, last-mile inspection — at the browser layer, especially for unmanaged/BYOD and contractor devices, integrated into Palo Alto Networks' Prisma SASE.

**What it does** — Prisma Access Browser turns the browser into a control point: it enforces data-loss controls (copy/paste, download, screenshot, watermarking), protects against phishing, web-based attacks and malicious extensions, and gives security teams visibility into web/SaaS usage without needing to manage the underlying device. For AI specifically, browser-layer controls are a pragmatic way to govern shadow-AI use (paste limits into chatbots, blocking risky GenAI sites) on devices the org doesn't own.

**Where it sits in the stack** — UX layer, [[enterprise-browser]]. It addresses the **sensitive-data** leg (DLP at the point of use) and **egress** leg (what data can leave into web apps / GenAI tools) of the lethal trifecta. Complements [[network-security-sase]] (the same Prisma Access fabric) and overlaps with [[browser-security-extension]] approaches.

**Deployment & architecture** — SaaS-managed Chromium browser installed on managed and unmanaged endpoints; part of the Prisma SASE portfolio so policy and visibility flow into the broader PANW console. Was offered complimentary to qualified Prisma SASE customers at acquisition time.

**Positioning & differentiators** — Palo Alto's answer to the enterprise-browser category, leaning on SASE integration as the differentiator (consistent policy across network and browser). Nearest neighbors: [[island]] (the category pioneer), [[menlo-security]], [[seraphic]], [[red-access]], plus the platform browsers [[chrome-enterprise]] and [[microsoft-edge-business]]; lighter-weight alternatives are [[browser-security-extension]] vendors like [[layerx]] and [[material-security]].

**Ownership, funding & M&A** — **Former Talon Cyber Security** (founded 2021, Tel Aviv; raised ~$143M). **Acquired by [[palo-alto-networks]] — VERIFIED:** intent announced Nov 2023, acquisition **closed 2023-12-28** (reported ~$625M); rebranded Prisma Access Browser. Confirmed against PANW's own closing press release. The seed flag "former Talon (PANW)" is **confirmed.** Corrected the stub's `ownership: independent` to `subsidiary`.

**CTO / hedge-fund lens** — Optional in the taxonomy, but a strong fit for funds with significant contractor/BYOD or third-party-manager access who need DLP and GenAI controls without full MDM. If you're already a Prisma SASE customer the marginal cost is low. Standalone, weigh against [[island]] and against just deploying a [[browser-security-extension]] on existing Chrome.

**Competitors / alternatives** — [[island]], [[menlo-security]], [[seraphic]], [[red-access]], [[chrome-enterprise]], [[microsoft-edge-business]], [[layerx]].

**Open questions / to verify**
- Exact reported acquisition price (~$625M is press-reported, not PANW-disclosed).
- Current feature parity / GenAI-specific controls vs. dedicated [[ai-access-governance]] tools.

**Sources**
- [PANW Closes Talon Cyber Security Acquisition](https://www.paloaltonetworks.com/company/press/2023/palo-alto-networks--closes-talon-cyber-security-acquisition-and-will-offer-complimentary-enterprise-browser-to-qualified-sase-ai-customers) — fetched 2026-06-28 — supports: Talon -> Prisma Access Browser, close 2023-12-28, capabilities; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed flag "former Talon (PANW)" — Talon Cyber Security acquired by Palo Alto Networks, closed 2023-12-28 (reported ~$625M), rebranded Prisma Access Browser, against PANW closing press release. Established Talon founded 2021 (Tel Aviv). Corrected ownership independent->subsidiary, confidence low->high.
