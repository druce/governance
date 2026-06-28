---
type: vendor
name: Glean
slug: glean
categories: [entitlement-aware-rag, enterprise-ai-assistant]
layer: retrieval
aliases: [Glean Technologies, Glean Assistant, Glean Work AI]
website: https://www.glean.com
founded: 2019
hq: Palo Alto, California, USA
ownership: independent
ownership_detail: Venture-backed independent; $150M Series F at $7.2B valuation led by Wellington Management (2025-06-10). No M&A.
ownership_confidence: high
funding_total: ~$610M+ (cumulative; ~$610M raised since early 2024 per TechCrunch)
last_funding: Series F, $150M, 2025-06-10 ($7.2B valuation)
deployment: [saas]
target_customer: enterprise / large enterprise (also mid-market)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [enterprise-search, rag, permissions-aware, work-ai, ai-assistant]
---

# Glean

> Primary category: [[entitlement-aware-rag]]. Secondary: [[enterprise-ai-assistant]].

**One-liner** — Permission-aware enterprise search and a "Work AI" assistant/agent platform that connects to all your SaaS apps and answers questions over company data — while enforcing each source system's access controls so a user never sees a document they couldn't already open themselves.

## What it does

Glean indexes content across an enterprise's apps (Google Workspace, Microsoft 365/SharePoint, Slack, Jira, Confluence, Salesforce, Zendesk, GitHub, etc.) and builds a unified search index plus a "Enterprise Knowledge Graph" of people, teams, documents, and relationships. On top of that sits Glean Assistant — a chat/RAG interface that answers natural-language questions, summarizes, and drafts using retrieved company content as grounding, plus an agent/workflow builder ("Work AI") for multi-step tasks. The core value is that employees get a single, current, trustworthy answer over fragmented internal knowledge instead of hunting across a dozen tools.

The non-negotiable control underneath all of it: **document-level permission enforcement at query time.** When Glean ingests content through a connector, it also ingests that source system's access-control lists (ACLs), group memberships, and org hierarchy, and keeps them synced. At query time it filters retrieval to only the documents the asking user is authorized to see — and, per Glean's docs, it defers to and never overrides the source system's permissions ("All document- and app-level permissions continue to be enforced by the original source systems"). This is what makes enterprise RAG safe: without it, an LLM grounded on the corporate index becomes an oversharing machine that surfaces HR files, M&A docs, or comp data to anyone who asks.

## Where it sits in the stack

- **Layer:** retrieval. Primary category [[entitlement-aware-rag]]; also [[enterprise-ai-assistant]].
- **Lethal-trifecta leg:** **sensitive-data**. Glean's job is to make sure the model only ever retrieves data the user is entitled to, so the "access to private data" leg of the trifecta is scoped to per-user authorization rather than the whole corpus. It does *not* by itself break the untrusted-input or egress legs — those need a runtime/guardrail layer ([[ai-runtime-security]]) and DLP/egress controls.
- **Trust zone:** lives in the green/internal zone but reaches across every connected SaaS app; the permission-mirroring is precisely what keeps cross-app retrieval from collapsing trust boundaries.

## Deployment & architecture

- **Delivery:** SaaS (Glean-hosted cloud). Connector-based ingestion with crawlers/APIs into ~100+ enterprise apps; permission/ACL sync via delta updates from source systems and identity providers.
- **Identity:** reads groups and members from the IdP (Azure AD / Entra, Google Groups documented; Okta group-based role assignment noted as not yet supported in the RBAC FAQ as fetched). Glean *reads* identity for group resolution but relies on connector ACLs for document authorization.
- **Interfaces:** web app, browser extension, Slack/Teams surfaces, and an API/SDK + Model Context Protocol (MCP) and agent tooling for building on top of the index.
- **Open item:** whether a customer-managed VPC / self-hosted / on-prem deployment is offered was not confirmable from the primary docs fetched — Glean is primarily a managed cloud service. Flagged below.

## Positioning & differentiators

- **Permission-mirroring is the headline.** Glean built its reputation on getting enterprise-search ACL enforcement right at scale before "RAG" was a buzzword; the permissions story is its core moat versus point LLM tools.
- **Horizontal Work AI platform**, not a single-app copilot — it spans all connected systems rather than being tied to one vendor's suite.
- **Nearest neighbors:** [[microsoft-365-copilot]] (bundled with M365, leans on Microsoft Graph/[[microsoft-graph]] permissions but weaker on non-Microsoft sources), [[gemini-enterprise]] (Google's Agentspace, strong on Workspace), and [[microsoft-graph]] as the underlying permissioned-retrieval substrate for Copilot. Glean's pitch against the platform copilots is breadth of connectors and being suite-neutral; the copilots' pitch against Glean is "already in your license, no extra vendor." Knostic and others have published research probing whether *any* of these (Glean included) fully prevent oversharing when source-system permissions are themselves sloppy — the control is only as good as the upstream ACLs.

## Ownership, funding & M&A

- **Independent, venture-backed.** No acquisition (no seed M&A flag; none found). Ownership confidence: **high**.
- **Series F: $150M at $7.2B valuation, announced 2025-06-10**, led by Wellington Management (new: Khosla Ventures, Bicycle Capital, Geodesic Capital, Archerman Capital; many existing investors incl. Sequoia, Kleiner Perkins, Lightspeed, ICONIQ, Coatue, DST, General Catalyst, Sapphire, IVP, Capital One Ventures, Citi).
- Prior: Series E $260M at $4.6B (Sept 2024); ~$2.2B (Feb 2024). TechCrunch puts cumulative funding at ~$610M since early 2024.
- **ARR:** surpassed $100M ARR in its last fiscal year, less than three years after launch (vendor/TechCrunch).
- **Founded 2019, HQ Palo Alto, CA.** Founders include Arvind Jain (ex-Google, co-founder/CEO).

## CTO / hedge-fund lens

- **Day-1 for the RAG/assistant use case.** If a fund deploys *any* enterprise LLM assistant over internal data, entitlement-aware retrieval is the table-stakes control — you cannot let an assistant surface deal docs, LP data, comp, or MNPI to unauthorized staff. Glean is one of the cleaner answers to that requirement.
- **SR 11-7 / model risk:** Glean is a retrieval/productivity layer, not a trading or valuation model, so it's generally outside formal model-risk governance — but its outputs touch sensitive data, so it belongs in data-governance, access-review, and information-barrier (Chinese wall) controls. The permission-mirroring helps enforce info barriers *if* the source-system ACLs already encode them.
- **Fit:** **medium** for a hedge fund. Strong product, but it is a heavyweight horizontal platform priced for larger enterprises; a 50-person fund may find it oversized versus the platform copilot they already license (M365 Copilot) or a lighter tool. Best fit: larger asset managers with many SaaS silos and a real internal-search pain. Key diligence items: data residency, whether a VPC/isolated tenancy is available, MNPI/information-barrier handling, and how it treats data in model grounding (Glean states it does not train foundation models on customer data — verify contractually).

## Competitors / alternatives

- [[microsoft-365-copilot]] — bundled Microsoft-suite copilot; permissions via [[microsoft-graph]].
- [[gemini-enterprise]] — Google Agentspace / Gemini Enterprise.
- [[microsoft-graph]] — permissioned-retrieval substrate (build-vs-buy alternative for Microsoft-centric shops).
- Other enterprise-search/RAG players (Sinequa, Coveo, Elastic-based builds) compete on retrieval but with varying assistant/agent maturity.

## Open questions / to verify
- Is a customer-managed VPC / self-hosted / on-prem (e.g., "Glean in your cloud") deployment offered, and at what tier? Primary docs fetched did not confirm.
- Data residency options (US/EU) and tenancy isolation specifics for a regulated buyer.
- Exact cumulative funding figure (sources cite ~$610M since early 2024; total-since-inception not pinned).
- Strength of oversharing prevention when upstream source ACLs are misconfigured (independent research e.g. Knostic raises this) — a real diligence question for any permission-mirroring tool.

## Sources
- [Glean Raises $150M Series F at $7.2B Valuation (Glean press)](https://www.glean.com/press/glean-raises-150m-series-f-at-7-2b-valuation-to-accelerate-enterprise-ai-agent-innovation-globally) — fetched 2026-06-28 — supports: Series F size/valuation/date, lead investor, founded 2019 Palo Alto, $100M ARR; confidence: high (vendor primary).
- [Enterprise AI startup Glean lands a $7.2B valuation (TechCrunch)](https://techcrunch.com/2025/06/10/enterprise-ai-startup-glean-lands-a-7-2b-valuation/) — fetched 2026-06-28 — supports: Series F, ~$610M total funding, valuation history, product description, integrations; confidence: high (independent press).
- [Enhancing AI security with permissions-aware frameworks (Glean perspectives)](https://www.glean.com/perspectives/security-permissions-aware-ai) — fetched 2026-06-28 — supports: permission mirroring, real-time IdP sync, query-time enforcement, permission-aware RAG, "never see documents they cannot access"; confidence: med (vendor explainer/marketing).
- [RBAC FAQ (Glean docs)](https://docs.glean.com/administration/identity/roles/faq) — fetched 2026-06-28 — supports: reads IdP groups, never overrides connector ACLs, source systems enforce document permissions, IdP support (Entra/Google Groups); confidence: high (vendor primary docs).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founding 2019 / HQ Palo Alto, independent venture-backed, Series F $150M at $7.2B (2025-06-10, lead Wellington), ~$610M cumulative, >$100M ARR; documented entitlement-aware-RAG mechanics (connector ACL sync + query-time enforcement, defers to source-system permissions). No M&A. Set ownership_confidence high, status researched, hedge_fund_fit medium. Open: VPC/self-hosted availability and data residency unconfirmed.
