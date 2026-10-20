# kagent — CNCF status, GitHub repo, Solo Enterprise for kagent, 2026 news

- URL: https://www.cncf.io/projects/kagent/
- URL: https://github.com/kagent-dev/kagent (and GitHub API metadata + releases)
- URL: https://www.solo.io/press-releases/kagent-enterprise ; https://www.solo.io/blog/kagent-enterprise
- URL: https://www.solo.io/discover/ai-agents
- URL: https://www.kagent.dev/docs/kagent/examples/human-in-the-loop (via search summary)
- URL: https://www.solo.io/press-releases/solo-io-brings-nemoclaw-to-production-agentic-runtime-for-kubernetes
- URL: https://blogs.vmware.com/cloud-foundation/2026/08/07/running-solo-io-enterprise-agentgateway-and-kagent-on-vmware-cloud-foundation/
- URL: https://www.cncf.io/blog/2025/08/19/celebrating-100-days-of-kagent/ (search summary)
- Fetched: 2026-10-20
- Good for: kagent status/licence/features, enterprise edition features, 2026 product news.
  Used for the taxonomy-gaps proposal (no wiki page).

## CNCF (primary)
- "kagent was accepted to CNCF on May 22, 2025 at the Sandbox maturity level." Repo kagent-dev/kagent.
- CNCF blog 2025-08-19 (100 days): ~100 contributors, >85% from outside Solo.io (search summary).

## GitHub (primary; API 2026-10-20)
- Apache-2.0. Created 2025-01-21. ~4,060 stars. Last push 2026-10-20.
- Latest stable tag v0.10.3 (2026-10-02); v1.0.0-alpha15/16 published 2026-10-19.
- README: Kubernetes-native; agents defined as CRDs; RemoteMCPServer resources; bundled MCP server
  with tools for Kubernetes, Istio, Helm, Argo, Prometheus, Grafana, Cilium; controller exposes
  gRPC, A2A and MCP APIs; runtimes Go/Python ADK, Codex, Claude or custom; LLM providers OpenAI,
  Azure OpenAI, Anthropic, Vertex AI, Ollama; OpenTelemetry tracing. "kagent is a Cloud Native
  Computing Foundation project." RBAC not described in README.
- HITL docs: per-tool `requireApproval` list on spec.declarative.tools.

## Origin (secondary)
- Announced by Solo.io March 2025 (The New Stack, techstrong.ai). Audience: DevOps/platform engineers.

## Solo Enterprise for kagent (vendor)
- Announced 2025-09-15. Adds: identity/policy model for agents acting on behalf of users; AgentOps
  dashboard with agent graph and end-to-end tracing; agent registry; declarative lifecycle;
  HITL/human-on-the-loop controls; bundled agentgateway; failover and memory management;
  multicluster/federated management. No pricing, no named customers.
- solo.io/discover/ai-agents (2026-10-20): "kagent gives every agent a verifiable identity and
  granular, policy-governed access"; FIPS 140-2 validated builds; enterprise support with SLAs.
  No customers named.
- Enterprise changelog: 0.5.10 (~2026-10-05) integrates agentevals with Replay mode (search summary).

## 2026 news (vendor)
- 2026-05-07: NVIDIA NemoClaw (built on OpenClaw) supported in kagent; on-behalf-of authorization,
  per-step tracing, multicluster federation, GitOps. "trusted by leading retail, financial services,
  and telecommunications enterprises" — unnamed. >300 contributors (Microsoft, Amazon, Oracle,
  Amdocs, Orange cited as contributors, not customers).
- 2026-08-07 (VMware/Broadcom blog): Solo Enterprise for agentgateway and for kagent validated on
  VMware Cloud Foundation; joint reference architecture "in development". FS only a hypothetical.
