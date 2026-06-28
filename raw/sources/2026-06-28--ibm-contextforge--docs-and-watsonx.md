URL: https://ibm.github.io/mcp-context-forge/ (docs) and https://developer.ibm.com/tutorials/build-mcp-tools-mcp-gateway-watsonx-orchestrate-agents/ (watsonx tutorial)
Fetched: 2026-06-28
Note: Secondary/primary IBM sources — official docs site and IBM Developer tutorial. Good for license confirmation, feature framing, and the watsonx Orchestrate relationship.

## Docs site (ibm.github.io/mcp-context-forge)
- "an open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs with centralized governance, discovery, and observability."
- Licensed under the Apache License 2.0 (footer).
- Gateway pillars described: Tools Gateway (MCP, REST, gRPC-to-MCP translation, TOON compression); Agent Gateway (A2A protocol, OpenAI-compatible and Anthropic agent routing); API Gateway (rate limiting, auth, retries, reverse proxy for REST); Plugin Extensibility (40+ plugins); Observability (OpenTelemetry → Phoenix/Jaeger/Zipkin/OTLP).
- Admin UI for management and monitoring.
- Deployment: PyPI, Docker, Docker Compose, Kubernetes/Helm, and major clouds (AWS, Azure, Google Cloud, IBM Cloud).
- Project maintained on GitHub under IBM org; docs do not explicitly state IBM commercial support.

## watsonx Orchestrate tutorial (developer.ibm.com) — note: page returned HTTP 403 on direct fetch; summary from IBM search index/snippet
- Title: "Deploying MCP Tools on watsonx Orchestrate by using ContextForge MCP Gateway".
- Shows how to deploy MCP Gateway on IBM Code Engine and integrate MCP tools into agents built on watsonx Orchestrate, providing "secure, centralized access for multiple agents and workflows."
- Indicates ContextForge is the recommended/used MCP gateway in IBM's own watsonx Orchestrate agent tutorials, though ContextForge itself is the standalone OSS project (not a watsonx feature).

## Also noted (search index)
- IBM Developer blog "Available Now: ContextForge MCP Gateway 1.0.0 Beta" exists (developer.ibm.com/blogs/context-forge-mcp-gateway-now-available/) — direct fetch returned 403; title corroborates 1.0 milestone timing.
