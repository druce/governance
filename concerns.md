# Ch 3. Concerns — reorganized by the 12 program dimensions

**Status:** Proposed rewrite of the Ch 3 concerns outline (source: `governance_notes_draft.md`, 2026-07-24). Every concern from §3.1–3.3, the Ch-3 intro list, the advanced-threats table (C1–C15), and the gap tables (F1–F11, T1–T8, G1–G10, O1–O9) is bucketed below. **Core** = Day-1/Day-2 concerns every program must address; **Advanced / Day 3** = concerns that become live as agents gain autonomy, memory, and inter-agent connectivity. Buckets with no Day-3 items omit that subsection.

At 30,000 foot level, 3 types of concerns:

1) **Agents as insider threats**, taking costly or dangerous actions, exfiltrating, deleting, other security and compliance violations, 
   1) **Why?**
      1) Prompt injection.
      2) Hallucinations, reward hacking, running off the rails and going feral
      3) User error
      4) Fraud
      5) Security compromise 
   2) Agents are like users, they cannot be fully controlled by policy guardrails, they are subject to social engineering.  Risks of deviating from expected behavior cannot be eliminated, only bounded by what the agent can do. Attacks and problems can occur at multiple layers, llms, agents, governance, composition of multiple components and layers. Architectural controls, permissions, trust zones dominate runtime checks on inputs and outputs and behavior. 
2) **Efficiency or cost-benefit/ROI concerns**: Agents not fit for task or performing to expectations: stochasticity not accounted for, model drift, big differences between dev, test and prod, high cost of tokens or human babysitting
3) **Meta concerns**:  governance issues, tech debt spiral, operational issues, outcomes not well measured so you don't even know if it's failing, accountability, vendor risk, key person risk, fragility, loss of oversight, skill and talent pipeline atrophy

---

## 1. Leadership 

- **Executive mandate** — The program has a named executive owner, stated objectives, constraints, principles for resolving conflicts, risk appetite, and resources for the platform team. Without leadership sanction and governance, citizen development *is* shadow IT. **Leadership approves** the major components, citizen-dev user contract, acceptable use policy, plans, budgets, timelines.
- **Program management, monitoring, and ROI measurement** — citizen development is in the firm's strategic plan with tracked objectives and metrics.
- **Leadership promotes** citizen dev, attends kickoffs/hackathons, celebrates wins by the org. 

## 2. Team 

- **Defined program roles** — platform team, champions per desk/function, reviewer pool, executive sponsor, and an escalation path to IT development must all be clearly specified, not implied.
- **Explicit contract** between citizen devs and IT with a **Federated operating model** — a central platform with distributed builders, so IT packages its knowledge as defaults and services rather than acting as a gatekeeper or bottleneck.
- **Key-person risk** — one-person tools are capped at low tiers, with shared ownership and a named backup operator required for promotion.
- **Governance capacity** — gates and human-in-the-loop approvals have trained reviewers and regular cadence, or governance becomes a new backlog people route around.

## 3. Data 

- **Data foundations as precondition** — citizen apps industrialize whatever data quality exists, so golden sources, named owners, and monitored quality must precede the program, not build a tower on a weak foundation like a data swamp.
- **Data well-documented** — a proper data dictionary / API catalog makes "use SQL, not a scraper" the easy happy path documented in the user contract.
- **Classification & labeling** — machine-readable sensitivity labels (public / internal / confidential / PII / MNPI / other data) determine zone assignment, DLP, tool eligibility.
- **Entitlements** — who-may-see-what is clean, documented, audited, lives in systems (RBAC, row/column security), so citizen apps inherit entitlements from infrastructure.

### Advanced / Day 3

- **Cryptologically secure data pipeline integrity** — data has signed ingestion pipelines, versioning and lineage.

## 4. Tech platform 

- **Version control & recoverability** — all citizen dev in git from day one, with a known-good version to roll back to, so a builder is never stranded on a broken build.

- **Consistent, repeatable, isolated environments** — dev containers, lockfiles, and project templates so every artifact survives a second machine and a second person, with dev and prod properly separated and permissioned. Zones and containers constrain the blast radius where the code runs. Sanctioned environments (Claude Code with managed settings and hooks, n8n) where discipline is built in. Behind network egress proxies, e.g. Zscaler, LiteLLM, MCP/tool gateway.

  Limit blast radius with **execution zones**, so agents and sub-agents can spin up with appropriate scope. Contain, don't explain:

  - **Green zone:** full internet and LLM access, no access to internal data. Users can run research on publicly available data. Github Codespaces, Cloudflare workers etc. Moving internal data into Red zone must be prevented or restricted/monitored, since a prompt will leak it.
  - **Yellow zone**: no internet access, full access to internal data and vetted enterprise LLMs. Users can run AI on internal data with no risk of exfiltration. Databricks, Snowflake, Sagemaker notebooks walled off from public internet, accessing vetted package registries. 
  - **Red Zone**: no unvetted prompts, access to internal and external data. Only highly vetted workflows with no risk of prompt injection. 

- **Realistic tests, not vibes** — edge cases, golden datasets, and negative tests, with special attention to AI stochasticity and hallucination-induced bugs.

- **Common primitives, not reinvented wheels** — curated firm libraries for auth, data access, logging, notification, and scheduling, because every reinvented wheel is a wheel nobody maintains. Documentation of which tool fits which job, with each tool properly restricted to appropriate access. The proxy layer / package registry users can pull from constrains supply chain attacks: Cloudmith, JFrog Artifactory + Curation, or Sonatype Nexus + Firewall .

- **Acceptable performance & resource utilization** — Well-behaved consumption of shared resources with SLAs: exponential backoff with jitter, and no retry-storm / thundering-herd rushes when a resource comes back online.

- **Software-supply-chain hygiene**: Scanners are the last line of defense for protection. First line of defense is the paved road they start from, the package proxy they're allowed to pull from, and the blast radius of where their code runs. Use AI PR code reviews, ideally different model from the one that built the code, and feed back to AI to fix and escalate to IT when necessary. Critical checks: Secrets in code, prompt injection, SQL injection, lethal trifecta issues like cross-tool bridges, malicious / hallucinated packages (must use safe package proxy and minimum-age flags), license/IP issues, user contract red lines, repeatable evals when LLMs update, up-to-date documentation, missing tests/edge cases, general code smells. Consider tools like Socket, Semgrep, GitHub Actions and GitHub Advanced Security, Code Security, Secret Protection, CodeQL. 

### Advanced / Day 3

- **Design-pattern catalog mapped to use cases** — approved architectures (plan-then-execute, critic-optimizer with LLM as judge, quarantined/dual LLM, code-then-execute, context minimization) so citizen devs get blueprints, not just guidelines.
- **Tool design rules** — ban generic-capability tools (raw shell, `execute_sql`) in favor of parameterized least-privilege tools, with strict structured output on anything crossing a trust boundary.
- **Sandboxing baseline** — separate filesystem for agents, production reachable only through dedicated tools, and long-lived credentials never stored on the agent runtime (secrets manager with access permissioned per approved action).
- **Platform compliance traps** — codify each platform's dangerous defaults (e.g., Copilot Studio's 30-day transcript retention vs. books-and-records, cross-geography data movement, sharing rules, licensing conventions).
- **More advanced software supply chain tools** like Snyk, Endor, Apiiro, Legit.

## 5. Observability, Controls, Logging, Monitoring

- **Append-only immutable logging** — every agent emits logs at an appropriate level of detail to SIEM. 
- **All agents wired to dashboards for health and evals.** — Users and IT should learn it broke, because an API went down or a silent LLM update introduced hallucinations, from an alert, not from traders cursing or the CFO.
- **Auditability** — logs, decision trails, and accountability sufficient to survive SEC exams and allocator DDQs.
- **Attribution & explainability** — outputs show data provenance, link back to sources, and are demonstrably repeatable and robust to minor input changes.
- **Session & delegation traceability** — agent session IDs on all logs, with sub-agent spawns mapped back to the originating agent and owner.
- **Kill switch** — a tested mechanism, clear authority, and a backup plan, to pull any agent offline when it deviates from reuired performance or intended goals.
- **Data-driven criticality reassessment** — usage data feeds re-tiering, so a personal script that became load-bearing gets noticed before it fails.
- **Trace mining & near-miss learning** — use AI to review traces for privilege escalation and dangerous combinations before they bite, feeding a near-miss learning loop.

### Advanced / Day 3

- **Kill switch ≠ revocation** — terminating a process leaves cached tokens and live sessions valid, so shutdown needs cross-system revocation propagation and recursive termination of spawned sub-agents.
- **Rollback, undo & reversibility classification** — classify each agent action reversible vs. irreversible, gate pre-approval on the irreversible ones, and build undo paths for the rest.
- **Tamper-evident logs & decision-chain audit trails** — hash-chained or signed logs a compromised agent can't erase, a never-log list for secrets/PII, and recorded rationale for each action ("the AI did it" fails a regulator); don't audit on chain-of-thought alone, since stated reasoning can be unfaithful.
- **Path-level policy enforcement** — evaluate policies over an agent's action *history* (read-MNPI then send-external-email may be individually benign), with shared cross-agent governance state.
- **AI-based oversight (agents watching agents)** — a trusted monitor reviews actions at machine speed, pauses flagged ones, and escalates only exceptions to the named owner — noting the monitor itself is injectable.
- **Behavioral anomaly detection tuned to agents** — per-agent baselines of tool-call patterns against declared scope, with semantics-aware rules and per-agent trust metrics, because SIEM content assumes deterministic services.

## 6. Governance

- **The user contract / citizen-dev policy** — a single signed document covering what the firm provides, what the builder must do, red/yellow/green action rules, and the principal-agent principle: the human owner is accountable for everything their agent does. Users have tools to self-assess against the contract and firm policies. **Extend existing policy, don't fork** — build on the firm's acceptable-use policy, end-user-computing policy, and model-risk framework rather than writing a parallel regime.
- **Framework alignment** — anchor the program to recognized frameworks: ISO/IEC 42001, 23894, 38507, 42005, 5338, 27001; NIST AI RMF; MITRE ATLAS; OWASP LLM/Agentic Top 10; Google SAIF; CSA AI Controls Matrix). Some aspects may be applicable to all levels, others may be mostly applicable to most load-bearing projects and IT-provided tools.
- **Active oversight duty** — deploying an agent is not the end of the job; the owner must maintain it as infrastructure and LLMs and business evolves, monitor it for performance and fitness for purpose, review flagged anomalies, and retain kill-switch authority.
- **Inventory & registry** — every artifact past personal-experiment stage is registered with owner, tier, zone, data classification, and dependencies.
- **Risk-proportional gating & promotion** — documented criteria per gate (experiment → sanctioned citizen dev → production), proportional to risk tier, with each gate asking what the worst-case scenario is under bad data, bad prompts, or runtime failure. Large changes outside assumptions use in gating must trigger review; higher tier agents should be re-reviewed on an annual cadence.
- **Risk-proportional human-in-the-loop** — the level of human review is set in contract and at gate review, per tier and action class.
- **Progressive earned autonomy** — agents start supervised and earn wider freedom only against a documented track record.
- **Regulatory exposure** — recordkeeping, comms surveillance, and the marketing rules are flagged for anything client-facing, not discovered at audit.
- **Accountability & delegation** — every agent has one responsible owner; unmonitored delegation and diffuse accountability are named failure modes.
- **AI sprawl** — uncontrolled proliferation of duplicative, orphaned, or shadow artifacts is managed as a standing program risk.
- **Cost management & billback** — Inference spend is metered, attributed, and charged back so costs stay visible and owned.
- **Lifecycle & orphaned apps** — maintenance expectations, upgrade cadence, deprecation, and controlled offboarding when the builder leaves.

### Advanced / Day 3

- **Autonomy as an explicit tier axis** — tier by autonomy and authority as well as builder × criticality × sensitivity, with written expansion criteria, scope-escalation triggers forcing re-review on "autonomy drift," and adaptive downgrade on anomaly.
- **Action-tier classification & plan-level approval** — green/yellow/red *action* classes enforced outside the agent's own judgment, with plan-mode approval up front instead of per-action clicks.
- **Approval fatigue / HITL overwhelm** — rubber-stamping is a measured failure mode: cap flag rates, present meaningful diffs, enforce minimum review times, and prefer policy-engine decisions where possible.
- **Trace-learned behavioral allowlists** — compile staging-phase traces into an enforced allowlist of tool sequences as a cheap, auditable "this is all it may do" promotion artifact.
- **Sub-agent spawning policy** — agents may appoint sub-agents only with explicit principal consent, with delegation chains linked in logs to the originating owner.
- **Safe behavioral defaults & duty to clarify** — least-disruptive action, conservative spend and scope, stop-and-ask on ambiguity, and time-boxed authority that lapses without review.
- **Emergent market-conduct risk** — trading-adjacent agents can *learn* spoofing-like or tacitly collusive behavior without instruction, requiring market-conduct surveillance of agent behavior and behavioral stress testing.
- **Automated sprawl detection** — actively scan for shadow, orphaned, and duplicative agents, permission drift, and undeclared AI inside approved SaaS, with periodic owner recertification — registry-only capture is insufficient.
- **Proactive, not reactive, governance** — incident-triggered-only governance kicks in only after damage may have occurred, so launch is gated on registry + IAM + policy + HITL + risk classes being in place.
- **Program KRIs & governance-effectiveness review** — quantitative indicators (injection attempts blocked, DLP hits, anomalous tool-call rates, sprawl index, approval review rates) with a biannual review of whether governance itself is working.
- **Regulatory watch** — a quarterly process tracking EU AI Act applicability, automated-decision restrictions, and regulator-grade explainability expectations into policy updates.

## 7. Security 

- **Secrets** — no credentials and API keys in code, ever; vault-issued, scoped, rotated credentials in every sanctioned runtime. Short session TTLs so an initial login isn't valid forever.
- **Least privilege** — agents and apps get only the data, tools, and endpoints they actually need, with no over-permissioning.
- **Data security / DLP / exfiltration** — sensitive data neither leaks into external AI tools nor out through the app itself, with DLP covering citizen-built egress paths.
- **Prompt injection & the lethal trifecta** — an agent combining untrusted input, sensitive data, and egress will eventually be steered, so every app must sever one leg (zone architecture) as a strict architectural rule, not an AI-guardrail judgment call.
- **Supply chain** — hallucinated/typosquatted packages, unvetted MCP servers, and low-code marketplace components, mitigated by curated allowlists and internal mirrors rather than per-app vetting.
- **Identity & access** — non-human identities for automations, SSO everywhere, RBAC, no shared logins, an app's entitlements never exceeding its builder's, and an audit trail of who accessed what through the app.
- **Excessive agency & blast radius** — over-permissioning with respect to *actions*: bound what an agent can do and how much damage a single malfunction can cause.

### Advanced / Day 3

- **Memory poisoning & memory lifecycle** — agent memory is a governed asset with TTL, validation-before-write, per-user scoping, and provenance, with memory-write as a promotion-gated capability.
- **Cross-session / delayed-detonation attacks** — a payload injected in one session detonates weeks later, so session-scoped logs never show it; requires cross-session memory audits and longitudinal drift monitoring.
- **Goal/plan hijack** — individually benign actions composing a hostile plan, distinct from prompt injection; countered by pre-execution plan validation and dry runs for high-risk actions.
- **Agent impersonation & spoofing** — mutual authentication between agents, because a spoofed "compliance agent" is a high-quality internal phishing platform.
- **Inter-agent propagation & contact policies** — worms, collusion, and cascading failures once agents call each other; countered by signed messages, circuit breakers, and owner-defined who-may-contact-whom policies with expiring, quota'd credentials.
- **Human manipulation by the agent** — the reverse channel: an injected agent socially engineering its own approver, sycophancy-driven over-trust, and disclosure when colleagues unknowingly interact with an agent.
- **Self-modification** — agents must not write to the repos, configs, prompts, or IAM that define them, a default hazard when builder and agent share a workspace.
- **Resource-overload / availability attacks** — a steered or hallucinating agent exhausts DB connections or hammers internal APIs; countered by statement timeouts, query-cost validation, connection caps, and per-agent rate limits.
- **Cross-user context leakage** — one builder's agent serving many users must scope session memory per user and entitlement, or user A's MNPI bleeds into user B's answers.
- **AI-enabled fraud against the firm** — deepfake voice and synthetic-identity attacks on the very approval workflows citizen agents widen (agents that send email or trigger payments).
- **Model supply chain** — fine-tuned or third-party checkpoints can carry dormant backdoors, so citizen devs are restricted to an allowlist of approved model endpoints with provenance verification.
- **Instance-level agent identity & lineage** — a unique ID per running instance stamped on every output and call, tied to a machine-readable agent card, with lineage links for copied or forked agents.
- **JIT / ephemeral credentials & on-behalf-of** — short-lived scoped tokens minted per task, with agents acting under the invoking user's entitlements instead of standing over-privileged service accounts.
- **Adversarial testing at the gates & control evaluations** — injection fuzzing, memory-poisoning probes, and privilege-escalation scenarios proportional to tier, plus red-teaming the control stack itself (can a hijacked agent subvert its monitors?).
- **Per-app lightweight threat modeling** — a scaled-down data-flow diagram, asset-impact table, and attack-vector walkthrough at the promotion gate.
- **MCP-specific vetting** — tool-metadata pinning and re-vetting on change (rug-pulls), static scanning of tool descriptions, OAuth posture checks for remote servers, sampling disabled by default, and caps on servers per agent.
- **Data-flow integrity at the tool-call level** — even with a fixed plan, injected data can redirect tool *arguments* (recipient, filename), requiring provenance tagging and a deterministic policy check before each call.

## 8. Training — Training and Education

- **Certification before empowerment** — training tier unlocks tool tier; nobody receives a sanctioned tool without the matching training to use it properly according to the user contract. 
- **Firm-wide AI literacy (Level 0)** — everyone learns what the tools can and can't do, hallucination, prompt injection in plain terms, the personal-AI-accounts rule, and how to report concerns.
- **Builder certification (Level 1)** — the user contract, tiers/zones/trifecta logic, gate process, and secrets hygiene, short and testable, renewed annually. Spec-driven development: spec, code, test.
- **Tool-specific training (Level 2)** — the golden path per sanctioned platform, its guardrails, and what it deliberately doesn't solve.
- **Advanced agentic training (Level 3)** — evals for stochastic components, agent failure modes (memory poisoning, goal drift, approval fatigue), and when to escalate to professional development.
- **Reviewer & approver training** — the people staffing gates and HITL approvals must be taught what a meaningful review looks like, or oversight degrades to rubber-stamping.
- **Ongoing learning loop** — microlearning from incidents and near-misses (blameless postmortems as teaching material) and refreshers when policy or tools change, with KPIs on the skilling program itself.
- **Knowledge sharing & community** — AI Slack channels, show-and-tells, a shared prompt/pattern library, and an internal showcase that drives reuse-before-build.
- **Support as enablement** — one visible front door for questions and gate submissions, weekly office hours, and paired builds with a platform engineer on first higher-tier projects.
- **Worked examples, anti-patterns & FAQ** — people copy examples, not policies, so the corpus includes annotated builds, named red lines, and honest answers to "why can't I use my personal ChatGPT."
- **Enablement as the third leg of enforcement** — most non-compliance is ignorance plus friction, so every gate-checklist item must trace to a template, a training module, and a support channel.

## 9. Analytics — Analytics, AI Development & MLOps

- **Evals for stochastic components** — any AI-dependent behavior carries evals with published metrics, because "know it works" is the standard and vibes are not evidence.
- **Model drift & silent updates** — no automatic adoption of new models: switch explicitly after evals, and eval regularly anyway because vendor models change silently.
- **Self-improvement under evaluation** — any agent that tunes or modifies its own behavior does so only inside an eval harness that catches regressions.
- **Escalation to professional MLOps** — when a citizen artifact contains a real model, eval loop, or production ML, it inherits MLOps discipline or transfers to the central team.

### Advanced / Day 3

- **Eval infrastructure as a platform service** — regression evals re-run on every upstream model change, model-version pinning, canary traffic with rollback, and LLM-judge scoring of production traffic with drift detection.
- **Goal/value misalignment** — the agent that "succeeds" at the metric while damaging the intent (task-proxy optimization), countered by context layers encoding priorities and binding constraints.
- **Agent performance reviews** — an HR-like lifecycle per agent: onboarding validation, periodic reviews of accuracy, drift, and bias, retraining, and retirement.

## 10. Use-Cases — Use Cases

- **Portfolio selection & sequencing** — low-risk / high-impact use cases first, with pilots sequenced to build the program's case.
- **Red-line use cases** — citizen development is *not* for the order/execution path, official NAV or books-and-records, client-facing output without compliance review, or unsupervised agents in production.
- **Don't automate a broken process** — automating a bad workflow industrializes its defects; fix the process or flag it before building on it.
- **Value tracking** — hours saved, spreadsheets retired, and backlog items self-served, tracked at the portfolio level so the program can defend its ROI.

## 11. Partnerships — External Partnerships

- **Vendor due diligence & the enterprise bar** — SOC 2 / ISO evidence, self-hosted or private-tenancy deployment, SSO/SCIM/RBAC, and exportable audit logs as the inclusion floor for any citizen-dev tool.
- **Baseline AI contract terms** — zero data retention, no training on firm data, contractual audit rights, and clear data ownership before any tool touches firm data.
- **Vendor viability & churn** — tools in this space evolve and die quickly: short contracts with opt-outs, POCs on your own data before believing accuracy claims, hedging across 2–3 platforms, and a data-export exit path.

### Advanced / Day 3

- **Governance by contract** — model-update notification with pre-enablement testing rights, subvendor "daisy chain" visibility, and loyalty/conflict-of-interest terms (does the platform use your prompts for its own purposes?).
- **Client/host security posture as a selection criterion** — identical tool-poisoning attacks succeed on some agent clients and fail on others, so the desktop/IDE agent client is a security decision, not a preference.
- **Vendor safety-transparency checklist** — require an agent system card, documented sandboxing and stop controls, guardrail defaults, incident-disclosure history, and a clear accountability split across model, platform, builder, and deployer.
- **Sovereignty & data residency** — hosting location, data residency, and provider country-of-origin as explicit selection-matrix columns.
- **Liability & insurance mapping** — map where control actually sits at each workflow step and align vendor indemnities and E&O/cyber coverage to it before a loss forces the question.
- **Agent conduct toward third parties** — citizen agents hitting vendor or counterparty sites must declare themselves and respect robots.txt/ToS, because undeclared agent traffic is a live legal and reputational risk.
- **Market-data licensing** — agents that redistribute or train on licensed market data can breach vendor terms, so data-license scope is checked at intake like any other entitlement. *(new)*

## 12. Process — Business Integration and Process Implementation

- **Real workflow integration & change management** — process owners sign off, before/after outcomes are measured, and adoption is tracked, because a tool nobody's workflow depends on is a hobby.
- **Criticality is a property of usage** — the danger zone is low-maturity code with high operational criticality, so governance must re-evaluate and retrofit controls (CI/CD, testing, BCP/DR) when citizen code becomes load-bearing.
- **Documentation standards** — README, runbook, data lineage, and a named owner per artifact, with the test being: could someone else operate this tomorrow?
- **BCP/DR proportional to criticality** — backup, restore, and failover with recovery *tested*, not assumed, including fallback when a required AI or cloud dependency goes down; the mission-critical house of cards is the named anti-goal.

### Advanced / Day 3

- **Fleet-level correlated failure** — dozens of agents on one model or gateway fail simultaneously (bad update, outage, shared jailbreak), so plan manual redundancy sized beyond single failures and buy diversity where it's cheap.
- **Support tiers, SLAs & ITSM integration** — who fixes a broken departmental agent at 7am, on what SLA, through which ticket queue, with standardized runbooks per support class.
- **Incident & near-miss learning loop** — low-friction reporting for users *and counterparties of the agent*, with a documented loop feeding lessons into gates, allowlists, and training, plus an ethics-hotline path for gray areas.

---

## Editorial notes (what was split, merged, or added)

- **No "Engineering discipline" bucket exists**, so §3.1 was distributed: version control, testing, environments, primitives, performance, and sanctioned tooling → **Tech**; logging and kill switch → **Observability**; evals and drift → **Analytics**; documentation and BCP → **Process**; the data-access map → **Data**.
- **Duplicates merged:** observability/logging appeared twice in §3.3 (merged into one Observability item); adversarial gate testing appeared in §3.3 and G3 (merged into one Security advanced item); progressive autonomy appeared in §3.3 and G1 (core principle in Governance, G1 detail as its advanced item); BCP appeared twice (§3.3 and the AI/cloud-outage bullet, merged in Process); self-modification and resource overload each appeared in §3.1 and C9/C10 (courtesy/backoff kept as Tech core, the attack variants as Security advanced); "emergent market manipulation" (§3.3) folded into C12; model-and-vendor drift split into model drift (**Analytics**) and vendor churn (**Partnerships**); AI sprawl (core) and O1 automated sprawl detection (advanced) kept as a core/advanced pair in Governance.
- **Splits:** "PII & sensitive data handling" split into data classification (**Data**) and regulatory exposure (**Governance**); C5 inter-agent propagation and G10 contact policies merged into one threat-plus-control item.
- **Additions:** one new concern — **market-data licensing** under Partnerships (flagged *(new)*). Everything else traces to the draft.
- The Documentation/Training/Support prose sections were absorbed into **Governance** (published program documents), **Training** (levels 0–3, reviewer training, support, community, "third leg of enforcement"), **Team** (roles, champions), and **Process** (production support model).





**Create a polished institutional-quality equity research report for [COMPANY / TICKER].**

- modern hedge-fund or institutional equity-research product: analytical, data-dense, highly legible, restrained, and sophisticated. 
- White or very light background with a dark navy institutional header on every page.

- restrained financial palette: navy and charcoal as primary colors; green for positive data, red for negative data, amber/gold for caution, and blue for neutral/informational signals.
- Clean sans-serif typography with strong hierarchy.
- Large, bold KPI numbers with small uppercase labels.
- thin borders, subtle shaded panels, rounded rectangular cards, generous alignment and consistent spacing.
- Favor **small multiples, KPI cards, compact tables, bar charts, timelines, scenario matrices and callout boxes** over decorative graphics.
- No gradients, stock photography, 3-D charts, unnecessary illustrations, oversized logos, or presentation-template gimmicks.
- Keep charts simple and analytical: direct labels, minimal legends, minimal gridlines, clear units and periods.
- Tables should resemble institutional research: compact, aligned numeric columns, alternating subtle row shading, highlighted company/total rows.

- 

