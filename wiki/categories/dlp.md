---
type: category
name: Data Loss Prevention (DLP)
slug: dlp
layer: data
priority: day-1
trifecta_role: egress (+ sensitive-data — blocks sensitive data leaving at the exit)
maps_to_seed_doc: Data Loss Prevention (DLP)
maps_to_seed_csv: DSPM / Data Governance / DLP (split — see Survey notes)
vendor_count: 9
status: drafted
last_updated: 2026-06-28
---

# Data Loss Prevention (DLP)

## Business objective

DLP prevents exfiltration of sensitive data via content- and lineage-aware controls.
The seed's metaphor: the **bouncer at the exits** — it stops sensitive data from
walking out the door, now including via AI prompts and pastes into chatbots. Where
[[dspm]] finds and labels data sitting still, DLP acts at the **moment data tries to
move** — into an email, an upload, a USB drive, or a prompt to a public model.

The AI era reshaped DLP: the highest-risk egress path is now an employee pasting
MNPI or client data into ChatGPT, or an agent sending data to an external tool. The
newer "AI-native" DLP vendors focus on that prompt/clipboard surface; the incumbents
focus on classic endpoint/network/email channels.

## When you need it

**Day-1.** For a hedge fund the exfiltration of MNPI, client data, or IP is the
nightmare scenario, and the cheapest place to stop it is at the exit. Classic DLP on
email and endpoints is often already owned; the AI-specific gap — data leaving via
prompts — is what is new and urgent the moment employees use public AI tools (they
do). Pair it with [[ai-access-governance]] for prompt-aware enforcement.

## Lethal-trifecta role

DLP directly breaks the **egress** leg — it is the control that stops sensitive data
from leaving even when an attacker or careless user has lined up the other two legs.
It also operates on the **sensitive-data** leg by recognizing what is sensitive in
the outbound stream. It lives at the boundary between the **green/yellow zones and
the outside (red)**: the last gate before data crosses out of trusted territory.

## Vendors

AI-native / prompt-aware DLP:

- [[cyberhaven]] — data-lineage-based DLP; tracks where data came from to judge
  egress; also [[ai-access-governance]] (data-flow visibility into AI usage).
- [[nightfall-ai]] — content-detection DLP with SaaS/AI coverage and API-based scanning.
- [[mind]] — AI-era DLP focused on data-in-motion.
- [[prompt-security]] — prompt-layer inspection and DLP for AI traffic (also
  [[ai-runtime-security]], [[ai-spm]]); seed flags acquisition (see below).
- [[lasso-security]] — DLP/guardrails for LLM and agent traffic (also
  [[ai-runtime-security]], [[agent-runtime-security]]).
- [[jazz-security]] — AI-native DLP (reclassified here from AI-SOC after research; it is a
  data-protection product, not a SOC analyst).

Platform / incumbent DLP:

- [[microsoft-purview]] — Purview DLP across M365/endpoint/cloud; default for
  Microsoft shops (also [[dspm]]).
- [[netskope]] — inline DLP within its SSE/SASE platform.
- [[forcepoint]] — long-standing enterprise DLP (endpoint/network/email).
- [[cyera]] — DSPM-led vendor extending into DLP/egress controls.

## Consolidation / M&A dynamics

- [[prompt-security]] — acquired by SentinelOne (per seed; unverified — to confirm in
  research).

The pattern: AI-native DLP startups (Prompt Security, and the broader runtime/guardrail
set) are being absorbed by endpoint, SSE, and runtime-security platforms that want a
prompt-aware egress story; classic DLP increasingly ships inside SASE/SSE suites
(Netskope, plus Palo Alto/Zscaler) rather than as standalone agents.

## Adjacent categories

- [[dspm]] — supplies the classification DLP enforces on; the CSV merges them, the
  doc and this taxonomy keep them split (see Survey notes).
- [[ai-access-governance]] — overlaps heavily on the prompt-egress surface; "CASB for
  AI" is largely DLP plus shadow-AI discovery and intent awareness.
- [[ai-runtime-security]] — inspects prompts/responses at the model boundary; several
  DLP vendors (Prompt Security, Lasso) live here too.
- [[network-security-sase]] — the TLS-inspecting layer where inline DLP often runs.

## Survey

**Question.** Which DLP / data-egress controls is your firm using or evaluating,
including controls over data leaving via AI prompts?

**Answer options.** Cyberhaven, Nightfall AI, MIND, Prompt Security, Lasso Security,
Microsoft Purview DLP, Netskope DLP, Forcepoint, Cyera, Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.**
- The seed CSV asks one merged question (`DSPM / Data Governance / DLP`). Per
  taxonomy gap **D2** we split it into [[dspm]] and DLP (this page). Vendors such as
  Cyera, Microsoft Purview, and Netskope answer *both*; expect the same vendor ticked
  on both pages, and reconcile that in analysis.
- Distinguish classic-channel DLP (Purview, Forcepoint, Netskope — often already
  owned) from AI-native prompt DLP (Cyberhaven, Nightfall, MIND, Prompt Security,
  Lasso). Respondents may not realize their incumbent suite already covers part of this.
- Overlap with [[ai-access-governance]] will confuse respondents — Cyberhaven and
  Lasso appear in both; consider asking "do you use a separate AI/prompt DLP control?"
  to disambiguate.
- M&A may date options: confirm Prompt Security (SentinelOne) status before fielding.

## Open taxonomy questions

- The DLP / [[ai-access-governance]] boundary is the fuzziest in the data layer —
  prompt-aware DLP and CASB-for-AI are converging. Candidate for an explicit "where
  does egress control end and shadow-AI governance begin" note.
- Should incumbent suite-DLP (Purview, Netskope, Forcepoint) be surveyed separately
  from AI-native DLP? They solve overlapping but differently-scoped problems.
- CSV merge vs doc split (shared with [[dspm]]) is resolved in favor of the doc spine.
