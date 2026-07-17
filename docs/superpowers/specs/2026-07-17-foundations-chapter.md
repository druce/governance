# Foundations chapter (proposed Ch 3) — brainstorm output

Drafted 2026-07-17. Companion to `2026-07-15-citizen-dev-primer-design.md`.
Slots between current Ch 2 (Motivation) and Ch 3 (Citizen development in 2026);
current Ch 3–12 renumber to 4–13.

## Design decisions

1. **Framing: prerequisites checklist, not tutorial.** "What must be true before
   the program starts" — Day-0 readiness with a self-assessment against the
   12-dimension maturity framework. A full data-governance treatment is its own
   document; the maturity-lens section (§4.5) alone would bury the message.
2. **Foundations are graduated by trust zone, not absolute.** The paralysis
   failure mode is "no citizen dev until the data estate is perfect" — meaning
   never. Red-zone work needs almost nothing; the data bar bites at yellow zone;
   green zone needs everything. The program starts immediately while foundations
   mature in parallel — and the program *motivates* foundations work rather than
   waiting on it.
3. **Boundary with other chapters:** this chapter = what must exist *before and
   independent of* the program (most of it the firm needs for AI generally).
   Ch 7 (reference architecture) = what the platform team *builds for* the
   program on top. §4.5's Data dimension slims to a cross-reference.
4. **"Labeling" here means sensitivity classification** (public / internal /
   confidential / MNPI / PII), not ML training-data labeling. Eval/ground-truth
   readiness (golden datasets for testing AI components) is a bullet under data
   quality if wanted, not a section.

---

## Ch 3. Foundations: what must be true before citizen development can succeed

*Framing: citizen development is a force multiplier on whatever foundations
exist. Governed data and clean identity get multiplied; chaos gets multiplied
just as efficiently. This chapter is the Day-0 checklist — and the
zone-graduated minimums that let you start before everything is fixed.*

### 3.1 Data foundations (the heart of the chapter)
- **Golden sources** — one documented source of truth per domain (positions,
  prices, trades, investor records, reference data); citizen apps built on "the
  copy Bob keeps" industrialize the copy Bob keeps.
- **Data quality** — accuracy, completeness, timeliness; named data
  owners/stewards per domain; quality monitored, not assumed. The GIGO argument
  in fund terms: an AI reconciliation tool on top of unreconciled data automates
  the production of confident errors.
- **Catalog & discoverability** — documented schemas, lineage, and the published
  data-access map; this is what makes "use the SQL mart, not a scraper" (the
  sane-implementation-choices concern) *possible* rather than aspirational.
- **Classification & labeling** — sensitivity labels (public / internal /
  confidential / MNPI / PII) applied and *machine-readable* (e.g., Purview
  labels). The load-bearing item: trust-zone assignment, DLP enforcement, and
  tool eligibility all key off labels. Unlabeled data is unusable data for
  citizen dev — there's no way to decide which zone an app belongs in.
- **Entitlements encoded, not tribal** — who may see what lives in systems
  (RBAC, row/column security), because citizen apps inherit entitlements from
  infrastructure, and infrastructure can't inherit tribal knowledge.

### 3.2 Knowledge & document foundations
- **Permissions hygiene in the document estate** — SharePoint/Drive oversharing
  fixed *before* any retrieval touches it; RAG amplifies every over-broad ACL
  into an incident (the wiki's entitlement-aware-RAG precondition).
- **Written-down processes** — AI can only automate what's articulated;
  undocumented workflows are automatable only by the one person who knows them,
  which recreates key-person risk in software form.

### 3.3 Identity & access foundations
- SSO + MFA on everything a citizen app might touch; no local logins, no shared
  accounts.
- RBAC groups that mirror the actual org; joiner/mover/leaver hygiene (stale
  entitlements become stale *app* entitlements).
- Service-account and secrets infrastructure existing (the vault the program
  will mandate must already exist).

### 3.4 Platform & tooling baseline
- Somewhere governed for data to live and compute to run: warehouse/lakehouse or
  at least read replicas of core systems; APIs (or replicas) for OMS,
  accounting, CRM — the systems citizen apps will want.
- Git hosting with SSO, available to every would-be builder — version control
  can't be a gate criterion if getting a repo requires a ticket.
- The governed AI access layer from the wiki's Day-1 list: enterprise assistant,
  AI gateway, prompt-DLP — citizen dev rides on these, it doesn't create them.

### 3.5 Security & compliance baseline
- The wiki's Tier-0/Tier-1 Day-1 stack confirmed: SASE AI-traffic controls on,
  SIEM ingesting, AUP written and signed.
- An EUC policy on the books (Ch 2's inheritance argument requires something to
  inherit).

### 3.6 People baseline
- Executive sponsor named; data owners identified; baseline AI-literacy training
  delivered (the Training dimension's Crawl level).

### 3.7 The readiness assessment & zone-graduated minimums
- Self-score against the 12-dimension maturity framework; the entry bar is
  roughly **Walk** in Data, Tech, Security, and Governance — not Fly in
  anything.
- The minimums table (the chapter's payoff):
  - **Red zone** (public data only): identity + AUP + sanctioned tools. Start
    this week.
  - **Yellow zone** (internal data, no egress): + labels on the data domains in
    scope, golden sources for those domains, entitlement-encoded access, secrets
    vault.
  - **Green zone** (production/write access): + everything, plus the
    heightened-review machinery of the governance chapter.
- Sequencing advice: let the pilot's data needs *drive* which domains get
  labeled and cataloged first — foundations work motivated by a concrete app
  beats a boil-the-ocean data program.

---

## Cross-reference adjustments when splicing into the spec

- Renumber current Ch 3–12 → 4–13; update internal references (tier axes "from
  Ch 3" → Ch 4; gates "Ch 5" → Ch 6; etc.).
- §4.5 (maturity lens) Data dimension: slim to a pointer at this chapter.
- Ch 7 (reference architecture): add boundary note — foundations pre-exist the
  program; the platform builds on them.
- Ch 9 (rollout) Crawl stage: reference the §3.7 readiness assessment.
- Appendix A crosswalk: add a foundations column or rows keyed to §3.x.
