---
type: vendor
name: Red Access
slug: red-access
categories: [enterprise-browser]
layer: ux
aliases: [RedAccess]
website: "https://redaccess.io/"
founded: 2021
hq: Tel Aviv, Israel
ownership: independent
ownership_detail: "Independent and venture-backed as of 2026-06-28; no acquisition found. Note: SentinelOne participated as an investor (S Ventures), not as an acquirer."
ownership_confidence: high
funding_total: $23M
last_funding: Series A, $17M, 2025-09-10 (led by Norwest Venture Partners)
deployment: [saas, sdk]
target_customer: enterprise / mid-market (remote workers, unmanaged devices, contractors)
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [untrusted-input, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [browser-security, secure-browsing, agentless, sse]
---

# Red Access

> Agentless "secure browsing" platform that adds enterprise security to any existing browser via a session-based architecture — pitched as a lightweight SSE alternative with no agents or network overhaul. Primary category: [enterprise-browser](../categories/enterprise-browser.md).

**One-liner** — Secures web/SaaS/GenAI sessions inside the browsers people already use, without deploying a dedicated browser, endpoint agent, or rerouting traffic through a network stack.

## What it does

Red Access protects browsing sessions across browsers, web apps, and SaaS/GenAI tools: data-loss prevention, secure access to corporate assets, and protection for remote workers on untrusted networks and unmanaged/BYOD devices. It markets itself as "the world's first agentless secure browsing platform" and as a way to extend Security Service Edge (SSE)–style controls "beyond the perimeter" without the heavy infrastructure, agents, or rollout delays of traditional SSE/proxy stacks.

## Where it sits in the stack

[enterprise-browser](../categories/enterprise-browser.md) category, **UX layer**. Like other browser-security tools it primarily controls the **egress** leg (what data can leave a session — uploads, downloads, paste-into-GenAI) and the **untrusted-input** leg (hostile web content) at the user's last mile, sitting on the boundary between the untrusted web (red zone) and corporate apps/data. Its session-based design integrates with existing firewalls/SSE rather than replacing them.

## Deployment & architecture

Delivered as SaaS with an **agentless, session-based architecture** — no endpoint agent and no network re-architecture; it integrates with existing infrastructure such as firewalls and extends SSE capabilities. This positions it against both inline-proxy/RBI designs and dedicated-browser approaches. (Exact in-browser delivery mechanism — extension vs injected runtime — to verify against current docs.)

## Positioning & differentiators

Red Access plays in the "secure any browser, agentless" segment:
- vs [seraphic](seraphic.md) — closest peer; both secure existing browsers without rerouting traffic. Red Access emphasizes an agentless, SSE-extension/session framing; Seraphic emphasizes browser-runtime protection and was acquired by CrowdStrike.
- vs [layerx](layerx.md) — both deliver browser-layer security on existing browsers (LayerX via extension); direct competitors.
- vs [island](island.md) and [prisma-access-browser](prisma-access-browser.md) — those ship a dedicated managed Chromium browser; Red Access avoids deploying a new browser.
- vs [menlo-security](menlo-security.md) — Menlo's heritage is remote browser isolation/proxy; Red Access avoids the proxy/network overhaul.
- vs [chrome-enterprise](chrome-enterprise.md) / [microsoft-edge-business](microsoft-edge-business.md) — native browser-management from the browser makers; Red Access is browser-agnostic with added security/DLP.

## Ownership, funding & M&A

- **Independent / venture-backed** as of 2026-06-28. No acquisition found.
- Founded **2021** in **Tel Aviv, Israel**; CEO and co-founder **Dor Zvi**.
- **$17M Series A** announced **2025-09-10**, led by **Norwest Venture Partners**, with **Ten Eleven Ventures, SentinelOne's S Ventures, Elron Ventures, and Singtel Innov8 Ventures**. **Total funding $23M.**
- The research brief flagged checking for a Palo Alto Networks (or other) acquisition; **none was found**. SentinelOne appears only as a **financial investor** (S Ventures), not an acquirer — no contradiction.

## CTO / hedge-fund lens

**Priority: optional.** For a hedge fund whose sensitive work lives in the browser and SaaS, an agentless browser-security layer is an attractive low-friction control, especially for contractors, BYOD, and remote access on untrusted networks, and for governing GenAI usage/data egress. The agentless framing means fast pilots without endpoint/agent rollout. Caveats for a buyer: smaller, earlier-stage vendor (Series A, ~$23M raised) — weigh vendor-maturity and longevity risk, and verify depth of DLP/GenAI controls in a pilot. No direct SR 11-7 / model-risk role; relevance is data egress and AI-usage governance, not model validation.

## Competitors / alternatives

[seraphic](seraphic.md), [layerx](layerx.md), [island](island.md), [menlo-security](menlo-security.md), [prisma-access-browser](prisma-access-browser.md), [chrome-enterprise](chrome-enterprise.md), [microsoft-edge-business](microsoft-edge-business.md)

## Open questions / to verify

- Exact in-browser delivery mechanism behind the "agentless" claim (extension vs injected runtime vs network session).
- Customer traction / named references and depth of GenAI DLP controls.
- Whether the ~$6M pre–Series A capital was a formal seed round (date/lead unverified).

## Sources
- [Red Access Secures $17M to Power a Lightweight SSE Alternative without Agents or Network Overhaul (BusinessWire)](https://www.businesswire.com/news/home/20250910522651/en/Red-Access-Secures-$17M-to-Power-a-Lightweight-SSE-Alternative-without-Agents-or-Network-Overhaul) — fetched 2026-06-28 — supports: $17M Series A 2025-09-10, Norwest lead + investors, $23M total, agentless secure browsing, founded 2021 Tel Aviv, CEO Dor Zvi; confidence: high
- [Red Access Raises $17 Million for Agentless Security Platform (SecurityWeek)](https://www.securityweek.com/red-access-raises-17-million-for-agentless-security-platform/) — fetched 2026-06-28 — supports: founding 2021, Tel Aviv HQ, CEO Dor Zvi, funding/investors, product/deployment, target customer; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2021 (Tel Aviv), CEO Dor Zvi, $17M Series A 2025-09-10 led by Norwest, $23M total. Confirmed company is independent (no acquisition); SentinelOne is an investor not an acquirer. Set ownership=independent, confidence high. No HARD contradiction (no Palo Alto / other acquirer found).
