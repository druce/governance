---
title: Helicone
type: vendor
name: Helicone
slug: helicone
aka: []
primary_category: llm-observability
also_listed_in: []
website: https://www.helicone.ai
founded: 2023
hq: San Francisco, CA
ownership_state: acquired-closed
owner: Mintlify
ownership_note: Acquired by Mintlify (announced and effective 2026-03-03; no separate closing date disclosed, terms undisclosed). Founders joined Mintlify; Helicone brand and site persist but the product is in maintenance mode and Mintlify is helping customers migrate off.
acquisition: {announced: 2026-03-03, closed: 2026-03-03, price: null}
funding_total: pre-seed/seed stage (small; YC W23)
last_funding: Pre-seed/seed (pre-acquisition); acquired by Mintlify 2026-03
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [inline-proxy, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: developers / engineering teams (~16,000 organizations cited)
last_verified: 2026-07-27
verify_after: 2026-10-27
tags: [open-source, observability, proxy, ai-gateway, yc-w23, maintenance-mode]
---

# Helicone

> **Researched 2026-06-28. Ownership re-verified 2026-07-27.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — Open-source, proxy-based LLM observability and AI gateway — one line of code to monitor LLM usage; acquired by Mintlify and now in maintenance mode.

**What it does** — Helicone sits as a proxy between your app and LLM providers: change one line (point your base URL at Helicone) and it logs every request/response, cost, latency, and usage, with caching, rate-limiting, and a unified gateway to 100+ models via an OpenAI-compatible endpoint. The low-friction proxy model was its signature. It processed ~14.2 trillion tokens across ~16,000 organizations.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer; its gateway features also overlap [ai-gateway](../categories/ai-gateway.md). As a proxy it sits on the model-traffic path, but it is an observability/routing layer, not a security firewall — it does not by itself screen prompts or block sensitive-data leakage. Adjacent to [litellm](litellm.md), [portkey](portkey.md), [openrouter](openrouter.md) on the gateway side.

**Deployment & architecture** — Inline proxy (the default, one-line integration), plus async logging SDK option; self-hostable OSS or Helicone Cloud SaaS. Integrates with OpenAI, Anthropic, Azure, and other providers at the API layer.

**Positioning & differentiators** — Best known for the proxy-based, one-line-change integration — the lowest-friction onboarding in the category and a combined observability + gateway pitch. Contrast with SDK/OTel-based [langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [langsmith](langsmith.md) (more eval depth, deeper instrumentation) and eval-first [braintrust](braintrust.md). The proxy model adds a network hop on the critical path, a tradeoff for the convenience.

**Ownership, funding & M&A** — **Acquired by Mintlify — a closed acquisition, announced 2026-03-03**, confirmed on both counterparties' blogs and re-verified 2026-07-27. Terms were not disclosed. No separate closing date was ever published: Helicone's own post used completed past tense on announcement day ("Helicone *has been* acquired by Mintlify"), founders Justin Torre and Cole Gottdank moved to Mintlify in San Francisco, and Mintlify has controlled the product and roadmap for the five months since — so the announcement date is treated as effective. This is a genuine company acquisition, not a partnership or a reseller tie-up, but it has strong **acqui-hire / technology-absorption** character: the team and the tech moved, the product was frozen rather than invested in. Founded 2023 (YC W23), HQ San Francisco; funding was early-stage/small. Confidence: high on the deal; medium only on the precise close date, which was never disclosed.

**What the Mintlify deal means for the product** — Mintlify sells a documentation/AI-knowledge platform, not an observability product, and it bought Helicone to power **its own** assistant, agent, and workflow products — intelligent routing, multi-provider fallback, and real-time observability inside a "unified full stack AI knowledge infrastructure." Helicone's capabilities therefore survive *inside Mintlify*, not as a standalone product line. The standalone Helicone product stays in **maintenance mode**: security updates, bug fixes, and new-model support keep shipping, but active feature development has ended. Mintlify has also committed to "work closely with every customer to support a smooth migration to another platform" — the vendor is steering its own customers off the product. **No sunset or shutdown date has been announced** by either party as of 2026-07-27, and `helicone.ai` remains live and still sells (free trial, pricing page, provider integrations) under a "Helicone Joins Mintlify" banner. Note the mismatch: the homepage still reads as a promotional, actively-sold product, and the frozen status is disclosed only in the linked announcement post.

**CTO / hedge-fund lens** — The maintenance-mode status makes Helicone a **weak choice for a new Day-1 deployment** — you would be adopting a frozen product. Of interest mainly to teams already on it (self-hosted OSS can keep running) or studying the proxy pattern. For new builds prefer an actively developed alternative. If you are already on it there is no fire drill — no shutdown date has been announced and Mintlify will help you migrate — but treat it as a wind-down and plan the exit on your own schedule rather than waiting for a sunset notice. The inline-proxy model also means LLM traffic (potentially MNPI) flows through Helicone unless self-hosted — self-host if you adopt it at all.

**Competitors / alternatives** — [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [datadog](datadog.md), [comet](comet.md), [litellm](litellm.md), [portkey](portkey.md).

**Open questions / to verify**
- Long-term fate of Helicone Cloud SaaS under Mintlify (how long it stays live) — no sunset date announced as of 2026-07-27.
- Whether the OSS repo continues to receive community contributions.
- Whether the exact acquisition close date is ever disclosed (none published; announcement date used as effective).

## Sources
- [Helicone is joining Mintlify (Helicone blog)](https://www.helicone.ai/blog/joining-mintlify) — fetched 2026-06-28, re-fetched 2026-07-27 — supports: acquisition by Mintlify 2026-03-03, completed past-tense framing, maintenance mode, proxy model, scale, founders; confidence: high.
- [Mintlify acquires Helicone (Mintlify blog)](https://www.mintlify.com/blog/mintlify-acquires-helicone) — fetched 2026-06-28, re-fetched 2026-07-27 — supports: acquisition confirmation/rationale, maintenance mode, customer-migration commitment, fold-in to Mintlify's AI products; confidence: high.
- [raw/sources/2026-07-27--helicone--mintlify-acquisition-closed.md](../../raw/sources/2026-07-27--helicone--mintlify-acquisition-closed.md) — cached 2026-07-27 — supports: deal type (acquisition, not partnership/merger), closed status and its evidence, undisclosed terms, no sunset date, live-site/brand-persistence check; confidence: high (medium on close date).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Helicone acquired by Mintlify (2026-03-03, confirmed), product now maintenance-mode — changed `ownership` independent→acquired (confidence low→high), set hedge_fund_fit low for new deployments; filled founding/HQ/proxy deployment. No seed M&A flag existed but acquisition found and recorded.
- [2026-07-27] URL audit flagged the live "Helicone Joins Mintlify" banner on helicone.ai and asked whether "Joins" meant an acquisition, a merger, an acqui-hire, or a partnership. Re-read both counterparties' announcement posts: it is a **closed acquisition** — Helicone says it "has been acquired by Mintlify" (completed past tense, 2026-03-03), Mintlify says "Mintlify is acquiring Helicone" and "Mintlify has acquired @helicone_ai", and Mintlify has run the product for five months since. Not a merger (Helicone absorbed, Mintlify the sole surviving brand) and not a partnership, though the shape is acqui-hire-like: founders moved, product frozen, tech folded into Mintlify's AI products. Changed `ownership_state` acquired-pending→**acquired-closed**, set `acquisition.closed` 2026-03-03 (announcement date used as effective — no separate closing date was ever disclosed; confidence medium on that one field), expanded `ownership_note`, bumped `last_verified`→2026-07-27 / `verify_after`→2026-10-27. Added a body section on what the deal means for the product: capabilities live on inside Mintlify, standalone product stays maintenance-mode, Mintlify is actively helping customers migrate away, **no sunset date announced**. Kept `website: https://www.helicone.ai` — the site is live, 200, no redirect, still sells, brand persists under Mintlify, so no rename. Cached `raw/sources/2026-07-27--helicone--mintlify-acquisition-closed.md`. `survey-v2.csv` has no Helicone row (checked) — no CSV change.
