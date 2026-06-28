---
title: Enterprise Content Sources
type: category
name: Enterprise Content Sources
slug: content-sources
layer: retrieval
priority: day-1
trifecta_role: sensitive-data
maps_to_seed_doc: Content Sources
maps_to_seed_csv: "— (folded into Enterprise Chat & RAG)"
vendor_count: 3
status: drafted
last_updated: 2026-06-28
---

> **STUB.** This is the plumbing layer, not the governance layer. The part that actually matters for keeping an AI from leaking data is **[entitlement-aware-rag](entitlement-aware-rag.md)** — read that page. This page exists to name the slot.

## Business objective

The systems of record an AI assistant reads from: where your knowledge actually lives — the SharePoints, Drives, and wikis the model retrieves from when answering. By itself, "content sources" is just your existing enterprise document estate. It becomes an AI concern the moment a RAG pipeline or assistant is pointed at it, because the AI inherits whatever access (and whatever permission sprawl) those repositories already carry.

## When you need it

Day-1 *if you are doing RAG* — but only in the trivial sense that you already have these systems. You are not buying a "content source"; you are deciding which existing repositories an assistant is allowed to index, and confirming their permission models are clean before you connect them. The real Day-1 work is the entitlement layer on top, not the repositories themselves.

## Lethal-trifecta role

This is the **sensitive-data** leg — it *is* the sensitive data. Content sources sit in the green/yellow zone (internal systems of record). Connecting an assistant to them without an entitlement-aware retrieval layer is how the sensitive-data leg gets exposed to an untrusted prompt.

## Vendors

These are infrastructure/systems of record, not a competitive survey shortlist:

- [sharepoint](../vendors/sharepoint.md) — SharePoint / OneDrive; the dominant enterprise document store and the default corpus for Microsoft-centric RAG.
- [confluence](../vendors/confluence.md) — Atlassian wiki; common engineering and internal-knowledge source.
- [google-drive](../vendors/google-drive.md) — Google Workspace document store; the Google-shop equivalent of SharePoint/OneDrive.

(Plus everything else with an API: ticketing systems, CRMs, file shares, data warehouses.)

## Consolidation / M&A dynamics

N/A — these are incumbent platform vendors (Microsoft, Atlassian, Google), not a churning startup category.

## Adjacent categories

- [entitlement-aware-rag](entitlement-aware-rag.md) — the governance layer that decides which of these documents a given user's query is allowed to see. The part that matters.
- [vector-retrieval](vector-retrieval.md) — the index built on top of these sources.
- [data-access-governance](data-access-governance.md) — the audit of who can open which file *before* an AI ever indexes it; the cleanup you do here pays off directly in RAG safety.
- [dspm](dspm.md) — knows where the sensitive data inside these sources actually lives.

## Survey

Folded into the [enterprise-ai-assistant](enterprise-ai-assistant.md) / [entitlement-aware-rag](entitlement-aware-rag.md) survey questions. No standalone survey question — respondents do not "evaluate and select" SharePoint vs Google Drive as an AI decision; they already own one.

## Open taxonomy questions

- Whether this slot deserves a page at all, or should be a section inside [entitlement-aware-rag](entitlement-aware-rag.md). Kept separate to mirror the seed doc's layer-cake row, but it carries no buying decision of its own.
