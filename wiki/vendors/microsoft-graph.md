---
title: Microsoft Graph
type: vendor
name: Microsoft Graph
slug: microsoft-graph
categories: [entitlement-aware-rag]
layer: retrieval
aliases: [Microsoft Graph API, Microsoft Search semantic index, Graph connectors, Copilot connectors]
website: "https://developer.microsoft.com/graph"
founded:                            # N/A — Microsoft platform/API, not a standalone company
hq: Redmond, WA (Microsoft)
ownership: public
ownership_detail: "Microsoft Corporation (NASDAQ: MSFT)"
ownership_confidence: high
funding_total:                      # N/A — first-party Microsoft platform
last_funding:                       # N/A
deployment: [saas, api]
target_customer: enterprise / regulated (any Microsoft 365 tenant; permission-aware grounding requires paid M365 Copilot licenses)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [microsoft, m365, copilot, retrieval, semantic-index, graph-connectors]
---

# Microsoft Graph

**One-liner** — The unified API and semantic index over your Microsoft 365 data (SharePoint, OneDrive, Exchange, Teams) that makes Microsoft 365 Copilot permission-aware: Copilot grounding only retrieves content the asking user already has rights to.

**Categories** — [entitlement-aware-rag](../categories/entitlement-aware-rag.md)

## What it does

Microsoft Graph is the single REST API and data fabric that exposes everything inside a Microsoft 365 tenant — mail, files, calendar, chats, sites, people, and the relationships between them. For the AI-governance reader, the part that matters is the **semantic index**: Microsoft builds a tenant-wide and per-user lexical + vector index over text-based M365 content (SharePoint files, OneDrive, mailbox content, OneNote, web pages) and uses it to ground Microsoft 365 Copilot. When a user prompts Copilot, the grounding step queries Graph and the semantic index, retrieves the most relevant passages, and appends them to the LLM prompt.

The job it does for governance: **permission-trimmed retrieval ("security trimming")**. The index "only surfaces the results to a user if the user already has access to the content controlled by role-based access control," and Microsoft "continue[s] to honor the user identity-based access boundary so that the grounding process only accesses content that the current user is authorized to access." In other words, Copilot inherits the exact SharePoint / OneDrive / Exchange ACLs a user already has — it does not create new access rights and cannot be made to read what the user couldn't already open. That is precisely the entitlement-aware-RAG property a buyer is looking for in this layer.

Graph also covers **external data** via Copilot connectors (Graph connectors), so the same permission-aware retrieval extends beyond native M365 content (see below).

## Where it sits in the stack

- **Category:** [entitlement-aware-rag](../categories/entitlement-aware-rag.md) (primary). **Layer:** retrieval.
- **Lethal-trifecta role:** addresses the **sensitive-data** leg. It is the access-control plane for what an LLM is allowed to retrieve — it constrains the "private data" the model can see to the user's existing entitlements. It does not, by itself, address untrusted-input (prompt injection) or egress/exfiltration; those need a runtime AI firewall, DLP, or browser/egress controls layered on top.
- **Trust zone:** lives inside the M365 tenant (green/trusted zone), enforcing the identity boundary at retrieval time.
- It is the engine underneath [microsoft-365-copilot](microsoft-365-copilot.md); the two are best read together (Copilot is the assistant UX, Graph + semantic index is the retrieval/entitlement substrate).

## Deployment & architecture

- **Cloud API, part of Microsoft 365.** Nothing to install; Graph and the semantic index are SaaS, automatically enabled, and "can't be disabled." Indexing requires no admin involvement. A semantic index is generated for users with a **paid Microsoft 365 Copilot license** (the index is what permission-aware Copilot grounding runs on).
- **Index residency:** tenant-level index stored in an isolated per-tenant container in the SharePoint region; EUDB customers stored in EU/EFTA datacenters; multi-geo boundaries respected. Prompts/responses/indexed data are **not** used to train foundation models. Purview Customer Key (BYOK) is supported.
- **Graph / Copilot connectors (external data):** two modes —
  - **Synced connectors** crawl and index external sources into the Graph index via the Microsoft Graph connectors API. Each ingested item carries content, metadata, and an **ACL that enforces permissions**, so "Search and Copilot only show items to users who have access in the source system." 100+ prebuilt connectors (Box, Dropbox, Google Drive, Confluence, Salesforce, ServiceNow, SAP, Workday, Jira, SQL/Oracle, network shares); custom connectors via the Agents Toolkit / connectors API; on-prem via the **Microsoft Graph connector agent**.
  - **Federated connectors** use **MCP** to fetch data live at query time (OAuth 2.0, read-only) without indexing — for sensitive/dynamic sources that shouldn't be indexed.
- **Integrations:** Microsoft Entra ID (identity), Microsoft Purview (DLP, sensitivity labels, DSPM for AI, Customer Key), SharePoint Advanced Management / Syntex (oversharing remediation), Copilot Studio / Agents Toolkit (custom agents grounded on Graph).

## Positioning & differentiators

- **Default, first-party entitlement-aware RAG for the Microsoft estate.** If a fund runs M365 + Copilot, Graph is the retrieval and permission-trimming layer — there is no separate purchase decision; it's the substrate Copilot already uses. Its differentiator over third-party RAG/assistant vendors is that it reuses the *exact same* M365/SharePoint access-control checks the rest of the tenant uses, in real time, rather than maintaining a parallel permissions copy.
- **Versus [glean](glean.md) and other enterprise-AI-assistants:** Glean and similar build their own unified index across SaaS apps with their own permission-mirroring; Graph is Microsoft-native and strongest where the data already lives in M365. Glean is the cross-stack alternative when the center of gravity isn't Microsoft.
- **Versus [knostic](knostic.md) and [microsoft-purview](microsoft-purview.md):** these are *complements*, not substitutes. Graph faithfully enforces whatever permissions exist — which is exactly why **oversharing** is its well-known weakness (below). Knostic adds a need-to-know/knowledge-level control on top of Copilot answers; Purview adds DSPM-for-AI, sensitivity-label-based trimming, and DLP that can block Copilot from processing labeled content.
- The retrieval mechanics are a documented Microsoft platform, not a marketing claim; the permission-trimming behavior is stated explicitly in Microsoft Learn.

### The oversharing caveat (important)

Graph's security trimming is only as good as the underlying ACLs. Because SharePoint "by default sets sharing settings to the most permissive option," many tenants have over-permissioned content (org-wide "Everyone except external users" links, broken inheritance, ownerless sites). Copilot then makes that latent exposure trivially discoverable via natural-language prompts — it surfaces nothing the user couldn't already reach, but it removes the friction that previously hid it. Indexing itself does **not** change permissions. Microsoft's own remediation path is **SharePoint Advanced Management (Syntex)**: Content Management Assessment, Data Access Governance reports (site-permissions baseline, EEEU, sharing-links activity), Restricted Access Control, and **Restricted Content Discovery** (keeps content out of Copilot/search without changing permissions) — plus Purview sensitivity labels and DLP. This is the gap that [knostic](knostic.md), [microsoft-purview](microsoft-purview.md), and [varonis](varonis.md)-style data-access-governance tools sell against.

## Ownership, funding & M&A

- **Ownership:** Microsoft Graph is a first-party Microsoft product/API, not an independent company. Owned by **Microsoft Corporation (NASDAQ: MSFT)**; `ownership: public`, confidence **high**. The prior stub's `ownership: independent` was incorrect and is corrected here.
- **Founded / funding / HQ:** N/A as company-level fields — Graph is a Microsoft platform (Microsoft HQ: Redmond, WA). No founding year or funding applies; left blank by design.
- **M&A:** none applicable (not an acquisition target; it's the platform). No seed M&A flag.

## CTO / hedge-fund lens

- **Day-1 if you run Microsoft 365 + Copilot.** For a Microsoft-centric fund, Graph isn't optional or even separately bought — it's the retrieval/entitlement engine you get the moment you license Copilot. The Day-1 work is not "deploy Graph," it's **govern what Graph will faithfully expose**: run the oversharing assessment and tighten SharePoint/OneDrive permissions *before* turning Copilot loose, or Copilot becomes a fast index into your worst-permissioned content.
- **Why it matters for a regulated shop:** the permission-aware grounding gives you a defensible "Copilot only sees what the user already could" story, and indexed data stays in-tenant and out of model training — both useful for compliance and information-barrier posture. It is **not** an information-barrier or MNPI control by itself; ethical-wall enforcement still needs Purview information barriers + correctly scoped SharePoint permissions.
- **SR 11-7 / model risk:** not a model-risk tool. It's data-access plumbing; relevant to data-governance and access-control controls, not model validation.
- **Fit:** **high** for any fund standardized on Microsoft 365. Low/irrelevant for shops whose knowledge lives outside M365 (there, look at [glean](glean.md) or building on a different RAG stack), though Graph connectors can pull external sources in.

## Competitors / alternatives

- [glean](glean.md) — cross-SaaS enterprise search/assistant with its own permission-mirroring index (the main non-Microsoft alternative).
- [microsoft-365-copilot](microsoft-365-copilot.md) — the assistant that consumes Graph; read together, not a competitor.
- [knostic](knostic.md) — adds need-to-know / knowledge-level controls on top of Copilot to curb oversharing.
- [microsoft-purview](microsoft-purview.md) — DSPM for AI, sensitivity-label trimming, DLP for Copilot; complement.
- [varonis](varonis.md) — data-access-governance / least-privilege remediation that reduces the oversharing surface Graph would otherwise expose.

## Open questions / to verify

- Exact latency / freshness of ACL changes propagating to the index (docs say tenant-document updates index "immediately," new shared SharePoint docs "daily" — confirm how fast a *revoked* permission is reflected in trimming).
- How federated (MCP) connectors handle audit/logging vs synced connectors for compliance evidence.
- Whether Restricted Content Discovery covers connector-ingested external content or only SharePoint sites.

## Sources

- [Semantic indexing for Microsoft 365 Copilot — Microsoft Learn](https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot) — fetched 2026-06-28 — supports: semantic index built from Graph; permission-trimmed grounding honors user identity-based access boundary / RBAC; auto-enabled, can't be disabled; index residency; not used to train models; oversharing-vs-indexing distinction; confidence: high.
- [Copilot connectors overview — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview) — fetched 2026-06-28 — supports: Graph/Copilot connectors (synced vs federated/MCP); each item carries an ACL; permission-based filtering so users only see source-permitted content; 100+ prebuilt connectors; on-prem connector agent; confidence: high.
- [Get ready for Microsoft 365 Copilot with SharePoint Advanced Management — Microsoft Learn](https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management) — fetched 2026-06-28 — supports: Copilot respects existing permissions; oversharing risk and remediation (Content Management Assessment, Data Access Governance reports, Restricted Access Control, Restricted Content Discovery); confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; rewrote from stub. Corrected ownership (independent → public, Microsoft/MSFT, confidence high). Established Microsoft Graph as the unified API + semantic index that gives M365 Copilot permission-trimmed (entitlement-aware) RAG grounding — honors user identity-based access boundary / SharePoint ACLs, does not create new access. Documented Graph/Copilot connectors (synced vs federated MCP, each item carries an ACL) for external data, and the well-known oversharing caveat + Microsoft's SharePoint Advanced Management / Purview remediation. Set hedge_fund_fit: high, trifecta_relevance: [sensitive-data], deployment: [saas, api], status: researched, sources_count: 3. No M&A flag (first-party Microsoft platform). No hard contradictions.
