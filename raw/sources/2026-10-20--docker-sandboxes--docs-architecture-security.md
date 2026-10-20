# Docker Sandboxes — product docs: overview, architecture, security, FAQ, local vs cloud, MCP gateway

- URL: https://docs.docker.com/ai/sandboxes/
- URL: https://docs.docker.com/ai/sandboxes/architecture/
- URL: https://docs.docker.com/ai/sandboxes/security/
- URL: https://docs.docker.com/ai/sandboxes/faq/
- URL: https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/
- URL: https://docs.docker.com/ai/sandboxes/mcp-gateway/
- Fetched: 2026-10-20
- Good for: isolation model, egress/credential mechanics, default posture and stated limitations, pricing model, telemetry, cloud vs local differences, relation of sbx MCP gateway to Docker Desktop MCP Toolkit. Vendor docs.

## Overview
- Runs AI coding agents in isolated environments locally ("local sandboxes") or on Docker-managed cloud infrastructure ("cloud sandboxes"), managed with the `sbx` CLI. Cloud sandboxes also via a Sandboxes API and SDK.
- Pricing: `sbx` CLI and local sandbox compute free, including commercial use. Cloud compute pay-as-you-go (no rates on page). Organization governance (central policy for local sandboxes) "requires a separate paid subscription". Model-provider charges separate.
- GA/beta status not stated.

## Architecture
- Each sandbox is a microVM ("Full (hypervisor)" isolation). Each sandbox runs its own Docker daemon (separate state, image cache); sandboxes do not share images.
- Workspaces: direct mount via virtiofs at the same absolute path; or clone mode (host repo mounted read-only at /run/sandbox/source).
- Network: all outbound TCP goes through a host-side proxy (HTTP/HTTPS forward proxy; other TCP forwarded transparently); both enforce policy. Only HTTP/HTTPS can chain to an upstream proxy.
- Credentials: agent sees a sentinel value; host-side proxy checks policy, swaps sentinel for real credential after the request leaves the microVM. Real credential stays on host.

## Security
- Outbound TCP deny-by-default; default allowed domains include broad wildcards (e.g. `*.googleapis.com`) — docs advise reviewing with `sbx policy ls`.
- Blocked by default: host filesystem outside workspace and shared skills store; host Docker daemon; host network; non-allowed destinations; sandbox-to-sandbox traffic; outbound UDP (unless experimental feature); ICMP.
- Agent has full control inside the VM including sudo; microVM is primary trust boundary.
- Stated limitations: direct-mode workspace changes are live on host (agent can edit Git hooks, CI configs, Makefile, package.json scripts); kit installs run as root (limited to Docker Hub by default); read-write shared skills join sandboxes into one trust boundary; local stdio MCP servers run on the host with host permissions; remote MCP servers run outside Sandboxes; VM state persists across restarts.

## FAQ
- Sign-in required: verified identity per sandbox, governance, audit logs, authenticating to Docker infrastructure.
- Telemetry: command, success, duration, Docker username; not prompts or code. Opt out `SBX_NO_TELEMETRY=1`. Local sandboxes upload diagnostics to an S3 endpoint (per domain list). Files transferred to cloud sandboxes are stored in the cloud.

## Local vs cloud
- Cloud: Docker-managed resources (provider/region not stated), linux/amd64 and arm64, public HTTPS URL for ports, TTL expiry, MCP via "Docker Agentic Platform". Separate secrets, network policy (network-only; no L7 method/path rules). AI Governance local policies are not applied to cloud sandboxes.
- `sbx move` copies a filesystem snapshot; credentials saved in files inside the sandbox can be included.

## MCP gateway
- Docker Sandboxes MCP gateway "is separate from the Docker Desktop MCP Toolkit"; the two don't share server settings. No deprecation statement either way. Relationship to the open-source docker/mcp-gateway codebase not stated.
- `sbx` on host manages registered servers and OAuth; local stdio servers run on host; tokens in OS credential store. With AI Governance, MCP access policies in Cedar control registration, tool calls, meta-tools, resources, prompts, approvals.
