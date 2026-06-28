# PROPOSED revision of the layer-cake table (2026-06-28)

Drop-in replacement for the table in `2026-06-19-AI-stack.md`, updated from the wiki's verified
research. **The seed file is left untouched (immutable).** Changes vs. the original:

- **M&A labelled inline** — `→ Acquirer, year` (or `→ Acquirer, announced` for pending deals). ~1/3 of
  named options are now acquired. Sources cached under `raw/sources/`; map: see the AI-security M&A map.
- **3 new rows** the original folded away: **Non-Human / Agent Identity**, **Identity Governance (IGA)**,
  **AI Red-Teaming / Guardrails**.
- **Corrections**: Jazz Security moved to **DLP** (it's AI-native DLP, not a SOC tool); **Robust
  Intelligence** renamed **Cisco AI Defense**; **GovernGPT** removed from AI Governance (it's a DDQ/RFP
  tool); **Material Security** removed from Browser Extension (it's email/workspace security);
  **WitnessAI** spelling normalised; **Comply.com** dropped (unverified).
- **Additions**: TrojAI, 7AI, Stytch, Natoma, Aembit/Oasis/Token/Entro/Clutch, etc.

Bold = the sensible default / most-shopped option in that row.

| Layer | Options (→ = acquired) | Business Objective | Priority |
| --- | --- | --- | --- |
| **Foundation Layer** | | | |
| **Identity & Access** | **Microsoft Entra ID**, Okta, Ping Identity *(now incl. ForgeRock)* | Every human *and* agent has a real identity, SSO, and RBAC. The bouncer at the door — verifies who you are and hands out least-privilege badges. | **Required — Day 1** |
| **Non-Human / Agent Identity** *(new row)* | **CyberArk** *(→ Palo Alto, 2026)*, Aembit, Oasis Security, Token Security, Entro Security, Clutch Security, Astrix *(→ Cisco, announced)*, Natoma *(→ Snowflake, announced)* | Give workloads and AI agents real, scoped, rot_able identities — not shared secrets. The badge office for the bots. | Day 2 — when agents proliferate |
| **Identity Governance (IGA / ISPM)** *(new row)* | **SailPoint**, Saviynt, Veza *(→ ServiceNow, 2026)*, ConductorOne, Lumos, Silverfort | Joiner/mover/leaver, access certification, right-sizing. The periodic "who still has the keys?" audit. | Day 1 if doing RAG; else Day 2 |
| **Secrets Manager** | **Azure Key Vault**, HashiCorp Vault *(→ IBM, 2025)*, AWS Secrets Manager, CyberArk Conjur *(→ Palo Alto, 2026)*, 1Password | Centralized secrets. The locked drawer for passwords and API keys, rotated without disrupting production. | **Required — Day 1** |
| **Enterprise logging / SIEM / SOC** | **Microsoft Sentinel**, Splunk *(→ Cisco, 2024)*, Palo Alto Cortex XSIAM, Sumo Logic *(→ Francisco Partners, 2023)*, Elastic, Google SecOps | Centralized logging for monitoring, detection, audit trail. The security-camera control room. | **Required — Day 1** |
| **AI SecOps / Agentic SOC Analysts** | **Palo Alto Cortex AgentiX**, CrowdStrike Charlotte AI, Prophet, Dropzone, 7AI, Radiant, Simbian, Torq | RoboCop reading the logs — agentic triage and response. | Day 2 |
| **EDR / XDR** | **CrowdStrike Falcon**, Microsoft Defender XDR, SentinelOne, Palo Alto Cortex XDR | Detect and respond to malware/intrusion at the endpoint. The immune system for laptops and servers. | Day 1 — usually already deployed |
| **Network Security / SASE** | **Palo Alto NGFW + Prisma Access**, Zscaler, Netskope, Cisco Secure Access, Cloudflare, Cato, Forcepoint | Inspect/control traffic in and out, incl. TLS-inspecting man-in-the-middle of ChatGPT/Claude traffic. The walls, checkpoints, and remote-work tunnel. | Day 1 — usually already deployed |
| **SaaS Security Posture (SSPM)** | **AppOmni**, Obsidian, Adaptive Shield *(→ CrowdStrike, 2025)*, Grip, Valence, Wing, DoControl | Continuously assess and harden SaaS configs. Catches the AI feature someone quietly switched on in Salesforce. | Day 2 |
| **Software Supply Chain & Coding Security** | **Snyk**, Semgrep, Endor Labs, Socket, Apiiro, Legit Security, Aikido, Sonatype, JFrog, GitHub Advanced Security, GitLab Ultimate | Secure the software supply chain. The safety inspector for code — incl. what your copilots generate. | Day 1 if shipping AI-generated code; else Day 2 |
| **Security Awareness / Anti-Deepfake** | **Adaptive Security** *(OpenAI-backed)*, Doppel, Reality Defender, GetReal, Pindrop | Defend the human layer against AI-era social engineering — deepfake voices, cloned execs, AI phishing. | Day 2 (AI-era tooling still emerging) |
| **Data Layer** | | | |
| **Data Classification & DSPM** | **Microsoft Purview**, BigID, Securiti *(→ Veeam, 2025)*, Cyera, Sentra, Symmetry Systems *(→ Zscaler, 2026)*, Normalyze *(→ Proofpoint, 2024)*, Wiz *(→ Google, 2026)*, Concentric, Bedrock, Rubrik | Discover, classify, and assess the posture of data at rest. The labeler that knows where MNPI/PII/privileged data lives and how exposed it is. | **Required — Day 1** |
| **Data Loss Prevention (DLP)** | **Cyberhaven**, Nightfall AI, MIND, Prompt Security *(→ SentinelOne, 2025)*, Lasso Security, Jazz Security, Netskope DLP, Microsoft Purview DLP, Forcepoint | Prevent exfiltration via content-/lineage-aware controls. The bouncer at the exits — incl. data leaving via AI prompts. | **Required — Day 1** |
| **Data Access Governance** | **Varonis**, Veza *(→ ServiceNow, 2026)*, Cyera, Sentra, Concentric, ConductorOne, Silverfort, Netwrix | Audit and right-size permissions; monitor access. Finds the folder where "Everyone" accidentally has access. | Day 1 if doing RAG; else Day 2 |
| **AI Model and Prompt Layer** | | | |
| **AI Runtime Security (AI Firewall)** | **Palo Alto Prisma AIRS** *(incl. Protect AI + Portkey)*, HiddenLayer, WitnessAI, Pillar Security, Cisco AI Defense *(ex-Robust Intelligence)*, SplxAI *(→ Zscaler, 2025)*, Aim Security *(→ Cato, 2025)*, Lasso Security, Enkrypt AI, CalypsoAI *(→ F5, 2025)*, Lakera *(→ Check Point, 2025)*, TrojAI *(→ A10, 2026)* | Protect AI apps at runtime from attack and exfiltration. The metal detector for prompts/responses — blocks injection, jailbreaks, leaks. | **Required — Day 1** |
| **AI Gateway** | **Portkey** *(→ Palo Alto, 2026)*, LiteLLM, Kong AI Gateway, F5 AI Gateway, Cloudflare, TrueFoundry, OpenRouter | Single exit door for all model traffic. The traffic cop and toll booth — routes, rate-limits, logs and archives everything. | **Required — Day 1** |
| **LLM Observability & Evaluation** | **Langfuse** *(→ ClickHouse, 2026)*, LangSmith, Arize Phoenix, Helicone *(→ Mintlify, 2026)*, Braintrust, Datadog, Comet (Opik), Fiddler, Arthur, TruLens *(Snowflake)*, WhyLabs *(→ Apple, 2025; wound down)* | Central prompt repo; trace, evaluate, debug behavior and spend. The flight recorder for your AI. | Day 1 — lightweight, want it from launch |
| **AI Red-Teaming / Guardrails** *(new row)* | **Mindgard**, SplxAI *(→ Zscaler)*, Lakera *(→ Check Point)*, HiddenLayer, Patronus AI, Haize Labs, Guardrails AI, NeMo Guardrails, Maxim AI, Promptfoo *(→ OpenAI, 2026)* | Offline attack-simulation + guardrail libraries — find injection/jailbreak weaknesses *before* production. The pen-tester for your model. | Day 2 (Day 1 if building your own AI apps) |
| **AI Access Governance (CASB for AI)** | **WitnessAI**, Harmonic Security, Aurascape, Cyberhaven, Zscaler AI Guard, Netskope One, Nudge Security, Reco, Lanai, Wald.ai, Portal26 | Govern how employees and agents *use* AI — discover shadow AI, enforce inline policy on what data flows to which model. The velvet-rope host for AI. Intent-aware, not just destination-aware. | Day 1 if employees use public AI tools (they do) |
| **AI-SPM / Agent Governance** | **Zenity**, Noma Security, Prisma AIRS, Cranium, Quilr, Wiz AI-SPM *(Google)*, Reco, Operant AI, Straiker | Discover, monitor, and govern agents org-wide — posture + runtime. The supervisor watching the bots you didn't know you had. | Day 2 — when agents proliferate |
| **Authorization Engine (Agent / Tool)** | **Cerbos**, OPA *(CNCF)* / Styra *(team → Apple, 2025)*, Permit.io, AuthZed (SpiceDB), Oso, Pomerium | Fine-grained, externalized authorization for agent actions. "Is this agent allowed to do this, right now?" | Day 2 — when agents act |
| **MCP Gateway / Tool Access Control** | **Solo.io agentgateway**, Arcade.dev, Kong (MCP ACLs), IBM ContextForge, Docker MCP Gateway, Obot, MintMCP, Prisma AIRS Agent Gateway | Single doorway for tools agents can reach. Allowlist, broker, audit — only sanctioned MCP servers/tools get through. | Day 2 — when agents use tools |
| **Tool Identity & Integration** | **Composio**, StackOne, Arcade.dev, CyberArk *(→ Palo Alto)*, Descope, Stytch *(→ Twilio, 2025)*, WorkOS | Secure, managed agent-to-tool integration. A universal adapter — managed auth and prebuilt connectors so agents reach SaaS without hand-built OAuth. | Day 2 — when agents integrate with SaaS |
| **Retrieval Layer** | | | |
| **Content Sources** | SharePoint, OneDrive, Confluence, Google Drive, etc. | Connect AI to systems of record. Where your knowledge actually lives. | Day 1 if doing RAG (existing systems) |
| **Vector Retrieval** | Azure AI Search, Pinecone, Weaviate, OpenSearch | Semantic search/retrieval infrastructure. The AI's card catalog. | Day 1 if doing RAG; else N/A |
| **Entitlement-Aware RAG** | **Glean**, Microsoft Graph (Copilot), Knostic | Permission-aware retrieval so the AI never surfaces forbidden data. Only shows documents you were already allowed to see. | Day 1 if doing RAG — non-negotiable then |
| **User Experience Layer** | | | |
| **Enterprise AI Assistant** | **Claude Enterprise / ChatGPT Enterprise**, Microsoft 365 Copilot, Gemini Enterprise, Amazon Q Business, Perplexity Enterprise | A governed, compliant general-purpose assistant. The chatbot your people use, with enterprise plumbing (logging, archival, no-train) attached. | **Required — Day 1** |
| **Third-Party AI Apps** | Domain-specific vendors, routed via the AI gateway with archival + SIEM logging | Bring vendor/shadow AI under the same controls. Funneled through the gateway so they don't go rogue. | Optional — as vendors are onboarded |
| **Enterprise Browser** | **Island**, Prisma Access Browser *(ex-Talon)*, Menlo, Seraphic *(→ CrowdStrike, announced)*, Red Access, Chrome Enterprise Premium, Edge for Business | Secure the browser where most AI use happens. A work browser with guardrails baked in. | Optional — architecture choice |
| **Browser Security Extension** | **LayerX** *(→ Akamai, announced)*, Grip Security, Chrome Enterprise controls | Browser-level DLP and monitoring. A bolt-on guard for your existing Chrome. | Optional — often either/or with enterprise browser |
| **Governance Layer** | | | |
| **AI Governance Platform** | **Credo AI**, Holistic AI, ModelOp, Fairly AI *(now Asenion)*, CalypsoAI *(→ F5)*, Vanta, IBM watsonx.governance, Monitaur, OneTrust | Prove and manage AI risk to regulators and the board. The control tower — inventories every model/use case and maps to NIST AI RMF / EU AI Act / SR 11-7. | Day 2 (Day 1 under SR 11-7 model risk) |
| **Enterprise GRC** | **ServiceNow GRC**, Archer *(Cinven)*, LogicGate, AuditBoard *(→ Hg, 2024)*, OneTrust, Onspring | One governed register for risk, controls, policy, audit. Where your AI risk tiers and approvals actually live. | Day 1 — usually already owned |
| **Third-Party / Vendor Risk + Cyber Ratings** | **ProcessUnity**, SecurityScorecard, BitSight, Black Kite, UpGuard | Assess and monitor third-party/vendor risk. The background check on every AI vendor before they touch your data. | Day 1 — extend existing TPRM to AI vendors |
| **Comms Surveillance** | **Behavox**, SteelEye, NICE Actimize, Theta Lake, Shield, Relativity Trace | MAR/market-abuse and conduct surveillance over comms captured to Smarsh/Global Relay. The compliance detective — now replaying AI prompts/responses too. | Day 2 |
| **Ephemeral Environments** | GitHub Codespaces, Azure Dev Boxes, Terraform Cloud *(IBM)*, Cloudflare Workers | Zone-scoped, reproducible, short-lived compute. Disposable workspaces that vanish — nothing sticky to compromise. | Day 2 — for dev/agentic workloads |
| **Policy-as-Code** | **Open Policy Agent (OPA)**, HashiCorp Sentinel *(IBM)*, Kyverno | Automated, version-controlled policy enforcement. Guardrails as software, not a PDF nobody reads. | Day 2 — automate after manual policy |
| **Policy / Process Layer** | | | |
| **Trust Zone Segmentation** | Red / yellow / green zones for ephemeral and persistent environments | Break the exfiltration chain so untrusted input, sensitive data, and egress (the lethal trifecta) never line up at once. | **Required — Day 1** (design it in) |
| **Risk Tiers** | Internal governance classification | Classify AI systems/use cases by risk so scrutiny matches the stakes. | **Required — Day 1** (process) |
| **Promotion Gates** | CI/CD approval workflows, change management | A controlled path to production — somebody signs off between experiment and live. | Day 1 — process, keep it lightweight |
| **HITL Approvals** | ServiceNow approvals, custom workflow engines | Human approval on high-stakes agent actions. | Day 2 — when agents take consequential actions |
| **Acceptable Use Policies** | Internal policy framework | Set organizational AI usage standards everyone signs. | **Required — Day 1** (cheapest control there is) |

---

### Notes for the author
- **Pending deals** (`announced`): Astrix→Cisco, Seraphic→CrowdStrike, LayerX→Akamai, Natoma→Snowflake, Symmetry→Zscaler — all announced but not confirmed closed as of 2026-06-28; verify before publishing.
- **Acqui-hires** (team, not company): WhyLabs→Apple and Styra/OPA→Apple — OPA itself stays under the CNCF.
- Consider an intro sentence on the **consolidation wave** (Palo Alto, Cisco, Zscaler, CrowdStrike, F5, Snowflake, Apple each running multi-deal AI roll-ups) and linking to the wiki's `ai-security-m-and-a-map` as the kept-current companion.
- **Open items to confirm before publishing:** "Comply.com" (could not verify); GovernGPT's true category (DDQ/RFP tool); Material Security's slot (email security, not browser).
