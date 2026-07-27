---
title: CyberArk
type: vendor
name: CyberArk
slug: cyberark
aka: [CyberArk Software, CyberArk Software Ltd., CYBR, Idira, Palo Alto Networks Idira]
primary_category: non-human-identity
also_listed_in: [secrets-management, identity-governance, tool-identity-integration]
website: https://www.paloaltonetworks.com/idira
founded: 1999
hq: 'Petah Tikva, Israel (US ops: Newton, Massachusetts)'
ownership_state: acquired-closed
owner: Palo Alto Networks
ownership_note: 'Acquired by Palo Alto Networks — announced 2025-07-30 ($45.00 cash + 2.2005 PANW shares per CYBR share; ~$25B announced equity value); closed 2026-02-11 per PANW Form 8-K. Final GAAP purchase consideration $21.1B (PANW 10-Q Q3 FY26) — below the headline because ~88% of consideration was PANW stock at a fixed 2.2005 ratio and the share price moved between signing and close. Was public (NASDAQ: CYBR, IPO 2014) until close; CyberArk Software Ltd. survives as a wholly owned PANW subsidiary. In May 2026 PANW rebranded the entire acquired portfolio as **Idira**; the CyberArk brand is being retired (PANW assigned the acquired trade name a 1-year useful life).'
acquisition: {announced: 2025-07-30, closed: 2026-02-11, price: $21.1B final consideration (announced as ~$25B equity value)}
funding_total: 'n/a (was public, NASDAQ: CYBR)'
last_funding: IPO 2014; acquired by Palo Alto Networks 2026-02-11
market_position: null
deployment_model: [saas, self-hosted, on-prem]
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
tags: [pam, identity, secrets, machine-identity, agentic-identity, acquired, palo-alto, idira, renamed]
sources:
  - {claim: acquisition-close, url: "https://www.sec.gov/Archives/edgar/data/1327567/000119312526045600/d40626d8k.htm", date: 2026-02-11, confidence: high}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm", date: 2026-06-03, confidence: high}
  - {claim: rebrand-idira, url: "https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-introduces-idira-next-generation-identity", date: 2026-05-12, confidence: high}
---

# CyberArk

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [non-human-identity](../categories/non-human-identity.md). **CyberArk is no longer a company or a brand — it is [palo-alto-networks](palo-alto-networks.md)' Identity Security pillar, sold as Idira.** The acquisition closed 2026-02-11; PANW rebranded the whole acquired portfolio as **Idira** on 2026-05-12. `cyberark.com` is still live (HTTP 200, no redirect) but now leads with "CyberArk is now Idira." Shop for this as **Idira**.

**One-liner** — The privileged-access-management incumbent — vaults, rotates, and brokers access to the most powerful human, machine, and AI-agent credentials — acquired by [palo-alto-networks](palo-alto-networks.md) (announced 2025-07-30 at ~$25B, closed 2026-02-11 for $21.1B in final consideration) and relaunched in May 2026 as **Idira**, PANW's identity-security platform. There is no independent CyberArk to buy from anymore.

**What it does** — CyberArk started in privileged access management (vaulting admin/root credentials, session isolation and recording, just-in-time elevation) and expanded across the identity spectrum: secrets management for DevOps/cloud ([conjur](conjur.md)), machine/non-human identity, workforce and customer identity, and identity governance. For an AI buyer, the relevant frontier is **identity security for agentic AI** — treating autonomous agents as a new class of privileged identity that needs least-privilege, just-in-time access and credential governance. That framing is the explicit rationale for the PANW acquisition, and it is now the organizing idea of the Idira platform.

**The Idira product map (2026-07-27)** — PANW's own 10-Q describes Idira in five modules, which is the cleanest available mapping from old CyberArk SKUs to what you actually buy today:

| Idira module | What was there before |
|---|---|
| Workforce Identity Security | Workforce Identity / Idaptive lineage, Workforce Password Management, secure browsing |
| IT and Developer Identity Security (Modern PAM) | the classic PAM core — JIT access, session isolation, credential protection, zero standing privileges |
| Machine Identity Security | Secrets Manager (ex-[conjur](conjur.md)), Certificate Manager and PKI (ex-Venafi), workload identity |
| Identity Governance and Administration | access certification, joiner-mover-leaver (ex-Zilla Security) |
| AI Agents Security | new — agent discovery, identity attributes, task-scoped access, activity recording, revoke-on-deviation |

The marketing site groups the same thing as three pillars — **Human**, **Machine**, **Agentic**. Component and technical names below the brand line are reported unchanged; it is the commercial wrapper that moved.

**Where it sits in the stack** — Foundation-layer identity. Tagged [non-human-identity](../categories/non-human-identity.md) (primary), [secrets-management](../categories/secrets-management.md) (via [conjur](conjur.md), now Idira Secrets Manager), [identity-governance](../categories/identity-governance.md) (access certs / lifecycle), and [tool-identity-integration](../categories/tool-identity-integration.md) (brokering agent->tool credentials). It limits blast radius by controlling which identities can reach which secrets/systems — constraining both access to sensitive data and outbound reach.

**Deployment & architecture** — Self-hosted vault, SaaS (the old Privilege Cloud / Identity Security Platform, now the Idira SaaS estate), and hybrid. Secrets Manager (ex-Conjur) provides API-driven secrets injection for CI/CD and cloud-native workloads. Integrates with IdPs, SIEM, cloud providers, and Kubernetes. Reporting on the rebrand says the technical platform and component names are unchanged, so existing deployments, connectors, and admin skills carry over — the change is above the product, not inside it.

**Positioning & differentiators** — Historically the PAM gold standard for regulated enterprises (banks, funds, governments), and that install base is intact. **What has changed is the frame: "independent PAM leader" is no longer an accurate description and should not be used in a shortlist rationale.** CyberArk is now one pillar of a four-pillar security platform (identity alongside Strata/Cortex/Prisma) owned by a vendor many funds already buy firewalls and SOC tooling from. Read that both ways:

- *Upside.* Consolidation leverage. Identity, network, and SOC on one paper contract, one renewal cycle, and — per PANW's pitch — shared agent telemetry. The Idira relaunch pushed **zero standing privilege** and agentic-identity controls as the headline capability, with modern-PAM SaaS customers getting ZSP at no additional cost, which is a genuine capability gain rather than a logo swap.
- *Downside.* You lose a best-of-breed vendor whose only job was PAM, and you gain concentration risk with a platform vendor that will price and roadmap identity against the rest of its portfolio. Anyone whose vendor-risk policy caps exposure to a single security supplier should re-score this. Buyers who deliberately kept identity independent of their network vendor no longer have that separation.

Against cloud-native secrets ([hashicorp-vault](hashicorp-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md)) the differentiator is still breadth — session controls, recording, an enterprise governance wrapper rather than just key storage. Against NHI startups ([astrix-security](astrix-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [token-security](token-security.md)) it is still the incumbent with the install base, now with a much larger balance sheet behind it. Note that the neighborhood consolidated at the same time — [hashicorp-vault](hashicorp-vault.md) is now part of IBM — so "buy the independent" is a shrinking option across identity and secrets generally, not just here.

**Ownership, funding & M&A** — Founded 1999 (Udi Mokady, Alon N. Cohen); HQ Petah Tikva, Israel, with major US ops in Newton, MA. Public on NASDAQ (CYBR) from its 2014 IPO. **Acquired by [palo-alto-networks](palo-alto-networks.md) — VERIFIED against SEC filings:** announced **2025-07-30** (merger agreement date) at ~$25B equity value, $45.00 cash + 2.2005 PANW shares per CyberArk share, 26% premium; **closed 2026-02-11** after US/EU/UK/Israel regulatory clearance and shareholder approval, via reverse-triangle merger with Israeli Merger Sub "Athens Strategies Ltd." PANW's Form 8-K names 2026-02-11 as "the Closing Date" in terms; CyberArk's Form 25-NSE (Nasdaq delisting) was filed the same day and its Form 15-12G deregistration on 2026-02-23. CyberArk Software Ltd. was **not** dissolved — it survives as a wholly owned PANW subsidiary.

**On the price — the headline number is not the number that changed hands.** PANW's Q3 FY2026 10-Q puts the final purchase consideration at **$21.1B** ($2,308M cash + $18,488M in 112M PANW shares + $265M replacement equity awards), against the ~$25B announced. Both are correct for what they measure: ~$25B was an equity value struck at PANW's July 2025 share price, ~88% of the consideration was stock at a **fixed** 2.2005 exchange ratio, and the value was remeasured at close six and a half months later. Cite ~$25B as *announced* and $21.1B as *final*. Purchase accounting also discloses $14.8B of goodwill, $6.3B of identified intangibles — including $3.5B of "platform renewals" amortized over 12–14 years, a straightforward read on how durable PANW thinks the install base is — and, tellingly, a **1-year useful life on the acquired trade name**. PANW was writing the CyberArk brand off before it announced it was retiring it. A $59M post-close workforce optimization plan runs through fiscal 2027.

**As an acquirer**, CyberArk was itself a serial buyer, and this is *not* what `ownership_state` refers to: it bought [conjur](conjur.md) (2017, ~$42M), Idaptive, Venafi (machine identity/certificates), and Zilla Security (IGA), among others. Those companies are now two acquisitions deep inside PANW.

**CTO / hedge-fund lens** — Day-2 in this taxonomy, but effectively Day-1 for a regulated fund that already needs PAM for its privileged human admins; AI/agent governance is an extension of controls you should already have. SR 11-7 relevance is indirect (credential governance for model-serving and agent infrastructure). Practical consequences of the deal:

1. **Search and shortlist under "Idira."** Searching "CyberArk" gets you legacy collateral and an increasingly transitional website. Every module name in this space changed in May 2026.
2. **Procurement routes through Palo Alto Networks.** A renewal is now a PANW renewal and is a candidate for bundling with Strata/Cortex — which is leverage if you are already a PANW shop and a lock-in question if you are not. PANW has published nothing about contract paper, entity, or support-channel changes; assume nothing and ask at renewal.
3. **No forced migration.** PANW's FAQ is explicit that existing customers "continue to use the platform as you always have" — new logo, same platform. Treat this as a branding event for running deployments, not a re-platforming one.
4. **Vendor-concentration review is the real action item.** If your firm's third-party risk policy scores concentration, PANW just became a much bigger share of the security stack for anyone running both PAN-OS/Cortex and CyberArk PAM. That is a governance question, not a technical one, and it is the thing most likely to surprise a risk committee.
5. **Diligence questionnaires and vendor registers need updating** — the counterparty is now Palo Alto Networks, and the legal entity you contract with may or may not still be CyberArk Software Ltd.

**Competitors / alternatives** — [astrix-security](astrix-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [token-security](token-security.md), [entro-security](entro-security.md), [silverfort](silverfort.md) (NHI/identity); [sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md) (IGA); [hashicorp-vault](hashicorp-vault.md) (secrets).

**Open questions / to verify**
- ~~Whether Conjur remains separately marketed or is folded into a unified Secrets Manager SKU~~ — **resolved 2026-07-27:** folded in. It is Idira **Secrets Manager** (SaaS or self-hosted) under Machine Identity; `conjur.org` 301s to the PANW page and the commercial Conjur brand is retired. See [conjur](conjur.md).
- Integration roadmap of the identity pillar into Cortex/Strata and how licensing is repackaged. PANW has stated the strategic intent but published no bundling or price mechanics. Open.
- **Contract, entity, and support mechanics.** Nothing published addresses whether renewals now paper through PANW entities, whether CyberArk Software Ltd. remains the contracting party, or what happens to the CyberArk support portal and community site. Absence of evidence, not evidence of no change — worth asking directly at renewal.
- Fate of `cyberark.com` and `docs.cyberark.com`. The main domain is live and unredirected as of 2026-07-27 but leads with "CyberArk is now Idira"; `docs.cyberark.com` already serves Idira-branded content. Expect eventual redirect; a link-rot risk for this wiki.
- The Idira-module → legacy-SKU mapping in the table above is **reconstructed** from PANW's 10-Q descriptions plus CyberArk's known acquisition history (Idaptive, Venafi, Zilla). Only the Conjur → Secrets Manager leg is independently confirmed. PANW has not published a mapping; treat the other rows as strong inference.

**Sources**
- [PANW Form 8-K, event date 2026-02-11 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1327567/000119312526045600/d40626d8k.htm) — fetched 2026-07-27, cached `raw/sources/2026-07-27--cyberark--panw-close-sec-filings-and-idira.md` — supports: **exact legal close date 2026-02-11** ("the Closing Date"), merger agreement dated 2025-07-30, Merger Sub Athens Strategies Ltd., CyberArk survives as wholly owned subsidiary; confidence: high (primary filing)
- [PANW Form 10-Q, quarter ended 2026-04-30 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm) — fetched 2026-07-27, same cache — supports: **$21.1B final purchase consideration** and its components, purchase price allocation, 1-year trade-name life, $59M workforce plan, and the Idira™ five-module description in PANW's own business section; confidence: high (primary filing)
- [Palo Alto Networks Introduces Idira (PANW investor relations)](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-introduces-idira-next-generation-identity) — fetched 2026-07-27, same cache — supports: rebrand announcement date **2026-05-12**, three-pillar framing, existing-customer upgrade tiers incl. ZSP at no additional cost; confidence: high
- [Idira platform overview (Palo Alto Networks)](https://www.paloaltonetworks.com/idira) — fetched 2026-07-27 — supports: Human/Machine/Agentic pillars, FAQ "you can continue to use the platform as you always have"; confidence: high (vendor marketing, but primary for naming and customer guidance)
- [cyberark.com](https://www.cyberark.com) — fetched 2026-07-27, same cache — supports: domain live, HTTP 200, **no redirect**; acquisition-completion banner and "CyberArk is now Idira" headline linking to the Idira platform page; confidence: high
- [Palo Alto Networks to Acquire CyberArk](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-announces-agreement-to-acquire-cyberark--the-identity-security-leader) — fetched 2026-06-28, cached `raw/sources/2026-06-28--cyberark--panw-acquire-press-release.md` — supports: 2025-07-30 announce, ~$25B announced terms, 26% premium, agentic-identity rationale; confidence: high
- [CyberArk Acquires Conjur (CyberArk press)](https://www.cyberark.com/press/cyberark-acquires-conjur-revolutionizing-devops-security-drive-greater-business-agility/) — fetched 2026-06-28 — supports: Conjur acq 2017, founding, HQ; confidence: high
- [Palo Alto Networks rebrands CyberArk with Idira platform release (SDxCentral)](https://www.sdxcentral.com/news/palo-alto-networks-rebrands-cyberark-with-idira-platform-release/) — fetched 2026-07-27 (via `raw/sources/2026-07-27--conjur--panw-idira-secrets-management.md`) — supports: platform and component names unchanged beneath the rebrand; confidence: medium-high (trade press)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed M&A flag: acquired by Palo Alto Networks (announced 2025-07-30, ~$25B; closed 2026-02-11) against PANW press release + SEC filings. Raised ownership_confidence low->high. Established founded 1999, HQ Petah Tikva (US: Newton MA), formerly NASDAQ: CYBR. Noted CyberArk's own acquisitions (Conjur 2017, Venafi, Idaptive, Zilla).
- [2026-07-27] **Major rebrand recorded: CyberArk → Idira.** URL audit found `cyberark.com` still live and unredirected (HTTP 200) but carrying "Palo Alto Networks Completes Acquisition of CyberArk to Secure the AI Era" and "CyberArk is now Idira." Re-verified the deal against **primary SEC filings** rather than press coverage. Close date **2026-02-11 confirmed exactly** by PANW Form 8-K, which defines it as "the Closing Date" (corroborated by CyberArk's same-day Form 25-NSE delisting and 2026-02-23 Form 15-12G deregistration) — no drift between the blog "completion" date and the legal close, matching the date [conjur](conjur.md) recorded. **Price corrected:** PANW's Q3 FY26 10-Q states final purchase consideration of **$21.1B**, not the ~$25B announced equity value; the gap is stock-price movement on a fixed 2.2005 exchange ratio between signing and close. `acquisition.price` now records both. Confirmed **Idira is a registered platform brand in PANW's own 10-Q** (Idira™, five modules), not just marketing; rebrand announced **2026-05-12** per PANW IR (this also settles the 2026-05-12 vs 05-13 ambiguity flagged in the conjur source file — 05-12 is the release, 05-13 is SDxCentral's story). Frontmatter: `website` → the Idira platform page; `aka` += `Idira`, `Palo Alto Networks Idira`, `CyberArk Software Ltd.`; `ownership_note` rewritten with both price figures; tags += `agentic-identity`, `palo-alto`, `idira`, `renamed`; added structured `sources:`. Body: new Idira product-map table, rewritten positioning (dropped the "independent PAM leader" framing — it is now one pillar of a four-pillar PANW platform, with vendor-concentration as the live buyer question), expanded M&A paragraph separating CyberArk-as-target from CyberArk-as-acquirer, and a five-point CTO checklist. Conjur SKU open question **resolved**. Source cached at `raw/sources/2026-07-27--cyberark--panw-close-sec-filings-and-idira.md`. See [conjur](conjur.md) for the downstream product page.
