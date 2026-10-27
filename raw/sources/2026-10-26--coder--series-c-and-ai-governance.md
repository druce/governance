# Coder — Series C, AI Governance add-on (AI Gateway / Agent Firewall), deployment, lifecycle controls

- URL: https://coder.com/blog/90m-series-c-led-by-kkr-to-advance-secure-enterprise-ai-development (2026-04-01; also GlobeNewswire via nasdaq.com)
- URL: https://coder.com/blog/secure-agentic-ai-now-production-ready (2026-02-03, with July 2026 rename update)
- URL: https://coder.com/docs/ai-coder/agent-firewall
- URL: https://coder.com/docs/ai-coder/ai-gateway
- URL: https://coder.com/docs/admin/templates/managing-templates/schedule
- URL: https://coder.com/use-cases/secure-development-environments
- URL: https://api.github.com/repos/coder/coder (+ /releases)
- Fetched: 2026-10-26
- Good for: funding and FS customer evidence (KKR, QRT), AI governance features and how they enforce,
  licensing tier, self-hosted/air-gapped deployment, workspace lifecycle controls. All vendor-published
  except GitHub API metadata.

## Series C (vendor blog / press release, 2026-04-01)
- $90M Series C led by funds managed by KKR (primarily KKR Next Generation Technology Growth Fund III);
  Qube Research & Technologies (QRT), Uncork Capital and existing investors participated.
- Founded 2017 in Austin, Texas. CEO Rob Whiteley.
- KKR (customer): rolled out to 500+ engineers; went from no AI-assisted code to >half of commits in
  Coder-managed environments in the first year.
- QRT (customer): rolled out to half of its 2,000+ employees (engineers, data scientists, analysts).
  QRT's Zohar Melamed: "Coder gives us the ability to audit every LLM request, control access across
  our global infrastructure".
- Vendor-claimed metrics: 300% YoY bookings growth over four quarters; NDR 184%.
- Third-party trackers (not primary): Series B $65M total incl. $35M extension June 2024 (Dealroom);
  total funding ~$175M (stockanalysis) — unverified.

## AI governance (blog 2026-02-03; docs)
- Coder 2.30 (2026-02-03): AI Bridge and Agent Boundaries GA as the "AI Governance Add-On" for Premium.
- July 2026 update on the post: AI Bridge renamed **AI Gateway**, Agent Boundaries renamed **Agent
  Firewall**, "no functional changes"; AI Governance now included with all newly purchased Premium licences.
- AI Gateway: sits between coding agents/IDEs and providers (OpenAI, Anthropic, AWS Bedrock incl. via
  corporate gateways). Users authenticate with Coder session/token; coderd calls upstream on their
  behalf (no per-user provider keys). Can record prompts, token usage, tool invocations, attributed to a
  user. Admins define approved MCP servers/tools. Runs in coderd or standalone; serves clients inside
  and outside Coder workspaces.
- Agent Firewall: "a process-level firewall that restricts and audits what autonomous programs" can
  access. Two jails: nsjail (default; Linux network namespace; needs CAP_NET_ADMIN) and landjail
  (Landlock V4; Linux 6.7+; "medium bypass resistance"; no PID namespace or UDP control). Allowlist rules
  by domain, HTTP method, path; non-matching requests blocked. Audit log per HTTP request (allow/deny,
  workspace, owner, template, method, URL, timestamp, matched rule) sent to the Coder control plane;
  response status not tracked. Gotcha: `use_real_dns` permits DNS-based exfiltration. Supports "any
  terminal-based agent".
- Use-case page: Agent Firewall "adds default-deny HTTP/HTTPS allowlists for AI coding agents on top of
  workspace network policies". Audit events stream to SIEM. "Independently audited annually under SOC 2
  Type II" (report scope not seen). Deploy on "your cloud, on-prem, or air-gapped infrastructure".
  Product telemetry on by default, can be turned off. Coder states it has no access to customer
  workspaces or source code. Named: US Defense Intelligence org (2,500+ developers); logos Discord,
  Square, Palantir, Payabl, Skai.

## Workspace lifecycle (docs)
- Default autostop on inactivity; dormancy threshold and dormancy auto-deletion; autostop requirement;
  failure cleanup. Dormancy/auto-delete/autostop requirement are Premium features.

## GitHub (API, 2026-10-26)
- coder/coder: AGPL-3.0, ~17.2k stars, not archived, pushed 2026-10-26; latest releases v2.38.2 /
  v2.37.6 / v2.36.9 published 2026-10-23. Repo description: "Secure environments for developers and
  their agents".
