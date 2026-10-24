# Passwordstate (Click Studios) — April 2021 supply-chain compromise

- URL: https://www.malwarebytes.com/blog/news/2021/04/password-manager-hijacked-to-deliver-malware-in-supply-chain-attack (Malwarebytes, 2021-04; quotes Click Studios' 2021-04-24 advisory)
- URL: https://www.darkreading.com/attacks-breaches/password-manager-suffers-supply-chain-attack (search snippet)
- Fetched: 2026-10-23
- Good for: one-line category-page description of Passwordstate and its incident.

## Extract
- Passwordstate: business password manager from Click Studios (.com.au — Australian; not confirmed by article), >29,000 customers across banking, government, etc.
- Malicious window 2021-04-20 20:33 UTC to 2021-04-22 00:30 UTC (~28 h). Attackers compromised the "In-Place Upgrade" function: the upgrade director on Click Studios' site pointed clients to an attacker CDN serving Passwordstate_upgrade.zip with a malicious DLL (moserware.secretsplitter.dll), named "Moserpass" by CSIS. It harvested system info and Passwordstate records (titles, usernames, passwords, URLs) to attacker servers.
- Click Studios: "a bad actor using sophisticated techniques compromised the In-Place Upgrade functionality"; victim count "appears to be very low"; affected customers told to reset all stored passwords.
