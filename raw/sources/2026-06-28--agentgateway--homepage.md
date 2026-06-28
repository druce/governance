URL: https://agentgateway.dev/
Fetched: 2026-06-28
Good for: official project site — one-liner, feature list, deployment models, governance, license.

---

One-liner: open source HTTP and gRPC gateway handling traditional application traffic
and AI-native protocols in a unified data plane (single binary).

Routes/manages traffic across services, LLM providers, MCP tools, and A2A through one binary,
eliminating need for multiple specialized gateways.

Features:
- MCP Gateway: discovery, RBAC, versioning, audit trails for MCP servers.
- A2A Gateway: identity, tracing, replay across frameworks (LangChain, CrewAI, ADK).
- LLM Gateway: routes to OpenAI, Claude, Gemini, self-hosted; failover, per-team token budgets.
- Security & Authorization: mTLS, OIDC, OPA-evaluated policies, "tamper-evident audit logs".
- Observability: OpenTelemetry by default; per-tool and per-tenant counters.

Deployment: standalone binary, Docker containers, Kubernetes (Helm charts).

Governance: "An AAIF Project" (Agentic AI Foundation, part of Linux Foundation).
Solo.io donated the project; open source governance.

License: Apache 2.0.

Marketing claims flagged: "zero-config TLS"; positioning as eliminating "stitching
together separate gateways."
