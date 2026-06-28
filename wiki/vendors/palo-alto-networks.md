---
type: vendor
name: Palo Alto Networks
slug: palo-alto-networks
categories: [network-security-sase, siem-soc, edr-xdr, ai-runtime-security, ai-soc-analysts, enterprise-browser, ai-gateway, non-human-identity]
layer: foundation
aliases: [PANW, Prisma, Cortex, Strata]
website: https://www.paloaltonetworks.com
founded: 2005
hq: Santa Clara, California, USA
ownership: public
ownership_detail: "Public (NASDAQ: PANW). Acquirer, not target — AI-security roll-up: Talon (closed 2023-12-28), Protect AI (2025-07-22), CyberArk incl. Conjur (closed 2026-02-11, ~$25B), Portkey (2026-05-29)."
ownership_confidence: high
funding_total: n/a (public)
last_funding: IPO 2012 (NYSE; now NASDAQ: PANW)
deployment: [saas, inline-proxy, api, on-prem, sdk]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 4
last_updated: 2026-06-28
tags: [platform, sase, xdr, siem, ai-security, acquirer]
---

# Palo Alto Networks

> Primary category: [network-security-sase](../categories/network-security-sase.md). The largest pure-play cybersecurity platform vendor, and the most aggressive consolidator in AI security.

**One-liner** — The incumbent network/SOC security platform (Strata SASE, Cortex XDR/XSIAM, Prisma Cloud) that has bought its way into a full AI-security stack: Prisma AIRS for AI runtime, Portkey as its AI gateway, CyberArk for identity, and Prisma Access Browser for enterprise browsing.

**What it does** — PANW sells three platform pillars plus a new fourth: **Strata** (next-gen firewalls, Prisma Access / SASE — the TLS-inspecting man-in-the-middle that sees user and AI traffic), **Cortex** (XDR, XSIAM SOC platform, agentic SOC analysts), **Prisma Cloud** (CNAPP), and now **Prisma AIRS** (AI runtime security + posture + red-teaming + AI gateway). The CyberArk deal adds an Identity Security pillar (PAM, secrets, machine/agent identity). For a buyer this means much of the AI-governance layer cake can be sourced from one vendor.

**Where it sits in the stack** — Spans nearly every layer this wiki tracks: [network-security-sase](../categories/network-security-sase.md), [siem-soc](../categories/siem-soc.md), [edr-xdr](../categories/edr-xdr.md), [ai-runtime-security](../categories/ai-runtime-security.md) (via [prisma-airs](prisma-airs.md)), [ai-gateway](../categories/ai-gateway.md) (via [portkey](portkey.md)), [ai-soc-analysts](../categories/ai-soc-analysts.md) (Cortex AgentiX), [enterprise-browser](../categories/enterprise-browser.md) (via [prisma-access-browser](prisma-access-browser.md)), and [non-human-identity](../categories/non-human-identity.md) / [secrets-management](../categories/secrets-management.md) / [identity-governance](../categories/identity-governance.md) (via [cyberark](cyberark.md) and [conjur](conjur.md)). Touches all three legs of the lethal trifecta: inspects untrusted input (AIRS, SASE), guards sensitive data (DLP in SASE/browser), and controls egress (SASE, AI gateway).

**Deployment & architecture** — Inline TLS-inspecting proxy (Prisma Access), on-box and virtual firewalls, SaaS consoles (Cortex, Prisma AIRS), API/SDK guardrails (AIRS API intercept), an enterprise browser, and now an AI gateway (Portkey) between apps and model APIs. Integrates with its own SIEM (XSIAM), IdP, and third-party tooling.

**Positioning & differentiators** — The "platformization" pitch: consolidate point tools onto Strata/Cortex/Prisma/Identity. Differentiator is breadth plus the SASE install base — it already mediates traffic, so AI controls bolt on. Nearest platform neighbors: [cisco](cisco.md) (also rolling up AI security: Robust Intelligence -> AI Defense, Splunk, Astrix, Galileo), [crowdstrike](crowdstrike.md) (SOC + Pangea), the Microsoft stack ([microsoft-entra](microsoft-entra.md)/Defender/Purview), and SASE peers [zscaler](zscaler.md) and [netskope](netskope.md).

**Ownership, funding & M&A** — Public, NASDAQ: PANW; founded 2005 (Nir Zuk); HQ Santa Clara; CEO Nikesh Arora since 2018; FY2025 revenue ~$9.22B. **AI-security roll-up, all verified against PANW press releases this research:**
- **Talon Cyber Security** -> Prisma Access Browser. Closed **2023-12-28**.
- **Protect AI** -> folded into Prisma AIRS. Closed **2025-07-22**.
- **CyberArk** (incl. Conjur secrets) -> new Identity Security pillar. Announced **2025-07-30** (~$25B: $45 cash + 2.2005 PANW shares/share); **closed 2026-02-11**.
- **Portkey** -> AI Gateway component of Prisma AIRS. Announced **2026-04-30**; **closed 2026-05-29**; terms undisclosed.

**CTO / hedge-fund lens** — Day-1 relevance is high because most funds already run something from PANW (a firewall, Prisma Access, or Cortex). The strategic question is consolidation risk vs. convenience: buying the AI-security layer from your existing SASE vendor is operationally simple and procurement-friendly, but concentrates dependency and means inheriting integration timelines for freshly-acquired products (Portkey, Protect AI) still being natively stitched in. Identity-Security-for-agentic-AI (CyberArk) is the piece most relevant to SR 11-7-style model/agent governance.

**Competitors / alternatives** — [cisco](cisco.md), [crowdstrike](crowdstrike.md), [zscaler](zscaler.md), [netskope](netskope.md), [microsoft-entra](microsoft-entra.md) (as platform stacks), plus the standalone vendors PANW's acquisitions displace.

**Open questions / to verify**
- Integration maturity of Portkey and Protect AI inside Prisma AIRS (marketing claims native; verify in product).
- CyberArk integration roadmap into Cortex/Strata post-close.

**Sources**
- [Palo Alto Networks to Acquire CyberArk](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-announces-agreement-to-acquire-cyberark--the-identity-security-leader) — fetched 2026-06-28 — supports: CyberArk deal terms/date; confidence: high
- [PANW Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents) — fetched 2026-06-28 — supports: Portkey close 2026-05-29, AI gateway role; confidence: high
- [PANW Completes Acquisition of Protect AI](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-completes-acquisition-of-protect-ai) — fetched 2026-06-28 — supports: Protect AI close 2025-07-22, Prisma AIRS; confidence: high
- [PANW Closes Talon Cyber Security Acquisition](https://www.paloaltonetworks.com/company/press/2023/palo-alto-networks--closes-talon-cyber-security-acquisition-and-will-offer-complimentary-enterprise-browser-to-qualified-sase-ai-customers) — fetched 2026-06-28 — supports: Talon close 2023-12-28 -> Prisma Access Browser; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed ownership=public (NASDAQ: PANW), founded 2005, HQ Santa Clara, FY25 rev ~$9.22B. Verified the full AI-security roll-up against PANW press releases: Talon (closed 2023-12-28), Protect AI (2025-07-22), CyberArk ~$25B (announced 2025-07-30, closed 2026-02-11), Portkey (closed 2026-05-29). Corrected seed's "ownership: acquired" — PANW is the acquirer, not a target.
