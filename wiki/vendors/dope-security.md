---
title: dope.security
type: vendor
name: dope.security
slug: dope-security
aka: [Dope Security, dope]
primary_category: network-security-sase
also_listed_in: [dlp, ai-access-governance]
website: https://dope.security/
founded: 2021
hq: Palo Alto, CA, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; ~$24M raised across 3 rounds, most recently a $16M Series A in March 2023. No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$24M
last_funding: Series A $16M, 2023-03
market_position: {network-security-sase: ai-native-disruptor}
deployment_model: [saas]
form_factor: [agent]
data_leaves_tenancy: "false"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market
last_verified: 2026-08-26
verify_after: null
tags: [sse, swg, on-device, fly-direct, ai-dlp, tls-inspection]
sources:
  - {claim: "Fly Direct architecture inspects TLS traffic on the endpoint with traffic going straight to the internet, eliminating the stopover data centre; lightweight agent under 100MB RAM, claimed up to 4x legacy proxy SWG performance; AI governance native with Dopamine DLP for prompts and uploads", url: "https://dope.security/post/sse-architecture-2026", date: 2026-08-26, confidence: low}
  - {claim: "~$24.0M raised across 3 funding rounds; most recent $16.0M Series A in March 2023", url: "https://pitchbook.com/profiles/company/489828-79", date: 2026-08-26, confidence: medium}
  - {claim: "shadow-AI discovery (per-user AI app/account inventory), corporate-vs-personal tenant control for ChatGPT etc., Dopamine DLP on prompts, all from the endpoint agent", url: "https://dope.security/post/shadow-ai-detection-governance", date: 2026-06-25, confidence: low}
---

# dope.security

> Primary category: [network-security-sase](../categories/network-security-sase.md). Also listed in [dlp](../categories/dlp.md) and [ai-access-governance](../categories/ai-access-governance.md).

**One-liner** — An SSE that inverts the category's architecture: TLS inspection runs **on the endpoint** and traffic goes straight to its destination, with no vendor data centre in the path.

**What it does** — A secure web gateway plus DLP delivered as a lightweight endpoint agent. Every other vendor in [network-security-sase](../categories/network-security-sase.md) works by hairpinning user traffic through the vendor's own points of presence, decrypting and inspecting there, then forwarding on. dope.security calls that the "stopover" and does the inspection locally instead — branded **Fly Direct**. The claimed consequences are lower latency (no detour), no vendor-side outage taking the workforce offline, and **user traffic never traversing the vendor's infrastructure**. Its AI-relevant piece is **Dopamine DLP**, applied to prompts and uploads to AI services rather than bolted on as a URL category.

**Shadow-AI / AI usage control** (basis for the [ai-access-governance](../categories/ai-access-governance.md) cross-list, added 2026-10-23). The vendor markets three AI-usage functions from the same endpoint agent. (1) A per-user **AI usage** inventory: which AI apps and accounts are in use, sanctioned or not, and personal or enterprise-licensed. (2) **Tenant control**, e.g. allowing corporate ChatGPT while blocking personal ChatGPT on the same domain by reading the workspace/tenant identifier in decrypted traffic. (3) **Dopamine DLP** to "stop regulated data from leaving in a prompt." The vendor argues SSO and network-log discovery undercounts shadow AI, because personal accounts in a browser tab generate no SSO event. That argument is fair, but it is also how the vendor sells its own product. A 2026-10 CTO-survey respondent was evaluating dope.security for this job ("Looking at Dope.security to address," demo stage). All of this is **vendor blog content**, with no independent test found.

**Naming / provenance** — Founded 2021 by Kunal Agarwal (previously Forcepoint). The brand is lowercase `dope.security`; expect "Dope Security" in lists. Founded 2021, Palo Alto CA.

**Ownership & viability** — `independent`, VC-backed, **~$24M raised**, latest a **$16M Series A in March 2023**. Three years without a disclosed round while competing against [zscaler](zscaler.md), [netskope](netskope.md), [palo-alto-networks](palo-alto-networks.md) and [fortinet](fortinet.md) is the central risk on this page — this is a small company selling into a category dominated by multi-billion-dollar incumbents. Treat as a genuine but early bet.

**Positioning & differentiators** —
- **The architecture is the product.** On-device inspection is a real, checkable difference, not marketing. It changes the answer to "does our web and AI-prompt traffic leave our control to be decrypted by a third party?" from *yes* to *no* — which is a materially different conversation with a compliance officer than the one [zscaler](zscaler.md) or [netskope](netskope.md) require.
- **No vendor-side outage domain.** SSE outages take entire workforces offline; there is no shared cloud plane here to fail.
- **Managed-device only, by construction.** The flip side: no agent, no coverage. Unmanaged devices, BYOD, contractors and non-endpoint traffic are outside the model in a way they are not for a cloud proxy.
- **Endpoint cost.** Inspection consumes local CPU; the vendor's counter is the sub-100MB footprint claim, which is a vendor claim and unverified.

**Who should choose them / anti-fit** — Fits a **fully managed-device fleet** at a firm that objects on principle or on regulation to a third party decrypting its traffic — a defensible position for a manager handling MNPI. **Anti-fit:** a firm with meaningful BYOD or contractor access, one needing branch/appliance coverage for non-endpoint traffic, or one whose procurement will not approve a Series-A vendor for a Day-1 control.

**Known weaknesses / gotchas** — Vendor size versus the incumbents is the dominant concern. Every performance and architecture claim above traces to the vendor's own marketing, which is unusually assertive (its blog publishes its own competitive "buyer's guides") — **treat those posts as marketing, not evidence**. No independent analyst placement found.

**Deployment & data handling** — Endpoint agent. **Traffic does not leave the tenancy for inspection** — that is the entire architectural claim, and it is the one thing worth verifying directly in a trial. What telemetry or metadata *is* sent to dope's cloud control plane is **unverified** and is the right follow-up question.

**Integrations & partnerships** — IdP and management-tool integrations claimed; specific list unverified.

**Compliance & FS traction** — **Unverified.** Cited references (a Fortune 100 deployment of 18,000+ devices, Outreach Health) are vendor-published and not financial services. Certifications not confirmed.

**Commercial** — Not public. Per-seat subscription; positioned as cheaper than legacy cloud proxies.

## Open questions

- Any funding since the 2023 Series A — the key viability question.
- What metadata reaches dope's control plane, given the "traffic never leaves" claim.
- Independent verification of the performance and footprint claims.
- Coverage story for unmanaged devices, BYOD and non-endpoint traffic.
- Certifications held; any financial-services customers.
- Depth of the AI-usage controls versus dedicated [ai-access-governance](../categories/ai-access-governance.md) tools: prompt-level coaching, file-upload coverage (not addressed in the 2026-06-25 post), and AI-app catalog size.

## Sources

- [SSE Architecture in 2026 (dope.security)](https://dope.security/post/sse-architecture-2026) — fetched 2026-08-26 — supports: Fly Direct architecture, agent footprint, Dopamine DLP; confidence: low (vendor marketing, competitive positioning content)
- [dope.security company profile (PitchBook)](https://pitchbook.com/profiles/company/489828-79) — fetched 2026-08-26 — supports: funding total, Series A; confidence: medium
- [Shadow AI: How to Find and Govern the Tools Your Team Already Uses (dope.security, 2026-06-25)](https://dope.security/post/shadow-ai-detection-governance) — fetched 2026-10-23 — supports: AI usage inventory, tenant control, Dopamine DLP on prompts; confidence: low (vendor marketing)
- Cached: `raw/sources/2026-08-26--dope-security--architecture-and-funding.md`, `raw/sources/2026-10-23--dope-security--shadow-ai-controls.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki — a human had added it to the SSE and DLP questions.
- [2026-10-23] Cross-listed to ai-access-governance on the evidence of dope.security's shadow-AI discovery, tenant control and prompt-DLP features (vendor blog); prompted by a 2026-10 CTO-survey write-in under AI Usage Control / Shadow-AI (evaluating, demo stage). Only the AI-usage claims were re-checked; last_verified left unchanged.
