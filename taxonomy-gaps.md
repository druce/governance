---
title: "Taxonomy gaps & decisions"
---

# Taxonomy gaps, decisions & open questions

Mismatches between the two seeds, the decisions taken to reconcile them, and questions
flagged for the human. Every decision here is also logged in `log.md` as a `taxonomy` or
`decision` entry. Status: **D** = decided (recorded) · **Q** = open question for the human.

---

## Decisions taken (D)

**D1 — Layer-cake doc is the spine; CSV maps into it.** The 7 doc layers define the
structure; the 23 CSV survey questions are mapped onto doc rows. Result: 42 canonical
categories (the union, deduped), not 23 and not 40.

**D2 — Keep DSPM and DLP split (against the CSV merge).** The CSV lumps everything into
one `DSPM / Data Governance / DLP` question; the doc treats **Data Classification & DSPM**
(data-at-rest posture) and **Data Loss Prevention** (egress-time controls) as two Day-1
rows with largely different vendors. We keep them split per the spine. *Survey implication:*
the CSV's single question should become two; many vendors (Cyera, Sentra, Concentric,
Purview, Netskope) legitimately answer both — note overlap on both pages.

**D3 — Merge "AI Access Governance (CASB for AI)" and "Shadow-AI / Insider risk."** Same
job (discover shadow AI, enforce inline policy on prompts), two names. Canonical slug
`ai-access-governance`; "Shadow-AI / Insider risk" kept as an alias and as the survey
question label candidate.

**D4 — Merge doc "AI SecOps / Security Automation" into `ai-soc-analysts`.** The doc's AI
SecOps row lists the same vendors as the CSV "AI SOC analysts" question (Prophet, Dropzone,
Radiant, Simbian, Charlotte, Cortex AgentiX). SOAR-flavored automation vendors (Jazz, Torq)
are tagged here with `siem-soc` secondary.

**D5 — Split the CSV "MCP / Agent Gateway & Tool Access" mega-question into three doc rows.**
That one CSV question conflates: (a) **authorization engines** (Cerbos, OPA, Styra,
Permit.io, Oso) → `authorization-engine`; (b) **MCP gateways / tool ACLs** (Kong,
agentgateway, TrueFoundry MCP, Obot, MintMCP, Pomerium) → `mcp-gateway`; (c) **tool identity
& integration / agent auth** (Composio, Arcade, StackOne, Descope, Stytch, WorkOS) →
`tool-identity-integration`. These are three different buying motions. *Survey implication:*
ask three questions, not one.

**D6 — Promote three CSV-only categories to canonical** even though the doc folds them in:
`ai-red-teaming` (doc folds into LLM Observability), `identity-governance` (IGA/ISPM; doc
folds into Identity & Access + Data Access Gov), `non-human-identity` (doc folds into
Identity & Access + Tool Identity). Each has a distinct vendor set and buying motion.

**D7 — Keep `comms-surveillance` separate from `ai-governance-platform`.** The CSV files
Behavox / Theta Lake under "AI Governance, Model Risk & Compliance"; the doc gives Comms
Surveillance its own row. For a hedge fund this is a distinct, high-priority function
(MAR/MNPI, e-comms capture) — keep it standalone.

**D8 — Split bundled CSV vendor cells** into separate vendor pages (see taxonomy.md):
1Password/Doppler/Infisical, OPA/Styra, Immuta/Collibra, Obot/MintMCP. `Promptfoo` gets its
own page. `Other (Please Specify)` rows are survey UI — no vendor pages, but preserved in
each category's survey scaffolding.

**D9 — Retrieval-infra and process categories kept but kept thin.** `content-sources`,
`vector-retrieval`, and the five `policy/process` rows (trust zones, risk tiers, promotion
gates, HITL, AUP) are categories for completeness but are infrastructure/practice, not
vendor shortlists. Pure-process pages carry **no `## Survey` scaffolding**.

---

## Soft mismatches noted (non-blocking)

- **Veza, Cyera, Sentra, Concentric, ConductorOne** straddle `identity-governance`,
  `data-access-governance`, and `dspm`. Primary category assigned per vendor in Phase 2;
  cross-tagged. The IGA-vs-DAG line is genuinely fuzzy (identity-centric vs data-centric
  view of the same "who can see what" problem).
- **Zenity, Lasso, Reco, Nudge, Noma** straddle `ai-spm` and `agent-runtime-security` (and
  Lasso also `ai-runtime-security` / `dlp`). The CSV itself flags "overlap with governance?"
  on Quilr. The AI-SPM vs Agent-Security line is the messiest in the taxonomy — see Q1.
- **CalypsoAI** appears in the doc under both AI Runtime Security and AI Governance; CSV
  flags `acq. by F5`. Cross-tag runtime (primary) + governance.
- **HiddenLayer, SplxAI, Lakera, Prompt Security** appear in both `ai-runtime-security` and
  `ai-red-teaming`. Runtime = inline protection; red-teaming = offline attack/eval. Cross-tag.
- **OneTrust** spans `enterprise-grc`, `ai-governance-platform`, and `dspm`. Primary = GRC.
- **Cloudflare, Kong, F5, TrueFoundry** span `ai-gateway` and `mcp-gateway`. Palo Alto spans
  ~6 categories. Cross-tag; pick primary per vendor.

---

## Open questions for the human (Q)

**Q1 — How finely should the agent-security cluster be cut?** I currently keep FIVE adjacent
categories: `ai-spm`, `agent-runtime-security`, `authorization-engine`, `mcp-gateway`,
`tool-identity-integration` (plus `non-human-identity` in Foundation). This faithfully
mirrors the two seeds but risks confusing survey respondents (vendors blur across them).
Options: (a) keep all five (max fidelity, current choice); (b) merge `ai-spm` +
`agent-runtime-security` into one "AI/Agent Security Posture & Runtime"; (c) merge the three
tool/authz rows into one "Agent Authorization & Tool Access." I lean (a) for the wiki +
(b/c) collapses noted as survey guidance. **Want your call before Phase 1.**

**Q2 — Do the pure-process categories (trust zones, risk tiers, promotion gates, HITL, AUP)
deserve full category pages, or one combined "AI Governance Process" page?** They have no
vendors. I currently plan five thin pages (faithful to the doc) but could fold them into one
`governance-process` page + keep `trust-zone-segmentation` standalone (it's the spine's
organizing idea). **Low stakes — will default to five thin pages unless you object.**

**Q3 — Retrieval infra depth.** `content-sources` and `vector-retrieval` are listed in the
doc but are plumbing a hedge-fund CTO mostly inherits. Build full pages, or one-line stubs
pointing at `entitlement-aware-rag` (the part that actually matters for governance)? I lean
stubs. **Default: stubs unless you want full pages.**

**Q4 — Survey-question granularity vs wiki-category granularity.** The wiki has 42 categories;
a survey can't ask 42 questions. Should I produce a separate `comparisons/survey-blueprint.md`
that collapses the 42 into a ~15-question survey (the real instrument), keeping the wiki
fine-grained? I think yes and will build it in Phase 4 unless told otherwise.

---

## Phase 5 — final taxonomy pass (2026-06-28, post-research)

**Outcome: the 42-category spine held.** Research did not argue for renames/merges/splits of
categories; the changes were **vendor moves** and ownership corrections. Decisions:

- **R1 — jazz-security moved `ai-soc-analysts` → `dlp`.** Research showed Jazz is AI-native DLP, not
  a SOC analyst/SOAR tool. Removed from ai-soc-analysts + siem-soc pages; added to dlp.
- **R2 — immuta primary → `data-access-governance`** (was dspm): it's access-enforcement, not posture.
- **R3 — collibra primary → `ai-governance-platform`** (was dspm): catalog/governance, not security DSPM.
  (Layer field left as data on the page — minor cosmetic residual.)
- **R4 — aurascape +`ai-runtime-security`** (hybrid inline+endpoint, not pure access-governance).
- **R5 — silverfort** noted: real center of gravity is ITDR/NHI runtime protection, not classic IGA
  (kept identity-governance primary; flagged on page).
- **R6 — material-security**: flagged as a likely mis-fit in `browser-security-extension` (it's
  email/workspace security; true peers Abnormal/Proofpoint). **Kept** there — the taxonomy has no
  email-security category and it does some workspace DLP. Open question if the taxonomy should add one.
- **R7 — governgpt**: it's a DDQ/RFP-response automation tool for IR/fundraising, **not** an SR 11-7
  model-risk platform. Left tagged `ai-governance-platform` with an inline caveat; candidate to drop
  from the survey shortlist. Open question.
- **R8 — fairly-ai** rebranded to **Asenion** (acquired anch.AI 2025-06). Alias noted on page; slug
  kept as `fairly-ai`.
- **R9 — symmetry-systems ownership corrected** independent → acquired (Zscaler, 2026-05-21) after a
  lint cross-check caught a research miss. Verified against Zscaler/Symmetry primary announcements.
- **robust-intelligence** kept as a thin alias of `cisco-ai-defense` (dedupe; both = same asset).

**Residual (documented, low-impact):** a few category-page *prose* vendor lists may still list a
vendor under a category it was re-tagged out of during research (frontmatter + `index.md` are
authoritative and correct). The 6 zero-vendor categories (5 process pages + `third-party-ai-apps`)
are intentionally vendorless.
