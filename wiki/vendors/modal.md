---
title: Modal
type: vendor
name: Modal
slug: modal
aka: [Modal Labs, Modal Sandboxes]
primary_category: ephemeral-environments
also_listed_in: []
website: https://modal.com/
founded: 2021
hq: New York, NY, USA
ownership_state: independent
owner: null
ownership_note: Venture-backed, late stage. $750M Series D at $15.75B post-money announced 2026-10-14, led by Accel with Kleiner Perkins and existing investors (Menlo, General Catalyst, Redpoint, Lux, Amplify, Bain Capital Ventures). Prior rounds were a $355M Series C at $4.65B (2026-05) and an $87M Series B at $1.1B (2025). Founded by Erik Bernhardsson (CEO) and Akshat Bubna (CTO).
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: Series D, $750M, 2026-10-14 (led by Accel; $15.75B post-money)
market_position: {ephemeral-environments: leader}
deployment_model: [saas]
form_factor: [api, sdk, platform]
data_leaves_tenancy: "true"
integrations: [aws-marketplace, gcp-marketplace, okta]
mcp_support: unverified
certifications: [soc2-type2, hipaa]
pricing_model: usage
fs_traction: unverified
target_customer: AI-native companies and engineering teams running inference, training, batch jobs and agent code execution
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [agent-sandbox, serverless, gpu, gvisor, code-execution, aie-nyc-2026]
sources:
  - {claim: "$750M Series D at $15.75B post-money, led by Accel, Kleiner Perkins joined; >$1B annualized run rate; Sandboxes ~$300M run rate; ~3B sandboxes, 1M concurrent; 200+ staff in NY/SF/Stockholm; named customers", url: "https://modal.com/blog/1-billion-annualized-run-rate-series-d", date: 2026-10-14, confidence: high}
  - {claim: "Series D corroborated by Bloomberg, Axios, TNW, SiliconANGLE (aggregated)", url: "https://ground.news/article/modal-ceo-ai-has-entered-a-new-era-of-software", date: 2026-10-16, confidence: medium}
  - {claim: "$355M Series C at $4.65B post-money (two tranches, first at $2.5B), led by Redpoint and General Catalyst, per Reuters", url: "https://pulse2.com/modal-labs-355-million-raised-at-4-65-billion-valuation-for-ai-infrastructure-platform/amp/", date: 2026-05-21, confidence: medium}
  - {claim: "Sandboxes run untrusted user/agent code on gVisor or VM runtime; 5 min default / 24 h max lifetime", url: "https://modal.com/docs/guide/sandbox", date: 2026-10-16, confidence: high}
  - {claim: "Sandbox egress open to public IPs by default; block_network, CIDR allowlist, SNI-based domain allowlist (beta)", url: "https://modal.com/docs/guide/sandbox-networking", date: 2026-10-16, confidence: high}
  - {claim: "SOC 2 Type II; HIPAA on Enterprise; TLS 1.3, encryption at rest, customer-supplied keys; function I/O retained up to 7 days", url: "https://modal.com/docs/guide/security", date: 2026-10-16, confidence: high}
  - {claim: "Plans and per-second rates; sandbox CPU/memory ~3x Function rates; Okta SSO, audit logs, HIPAA, AWS/GCP marketplace committed spend are Enterprise-only", url: "https://modal.com/pricing", date: 2026-10-16, confidence: high}
  - {claim: "Founded 2021 by Erik Bernhardsson and Akshat Bubna; New York HQ", url: "https://sacra.com/c/modal-labs/", date: 2026-10-16, confidence: medium}
---

# Modal

> Primary category: [ephemeral-environments](../categories/ephemeral-environments.md).

**One-liner** — A serverless compute cloud for AI workloads (GPU inference, training, batch jobs). Its **Sandboxes** product has become the largest disclosed business in disposable, isolated environments for running agent-generated code.

**What it does** — Modal lets engineers run Python (and, for sandboxes, JavaScript and Go clients) on its multi-cloud CPU and GPU fleet without managing servers, paying per second. Its main product line is serverless Functions for inference, training and batch work. **Modal Sandboxes**, launched in 2023, are containers created at runtime through `Sandbox.create` to run **untrusted user or agent code**: an LLM-written script, a repo checkout with its test suite, a CI step. Each sandbox picks one of two isolation runtimes. **gVisor**, Google's user-space kernel, intercepts the guest's system calls, and Modal describes it as strong isolation suitable for most workloads. The **VM** runtime gives the sandbox its own Linux kernel and is needed for Docker-in-sandbox or FUSE mounts. Default lifetime is 5 minutes, maximum 24 hours, with filesystem snapshots to carry state beyond that. Modal says sandboxes alone reached about a **$300M annualized run rate** by October 2026, roughly 3 billion sandboxes created, with scale to a million concurrent (company claims).

**How agent code sandboxes differ from the dev environments in this category.** [github-codespaces](github-codespaces.md) and [azure-dev-boxes](azure-dev-boxes.md) give a *human developer* a long-lived workstation, provisioned in minutes and billed per seat or hour. A Modal Sandbox is created *by a program* inside an agent loop, often lives for seconds, can number in the thousands at once, and treats the code inside as hostile. That last point is the important one: the isolation runtime (gVisor or VM) and the egress policy are the security control, not a convenience. The category goal, disposable compute with nothing persistent to compromise, is the same. The owner is the agent-platform or quant-engineering team, not developer-experience.

**Naming / provenance** — Legal/brand name appears as both **Modal** and **Modal Labs**. Founded in **2021** by Erik Bernhardsson (CEO; previously Spotify and Better.com) and Akshat Bubna (CTO). Headquartered in New York, with offices in San Francisco and Stockholm. Not to be confused with the generic "modal" UI term or unrelated companies of the same name.

**Ownership & viability** — `independent`, late-stage venture. **$750M Series D at $15.75B post-money, announced 2026-10-14**, led by Accel with Kleiner Perkins. All existing investors participated: Menlo Ventures, General Catalyst, Redpoint, Lux Capital, Amplify Partners and Bain Capital Ventures. That came five months after a **$355M Series C at $4.65B (May 2026**, led by Redpoint and General Catalyst; reported as two tranches, the first priced at $2.5B). The Series C in turn followed an **$87M Series B at $1.1B (2025)**. The company says it passed a **$1B annualized run rate**, and it has 200+ staff. Total funding raised is not stated by the company and is left null here rather than summed from press reports. Viability risk is low for a vendor in this category. The realistic risks are price (the growth is GPU- and agent-driven, and margins depend on capacity contracts) and strategic absorption by a hyperscaler or AI lab. At this valuation that is a large deal, not a tuck-in.

**Positioning & differentiators** — Labelled `leader` in this category: with a disclosed ~$300M sandbox run rate and named AI-lab-scale users, Modal is the largest identifiable agent-sandbox provider. That claim is limited to agent sandboxes, not human dev workstations, where Codespaces and Dev Boxes dominate.
- **vs. [daytona](daytona.md):** Daytona does only sandboxes, on its own bare metal with Sysbox-hardened containers, and emphasises long-lived stateful machines (pause, fork, Windows desktops). Modal isolates with gVisor or a VM runtime and has a much bigger balance sheet. It also puts sandboxes next to GPU inference and batch compute on one bill. Choose on isolation model, statefulness needs and data-residency options.
- **vs. [cloudflare-workers](cloudflare-workers.md):** Workers are V8 isolates for request handlers. A Modal Sandbox is a full Linux userland with arbitrary binaries and optional GPUs.
- **vs. [github-codespaces](github-codespaces.md) / [azure-dev-boxes](azure-dev-boxes.md):** a different job (see above), not a substitute.
- **Breadth is both the strength and the catch.** Sandboxes run on the same platform as Modal's inference and training. That is convenient if Modal is already the ML platform, and more vendor surface to review if all you want is a code sandbox.

**Who should choose them / anti-fit** — Fits a firm that **builds its own agents that execute generated code**, or runs ML research on serverless GPUs and wants sandboxes on the same platform. Example: a quant research platform whose internal agent writes and runs analysis code, or an eval harness that needs thousands of throwaway environments. **Anti-fit:** firms without a code-execution workload. Also anti-fit: firms whose policy requires that code and data never leave their own cloud account, because no self-hosted or BYOC option was found. Small teams that need SSO or audit logs will find those gated to Enterprise.

**Known weaknesses / gotchas** —
- **Egress is open by default.** Sandboxes can reach any public IP unless you set `block_network`, a CIDR allowlist, or the domain allowlist. The domain allowlist is beta, matches on TLS SNI without decrypting, and Modal itself warns that domain fronting can bypass it. It recommends a sidecar proxy. Any sandbox holding credentials or firm data needs an explicit egress policy.
- **No in-tenancy option found.** Everything runs on Modal's multi-cloud fleet. By default, inputs route through `us-east` and payloads over 2 MiB are staged in `us-east` object storage even when a container region is pinned. Check this against data-residency obligations.
- **Pricing multipliers stack.** Sandbox CPU and memory cost roughly 3x Function rates. Non-preemptible execution is 3x and region pinning 1.15–1.75x on top. Model costs on realistic agent workloads before committing.
- **gVisor compatibility.** gVisor does not implement every Linux syscall. Some workloads must use the VM runtime, and GPU sandboxes are gVisor-only.

**Deployment & data handling** — **SaaS only** (no self-hosted or BYOC found). Code, files and outputs placed in a sandbox are processed on Modal's infrastructure across multiple unnamed clouds, hence `data_leaves_tenancy: "true"`. Container regions are selectable (us/eu/ap and narrower, plus jp/uk/ca) for a price multiplier. TLS 1.3 in transit, encryption at rest, and customer-supplied encryption keys are available. Retention: Function inputs and outputs up to 7 days; volumes and images until deleted. Sandbox-specific log retention is **unverified**. Inbound access is off by default and uses encrypted tunnels, inbound CIDR allowlists and connect tokens.

**Integrations & partnerships** — Python SDK (primary) and JavaScript/Go clients for sandboxes. **Enterprise customers can use committed spend on the AWS and GCP marketplaces**, a procurement shortcut. Okta SSO on Enterprise. Agent-framework integrations and MCP support were **not verified**. The page records `mcp_support: unverified` rather than guess. Named customers include Cognition, Ramp, Linear, Hebbia, DoorDash, Runway, Suno and Physical Intelligence.

**Compliance & FS traction** — **SOC 2 Type II** on all plans (report via trust center). **HIPAA** on Enterprise, with some products out of scope for PHI. GDPR DPA available. ISO 27001 not mentioned. **No named buy-side or bank customers found.** Ramp (corporate cards) and Hebbia (an AI research tool sold into finance) are fintech or vendor-to-finance names, not regulated asset managers.

**Commercial** — Usage-based, billed per second. Starter $0/month (+$30 credit), Team $250/month (+$100 credit), Enterprise custom with volume discounts. Sandbox CPU about $0.00003942/core-second and memory about $0.00000667/GiB-second. Multipliers apply for non-preemptible execution (3x) and region pinning (1.15–1.75x). Source: pricing page, 2026-10-16.

## Open questions

- Any BYOC or dedicated/single-tenant deployment for regulated customers?
- Which clouds and regions physically host sandboxes; sub-processor list.
- Sandbox log and snapshot retention; whether sandbox stdout/stderr is retained like Function I/O.
- MCP and agent-framework integrations (first-party or community).
- Any FS customers; ISO 27001 status.
- Total funding to date (company has not stated it).

## Sources

- [Series D: $1B in annualized run rate (Modal blog, 2026-10-14)](https://modal.com/blog/1-billion-annualized-run-rate-series-d) — fetched 2026-10-16 — supports: Series D terms, run rates, headcount, customers; confidence: high (vendor, corroborated)
- [Ground News aggregation of Series D coverage (Bloomberg, Axios, TNW)](https://ground.news/article/modal-ceo-ai-has-entered-a-new-era-of-software) — fetched 2026-10-16 — supports: independent corroboration of Series D; confidence: medium
- [Modal Labs $355M at $4.65B (Pulse 2.0, citing Reuters)](https://pulse2.com/modal-labs-355-million-raised-at-4-65-billion-valuation-for-ai-infrastructure-platform/amp/) — fetched 2026-10-16 — supports: Series C; confidence: medium
- [Modal docs: Sandboxes](https://modal.com/docs/guide/sandbox), [Sandbox networking](https://modal.com/docs/guide/sandbox-networking), [Security](https://modal.com/docs/guide/security), [Region selection](https://modal.com/docs/guide/region-selection) — fetched 2026-10-16 — supports: isolation runtimes, egress controls, certifications, retention, residency; confidence: high (vendor docs)
- [Modal pricing](https://modal.com/pricing) — fetched 2026-10-16 — supports: plans, rates, Enterprise gating; confidence: high
- [Sacra: Modal Labs](https://sacra.com/c/modal-labs/) — fetched 2026-10-16 — supports: founding, founders, HQ; confidence: medium
- Cached: `raw/sources/2026-10-16--modal--series-d-and-funding.md`, `raw/sources/2026-10-16--modal--sandbox-docs-security-pricing.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
