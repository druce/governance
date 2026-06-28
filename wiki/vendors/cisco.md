---
type: vendor
name: Cisco
slug: cisco
categories: [network-security-sase, ai-runtime-security, ai-red-teaming, non-human-identity, siem-soc]
layer: foundation
aliases: [Cisco Systems]
website: https://www.cisco.com
founded: 1984
hq: San Jose, California, USA
ownership: public
ownership_detail: "Public (NASDAQ: CSCO). Active acquirer in AI security: Splunk (closed 2024-03-18, $28B), Robust Intelligence (closed ~2024-09-24, now Cisco AI Defense), Galileo (announced 2026-04-09; reported closed 2026-05-22), Astrix Security (intent announced 2026-05-04, pending)."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, on-prem, self-hosted, inline-proxy, api]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 4
last_updated: 2026-06-28
tags: [acquirer, platform, networking, security]
---

# Cisco

> Primary category: [network-security-sase](../categories/network-security-sase.md). Cisco is the network/security incumbent assembling an AI-security stack mostly by acquisition.

**One-liner** — The networking and enterprise-security incumbent that, via [splunk](splunk.md) (SIEM), [cisco-ai-defense](cisco-ai-defense.md) (the former [robust-intelligence](robust-intelligence.md)), [galileo](galileo.md) (AI observability/eval) and a pending buy of [astrix-security](astrix-security.md) (non-human identity), is stitching together an end-to-end "secure the AI" platform.

**What it does** — Cisco's relevance here is twofold. (1) Its **network-security/SASE** estate (Secure Access, Umbrella, Firewall, Duo, Identity Intelligence) is the TLS-inspecting plumbing many enterprises already run — see [network-security-sase](../categories/network-security-sase.md). (2) It has bought its way into AI security: model/prompt runtime defense and red-teaming (Cisco AI Defense), AI agent observability and guardrails (Galileo, folding into Splunk Observability), SIEM/SOC (Splunk), and — pending — agentic/non-human identity (Astrix). The pitch is one vendor spanning network, identity, SOC, and AI-model security.

**Where it sits in the stack** — Spans several layers: [network-security-sase](../categories/network-security-sase.md) (foundation egress/inspection), [siem-soc](../categories/siem-soc.md) via [splunk](splunk.md), [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-red-teaming](../categories/ai-red-teaming.md) via [cisco-ai-defense](cisco-ai-defense.md), [llm-observability](../categories/llm-observability.md)/guardrails via [galileo](galileo.md), and [non-human-identity](../categories/non-human-identity.md) via [astrix-security](astrix-security.md) (pending). Trifecta-wise the portfolio touches all three legs: untrusted input (AI Defense prompt-injection defense), sensitive data (DLP/inspection), and egress (SASE, AI gateway controls).

**Deployment & architecture** — Mixed: on-box and cloud-delivered network security (inline proxy / man-in-the-middle TLS inspection), SaaS for Duo/Identity Intelligence/Secure Access, Splunk as SaaS or self-hosted, and API/SDK-delivered AI Defense guardrails. Telemetry from the acquired AI-security products is being funneled into Splunk as the SOC backbone.

**Positioning & differentiators** — Breadth and incumbency, not best-of-breed in any single AI-security niche. The differentiator is consolidation: a shop already running Cisco networking + Duo + Splunk can add AI Defense and (eventually) Astrix without onboarding new vendors. The tradeoff is integration debt — these are recently acquired, separately-built products still being knit together.

## Ownership, funding & M&A

Cisco is a public company (NASDAQ: CSCO), founded 1984, HQ San Jose, CA. It is the **acquirer** in four AI-security-relevant deals flagged by the seed — all verified:

- **[splunk](splunk.md)** — completed **2024-03-18**, ~**$28B** (announced 2023-09-21). Largest acquisition in Cisco history. Confirmed (high).
- **[robust-intelligence](robust-intelligence.md) → [cisco-ai-defense](cisco-ai-defense.md)** — intent announced **2024-08-26**, closed ~**2024-09-24**. Robust Intelligence's tech became Cisco AI Defense / Foundation AI. Confirmed (high).
- **[galileo](galileo.md)** — intent announced **2026-04-09**; secondary press reports completion **2026-05-22** (Cisco's own note said expected close Q4 FY2026). Confirmed announced (high); close date medium.
- **[astrix-security](astrix-security.md)** — **intent** announced **2026-05-04**; **not yet closed** as of 2026-06-28. Terms undisclosed (press cites ~$400M, unconfirmed). Confirmed as intent (high); completion pending.

## CTO / hedge-fund lens

Most funds already touch Cisco somewhere (network gear, Duo MFA, or Splunk). That makes Cisco a natural **consolidation play**: if you run Splunk for SIEM (Day-1) you can evaluate Cisco AI Defense and Astrix as add-ons rather than net-new vendors. But don't assume the AI-security pieces are mature just because Cisco owns them — they are freshly acquired. Evaluate Cisco AI Defense and Galileo on their own merits against best-of-breed neighbors. SR 11-7 / model-risk relevance is indirect (via AI Defense red-teaming and Galileo eval logs feeding evidence), not a governance platform in itself.

## Competitors / alternatives

[palo-alto-networks](palo-alto-networks.md) (the closest mirror-image roll-up: Prisma AIRS, Cortex, CyberArk), [crowdstrike](crowdstrike.md), [zscaler](zscaler.md), [netskope](netskope.md), [microsoft-sentinel](microsoft-sentinel.md) (vs Splunk).

## Open questions / to verify

- Confirm Galileo deal **close** with a Cisco primary (intent + secondary close found; Cisco closing PR not yet located).
- Track Astrix close (pending); confirm final terms if disclosed.

## Sources
- [Cisco Blogs — Intent to Acquire Astrix Security](https://blogs.cisco.com/news/cisco-announces-intent-to-acquire-astrix-security) — fetched 2026-06-28 — supports: Astrix intent 2026-05-04, NHI/agentic identity, Splunk/Duo/Identity Intelligence integration; confidence: high
- [Cisco Blogs — Intent to Acquire Galileo](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) — fetched 2026-06-28 — supports: Galileo intent 2026-04-09, AI observability/guardrails into Splunk Observability; confidence: high
- [Cisco Blogs — Intent to Acquire Robust Intelligence](https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence) — fetched 2026-06-28 — supports: Robust Intelligence announced 2024-08-26, basis of Cisco AI Defense; confidence: high
- [Network World — Cisco completes $28B Splunk acquisition](https://www.networkworld.com/article/2066444/cisco-completes-28-billion-splunk-acquisition.html) — fetched 2026-06-28 — supports: Splunk close 2024-03-18, $28B; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Cisco is public (CSCO) and the acquirer of Splunk (closed 2024-03-18, $28B), Robust Intelligence (closed ~2024-09-24 → Cisco AI Defense), Galileo (announced 2026-04-09, reported closed 2026-05-22) and Astrix Security (intent 2026-05-04, pending). Added siem-soc category. Set ownership=public, confidence high.
