# Citizen-Dev Primer — Gap Analysis & Recommendations

**Date:** 2026-07-17
**Status:** Recommendations to fold into the primer outline
**Baseline:** `2026-07-15-citizen-dev-primer-design.md` (Ch 1–12 outline)
**Inputs:** 47 PDFs + 1 text file in `./agents/`, reviewed against the outline by six
themed review passes (governance frameworks; OWASP/threat taxonomies; MCP & prompt
injection; runtime control & identity; consulting playbooks; finance/platform docs).

**Verdict:** the five-part skeleton (concerns → foundations → tooling → implementation
→ operating) is sound and the security basics are well covered. The corpus surfaces
**four structural gaps** (no home in any current chapter) and a set of concrete gaps
inside each existing chapter.

---

## A. Structural gaps — new chapters or major new sections

### A1. Value & portfolio management (new chapter or major section in Ch 9/10)
*Sources: McKinsey "Seizing the agentic AI advantage"; Economist/Databricks "Making AI
Deliver 2026"; AWS CAF for AI; MIT SMR/BCG "Emerging Agentic Enterprise".*

Activity ≠ impact — boards mistake pilot counts for progress when no measurement
mechanism exists. Missing:

- **Use-case intake & prioritization pipeline** — which citizen ideas get built at all;
  prioritize where data is good and users are willing to change process; milestone-based
  funding.
- **Per-agent business-impact tracking after the pilot** — mandated, owned by the
  governance council; counterfactual measurement (centaur pair vs human-alone).
- **Disciplined attrition** — periodic portfolio reviews that *kill* stalled, redundant,
  or unscalable agents. The outline has promotion gates going up but no retirement flow
  going down. Formally "close the experimentation phase" for each cohort.
- **Reuse-before-build** — norms and review so one team's agent is reused, not rebuilt;
  the registry enables it but a reuse mandate is a process, not a tool.
- **Investment governance** — recurring cross-functional investment review; a financial
  hurdle before anything scales; recurring run costs estimated up front (for GenAI they
  can exceed build costs); budget for permanent uncertainty rather than fixed-horizon NPV.

### A2. Governance bodies & independent challenge (extend Ch 6 + Ch 8)
*Sources: WEF "Empowering AI Leadership" (Fig 16–17); McKinsey Responsible AI 2026;
LIMRA CEO guide; Copilot Studio maturity model; Deloitte State of AI 2026.*

Current roles are all technology-side. Add:

- **Chartered cross-functional AI council** with legal, compliance, and HR at the table;
  decision rights, escalation paths, meeting cadence; compliance embedded in the
  governance loop, not just as a gate reviewer.
- **One explicitly accountable responsible-AI owner** with a budget (orgs with one score
  2.6/4 vs 1.8 maturity without).
- **Board/ExCo reporting cadence** — KPI-based upward reporting (incidents, reliability,
  value, trust signals).
- **Three Lines of Defence / SR 11-7-style independent validation** — WEF explicitly
  places citizen developers in the first line and requires second-line independent
  review-and-challenge with a validation memo and sign-off, plus third-line internal
  audit. Promotion gates ≠ independent validation; LLM outputs feeding investment
  decisions engage existing model-risk-management expectations.
- **AI Safe Use Policy** as a regulator-expected named artifact, reviewed annually.

### A3. Workforce, adoption & trust (extend Ch 8 well beyond training)
*Sources: Deloitte State of AI 2026; MIT SMR/BCG; Economist/Databricks; LIMRA;
Microsoft failure-mode taxonomy.*

- **Job/task redesign** — map roles into tasks, assign each to human / agent /
  collaboration; publish which tasks must remain human-led; "job crafting" (involve the
  people whose work is automated in redesigning their role — documented to sharply raise
  adoption); junior–senior pairing against skill atrophy.
- **Incentives & career architecture** — performance incentives for effective AI
  leverage; promotion criteria rewritten around orchestration, exception handling, and
  oversight; dual career paths; the entry-level pipeline question.
- **Adoption & trust program** — measure the access-to-activation gap and worker
  sentiment segments (enthusiasts / fence-sitters / sceptics — the largest group needs
  proof, not policy); psychological safety to challenge agent output (prize the
  sceptics); leaders visibly using AI; scripted answers to job-security fears; office
  hours, showcases, celebrated wins. Shadow AI is a symptom of governance that hasn't
  earned trust.
- **Organizational deskilling / knowledge loss** (Microsoft taxonomy: a novel *safety*
  harm) — as agents absorb processes, humans lose the ability to perform or validate
  them, undermining the "active oversight" the user contract depends on. One paragraph
  in Ch 10 ops + a mitigation (manual redundancy drills, see C8).
- **External capacity** — peer benchmarking groups; fractional external experts (outside
  counsel for AI regulation) rather than staffing everything internally.

### A4. External framework crosswalk (new appendix)
*Sources: NIST COSAIS concept paper; securing-ai (Booz Allen) framework appendix;
securing-mcp; AAGMM; WEF.*

Map the program's controls to NIST AI RMF, NIST SP 800-53 COSAIS overlays (in
progress), ISO 27001/42001, OWASP Agentic Top 10 / LLM Top 10, MITRE ATLAS, Gartner AI
TRiSM. Auditors, allocator DDQs, and regulators assess in these vocabularies; the
crosswalk is cheap and makes the document defensible. Fits naturally as an extra column
in Appendix A.

---

## B. Chapter-by-chapter gaps

### B1. Concerns (Ch 3) — missing agentic threat classes

| # | Gap | Recommendation | Sources |
|---|-----|----------------|---------|
| C1 | **Memory poisoning & memory lifecycle** | Treat agent memory as a governed asset distinct from RAG hygiene: TTL/expiry, validation-before-write, per-user/session scoping, provenance, curation; memory-write as a promotion-gated capability. | OWASP T&M T1; OWASP Top10 ASI06; Microsoft taxonomy (40%→80% attack-success case study) |
| C2 | **Cross-session / delayed-detonation attacks (sleepers, drift)** | Name the temporality problem: a payload injected in one session detonates weeks later; session-scoped logs never show it. Requires cross-session memory audits + longitudinal behavioral-drift monitoring. | Layered survey (T3/T4); Microsoft (flow manipulation) |
| C3 | **Goal/plan hijack (intent manipulation)** | Distinct from prompt injection: individually benign actions composing a hostile plan. Control: pre-execution plan validation (rule-based or LLM-judge; dry runs for high-risk actions). | OWASP T&M T6; Top10 ASI01; layered survey L2 |
| C4 | **Agent impersonation & spoofing** | Mutual authentication between agents and verification that "the compliance agent" is genuine; a spoofed internal agent is a high-quality internal phishing platform. | OWASP T&M T9; Microsoft; Top10 ASI03 |
| C5 | **Inter-agent propagation: worms, collusion, cascading failures** | Once citizen agents call each other: signed messages, control-vs-data channel separation, circuit breakers between agents, contact policies. Current list is single-agent-centric. | OWASP T&M T12–T14; Top10 ASI07/08; open-challenges (infectious jailbreaks, secret collusion) |
| C6 | **Human manipulation by the agent** | The reverse channel: an injected agent socially engineering its own approver ("routine, please approve"); sycophancy-driven over-trust; disclosure when colleagues interact with an agent. | OWASP T&M T15; Top10 ASI09; Microsoft |
| C7 | **Approval fatigue / HITL overwhelm** | Rubber-stamping is a *measured* failure mode: cap flag rates, meaningful diff presentation, minimum review times, measure approval review rates; prefer policy-engine decisions where possible. | OWASP T&M T10; OpenAI Practices §4.2; design-patterns; CaMeL |
| C8 | **Fleet-level correlated failure / monoculture** | Dozens of agents on one model/gateway fail simultaneously (bad model update, provider outage, shared jailbreak), overwhelming human fallback sized for single failures. Mitigation: manual-redundancy planning (humans can still run the critical process), diversity where cheap. | OpenAI Practices §5.4; WEF AI Agents in Action; open-challenges |
| C9 | **Self-modification** | Explicit rule: agents must not write to the repos, configs, prompts, or IAM that define them. Citizen setups where builder and agent share a workspace make this the default hazard. | OWASP securing guide §6.2.3; MATRA IS7 |
| C10 | **Resource overload / availability attacks** | Beyond cost: an agent (steered or hallucinating) exhausts DB connections or hammers internal APIs. Statement timeouts, query-cost validation, connection caps, per-agent rate limits at the gateway. | OWASP T&M T4; MATRA IS5 (cartesian-join takedown) |
| C11 | **Cross-user context leakage in shared agents** | One builder's agent serving many users: session memory and context scoped per user/entitlement or user A's MNPI bleeds into user B's answers. Distinct from document entitlements. | Microsoft; OWASP securing guide KC4.5/4.6 |
| C12 | **Emergent market-conduct risk** (fund-specific) | Trading-adjacent agents can *learn* spoofing-like or tacitly collusive behavior without instruction → market-abuse exposure. Market-conduct surveillance of agent behavior; CCAR-style behavioral stress testing. Expands the existing one-line "emergent market manipulation" bullet. | "Agentic Regulator" (2512.11933) |
| C13 | **AI-enabled fraud against the firm** | Deepfake voice / synthetic identity attacks on the very approval workflows citizen agents widen (agents that send email or trigger payments). | FS Research Roundup; WEF ($240k deepfake CEO-voice case) |
| C14 | **Model supply chain (backdoored checkpoints)** | Package/MCP allowlists don't cover models: fine-tuned or third-party checkpoints can carry dormant triggers that survive safety fine-tuning. Restrict citizen devs to an allowlist of approved model endpoints with provenance verification. | Layered survey (sleeper agents); Top10 ASI04; securing guide §6.2.1 |
| C15 | **Goal/value misalignment as a risk class** | The agent that "succeeds" at the metric while damaging the intent (task-proxy optimization). Context layers encoding priorities and binding constraints. | Trustworthy AI Agents; FS Roundup |

**Framing to adopt in Ch 3 (reinforces the trifecta chapter):**
- *Architectural controls dominate input-level defenses* — prompt injection cannot be
  eliminated, only bounded by what the agent **can do** (MATRA, empirical).
- *Defenses don't transfer across layers* — model, planning, memory, tools,
  coordination, ecosystem, governance each need their own control; attackers route
  through the uncovered layer (layered survey).
- *Assess accidental/hallucination threat sources as rigorously as adversaries* (MATRA).

### B2. Foundations & reference architecture (Ch 4 + Ch 7)

| # | Gap | Recommendation | Sources |
|---|-----|----------------|---------|
| F1 | **Instance-level agent identity + agent cards + lineage** | Beyond NHI credentials: unique ID per running instance stamped on every output/API call, tied to a registry entry; machine-readable agent card (owner, permissions, tools, eval results, incident history) that internal services can condition access on; lineage links for copied/forked/fine-tuned agents. Citizen proliferation is exactly the lineage problem. | IDs-for-AI-systems; Visibility (Chan); OpenAI Practices §4.6; WEF Table 2 |
| F2 | **JIT/ephemeral credentials + OAuth on-behalf-of** | Short-lived scoped tokens minted per task; agents act with the invoking user's identity/entitlements (OBO) instead of standing over-privileged service accounts. Also the cleanest fix for F1/C11; abandoned agents expire by default. | OWASP securing guide §3.2.8/§4.1.1; Databricks; zero-trust framework; SAGA |
| F3 | **Kill switch ≠ revocation** | Terminating a process leaves cached tokens and live sessions valid. Need a unified session layer with cross-system revocation propagation; graceful shutdown procedures incl. recursive termination of spawned sub-agents and unwinding partial workflows. | zero-trust framework; OpenAI Practices §4.7 |
| F4 | **Rollback/undo + reversibility classification** | Classify each agent action reversible vs irreversible; pre-approval only for irreversible actions (after-the-fact ledger review for the rest); build undo paths (saved-state reversal, transaction voiding). | Infrastructure (Chan) §5.2; Practices §4.2/4.4 |
| F5 | **Tamper-evident logs + decision-chain audit trails** | Append-only / hash-chained / signed logs (a compromised agent can't erase evidence); a never-log list (agents leak secrets/PII into their own logs); record what was considered, rejected, what triggered each action, and who authorized it — "the AI did it" fails a regulator. Caveat: CoT traces can be unfaithful — don't audit on agent-stated reasoning alone. | securing-mcp; OWASP securing guide; Trustworthy AI Agents; layered survey |
| F6 | **RAG/vector-store ingestion integrity** | Signed ingestion pipeline (checksums, malware scanning), document-level RBAC in the vector store itself, lineage. Data-source entitlements alone don't cover the retrieval layer citizen agents actually query. | AITEC Securing AI Workflows; securing-ai |
| F7 | **Runtime path-level policy enforcement** | Policies evaluated over the agent's action *history* (read-MNPI-file then send-external-email are individually benign), with shared cross-agent governance state (information barriers across the fleet). Per-request gateway/RBAC/OPA point checks structurally miss sequences. | runtime-governance ("policies on paths"); AgentGuardian |
| F8 | **AI-based oversight layer (agents-watching-agents)** | Active supervisory loop, not just SIEM ingestion: a trusted monitor reviews actions/reasoning at machine speed, pauses flagged actions, escalates only exceptions to the named owner ("monitor-triaged approvals") — the only way "active oversight duty" scales. Caveat: the monitor itself is injectable. | Practices §4.5; evaluating-control-measures; Infrastructure §4.2; Economist (Takeda control plane) |
| F9 | **Eval infrastructure as a platform service** | Regression evals re-run on every upstream model change; model version pinning; canary traffic + rollback for model/agent updates; LLM-judge scoring of production traffic with quality-drift detection and expert feedback loops. Silent vendor model updates are a regression source the gates don't catch. | Databricks; AITEC (all three); Copilot Studio ALM |
| F10 | **Behavioral anomaly detection tuned to agents** | Per-agent/per-role baselines of tool-call patterns against *declared scope* (scope-creep detection); semantics-aware rules (config read vs `~/.aws/credentials` read); trust metrics per agent (task success, error awareness, consistency). SIEM content assumes deterministic services. | securing-mcp; zero-trust; Agentic Regulator; AgentGuardian |
| F11 | **Sandboxing baseline with per-action credential provisioning** | Separate filesystem; production reachable only through dedicated tools; long-lived credentials never stored on the agent runtime — provisioned per approved action. Only 9/30 commercial agents even document sandboxing, so it must be a program-side requirement. | evaluating-control-measures; AI Agent Index; securing-mcp (mandatory containerization) |

### B3. Tooling & selection matrix (Ch 5/6 tooling chapter)

| # | Gap | Recommendation | Sources |
|---|-----|----------------|---------|
| T1 | **MCP client/host security posture as a selection criterion** | Identical tool-poisoning attacks: 0% success on Claude Desktop, 100% on Cursor. Score clients on tool-description validation, parameter visibility, sandboxing, injection warnings. The desktop/IDE agent client is a security decision, not a preference. | mcp-threat-modeling |
| T2 | **Vendor safety-transparency checklist** | Require: agent system card, documented sandboxing, documented stop/pause controls, guardrail *defaults* (not user-delegated), incident-disclosure history, clarity on the model→platform→builder→deployer accountability split. 9/30 deployed agents document no guardrails; 4/30 lack stop controls. | AI Agent Index |
| T3 | **Contract terms as ongoing governance** | Beyond point-in-time DD: training-on-your-data and zero-day-retention clauses (sample language exists in AITEC deck), model-update notification with pre-enablement simulation/testing rights, contractual audit rights, subvendor "daisy chain" visibility, loyalty/conflict-of-interest terms (does the platform use your prompts for its own purposes?). | LIMRA ("governance by contract"); AITEC tactical; Citi GPS; Kolt (loyalty) |
| T4 | **Vendor churn & viability management** | Vendors rapidly evolve/churn: prefer short contracts with opt-outs, POC on your own data before believing accuracy claims, hedge with 2–3 platform partners, inventory vendor-*embedded* AI arriving silently inside already-licensed SaaS. | AITEC tactical; securing-ai; FS Roundup |
| T5 | **Sovereignty / data residency** | Hosting location, data residency, and provider country-of-origin as explicit matrix columns (77% of firms weigh it). | Deloitte; McKinsey |
| T6 | **Secure design-pattern catalog mapped to tiers** | The trifecta says what's forbidden; supply the approved architectures: action-selector, plan-then-execute, LLM map-reduce, dual/quarantined LLM (CaMeL), code-then-execute, context-minimization. Map risk tiers to permitted patterns ("tier-2 agents touching untrusted data must use plan-then-execute or quarantined-LLM parsing"). Blueprints, not just prohibitions. | design-patterns paper; CaMeL; OWASP securing guide |
| T7 | **Tool design rules** | Ban generic-capability tools (`execute_sql`, raw shell) in favor of parameterized, purpose-built, least-privilege tools; strict structured output / constrained decoding on any LLM output crossing a trust boundary (injections rarely survive strict formatting). Cheap and checkable at gate review. | design-patterns; CaMeL; securing-mcp |
| T8 | **Data-flow integrity / tool-call-level policy hooks** | Even with a fixed plan, injected data can redirect tool *arguments* (recipient, filename). Selection criterion: does the platform support provenance/capability tagging and a deterministic policy check before each tool call? | CaMeL |

### B4. Governance, gates & user contract (Ch 6)

| # | Gap | Recommendation | Sources |
|---|-----|----------------|---------|
| G1 | **Autonomy as an explicit tier axis + progressive, earned expansion** | Tier by autonomy/authority as well as builder×criticality×sensitivity; deploy copilot-mode first, graduate to autopilot per workflow only against a documented clean-session track record with written expansion criteria (Anthropic pattern: ~20% auto-approval → 40%+ after ~750 clean sessions); **scope-escalation triggers** — pre-agreed criteria forcing full re-review when an agent's authority widens ("autonomy drift"); adaptive downgrade — automatically reduce permissions/autonomy on anomaly detection (midpoint between "running" and "kill"). | Trustworthy AI Agents; MIT SMR; PwC; WEF; Copilot Studio maturity |
| G2 | **Action-tier classification + plan-level approval** | Green/yellow/red *action* classes enforced outside the agent's own judgment; Plan Mode — approve the intended plan up front rather than per-action clicks (resolves oversight-vs-throughput); the 60-second override test. Refines the existing HITL item. | Trustworthy AI Agents (Anthropic five principles) |
| G3 | **Adversarial testing at the gates** | Proportional to tier: injection fuzzing, memory-poisoning probes, privilege-escalation scenarios (tools exist: AgentDojo, Agent Security Bench, AgentPoison); recurring red-team exercises against high-tier agents; and **control evaluations** — red-teaming the *control stack itself* (can a hijacked agent subvert the monitors?) with results documented as safety cases. Current evals are functional only. | OWASP securing guide §7; Microsoft; evaluating-control-measures (UK AISI); securing-ai; Copilot Studio |
| G4 | **Per-app lightweight threat modeling** | Scaled-down DFD + asset×CIA impact + attack-vector walkthrough at the promotion gate (MATRA method, directly reusable); operationalizes the tiering. | MATRA; OWASP securing guide §2.2 |
| G5 | **Trace-learned behavioral allowlists as a promotion artifact** | Record staging-phase traces, compile into an enforced allowlist of tool sequences + generalized input constraints — a cheap auditable "this is all it may do" contract that doubles as a hallucination/malfunction trap. | AgentGuardian |
| G6 | **MCP-specific vetting** | Tool-metadata version pinning + hashing/diffing with re-vet on change (rug-pulls); static scanning of tool descriptions at registration; OAuth posture checklist for remote servers (mandatory S256 PKCE, restricted redirect_uri, opaque delegated state — 40% of remote MCP servers have *no* auth; 100% of tested OAuth ones were flawed); MCP `sampling` disabled or gated by default (server-injected prompts indistinguishable from user input); cap servers per agent / gate cross-server data flow (78% attack success at 5 servers). | mcp-threat-modeling; mcp-remote-auth; breaking-the-protocol; securing-mcp |
| G7 | **Sub-agent spawning policy in the user contract** | Agency law's default: an agent may appoint sub-agents only with principal consent. State it explicitly; logs must link sub-agent chains to the originating owner; delegation credentials for "agent acting for agent acting for user". | Kolt; Visibility (Chan); AAGMM; zero-trust |
| G8 | **Safe behavioral defaults + duty to clarify** | Codify for all citizen agents: least-disruptive action, conservative spend/scope defaults, stop-and-ask when instructions are ambiguous rather than exercising discretion; periodic re-authorization / time-boxing so standing authority lapses without review. | Practices §4.2/4.3; Kolt |
| G9 | **Liability/autonomy mapping for contracts & insurance** | Map where control actually sits at each workflow step (human-directed / supervised / autonomous); align vendor indemnities, warranties, and E&O/cyber coverage to who controls each decision point — before a loss forces the question. | Above the Law autonomy-mapping; Kolt |
| G10 | **Inter-agent contact policies** | Owner-defined who-may-contact-whom, enforced with expiring, request-quota'd credentials bounding a compromised agent's window. Identity/authz items are currently all agent-to-resource, not agent-to-agent. | SAGA; zero-trust |

### B5. Rollout & operating (Ch 9 + Ch 10)

| # | Gap | Recommendation | Sources |
|---|-----|----------------|---------|
| O1 | **Automated sprawl detection** | Scanning for shadow/orphaned/duplicative agents, permission drift, unmonitored delegation chains; periodic owner recertification. AAGMM simulations: the single highest-leverage control (~74% sprawl reduction); registry-only capture is insufficient — also actively discover undeclared usage and AI features appearing inside approved SaaS. | AAGMM; securing-ai (shadow AI); "Running Loose"; Databricks |
| O2 | **Reactive governance ≈ zero benefit** | AAGMM's simulation result: incident-triggered-only governance provides near-zero security benefit in adversarial scenarios — argument for gating launch on Level-3 controls (registry + IAM + policy + HITL + risk classes), not incident response alone. Use in Ch 9 sequencing. | AAGMM |
| O3 | **Support tiers, SLAs, ITSM integration** | Who fixes a broken departmental agent, on what SLA, through which ticket queue; agent support tiers (personal / departmental / mission-critical), uptime/error monitoring for critical agents, standardized runbooks per class, agent problems in the existing ITSM. | Copilot Studio maturity model |
| O4 | **Program KRIs + governance-effectiveness review** | Quantitative indicators: injection attempts blocked, DLP hits per agent, anomalous tool-call rate per user/role, sandbox/containerization coverage, sprawl index, incidents per 1,000 agent actions, approval review rates (C7). Biannual review of whether governance itself works; outcome metrics formally feeding policy updates. Governance must not thin out after go-live (58% review pre-deploy, 12% only on failure). | securing-mcp; AAGMM; Economist; LIMRA; McKinsey RAI |
| O5 | **Regulatory watch process** | Quarterly regulatory monitoring updating internal policy; EU AI Act (applies Aug 2026 — logging, human oversight, documented risk management; penalties to 7% of global revenue) if any EU management company or marketing; restrictions on solely-automated decisions affecting clients; regulator-grade explainability ("know your AI") beyond telemetry; named accountability *to the regulator* with override mechanisms. | LIMRA; Trustworthy AI Agents; Citi GPS; Economist FS profile |
| O6 | **Platform compliance traps** | Concrete defaults to codify: Copilot Studio 30-day conversation-transcript retention (extend/export for books-and-records), cross-geography data-movement toggles, sharing rules with viewer caps, Entra-group (not individual) licensing, naming conventions. | Copilot Studio guidance |
| O7 | **Incident/near-miss learning loop** | Low-friction reporting channels for users *and counterparties of the agent*; near-miss capture; documented loop feeding lessons into gates, allowlists, and training; ethics hotline / sensitive-use triage path for gray-area cases. | Infrastructure (Chan) §5.1; WEF; Copilot Studio |
| O8 | **Agent self-identification to third parties** | Citizen agents hitting vendor/counterparty sites declare themselves (published user-agent/IP ranges; signed requests per RFC 9421 where supported), respect robots.txt/ToS — undeclared agent traffic is a live legal/reputational risk (Cloudflare/Amazon disputes). | AI Agent Index |
| O9 | **Agent "performance reviews" (HR-for-agents)** | Lifecycle function mirroring HR: onboarding/validation, periodic reviews (accuracy, drift, bias), retraining, retirement; agents as simultaneously appreciating assets (learning) and depreciating tools (drift). | MIT SMR/BCG |

---

## C. Priority triage

**Tier 1 — structural, do first (change the outline's shape):**
A1 value/portfolio chapter · A2 governance bodies + independent validation · G1 autonomy
axis + earned expansion · F1 instance identity/agent cards · O1 sprawl detection · A4
framework crosswalk.

**Tier 2 — high-leverage additions inside existing chapters:**
C1/C2 memory + temporality · C5 inter-agent risks · F2 JIT/OBO credentials · F3
revocation ≠ kill switch · F5 decision-chain audit trails · F9 eval infrastructure /
model pinning · G3 adversarial testing + control evals · G2 plan-level approval · T1
MCP client posture · T6 design-pattern catalog · O4 KRIs · A3 workforce/adoption.

**Tier 3 — name them, a paragraph each:**
C6–C15 remaining threat classes · F4 rollback · F6 RAG ingestion integrity · F7/F8/F10
runtime enforcement & monitoring (mark as day-2/aspirational; vendor categories exist in
the wiki) · G4–G10 gate/contract details · T2–T5/T7/T8 matrix columns · O2/O3/O5–O9.

---

## D. Source notes

Strongest single sources for this use case:

- **Economist/Databricks "Making AI Deliver 2026"** — KONE's 4,000-citizen-developer
  three-tier model (cybersecurity + privacy the only hard limits at the bottom tier);
  Atlassian (13,000 democratised agents) vs Takeda (centralised agentic control plane)
  as the structure-matches-risk-profile contrast.
- **Microsoft Copilot Studio guidance** — Zone 1/2/3 (citizen → partnered →
  professional) is essentially this program, productized; concrete admin/compliance
  defaults.
- **LIMRA "CEO's Strategic Guide to AI"** — turnkey governance + change-management kit
  for a small regulated firm; the vendor-governance question list.
- **OWASP Agentic Top 10 + Securing Agentic Applications guide** — the concerns chapter
  backbone; introduces "Least-Agency" as a principle worth quoting.
- **Anthropic "Trustworthy Agents in Practice"** (via commentary PDF) — progressive
  trust, plan-mode approval, action-tier classes, 60-second override test.
- **WEF Empowering AI Leadership** — the only doc explicitly placing citizen developers
  inside Three Lines of Defence.

Cross-cutting framings worth quoting in Ch 3: architectural controls dominate
input-level defenses (MATRA); defenses don't transfer across layers (layered SoK
survey); "a governance layer that never changes is compliance theater" (Trustworthy AI
Agents).

`newgen.txt` is an essay on AI and active management — out of scope except the **Risk
Overseer** role framing (designing operating boundaries, error tolerances, and
escalation protocols as a creative/product role, not compliance policing) — useful for
Ch 8 platform-team job descriptions.
