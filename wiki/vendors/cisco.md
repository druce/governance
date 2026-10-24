---
title: Cisco
type: vendor
name: Cisco
slug: cisco
aka: [Cisco Systems]
primary_category: network-security-sase
also_listed_in: [ai-runtime-security, ai-red-teaming, non-human-identity, siem-soc, identity-access]
website: https://www.cisco.com
founded: 1984
hq: San Jose, California, USA
ownership_state: public
owner: null
ownership_note: 'Public (NASDAQ: CSCO). Active acquirer in AI security: Splunk (closed 2024-03-18, $28B), Robust Intelligence (closed ~2024-09-24, now Cisco AI Defense), Galileo (announced 2026-04-09; reported closed 2026-05-22), Astrix Security (intent announced 2026-05-04, pending).'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas, on-prem, self-hosted]
form_factor: [inline-proxy, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [acquirer, platform, networking, security, duo, mfa, sso]
sources:
  - {claim: "Cisco Duo provides MFA, SSO, passwordless, device trust, and Duo Directory (cloud user directory usable as an IdP); list pricing Essentials $3 / Advantage $6 / Premier $9 per user per month, Duo Free up to 10 users", url: "https://duo.com/product", date: 2026-10-23, confidence: medium}
---

# Cisco

> Primary category: [network-security-sase](../categories/network-security-sase.md). Cisco is the network/security incumbent assembling an AI-security stack mostly by acquisition.

**One-liner** — The networking and enterprise-security incumbent that, via [splunk](splunk.md) (SIEM), [cisco-ai-defense](cisco-ai-defense.md) (the former [robust-intelligence](robust-intelligence.md)), [galileo](galileo.md) (AI observability/eval) and a pending buy of [astrix-security](astrix-security.md) (non-human identity), is stitching together an end-to-end "secure the AI" platform.

**What it does** — Cisco's relevance here is twofold. (1) Its **network-security/SASE** estate (Secure Access, Umbrella, Firewall, Duo, Identity Intelligence) is the TLS-inspecting plumbing many enterprises already run — see [network-security-sase](../categories/network-security-sase.md). (2) It has bought its way into AI security: model/prompt runtime defense and red-teaming (Cisco AI Defense), AI agent observability and guardrails (Galileo, folding into Splunk Observability), SIEM/SOC (Splunk), and — pending — agentic/non-human identity (Astrix). The pitch is one vendor spanning network, identity, SOC, and AI-model security.

**Where it sits in the stack** — Spans several layers: [network-security-sase](../categories/network-security-sase.md) (foundation egress/inspection), [identity-access](../categories/identity-access.md) via **Duo**, [siem-soc](../categories/siem-soc.md) via [splunk](splunk.md), [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-red-teaming](../categories/ai-red-teaming.md) via [cisco-ai-defense](cisco-ai-defense.md), [llm-observability](../categories/llm-observability.md)/guardrails via [galileo](galileo.md), and [non-human-identity](../categories/non-human-identity.md) via [astrix-security](astrix-security.md) (pending). Across the portfolio it screens untrusted input (AI Defense prompt-injection defense), protects sensitive data (DLP/inspection), and controls outbound data flows (SASE, AI gateway controls).

**Deployment & architecture** — Mixed: on-box and cloud-delivered network security (inline proxy / man-in-the-middle TLS inspection), SaaS for Duo/Identity Intelligence/Secure Access, Splunk as SaaS or self-hosted, and API/SDK-delivered AI Defense guardrails. Telemetry from the acquired AI-security products is being funneled into Splunk as the SOC backbone.

**Identity (Duo)** — cross-listed to [identity-access](../categories/identity-access.md), 2026-10-23. Cisco Duo is a full workforce-identity product, not just a SASE add-on. Its product page (fetched 2026-10-23) lists **MFA**, cloud **SSO**, passwordless, device trust, and **Duo Directory**, a cloud user directory that lets Duo act as the identity provider. Before Duo Directory, Duo SSO typically layered MFA and policy over an existing Active Directory or third-party SAML IdP. Duo also includes ITDR, Cisco Identity Intelligence/ISPM, and a newly listed "Agentic IAM" offering (no detail published). List pricing on the page is $3, $6 or $9 per user per month (Essentials, Advantage, Premier), with a free tier up to 10 users. Many funds run Duo as the MFA layer in front of Entra ID or Okta rather than as the primary IdP. A 2026-10 CTO-survey respondent wrote in "Duo" under Identity Providers. Ask whether Duo is your *directory* or only your *second factor*, because the answer changes which identity questions this survey slot covers.

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
- [Cisco Duo — product overview](https://duo.com/product) — fetched 2026-10-23 — supports: MFA, SSO, passwordless, device trust, Duo Directory, ITDR, list pricing tiers; confidence: medium (vendor). Cached: `raw/sources/2026-10-23--cisco--duo-iam.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Cisco is public (CSCO) and the acquirer of Splunk (closed 2024-03-18, $28B), Robust Intelligence (closed ~2024-09-24 → Cisco AI Defense), Galileo (announced 2026-04-09, reported closed 2026-05-22) and Astrix Security (intent 2026-05-04, pending). Added siem-soc category. Set ownership=public, confidence high.
- [2026-10-23] Cross-listed to identity-access on the evidence of Duo's product page (MFA, SSO, passwordless, device trust, Duo Directory as IdP); prompted by a 2026-10 CTO-survey write-in ("Duo" under Identity Providers). Only the Duo claims were checked; last_verified left unchanged.
