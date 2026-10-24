---
title: Lakera
type: vendor
name: Lakera
slug: lakera
aka: [Lakera AI, Lakera Guard]
primary_category: ai-runtime-security
also_listed_in: [ai-red-teaming]
website: https://www.lakera.ai
founded: 2021
hq: Zurich, Switzerland (and San Francisco, USA)
ownership_state: acquired-closed
owner: Check Point Software
ownership_note: 'Acquired by Check Point Software (NASDAQ: CHKP) — announced 2025-09-16, closed 2025-10-22 for ~$201.8M total consideration per Check Point''s FY2025 20-F (press reported ~$300M at announcement). All shares of Lakera AI AG; anchors Check Point''s Global Center of Excellence for AI Security. Lakera brand still live at lakera.ai as of 2026-07-27, but the 20-F assigns the trademark a 1-year useful life'
acquisition: {announced: 2025-09-16, closed: 2025-10-22, price: ~$201.8M total consideration (press reported ~$300M)}
funding_total: ~$30M
last_funding: $20M Series A — July 2024 (led by Atomico; Citi Ventures, Dropbox, redalpine)
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [acquired, check-point, ai-firewall, prompt-injection, gandalf, red-teaming]
sources:
  - {claim: "Check Point completed the acquisition of all outstanding shares of Lakera AI AG on 2025-10-22 for total consideration of approximately $201.8M", url: "https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm", date: 2026-07-27, confidence: high}
  - {claim: "Lakera brand still live — lakera.ai returns 200 with no redirect and the original title, but the footer reads '©1994-2026 Check Point Software Technologies Ltd.'", url: "https://www.lakera.ai/", date: 2026-07-27, confidence: high}
---

# Lakera

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [Check Point Software](check-point.md) (NASDAQ: CHKP) — closed 2025-10-22** for ~$201.8M. The **Lakera brand is still live** (lakera.ai loads unchanged, with a Check Point copyright footer), so it remains buyable under its own name — but as a Check Point product line, not an independent vendor.

**One-liner** — The AI-native runtime-security pure-play of "Gandalf" fame (real-time prompt-injection / GenAI defense), now Check Point's AI-security engine and the foundation of its Global Center of Excellence for AI Security.

## What it does
Lakera protects LLMs, GenAI apps and autonomous/agentic systems at runtime. Its core product, **Lakera Guard**, screens inputs and outputs in real time against prompt injection, jailbreaks, data leakage, and model manipulation across multiple AI frameworks. Its threat intelligence is fed partly by **Gandalf**, a viral prompt-injection education game (>1M players; >50M data points) used even by Microsoft for security training. Lakera also does AI red teaming.

## Where it sits in the stack
Primary [ai-runtime-security](../categories/ai-runtime-security.md) (inline AI firewall / guardrails) with a secondary [ai-red-teaming](../categories/ai-red-teaming.md) tag. Layer: model-prompt. Lethal-trifecta role: strongest on **untrusted input** (it is the best-known prompt-injection defender) and **sensitive data** (output/data-leak screening). Sits at the green↔red boundary in front of model endpoints.

## Deployment & architecture
SaaS and self-hosted; primarily **API-based** (low-latency guardrail calls around model requests) plus SDK integration — model- and cloud-agnostic. Post-close, Lakera combines with Check Point Infinity / GenAI Protect and forms the foundation of Check Point's **Global Center of Excellence for AI Security**. Integrations: AI gateways, the app's LLM pipeline, SIEM.

## Positioning & differentiators
Lakera is the category's best-known **prompt-injection** specialist, with a research-and-community moat (Gandalf, an open prompt-injection dataset) and a lightweight API-first guardrail rather than a heavy inline proxy. Founders came from Google/Meta AI.

**Since 2025-10-22, read that positioning as a platform vendor's, not a pure-play's.** Lakera is no longer an independent, model-neutral third party you can buy without a relationship to a network-security incumbent; it is how Check Point competes in AI security. That moves it out of the "best-of-breed specialist" bucket and into the same bucket as [prisma-airs](prisma-airs.md) (Palo Alto), [cisco-ai-defense](cisco-ai-defense.md) (Cisco), F5's [calypsoai](calypsoai.md), Cato's [aim-security](aim-security.md) and SentinelOne's [prompt-security](prompt-security.md) — the 2025 wave in which nearly every major network/security platform bought its AI guardrail rather than building one. What survives the deal is the technical differentiation (the prompt-injection research and Gandalf-fed threat intel are genuinely ahead of most of that peer group); what does not survive is the neutrality argument.

Alternatives still independent as of this page's last check, if vendor-neutrality is a requirement: [witnessai](witnessai.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [hiddenlayer](hiddenlayer.md). The pure-play population in this category is thinning fast; assume any name on that list can be acquired inside a buying cycle.

## Ownership, funding & M&A
Founded **2021** by David Haber (CEO), Dr. Mateo Rojas-Carulla and Dr. Matthias Kraft; dual HQ **Zurich + San Francisco**. Funding **~$30M total**, headlined by a **$20M Series A (July 2024)** led by Atomico (Citi Ventures, Dropbox, redalpine).

**Acquired by Check Point Software** (NASDAQ: CHKP). Announced **2025-09-16**; **closed 2025-10-22** — Check Point "completed the acquisition of all outstanding shares of Lakera AI AG," per Note 3 of its audited **FY2025 Form 20-F**. Sign-to-close was 36 days. **Confidence: high** (issuer's own audited SEC filing, not press).

**Price: ~$201.8M total consideration**, also from the 20-F. This is materially below the **~$300M** that press (Calcalist and downstream coverage) reported at announcement and that this page previously carried. The two are not necessarily in conflict — accounting "total consideration" excludes amounts that must be expensed as post-close compensation, and retention/earn-out packages are routinely folded into the number journalists are briefed on — but **no primary source itemizes the ~$100M gap**, so treat $201.8M as the authoritative purchase price and ~$300M as an unofficial figure of uncertain composition.

> Contradiction (soft / scope-mismatch): audited total consideration $201.8M (Check Point 20-F, FY2025) vs. ~$300M reported at announcement (Calcalist). Different measures, most likely purchase price vs. purchase price plus retention. Noted 2026-07-27; using the filed figure.

The purchase price allocation is worth reading, because it telegraphs intent: **goodwill is $150.1M — 74% of the price** — "primarily attributed to synergies," i.e. this was bought for technology and team fit, not for Lakera's revenue. Core technology got a **7-year** useful life, but the **Lakera trademark and its customer relationships were each assigned a 1-year** useful life. Check Point's own accounting assumption is that the brand and the standalone customer base have about a year of remaining value from October 2025, while the engine has seven — the standard fingerprint of a plan to absorb the product and retire the standalone identity. (The useful lives are filing facts; the read on intent is ours.)

## Brand status (checked 2026-07-27)
`lakera.ai` returns **200 with no redirect** to checkpoint.com, and the page title is still "Lakera: The AI-Native Security Platform to Accelerate GenAI" — independent-vendor marketing, no Check Point co-branding above the fold. The tell is the footer: **"©1994-2026 Check Point Software Technologies Ltd."** — 1994 is Check Point's founding year, three decades before Lakera existed, so that copyright line is the parent's boilerplate on a property it owns. So: **ownership changed 2025-10-22, the marketing site has not.** The wiki keeps `lakera` as the slug and `lakera.ai` as the website, and the survey keeps "Lakera (Check Point)" as the option. Given the 1-year trademark life in the 20-F, expect this to need re-checking inside a year.

## CTO / hedge-fund lens
Day-1 control type — a runtime AI firewall focused on prompt injection is a baseline control for any shop exposing LLMs to untrusted input. Lakera's API-first model suits teams that want guardrails in code without standing up an inline proxy. Indirect SR 11-7 relevance (control + red-team evidence).

Post-close, the practical questions are commercial rather than technical:

- **You are now buying from Check Point.** Procurement, contracting, support escalation and roadmap influence run through a large public platform vendor (NASDAQ: CHKP, ~$678M of revenue in Q3 2025 alone). If you are already a Check Point shop, that is a simplification and you should ask about bundling into your Infinity agreement. If you are not, you are opening a vendor relationship with a network-security incumbent to get a guardrail API — weigh that against a still-independent alternative.
- **Standalone availability is not yet in doubt, but is not guaranteed either.** The product is still sold under its own brand and site as of 2026-07-27. But Check Point amortizes the trademark and the acquired customer relationships over one year, which is what a company does when it expects the standalone line to be substantially absorbed. Contract accordingly: ask for multi-year pricing, renewal protection, and written commitment on continued availability of the standalone API rather than assuming today's packaging persists.
- **The technology risk is low and the counterparty risk went down.** Unlike an acqui-hire, this was a $201.8M cash purchase of a product line with a 7-year technology life and a Center-of-Excellence mandate — Check Point intends to invest in the engine. For a fund, the acquisition arguably *reduces* the "will this startup exist in three years" concern that applies to the remaining pure-plays.

Still a good fit for funds building their own LLM apps/agents; just diligence it as a Check Point product with a legacy brand, not as a Swiss startup.

## Competitors / alternatives
[prompt-security](prompt-security.md), [calypsoai](calypsoai.md), [witnessai](witnessai.md), [aim-security](aim-security.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [hiddenlayer](hiddenlayer.md).

## Open questions / to verify
- ~~Confirm the deal closed~~ — **resolved 2026-07-27**: closed 2025-10-22 per Check Point's FY2025 20-F.
- ~~Official deal value~~ — **resolved 2026-07-27**: ~$201.8M total consideration per the 20-F. Still open: what the ~$100M gap to the reported ~$300M consists of (presumed retention/earn-out, unconfirmed).
- **How long the Lakera brand survives.** Site is unchanged as of 2026-07-27, but the 20-F assigns the trademark a 1-year useful life. Re-check for a rebrand to a Check Point product name.
- Whether Lakera Guard remains purchasable **standalone**, outside a Check Point Infinity agreement, and at what packaging/pricing.
- Whether the founders (David Haber et al.) are still at Check Point running the Global Center of Excellence for AI Security.

## Sources
- [Check Point Software Technologies Ltd., Form 20-F for FY2025 (SEC), Note 3: Acquisitions (f)](https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm) — filed 2026-03-31, fetched 2026-07-27 — supports: **close date 2025-10-22**, "completed the acquisition of all outstanding shares of Lakera AI AG", **total consideration ~$201.8M**, purchase price allocation (goodwill $150.1M; core technology $44.0M / 7 yrs; customer relationships $4.4M / 1 yr; trademark $0.3M / 1 yr); confidence: high (audited issuer filing)
- [Check Point Q3 2025 results, Form 6-K (SEC)](https://www.sec.gov/Archives/edgar/data/1015922/000117891325003565/2533887.htm) — filed 2025-10-28, fetched 2026-07-27 — supports: CEO Nadav Zafrir framing Lakera as advancing the "AI First strategy"; Q3 2025 revenue $678M; confidence: high
- [lakera.ai homepage](https://www.lakera.ai/) — fetched 2026-07-27 — supports: brand still live (HTTP 200, no redirect, original title) with a "©1994-2026 Check Point Software Technologies Ltd." footer; confidence: high
- [Check Point Acquires Lakera… (Check Point press release)](https://www.checkpoint.com/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/) — fetched 2026-06-28 — supports: 2025-09-16 announce, founders, founding 2021, Zurich/SF HQ, Center of Excellence integration, then-expected Q4 2025 close; confidence: high
- [Lakera raises $20M Series A (TechCrunch)](https://techcrunch.com/2024/07/24/lakera-which-protects-enterprises-from-llm-vulnerabilities-raises-20m/) — fetched 2026-06-28 — supports: $20M Series A, ~$30M total, Atomico lead, Gandalf; confidence: high
- [Check Point acquires Lakera in $300 million deal (Calcalist)](https://www.calcalistech.com/ctechnews/article/rj5bc1vige) — fetched 2026-06-28 — supports: the ~$300M figure reported at announcement; confidence: low-med (superseded on price by the 20-F's $201.8M; retained to document the discrepancy)
- Cached: `raw/sources/2026-07-27--lakera--checkpoint-20f-close-date-and-price.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by Check Point Software** (announced 2025-09-16, ~$300M reported, expected close Q4 2025). Seed flag verified. Filled founding (2021), Zurich/SF HQ, founders, ~$30M funding, Gandalf/prompt-injection positioning. Confidence high (close pending per release).
- [2026-07-27] **Deal closed — `acquired-pending` → `acquired-closed`.** URL audit found lakera.ai live and unchanged under the Lakera brand but carrying a "©1994-2026 Check Point Software Technologies Ltd." footer. Went to the acquirer's SEC filings rather than press: Check Point's audited **FY2025 Form 20-F** (Note 3(f)) states it "completed the acquisition of all outstanding shares of Lakera AI AG" on **2025-10-22** for **total consideration of approximately $201.8M** — correcting both the null close date and the ~$300M press price this page had carried. Recorded the price discrepancy as a soft/scope-mismatch contradiction (audited consideration vs. a press figure that likely includes retention). Added the purchase price allocation and the signal in it: 74% goodwill, 7-year technology life but **1-year** trademark and customer-relationship lives. Kept `website: https://www.lakera.ai` and the `lakera` slug — brand persists, no rename. Rewrote positioning (Lakera is now a platform vendor's product, grouped with prisma-airs / cisco-ai-defense / calypsoai / aim-security / prompt-security, not with the remaining pure-plays) and the CTO lens (buy-from-Check-Point implications, contracting advice, standalone-availability risk). `verify_after` cleared; new open questions on brand survival and standalone packaging.
- [2026-10-23] Linked parent page [check-point](check-point.md) (created 2026-10-23). Check Point's Q4/FY2025 results release gives ~$190M *net cash* consideration vs the 20-F's ~$201.8M *total* consideration; different measures, no change to page figures.
