---
title: SurePath AI
type: vendor
name: SurePath AI
slug: surepath-ai
aka: []
primary_category: ai-access-governance
also_listed_in: []
website: https://www.surepath.ai
founded: 2023
hq: Denver, Colorado, USA
ownership_state: acquired-closed
owner: F5
ownership_note: Acquired by [f5](f5.md) — announced 2026-06-22 as already completed alongside the F5 AI Security Platform launch; terms undisclosed. Cash paid inside F5 fiscal Q3 2026 per its GAAP cash-flow statement. Brand and standalone product both survive (unlike calypsoai)
acquisition: {announced: 2026-06-22, closed: 2026-06-22, price: undisclosed (~$47.6M cash net of cash acquired — inferred from F5 Q3 FY2026 cash flow; not itemized by F5)}
funding_total: $6.3M (pre-acquisition)
last_funding: $5.2M seed announced 2024-11-14 (Uncork Capital lead, Operator Collective)
market_position: null
deployment_model: [saas]
form_factor: [inline-proxy, platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: mid-to-large enterprise
last_verified: 2026-07-27
verify_after: 2026-08-10
tags: [acquired, f5, shadow-ai, ai-discovery, ai-access-governance]
---

# SurePath AI

> **Researched 2026-07-13; re-verified 2026-07-27.** Primary category: [ai-access-governance](../categories/ai-access-governance.md). **Acquired by [f5](f5.md)** — announced 2026-06-22 as already done, closed inside F5's fiscal Q3 2026. **The brand survives**: `surepath.ai` is live and still selling, with a "SurePath AI is now a part of F5" banner — the opposite of what happened to [calypsoai](calypsoai.md).

**One-liner** — A network-based shadow-AI discovery and workforce-GenAI governance platform (find every AI tool in use, classify intent, enforce inline policy), now the AI-discovery pillar of the F5 AI Security Platform but still sold under its own name.

## What it does
SurePath AI governs how employees use generative AI — the tools you build, adopt, or buy, including the ones nobody approved. Its distinguishing mechanism is **network-based discovery**: deployment via network redirects and out-of-band analysis rather than per-application integrations, so it sees sanctioned and unsanctioned AI use alike. On top of discovery it layers **intent classification** (what the user is trying to do, not just which domain they hit), inline risk mitigation (detects and redacts sensitive data in prompts, role-based access controls, policy-driven guardrails), audit trails of GenAI conversations, and a branded **enterprise GenAI portal** that gives employees a sanctioned front door to public and private models. F5 also credits it with tracing agent tool calls and MCP server connections — extending the visibility layer from human chat use to agentic workflows.

## Where it sits in the stack
Primary [ai-access-governance](../categories/ai-access-governance.md) (CASB-for-AI / shadow-AI): it governs the AI your people reach for, not the AI apps you build (that's [ai-runtime-security](../categories/ai-runtime-security.md)). Layer: model-prompt. It is exactly the category's "velvet rope" pattern — discovery of unsanctioned use plus intent-aware inline policy on what data flows to which model — with the added twist of a sanctioned-portal carrot alongside the enforcement stick.

## Deployment & architecture
Cloud SaaS (admin console at admin.surepath.ai) with enforcement via network redirects; discovery analysis runs out-of-band. The no-per-app-integration approach is the selling point versus API-integrated rivals: faster coverage of the long tail of AI-enabled SaaS, at the cost of the deeper in-app context an API integration can see. Whether prompt/conversation data leaves the customer tenancy (retention, training use) is unverified.

## Positioning & differentiators
- **Network-based, integration-free discovery** — coverage of shadow AI without waiting on connectors; F5 calls it a pioneer of network-based AI discovery.
- **Intent classification** — policy keyed to what the user is doing, not just the destination domain; same intent-aware pattern as [witnessai](witnessai.md).
- **Enable, not block** — the enterprise GenAI portal + request enrichment aim to convert shadow users into governed users, closer in spirit to [nudge-security](nudge-security.md) than to a pure blocker.
- **Agent/MCP visibility** (per F5) — traces agent tool calls and MCP server connections, a forward-looking angle most shadow-AI peers lack.

Nearest neighbors: [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [lanai](lanai.md), [wald-ai](wald-ai.md), [portal26](portal26.md), [nudge-security](nudge-security.md).

## Ownership, funding & M&A
Founded **2023**, HQ **Denver, Colorado**; founders Casey Bleeker (CEO) and Randy Birdsall. Raised a **$5.2M seed** (announced 2024-11-14, led by Uncork Capital with Operator Collective; **$6.3M total**). **Acquired by [f5](f5.md)**, announced **2026-06-22** simultaneously with the launch of the **F5 AI Security Platform**, where SurePath is the discovery/visibility layer feeding F5's guardrails and red-team products (the ex-[calypsoai](calypsoai.md) assets). **Terms undisclosed.**

**This is a separate, second F5 deal — not part of the CalypsoAI transaction.** Different targets, different years, different money: CalypsoAI (Dublin, AI runtime guardrails) closed 2025-09-26 for $145.2M cash in F5's fiscal 2025; SurePath (Denver, shadow-AI discovery) closed nine months later in F5's fiscal Q3 2026. The two are complementary rather than overlapping — SurePath finds the AI usage, CalypsoAI's technology tests and polices it — which is exactly how F5's platform narrative stacks them.

**On the close (announced ≠ closed, resolved here).** F5 published no completion notice and no separate closing date, and — unlike CalypsoAI — filed **no 8-K**; as of 2026-07-27 no F5 SEC filing mentions SurePath by name (EDGAR full-text search returns only SurePath's own 2024 Form D). The deal is nonetheless **closed**, on three converging pieces of evidence: (1) the 2026-06-22 release uses completed-transaction language throughout ("F5 acquires…", "The addition of SurePath AI powers…") with none of the "definitive agreement / subject to closing conditions" hedging F5 used during CalypsoAI's pending phase; (2) `surepath.ai` states "SurePath AI is now a part of F5"; and (3) F5's Q3 FY2026 earnings release shows **$47.619M** of "acquisition of businesses, net of cash acquired" for the nine months ended 2026-06-30 against **nil** for the six months ended 2026-03-31 — so acquisition cash actually moved inside the quarter 2026-04-01 → 2026-06-30, and SurePath is the only acquisition F5 announced in that window. The page therefore records **closed 2026-06-22**, the announcement date, since announce and close were effectively simultaneous.

That same arithmetic implies a purchase price of roughly **$47.6M in cash, net of cash acquired** — a plausible ~7.5× return on $6.3M of venture funding for a 3-year-old, ~20-person company. **F5 has not itemized this figure**, so it is an inference from F5's own GAAP cash flows, not a disclosed number; it is stated with that caveat and nothing more precise is claimed. F5's **Q3 FY2026 Form 10-Q** (period 2026-06-30) had not been filed as of 2026-07-27 — expect it in early August 2026, and re-check for a Note 4 business-combination disclosure with the exact date and purchase-price allocation. Confidence: high on the acquisition and on "closed"; medium on the price.

**Brand outcome differs sharply from CalypsoAI's.** F5's CTO Jimmy White said F5 will continue "to offer SurePath AI as an independent platform" alongside integrating its capabilities into the F5 Application Delivery and Security Platform (ADSP), and the observable evidence matches: `surepath.ai` is live (HTTP 200, no redirect), still SurePath-branded end to end, still taking demo requests, with `admin.surepath.ai` still the console. `calypsoai.com`, by contrast, 301-redirects to F5's AI Guardrails page and the CalypsoAI name is gone. Nor has SurePath been renamed into an F5 SKU: the F5 AI Security Platform page lists **AI discovery** as one of four pillars, but the only named products under it are **Guardrails** and **Red teaming** — there is no F5-branded "AI Discovery" product as of 2026-07-27.

## CTO / hedge-fund lens
Shadow-AI governance is a Day-1 concern for a fund (MNPI in consumer chatbots), and SurePath's integration-free network deployment suits a lean IT team. But the F5 acquisition changes the evaluation. You can still buy it standalone today — F5 says it will keep selling SurePath as an independent platform, and the site and console are unchanged — yet the direction of travel is clear: it is the visibility layer of the F5 AI Security Platform, and the independent-platform commitment carries no stated horizon (CalypsoAI's brand lasted about ten months). Price a multi-year commitment accordingly. Natural fit if you're already an F5 shop or want discovery + guardrails + red-team from one vendor; if not, the independent specialists ([harmonic-security](harmonic-security.md), [witnessai](witnessai.md), [aurascape](aurascape.md)) or your SASE vendor's AI-guard module are the comparators. Site claims finance-sector customers (unnamed) — fs_traction: claimed, not verified.

## Competitors / alternatives
[witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [nudge-security](nudge-security.md), [lanai](lanai.md), [cyberhaven](cyberhaven.md), [wald-ai](wald-ai.md), [portal26](portal26.md), [acuvity](acuvity.md) (the closest analogue — also discovery-led, also platform-acquired in 2026, by Proofpoint), [zscaler](zscaler.md) (AI Guard), [netskope](netskope.md) (Netskope One).

## Open questions / to verify
- ~~**Acquisition close date** — announced 2026-06-22; no completion notice found as of 2026-07-13.~~ **Resolved 2026-07-27: closed.** No separate completion date was ever published; announce and close were effectively simultaneous, and F5's cash-flow statement puts the payment inside the quarter ended 2026-06-30. Recorded as closed 2026-06-22.
- **Deal price** — undisclosed by F5. Inferred at **~$47.6M cash net of cash acquired** from F5's Q3 FY2026 cash-flow line; **not confirmed**. F5's Q3 FY2026 Form 10-Q was not yet filed as of 2026-07-27 — check EDGAR after **2026-08-10** for a Note 4 business-combination disclosure, and correct this page if the filing names a different figure or date. (Precedent: the 10-Q moved CalypsoAI's close date 12 days and its price by ~$35M versus the press narrative.)
- ~~Whether SurePath remains purchasable standalone or is absorbed into F5 AI Security Platform SKUs; brand survival.~~ **Resolved 2026-07-27 (provisionally): brand survives.** `surepath.ai` is live, unredirected and still selling; F5 says it will continue offering SurePath as an independent platform. Open sub-question: for how long, and whether it eventually becomes an "F5 AI Discovery" SKU — no such product exists yet.
- Data handling: does prompt/conversation capture leave the customer tenancy; retention and training-use policy.
- Depth of MCP/agent tracing (F5 marketing claim — no independent corroboration found).
- Certifications (SOC 2 etc.) and named FS customers.

## Sources
- [F5 Q3 FY2026 earnings release (Form 8-K Ex-99.1, SEC, filed 2026-07-27)](https://www.sec.gov/Archives/edgar/data/1048695/000104869526000063/ex991-q326earningsreleasef.htm) — fetched 2026-07-27 — supports: $47.619M "acquisition of businesses, net of cash acquired" for the nine months ended 2026-06-30, which against nil at the six-month mark places the close and the cash payment inside fiscal Q3 2026; confidence: high on the figure, med on attributing it to SurePath. Cached: `raw/sources/2026-07-27--surepath-ai--f5-close-evidence.md`
- [F5 Form 10-Q, FY2026 Q2 (SEC, filed 2026-05-05)](https://www.sec.gov/Archives/edgar/data/1048695/000104869526000051/ffiv-20260331.htm) — fetched 2026-07-27 — supports: nil acquisition cash in the six months ended 2026-03-31, the baseline for the arithmetic above; confidence: high (primary/SEC)
- [SurePath AI homepage banner](https://www.surepath.ai/) — fetched 2026-07-27 — supports: "SurePath AI is now a part of F5"; site live at HTTP 200 with no redirect and full SurePath branding intact; confidence: high
- [F5 AI Security Platform product page](https://www.f5.com/products/ai-security-platform) — fetched 2026-07-27 — supports: AI discovery is a platform pillar; only Guardrails and Red teaming are named products; no F5-branded AI Discovery SKU; confidence: high
- [F5 Acquires SurePath AI to Extend Reach of Cybersecurity Portfolio (Security Boulevard, 2026-06-22)](https://securityboulevard.com/2026/06/f5-acquires-surepath-ai-to-extend-reach-of-cybersecurity-portfolio/) — fetched 2026-07-27 — supports: F5 CTO Jimmy White on continuing to offer SurePath as an independent platform plus ADSP integration; deal described as done; confidence: med (trade press quoting a vendor exec)
- [F5 launches AI Security Platform (F5 press release, published 2026-06-22)](https://www.f5.com/company/news/press-releases/f5-ai-security-platform-control-enterprise-risk) — fetched 2026-07-13, re-fetched 2026-07-27 — supports: acquisition announced 2026-06-22 in completed-transaction language, terms undisclosed, no separate close date, network-based discovery + intent classification + MCP tracing description; confidence: high. Cached: `raw/sources/2026-07-13--surepath-ai--f5-acquisition-pr.md`
- [SurePath AI homepage](https://www.surepath.ai/) — fetched 2026-07-13 — supports: product capabilities, GenAI portal, target sectors, SaaS deployment; confidence: med (vendor marketing). Cached: `raw/sources/2026-07-13--surepath-ai--homepage.md`
- [SurePath AI announces over $5M in seed funding (PRNewswire)](https://www.prnewswire.com/news-releases/surepath-ai-announces-over-5-million-in-seed-funding-to-secure-genai-adoption-in-the-enterprise-302304040.html) — fetched 2026-07-13 — supports: $5.2M seed 2024-11-14, Uncork/Operator Collective, $6.3M total, Denver HQ, founded 2023, founders; confidence: med (company release, factual details). Cached: `raw/sources/2026-07-13--surepath-ai--seed-funding-pr.md`

## History
- [2026-07-27] URL audit found `surepath.ai` live (200, no redirect) with a "SurePath AI is now a part of F5" banner. Re-verified: status corrected **acquired-pending → acquired-closed** (closed 2026-06-22; F5 never published a separate completion date, and its Q3 FY2026 cash-flow statement shows the acquisition cash paid inside the quarter ended 2026-06-30). Added an inferred price of **~$47.6M cash net of cash acquired** (F5 has not itemized it; flagged as inference). Confirmed this is a **separate, second F5 deal**, unrelated to [calypsoai](calypsoai.md) (closed 2025-09-26, $145.2M, F5 fiscal 2025). Resolved the brand-survival question the opposite way from CalypsoAI: **SurePath brand and standalone product persist**; there is no F5 "AI Discovery" SKU. `verify_after` set to 2026-08-10 to check the Q3 FY2026 10-Q for a confirmed date and price.
- [2026-07-13] Page created via wiki-create (user-requested addition, not in seeds) and researched same day: categorized ai-access-governance; F5 acquisition announced 2026-06-22 flagged acquired-pending with verify_after 2026-10-01.
