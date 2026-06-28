---
type: category
name: Entitlement-Aware RAG
slug: entitlement-aware-rag
layer: retrieval
priority: day-1
trifecta_role: sensitive-data
maps_to_seed_doc: Entitlement-Aware RAG
maps_to_seed_csv: "(in Enterprise Chat & RAG)"
vendor_count: 3
status: drafted
last_updated: 2026-06-28
---

## Business objective

Retrieval that remembers your permissions: a permission-aware retrieval layer so an AI assistant only surfaces documents the asking user was *already* allowed to see. This is the single most under-appreciated control in the whole RAG stack. The failure mode is concrete and common: the finance analyst asks the company assistant "what's our comp philosophy," and because the HR planning deck was indexed without carrying its access-control list, the model cheerfully cites everyone's salaries.

RAG breaks the normal permission model. In a traditional app, you open a file and the file system checks whether *you* can read it. In naive RAG, the *retriever* opens every file on the user's behalf with a single service-account identity, embeds the contents, and the model answers from whatever it found. The original per-user ACL is gone unless something deliberately re-enforces it at query time. Entitlement-aware RAG is that something: it propagates the user's identity through retrieval so the index is filtered to *their* effective permissions before the model ever sees a snippet.

There are two broad ways to get there:
- **Security-trimming at query time** — the retriever filters candidate documents against the user's live entitlements (from the source system or an identity graph) on every request. Correct if the underlying permissions are correct.
- **Permission-aware indexing / overlay guardrails** — the index stores ACLs alongside embeddings, and/or a policy layer sits above retrieval to catch oversharing the source permissions would have allowed (the "your permissions are a mess and the AI just made that searchable" problem).

## When you need it

**Day-1, and non-negotiable, the moment you point an assistant at internal content.** Not Day-2, not "after the basics." If you are doing RAG over real corporate data — and an [enterprise-ai-assistant](enterprise-ai-assistant.md) like Copilot or Glean *is* RAG over your corporate data — this is the control that stands between a convenient assistant and a self-service data-leak engine. For a hedge fund the stakes are sharp: MNPI, deal docs, LP/investor data, comp, and legal-privileged material are exactly the things an over-broad assistant will helpfully retrieve and summarize.

Two hard truths a CTO should internalize before go-live:
1. **RAG inherits your permission sprawl and makes it instantly queryable.** Years of "share with Everyone" folders that were safe-by-obscurity become a one-prompt search away. This is why [data-access-governance](data-access-governance.md) cleanup is a prerequisite, not a parallel nice-to-have.
2. **Security-trimming is necessary but not sufficient.** Even with perfect ACL enforcement, the AI can *infer* sensitive facts from documents the user is technically allowed to see, or aggregate fragments into something none of them individually exposed. This "knowledge boundary" / inference problem is the gap pure-trimming vendors don't close.

## Lethal-trifecta role

This is the **sensitive-data** control in the retrieval layer — it governs *which* sensitive data reaches the model context for a given user. It does not break the trifecta on its own; it bounds the blast radius of the sensitive-data leg. Combined with [ai-runtime-security](ai-runtime-security.md) (the untrusted-input/egress legs) it is part of how you keep all three legs from lining up: an injected prompt that tries to make the assistant exfiltrate the HR deck fails because the deck was never retrievable for that user in the first place.

It lives across the yellow and green zones: the retrieval pipeline reaches into internal systems of record (green), and the assistant consuming it may face untrusted input (red/yellow). Entitlement-aware RAG is the membrane between them.

## Vendors

This is a small, somewhat mixed slot — part platform feature, part dedicated overlay. Three named anchors, grouped by what they actually are:

**Assistant/platform with built-in entitlement enforcement**
- [glean](../vendors/glean.md) — enterprise search + assistant whose core differentiator is a permissions-mirroring index: it crawls connected [content-sources](content-sources.md), replicates each source's ACLs into its own index, and security-trims results to the asking user at query time. Also listed under [enterprise-ai-assistant](enterprise-ai-assistant.md) because for many buyers Glean *is* the assistant and the entitlement layer in one.
- [microsoft-graph](../vendors/microsoft-graph.md) — the identity-and-permissions substrate Microsoft 365 Copilot retrieves through; Copilot honors existing Microsoft 365 / SharePoint permissions via Graph, which is why Microsoft-shop RAG entitlement largely reduces to "are your Graph/SharePoint permissions actually clean." A capability inside the platform rather than a product you buy separately.

**Dedicated overlay / knowledge-boundary guardrail**
- [knostic](../vendors/knostic.md) — purpose-built for the gap the above leave open: it sits over Copilot/Glean-class assistants and enforces *need-to-know* knowledge boundaries, catching oversharing and inference that raw ACL-trimming permits. Positioned as the "your permissions are messier than you think, and the AI just exposed it" remediation layer. Also cross-listed under [enterprise-ai-assistant](enterprise-ai-assistant.md).

## Consolidation / M&A dynamics

No seed-flagged acquisitions in this slot. The structural dynamic to watch is **absorption into the platform**: as [enterprise-ai-assistant](enterprise-ai-assistant.md) vendors (Microsoft via Graph, Glean natively) make entitlement-aware retrieval table-stakes, the open question is whether dedicated overlays like Knostic remain standalone or get acquired by an assistant/[data-access-governance](data-access-governance.md) vendor. Treat any specific M&A claim as unverified pending research.

## Adjacent categories

- [content-sources](content-sources.md) — the repositories whose permissions this layer must faithfully mirror; garbage-in if their ACLs are wrong.
- [vector-retrieval](vector-retrieval.md) — the index this control wraps; an entitlement layer is what turns a raw vector store into safe RAG.
- [enterprise-ai-assistant](enterprise-ai-assistant.md) — the primary consumer; entitlement-aware RAG is the safety precondition for turning an assistant loose on internal data.
- [data-access-governance](data-access-governance.md) — the upstream cleanup ("who can open which file") that determines whether security-trimming yields correct results; do this *first*.
- [dspm](dspm.md) — knows where sensitive data lives, so you can prioritize which corpora need the tightest boundaries.
- [ai-runtime-security](ai-runtime-security.md) — guards the prompt/response path (injection, exfiltration) that sits in front of retrieval.

## Survey

**Question.** For governing what your AI assistant can retrieve, which entitlement-aware RAG / permission-enforcement approach are you using or evaluating? (Select all that apply.)

**Answer options.**
- Glean (native permissions-mirroring index)
- Microsoft Graph / Copilot built-in permission enforcement
- Knostic (knowledge-boundary / oversharing overlay)
- Built-in security-trimming from our vector/search platform (e.g. Azure AI Search ACLs)
- Custom in-house entitlement enforcement
- Not addressed yet / unaware this was needed
- Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.**
- This question doubles as a **maturity signal**. A respondent who picks "Not addressed yet" while also running an internal-data assistant has an open exposure — worth a follow-up.
- Heavy overlap with [enterprise-ai-assistant](enterprise-ai-assistant.md): Glean and Microsoft appear in both. Frame this question as "how do you enforce *who sees what*," distinct from "which assistant do you use," or respondents will just re-pick their assistant.
- Expect confusion between "we honor existing permissions" (trimming) and "we catch oversharing/inference" (knowledge boundary). The two added rows (platform trimming vs Knostic-style overlay) exist to separate those; consider a one-line explainer.
- Small real shortlist — most buyers will land on a platform feature rather than a third product. Knostic is the niche but governance-significant standalone option.

## Open taxonomy questions

- **Feature vs category.** Much of this is delivered as a capability inside [enterprise-ai-assistant](enterprise-ai-assistant.md) (Glean, Copilot/Graph) rather than a standalone purchase. Kept as its own category because the *control* is governance-critical and warrants a survey question even when the *vendor* is shared.
- **Boundary with [data-access-governance](data-access-governance.md).** DAG fixes the permissions; entitlement-aware RAG enforces them at retrieval time. Clean conceptual split, but vendors and buyers blur them — flag for the final taxonomy pass whether to cross-reference more tightly.
- Whether to split "security-trimming" and "knowledge-boundary/inference control" into two sub-categories if the vendor set grows.
