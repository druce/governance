URL: https://github.com/agentgateway/agentgateway
Fetched: 2026-06-28
Good for: primary repo — what agentgateway is, license, governance, features, language, maturity.

---

AgentGateway: "the first complete connectivity solution for Agentic AI" — an open source
proxy built on AI-native protocols (MCP & A2A). Marketing framing ("first complete").

Three gateways:
- LLM Gateway: unified OpenAI-compatible API to major providers; budget/spend controls,
  prompt enrichment, load balancing, failover.
- MCP Gateway: connects LLMs to tools via Model Context Protocol; tool federation,
  stdio/HTTP/SSE/Streamable HTTP transports, OpenAPI integration, OAuth authentication.
- A2A Gateway: agent-to-agent; capability discovery, modality negotiation, task collaboration.

Security & governance: Auth (JWT, API keys, OAuth), fine-grained RBAC with CEL policy
engine, rate limiting, TLS, OpenTelemetry metrics/logs/tracing.

License: Apache 2.0. "A Linux Foundation project."

Maturity (as of fetch): ~3.6k GitHub stars, 599 forks, 90 releases, latest v1.3.1.
Built primarily in Rust (61.3%), Go (24.3%), TypeScript (11.0%).
Deployment: standalone binary and Kubernetes options. Active community meetings.
