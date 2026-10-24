# LastPass — 2022 breach, crypto thefts linked to it, ICO fine, US class settlement

- URL: https://blog.lastpass.com/posts/notice-of-recent-security-incident (LastPass, primary; dated 2022-12-22, superseded by a March 2023 update)
- URL: https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/ (KrebsOnSecurity, 2025-03-07)
- URL: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/ (UK ICO, primary, 2025-12-11)
- URL: https://news.bloomberglaw.com/privacy-and-data-security/lastpass-gets-initial-nod-for-24-5-million-data-breach-deal (Bloomberg Law, 2026-02-03; via search snippet — paywalled)
- URL: https://lastpasssettlement.com/Home/FAQ (official settlement site; returned 403 to fetch — not read directly)
- Fetched: 2026-10-23
- Good for: the factual record of the 2022 incidents and every downstream consequence, from primary sources where possible.

## LastPass notice (2022-12-22)
- August 2022: unauthorised access to the development environment; source code and technical information taken. LastPass then said no customer data or vaults accessed.
- 2022-11-30: LastPass disclosed unusual activity in a third-party cloud storage service.
- 2022-12-22 update: attacker used credentials and keys obtained in August to access and decrypt some storage volumes and copied backups containing:
  - account metadata: company names, end-user names, billing addresses, email addresses, telephone numbers, IP addresses;
  - a customer vault backup: **website URLs unencrypted**; usernames, passwords, secure notes, form-fill data encrypted (AES-256) with a key derived from the user's master password.
- Default PBKDF2 iterations 100,100; 12-character master-password minimum since 2018. LastPass said default-setting vaults would take "millions of years" to brute force; users with non-default (weaker / older low-iteration) settings advised to consider changing stored passwords. Federated-login business customers: attacker lacked key fragments.

## KrebsOnSecurity (2025-03-07)
- 2025-03-06: federal prosecutors (N.D. Cal.) said they seized ~$24M in crypto clawed back after a $150M theft on 2024-01-30. Complaint names "Victim-1"; ZachXBT identified Ripple co-founder Chris Larsen.
- Seizure complaint written by a US Secret Service agent; investigators believe the thieves used keys from a password vault stolen in the 2022 password-manager breach (LastPass, per Krebs).
- Researchers Nick Bax and Taylor Monahan: dozens of six-figure crypto-theft victims had all stored seed phrases in LastPass "Secure Notes" before 2022; no typical precursor (SIM swap, email compromise). Monahan: "hundreds of millions of dollars" stolen (not independently verified). Further thefts reported as late as Dec 2024.
- Many victims were long-time users with weaker master passwords / fewer PBKDF2 iterations.
- LastPass: no definitive proof linking thefts to its incidents; law enforcement has shown it no "conclusive evidence."

## UK ICO (2025-12-11)
- £1.2 million fine on **LastPass UK Ltd**; up to **1.6 million UK users** affected.
- Chain: employee corporate laptop (Europe) compromised → dev environment and encrypted company credentials; then a US-based senior employee's personal laptop infected via a known vulnerability in a third-party streaming service, master password captured, MFA bypassed; personal and business vaults linked by one master password → backup database accessed.
- ICO found no evidence the hacker decrypted customer passwords (zero-knowledge; master passwords never shared with LastPass).
- Finding: LastPass did not implement sufficiently robust technical and security measures.

## US class action (Bloomberg Law, 2026-02-03, via search snippet)
- *In re LastPass Data Security Incident Litigation*, No. 1:22-cv-12047-PBS (D. Mass.). Preliminary approval of a settlement of up to ~$24.5M: ~$8.2M fund for class losses plus ~$16.3M for further compensation. Plaintiffs' motion for final approval dated 2026-05-18. **Final approval not confirmed** as of 2026-10-23.
- Separate Canadian (British Columbia) settlement approved; claims deadline 2026-06-23 (search snippet, hammerco.ca — not read directly).
