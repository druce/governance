---
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
exists. Distinct from [[ai-runtime-security]] (protects the AI apps you build) — this
governs the AI your people reach for. It is the usage-governance complement to the
data-side [[dlp]] control.

## Lethal-trifecta role

Breaks the **sensitive-data** and **egress** legs at the human/agent boundary: it
prevents sensitive data from reaching an untrusted external model (egress control)
and redacts or blocks the sensitive content itself before it leaves
(sensitive-data control). It polices the edge between the green zone (internal data)
and the red zone (public AI on the open internet) — the velvet rope precisely where
employees would otherwise hand data to an outside model.

## Vendors

**AI-native shadow-AI / access-governance specialists**
- [[witnessai]] — intent-aware inline policy on prompts and responses (primary here; cross-listed in [[ai-runtime-security]]).
- [[harmonic-security]] — shadow-AI discovery and data-protection for prompts.
- [[aurascape]] — AI activity discovery and inline governance across AI apps.
- [[lanai]] — discovery and governance of AI usage embedded in SaaS.
- [[wald-ai]] — AI usage discovery plus prompt redaction.
- [[portal26]] — AI usage visibility, governance, and forensics.
- [[nudge-security]] — SaaS/AI discovery and shadow-AI governance (primary in [[ai-spm]]; cross-listed in [[sspm]]).
- [[reco]] — SaaS/AI posture and shadow-AI discovery (primary in [[ai-spm]]; cross-listed in [[sspm]]).
- [[quilr]] — AI usage governance / data protection (cross-listed in [[ai-spm]]).

**Data-security lineage doing AI usage governance**
- [[cyberhaven]] — data-lineage DLP extended to data-flow visibility into AI usage (primary in [[dlp]]).
- [[lasso-security]] — AI/agent security plus shadow-AI (primary in [[dlp]]).
- [[prompt-security]] — prompt inspection / AI DLP with shadow-AI discovery (primary in [[dlp]]).

**Network/SASE incumbents with an "AI guard" module**
- [[zscaler]] — Zscaler AI Guard, shadow-AI control inside its SSE platform (primary in [[network-security-sase]]).
- [[netskope]] — Netskope One AI controls inside its CASB/SSE platform (primary in [[network-security-sase]]).
- [[grip-security]] — SaaS/identity discovery extended to shadow AI (primary in [[sspm]]).

## Consolidation / M&A dynamics

Per seed flags (unverified — to confirm in research): Prompt Security flagged as
acquired by [[sentinelone]]. The structural dynamic here is platform encroachment
rather than startup-to-startup rollups: SASE/CASB incumbents (Zscaler, Netskope,
Palo Alto) are adding "AI guard" modules that compete directly with the AI-native
specialists (WitnessAI, Harmonic, Aurascape), and DLP/SSPM vendors (Cyberhaven,
Grip, Reco, Nudge) are extending into the same shadow-AI discovery job. Buyers must
decide whether shadow-AI is a feature of their existing SSE/DLP or a standalone tool.

## Adjacent categories

- [[dlp]] — the data-exfiltration control this layer overlaps most with; AI access governance is content/intent-aware DLP aimed specifically at AI usage. Cyberhaven, Prompt Security, Lasso straddle both.
- [[network-security-sase]] — the foundation-layer proxy that sees AI *traffic*; this layer adds prompt-level intent. Zscaler/Netskope appear in both.
- [[ai-runtime-security]] — protects internally built AI apps; this governs employee/agent use of external AI. WitnessAI and the DLP-lineage vendors span both.
- [[ai-spm]] — inventories and governs AI *assets/agents* org-wide; shadow-AI discovery is an input. Reco, Nudge, Quilr span both.
- [[enterprise-browser]] / [[browser-security-extension]] — an alternative enforcement point for the same shadow-AI problem at the browser.

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
- Cross-listing with [[dlp]] (Cyberhaven, Prompt Security, Lasso) and [[ai-spm]] (Reco, Nudge, Quilr) means the same vendor may be selected in multiple categories; that's expected but note it for analysis.
- M&A: Prompt Security flagged → SentinelOne. Show recognizable names.

## Open taxonomy questions

- Is "shadow-AI / insider risk" (CSV name) the same buy as "CASB for AI / access governance" (doc name)? Merged here on the judgment that it's one job with two labels — confirm in research.
- The line with [[dlp]] is blurry: AI access governance is essentially AI-aware DLP plus discovery. Worth a stated rule (intent/usage-governance here; content/lineage exfiltration control in DLP).
- Does the SASE-module approach (Zscaler/Netskope) eventually absorb the standalone category, making this a feature rather than a market?
