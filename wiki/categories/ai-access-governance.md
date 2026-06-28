---
title: AI Access Governance (CASB for AI) / Shadow-AI
type: category
name: AI Access Governance (CASB for AI) / Shadow-AI
slug: ai-access-governance
layer: model-prompt
priority: day-1
trifecta_role: sensitive-data / egress
maps_to_seed_doc: AI Access Governance (CASB for AI)
maps_to_seed_csv: Shadow-AI / Insider risk
vendor_count: 11
status: drafted
last_updated: 2026-06-28
---

# AI Access Governance (CASB for AI) / Shadow-AI

## Business objective

The velvet-rope host for AI. This layer governs how employees and agents *use* AI:
it discovers shadow AI (the unsanctioned ChatGPT/Claude/Gemini accounts and the
hundreds of AI-enabled SaaS features people quietly turn on), and enforces inline
policy on what data is allowed to flow to which model. The defining trait is
**intent-aware, not just destination-aware** — it reads the prompt at the door,
waves sanctioned use through, and stops sensitive data leaving on a prompt's arm,
rather than simply blocking a domain.

Think of it as a CASB reframed for the AI era. Where a SASE proxy sees "traffic to
openai.com," AI access governance sees "this user is about to paste a client list
into a public model" and acts on the content and intent.

## When you need it

Day-1 if employees use public AI tools — which they do, with or without approval.
Shadow AI is the single most common real exposure for a firm that hasn't formally
"done AI" yet: people are already pasting MNPI, deal terms, and client data into
consumer chatbots. For a hedge fund this is acute (MNPI/insider-risk, MAR), so
discovery + inline control is an early priority even before any internal AI app
exists. Distinct from [ai-runtime-security](ai-runtime-security.md) (protects the AI apps you build) — this
governs the AI your people reach for. It is the usage-governance complement to the
data-side [dlp](dlp.md) control.

## Lethal-trifecta role

Breaks the **sensitive-data** and **egress** legs at the human/agent boundary: it
prevents sensitive data from reaching an untrusted external model (egress control)
and redacts or blocks the sensitive content itself before it leaves
(sensitive-data control). It polices the edge between the green zone (internal data)
and the red zone (public AI on the open internet) — the velvet rope precisely where
employees would otherwise hand data to an outside model.

## Vendors

**AI-native shadow-AI / access-governance specialists**
- [witnessai](../vendors/witnessai.md) — intent-aware inline policy on prompts and responses (primary here; cross-listed in [ai-runtime-security](ai-runtime-security.md)).
- [harmonic-security](../vendors/harmonic-security.md) — shadow-AI discovery and data-protection for prompts.
- [aurascape](../vendors/aurascape.md) — AI activity discovery and inline governance across AI apps.
- [lanai](../vendors/lanai.md) — discovery and governance of AI usage embedded in SaaS.
- [wald-ai](../vendors/wald-ai.md) — AI usage discovery plus prompt redaction.
- [portal26](../vendors/portal26.md) — AI usage visibility, governance, and forensics.
- [nudge-security](../vendors/nudge-security.md) — SaaS/AI discovery and shadow-AI governance (primary in [ai-spm](ai-spm.md); cross-listed in [sspm](sspm.md)).
- [reco](../vendors/reco.md) — SaaS/AI posture and shadow-AI discovery (primary in [ai-spm](ai-spm.md); cross-listed in [sspm](sspm.md)).
- [quilr](../vendors/quilr.md) — AI usage governance / data protection (cross-listed in [ai-spm](ai-spm.md)).

**Data-security lineage doing AI usage governance**
- [cyberhaven](../vendors/cyberhaven.md) — data-lineage DLP extended to data-flow visibility into AI usage (primary in [dlp](dlp.md)).
- [lasso-security](../vendors/lasso-security.md) — AI/agent security plus shadow-AI (primary in [dlp](dlp.md)).
- [prompt-security](../vendors/prompt-security.md) — prompt inspection / AI DLP with shadow-AI discovery (primary in [dlp](dlp.md)).

**Network/SASE incumbents with an "AI guard" module**
- [zscaler](../vendors/zscaler.md) — Zscaler AI Guard, shadow-AI control inside its SSE platform (primary in [network-security-sase](network-security-sase.md)).
- [netskope](../vendors/netskope.md) — Netskope One AI controls inside its CASB/SSE platform (primary in [network-security-sase](network-security-sase.md)).
- [grip-security](../vendors/grip-security.md) — SaaS/identity discovery extended to shadow AI (primary in [sspm](sspm.md)).

## Consolidation / M&A dynamics

Per seed flags (unverified — to confirm in research): Prompt Security flagged as
acquired by [sentinelone](../vendors/sentinelone.md). The structural dynamic here is platform encroachment
rather than startup-to-startup rollups: SASE/CASB incumbents (Zscaler, Netskope,
Palo Alto) are adding "AI guard" modules that compete directly with the AI-native
specialists (WitnessAI, Harmonic, Aurascape), and DLP/SSPM vendors (Cyberhaven,
Grip, Reco, Nudge) are extending into the same shadow-AI discovery job. Buyers must
decide whether shadow-AI is a feature of their existing SSE/DLP or a standalone tool.

## Adjacent categories

- [dlp](dlp.md) — the data-exfiltration control this layer overlaps most with; AI access governance is content/intent-aware DLP aimed specifically at AI usage. Cyberhaven, Prompt Security, Lasso straddle both.
- [network-security-sase](network-security-sase.md) — the foundation-layer proxy that sees AI *traffic*; this layer adds prompt-level intent. Zscaler/Netskope appear in both.
- [ai-runtime-security](ai-runtime-security.md) — protects internally built AI apps; this governs employee/agent use of external AI. WitnessAI and the DLP-lineage vendors span both.
- [ai-spm](ai-spm.md) — inventories and governs AI *assets/agents* org-wide; shadow-AI discovery is an input. Reco, Nudge, Quilr span both.
- [enterprise-browser](enterprise-browser.md) / [browser-security-extension](browser-security-extension.md) — an alternative enforcement point for the same shadow-AI problem at the browser.

## Survey

**Question:** Which AI access governance / shadow-AI tools are you using or evaluating
to discover unsanctioned AI use and enforce inline policy on what data flows to AI
tools?

**Answer options:** WitnessAI, Harmonic Security, Aurascape, Nudge Security, Lanai,
Cyberhaven, Wald.ai, Portal26, Reco, Zscaler (AI Guard), Netskope One, Other (Please
Specify).

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:**
- Table-stakes / most-recognized AI-native: WitnessAI, Harmonic, Aurascape, Nudge.
- Big overlap risk: respondents who already have Zscaler/Netskope/Palo Alto SASE may not see "shadow-AI" as a separate buy — list the incumbent "AI guard" modules so they're counted, and consider an "already covered by our SASE/DLP" option.
- Cross-listing with [dlp](dlp.md) (Cyberhaven, Prompt Security, Lasso) and [ai-spm](ai-spm.md) (Reco, Nudge, Quilr) means the same vendor may be selected in multiple categories; that's expected but note it for analysis.
- M&A: Prompt Security flagged → SentinelOne. Show recognizable names.

## Open taxonomy questions

- Is "shadow-AI / insider risk" (CSV name) the same buy as "CASB for AI / access governance" (doc name)? Merged here on the judgment that it's one job with two labels — confirm in research.
- The line with [dlp](dlp.md) is blurry: AI access governance is essentially AI-aware DLP plus discovery. Worth a stated rule (intent/usage-governance here; content/lineage exfiltration control in DLP).
- Does the SASE-module approach (Zscaler/Netskope) eventually absorb the standalone category, making this a feature rather than a market?
