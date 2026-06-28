---
type: vendor
name: Cato Networks
slug: cato-networks
categories: [network-security-sase, ai-spm]
layer: foundation
aliases: [Cato]
website: https://www.catonetworks.com
founded: 2015
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: "Private/VC-backed (Series G extended to $409M, 2025). Acquirer of [aim-security](aim-security.md) — announced 2025-09-03 (~$350M reported), Cato's first acquisition"
ownership_confidence: high
funding_total: ">$700M raised (Series G round $409M, 2025)"
last_funding: "Series G extended +$50M (Acrew Capital), total $409M — 2025"
deployment: [saas, inline-proxy]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [sase, sse, acquirer, network-security]
---

# Cato Networks

> **Researched 2026-06-28.** Primary category: [network-security-sase](../categories/network-security-sase.md). Cato is the **acquirer** of [aim-security](aim-security.md) (not itself acquired — the seed stub mislabeled this).

**One-liner** — A cloud-native SASE platform (network + security in one cloud service) that bought AI-security pure-play [aim-security](aim-security.md) in 2025 to fold an AI firewall, shadow-AI control, and AI-SPM into its SASE Cloud.

## What it does
Cato delivers SASE (Secure Access Service Edge): SD-WAN, ZTNA, secure web gateway, CASB, FWaaS, threat prevention, and data protection as a single cloud-native service, converging enterprise networking and security. Its global private backbone inspects all traffic inline, which is the natural place to enforce AI controls. With the [aim-security](aim-security.md) acquisition, Cato adds: securing employee use of public AI apps (shadow AI / [ai-access-governance](../categories/ai-access-governance.md)), an "AI Firewall" protecting private AI apps and agents ([ai-runtime-security](../categories/ai-runtime-security.md)), and AI Security Posture Management ([ai-spm](../categories/ai-spm.md)).

## Where it sits in the stack
Primary [network-security-sase](../categories/network-security-sase.md) (Foundation layer — the TLS-inspecting man-in-the-middle that everything else rides on) with a secondary [ai-spm](../categories/ai-spm.md) tag from the Aim acquisition. Lethal-trifecta role: as the inline SASE chokepoint it can touch all three legs — inspecting **untrusted input**, blocking **sensitive-data** egress (DLP/CASB), and controlling **egress** to AI services. Sits at the green↔red boundary for the whole enterprise.

## Deployment & architecture
SaaS, delivered through Cato PoPs on a global private backbone; agents/clients and site connectors route traffic inline through the Cato SASE Cloud (inline proxy model). Aim's AI security is being integrated natively into that platform rather than sold as a bolt-on. Standard integrations: IdP/SSO, SIEM, endpoint.

## Positioning & differentiators
Cato's differentiator is a single-vendor, single-platform SASE built ground-up (vs stitched-together acquisitions), founded by [[Shlomo Kramer]] (co-founder of Check Point and Imperva). The Aim deal — Cato's **first-ever acquisition** — is its move to make AI security a native SASE capability rather than a separate product. Competes with the other SASE/SSE incumbents folding in AI security: [zscaler](zscaler.md), [netskope](netskope.md), [palo-alto-networks](palo-alto-networks.md), [cloudflare](cloudflare.md), [cisco](cisco.md), [forcepoint](forcepoint.md).

## Ownership, funding & M&A
**Private / VC-backed.** Founded **2015** by Shlomo Kramer and Gur Shatz; HQ **Tel Aviv, Israel**. In 2025 it extended its Series G with an additional $50M from Acrew Capital (round total **$409M**) and reported surpassing **$300M ARR**. **Acquired [aim-security](aim-security.md)** — announced **2025-09-03**; deal value not officially disclosed, press reports ~$350M. Verified against Cato's own press release and corroborating press. The seed framed Cato as "acquired," which is wrong — Cato is the buyer. **Confidence: high.**

## CTO / hedge-fund lens
Day-1 *if* you're adopting SASE as your network-security backbone; the AI-security additions are a reason to consolidate AI controls onto the same platform rather than buy a separate AI firewall. For a hedge fund already on a different SASE/SSE vendor, Cato's AI features are a competitive comparison point, not a standalone buy. Indirect SR 11-7 relevance (control/monitoring point, not a model-risk system). Fits mid-market to enterprise that wants one vendor for network + AI traffic security.

## Competitors / alternatives
[zscaler](zscaler.md), [netskope](netskope.md), [palo-alto-networks](palo-alto-networks.md), [cloudflare](cloudflare.md), [cisco](cisco.md), [forcepoint](forcepoint.md).

## Open questions / to verify
- Official Aim deal value (only press estimates ~$350M; not disclosed by Cato).
- Whether the Aim brand/standalone product persists or is fully absorbed.
- Precise cumulative funding total (Series G round = $409M; lifetime raised higher).

## Sources
- [Cato Networks Acquires Aim Security… (Cato press release)](https://www.catonetworks.com/news/cato-acquires-aim-security-to-extend-sase-leadership-and-secure-enterprise-ai-transformation/) — fetched 2026-06-28 — supports: 2025-09-03 announce, first acquisition, Aim capabilities, Cato founding/HQ, $409M Series G, $300M ARR; confidence: high
- [Cato Networks acquires AI security startup Aim Security (CyberScoop)](https://cyberscoop.com/cato-networks-acquires-ai-security-startup-aim-security/) — fetched 2026-06-28 — supports: ~$350M reported value, deal context; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership from "acquired" to **independent** (Cato is the acquirer). Confirmed Cato **acquired [aim-security](aim-security.md)** (announced 2025-09-03, ~$350M reported, Cato's first acquisition). Filled founding (2015), Tel Aviv HQ, Series G ($409M), $300M ARR. Confidence high.
</content>
