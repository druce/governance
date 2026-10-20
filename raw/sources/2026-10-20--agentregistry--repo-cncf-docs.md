# agentregistry — GitHub repo, CNCF sandbox application, Solo Enterprise docs, launch PR

- URL: https://github.com/agentregistry-dev/agentregistry (and GitHub API metadata + releases)
- URL: https://github.com/cncf/sandbox/issues/477 ("[Sandbox] agentregistry")
- URL: https://www.solo.io/press-releases/agent-skills-kubernetes-ecosystem
- URL: https://www.solo.io/blog/understanding-the-agentregistry-project-and-the-problems-it-solves
- URL: https://docs.solo.io/agentregistry/latest/ ; .../about/about/ ; .../about/concepts/ ; .../security/overview/
- Fetched: 2026-10-20
- Good for: what agentregistry catalogs, OSS vs enterprise controls (OIDC, RBAC AccessPolicy,
  approval queue, runtime authorization, discovery), CNCF status (primary record), licence, maturity.

## GitHub (primary; API metadata 2026-10-20)
- Tagline: "Fast-track AI innovation with a centralized, trusted, curated registry." Hub for
  finding, managing and running MCP servers, agents and skills.
- Licence Apache-2.0. Repo created 2025-10-27. ~526 stars, 99 forks. Not archived; last push 2026-10-16.
- Releases: v0.3.2 (2026-03-16), v0.3.3 (2026-04-02), v0.4.0 (2026-08-03). Pre-1.0.
- README "Security & Governance": "Curate and approve agents, servers, and skills before
  company-wide deployment"; "Keep control of what gets published and promoted"; metadata "to help
  teams assess trustworthiness and security". Auth is delegated to agentgateway ("Enforce identity
  and access policies before requests reach your MCP servers", JWT validation). No scanning or
  scoring described in the README. CLI: `arctl`.

## CNCF sandbox application (primary)
- Issue cncf/sandbox#477 opened 2026-03-25 (same day as KubeCon EU announcement).
- TOC vote called 2026-09-22; closed 2026-09-29: PASSED, 81.82% in favour (9 for, 0 against,
  1 abstain, 1 not voted).
- Bot, 2026-09-29: "The TOC vote for agentregistry has passed! ... Next step: Please finalize the
  Contribution Agreement. This is required before official CNCF on-boarding can begin."
- As of 2026-10-20 the issue is still OPEN with label `contribution-agreement/unsigned`.
  cncf.io/projects/agentregistry/ returned 404 on 2026-10-20 (not yet listed).
- Overlap noted in thread (2026-09-10): Apicurio Registry (CNCF Sandbox, vote passed 2026-03-12)
  ships an AI-agent registry feature set.
- NOTE: SD Times (2026-04-17) and Cloud Native Now (2026-03-25) described agentregistry as already
  "donated ... as a sandbox project" in March 2026. The primary record shows that was the
  application date; acceptance vote passed only 2026-09-29.

## Launch press release (vendor, 2025-11-12, KubeCon NA Atlanta)
- "a centralized, trusted, and curated open source registry for AI applications and artifacts";
  publish, discover, version, share. Pitches security, governance and metadata management beyond
  the community MCP registry. Adds Agent Skills support. Third Solo agentic OSS project after
  kagent and agentgateway. Licence not stated in the release.

## Solo blog (vendor, 2026-08-20, Eitan Suez)
- Catalogs agents, MCP servers, skills, prompts, plugins, models. "sits on top of" npm/PyPI/OCI
  registries rather than replacing them. Problem framing: "nobody knows which ones are approved or
  how to run them consistently". Enterprise edition adds target runtimes (AWS Bedrock AgentCore) and
  discovery of agents already running in Azure AI Foundry / Microsoft Copilot Studio.

## Solo Enterprise for agentregistry docs (vendor; latest shown 2026.9.0 on 2026-10-20)
- Commercial "AI artifact platform" on the OSS project. Install on Kubernetes / EKS / air-gapped;
  Helm; bring-your-own PostgreSQL. Reference section lists "SBOMs and CVE scans" (contents not read).
- Security: every request must carry a JWT from an external OIDC IdP (Keycloak, Okta, Auth0
  examples). Role read from a JWT claim (default `Groups`). Superuser role (default `admin`)
  bypasses policy; everyone else has no access until an AccessPolicy grants actions
  (registry:read/publish/edit/deploy/delete/admin, runtime:invoke).
- Approval mode: create/update/delete by non-admins is "staged", "held in a pending state, invisible
  to other users, until an admin approves". Managed via UI, REST API, Python client.
- Runtime authorization: which MCP tools/agents a deployed agent may call. For kagent: AccessPolicy
  with Deployment principal, requires Solo Enterprise for Istio + agentgateway, enforced at the
  agentgateway waypoint. For Bedrock AgentCore: RuntimeAccessPolicy via a managed gateway.
- Discovery (read-only) of unmanaged agents in AWS Bedrock AgentCore, Azure AI Foundry, Microsoft
  Copilot Studio and Solo Enterprise for kagent — shown in an "Instances" view.
- Observability: OpenTelemetry traces; MCP gateway logs carry session ID, tool name, resource type.
  Audit-logs page exists under Compliance (not read).
- An "OSS vs. Enterprise" page is linked but returned 404 when fetched directly.
- No pricing published anywhere found.
