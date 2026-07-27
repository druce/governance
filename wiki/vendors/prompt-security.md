---
title: Prompt Security
type: vendor
name: Prompt Security
slug: prompt-security
aka: [Prompt, Prompt Security (SentinelOne)]
primary_category: dlp
also_listed_in: [ai-runtime-security, ai-spm, ai-access-governance]
website: https://prompt.security
founded: 2023
hq: Tel Aviv, Israel
ownership_state: acquired-closed
owner: SentinelOne
ownership_note: 'Acquired by SentinelOne (NYSE: S) — announced 2025-08-05, completed 2025-09-05 (per SentinelOne Form 8-K filed 2025-09-08 and Q3 FY2026 10-Q Note 4). Cash + Class A stock; ~$180M deal value per the 8-K, $159.3M booked as GAAP purchase consideration. Now SentinelOne''s GenAI security product.'
acquisition: {announced: 2025-08-05, closed: 2025-09-05, price: '~$180M cash + stock (8-K); $159.3M GAAP purchase consideration (10-Q Note 4)'}
funding_total: ~$23M (pre-acquisition)
last_funding: Series A (Hetz Ventures, Jump Capital, Ridge Ventures; strategics Okta, F5)
market_position: null
deployment_model: [saas]
form_factor: [inline-proxy, api, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / mid-market
last_verified: 2026-07-27
verify_after: null
tags: [genai-security, ai-firewall, prompt-injection, shadow-ai, dlp, sentinelone]
---

# Prompt Security

> Primary category: [dlp](../categories/dlp.md). Cross-listed in [ai-runtime-security](../categories/ai-runtime-security.md), [ai-spm](../categories/ai-spm.md), and [ai-access-governance](../categories/ai-access-governance.md). **Acquired by [sentinelone](sentinelone.md)** (2025).

**One-liner** — A GenAI security platform that gives enterprises visibility and control over employee and developer AI use — shadow-AI discovery, prompt-injection defense, and prompt/response DLP — now SentinelOne's AI-security product.

## What it does
Prompt Security inspects GenAI traffic in real time to enforce policy on both sides of the prompt: it blocks **prompt injection** and jailbreaks (untrusted input), redacts/prevents **sensitive-data leakage** into prompts and from responses (DLP), discovers **shadow AI** (which AI tools employees use), and governs AI agent behavior. Coverage spans browsers, desktop apps, and APIs, so it controls both workforce AI usage and homegrown AI applications.

## Where it sits in the stack
It straddles several layers, which is why it's cross-listed:
- [dlp](../categories/dlp.md) — prevents sensitive data leaving via prompts/responses.
- [ai-runtime-security](../categories/ai-runtime-security.md) — inline AI firewall blocking prompt injection.
- [ai-access-governance](../categories/ai-access-governance.md) — CASB-for-AI shadow-AI discovery and policy over sanctioned/unsanctioned tools.
- [ai-spm](../categories/ai-spm.md) — inventory/posture of AI usage and agents.
It lives in the yellow (AI application/usage) trust zone, screening untrusted input, preventing sensitive-data leakage, and controlling outbound data flows.

## Deployment & architecture
Multi-channel enforcement: browser extension, desktop agent, and API/SDK/inline-proxy in front of models or AI gateways — i.e., it can govern SaaS AI usage and self-built apps without forcing all traffic through one network choke point. Integrates with IdP, SIEM/SOC, and AI gateways. Post-acquisition, capabilities are being integrated into [sentinelone](sentinelone.md) Singularity.

## Positioning & differentiators
- Known for broad coverage across the "shadow AI + AI firewall + AI DLP" combination in one product, rather than specializing in only red-teaming or only guardrails.
- Nearest neighbors: [witnessai](witnessai.md), [lasso-security](lasso-security.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md) (access governance); [lakera](lakera.md), [pangea](pangea.md), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md) (runtime/guardrails).
- Strategic-investor signal: Okta and F5 backed it pre-acquisition.

## Ownership, funding & M&A
**Seed flag "acq by SentinelOne" — CONFIRMED and closed.** [sentinelone](sentinelone.md) signed the merger agreement and announced the deal on 2025-08-05, and **completed it on 2025-09-05** — confirmed twice in SentinelOne's own SEC filings (Form 8-K filed 2025-09-08: the acquisition "was completed on September 5, 2025"; Q3 FY2026 Form 10-Q Note 4 repeats the same date). The announcement-day release was explicit that the deal was still pending, "subject to any applicable regulatory approvals and customary closing conditions," so the two dates are genuinely a month apart.

On price, three numbers circulate and only two are sourced to SentinelOne: **~$180M** (cash + Class A stock) is the deal value in the 8-K, and **$159.3M** is the GAAP purchase consideration in the 10-Q's purchase-price allocation ($133.6M cash + $17.2M stock + $0.9M assumed options + $7.6M indemnity holdback), with the gap treated as post-combination compensation. The widely repeated **~$250M** is a Calcalist/CTech press estimate that appears in no SentinelOne filing or release — treat it as unconfirmed. PPA also shows goodwill of $130.4M and $21.6M of intangibles ($20.0M developed technology, $1.6M customer relationships, both 2-year lives).

Pre-acquisition: founded August 2023 in Tel Aviv by Itamar Golan (CEO) and Lior Drihem (CTO), both ex-Unit 8200; ~$23M raised (Hetz Ventures, Jump Capital, Ridge Ventures, plus strategics Okta and F5) — a strong outcome for a two-year-old company. Confidence: high on the acquisition, dates and filed price figures.

> Don't conflate this with SentinelOne's **Observo, Inc.** deal, signed 2025-09-08 and completed 2025-09-22 (~$225M per 8-K) — a separate acquisition in the same fiscal quarter.

## CTO / hedge-fund lens
Day-1 for the AI-usage control problem: if employees are pasting into ChatGPT/Claude and you need shadow-AI visibility plus prompt DLP, this is exactly the control. Now that it's part of SentinelOne, it's most attractive to existing SentinelOne shops; others should still shortlist it but evaluate the platform-lock implications. Touches model-risk/data-governance posture but is not itself an SR 11-7 governance platform. Fits enterprise and mid-market.

## Competitors / alternatives
[witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [lasso-security](lasso-security.md), [aurascape](aurascape.md), [wald-ai](wald-ai.md), [cyberhaven](cyberhaven.md) (access governance / AI DLP); [lakera](lakera.md), [pangea](pangea.md) (now CrowdStrike), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [hiddenlayer](hiddenlayer.md) (runtime/guardrails).

## Open questions / to verify
- ~~Final purchase price and confirmed close date~~ — **RESOLVED 2026-07-27**: closed 2025-09-05; ~$180M deal value / $159.3M GAAP purchase consideration per SentinelOne's 8-K and 10-Q. The ~$250M press figure is unsupported by any filing.
- Whether it remains sold standalone or only within SentinelOne Singularity.

## Sources
- [SentinelOne Form 8-K (filed 2025-09-08)](https://www.sec.gov/Archives/edgar/data/1583708/000110465925088079/tm2525181d1_8k.htm) — fetched 2026-07-27 — supports: **close date 2025-09-05** ("completed on September 5, 2025"), merger agreement dated 2025-08-05, ~$180M cash + Class A stock deal value; confidence: high (primary). Cached: `raw/sources/2026-07-27--prompt-security--sentinelone-close-date.md`
- [SentinelOne Form 10-Q, quarter ended 2025-10-31](https://www.sec.gov/Archives/edgar/data/1583708/000158370825000159/s-20251031.htm) (filed 2025-12-04), Note 4 *Acquisitions* — fetched 2026-07-27 — supports: close date 2025-09-05 (independent corroboration), $159.3M purchase consideration breakdown, goodwill $130.4M, intangibles $21.6M; also separates the Observo deal (closed 2025-09-22) from Prompt; confidence: high (primary)
- [SentinelOne to Acquire Prompt Security to Advance GenAI Security](https://www.sentinelone.com/press/sentinelone-to-acquire-prompt-security-to-advance-genai-security/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: announcement date 2025-08-05, capabilities, and explicit pending language ("expected to close in ... third quarter of fiscal year 2026 ... subject to ... customary closing conditions"); confidence: high
- [SentinelOne buys Prompt for $250M (Calcalist)](https://www.calcalistech.com/ctechnews/article/im5ma59bu) — fetched 2026-06-28 — supports: founded 2023, two years old; the ~$250M value is a **press estimate contradicted by SentinelOne's filings** (see 8-K/10-Q above) — do not cite it as fact; confidence: low on price, med otherwise
- [Prompt Security + SentinelOne: A New Chapter Begins (Prompt blog)](https://prompt.security/blog/prompt-security-sentinelone-a-new-chapter-begins) — fetched 2026-06-28 — supports: founders, Tel Aviv HQ, deal narrative; confidence: med (vendor)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by SentinelOne (announced 2025-08-05, ~$250M cash+stock, closed fiscal Q3 FY2026) — raised ownership_confidence to high. Established founded Aug 2023, HQ Tel Aviv, founders Golan/Drihem, ~$23M raised (incl. Okta, F5). Kept the four cross-listed categories. Set hedge_fund_fit high.
- [2026-07-27] Date-sanity sweep — **corrected a fabricated close date**. `closed` was 2025-08-05, an exact copy of the announcement date, which the page's own `ownership_note` contradicted by saying the deal "closed in SentinelOne fiscal Q3 FY2026" (a quarter ending 2025-10-31). Checked SentinelOne's SEC filings: the Form 8-K filed 2025-09-08 states the acquisition "was completed on September 5, 2025", and the Q3 FY2026 10-Q Note 4 independently repeats that date — so the real close is **2025-09-05**, one month after announcement. Also replaced the null `price` with the two filed figures (~$180M deal value per the 8-K; $159.3M GAAP purchase consideration per the 10-Q PPA) and demoted the ~$250M Calcalist number to an explicitly unconfirmed press estimate, since it appears in no SentinelOne filing or release. `ownership_state: acquired-closed` confirmed correct and now genuinely sourced. Added a note distinguishing the separate Observo deal (closed 2025-09-22) that fell in the same quarter. Cached 1 new source.
