---
type: vendor
name: SharePoint / OneDrive (Microsoft)
slug: sharepoint
categories: [content-sources]
layer: retrieval
aliases: [SharePoint Online, OneDrive for Business]
website: https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
founded: 2001
hq: Redmond, WA, USA
ownership: public
ownership_detail: First-party Microsoft 365 service (Microsoft Corp, NASDAQ: MSFT)
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, on-prem]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [first-party, content-source, rag-source, microsoft]
---

# SharePoint / OneDrive (Microsoft)

**One-liner** — Microsoft 365's document and collaboration repositories — for most enterprises the single biggest pile of unstructured content, and therefore the primary corpus enterprise RAG and Copilot retrieve from.

**What it does** — SharePoint Online (sites/libraries) and OneDrive for Business (personal storage) hold the documents, intranet pages, and files knowledge workers create. In an AI stack they are **content sources**: the data RAG pipelines and [microsoft-365-copilot](microsoft-365-copilot.md) index and answer over. The governance concern is not the product but its **permissions** — RAG inherits whatever access model (often over-shared) lives in SharePoint, which is exactly why [entitlement-aware-rag](../categories/entitlement-aware-rag.md) and DSPM exist.

**Where it sits in the stack** — [content-sources](../categories/content-sources.md) in the retrieval layer (Day-1 *if* doing RAG). Lethal-trifecta role: it is the **sensitive-data** leg — the trove an attacker wants exfiltrated. Pairs with [microsoft-purview](microsoft-purview.md) (classification/DLP) and [microsoft-graph](microsoft-graph.md) (entitlement-aware retrieval).

**Deployment & architecture** — SaaS (SharePoint Online / OneDrive in Microsoft 365); legacy on-prem SharePoint Server still exists. Surfaced to AI via Microsoft Graph, Copilot connectors, and third-party RAG ingestion.

**Positioning & differentiators** — Not a security product; it is the *content* the rest of the stack governs. Sibling content sources: [confluence](confluence.md), [google-drive](google-drive.md).

**Ownership, funding & M&A** — First-party Microsoft 365 service (Microsoft Corp, public, NASDAQ: MSFT). No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 RAG input, not a buying decision — you already own it. The real work is fixing SharePoint permissions and labeling **before** pointing an LLM at it, so RAG does not surface MNPI or over-shared files to the wrong users.

**Competitors / alternatives** — [confluence](confluence.md), [google-drive](google-drive.md) (peer content repositories).

## Sources
- [raw/sources/2026-06-28--retrieval-infra--first-party-ownership.md] — supports: Microsoft 365 ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); brief stub — RAG content source, not a security product. Ownership Microsoft (public, high). Flagged permissions/DSPM as the real governance concern.
