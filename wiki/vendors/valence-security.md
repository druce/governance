---
type: vendor
name: Valence Security
slug: valence-security
categories: [sspm]
layer: foundation
aliases: []
website: https://www.valencesecurity.com
founded: 2021
hq: Tel Aviv, Israel (R&D); US presence in South San Francisco, California
ownership: independent
ownership_detail: "Venture-backed, independent as of 2026-06-28; no acquisition found. Series A ($25M) led by M12 (Microsoft), Oct 2022."
ownership_confidence: high
funding_total: ~$32M
last_funding: "Series A $25M led by M12 / Microsoft (2022-10-26); prior $7M Seed led by YL Ventures (2021)"
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [sspm, saas-security, ai-security, itdr]
---

# Valence Security

> Primary category: [sspm](../categories/sspm.md).

**One-liner** — A SaaS (and increasingly AI) security platform that discovers SaaS/AI app usage, finds and prioritizes posture risk, and emphasizes collaborative, business-user-driven remediation so security teams aren't the only ones fixing misconfigurations.

**Categories** — [sspm](../categories/sspm.md)

## What it does
Valence connects via API to an organization's SaaS apps, inventories SaaS and AI usage (including shadow apps and OAuth integrations), and identifies risks across misconfigurations, identities, third-party integrations, and data sharing. Its signature angle is **remediation workflow**: routing fixes to the relevant app owners/business users (not just dumping findings on the security team) to actually close risks. It now layers in AI Security Posture Management (governing AI tools and agents) and ITDR (identity-based threat detection/response across SaaS).

## Where it sits in the stack
Sits in [sspm](../categories/sspm.md) (foundation layer), spanning SaaS discovery, SSPM, AI-SPM, and ITDR. Trifecta-wise it primarily addresses the **sensitive-data** leg (reducing SaaS/AI data exposure and over-broad integrations). The newer AI-SPM/discovery features make it directly relevant to **shadow-AI** inventory — a growing reason a fund might look at this layer.

## Deployment & architecture
SaaS-delivered; API/OAuth integrations into target SaaS and AI apps (no inline proxy or endpoint agent for core function). Supports 175+ SaaS/AI applications (vendor claim). Remediation routing integrates with collaboration/ticketing so app owners receive and action fixes.

## Positioning & differentiators
Known for the "collaborative remediation" / SaaS-mesh-risk framing (third-party app-to-app integration risk) and an early pivot to AI/agentic-era security messaging (treat "Leader in SaaS and AI Security" as marketing). Smaller and later-stage-funded than [appomni](appomni.md) and [obsidian-security](obsidian-security.md). Nearest neighbors: [appomni](appomni.md) (enterprise posture/data-access depth), [obsidian-security](obsidian-security.md) (identity threat detection), [grip-security](grip-security.md) (SaaS/identity discovery-led), [adaptive-shield](adaptive-shield.md) (CrowdStrike), [wing-security](wing-security.md), [reco](reco.md), [nudge-security](nudge-security.md), [docontrol](docontrol.md).

## Ownership, funding & M&A
Independent, venture-backed. Founded 2021 (exited stealth 2021) by Yoni Shohet (CEO) and Shlomi Matichin (CTO); Israeli R&D roots (Tel Aviv) with a US presence (South San Francisco, CA — per third-party profiles; not stated on the vendor company page). Funding: $7M Seed (2021, led by YL Ventures) and a $25M Series A led by M12 (Microsoft's venture fund), announced 2022-10-26, with YL Ventures, Porsche Ventures, Akamai, Alumni Ventures, and angel Michael Fey — **~$32M total**. No acquisition found as of 2026-06-28 — `ownership_confidence: high` that it remains independent. (Seed registry asked to confirm "independent?" — confirmed independent.)

## CTO / hedge-fund lens
**Day-2.** Like its peers, it secures SaaS a fund already runs; the differentiated draw for a lean shop is the remediation routing (less security-team toil) and the shadow-SaaS/AI discovery. Fit is **medium**: a smaller, SaaS-heavy fund worried about ungoverned third-party app and AI-tool connections may find the discovery + delegated-remediation model a good match; deep-pocketed enterprises may prefer the larger incumbents. Supports data-governance/access-review evidence; not directly an SR 11-7 model-risk control, though AI-SPM features touch AI-tool governance.

## Competitors / alternatives
[appomni](appomni.md), [obsidian-security](obsidian-security.md), [grip-security](grip-security.md), [adaptive-shield](adaptive-shield.md), [wing-security](wing-security.md), [reco](reco.md), [nudge-security](nudge-security.md), [docontrol](docontrol.md)

## Open questions / to verify
- Whether any funding round has closed since the 2022 Series A; current total beyond ~$32M.
- Definitive current HQ split (Tel Aviv R&D vs US office) — vendor page omits both.
- Maturity of AI-SPM/agentic-security features vs. peers.

## Sources
- [Our Story, Leadership, and Investors (vendor company page)](https://www.valencesecurity.com/company) — fetched 2026-06-28 — supports: founders, investors, independent ownership, SSPM/AI-SPM/ITDR/discovery scope; confidence: high (primary, vendor tone).
- [Valence Security Announces $25M Series A (vendor press release; corroborated by TechCrunch/SecurityWeek/BusinessWire)](https://www.valencesecurity.com/news/valence-security-announces-25m-series-a-to-scale-delivery-of-collaborative-saas-security-remediation-solutions-to-customers) — fetched 2026-06-28 — supports: $25M Series A led by M12 (2022-10-26), $7M Seed (2021), ~$32M total, founded 2021; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (no acquisition), founded 2021 by Yoni Shohet/Shlomi Matichin, Tel Aviv/SSF, ~$32M total ($25M Series A led by M12, 2022; $7M Seed 2021). Set ownership_confidence high, status researched.
