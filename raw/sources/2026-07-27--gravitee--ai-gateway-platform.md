# Gravitee AI Gateway — product page + 4.10 release

- URL: https://www.gravitee.io/platform/ai-gateway (product page, vendor marketing)
  + https://www.gravitee.io/blog/gravitee-4.10-one-control-point-to-secure-govern-ai-agents-mcp-and-llms (4.10 release blog)
  + https://documentation.gravitee.io/apim/4.10/agent-mesh (docs)
- Fetched: 2026-07-27
- Good for: confirming Gravitee has a *specific* AI-gateway and MCP-gateway product line
  (not just generic API management); feature names; deployment models.

## Facts

- Gravitee's **AI Gateway** is marketed as one control point for three protocol-aware
  paths, each with its own governance layer:
  - **LLM Proxy** — governs the model path. A dedicated v4 API type that sits between an
    LLM consumer and one or more providers, exposing an **OpenAI-compatible interface**.
    Named providers: **Anthropic, AWS Bedrock, OpenAI, Google Gemini, Vertex**.
    Token-aware controls (token quotas/rate limits), **semantic caching**, cost attribution.
  - **MCP Proxy** — governs the tool path. Protocol-native: introspects JSON-RPC 2.0
    payloads for tool discovery/invocation; **Proxy and Studio modes**;
    **method-level and resource-level access control**.
  - **A2A Proxy** — governs the agent-to-agent path; delegated authorization with
    "fully traceable on-behalf-of chains."
- **Security/policy**: OAuth 2.1 + PKCE, **PII filtering**, prompt guardrails,
  method-level ACLs, "protocol-aware enforcement" that targets tool names and MCP
  methods directly (rather than URL paths).
- **AI IAM (Agentic Identity & Access Management)**, shipped in 4.10: standards-based
  authorization for agent tool access, separating decision from enforcement. Uses
  **OpenFGA** (ReBAC) and the **AuthZen** standard for tool-level permissions. MCP
  resource-server functionality delegates authn/token management to Gravitee
  Access Management.
- **Observability**: OpenTelemetry-based; traces enriched with Catalog entity IDs and
  policy decisions at every step; unified cost attribution by team, model, use case,
  or agent.
- **Deployment**: "SaaS, self-hosted, and hybrid," sold as part of Gravitee Agent
  Management.
- **Umbrella naming**: "Gravitee AI Agent Management" = Agent Gateway + Agent Catalog +
  Agent Tool Server. Gravitee 4.10 release date given as **2026-01-22**.

## Caveat

All of the above is vendor marketing/docs. No independent corroboration of the
guardrail/PII-filter efficacy was found.
