# Citizen-dev platforms & agent frameworks with leading examples

Drafted 2026-07-16. Companion to `2026-07-15-citizen-dev-primer-design.md` (Ch 6
tooling landscape) and `2026-07-15-wiki-category-leaders.md` (the governance-side
categories, which come from the wiki).

**⚠ Status: unverified priors.** Unlike the wiki extract, these categories are NOT
covered by the governance wiki — names, deployment modes, and certification claims
below come from model priors and MUST be researched and cited at writing time per
the spec's verification flag (SOC 2 / self-host / ownership / licensing all churn).
Enterprise-bar notes are what to *check*, not established fact.

## Agentic coding (conversational development of real software)

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Agentic coding CLI / IDE | Claude Code; GitHub Copilot Enterprise | Claude Code: enterprise via Bedrock/Vertex or enterprise API, managed settings + hooks as policy points. Copilot: deepest GitHub/Entra integration, audit-log surface |
| AI-native IDE | Cursor (Business) | Hosted-service dependency; check SOC 2, zero-retention mode, policy controls vs. the CLI agents |

## Agent frameworks (code-first, for the top of the builder spectrum)

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Orchestration framework | LangGraph (LangChain); OpenAI Agents SDK | LangGraph: de-facto OSS default, self-hostable; LangGraph Platform / LangSmith for managed control plane. OpenAI SDK: lighter, provider-leaning |
| Provider agent SDK | Claude Agent SDK; Microsoft Agent Framework (ex-AutoGen/Semantic Kernel) | Provider SDKs inherit the provider's enterprise terms; MS framework rides Azure tenancy |
| Multi-agent / role-based | CrewAI | OSS core self-hostable; enterprise control plane newer — verify certs and viability |

## Managed / low-code agent builders

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Suite-native agent builder | Microsoft Copilot Studio; Salesforce Agentforce | Ride the M365/Salesforce estate: tenancy, DLP policies, connector governance already in place; lock-in and per-seat/per-conversation pricing traps |
| Cloud-platform agent runtime | Amazon Bedrock Agents / AgentCore; Google Vertex AI Agent Builder | Run inside the firm's cloud boundary; IAM-native; strongest story for yellow/green-zone agents |

## Internal-tool builders (UI + logic on existing data)

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Internal-tool platform | Retool (self-hosted); Superblocks (on-prem agent) | Both market self-host/VPC + SOC 2 + SSO/SCIM + audit logs; Superblocks' agent keeps data on-prem with SaaS control plane |
| OSS alternative | Appsmith | Self-hostable OSS; enterprise edition for SSO/RBAC/audit — verify gap vs. Retool on governance depth |

## Enterprise low-code suites

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Citizen low-code suite | Microsoft Power Platform (Power Apps / Automate / Dataverse) | Usually already licensed via M365; environments, DLP policies, managed environments, CoE toolkit = deepest governance surface; sprawl-by-default risk |
| Pro low-code (IT-led) | OutSystems; Mendix | Enterprise app platforms — heavier than citizen tier; relevant as the promotion target for apps that outgrow citizen tooling |

## Workflow automation / iPaaS / RPA

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Self-hostable automation | n8n | Self-hosted deployment is the governance anchor; verify enterprise tier (SSO, RBAC, audit, secrets integration) |
| Enterprise iPaaS | Workato; Power Automate | Workato: enterprise connector catalog (Salesforce, NetSuite), governed OAuth, SOC 2. Power Automate: within Microsoft estate + data gateway to on-prem |
| Security automation | Tines | Common in fund security teams; strong audit posture — a pattern for what governed citizen automation looks like |
| RPA (legacy last resort) | UiPath | Still present in funds for no-API systems; prefer APIs; screen-scraping = the "sane implementation choices" anti-pattern institutionalized |

## Analytics & data-app self-service

| Family | Leading examples | Enterprise-bar notes (to verify) |
|---|---|---|
| Data-app framework | Streamlit — esp. Streamlit in Snowflake | Run-the-app-next-to-the-data: inherits Snowflake RBAC, no egress — the cleanest yellow-zone pattern |
| Collaborative notebooks / apps | Hex; Dataiku | Hex: SQL/Python notebooks → shareable apps, SOC 2, VPC options. Dataiku: enterprise DS platform common in asset management; governance features built in |
| Visual analytics workflow | KNIME; Posit (Shiny/Workbench) | Self-hostable; KNIME strong for no-code data pipelines; Posit for the R-leaning analyst tier |
| Spreadsheet on-ramp | Python in Excel + Copilot | Where the existing EUC estate meets the new world; governed by M365 tenancy — the migration path, not the destination |

## Explicitly below the enterprise bar (name-and-exclude in the primer)

| Family | Examples | Why excluded (§6.1) |
|---|---|---|
| Hosted vibe-coding builders | Lovable; v0; Bolt | SaaS-only, code + data on vendor infra, thin enterprise controls — fine for throwaway prototypes on public data (red zone) at most |
| Hosted app/agent platforms | Replit; Glide; Softr; Airtable-class builders | Predominantly hosted multi-tenant; some claim enterprise tiers — verify, but default posture is exclude |
| Consumer automation | Zapier (consumer/team tiers) | SMB posture, credential sprawl; enterprise tier exists — if allowed at all, only via governed connections |

---

## Mapping to the primer

- **Ch 6.2** agentic coding → first two tables. **Ch 6.3** internal-tool builders.
  **Ch 6.4** low-code suites. **Ch 6.5** automation/iPaaS/RPA. **Ch 6.6** analytics
  self-service. Agent frameworks and managed agent builders extend §6.2 or earn a
  §6.2b — they're where citizen dev goes agentic (Ch 9 Run/Fly).
- **Builder-spectrum fit:** frameworks/CLIs → technical analyst and up; internal-tool
  builders + Streamlit/Hex → analyst tier; Power Platform / Copilot Studio /
  automation → ops and power-user tier; Python-in-Excel → the on-ramp.
- **Trust-zone fit:** cloud-native runtimes (Bedrock, Vertex, Streamlit-in-Snowflake,
  self-hosted n8n/Retool) are the yellow-zone workhorses; hosted-only tools cap at
  red zone.

## Caveats

- Every certification, deployment-mode, and ownership claim here needs a dated
  primary source before publication (`raw/sources/` per repo rules).
- This market churns faster than the security categories: agent-framework
  consolidation (AutoGen/Semantic Kernel → MS Agent Framework) and low-code vendors
  bolting on "AI agent" tiers mean names and positioning may already be stale.
- Pricing/licensing (Power Platform especially) is a known trap-field — needs its
  own verification pass.
