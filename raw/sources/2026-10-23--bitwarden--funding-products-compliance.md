# Bitwarden — funding, company facts, Secrets Manager, compliance, MCP/agent work

- URL: https://www.helpnetsecurity.com/2022/09/07/bitwarden-funding/ (2022-09-07; BusinessWire original returned 403)
- URL: https://bitwarden.com/about/ (vendor, primary)
- URL: https://bitwarden.com/products/secrets-manager/ (vendor, primary)
- URL: https://bitwarden.com/compliance/ (vendor, primary)
- URL: https://bitwarden.com/blog/bitwarden-mcp-server/ and https://www.businesswire.com/news/home/20250710815039/en/Bitwarden-Brings-Agentic-AI-to-Secure-Credential-Management (2025-07; via search snippets — fetch 403)
- URL: https://secure.businesswire.com/news/home/20251030669790/en/Bitwarden-Enhances-MCP-Server-to-Enable-AI-Workflows-in-Enterprise-Administration (2025-10-30; search snippet)
- Fetched: 2026-10-23
- Good for: ownership (minority growth equity, not control), machine-secrets product scope, certifications, agent-era features.

## Funding (Help Net Security, 2022-09-07)
- $100M **minority** growth investment led by **PSG**; existing investor **Battery Ventures** participated. PSG's Tom Reardon and Govind Anand joined the board. Use: developer secrets, passwordless, authentication. Valuation not disclosed. No later round found (search 2026-10-23).

## Company (bitwarden.com/about)
- Founded 2016; founder Kyle Spearrin (Founder & Chief Innovation Officer). HQ Santa Barbara, California. Bitwarden, Inc. is parent of 8bit Solutions LLC. CEO listed: **Michael Sullivan** (Michael Crandell was CEO at the 2022 round).
- "over 80,000 businesses and more than 15 million users."
- Products: Password Manager, Secrets Manager, Passwordless.dev (FIDO2/WebAuthn passkey dev toolkit), Authenticator. Open-source positioning.

## Secrets Manager (product page)
- Projects, **machine accounts** (non-human identities for apps, pipelines and AI agents, each with scoped access token), end-to-end encrypted secrets.
- RBAC, audit/event logs exportable to CSV/SIEM; SSO, SCIM, Directory Connector on Enterprise.
- CLI (`bws run` injects secrets into a process); SDKs: Python, Ruby, Go, C++, C#, Rust, Java, JS, PHP.
- Integrations: GitHub Actions, GitLab CI/CD, Jenkins, Kubernetes Operator, Ansible.
- Self-hosting on Enterprise plan.
- Pricing (annual, USD): Free (2 users, 3 projects, 3 machine accounts); Teams $6/user/mo (20 machine accounts); Enterprise $12/user/mo (50 machine accounts); extra machine accounts $1 each.

## Compliance (bitwarden.com/compliance)
- SOC 2 Type II and SOC 3; ISO 27001 (ISO 27001:2022 announced March 2025 per BusinessWire snippet); HIPAA (annual third-party audit); GDPR/SCCs; CCPA; DPF.
- **Not FedRAMP** — "actively pursuing."
- Annual third-party source-code audits and pen tests per client; HackerOne bug bounty.
- Cloud vault data in Microsoft Azure, US or EU region. Full stack self-hostable.

## Agent-era (search snippets)
- July 2025: Bitwarden MCP server — local-first, runs on user machine over the Bitwarden CLI, on GitHub; blog recommends a local self-hosted LLM when using it.
- Oct 2025: MCP server enhanced for enterprise administration; "Agent Access SDK" announced as an open standard for just-in-time, human-in-the-loop credential release to agents — described by Bitwarden as **alpha**, not for production data.
