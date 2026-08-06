# Outline proposal



# Citizen Development in a Hedge Fund — A Primer and Implementation Guide

**Date:** 2026-07-15
**Status:** Proposed outline
**Audience for the finished document:** hedge-fund / asset-manager CTO and tech leadership designing and sanctioning a citizen-development program.
**Tool scope:** broad landscape, enterprise-grade only (see Ch 4 inclusion bar).



---

 Consider this an outline and first draft notes (lots of AI slop)

1. Concerns to address - by category
2. Foundational tooling / prerequisites by category
3. Day 1 tooling by category and stack case studies
4. Implementation
5. Operation
8. Advanced / Day 3 / future concerns, implementation, operation

Potential group process:

Participant contract: Chatham house rules, don't share anything proprietary obviously, maybe check what e.g. b-schools say for group. project

Divide labor into groups:

1. compliance, governance, teams, training, citizen dev policies and user. contract, ongoing processes, gating, monitoring

2. tech stacks, 
   1. security / devops / runtime infrastructure
   2. deb process / agent frameworks / no-code / dev environments
   3. data engineering
3. Use cases
   1. front office use cases
   2. middle/back office use cases

Provide a shared directory where people can contribute reference docs, white papers, academic papers, etc, industry press, vendor docs, and apply AI to them

https://drive.google.com/drive/folders/1HAcg-nroLAo2bHvZLHtqhxDtYO8W4ef9?usp=sharing

Ideal scenario would be e.g. Slack that is connected to the docs and AI with groups able to converse with docs and draft and each other, channel for each writing group. I think people should view as a personal project out of work like they are doing exec MBA with a shared educational project. 

Kickoff Zoom, brainstorm groups and  get people to join groups

Each group elects a leader, submits draft of their chapter/section on a schedule in a shared directory

Assemble doc, group leaders maybe submit comments with input from team, have a Zoom meeting to finalize, write introductory part (exec summary/motivation below)

Consider leveraging result for social/event/membership drive
for instance could do a session with a public YouTube posted on website to present finding
encourage members to share on socials and refer new members
do a press release and try to place in e.g. Institutional Investor, hedge fund week or whatever the go-to  pubs are, highlight other good stuff AITEC does like DDQ



# Chapter outline

## Intro / Executive summary 
- Origin story of the document.
- A playbook for standing up a governed citizen developer program.
- **Thesis**: end users know the business; IT knows what makes software succeed; a thoughtful citizen-developer program packages IT's knowledge as platform defaults, templates, and services. It makes the disciplined path the default path, and as you follow the path, it governs with risk-proportionate approval gates, checks and balances. In appropriate business-critical enterprise use cases there is a path from citizen prototype to full-fledged IT project. 
- The big win is a program that can deliver execution on the long tail of dev needs that central IT will never reach, with risk held inside explicit tiers and zones, and review proportionate to risk. 
- Firms that channel AI-assisted citizen development compound its benefits, while firms that block it inherit shadow-AI risk with less of the upside.
- Business objectives (what we are maximizing), constraints (regulatory and business rules that must never be violated, principles for resolving conflicts)
- Focus on day 1/day 2 - with brief discussion of advanced concerns for future
- Focus tends to be on firms with resources for a comprehensive program: could break types into enterprise vs. small shops and annotate recipes/recommendations with types of firms 
- Focus is on citizen devs making agents that talk to AI since that is the high risk use case. If someone just wants to make a dashboard with no access to AI, that doesn't need the full governance structure.
- Outline of how the doc proceeds
  1. Intro/why
  2. Concerns
  3. Foundations and prerequisites
  4. Tooling
  5. Implementation and deployment
  6. Operations and governance
  7. People and enablement
  8. Do's and don'ts, example stacks and recipes, anti-patterns
  9. Appendices, docs and schemas

## Ch 1. Motivation: 
### 1.1 The knowledge asymmetry
- **The end user is closest to the problem:** knows the workflow, the data, the tacit knowledge and 'real' requirement; iterates at the speed of their own frustration.
- **IT knows the invisible 80% of successful software:** integration, testing, version control, CI/CD, logs, metrics, reporting, security, BCP/DR, robustness and resilience, maintainability/tech debt, tradeoffs of speed, cost, capability, tradeoffs of AI intelligence vs. predictability — everything that determines whether the project still works in six months when the author is on vacation or leaves the firm.
- **Neither party can substitute for the other:** they are complementary, and a requirement round-trip through a product manager and a spec document can lose critical tacit knowledge.
- **Historical failure modes:**
  - **IT monopoly**: multi-year backlog; the business routes around it; the ungoverned Excel/VBA/script estate likely already present in every organization. Shadow IT becomes a workaround, a symptom of monopoly and failure to address business requirements, not clueless users' gratuitous noncompliance.
  - **Free-for-all**: a portfolio of mission-critical houses of cards — untested, undocumented, unrecoverable risks, key-person-dependency.
- **There are parallels to PCs in the 1980s:** IT was resistant to users with PCs, writing batch files, Excel workflows. Eventually processes evolved to balance the cost and functionality benefits of PCs with the risks. The IT folks were not wrong. As recently as 2012 the [London Whale](https://www.henricodolfing.ch/en/case-study-18-how-excel-errors-and-risk-oversights-cost-jp-morgan-6-billion/) had a $16b loss, from large trades managed through series of worksheets including copy-paste workflows that were not appropriately governed and may have had formula errors. However well-run orgs have implemented best practices to avoid these pitfalls. 
- **Problem statement: maximize value-add from end-user citizen devs without breaking everything.**
### 1.2 Why now: AI broke the old equilibrium
- **AI coding tools collapsed the cost of producing working-looking software;** the free-for-all can happen whether sanctioned or not.
- **The same tooling can collapse the cost of proper governance and discipline:** Claude Code can make tests, git, and review the default path; low-code runtimes build in logging and credential handling.
- **Firms that channel this can compound its beneifts; firms that block it can get shadow AI risks plus less of the upside.**
### 1.3 Citizen Development in 2026

Low-code platforms have evolved from drag-and-drop form builders to vibe-coding real software with Claude Code, alongside a matured low-code market that can include AI calls and can also be created via AI prompts in addition to drag-and-drop flowcharts.

![image-20260731113604618](/Users/drucev/Library/Application Support/typora-user-images/image-20260731113604618.png)



![n8n Review (2026): The Workflow Automation Tool Power Users Actually Stick With](https://storage.ghost.io/c/08/a3/08a3cb77-16f2-4623-b90a-2936db90af0a/content/images/size/w1200/2026/01/n8n-screenshot-readme.png)

The line between "citizen" and "professional" developer is now a ladder of implementation discipline, not a ladder of syntax and coding knowledge.

Each rung: what they can build, what tooling fits them, what supervision they need.

- Power user 
- → analyst who automates 
- → technical analyst / quant-adjacent 
- → embedded developer

Similarly, there is an end-product artifact ladder;

- Personal script 
- → shared team tool 
- → official department workflow 
- → business-critical application.

We can create 2 axes of maturity vs.  how critical the code is in daily operations. 

![image-20260731120253511](/Users/drucev/Library/Application Support/typora-user-images/image-20260731120253511.png)

The danger zone is low maturity, high criticality. Governance must exist to re-evaluate code and implement controls and process like CI/CD, testing, BCP/DR when citizen-developed code becomes load-bearing.

What citizen development is *not*: 

- *Not* a replacement for central dev on high-stakes trading-adjacent, books-and-records, or client-facing systems.
- *Not* unsupervised agents in production
- *Not* consumer AI SaaS on enterprise data.

### 1.4 Synthesis / problem definition

- **Objectives**: Maximize value added.
- **Constraints**: Regulatory and business rules that must be followed.
- **Principles**: Rules for resolving conflicts between objectives.
- Users supply problem knowledge; the IT platform supplies software implementation, operation, and governance knowledge as **platform defaults, shared primitives, usage policies, and governance and gates proportionate to risk**.
- Success criterion for every mechanism in this document: are safe, happy paths available, easier than the unsafe, sad paths, and are appropriate risk-proportionate controls in place to ensure citizen devs avoid shenanigans and stay on safe paths?
- important concepts/components
  - Agent frameworks / platforms like Claude Code
  - Observability and control infrastructure: SIEM, role-based and attribute-based access controls, trust zones, a governance/security stack
  - Governance and process: Tests/evals, promotion gates

![image-20260731114507910](/Users/drucev/Library/Application Support/typora-user-images/image-20260731114507910.png)

## Ch 2. Concerns

At 30,000 foot level, 3 types of concerns:

1) **Agents as insider threats**, taking costly or dangerous actions, exfiltrating, deleting, other security and compliance violations, 
   1) **Why?**
      1) Prompt injection.
      2) Hallucinations, reward hacking, running off the rails and going feral
      3) User error
      4) Fraud
      5) Security compromises 
   2) Agents are like users, they cannot be fully controlled by policy guardrails, they are subject to social engineering.  Risks of deviating from expected behavior cannot be eliminated, only bounded by what the agent can do. Attacks and problems can occur at multiple layers, llms, agents, governance, composition of multiple components and layers. Architectural controls, permissions, trust zones dominate runtime checks on inputs and outputs and behavior. 
2) **Efficiency or cost-benefit/ROI concerns**: Agents not fit for task or performing to expectations: stochasticity not accounted for, model drift, big differences between dev, test and prod, high cost of tokens or human babysitting
3) **Meta concerns**:  governance issues, tech debt spiral, operational issues, outcomes not well measured so you don't even know if it's failing, accountability, vendor risk, key person risk, fragility, loss of oversight, skill and talent pipeline atrophy

---

### 2.1. Leadership 

- **Executive mandate** — The program has a named executive owner, stated objectives, constraints, principles for resolving conflicts, risk appetite, and resources for the platform team. Without leadership sanction and governance, citizen development *is* shadow IT. **Leadership approves** the major components, citizen-dev user contract, acceptable use policy, plans, budgets, timelines.
- **Program management, monitoring, and ROI measurement** — citizen development is in the firm's strategic plan with tracked objectives and metrics.
- **Leadership promotes** citizen dev, attends kickoffs/hackathons, celebrates wins by the org. 

### 2.2. Team 

- **Defined program roles** — 
  - Platform team
  - Champions/owners per desk/function
  - Reviewers
  - Executive sponsor, 
  - Transition path to IT-owned development must all be clearly specified
- **Explicit user contract** between citizen devs and IT with a **Federated operating model** — a central platform with distributed builders, but common standards. IT packages its knowledge as defaults and services rather than acting as a gatekeeper or bottleneck. Use policies, citizen devs understand what agents can/cannot do, understand they are responsible for what the agent does. 
- **Key-person risk** — one-person tools are capped at low tiers, with shared ownership and a named backup operator required for promotion. **Documentation** standards in the user contract: README, runbook, data lineage, named owner; the test: could someone else operate this tomorrow? 
- **Governance capacity** — gates and human-in-the-loop approvals have trained reviewers and regular cadence, or governance becomes a new backlog people route around.
- **Regular review of the citizen-dev program with metrics**, number of projects and milestones achieved, increasing program capability and maturity 

### 2.3. Data 

- **Data foundations as precondition** — citizen apps industrialize whatever data quality exists, so golden sources, named owners, and monitored quality must precede the program, not build a tower on a weak foundation like a data swamp.
- **Data well-documented** — a proper data dictionary / API catalog makes "use SQL, not a scraper" the easy happy path documented in the user contract.
- **Classification & labeling** — machine-readable sensitivity labels (public / internal / confidential / PII / MNPI / other data) determine zone assignment, DLP, tool eligibility.
- **Entitlements** — who-may-see-what is clean, documented, audited, lives in systems (RBAC, row/column security), so citizen apps inherit entitlements from infrastructure.

### Advanced / Day 3

- **Cryptologically secure data pipeline integrity** — data has signed ingestion pipelines, versioning and lineage.

### 2.4. Tech platform 

- **Version control & recoverability** — all citizen dev in git from day one, with a known-good version to roll back to, so a builder is never stranded on a broken build.

- **Consistent, repeatable, isolated environments** — dev containers, lockfiles, and project templates so every artifact survives a second machine and a second person, with dev and prod properly separated and permissioned. Zones and containers constrain the blast radius where the code runs. Sanctioned environments (Claude Code with managed settings and hooks, n8n) where discipline is built in. Behind network egress proxies, e.g. Zscaler, LiteLLM, MCP/tool gateway.

  Limit blast radius with **execution zones**, so agents and sub-agents can spin up with appropriate scope. Contain, don't explain:

  - **Green zone:** full internet and LLM access, no access to internal data. Users can run research on publicly available data. Github Codespaces, Cloudflare workers etc. Moving internal data into Green zone must be prevented or restricted/monitored, since a prompt will leak it. Implementation:
    - **External services:** Anthropic-managed sandboxes (least work). [Claude Code Docs](https://code.claude.com/docs/en/sandbox-environments)[Claude Platform Docs](https://platform.claude.com/docs/en/managed-agents/environments) . similar with other AI providers, Snowflake, Databricks. Or Sandbox-as-a-service (E2B, Modal, Daytona, Cloudflare Sandbox, Fly Sprites, Codespaces, Coder, or GCP Cloud Workstations). There are question marks: integration with identity, pushing code to private repos, logging, market data. However, agents going feral completely outside you firewall are relatively safe.
    - **Self-managed devcontainers** on e.g. Azure-hosted compute (most control). The claude-code repo publishes a reference devcontainer with a default-allow iptables firewall for external egress, no access to internal except users can ssh in. Trail of Bits maintains a hardened variant built for the untrusted-workload case. Wise to red-team it and see if Claude can escape it.
  - **Yellow zone**: no internet access, managed access to internal data and vetted enterprise LLMs. Users can run AI on internal data with no risk of exfiltration. A devcontainer with inverted firewall rules from red zone, no access except to vetted internal resources, data warehouse, package registry. Or Databricks, Snowflake, Sagemaker notebooks walled off from public internet, accessing data warehouse. 
  - **Red Zone**: no unvetted prompts, access to internal and external data. Only highly vetted workflows with no risk of prompt injection. 

- **Realistic tests and evals, not vibes** — edge cases, golden datasets, and negative tests, with special attention to AI stochasticity and hallucination-induced bugs. Evals for model drift, and auto-self-improvement

- **Common primitives, not reinvented wheels** — curated firm libraries for auth, data access, logging, notification, and scheduling, because every reinvented wheel is a wheel nobody maintains. The proxy layer / package registry users can pull from constrains supply chain attacks: Cloudmith, JFrog Artifactory + Curation, or Sonatype Nexus + Firewall . Documentation of which tool fits which task, each tool properly restricted to appropriate access. Tooling that automates good practice. **Sane implementation defaults and paved roads**: no web scraping when the warehouse or a REST API has the data; a published data-access map so the sane path is the discoverable path.

- **Acceptable performance & resource utilization** — Well-behaved consumption of shared resources with SLAs: exponential backoff with jitter, and no retry-storm / thundering-herd rushes when a resource comes back online.

- **Software-supply-chain hygiene**: Scanners are the last line of defense for protection. First line of defense is the paved road they start from, the package proxy they're allowed to pull from, and the blast radius of where their code runs. Use AI PR code reviews, ideally different model from the one that built the code, and feed back to AI to fix and escalate to IT when necessary. Critical checks: Secrets in code, prompt injection, SQL injection, lethal trifecta issues like cross-tool bridges, malicious / hallucinated packages (must use safe package proxy and minimum-age flags), license/IP issues, user contract red lines, repeatable evals when LLMs update, up-to-date documentation, missing tests/edge cases, general code smells. Consider tools like Socket, Semgrep, GitHub Actions and GitHub Advanced Security, Code Security, Secret Protection, CodeQL. 



### Advanced / Day 3

- **Design-pattern catalog mapped to use cases** — approved architectures (plan-then-execute, critic-optimizer with LLM as judge, quarantined/dual LLM, code-then-execute, context minimization) so citizen devs get blueprints, not just guidelines.
- **Tool design rules** — ban generic-capability tools (raw shell, `execute_sql`) in favor of parameterized least-privilege tools, with strict structured output on anything crossing a trust boundary.
- **Sandboxing baseline** — separate filesystem for agents, production reachable only through dedicated tools, and long-lived credentials never stored on the agent runtime (secrets manager with access permissioned per approved action).
- **Platform compliance traps** — codify each platform's dangerous defaults (e.g., Copilot Studio's 30-day transcript retention vs. books-and-records, cross-geography data movement, sharing rules, licensing conventions).
- **More advanced software supply chain tools** like Snyk, Endor, Apiiro, Legit.

### 2.5. Observability, Controls, Logging, Monitoring

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

### 2.6. Governance

- **The user contract / citizen-dev policy** — a single signed document covering what the firm provides, what the builder must do, red/yellow/green action rules, and the principal-agent principle: the human owner is accountable for everything their agent does. Users have tools to self-assess against the contract and firm policies. **Extend existing policy, don't fork** — build on the firm's acceptable-use policy, end-user-computing policy, and model-risk framework rather than writing a parallel regime.
-  **Framework alignment** — anchor the program to recognized frameworks: I[SO/IEC 42001 (AI management system)](https://www.iso.org/standard/42001), [ISO/IEC 23894 (AI risk management)](https://www.iso.org/standard/77304.html), [ISO/IEC 38507 (board-level governance of AI)](https://www.iso.org/standard/56641.html), [ISO/IEC 42005 (AI system impact assessment)](https://www.iso.org/standard/81118.html), [ISO/IEC 5338 (AI system lifecycle) ](https://www.iso.org/standard/81118.html), [ISO/IEC 27001 (cybersecurity)]( https://www.iso.org/standard/27001), [NIST AIMF](https://www.nist.gov/itl/ai-risk-management-framework) and [playbook](https://airc.nist.gov/airmf-resources/playbook/), [MITRE ATLAS](https://atlas.mitre.org/), OWASP [AI top 10](https://genai.owasp.org/llm-top-10/), [Agent top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [Agent security](https://genai.owasp.org/initiatives/agentic-security-initiative/), [AI security](https://owaspai.org/), [Google SAIF](https://safety.google/safety/saif/), [CSA AI Controls Matrix](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1)  
- **Active oversight duty** — deploying an agent is not the end of the job; the owner must maintain it as infrastructure and LLMs and business evolves, monitor it for performance and fitness for purpose, review flagged anomalies, and retain kill-switch authority.
- **Inventory & registry** — every artifact past personal-experiment stage is registered with owner, tier, zone, data classification, and dependencies.
- **Risk-proportionate gating & promotion** — documented criteria checklist per gate (experiment → sanctioned citizen dev → production deployment), proportionate to risk tier, with each gate asking what the worst-case scenario is under bad data, bad prompts, or runtime failure. Large changes outside assumptions use in gating must trigger review; higher tier agents should be re-reviewed on an annual cadence. Meets technical standards, tests, controls, observability, DR/BCP/rollback/killswitch; acceptable risks, managed appropriately; maturity appropriate for criticality.
- **Risk-proportionate human-in-the-loop operation** — the level of human review is set in contract and at gate review, per tier and action class.
- **Progressive earned autonomy** — agents start supervised and earn wider freedom only against a documented track record.
- **Regulatory exposure** — sensitive apps flagged at intake for heightened review, not discovered at audit: recordkeeping, comms surveillance, anything client-facing, anything on proprietary data, PII, HR or legal.
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

### 2.7. Security 

- **Secrets** — no credentials and API keys in code, ever; vault-issued, scoped, rotated credentials in every sanctioned runtime. Short session TTLs so an initial login isn't valid forever.
- **Least privilege** — agents and apps get only the data, tools, and endpoints they actually need, with no over-permissioning.
- **Data security / DLP / exfiltration** — sensitive data neither leaks into external AI tools nor out through the app itself, with DLP covering citizen-built egress paths.
- **Prompt injection & the lethal trifecta** — an agent combining untrusted input, sensitive data, and egress will eventually go astray, so every app must sever one leg (green/yellow/red zone architecture) as a strict architectural rule, not an AI-guardrail judgment call.
- **Supply chain** — hallucinated/typosquatted packages, unvetted MCP servers, and low-code marketplace components, mitigated by curated allowlists, package registry, minimum-age requirements, and internal mirrors rather than per-app vetting. Use threat intelligence feeds, vendor risk socrecards.
- **Identity & access** — non-human identities for automations, SSO everywhere, RBAC, no shared logins, an app's entitlements never exceeding its builder's, and an audit trail of who accessed what through the app. Logging of who did what is complex for agents if they can spawn sub-agents: should log e.g. log agent id, session id, parent, and root of call tree.
- **Excessive agency & blast radius** — over-permissioning with respect to *actions*: bound what an agent can do and how much damage a single malfunction can cause.

### Advanced / Day 3

- for most sensitive agents can consider advanced testing: injection fuzzing, memory-poisoning probes, privilege-escalation scenarios (tools exist: AgentDojo, Agent Security Bench, AgentPoison); recurring red-team exercises against high-tier agents;
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
- **Adversarial testing at the gates & control evaluations** — injection fuzzing, memory-poisoning probes, and privilege-escalation scenarios proportionate to tier, plus red-teaming the control stack itself (can a hijacked agent subvert its monitors?).
- **Per-app lightweight threat modeling** — a scaled-down data-flow diagram, asset-impact table, and attack-vector walkthrough at the promotion gate.
- **MCP-specific vetting** — tool-metadata pinning and re-vetting on change (rug-pulls), static scanning of tool descriptions, OAuth posture checks for remote servers, sampling disabled by default, and caps on servers per agent.
- **Data-flow integrity at the tool-call level** — even with a fixed plan, injected data can redirect tool *arguments* (recipient, filename), requiring provenance tagging and a deterministic policy check before each call.

### 2.8. Training / Support / Documentation 

- **Certification before empowerment** — training tier unlocks tool tier; nobody receives a sanctioned tool without the matching training to use it properly according to the user contract. 
- **Firm-wide AI literacy (Level 0)** — everyone learns what the tools can and can't do, hallucination, prompt injection in plain terms, the personal-AI-accounts rule, and how to report concerns.
- **Builder certification (Level 1)** — the user contract, tiers/zones/trifecta logic, gate process, and secrets hygiene, short and testable, renewed annually. Spec-driven development: spec, code, test.
- **Tool-specific training (Level 2)** — the golden path per sanctioned platform, its guardrails, and what it deliberately doesn't solve.
- **Advanced agentic training (Level 3)** — evals for stochastic components, agent failure modes (memory poisoning, goal drift, approval fatigue), and when to escalate to professional development.
- **Knowledge sharing & community** — AI Slack channels, show-and-tells, a shared prompt/pattern library, and an internal showcase that drives reuse-before-build.
- **Worked examples, anti-patterns & FAQ** — people copy examples, not policies, so the corpus includes annotated builds, named red lines, and honest answers to "why can't I use my personal ChatGPT."
- **Documentation**: Use AI to document AI. Comprehensive knowledge base wikis updated on a schedule from primary sources,  with owners responsible to review AI-generated issues and edits.
- **Reviewer & approver training** — the people staffing gates and HITL approvals must be taught what a meaningful review looks like, or oversight degrades to rubber-stamping.
- **Ongoing learning loop** — microlearning from incidents and near-misses (blameless postmortems as teaching material) and refreshers when policy or tools change, with KPIs on the skilling program itself.
- **Support as enablement** — one visible front door for questions and gate submissions, weekly office hours, and paired builds with a platform engineer on first higher-tier projects.
- **Enablement as the third leg of enforcement** — most non-compliance is ignorance plus friction, so every gate-checklist item must trace to a template, a training module, and a support channel.

### 2.9. Analytics

- **Evals for stochastic components** — any AI-dependent behavior carries evals with published metrics, because "know it works" is the standard and vibes are not evidence.
- **Model drift & silent updates** — no automatic adoption of new models: switch explicitly after evals, and eval regularly anyway because vendor models change silently.
- **Self-improvement under evaluation** — any agent that tunes or modifies its own behavior does so only inside an eval harness that catches regressions.
- **Escalation to professional MLOps** — when a citizen artifact contains a real model, eval loop, or production ML, it inherits MLOps discipline or transfers to the central team.

### Advanced / Day 3

- **Eval infrastructure as a platform service** — regression evals re-run on every upstream model change, model-version pinning, canary traffic with rollback, and LLM-judge scoring of production traffic with drift detection.
- **Goal/value misalignment** — the agent that "succeeds" at the metric while damaging the intent (task-proxy optimization), countered by context layers encoding priorities and binding constraints.
- **Agent performance reviews** — an HR-like lifecycle per agent: onboarding validation, periodic reviews of accuracy, drift, and bias, retraining, and retirement.

### 2.10. Use-Cases

- **Portfolio selection & sequencing** — low-risk / high-impact use cases first, with pilots sequenced to build the program's case.
- **Red-line use cases** — citizen development is *not* for the order/execution path, official NAV or books-and-records, client-facing output without compliance review, or unsupervised agents in production.
- **Don't automate a broken process** — automating a bad workflow industrializes its defects; fix the process or flag it before building on it.
- **Value tracking** — hours saved, spreadsheets retired, and backlog items self-served, tracked at the portfolio level so the program can defend its ROI.

### 2.11. External Partnerships

- [Consulting firm list](https://docs.google.com/spreadsheets/d/1E7uJWdiLfPMsvwikJRCc75genBz00lumv57b1H_nGK4/edit?usp=sharing)
- **Vendor due diligence & the enterprise bar** — SOC 2 / ISO evidence, self-hosted or private-tenancy deployment, SSO/SCIM/RBAC, and exportable audit logs as the inclusion floor for any citizen-dev tool. Vendor risk scorecards: SecurityScorecard, BitSight, ProcessUnity etc.
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

### 2.12. Process — Business Integration and Process Implementation

- **Real workflow integration & change management** — process owners sign off, before/after outcomes are measured, and adoption is tracked, because a tool nobody's workflow depends on is a hobby.
- **Criticality is a property of usage** — the danger zone is low-maturity code with high operational criticality, so governance must re-evaluate and retrofit controls (CI/CD, testing, BCP/DR) when citizen code becomes load-bearing.
- **Documentation standards** — README, runbook, data lineage, and a named owner per artifact, with the test being: could someone else operate this tomorrow?
- **BCP/DR proportionate to criticality** — backup, restore, and failover with recovery *tested*, not assumed, including fallback when a required AI or cloud dependency goes down; the mission-critical house of cards is the named anti-goal.

### Advanced / Day 3

- **Fleet-level correlated failure** — dozens of agents on one model or gateway fail simultaneously (bad update, outage, shared jailbreak), so plan manual redundancy sized beyond single failures and buy diversity where it's cheap.
- **Support tiers, SLAs & ITSM integration** — who fixes a broken departmental agent at 7am, on what SLA, through which ticket queue, with standardized runbooks per support class.
- **Incident & near-miss learning loop** — low-friction reporting for users *and counterparties of the agent*, with a documented loop feeding lessons into gates, allowlists, and training, plus an ethics-hotline path for gray areas.



## Ch 3. Foundations / prerequisites

Sequence is 

1. Prerequisites for enterprise AI: data, tech infrastructure, process
2. Ability to do agents at enterprise level
3. Ability to manage citizens building agent

here we discuss 1., prerequisites

### 3.1 Data foundations

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

### Foundation layer

| Category                       | Tier  | Leading examples                           |
| ------------------------------ | ----- | ------------------------------------------ |
| Identity & Access (IdP/SSO)    | day-1 | Microsoft Entra ID; Okta                   |
| Secrets Manager                | day-1 | Azure Key Vault; HashiCorp Vault           |
| SIEM / SOC                     | day-1 | Microsoft Sentinel; Splunk                 |
| EDR / XDR                      | day-1 | CrowdStrike; Microsoft Defender            |
| Network Security / SASE        | day-1 | Palo Alto Networks; Zscaler                |
| Identity Governance (IGA/ISPM) | day-2 | SailPoint; Saviynt                         |
| Non-Human / Agent Identity     | day-2 | CyberArk; Astrix Security                  |
| SSPM                           | day-2 | AppOmni; Obsidian Security                 |
| Software Supply Chain          | day-2 | Snyk; GitHub Advanced Security             |
| AI SecOps / Agentic SOC        | day-2 | Prophet Security; CrowdStrike Charlotte AI |
| Anti-Deepfake / Awareness      | day-2 | Adaptive Security; Reality Defender        |

### Data layer

| Category                   | Tier  | Leading examples                                        |
| -------------------------- | ----- | ------------------------------------------------------- |
| DSPM / Data Classification | day-1 | Microsoft Purview; Cyera                                |
| DLP                        | day-1 | Microsoft Purview; Cyberhaven                           |
| Data Access Governance     | day-2 | Varonis (page names no clear #2 — "category archetype") |

### Model & prompt layer

| Category                          | Tier  | Leading examples                                            |
| --------------------------------- | ----- | ----------------------------------------------------------- |
| AI Gateway                        | day-1 | LiteLLM (OSS default); Portkey                              |
| AI Runtime Security (AI Firewall) | day-1 | Prisma AIRS; HiddenLayer                                    |
| AI Access Governance / Shadow-AI  | day-1 | WitnessAI; Harmonic Security                                |
| LLM Observability & Eval          | day-1 | Langfuse; LangSmith                                         |
| AI Red Teaming / Guardrails       | day-2 | Mindgard; Guardrails AI (weak cues — OSS-skewed, no anchor) |
| AI-SPM                            | day-2 | Noma; Wiz                                                   |
| Agent Security (Runtime)          | day-2 | Zenity; Lasso Security (nascent)                            |
| Authorization Engine              | day-2 | Open Policy Agent; Styra                                    |
| MCP Gateway / Tool Access         | day-2 | Solo.io agentgateway; Kong (very new, no production anchor) |
| Tool Identity & Integration       | day-2 | Composio; Descope (nascent)                                 |

### Retrieval layer

| Category                   | Tier        | Leading examples                                             |
| -------------------------- | ----------- | ------------------------------------------------------------ |
| Entitlement-Aware RAG      | situational | Glean; Microsoft Graph (as Copilot's substrate)              |
| Enterprise Content Sources | situational | SharePoint; Google Drive (stub — infrastructure, not a shortlist) |
| Vector Retrieval           | situational | Azure AI Search; Pinecone (stub)                             |

### UX layer

| Category                   | Tier        | Leading examples                          |
| -------------------------- | ----------- | ----------------------------------------- |
| Enterprise AI Assistant    | day-1       | ChatGPT Enterprise; Microsoft 365 Copilot |
| Enterprise Browser         | situational | Island; Prisma Access Browser             |
| Browser Security Extension | situational | LayerX; Grip Security                     |
| Third-Party AI Apps        | practice    | no products — process category            |

### Governance layer

| Category                    | Tier          | Leading examples                                             |
| --------------------------- | ------------- | ------------------------------------------------------------ |
| Enterprise GRC              | day-1         | ServiceNow; Archer                                           |
| Vendor Risk / Cyber Ratings | day-1         | BitSight; SecurityScorecard                                  |
| AI Governance / Model Risk  | firm-specific | Credo AI; ModelOp (fragmented, no dominant player)           |
| Comms Surveillance          | firm-specific | Behavox; NICE Actimize                                       |
| Policy-as-Code              | day-2         | Open Policy Agent; Styra                                     |
| Ephemeral Environments      | practice*     | GitHub Codespaces; Azure Dev Boxes (*practice-tier but carries vendors) |

## 

## Ch 4. Agent tooling

### 4.1 The enterprise bar (inclusion criteria for everything in this chapter)

- Certifications: SOC 2 Type II minimum; ISO 27001; HIPAA-capable where relevant as a proxy for control maturity.
- Deployment: self-hosted, private-VPC, or enterprise-cloud tenancy; data stays in the firm's boundary; explicitly **excluded**: SMB SaaS-only tools (consumer Zapier tiers, Airtable-class app builders, hosted-only vibe-coding platforms).
- Identity & control: SSO/SAML + SCIM, granular RBAC, environment separation (dev/test/prod), audit logs exportable to SIEM.
- AI/data terms: zero retention, no training on firm data, contractual audit rights.
- Vendor viability: funding/ownership status (cross-reference the wiki's M&A map), exit path, data export.

### 4.2 Agentic coding 

- Enterprise deployment paths: Bedrock/Vertex or enterprise API; managed settings, permission modes, hooks as policy enforcement points; CLAUDE.md as the carrier of firm standards; devcontainer templates.
- Why it fits the top of the builder spectrum; what it deliberately doesn't solve (hosting, entitlements) and must inherit from the platform.
- Adjacent: GitHub Copilot Enterprise, Cursor for business — where they overlap and differ on auditability and policy control.

cowork type environments

### 4.3 Internal-tool builders

- Retool (self-hosted), Superblocks (on-prem agent architecture), Appsmith (self-hostable OSS) — UI + logic on top of existing databases and APIs.
- Evaluation against the catalog: what they automate (auth, RBAC, audit logs, connector credential handling) vs. leave open (testing, version-control depth, sprawl).

### 4.4 Enterprise low-code suites

- Microsoft Power Platform (Power Apps, Power Automate, Dataverse) — most funds already license it via M355; environments, DLP policies, managed environments, CoE toolkit as governance surface.
- The trade: deepest governance tooling vs. platform lock-in and sprawl-by-default; licensing traps.

### 4.5 Workflow automation & iPaaS

- n8n (self-hosted) as the governed automation anchor; Workato (enterprise iPaaS); Tines (security automation); Power Automate within the Microsoft estate.
- Where RPA (UiPath) still appears in funds and why it's a last resort vs. APIs.

### 4.6 Analytics & data-app self-service

- Streamlit — especially Streamlit in Snowflake: the run-the-app-next-to-the-data pattern that sidesteps egress entirely.
- Hex, Dataiku, KNIME, Posit/Shiny for the analyst tier; Python-in-Excel and Copilot as the on-ramp from the spreadsheet estate.

### 4.7 Data-plane connectivity (the deciding dimension)

- **On-prem data**: gateway/agent architectures (Retool self-host, Superblocks agent, Power Platform data gateway); read replicas and service accounts; never direct prod-DB credentials.
- **Enterprise cloud data** (Snowflake, Databricks, S3): native runtimes vs. external connection; entitlement inheritance; compute cost governance.
- **SaaS systems** (Salesforce, NetSuite, market-data APIs): governed OAuth connections, scoped service accounts, iPaaS-mediated vs. direct API; write-access as an automatic tier escalation.
- The connectivity rule: apps come to the data through governed connectors; credentials never live in the app.

#### Agent frameworks (code-first, for the top of the builder spectrum)

| Family                   | Leading examples                                             | Enterprise-bar notes (to verify)                             |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Orchestration framework  | LangGraph (LangChain); OpenAI Agents SDK                     | LangGraph: de-facto OSS default, self-hostable; LangGraph Platform / LangSmith for managed control plane. OpenAI SDK: lighter, provider-leaning |
| Provider agent SDK       | Claude Agent SDK; Microsoft Agent Framework (ex-AutoGen/Semantic Kernel) | Provider SDKs inherit the provider's enterprise terms; MS framework rides Azure tenancy |
| Multi-agent / role-based | CrewAI                                                       | OSS core self-hostable; enterprise control plane newer — verify certs and viability |

#### Managed / low-code agent builders

| Family                       | Leading examples                                             | Enterprise-bar notes (to verify)                             |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Suite-native agent builder   | Microsoft Copilot Studio; Salesforce Agentforce              | Ride the M365/Salesforce estate: tenancy, DLP policies, connector governance already in place; lock-in and per-seat/per-conversation pricing traps |
| Cloud-platform agent runtime | Amazon Bedrock Agents / AgentCore; Google Vertex AI Agent Builder | Run inside the firm's cloud boundary; IAM-native; strongest story for yellow/green-zone agents |

#### Internal-tool builders (UI + logic on existing data)

| Family                 | Leading examples                                  | Enterprise-bar notes (to verify)                             |
| ---------------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| Internal-tool platform | Retool (self-hosted); Superblocks (on-prem agent) | Both market self-host/VPC + SOC 2 + SSO/SCIM + audit logs; Superblocks' agent keeps data on-prem with SaaS control plane |
| OSS alternative        | Appsmith                                          | Self-hostable OSS; enterprise edition for SSO/RBAC/audit — verify gap vs. Retool on governance depth |

#### Enterprise low-code suites

| Family                 | Leading examples                                             | Enterprise-bar notes (to verify)                             |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Citizen low-code suite | Microsoft Power Platform (Power Apps / Automate / Dataverse) | Usually already licensed via M365; environments, DLP policies, managed environments, CoE toolkit = deepest governance surface; sprawl-by-default risk |
| Pro low-code (IT-led)  | OutSystems; Mendix                                           | Enterprise app platforms — heavier than citizen tier; relevant as the promotion target for apps that outgrow citizen tooling |

#### Workflow automation / iPaaS / RPA

| Family                   | Leading examples        | Enterprise-bar notes (to verify)                             |
| ------------------------ | ----------------------- | ------------------------------------------------------------ |
| Self-hostable automation | n8n                     | Self-hosted deployment is the governance anchor; verify enterprise tier (SSO, RBAC, audit, secrets integration) |
| Enterprise iPaaS         | Workato; Power Automate | Workato: enterprise connector catalog (Salesforce, NetSuite), governed OAuth, SOC 2. Power Automate: within Microsoft estate + data gateway to on-prem |
| Security automation      | Tines                   | Common in fund security teams; strong audit posture — a pattern for what governed citizen automation looks like |
| RPA (legacy last resort) | UiPath                  | Still present in funds for no-API systems; prefer APIs; screen-scraping = the "sane implementation choices" anti-pattern institutionalized |

#### Analytics & data-app self-service

| Family                         | Leading examples                        | Enterprise-bar notes (to verify)                             |
| ------------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| Data-app framework             | Streamlit — esp. Streamlit in Snowflake | Run-the-app-next-to-the-data: inherits Snowflake RBAC, no egress — the cleanest yellow-zone pattern |
| Collaborative notebooks / apps | Hex; Dataiku                            | Hex: SQL/Python notebooks → shareable apps, SOC 2, VPC options. Dataiku: enterprise DS platform common in asset management; governance features built in |
| Visual analytics workflow      | KNIME; Posit (Shiny/Workbench)          | Self-hostable; KNIME strong for no-code data pipelines; Posit for the R-leaning analyst tier |
| Spreadsheet on-ramp            | Python in Excel + Copilot               | Where the existing EUC estate meets the new world; governed by M365 tenancy — the migration path, not the destination |

#### Excluded below the enterprise bar 

| Family                      | Examples                                      | Why excluded (§6.1)                                          |
| --------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| Hosted vibe-coding builders | Lovable; v0; Bolt                             | SaaS-only, code + data on vendor infra, thin enterprise controls — fine for throwaway prototypes on public data (green zone) at most |
| Hosted app/agent platforms  | Replit; Glide; Softr; Airtable-class builders | Predominantly hosted multi-tenant; some claim enterprise tiers — verify, but default posture is exclude |
| Consumer automation         | Zapier (consumer/team tiers)                  | SMB posture, credential sprawl; enterprise tier exists — if allowed at all, only via governed connections |

### 4.8 Selection matrices or decision trees

- Tool family × concerns catalog (which concerns each automates, mitigates, or ignores).
- Tool family × builder-spectrum rung; 
- A short opinionated shortlist/decision tree per fund size, dated, with detail delegated to the wiki.

## Ch 5. Implementation and deployment plan

### 5.1 Mapped to Crawl → Walk → Run → Fly

- Crawl: policy written, tools sanctioned, execution environment deployed, fregistry stood up, pilot cohort picked.
  - user contract must-haves and optional
- Walk: pilot builds in yellow/green zones, gates exercised for real, primitives library seeded.
- Run: broad enablement, champions active, first promotions through Gate 3, agentic patterns under HITL.
- Fly: gates enforced by technical controls, portfolio-level value tracking, graduation paths for autonomous agents.

### 5.2 The pilot

- Selection: low-risk / high-visibility / data-available; 5–10 builders across functions; explicit success and kill criteria.

### 5.3 Metrics

- Delivery: tools built, hours saved, spreadsheets retired, backlog items self-served.
- Risk: incidents, gate-failure reasons, unregistered-app discoveries, secrets-scan hits.
- 30/60/90 skeleton with owner per item.

### 5.4 The platform

- One diagram: identity spine → data access layer → sanctioned tool runtimes → deployment targets, with the AI gateway and SIEM wrapped around everything.
- 9.5 Identity spine
  - SSO on every tool; RBAC groups mapped to desks/functions; non-human identities for schedulers and agents; entitlement inheritance principle.

- 9.3 Data access layer
  - Entitlement-aware, read-only marts for citizen consumption; the published data-access map / API catalog; service-account issuance process.

- Secrets management
  - Vault integration in every sanctioned runtime; no secrets in code as an enforced (scanned) rule, not a request.

- 9.5 AI gateway & logging
  - All model calls through the gateway: logging, DLP, model allow-lists, cost attribution; SIEM export from every runtime.

- 9.6 Environments & deployment paths
  - Golden repo templates, devcontainers, CI defaults; the graduated path: laptop → zone-scoped sandbox → hosted internal app → (rarely) production.
  - Ephemeral environments for green-zone experimentation.

- The primitives library and reference apps
  - Firm-blessed building blocks: auth client, data connectors, logging/alerting, notification, scheduling, prompt library, document generation; contribution process so the library grows from real use.

- 9.8 The registry
  - Minimum record: owner, tier, zone, data classification, dependencies, last review; automated discovery to catch the unregistered.

## Ch 6. Operation and governance

### 6.1 Policy and User contract

- The contract with the citizen developer: 
  - what tools, API, artifacts IT gives you , documentation, help
  - what the dev must do 
    - e.g. must store passwords in secrets manager
    - must have a dev and prod, must put stuff in source control
    - follow mandatory review process / gate for deploying with risk-appropriate testing, logging etc
    - agent must follow policies
      - red - prohibited , never do
      - yellow - heightened review and human in the loop
      - green - OK
    - they are responsible for success, ROI
    - **The Principal-Agent Relationship:** In legal and operational terms, the human creator is the "principal" and the AI is their "agent." Therefore, the human user is ultimately responsible and accountable for their agent's actions, decisions, and any resulting misbehavior.
    - **Active Oversight:** The contract should state that "deploying" an agent is not the end of the job. The user is required to actively monitor the agent's audit logs, review flagged anomalies, and maintain the authority to trigger a "kill switch" to pull the agent offline if it deviates from its intended goals
- Defined owners and business objectives for AI apps
- Extend the existing acceptable use policy, end-user computing, model-risk framework rather than writing a parallel one; 
- Enforcement mechanics:
  -  technical control
  -  attestation
  -  periodic review/audit.

### 6.2 The review cadence

- Quarterly registry review: criticality re-assessment, orphan detection, stale-app deprecation.

### 6.3 Incident response

- Citizen-built apps in the IR plan; kill-switch authority and process; blameless postmortems feeding gate-checklist updates.

### 6.4 Offboarding & ownership transfer

- Builder departure playbook; succession as a standing gate criterion, not an afterthought.

### 6.5 Program evolution

- Feeding lessons into the maturity assessment; annual re-score against the 12 dimensions; policy version control.

- -  

### 6.6 Risk tiers

- Tier axes from Ch 3: builder capability × artifact criticality × data sensitivity.
- Tier 0 personal experiment / Tier 1 shared tool / Tier 2 department workflow / Tier 3 business-critical — requirements escalate per the concerns catalog.
- Criticality re-assessment triggers: user count, dependency by another process, P&L or reporting linkage.

### 6.7 Trust zones (red / yellow / green)

- Zone definitions and the trifecta logic; zone assignment at intake based on data classification and egress needs.
- Zone as an *environment* property, enforced by infrastructure (Ch 7), not by promise.

### 6.8 Promotion gates

- Gate 1 (experiment → sanctioned project): registration, data classification, zone assignment, named owner.
- Gate 2 (sanctioned → production-ready): tests passing, docs, second operator, secrets vaulted, monitoring wired, BC/DR plan proportionate to tier.
- Gate 3 (production → IT-adopted, when warranted): handover package, code review by professional dev, ongoing ownership decision.
- Published checklists per gate; review SLAs so gates aren't a new backlog.

### 6.9 Heightened-review triggers

- Red-zone apps (internal data + external access); anything touching MNPI, investor PII, position data, regulatory- or client-facing output; anything with write access to a system of record. 

## Ch 7. People & enablement

### 7.1 Roles

- Platform team (builds Ch 7), champions per desk/function, reviewer pool, executive sponsor.

### 7.2 Training path

- Tiered curriculum: AI literacy & failure modes → sanctioned-tool training → guardrails & gate process → certification that unlocks tooling.

### 7.3 Support model

- Office hours, internal guild/channel, paired builds with IT for first Tier-2 projects.

### 7.4 IT's role shift

- From builder of everything to platform operator, reviewer, and adoptive parent of promoted apps; what this means for IT hiring and incentives.

## Ch 8. Do's and don'ts: Worked examples & anti-patterns

### 8.1 Worked examples (each annotated: tier, zone, tools, which concerns bit and how the gates caught them)

- Ops reconciliation automation (yellow zone, n8n + warehouse).
- Research data-wrangling app (yellow zone, Claude Code + Streamlit-in-Snowflake).
- Investor-reporting draft automation (red zone — heightened review walkthrough).
- Compliance surveillance helper (yellow zone, heightened review for data sensitivity).
- Market-data monitor (green zone, public data only).

### 8.2 Anti-patterns (the red lines, with reasoning)

- Anything in the order/execution path; official NAV or books-and-records without IT adoption; client-facing output without compliance review; personal AI accounts on firm data; the scraper that had a SQL alternative; the un-gated agent with warehouse credentials and internet access.

## Ch 9. Appendices

- **A. The crosswalk table** — every concern → maturity dimension → wiki control category → gate where checked. The traceability spine in one table.
- **B. Gate checklists** — printable, per tier.
- **C. Policy templates** — user contract, sanctioned-tool list, tiering rubric, intake form, heightened-review form.
- **D. Tool shortlist** — dated, with certifications/deployment-mode table, linking to wiki vendor pages.
- **E. Selected bibliography** — most important sources used
- **E. Glossary & FAQ** — including answers to typical user issues and objections "why can't I just use my personal ChatGPT," "why does my app need tests if it works."

### 











| #    | Gap                                                          | Recommendation                                               | Sources                                                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C1   | **Memory poisoning & memory lifecycle**                      | Treat agent memory as a governed asset distinct from RAG hygiene: TTL/expiry, validation-before-write, per-user/session scoping, provenance, curation; memory-write as a promotion-gated capability. | OWASP T&M T1; OWASP Top10 ASI06; Microsoft taxonomy (40%→80% attack-success case study) |
| C2   | **Cross-session / delayed-detonation attacks (sleepers, drift)** | Name the temporality problem: a payload injected in one session detonates weeks later; session-scoped logs never show it. Requires cross-session memory audits + longitudinal behavioral-drift monitoring. | Layered survey (T3/T4); Microsoft (flow manipulation)        |
| C3   | **Goal/plan hijack (intent manipulation)**                   | Distinct from prompt injection: individually benign actions composing a hostile plan. Control: pre-execution plan validation (rule-based or LLM-judge; dry runs for high-risk actions). | OWASP T&M T6; Top10 ASI01; layered survey L2                 |
| C4   | **Agent impersonation & spoofing**                           | Mutual authentication between agents and verification that "the compliance agent" is genuine; a spoofed internal agent is a high-quality internal phishing platform. | OWASP T&M T9; Microsoft; Top10 ASI03                         |
| C5   | **Inter-agent propagation: worms, collusion, cascading failures** | Once citizen agents call each other: signed messages, control-vs-data channel separation, circuit breakers between agents, contact policies. Current list is single-agent-centric. | OWASP T&M T12–T14; Top10 ASI07/08; open-challenges (infectious jailbreaks, secret collusion) |
| C6   | **Human manipulation by the agent**                          | The reverse channel: an injected agent socially engineering its own approver ("routine, please approve"); sycophancy-driven over-trust; disclosure when colleagues interact with an agent. | OWASP T&M T15; Top10 ASI09; Microsoft                        |
| C7   | **Approval fatigue / HITL overwhelm**                        | Rubber-stamping is a *measured* failure mode: cap flag rates, meaningful diff presentation, minimum review times, measure approval review rates; prefer policy-engine decisions where possible. | OWASP T&M T10; OpenAI Practices §4.2; design-patterns; CaMeL |
| C8   | **Fleet-level correlated failure / monoculture**             | Dozens of agents on one model/gateway fail simultaneously (bad model update, provider outage, shared jailbreak), overwhelming human fallback sized for single failures. Mitigation: manual-redundancy planning (humans can still run the critical process), diversity where cheap. | OpenAI Practices §5.4; WEF AI Agents in Action; open-challenges |
| C9   | **Self-modification**                                        | Explicit rule: agents must not write to the repos, configs, prompts, or IAM that define them. Citizen setups where builder and agent share a workspace make this the default hazard. | OWASP securing guide §6.2.3; MATRA IS7                       |
| C10  | **Resource overload / availability attacks**                 | Beyond cost: an agent (steered or hallucinating) exhausts DB connections or hammers internal APIs. Statement timeouts, query-cost validation, connection caps, per-agent rate limits at the gateway. | OWASP T&M T4; MATRA IS5 (cartesian-join takedown)            |
| C11  | **Cross-user context leakage in shared agents**              | One builder's agent serving many users: session memory and context scoped per user/entitlement or user A's MNPI bleeds into user B's answers. Distinct from document entitlements. | Microsoft; OWASP securing guide KC4.5/4.6                    |
| C12  | **Emergent market-conduct risk** (fund-specific)             | Trading-adjacent agents can *learn* spoofing-like or tacitly collusive behavior without instruction → market-abuse exposure. Market-conduct surveillance of agent behavior; CCAR-style behavioral stress testing. Expands the existing one-line "emergent market manipulation" bullet. | "Agentic Regulator" (2512.11933)                             |
| C13  | **AI-enabled fraud against the firm**                        | Deepfake voice / synthetic identity attacks on the very approval workflows citizen agents widen (agents that send email or trigger payments). | FS Research Roundup; WEF ($240k deepfake CEO-voice case)     |
| C14  | **Model supply chain (backdoored checkpoints)**              | Package/MCP allowlists don't cover models: fine-tuned or third-party checkpoints can carry dormant triggers that survive safety fine-tuning. Restrict citizen devs to an allowlist of approved model endpoints with provenance verification. | Layered survey (sleeper agents); Top10 ASI04; securing guide §6.2.1 |
| C15  | **Goal/value misalignment as a risk class**                  | The agent that "succeeds" at the metric while damaging the intent (task-proxy optimization). Context layers encoding priorities and binding constraints. | Trustworthy AI Agents; FS Roundup                            |



### B2. Foundations & reference architecture (Ch 4 + Ch 7)

| #    | Gap                                                          | Recommendation                                               | Sources                                                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| F1   | **Instance-level agent identity + agent cards + lineage**    | Beyond NHI credentials: unique ID per running instance stamped on every output/API call, tied to a registry entry; machine-readable agent card (owner, permissions, tools, eval results, incident history) that internal services can condition access on; lineage links for copied/forked/fine-tuned agents. Citizen proliferation is exactly the lineage problem. | IDs-for-AI-systems; Visibility (Chan); OpenAI Practices §4.6; WEF Table 2 |
| F2   | **JIT/ephemeral credentials + OAuth on-behalf-of**           | Short-lived scoped tokens minted per task; agents act with the invoking user's identity/entitlements (OBO) instead of standing over-privileged service accounts. Also the cleanest fix for F1/C11; abandoned agents expire by default. | OWASP securing guide §3.2.8/§4.1.1; Databricks; zero-trust framework; SAGA |
| F3   | **Kill switch ≠ revocation**                                 | Terminating a process leaves cached tokens and live sessions valid. Need a unified session layer with cross-system revocation propagation; graceful shutdown procedures incl. recursive termination of spawned sub-agents and unwinding partial workflows. | zero-trust framework; OpenAI Practices §4.7                  |
| F4   | **Rollback/undo + reversibility classification**             | Classify each agent action reversible vs irreversible; pre-approval only for irreversible actions (after-the-fact ledger review for the rest); build undo paths (saved-state reversal, transaction voiding). | Infrastructure (Chan) §5.2; Practices §4.2/4.4               |
| F5   | **Tamper-evident logs + decision-chain audit trails**        | Append-only / hash-chained / signed logs (a compromised agent can't erase evidence); a never-log list (agents leak secrets/PII into their own logs); record what was considered, rejected, what triggered each action, and who authorized it — "the AI did it" fails a regulator. Caveat: CoT traces can be unfaithful — don't audit on agent-stated reasoning alone. | securing-mcp; OWASP securing guide; Trustworthy AI Agents; layered survey |
| F6   | **RAG/vector-store ingestion integrity**                     | Signed ingestion pipeline (checksums, malware scanning), document-level RBAC in the vector store itself, lineage. Data-source entitlements alone don't cover the retrieval layer citizen agents actually query. | AITEC Securing AI Workflows; securing-ai                     |
| F7   | **Runtime path-level policy enforcement**                    | Policies evaluated over the agent's action *history* (read-MNPI-file then send-external-email are individually benign), with shared cross-agent governance state (information barriers across the fleet). Per-request gateway/RBAC/OPA point checks structurally miss sequences. | runtime-governance ("policies on paths"); AgentGuardian      |
| F8   | **AI-based oversight layer (agents-watching-agents)**        | Active supervisory loop, not just SIEM ingestion: a trusted monitor reviews actions/reasoning at machine speed, pauses flagged actions, escalates only exceptions to the named owner ("monitor-triaged approvals") — the only way "active oversight duty" scales. Caveat: the monitor itself is injectable. | Practices §4.5; evaluating-control-measures; Infrastructure §4.2; Economist (Takeda control plane) |
| F9   | **Eval infrastructure as a platform service**                | Regression evals re-run on every upstream model change; model version pinning; canary traffic + rollback for model/agent updates; LLM-judge scoring of production traffic with quality-drift detection and expert feedback loops. Silent vendor model updates are a regression source the gates don't catch. | Databricks; AITEC (all three); Copilot Studio ALM            |
| F10  | **Behavioral anomaly detection tuned to agents**             | Per-agent/per-role baselines of tool-call patterns against *declared scope* (scope-creep detection); semantics-aware rules (config read vs `~/.aws/credentials` read); trust metrics per agent (task success, error awareness, consistency). SIEM content assumes deterministic services. | securing-mcp; zero-trust; Agentic Regulator; AgentGuardian   |
| F11  | **Sandboxing baseline with per-action credential provisioning** | Separate filesystem; production reachable only through dedicated tools; long-lived credentials never stored on the agent runtime — provisioned per approved action. Only 9/30 commercial agents even document sandboxing, so it must be a program-side requirement. | evaluating-control-measures; AI Agent Index; securing-mcp (mandatory containerization) |

### B3. Tooling & selection matrix (Ch 5/6 tooling chapter)

| #    | Gap                                                          | Recommendation                                               | Sources                                                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| T1   | **MCP client/host security posture as a selection criterion** | Identical tool-poisoning attacks: 0% success on Claude Desktop, 100% on Cursor. Score clients on tool-description validation, parameter visibility, sandboxing, injection warnings. The desktop/IDE agent client is a security decision, not a preference. | mcp-threat-modeling                                          |
| T2   | **Vendor safety-transparency checklist**                     | Require: agent system card, documented sandboxing, documented stop/pause controls, guardrail *defaults* (not user-delegated), incident-disclosure history, clarity on the model→platform→builder→deployer accountability split. 9/30 deployed agents document no guardrails; 4/30 lack stop controls. | AI Agent Index                                               |
| T3   | **Contract terms as ongoing governance**                     | Beyond point-in-time DD: training-on-your-data and zero-day-retention clauses (sample language exists in AITEC deck), model-update notification with pre-enablement simulation/testing rights, contractual audit rights, subvendor "daisy chain" visibility, loyalty/conflict-of-interest terms (does the platform use your prompts for its own purposes?). | LIMRA ("governance by contract"); AITEC tactical; Citi GPS; Kolt (loyalty) |
| T4   | **Vendor churn & viability management**                      | Vendors rapidly evolve/churn: prefer short contracts with opt-outs, POC on your own data before believing accuracy claims, hedge with 2–3 platform partners, inventory vendor-*embedded* AI arriving silently inside already-licensed SaaS. | AITEC tactical; securing-ai; FS Roundup                      |
| T5   | **Sovereignty / data residency**                             | Hosting location, data residency, and provider country-of-origin as explicit matrix columns (77% of firms weigh it). | Deloitte; McKinsey                                           |
| T6   | **Secure design-pattern catalog mapped to tiers**            | The trifecta says what's forbidden; supply the approved architectures: action-selector, plan-then-execute, LLM map-reduce, dual/quarantined LLM (CaMeL), code-then-execute, context-minimization. Map risk tiers to permitted patterns ("tier-2 agents touching untrusted data must use plan-then-execute or quarantined-LLM parsing"). Blueprints, not just prohibitions. | design-patterns paper; CaMeL; OWASP securing guide           |
| T7   | **Tool design rules**                                        | Ban generic-capability tools (`execute_sql`, raw shell) in favor of parameterized, purpose-built, least-privilege tools; strict structured output / constrained decoding on any LLM output crossing a trust boundary (injections rarely survive strict formatting). Cheap and checkable at gate review. | design-patterns; CaMeL; securing-mcp                         |
| T8   | **Data-flow integrity / tool-call-level policy hooks**       | Even with a fixed plan, injected data can redirect tool *arguments* (recipient, filename). Selection criterion: does the platform support provenance/capability tagging and a deterministic policy check before each tool call? | CaMeL                                                        |

### B4. Governance, gates & user contract (Ch 6)

| #    | Gap                                                          | Recommendation                                               | Sources                                                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| G1   | **Autonomy as an explicit tier axis + progressive, earned expansion** | Tier by autonomy/authority as well as builder×criticality×sensitivity; deploy copilot-mode first, graduate to autopilot per workflow only against a documented clean-session track record with written expansion criteria (Anthropic pattern: ~20% auto-approval → 40%+ after ~750 clean sessions); **scope-escalation triggers** — pre-agreed criteria forcing full re-review when an agent's authority widens ("autonomy drift"); adaptive downgrade — automatically reduce permissions/autonomy on anomaly detection (midpoint between "running" and "kill"). | Trustworthy AI Agents; MIT SMR; PwC; WEF; Copilot Studio maturity |
| G2   | **Action-tier classification + plan-level approval**         | Green/yellow/red *action* classes enforced outside the agent's own judgment; Plan Mode — approve the intended plan up front rather than per-action clicks (resolves oversight-vs-throughput); the 60-second override test. Refines the existing HITL item. | Trustworthy AI Agents (Anthropic five principles)            |
| G3   | **Adversarial testing at the gates**                         | proportionate to tier: injection fuzzing, memory-poisoning probes, privilege-escalation scenarios (tools exist: AgentDojo, Agent Security Bench, AgentPoison); recurring red-team exercises against high-tier agents; and **control evaluations** — red-teaming the *control stack itself* (can a hijacked agent subvert the monitors?) with results documented as safety cases. Current evals are functional only. | OWASP securing guide §7; Microsoft; evaluating-control-measures (UK AISI); securing-ai; Copilot Studio |
| G4   | **Per-app lightweight threat modeling**                      | Scaled-down DFD + asset×CIA impact + attack-vector walkthrough at the promotion gate (MATRA method, directly reusable); operationalizes the tiering. | MATRA; OWASP securing guide §2.2                             |
| G5   | **Trace-learned behavioral allowlists as a promotion artifact** | Record staging-phase traces, compile into an enforced allowlist of tool sequences + generalized input constraints — a cheap auditable "this is all it may do" contract that doubles as a hallucination/malfunction trap. | AgentGuardian                                                |
| G6   | **MCP-specific vetting**                                     | Tool-metadata version pinning + hashing/diffing with re-vet on change (rug-pulls); static scanning of tool descriptions at registration; OAuth posture checklist for remote servers (mandatory S256 PKCE, restricted redirect_uri, opaque delegated state — 40% of remote MCP servers have *no* auth; 100% of tested OAuth ones were flawed); MCP `sampling` disabled or gated by default (server-injected prompts indistinguishable from user input); cap servers per agent / gate cross-server data flow (78% attack success at 5 servers). | mcp-threat-modeling; mcp-remote-auth; breaking-the-protocol; securing-mcp |
| G7   | **Sub-agent spawning policy in the user contract**           | Agency law's default: an agent may appoint sub-agents only with principal consent. State it explicitly; logs must link sub-agent chains to the originating owner; delegation credentials for "agent acting for agent acting for user". | Kolt; Visibility (Chan); AAGMM; zero-trust                   |
| G8   | **Safe behavioral defaults + duty to clarify**               | Codify for all citizen agents: least-disruptive action, conservative spend/scope defaults, stop-and-ask when instructions are ambiguous rather than exercising discretion; periodic re-authorization / time-boxing so standing authority lapses without review. | Practices §4.2/4.3; Kolt                                     |
| G9   | **Liability/autonomy mapping for contracts & insurance**     | Map where control actually sits at each workflow step (human-directed / supervised / autonomous); align vendor indemnities, warranties, and E&O/cyber coverage to who controls each decision point — before a loss forces the question. | Above the Law autonomy-mapping; Kolt                         |
| G10  | **Inter-agent contact policies**                             | Owner-defined who-may-contact-whom, enforced with expiring, request-quota'd credentials bounding a compromised agent's window. Identity/authz items are currently all agent-to-resource, not agent-to-agent. | SAGA; zero-trust                                             |

### B5. Rollout & operating (Ch 9 + Ch 10)

| #    | Gap                                                | Recommendation                                               | Sources                                                      |
| ---- | -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| O1   | **Automated sprawl detection**                     | Scanning for shadow/orphaned/duplicative agents, permission drift, unmonitored delegation chains; periodic owner recertification. AAGMM simulations: the single highest-leverage control (~74% sprawl reduction); registry-only capture is insufficient — also actively discover undeclared usage and AI features appearing inside approved SaaS. | AAGMM; securing-ai (shadow AI); "Running Loose"; Databricks  |
| O2   | **Reactive governance ≈ zero benefit**             | AAGMM's simulation result: incident-triggered-only governance provides near-zero security benefit in adversarial scenarios — argument for gating launch on Level-3 controls (registry + IAM + policy + HITL + risk classes), not incident response alone. Use in Ch 9 sequencing. | AAGMM                                                        |
| O3   | **Support tiers, SLAs, ITSM integration**          | Who fixes a broken departmental agent, on what SLA, through which ticket queue; agent support tiers (personal / departmental / mission-critical), uptime/error monitoring for critical agents, standardized runbooks per class, agent problems in the existing ITSM. | Copilot Studio maturity model                                |
| O4   | **Program KRIs + governance-effectiveness review** | Quantitative indicators: injection attempts blocked, DLP hits per agent, anomalous tool-call rate per user/role, sandbox/containerization coverage, sprawl index, incidents per 1,000 agent actions, approval review rates (C7). Biannual review of whether governance itself works; outcome metrics formally feeding policy updates. Governance must not thin out after go-live (58% review pre-deploy, 12% only on failure). | securing-mcp; AAGMM; Economist; LIMRA; McKinsey RAI          |
| O5   | **Regulatory watch process**                       | Quarterly regulatory monitoring updating internal policy; EU AI Act (applies Aug 2026 — logging, human oversight, documented risk management; penalties to 7% of global revenue) if any EU management company or marketing; restrictions on solely-automated decisions affecting clients; regulator-grade explainability ("know your AI") beyond telemetry; named accountability *to the regulator* with override mechanisms. | LIMRA; Trustworthy AI Agents; Citi GPS; Economist FS profile |
| O6   | **Platform compliance traps**                      | Concrete defaults to codify: Copilot Studio 30-day conversation-transcript retention (extend/export for books-and-records), cross-geography data-movement toggles, sharing rules with viewer caps, Entra-group (not individual) licensing, naming conventions. | Copilot Studio guidance                                      |
| O7   | **Incident/near-miss learning loop**               | Low-friction reporting channels for users *and counterparties of the agent*; near-miss capture; documented loop feeding lessons into gates, allowlists, and training; ethics hotline / sensitive-use triage path for gray-area cases. | Infrastructure (Chan) §5.1; WEF; Copilot Studio              |
| O8   | **Agent self-identification to third parties**     | Citizen agents hitting vendor/counterparty sites declare themselves (published user-agent/IP ranges; signed requests per RFC 9421 where supported), respect robots.txt/ToS — undeclared agent traffic is a live legal/reputational risk (Cloudflare/Amazon disputes). | AI Agent Index                                               |
| O9   | **Agent "performance reviews" (HR-for-agents)**    | Lifecycle function mirroring HR: onboarding/validation, periodic reviews (accuracy, drift, bias), retraining, retirement; agents as simultaneously appreciating assets (learning) and depreciating tools (drift). |                                                              |

Documentation

Program-level (the firm publishes, IT/platform team owns):
- The user contract / AI Safe Use Policy — the single document every builder signs: what the firm provides, what the builder must do, the red/yellow/green action rules, principal-agent accountability ("you own what your agent does"), active-oversight duty, sub-agent and spawning rules. LIMRA notes regulators now expect a named AI use policy, reviewed annually.
- The tiering rubric and gate checklists — printable, per tier, so a builder can self-assess before intake. If builders can't predict what Gate 2 requires, the gate becomes a backlog and they route around it.
- The sanctioned-tool list with decision guidance — not just "what's allowed" but which tool for which job and which zone (your Ch 5 selection matrix, condensed to one page).
- The data-access map / API catalog — the single highest-leverage doc per your own spec: "use the SQL mart, not a scraper" only works if the mart is discoverable, with schemas, owners, and how to request access.
- Golden-path templates and pattern docs — repo templates, devcontainers, CLAUDE.md standards, the primitives library docs, and the secure design-pattern catalog (plan-then-execute, quarantined-LLM, etc.) mapped to tiers — blueprints, not just prohibitions.
- Worked examples and anti-patterns (your Ch 11) — the corpus is unanimous that people copy examples, not policies.
- FAQ — including the honest answers: "why can't I use my personal ChatGPT," "why does my app need tests if it works."

Artifact-level (the builder produces; enforced at gates, proportionate to tier):
- README + runbook ("could someone else operate this tomorrow?"), named owner and second operator, data lineage, registry entry (tier, zone, classification, dependencies), and for higher tiers: eval results, threat-model sketch, BCP note. Templates for all of these, so writing them is a fill-in exercise, not authorship.

Training

The load-bearing principle from your spec, endorsed everywhere in the corpus: training tier unlocks tool tier — certification before empowerment.

- Level 0 — firm-wide AI literacy (everyone, ~1 hour): what the tools can/can't do, hallucination, prompt injection in plain terms, the personal-AI-accounts rule, how to report concerns. Deloitte's data says role-specific, hands-on beats generic e-learning by a wide margin.
- Level 1 — builder certification (prerequisite for any sanctioned tool): the user contract, tiers/zones/trifecta logic, the gate process, secrets hygiene, "criticality is a property of usage." Short, testable, renewed annually.
- Level 2 — tool-specific training per sanctioned platform (Claude Code with firm hooks, n8n, Streamlit-in-Snowflake…): the golden path for
- Level 2 — tool-specific training per sanctioned platform (Claude Code with firm hooks, n8n, Streamlit-in-Snowflake…): the golden path for that tool, its guardrails, what it deliberately doesn't solve.
- Level 3 — advanced/agentic (top of the builder spectrum): evals for stochastic components, agent failure modes (memory poisoning, approval fatigue, goal drift), when to escalate to professional dev.
- Reviewer/approver training — the gap most programs miss (per the approval-fatigue literature): the people staffing gates and HITL approvals need training on what a meaningful review looks like, or oversight degrades to rubber-stamping.
- Ongoing: microlearning on incidents and near-misses (blameless postmortems as teaching material), refreshers when policy or tools change. LIMRA recommends KPIs for the skilling program itself (certification rates, time-to-first-build, gate-failure reasons trending down).

Support

- A visible front door: one channel (Slack/Teams) for questions, one intake form for gate submissions. If getting help requires knowing whom to ask, only the well-connected build safely.
- Office hours — weekly, platform team staffed; the cheapest way to catch bad architecture before it's load-bearing.
- Champions network — per desk/function, trained one level above their peers; Deloitte and AITEC both find peer champions move adoption more than any mandate. Give them real perks (early tool access, recognition) — it's a role, not a title.
- Paired builds — platform engineer pairs with the builder on their first Tier-2/yellow-zone project; the pairing is the training and the review.
- Production support model — the Copilot Studio maturity model's point, and a gap in most programs: once an agent is promoted, who fixes it at 7am? Define support tiers (personal = builder-supported, departmental = builder + platform SLA, mission-critical = IT-adopted), route agent incidents through the existing ITSM queue, and require a runbook + second operator as the price of promotion.
- Community infrastructure — an internal showcase/gallery of registered apps (drives reuse-before-build), a shared prompt/pattern library with a contribution path, and celebrated wins (town halls, demo days). The Economist report's KONE case scaled to 4,000 citizen developers largely on this social layer with only a thin hard-limit rulebook at the bottom tier.

One framing worth putting in the primer: documentation, training, and support are the third leg of enforcement. Your spec lists technical controls and attestation as enforcement mechanics — but most non-compliance in the corpus is ignorance plus friction, not malice. Every gate checklist item should trace to a template that makes it easy, a training module that explains it, and a support channel that unblocks it; anything that fails that trace is a rule people will break.

This maps onto the spec as Ch 8 (expanded per gap A3 — adoption, sentiment, reviewer training) plus Appendices B/C/E. Want me to fold it into the design spec as a revised Ch 8, or file it as a standalone section draft alongside the gap analysis?

### 3.5 The maturity lens: all 12 dimensions applied to citizen development
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

- 

- 
