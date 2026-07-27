---
title: Aim Security
type: vendor
name: Aim Security
slug: aim-security
aka: [Aim, Aim Labs, Cato AI Security]
primary_category: ai-runtime-security
also_listed_in: [ai-spm]
website: https://www.catonetworks.com/platform/ai-security-aisec/
founded: 2022
hq: Tel Aviv, Israel
ownership_state: acquired-closed
owner: Cato Networks
ownership_note: Acquired by [cato-networks](cato-networks.md) — announced and closed 2025-09-03 (Cato's first acquisition; price undisclosed, ~$350M reported). Brand retired — aim.security 301-redirects to catonetworks.com with zero Aim branding; capability sold as Cato AI Security (GA 2026-03-17)
acquisition: {announced: 2025-09-03, closed: 2025-09-03, price: null}
funding_total: ~$28M (Series A; pre-acquisition)
last_funding: $10M Series A extension / ~$18M Series A (YL Ventures, Canaan Partners)
market_position: null
deployment_model: [saas]
form_factor: [api, inline-proxy]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [acquired, ai-firewall, shadow-ai, ai-spm, unit-8200, cato]
sources:
  - {claim: "Aim brand retired; www.aim.security 301-redirects to catonetworks.com homepage with zero Aim branding anywhere on Cato's AI-security pages", url: "https://www.catonetworks.com/platform/ai-security-aisec/", date: 2026-07-27, confidence: high}
  - {claim: "Aim capabilities converged into the Cato SASE Platform and launched as Cato AI Security, generally available worldwide; GPU inspection layer branded Cato Neural Edge", url: "https://www.catonetworks.com/news/cato-introduces-first-gpu-powered-sase-platform-with-native-ai-security/", date: 2026-07-27, confidence: high}
  - {claim: "Acquisition announced in the past tense with no definitive-agreement or pending-close language, and Aim customers able to deploy same-day — deal closed 2025-09-03; price undisclosed", url: "https://www.catonetworks.com/news/cato-acquires-aim-security-to-extend-sase-leadership-and-secure-enterprise-ai-transformation/", date: 2026-07-27, confidence: high}
---

# Aim Security

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [cato-networks](cato-networks.md)** — deal **closed 2025-09-03**. **Brand retired:** `aim.security` now 301-redirects to `catonetworks.com`. The shopping unit is **Cato AI Security**, not Aim.

**One-liner** — An enterprise AI-security pure-play (AI firewall + shadow-AI control + AI-SPM) bought by SASE vendor [cato-networks](cato-networks.md) in its first-ever acquisition, now fully absorbed and sold as Cato AI Security.

## What it does
Aim secures enterprise AI across three jobs: (1) **securing employee use of public AI apps** — shadow-AI discovery and policy (CASB-for-AI / [ai-access-governance](../categories/ai-access-governance.md)); (2) **protecting private AI apps and agents** via an inline **AI Firewall** that screens prompts/responses for prompt injection, data leakage and abuse ([ai-runtime-security](../categories/ai-runtime-security.md)); and (3) **securing the AI development lifecycle** via AI Security Posture Management — discovering and governing the AI assets an org builds ([ai-spm](../categories/ai-spm.md)). It targeted Fortune 500 / Global 2000 buyers. Aim's research team is also known publicly for AI vulnerability discovery (e.g., "EchoLeak"-class agent/Copilot exploits).

## Where it sits in the stack
Primary [ai-runtime-security](../categories/ai-runtime-security.md) (the AI firewall) with a secondary [ai-spm](../categories/ai-spm.md) tag (posture management); also overlaps [ai-access-governance](../categories/ai-access-governance.md) (shadow AI). Layer: model-prompt. Lethal-trifecta role: covers all three legs — **untrusted input** (prompt-injection defense), **sensitive data** (DLP on AI traffic), **egress** (governing what leaves to public AI). Sits at the green↔red boundary.

## Deployment & architecture
SaaS with API and inline deployment in front of AI apps/agents. **As of 2026-03-17 the integration is done**: Aim's inspection runs natively inside the [cato-networks](cato-networks.md) SASE Platform on **Cato Neural Edge**, a GPU-accelerated (NVIDIA) inspection layer deployed across Cato's private backbone, so AI controls ride the same inline path as SD-WAN/SSE rather than as a standalone proxy. Standalone-Aim deployments were offered a migration path. Integrations: IdP, SIEM, the enterprise's AI gateways and SaaS estate.

## Positioning & differentiators
Aim covered the full enterprise-AI-security span (shadow AI + runtime firewall + AI-SPM) in one product rather than picking a single slice — that breadth is part of why a SASE vendor bought it to instantly fill its AI-security line. Founded by [[Unit 8200]] veterans, backed by [[YL Ventures]] and Canaan Partners.

**Post-acquisition (verified 2026-07-27):** the three-leg product structure survived the absorption but the name did not. Cato sells it as **Cato AI Security (AISEC)** with the legs renamed: *AI Security for End Users* (shadow-AI discovery and policy on public GenAI), *AI Security for Applications* (Aim's AI Firewall — prompt injection, data leakage, runtime attacks against private AI apps/agents), *Agentic AI Security* (visibility and logging of agent↔model↔MCP-server interactions, tool calls, APIs), and *AI-SPM* (posture, tested against EU AI Act and ISO 42001). The differentiator is no longer "best-of-breed AI-security pure-play" but "AI security you don't deploy separately because it's already in the SASE path you bought" — which is a platform argument, and only compelling if you are already buying Cato.

Nearest neighbors: [witnessai](witnessai.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md), [prisma-airs](prisma-airs.md), [harmonic-security](harmonic-security.md), [zenity](zenity.md).

## Ownership, funding & M&A
Founded **2022** (HQ **Tel Aviv**, US presence in New York) by Unit 8200 veterans (Matan Getz, CEO; Adir Gruss, CTO). VC-backed by YL Ventures and Canaan Partners (~$28M raised across seed + Series A pre-acquisition; exact total not itemized in sources — noted as unknown-precise). **Acquired by [cato-networks](cato-networks.md)** — announced and **closed 2025-09-03**; value not officially disclosed, press reports ~$350M (some reports $350–400M). This is Cato's first acquisition. **Confidence: high.**

**Why closed, not pending (re-checked 2026-07-27):** Cato's press release is written entirely in the past tense with no "definitive agreement," no expected-close window and no regulatory condition, and it told existing Aim customers they could deploy "today" — a post-close integration plan. Same-day independent coverage (SecurityWeek, CyberScoop, SiliconANGLE, Help Net Security) reported it as done. There is no separate completion announcement, which is normal for a private cash-and-stock deal of this size. Corroborating behavioural evidence: the entire `aim.security` domain 301-redirects to Cato's homepage, and Cato's AI-security product pages carry no Aim branding at all.

## CTO / hedge-fund lens
Day-1 control type (AI firewall + shadow-AI), but **you cannot buy Aim** — as of 2026-07-27 the only way to get this technology is as **Cato AI Security** on the [cato-networks](cato-networks.md) SASE Platform. That makes it a SASE-platform decision, not an AI-security decision: relevant if you are already on Cato or actively choosing a SASE vendor, and a competitive comparison point otherwise. Do not shortlist "Aim Security" — the name is retired and any vendor list still carrying it is stale. Indirect SR 11-7 relevance (control point, plus AI-asset inventory from AI-SPM has mild model-governance value; the AI-SPM leg now advertises EU AI Act / ISO 42001 testing, which is compliance-adjacent but not model-risk management).

## Competitors / alternatives
[witnessai](witnessai.md), [prompt-security](prompt-security.md), [lakera](lakera.md), [calypsoai](calypsoai.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [harmonic-security](harmonic-security.md), [zenity](zenity.md).

## Open questions / to verify
- Precise total funding (sources cite YL Ventures/Canaan backing; figure ~$28M approximate).
- Official deal value — still **not disclosed** by Cato as of 2026-07-27; press estimates range ~$350M (Calcalist) to $350–400M. Left `null` in frontmatter rather than guessed.
- ~~Whether the Aim brand survives inside Cato or is fully absorbed.~~ **Resolved 2026-07-27: fully absorbed, brand retired.**
- Whether Cato AI Security is separately licensable/priced or bundled into SASE tiers — Cato does not publish pricing; unverified.
- Whether Aim's founders (Matan Getz, Adir Gruss) are still at Cato — not confirmed either way.

## Sources
- [Cato AI Security (AISEC) product hub — Cato Networks](https://www.catonetworks.com/platform/ai-security-aisec/) — fetched 2026-07-27 — supports: successor product name/URL, five capability legs, zero surviving Aim branding; confidence: high
- [Cato Introduces the Industry's First GPU-Powered SASE Platform with Native AI Security (Cato press release, 2026-03-17)](https://www.catonetworks.com/news/cato-introduces-first-gpu-powered-sase-platform-with-native-ai-security/) — fetched 2026-07-27 — supports: Aim capabilities converged into the SASE Platform and launched as Cato AI Security, GA worldwide; Cato Neural Edge GPU inspection layer; confidence: high
- [Cato Networks Acquires Aim Security… (Cato press release)](https://www.catonetworks.com/news/cato-acquires-aim-security-to-extend-sase-leadership-and-secure-enterprise-ai-transformation/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: acquirer, announced/closed 2025-09-03, past-tense close language, Aim's three capabilities, founding 2022, YL/Canaan backing; confidence: high
- [Cato Networks Acquires AI Security Firm Aim Security (SecurityWeek)](https://www.securityweek.com/cato-networks-acquires-ai-security-firm-aim-security/) — fetched 2026-07-27 — supports: independent same-day confirmation the deal was done, not pending; confidence: high
- [Cato Networks acquires AI security startup Aim Security (CyberScoop)](https://cyberscoop.com/cato-networks-acquires-ai-security-startup-aim-security/) — fetched 2026-06-28 — supports: ~$350M reported value, Unit 8200 founders; confidence: med
- Cached: [raw/sources/2026-07-27--aim-security--cato-ai-security-brand-retired.md](../../raw/sources/2026-07-27--aim-security--cato-ai-security-brand-retired.md)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **confirmed acquired by [cato-networks](cato-networks.md)** (announced 2025-09-03, ~$350M reported, Cato's first acquisition). Seed flag verified. Filled founding (2022), Tel Aviv HQ, YL/Canaan backing, three-part product. Confidence raised to high.
- [2026-07-27] URL audit found `www.aim.security` 301-redirects to `catonetworks.com` with **zero Aim branding**. Re-researched: the acquisition **closed 2025-09-03** (same day as announced — Cato's PR is past-tense with no definitive-agreement or pending-close language; same-day independent coverage reports it as done; no separate completion announcement exists). `ownership_state` **acquired-pending → acquired-closed**; `verify_after` cleared; `acquisition.closed` set to 2025-09-03. Aim **brand retired** — the site folded wholesale into Cato Networks and the technology is now GA as **Cato AI Security** (launched 2026-03-17, running on the GPU-accelerated Cato Neural Edge inspection layer). `website` repointed from `aim.security` to Cato's AI Security (AISEC) product hub; `aka` gained "Cato AI Security". Price remains officially undisclosed → `null`.
</content>
