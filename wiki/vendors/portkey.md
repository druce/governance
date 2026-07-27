---
title: Portkey
type: vendor
name: Portkey
slug: portkey
aka: [Portkey AI]
primary_category: ai-gateway
also_listed_in: []
website: https://portkey.ai
founded: 2023
hq: San Francisco, California, USA
ownership_state: acquired-closed
owner: Palo Alto Networks
ownership_note: 'Acquired by Palo Alto Networks — definitive agreement signed and announced 2026-04-30; closed 2026-05-29. Both dates confirmed against PANW''s Form 10-Q for the quarter ended 2026-04-30 (filed 2026-06-03): Note 6 records the signing, Note 17 Subsequent Events records the completion. Total consideration $140M in cash and replacement awards, subject to adjustments — disclosed only in the 10-Q; neither PANW press release stated terms. Becomes the AI Gateway component of Prisma AIRS. Recorded as a business combination in PANW fiscal Q4 2026.'
acquisition: {announced: 2026-04-30, closed: 2026-05-29, price: $140M cash + replacement awards}
funding_total: ~$18M (≈$3M seed 2023 + $15M Series A Feb 2026)
last_funding: Series A $15M led by Elevation Capital, announced 2026-02-19 (acquired by PANW ~3 months later)
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [api, inline-proxy]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [ai-gateway, llm-routing, observability, palo-alto, acquired]
sources:
  - {claim: acquisition-close, url: "https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm", date: 2026-06-03, confidence: high}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm", date: 2026-06-03, confidence: high}
  - {claim: acquisition-announced, url: "https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents", date: 2026-04-30, confidence: high}
---

# Portkey

> **Researched 2026-06-28; re-verified 2026-07-27 against PANW's SEC filings.** Primary category: [ai-gateway](../categories/ai-gateway.md). The AI gateway / control plane Palo Alto Networks bought to anchor Prisma AIRS. **No longer an independent company** — the acquisition closed 2026-05-29 for $140M. `portkey.ai` is still live (HTTP 200, no redirect) under the Portkey brand, but banners the PANW completion release; shop for this as **Prisma AIRS AI Gateway** and price it as part of a PANW platform deal.

**One-liner** — A high-performance AI gateway and control plane that sits between enterprise apps and model APIs — routing, rate-limiting, caching, governing, and observing LLM traffic — acquired by [palo-alto-networks](palo-alto-networks.md) in May 2026 to become the gateway layer of [prisma-airs](prisma-airs.md).

**What it does** — Portkey is the "single exit door" for model traffic: one API endpoint in front of many model providers, with routing/failover, load balancing, cost and rate controls, prompt/response logging, caching, and guardrail hooks. It markets itself as a unified control plane for production AI and claims to process trillions of tokens per month at the low latency needed for agent-to-agent communication.

**Where it sits in the stack** — Model/prompt-layer [ai-gateway](../categories/ai-gateway.md). As a chokepoint on model traffic it primarily controls outbound data flows (what leaves to which model/provider) and is the natural enforcement point to bolt untrusted-input inspection (prompt injection screening) onto. Under PANW it becomes the AI Gateway that feeds Prisma AIRS three capabilities: AI runtime security (traffic inspection), agent identity security, and AI observability.

**Deployment & architecture** — Inline gateway/proxy deployed as SaaS or self-hosted, fronting provider APIs via a unified API; SDKs and an OpenAI-compatible interface; integrates with observability and guardrail tooling. Designed for high-throughput agentic workloads.

**Positioning & differentiators** — Known for combining a fast gateway with built-in governance/observability rather than being a thin proxy. **This is no longer an independent-vendor comparison.** Post-close, Portkey's pitch is not "best gateway" but "the gateway that is natively wired into a full AI-security platform" — PANW positions it as the enforcement point where three previously separate acquisitions meet: AI Runtime Security inspects the traffic, [Idira](cyberark.md) (the rebranded CyberArk portfolio) authenticates the agent identity behind each call, and Chronosphere carries the telemetry. That bundle is the differentiator and the lock-in in equal measure. Nearest neighbors, now all more independent than Portkey is: [litellm](litellm.md) (OSS routing), [kong](kong.md) (API-gateway lineage, MCP), [truefoundry](truefoundry.md), [cloudflare](cloudflare.md) AI Gateway, [openrouter](openrouter.md). Note that the neutral-gateway field is consolidating generally — [f5](f5.md) acquired CalypsoAI on a similar thesis — so "buy independent" increasingly means buying OSS.

**Ownership, funding & M&A** — Founded 2023 (Rohit Agarwal, Ayush Garg); HQ San Francisco. Raised ~$3M seed (Lightspeed, 2023) and a **$15M Series A led by Elevation Capital** announced 2026-02-19. **Acquired by [palo-alto-networks](palo-alto-networks.md) — VERIFIED against SEC filings:** PANW signed the definitive agreement and announced it 2026-04-30, and **completed the acquisition 2026-05-29** for **total consideration of $140M in cash and replacement awards, subject to adjustments**. Both dates and the price come from PANW's Form 10-Q for the quarter ended 2026-04-30 (filed 2026-06-03) — Note 6 records the signing and the $140M, Note 17 Subsequent Events records the close; PANW's MD&A repeats the close date. Neither PANW press release disclosed terms, so the price is available *only* from the filing. PANW books it as a business combination in fiscal Q4 2026. The exit came only ~3 months after the Series A — very fast, and at $140M a modest tuck-in: for scale, PANW closed [CyberArk](cyberark.md) at $21.1B final consideration (2026-02-11) and Koi Security at $231M (2026-04-14) in the same fiscal year.

**CTO / hedge-fund lens** — An AI gateway is Day-1 if you run LLM apps and want one governed exit door for model traffic (logging, cost control, provider failover, policy). Portkey no longer answers that as a standalone purchase: its roadmap, pricing, and support are now PANW's, and the value case is strongest for shops that are already (or willing to become) Prisma AIRS customers. Two concrete procurement consequences. First, **check the commercial terms, not just the tech** — a $140M tuck-in folded into a platform is the classic setup for standalone SKUs to be retired or repriced into a bundle at renewal; get the standalone-availability commitment in writing rather than inferring it from the site still being live. Second, if you specifically wanted a *neutral* gateway — one that does not tie your model-traffic chokepoint to a single security vendor's platform — the realistic answer is now OSS ([litellm](litellm.md)) or a general API gateway ([kong](kong.md)), since the independent commercial options in this category keep getting bought. Placing your chokepoint inside a vendor platform is a defensible choice; making it accidentally is not.

**Competitors / alternatives** — [litellm](litellm.md), [kong](kong.md), [truefoundry](truefoundry.md), [cloudflare](cloudflare.md), [openrouter](openrouter.md), [f5](f5.md).

**Open questions / to verify**
- Whether Portkey stays available as a standalone product or only inside Prisma AIRS. Still open as of 2026-07-27 — `portkey.ai` continues to sell under its own brand and pricing, but that is the normal ~2-month post-close state and is not evidence of a long-term standalone commitment.
- Continued support for the open-source / self-hosted gateway under PANW.
- Whether the Portkey brand survives or is absorbed into the Prisma AIRS naming (PANW retired the CyberArk brand in favor of Idira within ~3 months of that close, so brand retirement here would not be surprising).
- Purchase-price allocation (goodwill / intangibles split) — not yet published; lands in PANW's FY2026 Form 10-K, expected ~September 2026.

**Sources**
- [PANW Form 10-Q, quarter ended 2026-04-30 (filed 2026-06-03)](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm) — fetched 2026-07-27 — supports: definitive agreement 2026-04-30, **close 2026-05-29** (Note 17 Subsequent Events + MD&A), **price $140M in cash and replacement awards** (Note 6); confidence: high (primary, SEC filing)
- [PANW Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents) — fetched 2026-06-28, re-fetched 2026-07-27 — supports: close 2026-05-29 (dateline), AI Gateway role in Prisma AIRS alongside Idira and Chronosphere; terms not disclosed here; confidence: high
- [PANW to Acquire Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents) — fetched 2026-07-27 — supports: announcement date 2026-04-30, expected close in PANW fiscal Q4 2026; confidence: high
- [Portkey Raises $15M Series A (Portkey blog)](https://portkey.ai/blog/series-a-funding/) — fetched 2026-06-28 — supports: founded 2023, SF HQ, $15M Series A 2026-02; confidence: high (vendor source for funding)
- Cached: `raw/sources/2026-07-27--portkey--panw-10q-close-date-and-price.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed M&A flag: acquired by Palo Alto Networks (announced 2026-04-30, closed 2026-05-29, terms undisclosed) against PANW completion press release. Becomes Prisma AIRS AI Gateway. Established founded 2023, SF HQ, ~$18M total funding incl. $15M Series A (Feb 2026) only ~3 months pre-acquisition. Raised ownership_confidence low->high.
- [2026-07-27] URL audit + M&A re-verification. `portkey.ai` live (HTTP 200, no redirect), now bannering "Palo Alto Networks has completed the acquisition of Portkey" — website unchanged. **Checked for the `closed == announced` copy-paste bug found on [natoma](natoma.md) during the same sweep: not present here.** Both dates independently re-confirmed against PANW's Form 10-Q for the quarter ended 2026-04-30 (filed 2026-06-03) — definitive agreement 2026-04-30 (Note 6), completion 2026-05-29 (Note 17 Subsequent Events, restated in MD&A); `acquired-closed` stands. **New fact:** the previously-undisclosed price is in the filing — **$140M in cash and replacement awards, subject to adjustments** — so `acquisition.price` moved from `null` to a verified figure. Added the 10-Q and the announcement release as source entries; expanded the M&A, positioning, and CTO-lens sections for a vendor that is no longer independent (platform lock-in, standalone-SKU risk at renewal, OSS as the neutral alternative).
