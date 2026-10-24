# Bitwarden CLI npm package compromise (2026-04-22)

- URL: https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/ (2026-04-23)
- URL: https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html (search snippet)
- URL: https://linuxiac.com/bitwarden-confirms-short-lived-npm-compromise-affecting-cli-package/ (search snippet)
- Fetched: 2026-10-23
- Good for: the one material supply-chain incident on Bitwarden's record; scope limited to one npm release.

## Extract
- `@bitwarden/cli@2026.4.0` on npm carried malicious code (bw1.js via preinstall hook) between 17:57 and 19:30 ET on 2026-04-22.
- Stole npm tokens, GitHub tokens, SSH keys, AWS/Azure/GCP credentials; exfiltrated by creating public GitHub repos in the victim's account.
- Bitwarden: limited to the npm distribution channel for the CLI; "no evidence that end user vault data was accessed or at risk"; access revoked, release deprecated. Bitwarden linked it to the wider Checkmarx supply-chain campaign; JFrog/Socket pointed to a compromised GitHub Action in Bitwarden's CI/CD (root cause not settled publicly). Browser extension, desktop, mobile, server, Snap not affected (Linuxiac).
