---
title: Keeper Security
type: vendor
name: Keeper Security
slug: keeper
aka: [Keeper, KeeperPAM]
primary_category: secrets-management
also_listed_in: [identity-access]
website: https://www.keepersecurity.com/
founded: 2011
hq: Chicago, IL, USA
ownership_state: independent
owner: null
ownership_note: Founder-led with growth-equity minority investors. Insight Partners invested earlier; Summit Partners took a significant minority stake in 2023 (Len Ferrington joined the board). Reported ~73% five-year ARR CAGR and ~250 hires since Summit's investment. Not PE-controlled.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: Minority growth equity from Summit Partners, 2023
market_position: {secrets-management: challenger}
deployment_model: [saas, on-prem]
form_factor: [platform, agent, browser-extension]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: smb to enterprise
last_verified: 2026-08-26
verify_after: null
tags: [password-manager, secrets-management, pam, zero-knowledge, agentic-ai-governance]
sources:
  - {claim: "Summit Partners completed a significant minority investment; Len Ferrington joined the board; since 2023 Keeper added ~250 staff and achieved a 5-year ARR CAGR of 73%; Insight Partners was the earlier investor", url: "https://www.summitpartners.com/news/keeper-security-announces-minority-growth-equity-investment-from-summit-partners", date: 2026-08-26, confidence: high}
  - {claim: "KeeperPAM adds session monitoring, access provisioning and behavioural analytics; Keeper extended agentic AI governance to Endpoint Privilege Manager (2026)", url: "https://www.prnewswire.com/news-releases/keeper-security-extends-agentic-ai-governance-to-endpoint-privilege-manager-302819881.html", date: 2026-08-26, confidence: medium}
---

# Keeper Security

> Primary category: [secrets-management](../categories/secrets-management.md). Also listed in [identity-access](../categories/identity-access.md).

**One-liner** — A zero-knowledge password manager that grew upward into privileged access management and machine secrets — the cheapest credible path from "we use a shared password vault" to something an examiner will accept.

**What it does** — Three layers on one zero-knowledge vault. **Password management** for humans (the original business, browser extension and apps). **Secrets management** for applications and CI/CD, competing with [doppler](doppler.md), [infisical](infisical.md) and the cloud-native stores. **KeeperPAM** adds the privileged-access layer: session monitoring and recording, access provisioning, remote connection brokering and behavioural analytics — moving it onto [cyberark](cyberark.md), [delinea](delinea.md) and [beyondtrust](beyondtrust.md) ground. In 2026 it extended **agentic AI governance** into its Endpoint Privilege Manager, i.e. applying privilege policy to AI agents acting on endpoints rather than only to humans.

**Naming / provenance** — Founded 2011 in Chicago by Darren Guccione and Craig Lurey, both still in place. Single brand throughout.

**Ownership & viability** — `independent` and, unusually for this category, **still founder-led**. Growth equity rather than control: **Insight Partners** earlier, then a **significant minority investment from Summit Partners in 2023** with Len Ferrington joining the board. Summit reports Keeper added ~250 staff since and compounded ARR at roughly **73% over five years**. Note this is the investor's published figure, not an audited one. The practical implication for a buyer: no PE control means less of the renewal-pricing pressure that [delinea](delinea.md) and [beyondtrust](beyondtrust.md) carry, but a minority-invested company at this growth rate is an obvious future control-transaction candidate.

**Positioning & differentiators** —
- **Zero-knowledge architecture.** Keeper cannot decrypt customer vaults — encryption and decryption happen on the device. For a firm placing every credential it owns with a vendor, this is the single most important architectural property, and it is the right thing to verify rather than assume.
- **Price and time-to-value versus the PAM incumbents.** A full [cyberark](cyberark.md) deployment is a project; Keeper is a purchase. For a manager with 50–500 staff that needs credential control it can actually finish deploying, this is the practical trade.
- **One product spanning human passwords, machine secrets and privileged sessions.** Most competitors do one of the three well. The flip side is that KeeperPAM is materially shallower than [cyberark](cyberark.md) on privileged-session control and lacks the depth [hashicorp-vault](hashicorp-vault.md) has on dynamic secrets.
- **Agentic-AI privilege is a real and early move.** Applying privilege policy to non-human agents overlaps [non-human-identity](../categories/non-human-identity.md); how substantive it is versus a feature announcement is unverified.

**Who should choose them / anti-fit** — Fits a **small-to-mid firm** that needs credential hygiene, some privileged-access control, and a defensible answer to a due-diligence questionnaire, without a PAM implementation project. **Anti-fit:** a large firm with complex privileged-session, jump-host and vaulting requirements (buy [cyberark](cyberark.md)); a platform-engineering team wanting dynamic short-lived secrets and encryption-as-a-service (buy [hashicorp-vault](hashicorp-vault.md)).

**Known weaknesses / gotchas** — PAM depth is well below the incumbents despite the KeeperPAM branding — do not assume feature parity from the category label. Concentration risk is inherent: one vendor holding every credential in the firm is a single point of catastrophic failure regardless of architecture, so the zero-knowledge claim, the breach history, and the recovery process all deserve real diligence.

**Deployment & data handling** — SaaS (with on-prem options). **Encrypted vault data resides with Keeper**, but under the zero-knowledge model the vendor holds no key. Confirm the key-management model, the recovery path, and what metadata (vault structure, access times, record titles) is visible to Keeper — that last one is where zero-knowledge claims usually have caveats.

**Integrations & partnerships** — IdP/SSO (SAML, SCIM), CI/CD secrets injection, SIEM export, MSP tooling. MCP support unverified.

**Compliance & FS traction** — **Unverified in specifics**, though Keeper markets FedRAMP and StateRAMP authorisation and SOC 2 / ISO 27001; **none independently confirmed here** and all should be checked directly given the product's role.

**Commercial** — Published per-seat tiers for business plans; enterprise and PAM pricing negotiated. Among the cheapest options in this category.

## Open questions

- Confirm certifications directly (FedRAMP, SOC 2 Type II, ISO 27001) — marketed but not verified here.
- What metadata is visible to Keeper under the zero-knowledge model.
- KeeperPAM's actual session-control depth versus [cyberark](cyberark.md) — feature-by-feature.
- Substance of the agentic-AI privilege governance beyond the announcement.
- Named financial-services customers; breach history.

## Sources

- [Keeper Security Announces Minority Growth Equity Investment from Summit Partners](https://www.summitpartners.com/news/keeper-security-announces-minority-growth-equity-investment-from-summit-partners) — fetched 2026-08-26 — supports: ownership structure, board, growth figures; confidence: high (primary, investor)
- [Keeper Security Extends Agentic AI Governance to Endpoint Privilege Manager (PR Newswire)](https://www.prnewswire.com/news-releases/keeper-security-extends-agentic-ai-governance-to-endpoint-privilege-manager-302819881.html) — fetched 2026-08-26 — supports: KeeperPAM scope, 2026 agentic-AI direction; confidence: medium (vendor release)
- Cached: `raw/sources/2026-08-26--keeper--ownership-and-pam-expansion.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
