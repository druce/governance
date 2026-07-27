---
title: Pangea
type: vendor
name: Pangea
slug: pangea
aka: [Pangea Cyber, Pangea AI Guardrail Platform]
primary_category: ai-red-teaming
also_listed_in: [ai-runtime-security]
website: https://pangea.cloud
founded: 2021
hq: Palo Alto, California, USA
ownership_state: acquired-closed
owner: CrowdStrike
ownership_note: 'Acquired by CrowdStrike (NASDAQ: CRWD) — announced 2025-09-16 at Fal.Con 2025, completed 2025-09-26 (per CrowdStrike FY2026 10-K Note 12 and Q3 FY2026 10-Q Note 11). $222.7M total consideration transferred as filed; the ~$260M in trade press is an unconfirmed deal-value estimate. Now part of CrowdStrike''s AI Detection and Response (AIDR).'
acquisition: {announced: 2025-09-16, closed: 2025-09-26, price: '$222.7M total consideration transferred (CrowdStrike FY2026 10-K Note 12)'}
funding_total: ~$51M (pre-acquisition)
last_funding: $26M Series B (Nov 2022, led by GV; Decibel, Okta Ventures)
market_position: null
deployment_model: [saas]
form_factor: [api, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / developers building AI apps
last_verified: 2026-07-27
verify_after: null
tags: [ai-guardrails, prompt-injection, aidr, crowdstrike]
---

# Pangea

> Primary category: [ai-red-teaming](../categories/ai-red-teaming.md) (AI guardrails). Also [ai-runtime-security](../categories/ai-runtime-security.md). **Acquired by [crowdstrike](crowdstrike.md)** (2025).

**One-liner** — A developer-first "AI guardrail" platform — prompt-injection blocking, AI DLP, and policy guardrails delivered as APIs/SDK — now the prompt-layer core of [crowdstrike](crowdstrike.md)'s AI Detection and Response (AIDR).

## What it does
Pangea provides a set of composable **AI security guardrails** that developers drop into AI applications or AI gateways: prompt-injection detection/blocking, sensitive-data redaction (AI DLP), malicious-content and PII filters, and policy enforcement on prompts and responses. It also protects workforce AI use (visibility + guardrails on how employees use AI). The pitch is "ship secure AI apps fast" via a few lines of code rather than standing up a separate inline appliance.

(Pangea began life in 2021 as a broader developer-first security-services API platform — auth, audit logging, secure-by-design building blocks — and pivoted to AI guardrails as that market emerged.)

## Where it sits in the stack
Model/prompt layer. It screens untrusted input (prompt injection) and prevents sensitive-data leakage on outbound flows, sitting in the yellow (AI application) trust zone. Functionally it overlaps [ai-runtime-security](../categories/ai-runtime-security.md) (AI firewall) and [ai-red-teaming](../categories/ai-red-teaming.md)/guardrails; it is more an embeddable guardrail toolkit than a standalone inline proxy.

## Deployment & architecture
API/SDK-first, cloud-delivered. Guardrails are invoked from application code or fronted by an AI gateway. Vendor claims prompt-injection blocking at ~99% efficacy and sub-30ms latency (marketing — unverified). Post-acquisition, capabilities are being folded into [crowdstrike](crowdstrike.md) Falcon as AIDR.

## Positioning & differentiators
- Developer-/API-first guardrails vs. inline-proxy AI firewalls like [witnessai](witnessai.md) or [prisma-airs](prisma-airs.md).
- Founders Oliver Friedrichs and Sourabh Satish previously built Phantom Cyber (SOAR, acquired by Splunk 2018) — a security-operations pedigree that fits CrowdStrike's SOC focus.
- Nearest neighbors: [lakera](lakera.md), [prompt-security](prompt-security.md), [hiddenlayer](hiddenlayer.md), [enkrypt-ai](enkrypt-ai.md), [pillar-security](pillar-security.md), [aim-security](aim-security.md) in the guardrails/AI-runtime space.

## Ownership, funding & M&A
**Seed flag "acq by CrowdStrike" — CONFIRMED and closed.** CrowdStrike announced a *signed definitive agreement* to acquire Pangea on 2025-09-16 at Fal.Con 2025, and **closed on 2025-09-26** — ten days later, per CrowdStrike's audited FY2026 Form 10-K (Note 12), corroborated by the Q3 FY2026 10-Q (Note 11) and by CrowdStrike's own XBRL date tag.

Total consideration transferred **as filed is $222.7M**: $212.1M cash (net of $9.4M cash and restricted cash acquired), $0.3M of replacement equity awards, and $10.3M of replacement liability awards. Allocation: goodwill $209.9M, developed technology $13.2M (72-month life), net tangible liabilities $0.4M. The **~$260M** figure that circulated in trade press on announcement day appears in no CrowdStrike filing or release — CrowdStrike disclosed no price at all in its press release. The gap is *consistent with* a headline number including retention equity attributed to post-combination service, which the filing says was explicitly excluded from purchase price, but the filing doesn't quantify it, so that bridge is inference rather than confirmed.

Pre-acquisition Pangea was independent, ~$51M raised, including a $26M Series B (Nov 2022) led by GV with Decibel and Okta Ventures. Confidence: high on the acquisition, close date and filed price.

> Don't conflate with **Onum Technology**, which CrowdStrike closed on 2025-09-12, two weeks before Pangea. The FY2026 cash-flow line of $382.3M covers both deals and is not the Pangea price.

## CTO / hedge-fund lens
Day-2. Relevant only if you are *building* AI applications and want embeddable guardrails, or if you're a CrowdStrike shop adopting AIDR. A fund that only *consumes* SaaS AI assistants would get more from an [ai-access-governance](../categories/ai-access-governance.md) CASB-for-AI tool than from a developer guardrail SDK. As a now-CrowdStrike product, evaluate it as part of the Falcon platform rather than a standalone purchase.

## Competitors / alternatives
[lakera](lakera.md), [prompt-security](prompt-security.md) (now [sentinelone](sentinelone.md)), [hiddenlayer](hiddenlayer.md), [prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md), [enkrypt-ai](enkrypt-ai.md), [witnessai](witnessai.md).

## Open questions / to verify
- ~~Exact close date and final price~~ — **RESOLVED 2026-07-27**: closed 2025-09-26; $222.7M total consideration transferred per CrowdStrike's FY2026 10-K. The ~$260M press figure is unconfirmed by any filing.
- Whether Pangea remains available as a standalone product or only inside Falcon AIDR going forward.
- The FY2026 10-K purchase-price allocation is still labeled preliminary and drifted slightly from the 10-Q (goodwill $210.2M → $209.9M); consideration and date are unchanged, but final numbers could move again.

## Sources
- [CrowdStrike Form 10-K, FY2026 (period ended 2026-01-31)](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm) (filed 2026-03-05), Note 12 *Business Combinations* — fetched 2026-07-27 — supports: **close date 2025-09-26**, **$222.7M total consideration transferred** ($212.1M cash net of cash acquired + $0.3M replacement equity awards + $10.3M replacement liability awards), goodwill $209.9M, developed technology $13.2M/72-month life, $3.1M acquisition costs; also separates the Onum deal (closed 2025-09-12); confidence: high (primary, audited). Cached: `raw/sources/2026-07-27--pangea--crowdstrike-close-date.md`
- [CrowdStrike Form 10-Q, quarter ended 2025-10-31](https://www.sec.gov/Archives/edgar/data/1535527/000153552725000033/crwd-20251031.htm) (filed 2025-12-03), Note 11 — fetched 2026-07-27 — supports: independent corroboration of the 2025-09-26 close date; confidence: high (primary)
- [CrowdStrike to Acquire Pangea to Secure Every Layer of Enterprise AI](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-pangea-to-secure-every-layer-of-enterprise-ai/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: announcement date 2025-09-16, "signed a definitive agreement" (i.e. pending, not closed), AIDR, Pangea capabilities; discloses **no** price; confidence: high
- [CrowdStrike Buys Pangea for $260M (BankInfoSecurity)](https://www.bankinfosecurity.com/crowdstrike-buys-pangea-for-260m-to-guard-enterprise-ai-use-a-29480) — fetched 2026-06-28 — the ~$260M value is a **press estimate contradicted by the filed $222.7M** — do not cite as fact; confidence: low on price
- [Pangea Cyber Closes $26M Series B (PR Newswire)](https://www.prnewswire.com/news-releases/pangea-cyber-closes-26m-series-b-from-gv-decibel-and-okta-ventures-for-developer-first-security-framework-to-deliver-secure-apps-faster-301689531.html) — fetched 2026-06-28 — supports: founded 2021, HQ Palo Alto, founders, $26M Series B; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED acquisition by CrowdStrike (announced 2025-09-16 at Fal.Con, ~$260M, completed ~Sept 2025) — raised ownership_confidence to high. Established Pangea founded 2021, HQ Palo Alto, founders ex-Phantom Cyber, ~$51M raised. Added `ai-runtime-security` as secondary category (guardrails overlap). Set hedge_fund_fit medium.
- [2026-07-27] Date-sanity sweep — **corrected a fabricated close date**. `closed` was 2025-09-16, an exact copy of the announcement date, which the page's own `ownership_note` already hedged against by saying "completed ~Sept 2025". CrowdStrike's press release announced only a *signed definitive agreement*, i.e. a pending deal. The audited FY2026 10-K (Note 12) gives the real close as **2025-09-26**, ten days later, corroborated by the Q3 FY2026 10-Q (Note 11) and CrowdStrike's XBRL date tag. Also replaced the null `price` with the filed **$222.7M total consideration transferred** and demoted the ~$260M BankInfoSecurity number to an unconfirmed press estimate — CrowdStrike disclosed no price publicly. Added a note distinguishing the Onum deal (closed 2025-09-12) and an open question tracking the still-preliminary PPA. `ownership_state: acquired-closed` confirmed correct and now genuinely sourced. Cached 1 new source.
