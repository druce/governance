---
title: Dashlane
type: vendor
name: Dashlane
slug: dashlane
aka: [Dashlane Omnix, Dashlane Business]
primary_category: secrets-management
also_listed_in: []
website: https://www.dashlane.com/
founded: 2009
hq: New York, New York, USA
ownership_state: independent
owner: null
ownership_note: Private, venture-backed. Last disclosed round a $110M Series D led by Sequoia Capital (announced 2019-05-30); earlier investors include Rho, FirstMark, Bessemer and TransUnion (Series C lead, 2016). Reported total raised conflicts ($185M+ vs $211M). No later round found as of 2026-10-23.
acquisition: {announced: null, closed: null, price: null}
funding_total: "$185M+ (TechCrunch, 2019); other outlets report $211M"
last_funding: Series D, $110M, 2019-05 (Sequoia lead)
market_position: {secrets-management: niche-specialist}
deployment_model: [saas]
form_factor: [platform, browser-extension]
data_leaves_tenancy: "true"
integrations: [microsoft-sentinel, slack, intune, jamf, knowbe4]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market to enterprise workforce (business); consumers
last_verified: 2026-10-23
verify_after: null
tags: [password-manager, credential-security, zero-knowledge, phishing-protection, shadow-it]
sources:
  - {claim: "$110M Series D led by Sequoia (2019-05-30); Jim Goetz joined board; $185M+ raised to date; CEO then Emmanuel Schalit", url: "https://techcrunch.com/2019/05/30/dashlane-series-d", date: 2026-10-23, confidence: high}
  - {claim: "Omnix launched 2025-04-25: credential risk detection incl. unmanaged apps, AI phishing warnings, Slack alerts, GPO/Intune/Jamf deployment; CEO John Bennett; named customers", url: "https://www.helpnetsecurity.com/2025/04/25/dashlane-introduces-omnix-for-ai-powered-credential-protection/", date: 2026-10-23, confidence: medium}
  - {claim: "Omnix AI Advisor (2026-03-19): natural-language assistant, MCP integration, runs in hardware-isolated Confidential AI Engine", url: "https://www.helpnetsecurity.com/2026/03/19/dashlane-omnix-ai-advisor/", date: 2026-10-23, confidence: medium}
  - {claim: "More than 25,000 brands; zero-knowledge architecture; product line", url: "https://www.dashlane.com/about", date: 2026-10-23, confidence: medium}
  - {claim: "Consumer Free plan retired 2025-09-16", url: "https://www.dashlane.com/blog/dashlane-free-ending", date: 2026-10-23, confidence: medium}
---

# Dashlane

> Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — A business and consumer password manager that has repositioned around *workforce credential security*. Its Omnix platform finds weak, reused and phished passwords across employees' work apps, including apps not behind SSO, and not only inside the vault.

**What it does** — The core is a zero-knowledge password vault with browser autofill, passkeys and sharing. The enterprise pitch since **April 2025** is **Omnix**, which adds three things on top of the vault:
- **Credential risk detection.** It checks credentials as employees type them, including on unmanaged SaaS and shadow-IT apps and for staff who do not use the vault. Checks run locally in the browser, and logs record only the domain and username.
- **AI phishing warnings** when users land on malicious sites.
- **Risk dashboards and in-context nudges** through Dashlane and Slack.

In **March 2026** it added **Omnix AI Advisor**, a natural-language assistant over that risk data that can produce on-demand compliance reports. It connects to external AI platforms through an MCP integration. Like [lastpass](lastpass.md), Dashlane is a **human-credential product**. No machine-secrets or CI-injection product was verified.

**Naming / provenance** — Founded in Paris in 2009. Its first password-manager release came in 2012 (per Wikipedia, low confidence). Now headquartered in New York, with teams in Paris and Lisbon; trademarks are held by Dashlane SAS. The CEO is **John Bennett**. One aggregator dates his appointment to 2023, succeeding JD Sherman, which is unverified here. Emmanuel Schalit was CEO at the 2019 round.

**Ownership & viability** — `independent`, venture-backed. The last disclosed round is a **$110M Series D led by Sequoia Capital (May 2019)**. Investors also include Rho, FirstMark, Bessemer, and TransUnion, which led the 2016 Series C. Reported totals conflict: TechCrunch said "$185M+" at the time, and other outlets say $211M. **No round has been disclosed in roughly seven years.** That means either profitability or quiet financing; this page could not confirm which. Dashlane retired its consumer **Free plan on 2025-09-16**, a monetisation move consistent with pressure to grow paid revenue. The acquisition-risk note: a venture-backed company this long after its last round is a natural target for a security platform or PE roll-up. Contract and data-export terms are worth checking.

**Positioning & differentiators** — `niche-specialist`: a credible password manager whose distinct angle is workforce credential-risk visibility, rather than secrets breadth or PAM.
- **Visibility beyond the vault.** Omnix's monitoring of credentials on unmanaged apps answers "which employees are reusing a compromised password on a SaaS app we don't federate?" Vault-centric competitors such as [1password](1password.md), [bitwarden](bitwarden.md) and [keeper](keeper.md) answer that less directly. That makes it partly a shadow-IT and phishing tool, adjacent to [sspm](../categories/sspm.md)-style discovery and to security-awareness training (it integrates with KnowBe4).
- **Versus [bitwarden](bitwarden.md):** no self-hosting, no open source and no machine-secrets product. Dashlane is the better fit only if the credential-risk telemetry is the point.
- **Versus [keeper](keeper.md) and [beyondtrust](beyondtrust.md):** no PAM. Dashlane does not do privileged session control.
- The confidential-computing claim for AI Advisor (a hardware-isolated enclave Dashlane says it cannot access) is a thoughtful design, but it is **vendor-asserted**.

**Who should choose them / anti-fit** — Fits a **firm whose problem is employee password hygiene and phishing exposure across a long tail of SaaS** and that wants telemetry to show it to a CISO, auditor or board. **Anti-fit:** anyone needing application/CI secrets, PAM, a self-hosted vault, or the lowest per-seat price.

**Known weaknesses / gotchas** —
- **Narrow product scope** for a "secrets management" slot: this is a staff-password tool, not a secrets manager.
- **Funding opacity:** no disclosed raise since 2019. Treat viability as unverified rather than at risk.
- **Browser-extension dependence.** The risk-detection value relies on the extension seeing what users type into web apps. That is powerful, but it is a sensitive capability to deploy, so review exactly what is collected and sent.
- No breach of Dashlane vault data was found in this pass. That is "not found", not "verified clean".

**Deployment & data handling** — SaaS only; no self-host option verified. Vault data is zero-knowledge encrypted and stored with Dashlane. Omnix sends risk metadata (domain, username, risk signals, not passwords, per the vendor) to Dashlane's cloud. AI Advisor processes that data inside an enclave. Data residency options are **unverified**.

**Integrations & partnerships** — Microsoft Sentinel (credential threat-intel feed), Slack alerts, KnowBe4, and deployment through Group Policy, Microsoft Intune and Jamf. SSO integration exists, but specific IdPs were not verified. An MCP integration was announced with AI Advisor (2026-03), but its direction (server or client) is not confirmed, so `mcp_support: unverified`. Climb is a North American distribution partner.

**Compliance & FS traction** — Certifications **not verified** here (SOC 2 / ISO 27001 not confirmed from a primary page). Named customers in the 2025 launch included Chapters Health System, Cineplex, Crane Co., the Port Authority of NY & NJ and Woolpert; none are investment managers. Dashlane claims more than 25,000 business customers. Two Oct 2026 survey respondents report it in production.

**Commercial** — Per-seat business plans; current business pricing not verified. The consumer Free plan was discontinued 2025-09-16.

## Open questions

- Certifications (SOC 2 Type II, ISO 27001) and data-residency options.
- Funding since 2019: profitability, debt or undisclosed equity.
- John Bennett's appointment date.
- Exactly what Omnix credential risk detection collects from the browser and where it is stored.
- Whether the MCP integration is a server, a client or both.
- Breach and incident history (none found in this pass).
- Named financial-services customers; current business pricing.

## Sources

- [Dashlane Series D (TechCrunch, 2019-05-30)](https://techcrunch.com/2019/05/30/dashlane-series-d) — fetched 2026-10-23 — supports: funding, lead, board, total raised; confidence: high
- [Dashlane introduces Omnix (Help Net Security, 2025-04-25)](https://www.helpnetsecurity.com/2025/04/25/dashlane-introduces-omnix-for-ai-powered-credential-protection/) — fetched 2026-10-23 — supports: Omnix scope, CEO, named customers; confidence: medium (vendor-announcement coverage)
- [Omnix AI Advisor (Help Net Security, 2026-03-19)](https://www.helpnetsecurity.com/2026/03/19/dashlane-omnix-ai-advisor/) — fetched 2026-10-23 — supports: AI Advisor, MCP integration, enclave claim; confidence: medium
- [About Dashlane](https://www.dashlane.com/about) — fetched 2026-10-23 — supports: customer count, product line; confidence: medium (vendor)
- [The Dashlane Free Plan Is Ending Soon (Dashlane blog)](https://www.dashlane.com/blog/dashlane-free-ending) — fetched 2026-10-23 (search snippet) — supports: Free plan retirement date; confidence: medium
- Cached: `raw/sources/2026-10-23--dashlane--funding-omnix-free-plan.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Added because 2 respondents to the Oct 2026 CTO survey wrote it in under Secrets Manager, both in production.
