# Truffle Security / TruffleHog — funding, OSS license, Enterprise, Analyze

- URL: https://www.securityweek.com/truffle-security-raises-25-million-for-secret-scanning-engine/
- URL: https://www.intelcapital.com/truffle-security-raises-25-million-series-b-to-expand-nhi-security/ (search snapshot)
- URL: https://www.fenwick.com/insights/experience/fenwick-represents-truffle-security-in-25m-series-b-funding (search snapshot)
- URL: https://trufflesecurity.com/
- URL: https://docs.trufflesecurity.com/hosted-scanner-deployment ; https://trufflesecurity.com/docs/configuring-a-scanner (search snapshot)
- URL: https://aws.amazon.com/marketplace/pp/prodview-nptkzku74mhh2 (search snapshot)
- URL: https://api.github.com/repos/trufflesecurity/trufflehog (+ /releases/latest)
- Fetched: 2026-10-26
- Good for: Truffle Security ownership/funding, TruffleHog OSS vs Enterprise scope, deployment and data handling.

## Company
- Truffle Security Co., San Francisco; founded 2021 (SecurityWeek). Co-founder & CEO Dylan Ayrey, who created open-source TruffleHog in 2016 (Intel Capital release).
- Series B $25M led by Intel Capital and a16z, with Abstract, Lytical Ventures and angels (Casey Ellis, Emilio Escobar, Haroon Meer per Fenwick) — announced 2025-11-06. Total raised "over $40M" (one source: $39M = $14M Series A + $25M B).
- Vendor claims: revenue more than doubled in year to Nov 2025; customers mid-market to Fortune 1000 in tech, retail, financial services. Named on site: Optro, TextNow, Klaviyo (none FS).
- Use of funds: TruffleHog Enterprise growth; launch of TruffleHog GCP Analyze; extend NHI analysis to AWS and Azure. Third-party profile (nhigovernance.com) lists AWS Analyze launched Aug 2026 — not confirmed from primary.

## OSS
- github.com/trufflesecurity/trufflehog: AGPL-3.0; ~28.7k stars; repo created 2016-12-31; last push 2026-10-26; latest release v3.99.7 (2026-10-24). Site: 800+ secret types with live verification against providers; 250k+ daily runs.

## Enterprise
- TruffleHog Enterprise: dashboard, continuous monitoring, alerts, developer remediation workflows with re-verification of rotation, team management, support.
- Sources: code repos (incl. history, deleted/hidden content, PR comments), Slack, Jira, Confluence, S3, GCP logs, support tickets.
- TruffleHog Analyze (SaaS/GCP/AWS variants): maps resources and permissions of leaked keys / NHIs.
- Deployment: Truffle-hosted scanner (tenant-isolated in Truffle infra) or self-hosted scanner (K8s/VM) reporting to Truffle's control plane; AWS Marketplace listing says secrets processed in memory, only detection metadata returned to control plane.
- No AI/MCP claims on homepage (2026-10-26). Certifications not stated on homepage.
