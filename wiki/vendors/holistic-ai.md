---
type: vendor
name: Holistic AI
slug: holistic-ai
categories: [ai-governance-platform]
layer: governance
aliases: [Holistic AI Limited]
website: https://www.holisticai.com
founded: 2020
hq: London, UK (US presence in Palo Alto, CA)
ownership: independent
ownership_detail: Private, VC-backed. Investors include Tola Capital, Mozilla Ventures (Mar 2024), Premji Invest, Innovate UK, Microsoft for Startups. No acquisition found.
ownership_confidence: medium
funding_total: "~$35M reported (uncertain — see note)"
last_funding: Venture round reported May 2024 (~$35M, low confidence); Mozilla Ventures investment Mar 2024
deployment: [saas, api]
target_customer: enterprise / regulated (Fortune 500, government, also SMEs)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 5
last_updated: 2026-06-28
tags: [ai-governance, model-risk, bias-audit, eu-ai-act, nist-ai-rmf, iso-42001, nyc-ll144]
---

# Holistic AI

**One-liner** — An AI governance, risk and compliance (AI GRC) platform that inventories an
organization's AI systems, runs technical risk/bias tests, and maps them to regulations
(EU AI Act, NIST AI RMF, ISO 42001, NYC Local Law 144); known originally for independent
bias audits of hiring algorithms.

**Categories** — [ai-governance-platform](../categories/ai-governance-platform.md)

## What it does

Holistic AI is an end-to-end **AI governance platform**. It does three jobs: (1) **discover and
inventory** AI systems across cloud, code repos and SaaS (to surface "shadow AI"); (2) **assess
risk** with a library of technical tests for bias, robustness/safety, security and performance;
and (3) **map and enforce compliance** against regulatory frameworks with control-mapping, gap
analysis, reporting and approval workflows. The company started in the **algorithmic audit**
niche — it is one of the recognized firms (alongside BABL AI, Conductor AI) that performs
independent **bias audits of Automated Employment Decision Tools (AEDTs)** to satisfy **NYC
Local Law 144**, producing the public "Summary of Results" and fairness impact ratios that law
requires. It has since broadened into a full governance/registry platform.

## Where it sits in the stack

This is a **[ai-governance-platform](../categories/ai-governance-platform.md)** play at the **governance layer** — the system-of-record
and policy/oversight tier that sits *above* the runtime data path, not in it. Its job is
inventory, documentation, risk assessment, attestation and regulatory mapping, not inline
traffic inspection.

- **Lethal-trifecta role:** **none directly.** Holistic AI does not break the untrusted-input,
  sensitive-data, or egress legs at runtime — it is an oversight/registry layer. (Its newer
  "Guardian Agents" / AI Safeguard runtime features edge toward monitoring, but the core product
  is governance, not a firewall.)
- **Trust zone:** spans the governance plane across all zones; it documents and risk-rates
  systems wherever they run rather than enforcing a boundary between red/yellow/green.

## Deployment & architecture

SaaS platform with connectors/integrations into cloud and dev tooling (AWS, Azure, GitHub,
Databricks; "20+ integrations" per vendor) for automated discovery, plus an API. Bias-audit
engagements are delivered as a service with results hosted on a dashboard and a public summary
page. Deployment specifics (e.g., self-hosted/on-prem options) are not clearly documented
publicly — treat as SaaS-first.

## Positioning & differentiators

Holistic AI's distinguishing angle is **regulatory/audit depth**: it grew out of academic
algorithm-auditing work at UCL and leans on standards credibility (its solutions appear in the
**OECD Trustworthy AI Toolkit**; it claims Observer Status with the **Council of Europe
Committee on AI** — vendor claim). Versus its neighbors:

- **[credo-ai](credo-ai.md)** — closest competitor; both are governance/registry + framework-mapping
  platforms. Credo AI is more policy/governance-workflow led; Holistic AI carries more
  technical-testing and formal-audit heritage.
- **[modelop](modelop.md)** — more focused on **operational model governance / ModelOps** for production
  model fleets (closer to SR 11-7 model inventory and monitoring in banks).
- **[ibm-watsonx-governance](ibm-watsonx-governance.md)** — incumbent/stack play bundled with IBM's AI platform; heavier,
  enterprise-IT anchored.
- **[monitaur](monitaur.md)** — model-risk/assurance focused, strong in insurance/regulated ML.
- **[fairly-ai](fairly-ai.md)** — overlapping AI GRC / compliance-automation focus, smaller.

Holistic AI's bias-audit lineage makes it relatively strong on **fairness/EEO** use cases
(hiring) where others are thinner.

## Ownership, funding & M&A

- **Ownership:** independent, private, VC-backed. No acquisition of the company was found.
  Confidence: **medium** (multiple sources agree it remains independent; Tracxn states no M&A).
- **Founded:** 2020, out of University College London, by **Emre Kazim** and **Adriano Soares
  Koshiyama** (co-CEOs). HQ **London**, with US presence in Palo Alto.
- **Investors:** Tola Capital, **Mozilla Ventures** (investment announced **2024-03-18**),
  Premji Invest, Innovate UK, Microsoft for Startups Pegasus Program, Kickstart Accelerator.
- **Funding total:** **uncertain.** A figure of ~$35M (venture, ~May 2024) is repeated by data
  aggregators, but that date collides with unrelated news and is **low confidence**. Earlier
  Innovate UK grant of ~£596,670 for an AI risk-management platform is documented.

> **Name-collision caution (not a contradiction):** A separate, unrelated **Paris-based AGI
> startup originally called "Holistic"/"Holistic AI" rebranded to "H"** and raised **~$220M
> seed** (DeepMind alumni; Accel) in **May 2024**. Crunchbase/PitchBook/press results frequently
> conflate the two. The $200M+ figures and the DeepMind founders belong to **H**, NOT to this
> London AI-governance vendor. Do not merge these companies.

## CTO / hedge-fund lens

- **Day-2, low fit for most funds.** This is an enterprise AI-GRC platform whose sweet spot is
  organizations deploying *many* AI systems and facing *direct* AI regulation — large enterprises,
  HR/hiring-tool vendors, and EU-exposed firms. A 50-person fund does not need a discovery-and-
  attestation platform of this scope on Day 1.
- **SR 11-7 / model risk:** adjacent but not a native fit. SR 11-7 is about *model* validation,
  documentation and independent review of quantitative/trading/credit models; Holistic AI's
  governance registry and risk-assessment workflow can *support* that documentation discipline,
  but it is built around **AI/ML system governance and regulatory mapping** (EU AI Act, NIST AI
  RMF, ISO 42001), not SR 11-7 model-validation methodology specifically. Funds that already run
  a model-risk function ([modelop](modelop.md), [monitaur](monitaur.md) are closer matches) will find more overlap
  there.
- **When you'd actually need it:** if the fund builds or sells AI-driven HR/screening tools
  (NYC LL144 exposure), has material **EU AI Act** obligations, or wants a single inventory +
  attestation system across a sprawling internal AI footprint. Otherwise it's premature.

## Competitors / alternatives

[credo-ai](credo-ai.md) · [ibm-watsonx-governance](ibm-watsonx-governance.md) · [modelop](modelop.md) · [monitaur](monitaur.md) · [fairly-ai](fairly-ai.md)

## Open questions / to verify
- **Exact funding total and latest round** — needs a primary press release; aggregator figures
  (~$35M) are conflated with the Paris "H" company. Currently low confidence.
- Whether self-hosted / on-prem deployment is offered (only SaaS confirmed).
- Current employee count / scale and revenue traction (unknown).
- Substantiate the Council of Europe "Observer Status" claim independently (vendor-stated).

## Sources
- [Mozilla Ventures invests in Holistic AI](https://mozilla.vc/mozilla-ventures-invests-in-leading-ai-governance-platform-holistic-ai/) — fetched 2026-06-28 — supports: investor (Mozilla Ventures, 2024-03-18), founder Emre Kazim, governance product scope; confidence: high
- [Holistic AI: NYC Bias Audits — GOV.UK assurance techniques](https://www.gov.uk/ai-assurance-techniques/holistic-ai-nyc-bias-audits) — fetched 2026-06-28 — supports: NYC Local Law 144 bias-audit capability, AEDT auditing, fairness impact ratios; confidence: high
- [Holistic AI Governance Platform (vendor page)](https://www.holisticai.com/ai-governance-platform) — fetched 2026-06-28 — supports: platform modules, 40+ tests, frameworks (EU AI Act/NIST/ISO 42001/LL144), integrations [MARKETING]; confidence: medium
- [Holistic AI | Tola Capital portfolio](https://tolacapital.com/portfolio/holistic-ai) — fetched 2026-06-28 — supports: investor Tola Capital, full-lifecycle governance description; confidence: medium
- [Holistic AI profile (aiexpert.network) + Tracxn](https://aiexpert.network/holistic-ai-ai-governance-for-enterprises/) — fetched 2026-06-28 — supports: 2020 founding, UCL origin, founders Kazim & Koshiyama, London HQ, independent ownership, investors, OECD toolkit; confidence: medium (aggregator; name-collision risk noted)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2020 founding (UCL), London HQ, co-CEOs Kazim & Koshiyama, independent VC-backed ownership (Tola Capital, Mozilla Ventures Mar-2024, Premji Invest); confirmed AI-GRC/bias-audit positioning and EU AI Act/NIST/ISO 42001/NYC LL144 mapping. Flagged name collision with unrelated Paris "H" ($220M) startup — funding total left low confidence. hedge_fund_fit set low (Day-2).
