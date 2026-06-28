---
type: vendor
name: Prompt Security
slug: prompt-security
categories: [dlp, ai-runtime-security, ai-spm, ai-access-governance]
layer: data
aliases: [Prompt, Prompt Security (SentinelOne)]
website: https://prompt.security
founded: 2023
hq: Tel Aviv, Israel
ownership: acquired
ownership_detail: "Acquired by SentinelOne — announced 2025-08-05, cash + stock, reported ~$250M, closed in SentinelOne fiscal Q3 FY2026. Now SentinelOne's GenAI security product."
ownership_confidence: high
funding_total: ~$23M (pre-acquisition)
last_funding: "Series A (Hetz Ventures, Jump Capital, Ridge Ventures; strategics Okta, F5)"
deployment: [inline-proxy, api, sdk, saas]
target_customer: enterprise / mid-market
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 3
last_updated: 2026-06-28
tags: [genai-security, ai-firewall, prompt-injection, shadow-ai, dlp, sentinelone]
---

# Prompt Security

> Primary category: [[dlp]]. Cross-listed in [[ai-runtime-security]], [[ai-spm]], and [[ai-access-governance]]. **Acquired by [[sentinelone]]** (2025).

**One-liner** — A GenAI security platform that gives enterprises visibility and control over employee and developer AI use — shadow-AI discovery, prompt-injection defense, and prompt/response DLP — now SentinelOne's AI-security product.

## What it does
Prompt Security inspects GenAI traffic in real time to enforce policy on both sides of the prompt: it blocks **prompt injection** and jailbreaks (untrusted input), redacts/prevents **sensitive-data leakage** into prompts and from responses (DLP), discovers **shadow AI** (which AI tools employees use), and governs AI agent behavior. Coverage spans browsers, desktop apps, and APIs, so it controls both workforce AI usage and homegrown AI applications.

## Where it sits in the stack
It straddles several layers, which is why it's cross-listed:
- [[dlp]] — prevents sensitive data leaving via prompts/responses (egress/sensitive-data legs).
- [[ai-runtime-security]] — inline AI firewall blocking prompt injection (untrusted-input leg).
- [[ai-access-governance]] — CASB-for-AI shadow-AI discovery and policy over sanctioned/unsanctioned tools.
- [[ai-spm]] — inventory/posture of AI usage and agents.
It lives in the yellow (AI application/usage) trust zone and addresses all three legs of the lethal trifecta.

## Deployment & architecture
Multi-channel enforcement: browser extension, desktop agent, and API/SDK/inline-proxy in front of models or AI gateways — i.e., it can govern SaaS AI usage and self-built apps without forcing all traffic through one network choke point. Integrates with IdP, SIEM/SOC, and AI gateways. Post-acquisition, capabilities are being integrated into [[sentinelone]] Singularity.

## Positioning & differentiators
- Known for broad coverage across the "shadow AI + AI firewall + AI DLP" trifecta in one product, rather than specializing in only red-teaming or only guardrails.
- Nearest neighbors: [[witnessai]], [[lasso-security]], [[harmonic-security]], [[aurascape]] (access governance); [[lakera]], [[pangea]], [[hiddenlayer]], [[prisma-airs]], [[cisco-ai-defense]] (runtime/guardrails).
- Strategic-investor signal: Okta and F5 backed it pre-acquisition.

## Ownership, funding & M&A
**Seed flag "acq by SentinelOne" — CONFIRMED.** [[sentinelone]] announced the acquisition 2025-08-05 (cash + stock; reported ~$250M per Calcalist, not officially disclosed), expected to close in fiscal Q3 FY2026; SentinelOne subsequently announced completion. Pre-acquisition: founded August 2023 in Tel Aviv by Itamar Golan (CEO) and Lior Drihem (CTO), both ex-Unit 8200; ~$23M raised (Hetz Ventures, Jump Capital, Ridge Ventures, plus strategics Okta and F5). A notable ~$250M outcome for a two-year-old company. Confidence: high on the acquisition; medium on price.

## CTO / hedge-fund lens
Day-1 for the AI-usage control problem: if employees are pasting into ChatGPT/Claude and you need shadow-AI visibility plus prompt DLP, this is exactly the control. Now that it's part of SentinelOne, it's most attractive to existing SentinelOne shops; others should still shortlist it but evaluate the platform-lock implications. Touches model-risk/data-governance posture but is not itself an SR 11-7 governance platform. Fits enterprise and mid-market.

## Competitors / alternatives
[[witnessai]], [[harmonic-security]], [[lasso-security]], [[aurascape]], [[wald-ai]], [[cyberhaven]] (access governance / AI DLP); [[lakera]], [[pangea]] (now CrowdStrike), [[prisma-airs]], [[cisco-ai-defense]], [[hiddenlayer]] (runtime/guardrails).

## Open questions / to verify
- Final purchase price (press-reported ~$250M) and confirmed close date.
- Whether it remains sold standalone or only within SentinelOne Singularity.

## Sources
- [SentinelOne to Acquire Prompt Security to Advance GenAI Security](https://www.sentinelone.com/press/sentinelone-to-acquire-prompt-security-to-advance-genai-security/) — fetched 2026-06-28 — supports: acquisition (2025-08-05), capabilities, fiscal Q3 close; confidence: high
- [SentinelOne buys Prompt for $250M (Calcalist)](https://www.calcalistech.com/ctechnews/article/im5ma59bu) — fetched 2026-06-28 — supports: ~$250M value, founded 2023, two years old; confidence: med
- [Prompt Security + SentinelOne: A New Chapter Begins (Prompt blog)](https://prompt.security/blog/prompt-security-sentinelone-a-new-chapter-begins) — fetched 2026-06-28 — supports: founders, Tel Aviv HQ, deal narrative; confidence: med (vendor)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by SentinelOne (announced 2025-08-05, ~$250M cash+stock, closed fiscal Q3 FY2026) — raised ownership_confidence to high. Established founded Aug 2023, HQ Tel Aviv, founders Golan/Drihem, ~$23M raised (incl. Okta, F5). Kept the four cross-listed categories. Set hedge_fund_fit high.
