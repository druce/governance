---
type: vendor
name: Claude Enterprise (Anthropic)
slug: anthropic-claude-enterprise
categories: [enterprise-ai-assistant]
layer: ux
aliases: [Claude for Work, Claude Enterprise, Anthropic Claude]
website: "https://claude.com/solutions/enterprise"
founded: 2021
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: "Private, independent company. Amazon (~$8B invested since 2023; mid-to-high-teens % stake) and Google (~14% equity, contractually capped at 15%) hold minority investments but do not control it. Filed confidentially for IPO 2026-06-01."
ownership_confidence: high
funding_total: "~$60B+ raised across rounds (as of 2026-06)"
last_funding: "Series H ~$65B at ~$965B valuation (2026); Series G $30B at $380B post-money (2026-02-12)"
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [llm-vendor, ai-assistant, frontier-model]
---

# Claude Enterprise (Anthropic)

**One-liner** — Anthropic's enterprise tier of Claude: the Claude chat assistant (plus Projects and Claude Code) wrapped in the admin, identity, audit, retention, and compliance controls a regulated buyer needs, with a default no-training-on-your-data commitment.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)

## What it does

Claude Enterprise is the governed, tenant-administered version of the Claude assistant aimed at organizations. Employees get the Claude web/desktop app, Projects (shared workspaces with their own knowledge/context), connectors and MCP-based integrations, and Claude Code for agentic coding. Around that, IT/security get an admin console with SSO, SCIM, role-based access, audit logging, custom data-retention controls, and a Compliance API. The pitch to a regulated buyer is that staff get a frontier model for drafting, summarizing, research, and coding without prompts and outputs leaking into model training or escaping audit.

## Where it sits in the stack

This is the **UX / [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)** layer — the chatbot people actually use, the direct competitor to [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [microsoft-365-copilot](microsoft-365-copilot.md), [gemini-enterprise](gemini-enterprise.md), [amazon-q-business](amazon-q-business.md), [perplexity-enterprise](perplexity-enterprise.md), and [glean](glean.md). As a first-party model app it is itself the "AI" that the rest of the governance stack ([ai-access-governance](../categories/ai-access-governance.md), [ai-runtime-security](../categories/ai-runtime-security.md), [dlp](../categories/dlp.md), [comms-surveillance](../categories/comms-surveillance.md)) is meant to wrap or watch.

Lethal-trifecta role: as a sanctioned assistant its main exposure is the **sensitive-data** leg — staff paste confidential/MNPI material into prompts and files. The no-training default plus retention controls plus the Compliance API are how you keep that data governed. It does not itself break the untrusted-input or egress legs; pairing it with a [dlp](../categories/dlp.md) / [ai-access-governance](../categories/ai-access-governance.md) / [comms-surveillance](../categories/comms-surveillance.md) control covers those.

## Deployment & architecture

- **SaaS** multi-tenant assistant (web, desktop, mobile) plus the **Anthropic API / Claude Platform** for programmatic use; also available through Amazon Bedrock and Google Vertex AI (those are the cloud marketplaces' own governance, not Claude Enterprise's admin console).
- **Identity:** SSO/SAML with **domain capture**, **SCIM provisioning** for automated joiner/mover/leaver, role-based access control (RBAC), self-serve seat management. Ties into your IdP (Okta, Entra, etc.).
- **Admin & audit:** audit logs (Owners/Primary Owners can export ~180 days of access metadata — user, timestamp, event type, device, platform, user agent; chat titles/content are *not* in the audit export, only identifiers), usage analytics, spend controls, IP allowlisting, OpenTelemetry (OTEL) monitoring (Enterprise-only).
- **Data retention:** custom retention controls (Enterprise-only); no training on your data by default.
- **Compliance API:** REST feed launched 2025-08-20. On Enterprise it exposes **conversation content** (chats, uploaded files, Projects) plus activity-feed events (logins, admin actions, config changes); on the Platform/API tier only activity events, no conversation content. ~30 typed events, 180-day window for the activity feed. This is the hook archiving/eDiscovery/SIEM vendors plug into.
- **Integrations:** native connectors + **MCP**; 60+ Compliance API integration partners (expanded from 28 announced 2026-05) spanning eDiscovery/archiving (Smarsh-style capture, Proofpoint, [theta-lake](theta-lake.md), RelativityOne/RSMF), SIEM ([crowdstrike](crowdstrike.md), [elastic](elastic.md), [sumo-logic](sumo-logic.md)), DLP ([forcepoint](forcepoint.md), [nightfall-ai](nightfall-ai.md), [zscaler](zscaler.md)), identity ([okta](okta.md), [sailpoint](sailpoint.md), [saviynt](saviynt.md)).

## Positioning & differentiators

- **No-training default + governance posture** is the headline. Anthropic leans on safety/trust branding and was one of the first frontier labs to certify to **ISO/IEC 42001** (AI management system).
- **Compliance API with conversation-content export** is a genuine differentiator for regulated buyers: it lets comms-surveillance/archiving tools ingest the actual prompts, responses, files, and Claude-generated artifacts (including deleted/archived messages, per partner claims like Smarsh) — the same way a bank archives Bloomberg chat or Slack. That directly addresses MAR/MNPI supervision needs, which is unusual among assistant vendors.
- **Claude Code** governance (enterprise-managed agentic coding) is a draw for engineering-heavy shops; admin controls, audit, and spend management extend to it.
- vs [microsoft-365-copilot](microsoft-365-copilot.md): Claude is model-first and not natively wired into your M365 data graph/entitlements, so it lacks Copilot's built-in [entitlement-aware-rag](../categories/entitlement-aware-rag.md) over SharePoint/Graph — you bring data in via connectors/Projects. vs [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md): closest analog; both offer SSO/SCIM/audit/no-training/Compliance-style export — differentiation is model quality, Claude Code, and Anthropic's ISO 42001/safety positioning.

## Ownership, funding & M&A

- **Independent private company**, founded **2021** (Dario & Daniela Amodei and others), HQ **San Francisco**. No seed M&A flag; not acquired. **(confidence: high)**
- **Amazon** has invested ~$8B since 2023 (mid-to-high-teens % stake) and **Google** holds ~14% equity (contractually capped at 15%). These are **minority investments, not control** — Anthropic governs itself. (Both also are major cloud/compute partners.) Verified 2026-06-28.
- Funding has escalated fast: Series F $13B at $183B (2025-09), **Series G $30B at $380B post-money (2026-02-12)**, then a Series H (~$65B, ~$965B valuation). Anthropic **filed confidentially for an IPO on 2026-06-01** — worth a calendar note since public-company status would change its risk/disclosure profile. (as-of 2026-06)

## CTO / hedge-fund lens

- **Day-1.** If your staff are going to use a frontier assistant (they are), a governed tenant with no-training, SSO/SCIM, audit, retention, and an archiving hook is the minimum bar. Claude Enterprise clears it.
- **Comms-surveillance fit is the standout for a fund.** The Compliance API streams conversation content into [comms-surveillance](../categories/comms-surveillance.md) / archiving tools (Smarsh, Proofpoint, [theta-lake](theta-lake.md), RelativityOne), so Claude usage can sit inside the same MAR/MNPI supervision and eDiscovery workflow as email and chat. Few assistant vendors offer this; for a regulated shop it can be the deciding feature.
- **Certifications** cover the regulated checklist: SOC 2 Type I & II, ISO 27001:2022, ISO/IEC 42001:2023, HIPAA-ready with BAA, GDPR/CCPA. Detailed SOC 2 report is available under NDA via the Trust Portal (trust.anthropic.com, on Vanta). Sign a DPA.
- **Caveats to verify in procurement:** (1) **data residency** — Anthropic markets US processing; confirm whether EU/region-pinned data residency is contractually available for your tenant (not clearly documented publicly). (2) The assistant is **not entitlement-aware** over your file stores out of the box — if you want RAG over internal data with permission trimming, that's connectors/Projects work or a separate [entitlement-aware-rag](../categories/entitlement-aware-rag.md) layer. (3) IPO filing (2026-06) means watch for any change in terms/governance.
- **SR 11-7 / model risk:** Claude as a general assistant is typically a productivity tool, not a model in a regulated decision pipeline; if you embed Claude (via API) into a model that informs investment/credit/risk decisions, that instance falls under your model-risk governance ([ai-governance-platform](../categories/ai-governance-platform.md)) regardless of the assistant's certifications.

## Competitors / alternatives

- [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md) — nearest analog (governed frontier assistant).
- [microsoft-365-copilot](microsoft-365-copilot.md) — assistant natively bound to M365 data/entitlements.
- [gemini-enterprise](gemini-enterprise.md), [amazon-q-business](amazon-q-business.md), [perplexity-enterprise](perplexity-enterprise.md), [glean](glean.md).

## Open questions / to verify

- **Data residency:** is EU / region-pinned residency contractually offered for Claude Enterprise tenants, or US-only processing? Not clearly documented publicly.
- Exact audit-log / Compliance-API retention beyond the 180-day activity window for conversation content; whether custom retention extends archival.
- Whether Global Relay (common at funds) has a published Claude Compliance API integration — Smarsh, Proofpoint, Theta Lake, RelativityOne are confirmed; Global Relay was not found as of 2026-06-28.
- Post-IPO (filed 2026-06-01): any change to terms, ownership, or governance.

## Sources

- [What Certifications has Anthropic obtained? — Anthropic Privacy Center](https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained) — fetched 2026-06-28 — supports: SOC 2 Type I/II, ISO 27001:2022, ISO 42001:2023, HIPAA-ready/BAA; scoped to commercial products; confidence: high
- [Enterprise solutions — Claude by Anthropic](https://claude.com/solutions/enterprise) — fetched 2026-06-28 — supports: SSO/SAML + domain capture, SCIM, RBAC, no-training default, custom retention (Enterprise-only), audit logs + OTEL, Compliance API, HIPAA-ready, SOC 2/ISO 27001/GDPR/CCPA; confidence: med (vendor marketing)
- [Get started with Claude Compliance API integrations — Claude Help Center](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations) — fetched 2026-06-28 — supports: Compliance API exposes conversation content on Enterprise; 60+ partners incl. Smarsh/Proofpoint/Theta Lake/RelativityOne for eDiscovery/archiving/supervision; confidence: high
- [Anthropic raises $30B Series G at $380B post-money valuation](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) + [Fortune: Amazon/Google stakes & IPO](https://fortune.com/2026/06/04/amazon-google-billions-anthropic-ipo/) — fetched 2026-06-28 — supports: independent; Amazon ~$8B/mid-high-teens %, Google ~14% capped 15%; Series G/H; IPO filing 2026-06-01; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Claude Enterprise as a Day-1 governed frontier assistant ([enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)). Confirmed enterprise governance posture: no-training default, SSO/SAML + domain capture, SCIM, RBAC, audit logs (~180d), custom retention, IP allowlisting, OTEL, and a Compliance API that exports conversation content into eDiscovery/archiving/SIEM partners (Smarsh, Proofpoint, Theta Lake, RelativityOne) — a strong comms-surveillance fit for funds (hedge_fund_fit: high). Certs: SOC 2 I/II, ISO 27001, ISO 42001, HIPAA-ready/BAA, GDPR/CCPA. Ownership: independent (Amazon/Google minority investments), confidence high; IPO filed 2026-06-01. Open: EU data residency, Global Relay integration. Cached 4 sources.
