URL: https://github.com/IBM/mcp-context-forge
Fetched: 2026-06-28
Note: Primary source — the IBM/mcp-context-forge GitHub repo README. Good for what it does, license, architecture, deployment, transports, maturity.

## Key extracted facts

- Self-description: "An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins."
- "an open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs" with centralized governance, discovery, and observability.

### Architecture
- Language & framework: Python with FastAPI backend.
- Transports: "HTTP, JSON-RPC, WebSocket, SSE, stdio and streamable-HTTP".
- Protocol support: MCP, A2A (OpenAI, Anthropic agent routing), gRPC-to-MCP translation.
- REST-to-MCP tool adapter with automatic JSON Schema extraction; virtualization of non-MCP services into virtual MCP servers; unified registries (prompts, resources, tools).
- TOON compression mentioned for tools gateway.

### Deployment
- PyPI package name: `mcp-contextforge-gateway` (`pip install mcp-contextforge-gateway`).
- Docker images, Docker Compose, Kubernetes Helm charts.
- Scaling: single-node Gunicorn → multi-replica Kubernetes with Redis-backed federation and caching.
- DB: SQLite (dev), PostgreSQL (production).

### Auth & security
- Auth: Basic, JWT, or custom schemes; user-scoped OAuth tokens; built-in rate limiting and retries.
- Plugin extensibility: 40+ plugins for transports, protocols, integrations, and guardrails.
- Note: sample MCP servers in the repo "lack session management, persistent state, multi-tenancy, authentication" and should not be used in production without appropriate security measures.

### Observability
- OpenTelemetry tracing with Phoenix, Jaeger, Zipkin, and other OTLP backends (vendor-agnostic).

### Maturity / ownership
- Owner: IBM (GitHub org IBM/mcp-context-forge). Apache License 2.0.
- Latest release v1.0.4, published 2026-06-23 ("Rust Migration, Docker Improvements, Security Enhancements, and Bug Fixes").
- ~4k GitHub stars, ~725 forks, 7,000+ tests (as of fetch).
- Lead maintainer: Mihai Criveti (IBM Distinguished Engineer, Agentic AI). Other contributors listed: Brian Hussey, Frederico Araujo, Jonathan Springer, Keval Mahajan, Manoj Jahgirdar, Nayana R Gowda.
- Documentation does not explicitly state IBM provides commercial support / warranties — presents as a corporate-backed open-source community project.
