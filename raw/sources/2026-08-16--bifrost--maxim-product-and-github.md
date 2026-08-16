# Bifrost (Maxim AI) — product page + GitHub repo

- URL: https://www.getmaxim.ai/bifrost (vendor product page) + https://github.com/maximhq/bifrost (repo README) + https://api.github.com/repos/maximhq/bifrost (repo metadata)
- Fetched: 2026-08-16
- Good for: what Bifrost is, provider/model counts, governance and MCP features,
  benchmark claims, license, repo traction, OSS-vs-enterprise split.

## Facts

**Identity.** Bifrost is an **open-source AI gateway written in Go**, built and
maintained by **Maxim AI** (`maximhq`), the eval/observability company already
covered at `wiki/vendors/maxim-ai.md`. Marketed as "the fastest enterprise AI
gateway." Product page lives on getmaxim.ai; docs live on a separate domain,
`docs.getbifrost.ai` (and `getbifrost.ai` resolves).

**Repo metadata (GitHub API, 2026-08-16).**
- `maximhq/bifrost`, created **2025-03-19**, last push 2026-08-16 (active).
- **7,339 stars, 1,049 forks, 870 open issues.** Not archived.
- License: **Apache-2.0**.
- Language: **Go**.
- Releases are per-component tags, e.g. `transports/v1.6.11` (2026-08-14),
  `plugins/telemetry/v1.5.37`, `plugins/semanticcache/v1.5.37` — a monorepo with
  independently versioned transports/plugins, not one product-level semver.
- Repo description: "Fastest enterprise AI gateway (50x faster than LiteLLM) with
  adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs
  overhead at 5k RPS."

**What it does.**
- Unified **OpenAI-compatible API** in front of many providers. Counts are
  inconsistent across vendor surfaces: product page says "8+ providers and 1000+
  AI models"; README says "23+ AI providers"; docs say "20+ providers". Named:
  OpenAI, Anthropic, AWS Bedrock, Google Vertex, Azure, Cerebras, Cohere, Mistral,
  Ollama, Groq.
- Drop-in SDK replacement (OpenAI/Anthropic/LangChain clients repoint at it).
- Automatic **failover** and load balancing across providers/keys; **semantic
  caching**; multimodal (text, image, audio, streaming).
- **Governance:** "virtual keys" are the primary governance entity — hierarchical
  budgets and rate limits across virtual keys → teams → customers, plus
  fine-grained access control and usage/cost tracking.
- **Observability:** Prometheus metrics and **OpenTelemetry** out of the box, plus
  a built-in dashboard/web UI and a first-party Maxim integration.
- **Plugins:** middleware written in **Go or WebAssembly** (analytics, governance,
  semantic cache, telemetry, a request mocker for testing).
- Deployment: `npx` quick start, Docker, or embed the **Go SDK** in-process.

**OSS vs enterprise split (per docs.getbifrost.ai, 2026-08-16).** Enterprise-only:
- clustering / HA,
- adaptive load balancing with predictive scaling,
- **MCP Gateway** (autonomous tool execution),
- content-safety **guardrails** (AWS/Azure/Google backends),
- IdP integration (Okta/Entra), RBAC, VPC isolation, audit logging,
- Datadog connector and automated log export to data lakes.

> Note the tension: the marketing page advertises "built-in MCP gateway" and
> "real-time model protection that blocks unsafe outputs" without flagging them as
> paid; the docs place both behind the enterprise license. Recorded as a gotcha.

**Benchmark claims (all vendor-run, no independent replication found).**
- Product page: "54x faster" P99 vs LiteLLM, "9.5x higher" throughput, "68% less"
  memory; headline specs "20 µs" added latency, "5,000 req/s", "3.3 GB" peak memory.
- README/docs: "**11 µs** added overhead at 5,000 RPS" on an AWS **t3.xlarge**,
  100% success rate at 5k RPS, 1.67 µs average queue wait, 24% overall latency
  reduction.
- Repo description says "50x faster than LiteLLM" and "<100 µs overhead at 5k RPS".
  The 20 µs / 11 µs / <100 µs figures are not reconciled anywhere on vendor
  surfaces.

**Traction claim.** Product page: "over 1,000+ teams use Bifrost." Vendor claim,
unverified.

**Commercial.** Three tiers: open source (self-hosted, Apache-2.0), enterprise
(managed), and edge. Enterprise offers a 14-day free trial. No list prices
published.

**Parent ownership.** Maxim AI: founded 2023 (Vaibhavi Gangwar, Akshay Deo), SF +
India, **$3M seed announced 2024-06-18** led by Elevation Capital. Searches on
2026-08-16 found **no funding round after that seed** and no M&A. Consistent with
the existing `maxim-ai.md` page.
