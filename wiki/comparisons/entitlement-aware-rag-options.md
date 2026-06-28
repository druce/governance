---
type: comparison
name: Entitlement-Aware RAG — options
slug: entitlement-aware-rag-options
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 14
---

# Entitlement-aware RAG, compared

[[entitlement-aware-rag]] is the **non-negotiable** control once you do RAG: the AI must **never
surface a document the user couldn't already open.** Plain vector search ignores permissions —
ask it "what's our comp plan?" and it will happily retrieve the CEO's file. Entitlement-aware
retrieval enforces the source system's ACLs at query time. For a hedge fund (MNPI, deal teams,
walls between strategies) this is the difference between RAG you can deploy and RAG that leaks.

## The core problem: ACLs at query time

Three things have to line up:
1. **Mirror the source ACLs** — know who can see each document (SharePoint/Drive/Confluence perms).
2. **Enforce at retrieval** — filter candidates by the *asking user's* identity, not post-hoc.
3. **Fix oversharing first** — if SharePoint already over-permits "Everyone," the AI just exposes it
   faster. ACL enforcement ≠ ACL hygiene; you need [[data-access-governance]]/[[dspm]] too.

## The options

| Option | What it is | How it enforces | Best fit |
|---|---|---|---|
| [[glean]] | Standalone work-AI platform + connectors | Mirrors connector ACLs; query-time permission filter | Cross-app enterprise search/assistant; heterogeneous estate |
| [[microsoft-graph]] | The permission/data fabric under M365 Copilot | Native ACL-trimmed grounding in M365 | All-Microsoft shops using Copilot |
| [[knostic]] | Need-to-know layer **on top of** Copilot/Glean | Advisory: detects oversharing/answer leakage, feeds [[microsoft-purview]] | Shops that already have Copilot and need a need-to-know gap-check |
| [[gemini-enterprise]] | Google's enterprise assistant | Honors source ACLs in Google estate | Google Workspace shops |
| [[amazon-q-business]] | AWS enterprise assistant | ACL-aware connector crawling | AWS-centric shops |

## How to tell them apart

- **[[glean]]** is the **independent cross-platform** answer — it connects to many systems, mirrors
  each connector's ACLs, and enforces at query time. Pick it when your knowledge is spread across
  SharePoint + Confluence + Drive + Slack + Jira and you want one governed assistant over all of it.
  ($150M Series F at $7.2B, 2025-06; independent.)
- **[[microsoft-graph]]** isn't a product you buy separately — it's the **ACL-trimmed grounding fabric**
  beneath M365 Copilot. If you're all-Microsoft, entitlement-aware retrieval is largely "on" via Graph.
  The catch: **SharePoint oversharing** is the well-known failure mode (Graph faithfully enforces bad
  ACLs), which is exactly the gap [[knostic]] and Purview address.
- **[[knostic]]** is **not** a retrieval engine — it's a **need-to-know / oversharing detection** layer
  that sits over Copilot/Glean, finds where the assistant *would* answer something a user shouldn't see,
  and feeds remediation into [[microsoft-purview]]. Advisory/read-only, not an inline guardrail. Buy it
  to *audit and close* the gap, not to serve retrieval.
- **[[gemini-enterprise]] / [[amazon-q-business]]** are the hyperscaler-native equivalents of the
  Copilot+Graph story for Google and AWS estates respectively — both honor source ACLs natively.

## CTO / hedge-fund lens
- **Day-1 the moment you do RAG.** Not optional. Decide it by your estate: Microsoft → Copilot+Graph
  (+ Knostic/Purview for oversharing); Google → Gemini Enterprise; mixed/heterogeneous → Glean.
- **The real project is ACL hygiene**, not the retrieval engine. Budget for [[data-access-governance]]
  ([[varonis]], [[veza]], [[cyera]], [[sentra]]) to fix "Everyone" permissions *before* go-live, or the
  AI becomes an oversharing accelerant.
- **Walls/MNPI:** confirm the retrieval layer can honor information-barrier groups (deal teams,
  research/trading walls), not just file ACLs — flag as a diligence question for each option.

## Survey-design notes
- This overlaps the [[enterprise-ai-assistant]] question — Glean, Gemini, Q, Copilot are *both* the
  assistant *and* the entitlement-aware-retrieval layer. Ask "how do you enforce permissions in RAG?"
  separately from "which assistant?" to avoid double-counting.
- Knostic answers a different question (oversharing detection) — keep it distinct from retrieval engines.

## Sources
Per-vendor sourcing on each linked page.

## History
- [2026-06-28] Created from Phase 3 Wave 2 (DLP+RAG and assistants) researched pages.
