---
type: category
name: SaaS Security Posture Management
slug: sspm
layer: foundation
priority: day-2
trifecta_role: none-detection
maps_to_seed_doc: SaaS Security Posture (SSPM)
maps_to_seed_csv: —
vendor_count: 7
status: drafted
last_updated: 2026-06-28
---

# SaaS Security Posture Management (SSPM)

## Business objective

Continuously assess and harden the configuration of your SaaS estate. The seed doc
calls it **the posture checker for your SaaS estate** — it catches the risky
setting and, critically for an AI program, **the AI feature someone quietly
switched on inside Salesforce** (or M365, Workday, ServiceNow, etc.). SSPM
inventories your SaaS apps, flags misconfigurations and over-broad permissions,
maps third-party OAuth grants and integrations, and tracks the new AI copilots and
agents that SaaS vendors are turning on by default.

## When you need it

**Day 2.** Not required to go live, but it becomes important as soon as your
SaaS vendors start shipping embedded AI (Copilot in M365, Einstein in Salesforce,
AI in Slack/Zoom) — because those features can expose data through permissions you
never audited, and they appear without a procurement event. For a hedge-fund CTO,
SSPM is the control that answers "what AI did our SaaS vendors quietly enable, and
who can it see?" The need scales with the size and sprawl of the SaaS estate; a
small shop on a handful of apps may defer it.

## Lethal-trifecta role

Not a direct trifecta control — it's **posture and detection**, not an inline
gate. Its trifecta relevance is indirect but real: misconfigured SaaS sharing and
default-on AI features are a common way **sensitive data** becomes reachable by an
AI feature or an over-permissioned integration. SSPM reduces that exposure surface
before it can be chained into an exfiltration path. Relevant wherever SaaS holds
sensitive data — effectively the **yellow/green** boundary inside SaaS apps.

## Vendors

- [[appomni]] — SSPM pioneer; broad app coverage and deep posture/data-exposure analysis.
- [[obsidian-security]] — SSPM with strong threat-detection/ITDR emphasis across SaaS.
- [[adaptive-shield]] — SSPM with SaaS misconfiguration and identity-posture focus.
- [[grip-security]] — SaaS/identity discovery and shadow-SaaS (and shadow-AI) governance.
- [[valence-security]] — SSPM emphasizing SaaS-to-SaaS integration and supply-chain risk.
- [[wing-security]] — SSPM with automated remediation and SaaS-app discovery.
- [[docontrol]] — SaaS data-access security and DLP-style controls for SaaS.

## Consolidation / M&A dynamics

SSPM is consolidating into larger security platforms. [[adaptive-shield]] is
reported to have been acquired by CrowdStrike (per seed; unverified — to confirm in
research), part of a pattern of endpoint/SOC platforms absorbing SaaS posture.
Several SSPM vendors are also stretching toward shadow-AI and SaaS-AI governance,
blurring the line with [[ai-access-governance]] and [[ai-spm]]. Expect further
roll-up as posture management converges with broader CNAPP/identity platforms.

## Adjacent categories

- [[ai-access-governance]] — shadow-AI discovery overlaps with SSPM's shadow-SaaS discovery; some vendors ([[grip-security]], [[reco]], [[nudge-security]]) span both.
- [[ai-spm]] — AI-asset/agent posture; conceptually SSPM's AI-native sibling.
- [[data-access-governance]] — who-can-see-what inside the data; SSPM looks at the SaaS-config layer above it.
- [[identity-governance]] — over-broad SaaS permissions are the joint concern.

## Survey

**Question:** Which SaaS Security Posture Management (SSPM) tool does your firm use
or evaluate to harden SaaS configurations and catch default-on AI features?

**Answer options (multi-select):**
- AppOmni
- Obsidian Security
- Adaptive Shield
- Grip Security
- Valence Security
- Wing Security
- DoControl
- Other (Please Specify)

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:** This category was doc-only (not in the seed survey
CSV), so it's a candidate addition — expect lower familiarity and more "Interested"
than "In production" responses than for table-stakes categories. Overlap with
shadow-AI tools ([[grip-security]], [[reco]], [[nudge-security]]) will confuse some
respondents; consider a clarifying prompt that SSPM = SaaS *configuration* posture,
not AI-prompt control. Adaptive Shield may need an "(acq. by CrowdStrike?)" note if
that M&A is confirmed.

## Open taxonomy questions

- Boundary with [[ai-access-governance]] and [[ai-spm]] is fuzzy — shadow-SaaS vs
  shadow-AI discovery overlap; some vendors are deliberately positioning across both.
- Doc-only category with no seed-CSV question; confirm it earns a standalone survey
  slot vs being folded into a SaaS/identity-posture question.
