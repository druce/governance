---
type: vendor
name: Cisco AI Defense
slug: cisco-ai-defense
categories: [ai-runtime-security, ai-red-teaming]
layer: model-prompt
aliases: [Robust Intelligence, robust-intelligence]
website: "https://www.cisco.com/site/us/en/products/security/ai-defense/"
founded: 2019
hq: San Jose, California, USA
ownership: subsidiary
ownership_detail: "Cisco product built on Robust Intelligence (founded 2019, San Francisco; founders Yaron Singer, Kojin Oshiba, Eric Balkanski, Alexander Rilee). Cisco announced intent to acquire Robust Intelligence 2024-08-26; closed ~2024-09-24. Rebranded/absorbed into Cisco AI Defense."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api, inline-proxy, sdk]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [ai-firewall, red-teaming, cisco]
---

# Cisco AI Defense

> Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). Built on the former [robust-intelligence](robust-intelligence.md), now owned by [cisco](cisco.md).

**One-liner** — Cisco's "security for AI" product: it validates and red-teams models before deployment and enforces runtime guardrails (prompt-injection, jailbreak, data-leak, toxic-content) on AI apps in production.

**What it does** — Two halves. (1) **Validation / algorithmic red teaming** — automatically probes models and AI applications for vulnerabilities (jailbreaks, prompt injection, data poisoning, unsafe outputs) before they ship, the capability that came from [robust-intelligence](robust-intelligence.md). (2) **Runtime protection** — an inline guardrail layer that inspects prompts and responses to block attacks and policy violations in production. Cisco positions it as model-agnostic protection that plugs into its network/SASE fabric so the same controls apply wherever AI traffic flows.

**Where it sits in the stack** — Squarely [ai-runtime-security](../categories/ai-runtime-security.md) (the AI firewall) with a strong [ai-red-teaming](../categories/ai-red-teaming.md) component. Trifecta role: breaks the **untrusted-input** leg (prompt-injection / jailbreak defense), and helps on **sensitive-data** and **egress** by inspecting model I/O. Lives at the model/prompt layer, fed by and feeding Cisco's network and SOC ([splunk](splunk.md)) zones.

**Deployment & architecture** — Delivered as a Cisco cloud service with API/SDK enforcement points and inline inspection that can ride Cisco Secure Access / network egress. Integrates with the broader Cisco Security Cloud and routes detections to [splunk](splunk.md). Model-agnostic across major LLM providers.

**Positioning & differentiators** — Among the earliest "AI firewall" entrants by pedigree — Robust Intelligence shipped one of the first AI firewalls and validation platforms out of Harvard ML research. Cisco's edge over standalone rivals is distribution: bundling AI Defense with network, identity (Duo), and SIEM that enterprises already own. Nearest neighbors: [prisma-airs](prisma-airs.md), [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md).

## Ownership, funding & M&A

A **Cisco** product, not an independent vendor. Robust Intelligence — founded **2019** in San Francisco by Yaron Singer (CEO), Kojin Oshiba, Eric Balkanski and Alexander Rilee — was acquired by Cisco (intent **2024-08-26**, closed ~**2024-09-24**) and its technology became Cisco AI Defense (and Cisco Foundation AI). Confirmed against Cisco's announcement and the "Robust Intelligence is now part of Cisco" page (high confidence). See [robust-intelligence](robust-intelligence.md) (alias page) for the legacy entity.

## CTO / hedge-fund lens

Day-1 if you are exposing internal or customer-facing LLM apps and want a single product that both **pre-deployment red-teams** and **runtime-guards** them. Strongest fit for a fund already standardized on Cisco/Splunk — the integration story is the reason to pick it over a pure-play. Red-teaming/validation output is useful SR 11-7 / model-risk **evidence** (documented testing of model behavior), though Cisco AI Defense is a security tool, not a governance system of record. If you have no Cisco footprint, weigh best-of-breed pure-plays on detection quality.

## Competitors / alternatives

[prisma-airs](prisma-airs.md), [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md), [enkrypt-ai](enkrypt-ai.md), [trojai](trojai.md), [splxai](splxai.md).

## Open questions / to verify

- Current pricing/packaging and whether validation and runtime are sold separately.
- Depth of model coverage and how guardrail detection benchmarks vs pure-plays.

## Sources
- [Cisco Blogs — Cisco Announces Intent to Acquire Robust Intelligence](https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence) — fetched 2026-06-28 — supports: 2024-08-26 intent, Robust Intelligence → AI Defense, founder Yaron Singer; confidence: high
- [Cisco — Robust Intelligence Is Now Part of Cisco](https://www.cisco.com/site/us/en/products/security/ai-defense/robust-intelligence-is-part-of-cisco/index.html) — fetched 2026-06-28 (page title confirms; body 403 to fetcher) — supports: Robust Intelligence absorbed into Cisco AI Defense; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Cisco AI Defense is built on Robust Intelligence (founded 2019 SF; Cisco intent 2024-08-26, closed ~2024-09-24). Set ownership=subsidiary (Cisco), confidence high. Merged robust-intelligence into this page as the canonical profile; that slug is now a thin alias.
