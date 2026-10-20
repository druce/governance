# NVIDIA OpenShell — independent and third-party analysis (Futurum, CSA, Tigera)

- URL: https://futurumgroup.com/?p=96053 ("NVIDIA Wants Agent Safety Enforced in Silicon", 2026-09-29)
- URL: https://labs.cloudsecurityalliance.org/agentic/csa-research-note-nemoclaw-security-assessment-20260327/ (CSA research note, 2026-03-27, status: draft)
- URL: https://www.tigera.io/?p=69229 ("NVIDIA OpenShell Secures the Agent. Who Governs the Fleet?", 2026-07-15)
- Not retrievable: https://www.trendmicro.com/en/research/26/c/what-openshell-gets-right-what-nemoclaw-still-cant-fix.html (HTTP 404 on 2026-10-20; title surfaced in search only)
- Fetched: 2026-10-20
- Good for: the "OpenShell analysis" critiques — limitations, scope gaps, policy-authoring burden. Tigera is a competitor/complement vendor (sells Lynx), label as vendor analysis.

## Futurum Group (Montenegro, Burke, Ashley), 2026-09-29 — analyst
- "Moving agent controls outside the agent's reach is the right instinct." Prover deterministic: "an agent cannot talk its way past it."
- "The prover can tell you the fence is where you drew it, not whether you drew it in the right place." NVIDIA docs: "a passing result does not establish least privilege or semantic safety."
- Cross-agent analysis still ongoing; NVIDIA has not published overhead measurements.
- Sentry depends on BlueField-4, "whose adoption is still limited"; "most enterprises do not have BlueField today"; Sentry "not fully open source"; telemetry gap flagged in March "still open".
- "The credential swap deserves more CIO attention than it will get"; MCP coverage unclear.
- Until OpenShell moves to a foundation, "governance sits with NVIDIA."
- "Reference deployments or third-party audits from regulated partners would carry more weight than the logos."
- Expect several agent control planes; partners may become competitors at the control point.

## CSA research note (draft), 2026-03-27 — NemoClaw/OpenShell vs AICM and MAESTRO
- Rates runtime isolation (Landlock, seccomp, network namespaces) "Strong"; out-of-process policy engine the key innovation (agent cannot access, terminate or signal it). Declarative YAML; filesystem/process locked at creation; network hot-reload.
- Agent never holds model API keys; calls go via gateway.
- Privacy-router classification rules static; extend to firm data classes before enabling cloud routing.
- Limits: "cannot prevent initial code execution"; "no mechanism to compare observed agent behavior against intended task parameters"; Evaluation & Monitoring coverage "Minimal"; policies drift wider over time.
- Not addressed: goal misalignment, behavioural drift, inter-agent trust / instruction verification, persistent agent identity and revocation, multi-agent coordination, prompt-injection detection, malicious skill installation (ClawHub), model/RAG poisoning.
- Recommends pairing with SIEM/behavioural monitoring, conservative allowlists, quarterly policy review.
- Partner notes (draft, unverified): Cisco DefenseClaw ↔ OpenShell policy logs; CrowdStrike sandbox telemetry → Falcon.

## Tigera blog (Alister Baroi), 2026-07-15 — vendor analysis
- "OpenShell is a secure runtime for a single agent on a single machine." "OpenShell answers 'what can this agent do on this box?'"
- Four policy layers: filesystem (Landlock, locked at creation), process (seccomp), network (default-deny, HTTP method/path, hot-reload), inference (privacy router swaps credentials so real key stays out of sandbox).
- Says NVIDIA docs exclude agent-to-agent governance, agent identity/authentication, cross-sandbox patterns. Kubernetes Helm chart then experimental/"not for production". Project described as alpha (pre-0.1.0).
- "Each sandbox still enforces its own YAML in isolation, with no shared agent identity and no view of its neighbors." Pitches Tigera Lynx (SPIFFE identity, Cedar, gateway, fleet audit) as the fleet layer.
