---
title: TrojAI
type: vendor
name: TrojAI
slug: trojai
aka: [Troj.AI]
primary_category: ai-runtime-security
also_listed_in: [ai-red-teaming]
website: https://troj.ai
founded: 2019
hq: Saint John, New Brunswick, Canada (Boston office)
ownership_state: acquired-closed
owner: A10 Networks
ownership_note: 'acq. by A10 Networks (NYSE: ATEN) — announced and closed 2026-06-15; simultaneous sign-and-close (press release says "has acquired"; no closing conditions stated); terms undisclosed; brand now "TrojAI by A10 Networks"; no 8-K filed (A10 calls the deal immaterial to FY2026); re-verified 2026-07-27'
acquisition: {announced: 2026-06-15, closed: 2026-06-15, price: null}
funding_total: ~$9.65M (pre-acquisition, disclosed)
last_funding: Seed $5.75M, Apr 2024 (Flying Fish Partners, Build Ventures, Techstars Ventures)
market_position: null
deployment_model: [self-hosted, saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise; MSSPs; sovereign / regulated buyers
last_verified: 2026-07-27
verify_after: 2026-08-15
tags: [ai-firewall, red-teaming, m-and-a, canada, a10-networks, acquired-closed]
sources:
  - {claim: acquisition-closed, url: "https://www.a10networks.com/news/press-releases/a10-networks-acquires-trojai-inc-expanding-ai-roadmap/", date: 2026-06-15, confidence: high}
  - {claim: acquisition-announced, url: "https://www.businesswire.com/news/home/20260615349365/en/A10-Networks-Acquires-TrojAI-Inc.-Expanding-AI-Roadmap", date: 2026-06-15, confidence: high}
  - {claim: acquisition-price-undisclosed, url: "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001580808&type=8-K", date: 2026-07-27, confidence: high}
  - {claim: brand-persists-as-trojai-by-a10, url: "https://troj.ai", date: 2026-07-27, confidence: high}
---

# TrojAI

> **Re-verified 2026-07-27 against A10's primary disclosures and EDGAR.** The June 2026 acquisition is **closed**, not pending — A10's own release says it "**has acquired**" TrojAI, with no closing conditions stated, and the brand has already been integrated as "**TrojAI by A10 Networks**." Price never disclosed. Primary category: [ai-runtime-security](../categories/ai-runtime-security.md).

> **One-liner** — AI-security platform pairing build-time red teaming (TrojAI Detect) with runtime threat protection (TrojAI Defend); acquired outright by network-infrastructure vendor A10 Networks (NYSE: ATEN) on 2026-06-15.

**Categories** — [ai-runtime-security](../categories/ai-runtime-security.md), [ai-red-teaming](../categories/ai-red-teaming.md)

## What it does
TrojAI secures enterprise AI across two layers. **TrojAI Detect** is automated **red teaming** — it probes models, applications, and agents for vulnerabilities at build time (jailbreaks, prompt injection, data leakage, harmful output), increasingly with *agent-led* multi-turn attack chains, and maps findings to OWASP / MITRE ATLAS / NIST. **TrojAI Defend** is a **runtime AI firewall** — inline inspection of prompts/responses to block prompt injection, sensitive-data leakage, and policy violations in production, including for AI coding agents (Claude Code, Codex). A newer *Agent Runtime Intelligence* capability (private preview as of early 2026) captures full agent execution traces for deeper runtime visibility.

## Where it sits in the stack
Spans [ai-runtime-security](../categories/ai-runtime-security.md) (Defend, the inline firewall — its primary slot) and [ai-red-teaming](../categories/ai-red-teaming.md) (Detect, build-time testing). In lethal-trifecta terms it addresses **untrusted-input** (catching prompt-injection/jailbreaks both pre-prod and inline) and **sensitive-data** (blocking data leakage in responses). It lives at the model/prompt boundary between users/apps and the model, and is meant to sit in the yellow zone in front of model calls.

## Deployment & architecture
API-based runtime inspection (Defend) that can be inserted in front of model endpoints / via an AI gateway; red-teaming (Detect) runs against model and app endpoints. Supports self-hosted / data-sovereign deployment — a point A10 emphasizes ("sovereign AI security"). Findings map to OWASP/MITRE/NIST; targets SIEM/SOC workflows and MSSP delivery. Post-acquisition, pairs with A10's hardware-based AI firewall appliances.

## Positioning & differentiators
One of the few players covering **both** build-time red teaming and runtime defense in one platform (vs. red-team-only [mindgard](mindgard.md)/[splxai](splxai.md) or runtime-leaning [prompt-security](prompt-security.md)). Differentiators: agent-led/multi-turn red teaming, coding-agent runtime protection, and a sovereignty/self-hosted posture attractive to regulated and non-US buyers and MSSPs. Canada-rooted with Boston go-to-market. Nearest neighbors: [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [enkrypt-ai](enkrypt-ai.md).

## Ownership, funding & M&A
**Acquired outright by [A10 Networks](https://www.a10networks.com/) (NYSE: ATEN) — announced *and closed* 2026-06-15.** Re-verified 2026-07-27.

**Why "closed" and not "pending."** A10's own release reads: *"A10 Networks (NYSE: ATEN) today announced that it **has acquired** TrojAI…"* — completed-transaction grammar, with **no** definitive-agreement, closing-conditions, or expected-close language anywhere in the document. This is an ordinary simultaneous sign-and-close: a small private tuck-in needing no regulatory clearance. Two independent corroborations: the wire copy is identical across BusinessWire and StockTitan, and **the brand integration is already live** — troj.ai now ships a logo reading "**TrojAI by A10 Networks**," which is post-close behaviour (pre-close, that degree of brand merger is precisely what gun-jumping rules forbid).

**Price: undisclosed and not derivable.** Terms were never released, and there is no filing to bound them against. A10 stated it *"does not expect the acquisition to have a material impact on its financial results for fiscal year 2026."* Consistent with that, **no 8-K was filed** — Item 2.01 is only triggered by acquiring a *significant* amount of assets, so an immaterial deal creates no obligation — and **EDGAR full-text search returns zero "TrojAI" hits across all A10 10-K/10-Q/8-K filings**. The absence of a filing is what a closed-but-immaterial tuck-in looks like, not evidence against closing. A10's first 10-Q covering the deal (quarter ended 2026-06-30) is due early August 2026 and is the first document that could carry a purchase-price allocation; `verify_after: 2026-08-15` is queued against it.

**Company.** Founded 2019 (incorporated 2020) by **James Stewart (CTO)** and **Stephen Goddard**; CEO since 2024 is **Lee Weiner** (ex-Rapid7). HQ Saint John, New Brunswick, Canada (independently confirmed against TrojAI, Inc.'s SEC Form D business address), with a Boston office. Pre-acquisition funding ~$9.65M disclosed (incl. $5.75M seed Apr 2024 — Flying Fish Partners, Build Ventures, Techstars Ventures; plus NBIF). `ownership_confidence: high`.

## What A10 gets — and why this is a diversification, not a bolt-on
A10 is a **networking-infrastructure** company: application delivery controllers, load balancers, DDoS mitigation, ~$250M revenue, historically sold to network and infrastructure teams. TrojAI moves it up the stack from the packet/flow layer to the **model and prompt layer** — a genuinely different discipline sharing almost no engineering substrate with ADC hardware, and sold to a different buyer (AppSec / AI platform teams rather than network ops). Read it as A10 buying a foothold in AI security rather than extending an existing line.

The stated thesis is **"sovereign AI security"**: pair A10's on-box/hardware AI firewall with TrojAI's software Detect + Defend so the entire pipeline can run inside a customer's own boundary. That self-hosted posture is the most durable part of the rationale for regulated and non-US buyers — and it is the capability most worth watching, since it is also the one a new parent could dilute in favour of appliance attach.

## CTO / hedge-fund lens
**Day-1 for the runtime-firewall job** if you expose LLMs/agents to users or untrusted content; the red-teaming half is a strong Day-2 assurance layer feeding [promotion-gates](../categories/promotion-gates.md). SR 11-7 / model-risk angle: Detect produces framework-mapped test evidence useful for model validation; Defend gives an enforcement + logging control. The A10 acquisition is a double-edged consideration for a hedge fund: it adds a public-company parent and appliance integration (good for procurement stability and on-prem/sovereign needs), but the product is now part of a networking vendor's roadmap, so watch for repositioning. Self-hosted/sovereign deployment is a plus for funds wary of routing prompts through a vendor cloud. Fit **medium** — credible, but smaller and less proven at scale than [prisma-airs](prisma-airs.md) or [hiddenlayer](hiddenlayer.md); the new owner changes the buying calculus.

## Competitors / alternatives
[hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [pillar-security](pillar-security.md), [lakera](lakera.md), [enkrypt-ai](enkrypt-ai.md), [mindgard](mindgard.md), [splxai](splxai.md), [prompt-security](prompt-security.md).

## Open questions / to verify
- ~~Acquisition close date and integration/rebrand under A10.~~ **Resolved 2026-07-27** — closed 2026-06-15 (simultaneous sign-and-close); brand now "TrojAI by A10 Networks" on troj.ai.
- **Purchase price** — never disclosed and no 8-K exists. Check A10's 10-Q for the quarter ended 2026-06-30 (due early Aug 2026) for a business-combination note or cash-paid-for-acquisitions line; A10's own materiality statement means it may never be broken out.
- Whether TrojAI Defend will be bundled with A10's firewall appliances vs. sold standalone, and whether the standalone SaaS survives.
- Whether the newer **Defend for MCP** and **Defend for Employees** SKUs (live on the post-acquisition site) are generally available or still early — they postdate the last product-detail research pass.
- Retention of Lee Weiner and the founding team under A10; no retention terms were announced.

## Sources
- [A10 Networks Acquires TrojAI Inc., Expanding AI Roadmap](https://www.a10networks.com/news/press-releases/a10-networks-acquires-trojai-inc-expanding-ai-roadmap/) — fetched 2026-06-28 — supports: acquisition 2026-06-15, rationale, two product layers; confidence: high
- [BusinessWire: A10 Networks Acquires TrojAI](https://www.businesswire.com/news/home/20260615349365/en/A10-Networks-Acquires-TrojAI-Inc.-Expanding-AI-Roadmap) — fetched 2026-06-28 — supports: acquisition, public-company parent; confidence: high
- [TrojAI extends platform — agent-led red teaming, runtime intelligence, coding-agent protection](https://www.prnewswire.com/news-releases/trojai-extends-enterprise-ai-security-with-agent-led-red-teaming-runtime-intelligence-and-coding-agent-protection-302716692.html) — fetched 2026-06-28 — supports: product capabilities; confidence: med (vendor)
- [A10 Networks EDGAR filing index (CIK 0001580808)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001580808&type=8-K) — checked 2026-07-27 — supports: no 8-K filed for TrojAI, zero "TrojAI" hits in any A10 periodic filing, exchange = NYSE; confidence: high
- [troj.ai](https://troj.ai) — checked 2026-07-27 — supports: brand persists as "TrojAI by A10 Networks", acquisition banner, current SKU list incl. Defend for MCP / for Employees; confidence: high
- (cached: `raw/sources/2026-06-28--trojai--a10-acquisition.md`, `raw/sources/2026-07-27--trojai--a10-close-verification.md`)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; ownership changed independent → **acquired** (A10 Networks, announced 2026-06-15, terms undisclosed) — NOT in seed flags; set ownership_confidence high. Established founding 2019 (Stewart/Goddard), CEO Lee Weiner, HQ Saint John NB, ~$9.65M raised pre-deal. Documented Detect (red team) + Defend (runtime) split. hedge_fund_fit = medium.
- [2026-07-27] **URL audit + M&A re-verification against primary sources and EDGAR. `acquired-closed` CONFIRMED — no correction needed.** The 2026-06-28 pass had set `closed` equal to `announced` with no separate citation (the defect shape found on natoma and symmetry-systems), so it was re-checked from scratch. It holds: A10's release says it "**has acquired**" TrojAI with no closing conditions stated, the wire copy is identical across two independent retrievals, and troj.ai has already rebranded to "TrojAI by A10 Networks" — brand integration is post-close behaviour. Verified A10 filed **no 8-K** and that EDGAR full-text search returns **zero "TrojAI" hits** in any A10 periodic filing, consistent with A10's own statement that the deal is immaterial to FY2026. Price remains undisclosed and undeterivable; left `null`. Confirmed HQ against TrojAI, Inc.'s SEC Form D. Confirmed A10 trades on **NYSE** (EDGAR `exchanges: ["NYSE"]`) — the page was already right. Set `last_verified: 2026-07-27`, `verify_after: 2026-08-15` (A10's Q2 10-Q, the first filing that could disclose price); added 4 `sources:` entries and tags. Added a section on why this is a diversification for a networking vendor; resolved the close-date open question and added price / SKU / retention ones. survey-v2.csv row corrected — it said "pending," which was wrong.
