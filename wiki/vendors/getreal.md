---
title: GetReal Security
type: vendor
name: GetReal Security
slug: getreal
categories: [anti-deepfake]
layer: foundation
aliases: [GetReal Labs, GetReal]
website: "https://www.getrealsecurity.com"
founded: 2022
hq: San Mateo, CA, USA
ownership: independent
ownership_detail: VC-backed; $17.5M Series A led by Forgepoint Capital (2025-03-26). No acquisition found.
ownership_confidence: high
funding_total: $17.5M (Series A)
last_funding: Series A, 2025-03-26 (Forgepoint Capital)
deployment: [saas, api]
target_customer: enterprise / government / defense (financial services, BPO, recruiting)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [deepfake, forensics, provenance, content-authenticity]
---

# GetReal Security

> Primary category: [anti-deepfake](../categories/anti-deepfake.md).

**One-liner** — An enterprise deepfake-defense and digital-forensics platform — co-founded by deepfake-detection authority Hany Farid — that detects, analyzes, and helps respond to synthetic media and impersonation across voice, video, and content provenance.

## What it does
GetReal combines real-time deepfake detection with forensic content analysis and content-provenance/authenticity verification. Beyond a yes/no detector, it positions as a "Forensics Platform as a Service" with detection plus human expert investigation and response. The job it does: when an org receives a suspicious call, video, or piece of media (e.g., a "CFO" on a video call authorizing a transfer), GetReal helps determine whether it is authentic and supports an incident response.

## Where it sits in the stack
Sits in [anti-deepfake](../categories/anti-deepfake.md) at the **foundation** layer, defending the authenticity of human communications and media. Lethal-trifecta relevance is **untrusted-input**-adjacent: it gates whether incoming media/identity can be trusted. It is a social-engineering / authenticity and digital-forensics control rather than a model/data control. Trust zone: the external-communications boundary (red→yellow), with an incident-response role inside the org.

## Deployment & architecture
- **SaaS platform + API** ("FPaaS"); product line spans:
  - **GetReal Protect** — real-time detection across voice and video.
  - **GetReal Inspect** — forensic content verification (launched Feb 2025).
  - **GetReal Prepare** / **GetReal Respond** — training and expert investigation services.
- Pitched for high-value communications (conferencing, calls). Has announced a partnership with [doppel](doppel.md) for deepfake brand/executive-impersonation attacks. Specific SIEM/IdP connectors not confirmed here.

## Positioning & differentiators
Known for the **Hany Farid pedigree** (digital forensics / provenance research) and a forensics-plus-services posture rather than a pure detection API. Differs from [reality-defender](reality-defender.md) (detection-API breadth across audio/video/image/text) by emphasizing forensic analysis, provenance, and expert response. Differs from [pindrop](pindrop.md) (telephony voice biometrics / call-center fraud at scale) by being communications- and media-forensics-oriented rather than call-channel infrastructure. Co-founded with Ted Schlein (Ballistic Ventures); CEO Matthew Moynahan. Other neighbors: [adaptive-security](adaptive-security.md), [doppel](doppel.md).

## Ownership, funding & M&A
- **Independent, VC-backed.** No acquisition found (no seed M&A flag).
- **$17.5M Series A** led by **Forgepoint Capital** (announced 2025-03-26), with Ballistic Ventures, Evolution Equity Partners, Cisco Investments, IQT, and Capital One Ventures.
- Founded 2022 (originally "GetReal Labs"). Ownership confidence **high**.
- HQ reported as San Mateo, CA (Bay Area); one older listing said Austin, TX — treated as soft/stale, San Mateo used with medium confidence.

## CTO / hedge-fund lens
**Day-2 / situational.** Strong fit for **executive-impersonation and synthetic-media fraud** — the deepfake-on-a-video-call or cloned-voice-authorizing-a-wire scenarios that directly threaten asset managers. The forensics + response services angle suits firms that want investigation support, not just a detector. Not a model-risk/SR 11-7 control. Better fit for larger or more targeted shops (those with public-facing executives, large wire flows, or recruiting/BPO exposure) than for a lean 50-person fund, which may not justify a dedicated platform yet.

## Competitors / alternatives
[reality-defender](reality-defender.md), [pindrop](pindrop.md), [doppel](doppel.md), [adaptive-security](adaptive-security.md)

## Open questions / to verify
- Exact HQ (San Mateo vs older Austin listing) and current headcount.
- Pricing; degree of automation vs. reliance on expert-services.
- Independent accuracy benchmarks; specific enterprise integrations.

## Sources
- [About GetReal Security](https://www.getrealsecurity.com/about-us) — fetched 2026-06-28 — supports: founders (Hany Farid, Ted Schlein), CEO Moynahan, founded 2022, product line, $17.5M Series A/Forgepoint, target customers; confidence: high (vendor) for product, med for HQ
- [GetReal Security Launches Unified Deepfake Defense Platform (Enterprise Security Tech)](https://www.enterprisesecuritytech.com/post/getreal-security-launches-unified-deepfake-defense-platform-to-counter-ai-powered-deception) — fetched 2026-06-28 — supports: independent corroboration of unified deepfake-defense / provenance positioning and exec-impersonation use cases; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed status ($17.5M Series A, Forgepoint lead 2025-03), Hany Farid/Ted Schlein founders, CEO Moynahan, founded 2022, San Mateo CA HQ (med conf), forensics+detection FPaaS product line; no M&A; set ownership_confidence high.
