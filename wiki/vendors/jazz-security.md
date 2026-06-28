---
title: Jazz Security
type: vendor
name: Jazz Security
slug: jazz-security
categories: [dlp]
layer: data
aliases: [Jazz]
website: "https://www.jazz.security"
founded: 2024
hq: Tel Aviv, Israel (US presence in New York)
ownership: independent
ownership_detail: VC-backed; $61M combined seed ($18M) + Series A ($43M), led by Glilot Capital Partners and Team8 (announced ~2026-03).
ownership_confidence: high
funding_total: ~$61M
last_funding: Series A $43M (2026-03; combined $61M seed+A)
deployment: [saas, on-prem]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [dlp, ai-native-dlp, data-loss-prevention, agentic-investigator]
---

# Jazz Security

> **Category correction.** The seed registry tagged Jazz under [ai-soc-analysts](../categories/ai-soc-analysts.md) + [siem-soc](../categories/siem-soc.md). Primary research shows Jazz is an **AI-native Data Loss Prevention (DLP)** product, not an agentic-SOC analyst. Reclassified primary to [dlp](../categories/dlp.md). The SOC adjacency is real but narrow: its "Agentic Investigator" triages DLP alerts, not general security alerts. Soft mismatch flagged 2026-06-28.

**One-liner** — An AI-native DLP platform that uses an autonomous "Agentic Investigator" to read intent and context, so data-loss alerts come with answers instead of rule-based noise.

**What it does** — Jazz replaces rigid, regex/rule-driven DLP with a forensic endpoint agent that watches how data is actually used, plus an autonomous Agentic Investigator that judges intent and context to decide whether a given data movement is risky. The pitch: traditional DLP buries teams in false positives while real leaks slip through; Jazz aims to cut the noise and surface genuine exfiltration/insider risk. Relevant to AI because it targets data leaving via modern workflows — including paste-into-chatbot and other AI egress paths.

**Where it sits in the stack** — [dlp](../categories/dlp.md) in the Data layer; adjacent to [ai-access-governance](../categories/ai-access-governance.md) (shadow-AI / data-into-LLM egress) and to [data-access-governance](../categories/data-access-governance.md). Lethal-trifecta role: it controls **sensitive-data** exposure and **egress** (data leaving to untrusted destinations). Lives at the endpoint/data boundary, the yellow-zone control point.

**Deployment & architecture** — Endpoint-agent architecture (forensic agent for data-usage visibility) with SaaS analysis backend. Endpoint-based control rather than inline network proxy.

**Positioning & differentiators** — Founded 2024 in Tel Aviv by Israeli intelligence veterans; CEO/co-founder Ido Livneh. Differentiates on "AI-native, context-and-intent" DLP vs. legacy rule-based DLP. Nearest neighbors: [cyberhaven](cyberhaven.md), [mind](mind.md), [nightfall-ai](nightfall-ai.md), and (for the AI-egress overlap) [prompt-security](prompt-security.md) / [lasso-security](lasso-security.md).

**Ownership, funding & M&A** — Independent, VC-backed. $61M total = $18M seed + $43M Series A, led by Glilot Capital Partners and Team8, with Encoded Ventures, MassMutual Ventures, Merlin Ventures, Ten Eleven Ventures and angels; emerged from stealth ~March 2026. No M&A; no seed acquisition flag. Confidence high on independence.

**CTO / hedge-fund lens** — **Day-1-ish for the data layer** (DLP is table-stakes for a regulated shop), but Jazz itself is a brand-new (2026 stealth exit) challenger — evaluate maturity vs. incumbents you may already own ([microsoft-purview](microsoft-purview.md) DLP, [forcepoint](forcepoint.md), [netskope](netskope.md)). The intent-aware angle is attractive for catching MNPI/sensitive-data exfil and AI-paste leakage with fewer false positives, which is a real hedge-fund pain. Diligence the endpoint agent's footprint and the autonomy of its investigator. Not an SR 11-7 item; it's a data-control.

**Competitors / alternatives** — [cyberhaven](cyberhaven.md), [mind](mind.md), [nightfall-ai](nightfall-ai.md), [prompt-security](prompt-security.md), [lasso-security](lasso-security.md), plus incumbent DLP in [microsoft-purview](microsoft-purview.md) / [netskope](netskope.md) / [forcepoint](forcepoint.md).

**Open questions / to verify** — Exact HQ split (Tel Aviv vs NY); GA/maturity status; whether it does network/cloud DLP or endpoint-only; how the Agentic Investigator handles false-negatives on real exfil.

## Sources
- [Jazz Emerges From Stealth With $61M for AI-Powered DLP (SecurityWeek)](https://www.securityweek.com/jazz-emerges-from-stealth-with-61m-in-funding-for-ai-powered-dlp/) — fetched 2026-06-28 — supports: DLP positioning, $61M funding, founders, agentic investigator; confidence: med.
- [Cyber startup Jazz raises $43M Series A (Calcalist)](https://www.calcalistech.com/ctechnews/article/b1hpyc6f11e) — fetched 2026-06-28 — supports: Series A amount, Tel Aviv founding, AI-era data-leak focus; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Jazz is an AI-native DLP company (NOT agentic-SOC), founded 2024 Tel Aviv, CEO Ido Livneh, $61M (seed+A) led by Glilot/Team8, independent. **Reclassified primary category from ai-soc-analysts/siem-soc to dlp; layer foundation→data; trifecta none→[sensitive-data, egress].** Soft category mismatch flagged. ownership_confidence high.
