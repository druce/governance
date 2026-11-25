---
title: Akto
type: vendor
name: Akto
slug: akto
aka: []
primary_category: agent-runtime-security
also_listed_in: [ai-runtime-security, ai-red-teaming, browser-security-extension]
website: https://www.akto.io/agentic-security
founded: 2022
hq: San Francisco, California, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; open-source core (GitHub: akto-api-security/akto)
acquisition: {announced: null, closed: null, price: null}
funding_total: unverified
last_funding: unverified
market_position: null
deployment_model: [saas, self-hosted]
form_factor: [platform, api, browser-extension]
data_leaves_tenancy: unverified
integrations: [aws-bedrock, azure-ai-foundry, vertex-ai, databricks, langchain, langgraph, litellm, copilot-studio, snowflake, salesforce, envoy, nginx, kong, ebpf]
mcp_support: true
certifications: []
pricing_model: freemium (open-source core; MCP Security and full platform commercial)
fs_traction: unverified
target_customer: security teams and platform engineers building or governing AI agents and MCP servers
last_verified: 2026-11-25
verify_after: null
tags: [agent-runtime, mcp-security, red-teaming, guardrails, discovery, shadow-ai, browser-extension, owasp-llm, ebpf, nhi-governance]
---

# Akto

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). Also listed in: [ai-runtime-security](../categories/ai-runtime-security.md), [ai-red-teaming](../categories/ai-red-teaming.md), [browser-security-extension](../categories/browser-security-extension.md).

**One-liner** — An agentic AI security platform with two product lines: **Akto Argus** secures the AI agents and MCP servers your engineering teams build and deploy; **Akto Atlas** secures the AI tools your employees use on their devices.

---

## Akto Argus — Agentic AI Security for Homegrown AI
*([Docs](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai))*

Argus covers the full security lifecycle — discover, test, enforce — for agents and MCP servers you build and run in your own cloud or on-premise environment.

### Agentic AI Discovery
*([Docs](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-ai-discovery))*

Continuously inventories AI agents, MCP servers and GenAI apps across dev, staging and production. Detects shadow agents (undocumented endpoints), zombie agents (deprecated but still live) and third-party agents. Builds a context graph of component dependencies, applies risk scoring, and flags sensitive-data signals including PROMPT_INJECTION. Connectors (50+):

- **Cloud AI platforms:** AWS Bedrock / BedrockAgentCore, Azure AI Foundry, Vertex AI, Databricks, Hugging Face, Snowflake
- **Agent frameworks:** LangChain, LangGraph, LiteLLM, Dify, N8N, TrueFoundry, Portkey, Arcade
- **Enterprise AI suites:** Microsoft Copilot Studio (async discovery + inline block mode + MCP Gateway routing), Microsoft 365 Copilot, Salesforce AgentForce, IBM watsonx Orchestrate, Glean, Amazon Q, Claude Agent SDK
- **API gateways:** Envoy, NGINX, Istio, HAProxy, Kong, Cloudflare, Apigee, Azure API Management, Mulesoft, F5, 3Scale, Layer7
- **Cloud infrastructure:** AWS (EKS, ECS, Fargate, Lambda, API Gateway, Beanstalk), GCP (GKE, Cloud Run, Apigee), Azure (AKS, Container Apps, App Services)
- **Other:** eBPF (incl. mTLS), Kubernetes, Docker, Kafka, AWS Traffic Mirroring, Manual Import, Akto SDK
- **[MCP Recon](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/connectors/others/mcp-recon):** IP-range / CIDR scanning to discover externally exposed MCP endpoints

### Agentic Red Teaming
*([Docs](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming))*

4,000+ AI-specific probes (vendor-reported) covering prompt injection, tool misuse, unsafe actions, policy bypass and emerging attack patterns; mapped to OWASP MCP Top 10 and AI Agent OWASP Top 10. Runs against HTTP, WebSocket, gRPC and MCP protocols. Supports custom probes via YAML templates with pre/post-request scripting, dynamic severity and wordlist support. Key integrations:

- [Scheduled runs](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming/how-to/schedule-tests) — daily / weekly / custom
- [CLI](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming/how-to/run-tests-in-cli-using-akto) — local probing (results not saved to dashboard; context-dependent probes skipped)
- [Bulk scanning](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming/how-to/run-bulk-scanning) and [Jira auto-ticket creation](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming/how-to/auto-create-jira-tickets) from findings

### Agentic Guardrails
*([Docs](https://ai-security-docs.akto.io/agentic-guardrails/overview))*

Inline enforcement via an **MCP Gateway** and an **Agent (AI) Gateway**. Blocks prompt injection (direct and indirect), tool abuse, schema violations and known attack signatures on live agent and MCP traffic. Policy controls include OWASP Core Rule Set (XSS, SQLi), tool permission enforcement, MCP schema conformance, geofencing and IP/CIDR blocking.

### MCP Security
*([Docs](https://ai-security-docs.akto.io/readme/mcp-security)) — paid feature*

Discovers MCP servers automatically and probes for tool poisoning, excessive permissions, unauthorized endpoint access and insecure authentication. Monitors for unusual tool activity with per-actor, per-IP and per-country threat views.

---

## Akto Atlas — Agentic AI Security for Employee Endpoints
*([Docs](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/overview))*

Atlas secures the AI agents, MCP servers and GenAI tools employees use on their own devices — IDEs, CLIs, browsers and local dev environments — without disrupting their workflow.

### Agentic AI Discovery
*([Docs](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/ai-agent-activity))*

Live inventory of every agentic asset (agents, MCP servers, LLMs, skills, plugins) per employee and device, with risk scores and sensitive-data flags. Surfaces shadow AI usage (personal accounts, unsanctioned tools) and local model usage. 40+ connectors:

- **Agentic CLIs & IDEs:** Claude Code, Codex, Gemini, Copilot, Kiro, Hermes, Amp, Cursor, VS Code, Antigravity, Neovim, OpenCode
- **[Browser extensions](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/endpoints-discovery-agents/browser-extensions):** Chrome, Firefox, Safari
- **Local models:** Ollama, vLLM, SGLang, Docker Model Runner
- **SaaS AI suites:** Claude Suite, ChatGPT Suite, Microsoft 365 Copilot, Copilot Studio, Amazon Q, Glean
- **MDM / EDR:** Microsoft Defender, SentinelOne, CrowdStrike, Intune, NinjaOne, Automox, Jamf, Mosyle

### AI Security Posture
*([Docs](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/endpoint-security-posture))*

Dashboard showing agentic assets, successful exploits, sensitive-data events and guardrail score. Compliance alignment against **FedRAMP, MITRE ATLAS, CIS Controls and CMMC** (vendor-reported; dashboard shows no data until sufficient signal is collected). Surfaces most-used agents, LLMs (including potential shadow usage) and MCP servers per device.

### Atlas Guardrails
*([Docs](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/atlas-guardrails))*

Inspect prompts, responses and tool calls locally inside each connector. Block sensitive-data exposure, prompt injection, risky MCP tool calls, shadow AI and personal-account sign-ins **before data leaves the device**.

### NHI Governance
*([Docs](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/nhi-governance))*

Inventories the credentials (API keys, tokens, secrets) that agentic tools silently create on employees' behalf. Tracks expiry, enforces rotation policies and flags violations before they become incidents.

---

## Where it sits in the stack

Primary [agent-runtime-security](../categories/agent-runtime-security.md) — Argus enforces at the agent's action boundary via inline gateways; Atlas enforces at the device edge. It is also substantively a runtime firewall ([ai-runtime-security](../categories/ai-runtime-security.md)), an adversarial testing platform ([ai-red-teaming](../categories/ai-red-teaming.md)), and a browser-extension endpoint play ([browser-security-extension](../categories/browser-security-extension.md)). Closest peers: [straiker](straiker.md) and [operant-ai](operant-ai.md) (agent runtime), [deepkeep](deepkeep.md) and [splxai](splxai.md) (red team + runtime), [prompt-security](prompt-security.md) (browser/guardrails), [knostic](knostic.md) (MCP/coding-agent angle).

## Deployment & architecture

Hybrid SaaS with self-hosted option. Argus connects via gateway integrations, eBPF agents, cloud connectors and traffic mirroring; the MCP and Agent Gateway sit inline. Atlas deploys via MDM-managed browser extensions, CLI/IDE hooks or existing EDR integrations. Open-source core: [akto-api-security/akto](https://github.com/akto-api-security/akto).

## Positioning & differentiators

- **Full lifecycle in one platform:** discovery → red teaming → runtime enforcement, where most peers do one or two of the three.
- **Both sides of the estate:** Argus covers server-side agents you build (CI/CD, cloud, MCP servers); Atlas covers the AI tools employees use on devices — few vendors span both.
- **MCP-native:** probes specifically for MCP-layer risks (tool poisoning, schema violations, insecure auth), not just generic LLM threats.
- **Open-source core** lowers adoption friction vs fully commercial peers.

## CTO / hedge-fund lens

**Day-2.** Argus is relevant once you have self-built agents or MCP servers in production — it gives the inventory + test + enforce loop that manual review can't scale to. Atlas is relevant when employees are using Claude Code, Cursor, Copilot or similar on managed devices and you need endpoint-level visibility before committing to a full enterprise browser. The hedge-fund angle: posture reports mapped to FedRAMP and MITRE ATLAS provide model-risk governance evidence, though FS traction is unverified. If your AI footprint is only governed SaaS assistants, Akto is premature.

## Competitors / alternatives

[straiker](straiker.md), [operant-ai](operant-ai.md), [deepkeep](deepkeep.md), [splxai](splxai.md), [lasso-security](lasso-security.md), [prompt-security](prompt-security.md), [knostic](knostic.md).

## Open questions / to verify

- Funding total and round history (no disclosed round found).
- Independent benchmark for probe count and detection accuracy (4,000+ is vendor-reported).
- FS customer references or named deployments.
- Data residency and retention terms for the SaaS offering.
- Whether the CLI integrates into CI/CD pipelines or is local-only (docs explicitly describe it as "local probing").

## Sources

- [Akto Argus docs (overview)](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/overview) — fetched 2026-11-25 — supports: Argus capabilities, 50+ connectors, 4,000+ probes, protocols; confidence: high (vendor docs).
- [Akto Argus: Agentic AI Discovery](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-ai-discovery) — fetched 2026-11-25 — supports: discovery connectors, shadow/zombie agents, context graph; confidence: high (vendor docs).
- [Akto Argus: Agentic Red Teaming](https://ai-security-docs.akto.io/akto-argus-agentic-ai-security-for-homegrown-ai/agentic-red-teaming) — fetched 2026-11-25 — supports: probe categories, scheduling, CLI, Jira integration; confidence: high (vendor docs).
- [Akto Argus: Agentic Guardrails](https://ai-security-docs.akto.io/agentic-guardrails/overview) — fetched 2026-11-25 — supports: MCP Gateway / Agent Gateway, blocking policies; confidence: high (vendor docs).
- [Akto Argus: MCP Security](https://ai-security-docs.akto.io/readme/mcp-security) — fetched 2026-11-25 — supports: MCP discovery, probe types, paid feature; confidence: high (vendor docs).
- [Akto Atlas docs (overview)](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/overview) — fetched 2026-11-25 — supports: Atlas capabilities, 40+ connectors, browser extensions, NHI governance, posture frameworks; confidence: high (vendor docs).
- [Akto Atlas: AI Security Posture](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/endpoint-security-posture) — fetched 2026-11-25 — supports: posture dashboard, compliance frameworks, caveat on data availability; confidence: high (vendor docs).
- [Akto Atlas: Browser Extensions](https://ai-security-docs.akto.io/akto-atlas-agentic-ai-security-for-employee-endpoints/endpoints-discovery-agents/browser-extensions) — fetched 2026-11-25 — supports: Chrome/Firefox/Safari coverage; confidence: high (vendor docs).
- [akto-api-security/akto (GitHub)](https://github.com/akto-api-security/akto) — fetched 2026-11-25 — supports: open-source core; confidence: high.

## History

- [2026-11-25] Vendor page created from Akto public docs and product site.
