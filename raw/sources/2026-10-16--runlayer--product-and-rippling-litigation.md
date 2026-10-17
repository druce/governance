# Runlayer — product/docs and Runlayer v. Rippling litigation

- URL: https://www.runlayer.com/
- URL: https://www.runlayer.com/security
- URL: https://docs.runlayer.com
- URL: https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/
- URL: https://forkast.news/the-first-mcp-lawsuit-runlayer-v-rippling-signals-a-maturing-agent-economy/
- URL: https://runtimewire.com/article/rippling-sues-runlayer-three-patents-trade-secret-fight
- Fetched: 2026-10-16
- Good for: current capabilities, deployment options, gaps in public docs, litigation status.

## Homepage (vendor marketing)
- Products: **AI Control Plane** (secure/control agents) and **AI Enablement**.
- "Governed MCP gateway across every major AI client"; access "under which identity, budget,
  OAuth grant, and runtime conditions"; "Start with 18,000+ MCPs" then approve a set;
  "Real-time security models scan tool calls, outputs, intent"; shadow AI discovery across
  unmanaged agents, MCPs, skills, plugins, client configs; usage/cost monitoring.
- Clients named: Claude, Cursor, ChatGPT, Codex. Customers: Decagon, Lemonade, Gusto, Opendoor,
  AngelList, PagerDuty, dbt Labs, Baseten; case studies Gusto, Jane, Homebase.
- No certifications, pricing, or deployment detail on homepage or /security page.
  **PII masking not named** anywhere found; /security says runtime scanning for "sensitive data".

## Docs index
- Hosted, or **self-hosted in customer's own AWS account** (ECS + Terraform) or Runlayer
  Operator on EKS/GKE.
- Roles; MCP tool invocation via PBAC, platform features via FGA; sessions + **audit logs**.
- Control: Shadow AI, Runtime Monitoring ("See, alert, and block any agent session"), Policies.
- Hooks SDK for custom agents; Custom MCP Servers; Platform API.
- Okta/Entra/SCIM, SIEM export, PII masking not shown on the index page.

## Litigation
- TechCrunch 2026-07-28: Runlayer sued **Rippling** — trade secret misappropriation, unfair
  competition, breach of contract. Alleges Rippling, as a trial customer under NDA for nearly a
  year, got roadmap/source access, then built a near-clone. Rippling confirmed launching its own
  MCP gateway, denies misuse. Runlayer retained Sullivan & Cromwell.
- Forkast: filed **S.D.N.Y.**, 2026-07-28.
- Runtimewire/TechCrunch-cited: Rippling countersued alleging infringement of **three patents**
  (filing listed 2026-08-10). Status as of 2026-10-16: unresolved; not independently confirmed
  from court docket.
