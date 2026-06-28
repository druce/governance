---
type: vendor
name: Cyberhaven
slug: cyberhaven
categories: [dlp, ai-access-governance]
layer: data
aliases: [Linea AI, LLiM, Data Detection and Response]
website: "https://www.cyberhaven.com"
founded: 2016
hq: Palo Alto, California, USA (founded in Lausanne, Switzerland)
ownership: independent
ownership_detail: Venture-backed independent. $100M Series D (2025-04-02) led by StepStone Group at a $1B valuation; total raised ~$250M. No acquisition.
ownership_confidence: high
funding_total: ~$250M (as of 2025-04)
last_funding: Series D, $100M, 2025-04-02 (StepStone Group; Schroders, Industry Ventures)
deployment: [saas, sdk]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [dlp, ddr, data-lineage, shadow-ai, insider-risk, dspm]
---

# Cyberhaven

> **One-liner** — An endpoint-based, AI-powered data-loss-prevention / "data detection and response" (DDR) platform that tracks the *lineage* of data — where it came from, how it moved, and where it's going — so it can stop sensitive data (including data pasted into ChatGPT and other shadow-AI tools) from leaking.

**Categories** — [dlp](../categories/dlp.md) (primary), [ai-access-governance](../categories/ai-access-governance.md)

## What it does

Cyberhaven is a data-security platform built around **data lineage**: rather than matching content against regex/pattern rules the way classic DLP does, its endpoint agent records the full chain of custody for data — the document it was copied from, the app it passed through, the user, and the destination. That history lets it classify *derived* and pasted content by the sensitivity of its source, and apply policy accordingly. Cyberhaven brands the approach **Data Detection and Response (DDR)**, explicitly analogizing it to how EDR transformed endpoint security: behavioral analysis applied to data flows instead of signatures.

The platform bundles three jobs that are usually sold separately: **DLP**, **insider risk management (IRM)**, and **DSPM** (data security posture). The differentiating AI layer is **Linea AI** and its **Large Lineage Model (LLiM)** — a foundation model trained to predict the next likely action in a corporate data workflow (the way an LLM predicts the next word), used to surface anomalous/risky data movement.

A large part of its current pitch is **shadow AI / GenAI data protection**: showing which AI tools employees use, what data is going into them, and blocking risky flows. The canonical example: an employee copies text from a sensitive file and pastes it into ChatGPT; the endpoint agent sees both the source (and its sensitivity) and the destination, and enforces policy on the paste. A newer **Agentic AI Security** offering extends this to autonomous AI agents and MCP servers running on endpoints — visibility into which agents run, what data they touch, and what actions they take.

## Where it sits in the stack

Primary home is the [dlp](../categories/dlp.md) category in the **data layer**, with a strong secondary footprint in [ai-access-governance](../categories/ai-access-governance.md) (CASB-for-AI / shadow-AI). In lethal-trifecta terms it controls the **sensitive-data** and **egress** legs: it watches sensitive data at the endpoint and blocks/controls its exfiltration to untrusted destinations (including AI tools). It does *not* address untrusted-input/prompt-injection — that is the job of [ai-runtime-security](../categories/ai-runtime-security.md). Trust-zone relevance: it instruments the endpoint (the boundary between green/internal and red/external), making it a data-egress control point rather than a model-traffic inspector.

## Deployment & architecture

- **Endpoint agent + SaaS console.** The core sensor is a lightweight endpoint agent (Windows/macOS) that observes file, clipboard, browser, and app events locally; analytics and policy live in the Cyberhaven SaaS backend. This is **endpoint DLP**, contrasted by the vendor with network/proxy DLP — there is no inline TLS proxy required.
- **Browser/SaaS coverage** for web apps and AI tools (e.g. detecting paste into ChatGPT/Claude/Gemini), plus cloud-data coverage for DSPM.
- **Integrations** — typical DLP/IRM ecosystem: SIEM/SOC for alerting, IdP for user context, and AI-tool/endpoint telemetry. (Specific connector list not fully verified — see open questions.)

## Positioning & differentiators

- **Lineage vs. pattern-matching.** The core claim that sets it apart from legacy content-inspection DLP ([nightfall-ai](nightfall-ai.md), Microsoft Purview DLP, Netskope DLP): it tracks data provenance across transformations, so it catches sensitive data even after it's been copied, renamed, or reformatted, and reduces false positives.
- **DDR framing + LLiM.** "Data detection and response" and a purpose-built lineage foundation model are its marketing wedge against both classic DLP and newer AI-era DLP entrants ([mind](mind.md), [prompt-security](prompt-security.md), [lasso-security](lasso-security.md)).
- **Shadow-AI overlap.** On the [ai-access-governance](../categories/ai-access-governance.md) side it competes with [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), Nudge, Aurascape and others — but Cyberhaven comes at shadow-AI from the *endpoint/data* direction (what data left the device) rather than the network/proxy direction.

## Ownership, funding & M&A

- **Independent, venture-backed.** No acquisition (the seed carried no M&A flag; confirmed none found).
- **Series D: $100M, announced 2025-04-02**, led by **StepStone Group** (Nasdaq: STEP), with new investors **Schroders** and **Industry Ventures**. Brought total funding to **~$250M** and a **$1B valuation** (a roughly 7x jump in a year). Source: Cyberhaven press release (primary). `ownership_confidence: high`.
- Company stated it plans to expand via both **M&A and organic innovation** — i.e. a potential acquirer, not a target, as of mid-2025.

> Soft note (leadership): the April 2025 press release attributes the CEO quote to **Howard Ting**; some third-party company profiles list **Nishant Doshi** as current CEO. Possible leadership transition; unverified. Non-blocking.

## CTO / hedge-fund lens

- **Day-1 if you are letting staff use external AI tools.** For a fund whose crown jewels are research, positions, and MNPI, controlling what gets pasted into ChatGPT/Claude is a real Day-1 data-egress problem, and endpoint DLP is a credible control. Cyberhaven's lineage angle is attractive where classic DLP drowns teams in false positives.
- **Caveat — agent footprint.** It requires an **endpoint agent** on every managed device; small funds with heavy BYOD or contractor populations get partial coverage. It is also a fuller-weight platform purchase than a narrow AI-paste blocker.
- **Overlap with what you may already own.** Many shops already run Microsoft Purview or a Netskope/Zscaler SSE with DLP; Cyberhaven is a rip-and-replace/augment decision, not additive-by-default.
- **Model-risk / SR 11-7:** not a model-governance tool; relevance is data-leakage and insider-risk controls that support an AI acceptable-use policy, not model validation.
- **Fit: medium** — strong for mid/large regulated shops worried about sensitive-data egress into AI; heavier than a small fund may want as a first control.

## Competitors / alternatives

- DLP / data layer: [nightfall-ai](nightfall-ai.md), [mind](mind.md), [prompt-security](prompt-security.md), [lasso-security](lasso-security.md), plus Microsoft Purview DLP and Netskope DLP.
- DSPM neighbors: [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [varonis](varonis.md).
- Shadow-AI / [ai-access-governance](../categories/ai-access-governance.md): [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), Aurascape, Nudge.

## Open questions / to verify

- Current CEO (Howard Ting vs. Nishant Doshi) — confirm and date any transition.
- Exact integration/connector list (SIEM, IdP, AI gateways, MCP) and OS support beyond Windows/macOS.
- Whether the Agentic AI Security / MCP-server-visibility product is GA or early access, and its pricing relationship to the core platform.
- Any funding/ownership change after 2025-04.

## Sources

- [Cyberhaven Raises $100 Million Series D at $1 Billion Valuation](https://www.cyberhaven.com/press-releases/cyberhaven-raises-100-million-series-d-at-1-billion-valuation) — fetched 2026-06-28 — supports: Series D $100M, $1B valuation, ~$250M total, StepStone lead, Palo Alto HQ, DDR/LLiM positioning; confidence: high (primary).
- [How Romanian-Ukrainian Founders Built Cyberhaven into an AI Cybersecurity Unicorn (The Recursive) + Cyberhaven brief history (CanvasBusinessModel)](https://therecursive.com/cyberhaven-founders-romanian-ukrainian-ai-cybersecurity-unicorn/) — fetched 2026-06-28 — supports: founded 2016, founders, Lausanne→Palo Alto, Linea AI/LLiM launched early 2024; confidence: med (secondary).
- [DLP for GenAI / What Is Shadow AI / Secure AI Adoption (Cyberhaven)](https://www.cyberhaven.com/blog/dlp-for-genai) — fetched 2026-06-28 — supports: shadow-AI positioning, endpoint-agent paste-into-ChatGPT mechanics, DSPM+DLP+IRM bundle; confidence: med (vendor marketing).
- [Cyberhaven Targets Shadow AI Agents With New Endpoint Security Platform (TipRanks) + AI Security product page](https://www.tipranks.com/news/private-companies/cyberhaven-targets-shadow-ai-agents-with-new-endpoint-security-platform) — fetched 2026-06-28 — supports: Agentic AI Security, MCP-server/agent endpoint visibility; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2016 (Lausanne, now Palo Alto HQ), founders, independent venture-backed status, $100M Series D (2025-04-02, StepStone, $1B valuation, ~$250M total) raised ownership_confidence to high; documented data-lineage/DDR/LLiM, endpoint-agent DLP, and shadow-AI / Agentic-AI positioning. Set status: researched, confidence: medium, 4 sources cached. Noted soft CEO-name discrepancy (Howard Ting vs. Nishant Doshi).
