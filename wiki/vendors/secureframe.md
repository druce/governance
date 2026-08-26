---
title: Secureframe
type: vendor
name: Secureframe
slug: secureframe
aka: [Secure Frame]
primary_category: enterprise-grc
also_listed_in: []
website: https://secureframe.com/
founded: 2020
hq: San Francisco, CA, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; $79M total raised. $56M Series B (February 2022) led by Accomplice with Kleiner Perkins, Optum Ventures, Kaiser Permanente, Gradient Ventures, Soma Capital, Gaingels, Impatient Ventures and Flexport. No round found since. No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: $79M
last_funding: Series B $56M led by Accomplice, 2022-02
market_position: {enterprise-grc: challenger}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: smb to mid-market
last_verified: 2026-08-26
verify_after: 2027-02-26
tags: [compliance-automation, soc2, iso27001, evidence-collection, grc]
sources:
  - {claim: "$56M Series B led by Accomplice with Kleiner Perkins, Optum Ventures, Kaiser Permanente, Gradient Ventures, Soma Capital, Gaingels, Impatient Ventures and Flexport; total raised $79M; Michael Viscuso (Carbon Black founder) joined the board; February 2022", url: "https://secureframe.com/newsroom/secureframe-raises-56m-to-accelerate-automated-security-and-compliance", date: 2026-08-26, confidence: high}
  - {claim: "Founded 2020; automates evidence collection, continuous monitoring and audit readiness across SOC 2, ISO 27001, HIPAA, PCI DSS and GDPR; positioned on guided onboarding for non-technical buyers", url: "https://research.contrary.com/company/secureframe", date: 2026-08-26, confidence: medium}
---

# Secureframe

> Primary category: [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — The third name in compliance automation alongside Vanta and Drata: automated evidence collection and continuous control monitoring for SOC 2 and ISO 27001, positioned on guided onboarding for firms without a security engineer.

**What it does** — The same core loop as [vanta](vanta.md) and [drata](drata.md). Connect cloud, identity, HR and device-management systems; continuously test controls against framework requirements; auto-collect audit evidence; run the audit through a partner auditor. Framework coverage spans **SOC 2, ISO 27001, HIPAA, PCI DSS and GDPR** among others. The differentiation it claims is process rather than technology: **structured workflows and guided onboarding aimed at non-technical buyers**, against Drata's engineering-team orientation and Vanta's startup self-serve motion.

**Naming / provenance** — Founded **2020** in San Francisco. Single brand; the survey instrument lists it as "Secure Frame" (two words), which is not the company's spelling.

**Ownership & viability** — `independent`, VC-backed, **$79M total raised**. The **$56M Series B closed February 2022**, led by **Accomplice** with **Kleiner Perkins** and others; **Michael Viscuso**, founder of Carbon Black, joined the board. **No round found since 2022** — four years, against [vanta](vanta.md) and [drata](drata.md), both of which raised at unicorn valuations and have since made acquisitions. That gap is the central concern on this page: in a three-horse race where the other two are considerably better capitalised, the third is an acquisition candidate. `verify_after: 2027-02-26`.

**Positioning & differentiators** —
- **Guided onboarding for non-technical buyers.** A genuine fit consideration for a small manager where compliance sits with an operations or legal person rather than an engineer.
- **Broad framework coverage** comparable to its peers.
- **Materially smaller than Vanta and Drata.** Fewer integrations, a smaller partner-auditor network, and less product expansion — Vanta and Drata have both pushed into trust centres, vendor risk and AI governance; Secureframe has moved less.
- **Not enterprise GRC.** Like Vanta and Drata, this is certification automation. It is not a risk register or a system of record — for that, see [hyperproof](hyperproof.md), [logicgate](logicgate.md) or [servicenow](servicenow.md). Filing all three in the same category is a taxonomy compromise, not an equivalence claim.

**Who should choose them / anti-fit** — Fits a **small firm pursuing its first SOC 2 or ISO 27001** — typically driven by institutional-investor due-diligence questionnaires — with no dedicated security engineer. **Anti-fit:** a firm that needs an ongoing risk-and-controls system of record rather than a certification push, and one that would be materially harmed by an acquisition-driven roadmap change mid-programme.

**Known weaknesses / gotchas** — Funding age versus better-capitalised rivals. **Compliance-automation platforms create real switching cost** — control mappings, evidence history and auditor relationships accumulate inside the tool — so vendor durability matters more here than the low price suggests. Coverage of AI-specific risk frameworks is unverified and likely thinner than [vanta](vanta.md)'s or [optro](optro.md)'s.

**Deployment & data handling** — SaaS. The platform reads configuration and identity data across the firm's estate, which is itself sensitive. Data handling and residency specifics **unverified**.

**Integrations & partnerships** — Cloud, IdP, HRIS, MDM and ticketing connectors; partner auditor network. Specific counts unverified. MCP support unverified.

**Compliance & FS traction** — **Unverified.** Customer base skews technology SMB; no financial-services references confirmed. Certifications held (as opposed to sold) not confirmed.

**Commercial** — Not public; tiered SaaS subscription. Generally the lowest-priced of the three main options.

## Open questions

- Any funding or ownership change since the February 2022 Series B — the most important item.
- Whether an AI-governance / AI-risk framework module exists.
- Data export terms — how much of the accumulated control and evidence history is portable on exit.
- Certifications held; named FS customers.
- Whether the wiki should split "compliance automation" out of [enterprise-grc](../categories/enterprise-grc.md) now that it holds four such vendors (Vanta, Drata, Secureframe, plus [centraleyes](centraleyes.md) adjacent).

## Sources

- [Secureframe Raises $56M (Secureframe newsroom)](https://secureframe.com/newsroom/secureframe-raises-56m-to-accelerate-automated-security-and-compliance) — fetched 2026-08-26 — supports: round size, lead, investors, total raised, board; confidence: high (primary)
- [Secureframe business breakdown (Contrary Research)](https://research.contrary.com/company/secureframe) — fetched 2026-08-26 — supports: founding year, product scope, positioning versus peers; confidence: medium
- Cached: `raw/sources/2026-08-26--secureframe--funding-and-positioning.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
