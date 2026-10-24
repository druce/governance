---
title: LastPass
type: vendor
name: LastPass
slug: lastpass
aka: [LastPass Business, LastPass Teams, LMI Parent L.P.]
primary_category: secrets-management
also_listed_in: []
website: https://www.lastpass.com/
founded: null
hq: Boston, Massachusetts, USA
ownership_state: pe-owned
owner: Francisco Partners and Elliott Management (via LMI Parent, L.P.)
ownership_note: Spun out of GoTo (formerly LogMeIn); separation announced December 2021 and completed 2024-05-01. Now an independent company under LMI Parent, L.P., the holding entity of the same private-equity sponsors that own GoTo (Francisco Partners and Elliott Management). No sale process found as of 2026-10-23.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {secrets-management: legacy-incumbent}
deployment_model: [saas]
form_factor: [platform, browser-extension]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: consumers and smb to mid-market businesses
last_verified: 2026-10-23
verify_after: null
tags: [password-manager, zero-knowledge, breach-history, pe-owned, regulatory-action]
sources:
  - {claim: "Separation from GoTo completed 2024-05-01; operates under LMI Parent, L.P., owned by Francisco Partners and Elliott Management; CEO Karim Toubba; HQ Boston; 100,000 businesses", url: "https://www.lastpass.com/company/newsroom/b948ad48-3268-4c9e-8b45-0d6d02d0b4e7", date: 2026-10-23, confidence: high}
  - {claim: "2022 incidents: August dev-environment breach; attacker later used stolen keys to copy backups including customer metadata and vault backups with unencrypted URLs and encrypted credentials/notes", url: "https://blog.lastpass.com/posts/notice-of-recent-security-incident", date: 2026-10-23, confidence: high}
  - {claim: "US Secret Service seizure complaint (2025-03) links a $150M Jan-2024 crypto theft to keys from a cracked vault stolen in the 2022 breach; researchers link dozens of thefts to seed phrases in LastPass Secure Notes; LastPass disputes conclusive link", url: "https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/", date: 2026-10-23, confidence: high}
  - {claim: "UK ICO fined LastPass UK Ltd £1.2M (2025-12-11) for insufficient security measures; up to 1.6M UK users; no evidence customer passwords decrypted", url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/", date: 2026-10-23, confidence: high}
  - {claim: "US class action settlement of up to ~$24.5M received preliminary approval (reported 2026-02-03), D. Mass. No. 1:22-cv-12047", url: "https://news.bloomberglaw.com/privacy-and-data-security/lastpass-gets-initial-nod-for-24-5-million-data-breach-deal", date: 2026-10-23, confidence: medium}
  - {claim: "June 2026 Klue OAuth / Salesforce incident exposed LastPass customer contact, support-case and CRM data; vaults not affected; FINRA issued an alert naming LastPass", url: "https://www.finra.org/rules-guidance/guidance/cybersecurity-alert-klue-oauth-breach-and-salesforce-data-exfiltration", date: 2026-10-23, confidence: high}
---

# LastPass

> Primary category: [secrets-management](../categories/secrets-management.md).

**One-liner** — A widely installed consumer and business password manager whose 2022 breach is the reference case for what happens when a password vendor's encrypted vault backups are stolen. Many firms still run it, often through inertia; the question for a CTO is whether to keep it.

**What it does** — A cloud password manager for people. It offers shared and personal vaults, browser autofill, passkeys, MFA, SSO integration for business tiers, and admin policy and reporting. It is a **human-credential vault, not a machine-secrets manager**. It has no equivalent to Bitwarden Secrets Manager, Doppler or HashiCorp Vault for injecting secrets into applications or CI, and none was verified here. It sits in [secrets-management](../categories/secrets-management.md) because respondents put it there. Read it as the staff-password slot of that category.

**Naming / provenance** — Founded independently in the late 2000s; the founding year is not verified here. LogMeIn acquired it, and LogMeIn later renamed itself GoTo. GoTo announced the spin-out in December 2021 and completed it on **2024-05-01**. LastPass's own release describes the result as "an independent company under LMI Parent, L.P." Separately, the June 2026 FINRA alert lists "NoPass (formerly LogMeIn)" among affected firms. The relationship of that entity to LastPass is not established here.

**Ownership & viability** — `pe-owned`. **Francisco Partners and Elliott Management** own it through **LMI Parent, L.P.**, the same sponsors that took LogMeIn private in 2020 and still own GoTo. "Independent" in LastPass's own messaging means separated from GoTo, not free of private-equity ownership. CEO Karim Toubba; HQ Boston. The company claims about 100,000 business customers (vendor figure, May 2024). No sale process or funding event was found as of 2026-10-23. Viability as a going concern is not in question. The live risk is **trust and franchise erosion**: the breach and its aftermath, described below, are the main reason buyers give for leaving.

**The 2022 breach and aftermath (factual record)** —
- **August 2022.** An attacker got into LastPass's development environment and took source code and technical information. LastPass said at the time that no customer data was accessed.
- **November–December 2022.** Using credentials and keys from the August intrusion, the attacker got into cloud storage and **copied backups** containing customer account metadata and **customer vault backups**. That metadata covered company names, user names, billing and email addresses, phone numbers and IP addresses. **Website URLs in the vaults were unencrypted.** Usernames, passwords, secure notes and form-fill data were encrypted with a key derived from each user's master password. Stolen encrypted vaults can be attacked offline indefinitely, so how hard each vault is to crack depends on that user's master password and PBKDF2 iteration count. LastPass said that at its defaults, 100,100 iterations and a 12-character minimum, cracking was impractical. Older accounts often had weaker settings. *(LastPass notice, 2022-12-22.)*
- **How the attacker got in.** The UK ICO's findings say a US-based senior employee's **personal** laptop was infected through a known vulnerability in a third-party streaming service. The attacker captured that employee's master password and bypassed MFA. The employee's personal and business vaults were linked under one master password, a practice LastPass's policy allowed.
- **Crypto thefts attributed to it.** Since 2023, researchers including Nick Bax and Taylor Monahan, plus KrebsOnSecurity, have linked dozens of six-figure cryptocurrency thefts to seed phrases that victims had stored in LastPass Secure Notes before the breach. In **March 2025**, a federal seizure complaint written by a **US Secret Service** agent said investigators believe a **$150M theft on 2024-01-30** used private keys extracted by cracking a vault stolen in the 2022 breach. About $24M was recovered. **LastPass disputes the link**, saying law enforcement has shown it no "conclusive evidence."
- **Regulatory.** On **2025-12-11** the **UK ICO fined LastPass UK Ltd £1.2M** for failing to implement sufficiently robust security measures, affecting up to 1.6M UK users. The ICO found no evidence customer passwords were decrypted.
- **Litigation.** A US class action (*In re LastPass Data Security Incident Litigation*, D. Mass., No. 1:22-cv-12047) reached a settlement of up to about **$24.5M**, which received preliminary approval (reported 2026-02-03). A final-approval motion was filed in May 2026, and **final approval is not confirmed here**. A parallel Canadian settlement was approved in British Columbia.

**A second, unrelated incident (June 2026).** Attackers stole OAuth tokens from Klue, a third-party sales-intelligence vendor, and used them to export LastPass's Salesforce data: customer names, contact details, support cases and CRM records. LastPass says products, infrastructure and vaults were not affected. **FINRA issued a cybersecurity alert naming LastPass** among the affected firms (others included [beyondtrust](beyondtrust.md), OneTrust, Snyk and Tanium). Exposure was limited to contact data, so this is not a vault breach, but it hands phishers a list of confirmed LastPass customers.

**Positioning & differentiators** — `legacy-incumbent`: a large, long-established install base, now losing ground on trust rather than features.
- **Versus [1password](1password.md), [bitwarden](bitwarden.md) and [keeper](keeper.md):** broadly comparable feature set for human passwords. LastPass is weaker on machine secrets, where it has no Secrets Manager equivalent. Bitwarden offers a self-host option that LastPass does not.
- **What it has going for it** is incumbency. Migrating every user's vault is real work, and staying on LastPass is not irrational if the 2022 exposure has been fully rotated out.

**Who should choose them / anti-fit** — Hard to recommend as a **new** purchase for a regulated investment manager when peers without this history cost about the same. **Existing customers** have a defensible case for staying only if they can show that every credential that was in a vault before late 2022 has been rotated. That especially means anything high-value kept in Secure Notes: seed phrases, API keys, infrastructure and broker credentials. **Anti-fit:** anyone needing machine or CI secrets, PAM, or a self-hosted vault.

**Known weaknesses / gotchas** —
- **Pre-2023 vault contents should be treated as exposed.** The encryption only buys time against offline cracking, and the crypto-theft pattern shows that time running out for weaker vaults. Ask whether old accounts had low PBKDF2 iteration counts.
- **Unencrypted URLs in the stolen vault** tell an attacker which services each user has accounts with. That is useful for targeted phishing even without decryption, and the June 2026 CRM leak adds contact details on top.
- **Regulator-recorded control failures** (ICO, 2025) are now part of any vendor-due-diligence file. Expect examiners or investors' operational due diligence teams to ask about them.
- Business messaging that LastPass is now "independent" can obscure that the same PE sponsors still own it.

**Deployment & data handling** — SaaS only; no self-hosted option was verified. Encrypted vaults are stored with LastPass. Under the zero-knowledge model LastPass does not hold users' master passwords, but **some vault fields (URLs, at least in 2022) were stored unencrypted**. Verify the current encryption scope of each field before relying on the zero-knowledge claim. Federated-login (SSO) business accounts use split key material, which the 2022 notice said the attacker did not obtain.

**Integrations & partnerships** — SSO/IdP federation and directory provisioning for business tiers; specifics and SIEM export were not verified here. MCP or agent support was not found.

**Compliance & FS traction** — Certifications **not verified** here. Five Oct 2026 survey respondents report it in production, which shows a real installed base among asset managers. That most likely reflects incumbency rather than new selection.

**Commercial** — Per-seat business tiers (Teams, Business); current prices not verified.

## Open questions

- Founding year.
- Current certifications (SOC 2 Type II, ISO 27001) and their scope.
- Final approval status of the US class settlement.
- Whether any other regulator (US FTC or a state attorney general) has acted on the 2022 breach. None was found in this pass, which is not the same as none existing.
- Current field-level encryption scope (are URLs now encrypted?) and default PBKDF2 iterations for legacy accounts.
- Whether LastPass offers any machine-secrets or CI integration product.
- Relationship, if any, between "NoPass (formerly LogMeIn)" in the FINRA alert and LastPass/GoTo.

## Sources

- [LastPass completes separation from GoTo (LastPass newsroom)](https://www.lastpass.com/company/newsroom/b948ad48-3268-4c9e-8b45-0d6d02d0b4e7) — fetched 2026-10-23 — supports: ownership, date, CEO, HQ; confidence: high (primary)
- [Notice of Recent Security Incident (LastPass, 2022-12-22)](https://blog.lastpass.com/posts/notice-of-recent-security-incident) — fetched 2026-10-23 — supports: 2022 timeline, data taken, encryption scope; confidence: high (primary)
- [Feds Link $150M Cyberheist to 2022 LastPass Hacks (KrebsOnSecurity)](https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/) — fetched 2026-10-23 — supports: Secret Service complaint, crypto-theft pattern, LastPass response; confidence: high
- [Password manager provider fined (UK ICO)](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/) — fetched 2026-10-23 — supports: £1.2M fine, failings, attack chain; confidence: high (primary regulator)
- [LastPass Gets Initial Nod for $24.5 Million Data Breach Deal (Bloomberg Law)](https://news.bloomberglaw.com/privacy-and-data-security/lastpass-gets-initial-nod-for-24-5-million-data-breach-deal) — fetched 2026-10-23 (search snippet; paywalled) — supports: US settlement; confidence: medium
- [Cybersecurity Alert: Klue OAuth Breach and Salesforce Data Exfiltration (FINRA)](https://www.finra.org/rules-guidance/guidance/cybersecurity-alert-klue-oauth-breach-and-salesforce-data-exfiltration) — fetched 2026-10-23 — supports: June 2026 incident, named firms; confidence: high (primary regulator)
- [LastPass confirms data breach in Klue supply chain attack (BleepingComputer)](https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/) — fetched 2026-10-23 — supports: data exposed, LastPass statement; confidence: high
- Cached: `raw/sources/2026-10-23--lastpass--ownership-goto-separation.md`, `raw/sources/2026-10-23--lastpass--breach-2022-and-aftermath.md`, `raw/sources/2026-10-23--lastpass--klue-salesforce-incident-2026.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Added because 5 respondents to the Oct 2026 CTO survey wrote it in under Secrets Manager, all 5 in production.
