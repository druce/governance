# Audition AI — product, deployment, and ownership

- Primary URLs:
  - https://audition-ai.com/ (homepage)
  - https://audition-ai.com/grc/ (GRC product)
  - https://audition-ai.com/agents/ (agents / connectors)
  - https://audition-ai.com/leadership/ and https://audition-ai.com/our-team/ (team, HQ, history)
  - https://www.saberin.com/ and https://saberindataplatform.com/ (parent company)
- Fetched: 2026-06-30
- Good for: Audition AI product scope, in-tenant Azure deployment, ownership (Saberin Group, bootstrapped), target market.

## Key facts (as of 2026-06-30)

- **One-liner:** Containerized, compliance-first enterprise AI platform for hedge funds / regulated financial firms. Deploys secure AI assistants, agents, and automations inside the customer's own Microsoft Azure tenant (or on-prem), with identity-bound access, DLP, and immutable audit trails.
- **Legal entity:** Saberin Data Platform, Inc. (a Saberin Group company). HQ: 325 Oser Avenue, Hauppauge, NY (Long Island). Saberin Group founded 2007.
- **Product components (vendor marketing):**
  - Local Agents — agentic workloads on Windows/Linux/cloud/on-prem.
  - Sidekick — personal desktop agents with browser, shell, and file access.
  - Agentic Swarms — coordinated parallel agent teams.
  - Enterprise Intelligence Engine — "sub-second" search across SharePoint, Egnyte, email, Teams, CRM, databases, local files, with citations.
  - Persona Marketplace — pre-built managed skills/assistants.
  - Integration Forge — MCP servers + arbitrary APIs; connectors (S3, Azure, O365, Slack, SQLite, Azure Managed SQL).
- **Deployment:** SaaS (Pro tiers $200/mo single-user); in customer's Azure Resource Group/tenant (Business tier, "your compute, storage, AI resources"); or on-prem. Listed on Azure Marketplace (publisher: Saberin Data Platform Inc).
- **Models:** multi-model via Azure AI Foundry (Claude, GPT, Gemini, Llama, Mistral); claims 11,000+ models, new frontier models "within hours."
- **Identity/access:** Azure Entra ID; "zero-trust"; permission-aware retrieval ("if a user doesn't have access to a document, the AI doesn't either").
- **Governance:** dual-layer guardrails = "Generative Rules" (behavioral) + traditional DLP (SSN/PCI/PII pattern matching); immutable audit trails; real-time email violation alerts; org-wide chat visibility; AI-generated compliance reports/dashboards. SEC / Reg S-P framing.
- **Leadership:** Sharon Saberin (Founder/CEO); Benjamin Saberin (Founder / Developer-Architect); Eldon Sprickerhoff (Cybersecurity Advisor — eSentire founder, MDR pioneer; corroborated independently); Michael "Mags" Maguire (Director of Customer Success).
- **Ownership/funding:** Independent, private (Saberin Group). No external/VC funding found in any search (Crunchbase org pages 403'd; no funding-news hits). Presumed bootstrapped/self-funded. No funding figure recorded. No M&A.
- **Customers:** claims "30+ Hedge Funds & Regulated Financial Firms" (vendor claim, unverified).

## Trifecta
- Sensitive-data leg: strong (in-tenant, permission-aware retrieval, DLP, "data never leaves your cloud").
- Egress leg: partial (in-tenant inference + DLP/audit on outputs, but no outbound network-egress firewall / shadow-AI CASB).
- Untrusted-input leg: weak/partial ("Generative Rules" policy enforcement, but no published prompt-injection defense for Sidekick agents that have shell+browser+file access — open risk).

## Caveats
- "30+ funds" and architecture internals (runtime isolation, prompt-injection defenses) not independently documented. Exact Audition AI product launch date unclear (blog dates Jan–Feb 2026 suggest 2025-era launch). Azure Marketplace + Crunchbase pages returned 403 on direct fetch; relied on search snippets + vendor pages.
