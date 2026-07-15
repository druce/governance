# Design: Citizen Development in a Hedge Fund — A Primer and Implementation Guide

**Date:** 2026-07-15
**Status:** Approved outline, pre-writing
**Audience for the finished document:** hedge-fund / asset-manager CTO and tech leadership designing and sanctioning a citizen-development program.
**Center of gravity:** full program playbook (case → governance → tooling → rollout → operations).
**Tool scope:** broad landscape, enterprise-grade only (see Ch 6 inclusion bar).

## Design decisions (settled during brainstorming)

1. **Organizing structure:** program-lifecycle narrative (why → risks → governance → tools → architecture → people → rollout → operations), not people/process/technology pillars and not a decision-framework-only doc.
2. **The concerns catalog (Ch 4) is the document's spine.** Gates (Ch 5) check it, tools (Ch 6) are scored against it, Appendix A crosswalks it to the 12-dimension maturity framework and the governance wiki's control categories.
3. **The builder spectrum × artifact spectrum (Ch 3) is reused as the risk-tiering axes (Ch 5)** — one consistent model throughout.
4. **EUC framing:** citizen-dev governance is presented as Excel-EUC governance 2.0, extending existing fund policy rather than inventing a parallel regime.
5. **Per-artifact concerns (§4.1–4.4) and program-level maturity dimensions (§4.5) are kept at separate altitudes** within Ch 4; Appendix A ties them formally.
6. **Trust zones and the lethal trifecta are bright-line architectural rules**, not judgment calls: every app severs one trifecta leg; green-zone apps get heightened review by construction.
7. **Enterprise bar for all tooling (§6.1):** SOC 2 Type II minimum (ISO 27001 / HIPAA-capable as maturity proxies), self-hosted / private-VPC / enterprise-cloud deployment, SSO+SCIM, RBAC, SIEM-exportable audit logs, zero-retention + no-training contractual terms. SMB SaaS-only tools explicitly excluded.
8. **Data-plane connectivity (§6.7) is the deciding tool-selection dimension** — on-prem, enterprise cloud warehouse, and SaaS (Salesforce, NetSuite) patterns each treated explicitly.

## Sources the document builds on

- **Maturity framework:** `druce.ai.dev/assets/2025/ai_maturity.html` (DIMENSIONS_DATA) — 12 dimensions × Crawl/Walk/Run/Fly: Leadership, Team, Data, Tech, Observability, Governance, Security, Training, Analytics/MLOps, Use-Cases, Partnerships, Process.
- **Blog post:** https://druce.ai/2026/04/ai-implementation — Crawl→Walk→Run→Fly arc, seven invariant constraints, "governance proportional to risk," "measure everything."
- **Governance wiki (this repo):** trust zones, risk-tiers, promotion-gates, hitl-approvals, acceptable-use-policies category pages; 42-category control taxonomy; M&A map for vendor viability checks.

## ⚠ Verification flag

Tool-specific claims in Ch 6 (certifications, self-host/deployment options, ownership/funding status, licensing) are **not to be trusted from priors** — research and cite current sources at writing time, per the repo's sourcing rules (cache to `raw/sources/`, date every claim).

---

# Full chapter outline

## Ch 1. Executive summary
- What this document is: a primer on AI-era citizen development and a playbook for standing up a governed program.
- The one-paragraph thesis: end users know the business; IT knows what makes software succeed; the program packages IT's knowledge as platform defaults and proportional gates so the disciplined path is the easy path.
- What the program delivers: throughput on the long tail of tooling needs central IT will never reach, with risk held inside explicit tiers and zones.
- The headline risks in two sentences, and the bright-line rules (trifecta severance, promotion gates, registry).
- How to read the document: Ch 2–4 primer; Ch 5–10 playbook; Ch 11–12 worked material and templates.

## Ch 2. Motivation: the fundamental tension
### 2.1 The knowledge asymmetry
- The end user is closest to the problem: knows the workflow, the data quirks, the real requirement; iterates at the speed of their own frustration.
- IT knows the invisible 80% of successful software: version control, testing, security, resilience, maintainability — everything that determines whether it still works in six months when the author is on vacation.
- Neither party can substitute for the other; the requirement round-trip through a spec document loses exactly the knowledge that matters.
### 2.2 The two historical failure modes
- **IT monopoly**: multi-year backlog; the business routes around it; the ungoverned Excel/Access/VBA estate every fund already owns. Shadow IT as a symptom of monopoly, not user misbehavior.
- **Free-for-all**: a portfolio of mission-critical houses of cards — untested, undocumented, unrecoverable, key-person-dependent, quietly holding API keys.
- The Excel-EUC precedent: funds have lived one full cycle of this already and most have an EUC policy to extend rather than invent.
### 2.3 Why now: AI broke the old equilibrium
- AI coding tools collapsed the cost of producing working-looking software; the free-for-all is happening whether sanctioned or not.
- The same tooling collapses the cost of discipline: Claude Code can make tests, git, and review the default path; low-code runtimes build in logging and credential handling.
- The window argument: firms that channel this now compound capability; firms that block it get shadow AI plus none of the upside.
### 2.4 The resolution
- Users supply problem knowledge; the firm supplies software knowledge as **platform defaults, shared primitives, and gates proportional to risk**.
- Success criterion for every mechanism in this document: does it make the safe path easier than the unsafe path?

## Ch 3. Citizen development in 2026
### 3.1 What changed in the definition
- From drag-and-drop form builders to conversational development of real software (vibe coding) alongside a matured low-code market.
- The line between "citizen" and "professional" developer is now a gradient of discipline, not a gradient of syntax knowledge.
### 3.2 The builder spectrum
- Excel power user → operations analyst who automates → technical analyst / quant-adjacent → embedded developer.
- Each rung: what they can build, what tooling fits them, what supervision they need.
### 3.3 The artifact spectrum
- Personal script → shared team tool → department workflow → business-critical application.
- Criticality is a property of *usage*, not intent — the experiment that becomes load-bearing; re-assessment triggers.
- These two spectrums become the axes of the risk-tiering model in Ch 5.
### 3.4 What citizen development is *not*
- Not a replacement for central dev on trading-adjacent, books-and-records, or client-facing systems.
- Not unsupervised agents in production; not personal AI accounts on firm data.

## Ch 4. The concerns catalog
*The backbone of the document. Each concern: what it is → why citizen developers characteristically miss it → what "good" looks like at each risk tier. Gates (Ch 5) check this catalog; tools (Ch 6) are scored against it; the crosswalk (Appendix A) traces it to the maturity framework and control categories.*

### 4.1 Engineering discipline
- **Version control & recoverability** — everything in git from the first prompt; a known-good tag to roll back to; the builder must never be stranded on a broken build they can't restore.
- **Real testing, not "looks right"** — edge cases, golden datasets, negative tests; the AI-specific failure mode: hallucination-induced bugs are *intermittent* — works 95% of the time, occasionally goes off the rails; evals for any stochastic component; "know it works" as the standard.
- **Sane implementation choices** — no web scraping when the warehouse or a REST API has the data; a published data-access map so the sane path is the discoverable path.
- **Acceptable performance** — response-time expectations by artifact type; not degrading shared resources (warehouse hammering, API quota exhaustion, rate-limit courtesy).
- **Common primitives over reinvented wheels** — curated libraries for auth, data access, logging, notification, scheduling; every reinvented wheel is a wheel nobody maintains.
- **Documentation** — README, runbook, data lineage, named owner; the test: could someone else operate this tomorrow?
- **Consistent dev environments** — devcontainers, lockfiles, project templates; artifacts must survive a second machine and a second person.
- **Tooling that automates good practice** — sanctioned environments (Claude Code with firm-managed settings/hooks, n8n, Retool) where discipline is built in rather than remembered.

### 4.2 Operational resilience
- **BC/DR** — backup, restore, failover proportional to criticality; the mission-critical house of cards as the named anti-goal; recovery *tested*, not assumed.
- **Key-person risk** — one-person tools capped at low tiers; shared ownership and a second operator as promotion criteria.
- **Lifecycle & orphaned apps** — maintenance expectations, upgrade cadence, deprecation, offboarding when the builder leaves.
- **Observability** — logging, monitoring, alerting wired to the firm's SIEM/dashboards; you learn it broke from an alert, not from the CFO.

### 4.3 Security
- **Secrets & least privilege** — no keys in code; vault-issued, scoped, rotated credentials; no over-permissioning; non-human identities for automations.
- **Data security / DLP / exfiltration** — sensitive data neither leaks into external AI tools nor out through the app itself; DLP coverage of citizen-built egress paths.
- **The lethal trifecta (bright-line rule)** — every app severs one leg: public data only (red zone), or internal data with no egress (yellow zone); an app needing both takes no untrusted input (green zone) and clears heightened security review. Architectural rule, not judgment call.
- **Supply chain** — hallucinated/typosquatted packages, unvetted MCP servers, low-code marketplace components; curated allow-lists and internal mirrors over per-app vetting.
- **Identity & access** — SSO on everything, RBAC, no shared logins; an app's entitlements never exceed its builder's; audit trail of who accessed what through the app.

### 4.4 Compliance & governance
- **PII & sensitive data handling** — Reg S-P, investor data, positions, MNPI; data classification determines permissible tools and zones.
- **Regulatory exposure** — recordkeeping, comms surveillance, marketing rule for anything client-facing; sensitive apps flagged at intake for heightened review, not discovered at audit.
- **Gating & promotion** — experiment → sanctioned project → production-ready; published criteria per gate, proportional to tier; the gate checklists *are* this catalog applied progressively.
- **Inventory & registry** — every artifact past personal-experiment stage registered: owner, tier, zone, data classification, dependencies.
- **Auditability** — logs, decision trails, accountability sufficient for SEC exams and allocator DDQs.

### 4.5 The maturity lens: all 12 dimensions applied to citizen development
*The concerns above are what can go wrong per artifact; the 12 dimensions are what the **program** must get right. Each dimension: how it applies, which concerns it owns, and the Crawl→Fly arc for citizen dev specifically.*

- **1. Leadership & Strategic Vision** — citizen dev needs an explicit mandate: named executive owner, stated risk appetite, funding for the platform team. Without leadership sanction, the program *is* shadow IT. Crawl: tolerated experiments → Fly: citizen dev in the firm's strategic plan with tracked ROI.
- **2. Teams, Talent & Org Design** — who plays which role: platform team, champion network, review pool, escalation path to professional dev. Owns key-person risk (a team-design failure, not an individual one). Federated model: central platform, distributed builders.
- **3. Data Engineering & Quality** — citizen apps industrialize whatever data quality exists; governed, entitlement-aware, documented data access is the precondition. Owns "sane implementation choices" and data foundations: no program on top of a data swamp.
- **4. Technology Platforms & Infrastructure** — the sanctioned toolchain, consistent environments, deployment paths, sandboxes. Owns environment consistency and tooling-automates-practice. The platform *is* this dimension applied to citizen dev.
- **5. Observability, Controls, Logging & Monitoring** — every citizen artifact emits logs to firm infrastructure; stochastic components carry evals with published metrics; usage telemetry feeds criticality re-assessment. Owns the observability concern and powers the registry.
- **6. Governance** — inventory, risk classification, promotion gates, policy documents, value tracking; the acceptable-use policy extended to *building*, not just using, AI. Owns the entire §4.4 family. Crawl: an AUP exists → Fly: gates enforced by technical controls, not memos.
- **7. Security & Threat Management** — trifecta severance, secrets, least privilege, supply chain, DLP integration; citizen-built apps join the firm's threat model and red-team scope. Owns the §4.3 family.
- **8. Training & Education** — certification before empowerment: builders trained on the firm's guardrails, AI failure modes (hallucination, prompt injection), and the gate process before receiving tools. Training tier unlocks tool tier.
- **9. Analytics, AI Development & MLOps** — the escalation path: when a citizen artifact contains a real model, eval loop, or production ML, it inherits MLOps discipline or transfers to the central team; the central AI/DS team as reviewer and adoptive parent of promoted apps.
- **10. Use Cases** — portfolio selection: low-risk/high-impact first; sequencing pilots to build the case; the anti-pattern of automating a broken process. Owns use-case selection and value tracking at the portfolio level.
- **11. External Partnerships & Vendors** — due diligence on the citizen-dev tools themselves: SOC 2/ISO evidence, contract terms (liability, audit rights, data ownership, zero-day retention, no training on firm data), vendor viability, exit strategy. Owns supply-chain risk at the vendor level.
- **12. Business Integration & Process** — apps embedded in real workflows with change management: process owners sign off, measurable before/after outcomes, adoption tracked; a tool nobody's workflow depends on is a hobby, a tool every workflow depends on is Tier 3.

## Ch 5. The governance framework
### 5.1 Risk tiers
- Tier axes from Ch 3: builder capability × artifact criticality × data sensitivity.
- Tier 0 personal experiment / Tier 1 shared tool / Tier 2 department workflow / Tier 3 business-critical — requirements escalate per the concerns catalog.
- Criticality re-assessment triggers: user count, dependency by another process, P&L or reporting linkage.
### 5.2 Trust zones (red / yellow / green)
- Zone definitions and the trifecta logic; zone assignment at intake based on data classification and egress needs.
- Zone as an *environment* property, enforced by infrastructure (Ch 7), not by promise.
### 5.3 Promotion gates
- Gate 1 (experiment → sanctioned project): registration, data classification, zone assignment, named owner.
- Gate 2 (sanctioned → production-ready): tests passing, docs, second operator, secrets vaulted, monitoring wired, BC/DR plan proportional to tier.
- Gate 3 (production → IT-adopted, when warranted): handover package, code review by professional dev, ongoing ownership decision.
- Published checklists per gate; review SLAs so gates aren't a new backlog.
### 5.4 Heightened-review triggers
- Green-zone apps (internal data + external access); anything touching MNPI, investor PII, or client-facing output; anything with write access to a system of record.
### 5.5 Policy integration
- Extending the existing EUC policy rather than writing a parallel one; relationship to model-risk policy, AUP, vendor-risk policy.
- Enforcement mechanics: what's technical control vs. attestation vs. periodic audit.

## Ch 6. The tooling landscape (enterprise-grade)
### 6.1 The enterprise bar (inclusion criteria for everything in this chapter)
- Certifications: SOC 2 Type II minimum; ISO 27001; HIPAA-capable where relevant as a proxy for control maturity.
- Deployment: self-hosted, private-VPC, or enterprise-cloud tenancy; data stays in the firm's boundary; explicitly **excluded**: SMB SaaS-only tools (consumer Zapier tiers, Airtable-class app builders, hosted-only vibe-coding platforms).
- Identity & control: SSO/SAML + SCIM, granular RBAC, environment separation (dev/test/prod), audit logs exportable to SIEM.
- AI/data terms: zero retention, no training on firm data, contractual audit rights.
- Vendor viability: funding/ownership status (cross-reference the wiki's M&A map), exit path, data export.
### 6.2 Agentic coding — Claude Code as the anchor
- Enterprise deployment paths: Bedrock/Vertex or enterprise API; managed settings, permission modes, hooks as policy enforcement points; CLAUDE.md as the carrier of firm standards; devcontainer templates.
- Why it fits the top of the builder spectrum; what it deliberately doesn't solve (hosting, entitlements) and must inherit from the platform.
- Adjacent: GitHub Copilot Enterprise, Cursor for business — where they overlap and differ on auditability and policy control.
### 6.3 Internal-tool builders
- Retool (self-hosted), Superblocks (on-prem agent architecture), Appsmith (self-hostable OSS) — UI + logic on top of existing databases and APIs.
- Evaluation against the catalog: what they automate (auth, RBAC, audit logs, connector credential handling) vs. leave open (testing, version-control depth, sprawl).
### 6.4 Enterprise low-code suites
- Microsoft Power Platform (Power Apps, Power Automate, Dataverse) — most funds already license it via M365; environments, DLP policies, managed environments, CoE toolkit as governance surface.
- The trade: deepest governance tooling vs. platform lock-in and sprawl-by-default; licensing traps.
### 6.5 Workflow automation & iPaaS
- n8n (self-hosted) as the governed automation anchor; Workato (enterprise iPaaS); Tines (security automation); Power Automate within the Microsoft estate.
- Where RPA (UiPath) still appears in funds and why it's a last resort vs. APIs.
### 6.6 Analytics & data-app self-service
- Streamlit — especially Streamlit in Snowflake: the run-the-app-next-to-the-data pattern that sidesteps egress entirely.
- Hex, Dataiku, KNIME, Posit/Shiny for the analyst tier; Python-in-Excel and Copilot as the on-ramp from the spreadsheet estate.
### 6.7 Data-plane connectivity (the deciding dimension)
- **On-prem data**: gateway/agent architectures (Retool self-host, Superblocks agent, Power Platform data gateway); read replicas and service accounts; never direct prod-DB credentials.
- **Enterprise cloud data** (Snowflake, Databricks, S3): native runtimes vs. external connection; entitlement inheritance; compute cost governance.
- **SaaS systems** (Salesforce, NetSuite, market-data APIs): governed OAuth connections, scoped service accounts, iPaaS-mediated vs. direct API; write-access as an automatic tier escalation.
- The connectivity rule: apps come to the data through governed connectors; credentials never live in the app.
### 6.8 Selection matrices
- Tool family × concerns catalog (which concerns each automates, mitigates, or ignores).
- Tool family × builder-spectrum rung; tool family × trust zone compatibility.
- A short opinionated shortlist per fund size, dated, with detail delegated to the wiki.

## Ch 7. Reference architecture & common primitives
### 7.1 The platform picture
- One diagram: identity spine → data access layer → sanctioned tool runtimes → deployment targets, with the AI gateway and SIEM wrapped around everything.
### 7.2 Identity spine
- SSO on every tool; RBAC groups mapped to desks/functions; non-human identities for schedulers and agents; entitlement inheritance principle.
### 7.3 Data access layer
- Entitlement-aware, read-only marts for citizen consumption; the published data-access map / API catalog; service-account issuance process.
### 7.4 Secrets management
- Vault integration in every sanctioned runtime; no secrets in code as an enforced (scanned) rule, not a request.
### 7.5 AI gateway & logging
- All model calls through the gateway: logging, DLP, model allow-lists, cost attribution; SIEM export from every runtime.
### 7.6 Environments & deployment paths
- Golden repo templates, devcontainers, CI defaults; the graduated path: laptop → zone-scoped sandbox → hosted internal app → (rarely) production.
- Ephemeral environments for red-zone experimentation.
### 7.7 The primitives library
- Firm-blessed building blocks: auth client, data connectors, logging/alerting, notification, scheduling, document generation; contribution process so the library grows from real use.
### 7.8 The registry (implementation)
- Minimum record: owner, tier, zone, data classification, dependencies, last review; automated discovery to catch the unregistered.

## Ch 8. People & enablement
### 8.1 Roles
- Platform team (builds Ch 7), champions per desk/function, reviewer pool, executive sponsor.
### 8.2 Training path
- Tiered curriculum: AI literacy & failure modes → sanctioned-tool training → guardrails & gate process → certification that unlocks tooling.
### 8.3 Support model
- Office hours, internal guild/channel, paired builds with IT for first Tier-2 projects.
### 8.4 IT's role shift
- From builder of everything to platform operator, reviewer, and adoptive parent of promoted apps; what this means for IT hiring and incentives.

## Ch 9. Rollout plan
### 9.1 Mapped to Crawl → Walk → Run → Fly
- Crawl: policy written, tools sanctioned, registry stood up, pilot cohort picked.
- Walk: pilot builds in yellow/red zones, gates exercised for real, primitives library seeded.
- Run: broad enablement, champions active, first promotions through Gate 3, agentic patterns under HITL.
- Fly: gates enforced by technical controls, portfolio-level value tracking, graduation paths for autonomous agents.
### 9.2 The pilot
- Selection: low-risk / high-visibility / data-available; 5–10 builders across functions; explicit success and kill criteria.
### 9.3 Metrics
- Delivery: tools built, hours saved, spreadsheets retired, backlog items self-served.
- Risk: incidents, gate-failure reasons, unregistered-app discoveries, secrets-scan hits.
- 30/60/90 skeleton with owner per item.

## Ch 10. Operating the program
### 10.1 The review cadence
- Quarterly registry review: criticality re-assessment, orphan detection, stale-app deprecation.
### 10.2 Incident response
- Citizen-built apps in the IR plan; kill-switch authority and process; blameless postmortems feeding gate-checklist updates.
### 10.3 Offboarding & ownership transfer
- Builder departure playbook; succession as a standing gate criterion, not an afterthought.
### 10.4 Program evolution
- Feeding lessons into the maturity assessment; annual re-score against the 12 dimensions; policy version control.

## Ch 11. Worked examples & anti-patterns
### 11.1 Worked examples (each annotated: tier, zone, tools, which concerns bit and how the gates caught them)
- Ops reconciliation automation (yellow zone, n8n + warehouse).
- Research data-wrangling app (yellow zone, Claude Code + Streamlit-in-Snowflake).
- Investor-reporting draft automation (green zone — heightened review walkthrough).
- Compliance surveillance helper (yellow zone, heightened review for data sensitivity).
- Market-data monitor (red zone, public data only).
### 11.2 Anti-patterns (the red lines, with reasoning)
- Anything in the order/execution path; official NAV or books-and-records without IT adoption; client-facing output without compliance review; personal AI accounts on firm data; the scraper that had a SQL alternative; the un-gated agent with warehouse credentials and internet access.

## Ch 12. Appendices
- **A. The crosswalk table** — every concern → maturity dimension → wiki control category → gate where checked. The traceability spine in one table.
- **B. Gate checklists** — printable, per tier.
- **C. Policy templates** — sanctioned-tool list, tiering rubric, intake form, heightened-review form.
- **D. Tool shortlist** — dated, with certifications/deployment-mode table, linking to wiki vendor pages.
- **E. Glossary & FAQ** — including "why can't I just use my personal ChatGPT," "why does my app need tests if it works."
