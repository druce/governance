URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/  and  https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/
Fetched: 2026-06-28
Note: Docker official docs — gateway architecture + catalog signing/provenance.

---

MCP Gateway (docs):
- Centralized proxy between clients and servers, "managing configuration, credentials, and access control."
- Container isolation: "MCP Gateway runs MCP servers in isolated Docker containers with restricted privileges, network access, and resource usage." Provides "isolation, consistent environments, and centralized control."
- Built-in logging and call-tracing for "full visibility and governance of AI tool activity."
- Manages credential injection; applies security restrictions before forwarding requests.
- Deployment: runs automatically in background when MCP Toolkit enabled in Docker Desktop. Manual install for Docker Engine — download binary from GitHub to ~/.docker/cli-plugins/ (Linux/macOS).

MCP Catalog (docs):
- Curated collection of verified MCP servers distributed via Docker Hub. 300+ servers (local containers + cloud-hosted remote from partners like New Relic, Stripe, Grafana).
- "All servers are versioned with full provenance and SBOM metadata." Docker "builds and signs all local servers in the catalog."
- Each server runs as an isolated container. Browse at hub.docker.com/mcp or in Docker Desktop MCP Toolkit; custom catalogs importable.

(Secrets-blocking interceptor / --block-secrets detail corroborated by Docker docs + community write-up dasroot.net/posts/2026/01/docker-mcp-gateway-interceptors-security/: pre-call interceptors for arg/type checks + safety classifiers; post-call interceptors for redaction/PII scrub; image provenance verification.)
