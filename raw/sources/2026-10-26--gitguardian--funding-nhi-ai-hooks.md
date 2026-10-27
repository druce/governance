# GitGuardian — funding, NHI Governance, AI-agent hooks, MCP

- URL: https://blog.gitguardian.com/series-c-pr/ (also PRNewswire 2026-02-11)
- URL: https://www.securityweek.com/gitguardian-raises-50-million-for-secrets-and-non-human-identity-security/ (search snapshot)
- URL: https://blog.gitguardian.com/gitguardian-closes-44-million-series-b/ ; https://www.securityweek.com/gitguardian-raises-44-million-create-code-security-platform (search snapshots)
- URL: https://www.gitguardian.com/nhi-governance
- URL: https://docs.gitguardian.com/releases/saas/2026/09/07/changelog (search snapshot)
- URL: https://gitguardian.com/industries/public-sector (search snapshot)
- URL: https://api.github.com/repos/GitGuardian/ggshield ; https://api.github.com/repos/GitGuardian/ggmcp
- Fetched: 2026-10-26
- Good for: GitGuardian ownership/funding, product scope (secrets detection -> NHI governance -> AI-agent hooks), deployment.

## Funding / ownership
- Founded 2017 by Jérémy Thomas and Eric Fourrier (CEO). HQ Paris + New York.
- Series B $44M led by Eurazeo w/ Sapphire, Balderton, BPI, Fly Ventures — announced 2021-12-07; total $56M at that point.
- Series C $50M led by Insight Partners with Quadrille Capital; existing Balderton, BPI, Eurazeo, Fly Ventures, Sapphire — 2026-02-11. Implied total ~ $106M (56+50; not a company-stated total).
- Use of funds: AI agent security, enterprise NHI governance, geographic expansion. CEO: moving "beyond secrets detection into full NHI lifecycle governance".
- Metrics (vendor, 2025): 350k secret exposures remediated (5x YoY); 610k+ repos monitored; 210k+ collaboration sources; 550+ secret types; 115k+ developers across enterprise customers; 600k+ developers overall; "most installed GitHub app"; 80%+ new ARR from North America. Named customers: Snowflake, ING, BASF, Bouygues Telecom, Deutsche Telekom.

## Products
- Secrets Detection (internal repos, CI, collaboration tools like Slack/Jira/Confluence), Public Monitoring (public GitHub), honeytokens, NHI Governance, ggshield CLI (MIT, ~2.0k stars, active 2026-10-26).
- NHI Governance (launched ~April 2025 per third-party nhigovernance.com profile): inventory of secrets used by NHIs incl. outside vaults; consumers, last rotation, permissions; map NHI→app→resource with owners; stale/unused/over-privileged detection; semi-automated rotation; revocation. ggscout collects and hashes secret metadata in-customer-environment, sends to platform. Integrates with "secrets managers" (list linked, vendors not named on page).
- AI: 2026-09-07 changelog — "AI Hooks" scan prompts and tool use in Claude Code, Cursor, Copilot CLI, VS Code, Codex, Mistral Vibe; agent & MCP inventory; claim AI-coding-tool users leak secrets ~2x baseline. ggmcp MCP server (MIT, created 2025-05-14).
- Deployment: SaaS plus self-hosted, including air-gapped on-prem (public-sector page). SOC 2: only found an older "SOC 2 Type I" blog post; current Type II / ISO 27001 not confirmed.
