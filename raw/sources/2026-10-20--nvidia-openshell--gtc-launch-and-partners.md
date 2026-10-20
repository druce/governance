# NVIDIA OpenShell — GTC launch (March 2026), NemoClaw, CrowdStrike and Cisco integrations

- URL: https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell
- URL: https://www.businesswire.com/news/home/20260316048931/en (CrowdStrike release; via search summary, not fully read)
- URL: https://blogs.cisco.com/ai/cisco-announces-defenseclaw
- URL: https://heise.de/-11213313 (via search summary)
- Fetched: 2026-10-20
- Good for: announce date, original framing (sandbox + policy engine + privacy router), Agent Toolkit placement, launch security partners.

## NVIDIA Technical Blog, 2026-03-16 (Ali Golshan, Alex Watson, John Myers)
- "Based on Apache 2.0, OpenShell sits between your agent and your infrastructure." Part of NVIDIA Agent Toolkit. Runs OpenClaw, Claude Code, Codex, Cursor, OpenCode unmodified.
- Components at launch: sandbox ("not generic container isolation"), policy engine (filesystem, network, process), privacy router.
- "Instead of relying on behavioral prompts, it enforces constraints on the environment the agent runs in"; evaluates actions "at the binary, destination, method, and path level"; "Policy updates happen live at sandbox scope as developer approvals are granted"; audit trail of allow/deny.
- Privacy router keeps sensitive context on local open models, sends to frontier models only when policy allows: "The router makes decisions based on your cost and privacy policy, not the agent's."
- NemoClaw announced same day at GTC as open-source stack running OpenClaw always-on assistants on OpenShell. Heise: NVIDIA says NemoClaw early-stage, not production-ready.

## Launch security partners (secondary coverage, March 2026)
- Multiple outlets: NVIDIA working with Cisco, CrowdStrike, Google, Microsoft Security (some add TrendAI) on OpenShell compatibility.
- CrowdStrike (press release 2026-03-16, "Secure-by-Design AI Blueprint"): Falcon embedded with OpenShell; Falcon AIDR planned to monitor prompts/responses/agent actions; endpoint coverage for local agents on DGX Spark/Station; identity controls. Independent coverage (Let's Data Science) frames it as an architecture/integration plan, not GA.
- Cisco DefenseClaw (blog 2026-03-23, DJ Sampath): "the agentic governance layer that sits on top of OpenShell"; "OpenShell provides the infrastructure-level sandbox that OpenClaw never had." Blocking an MCP server removes its endpoint from the sandbox allow-list so OpenShell denies connections. Adds pre-install scanning (skill-scanner, mcp-scanner, a2a-scanner, CodeGuard, AI BOM), runtime content scanning, Splunk telemetry. Repo github.com/cisco-ai-defense/defenseclaw, slated 2026-03-27. Licence not named in post.
