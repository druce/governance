# Daytona — docs, trust center, pricing, network limits, GitHub repo status

- URL: https://www.daytona.io/docs/en/
- URL: https://www.daytona.io/docs/en/network-limits/
- URL: https://www.daytona.io/docs/en/bring-your-own-compute/ (via search summary)
- URL: https://trust.daytona.io/
- URL: https://www.daytona.io/pricing
- URL: https://github.com/daytonaio/daytona and https://api.github.com/repos/daytonaio/daytona
- Fetched: 2026-10-16
- Good for: product capabilities, egress controls, BYOC, certifications, sub-processors, pricing,
  open-source status. Vendor-published except the GitHub API metadata.

## Docs (vendor)
- Sandboxes: "full composable computers" with "complete isolation, a dedicated kernel, filesystem,
  network stack, and allocated vCPU, RAM, and disk"; <90 ms start; OCI/Docker compatible; stateful
  snapshots; volumes. SDKs: TypeScript, Python, Ruby, Go, Java; plus API and CLI. Pages exist for MCP
  Server, SSO, Audit Logs, Secrets, Regions, BYOC (contents not all fetched).
- Note: "dedicated kernel" in docs vs Sysbox containers per founder — not reconciled.

## Network limits (vendor docs)
- Tier 1–2 orgs: restricted egress, org-level rules override; essential services (package registries,
  git hosts, model providers) reachable.
- Tier 3–4: full internet by default; per-sandbox `networkAllowList` (≤10 IPv4 CIDRs),
  `domainAllowList` (≤100 domains, wildcards), or `networkBlockAll`. Runtime update on Tier 3–4.
  `outboundProxyUrl` to route HTTP(S) via an upstream proxy (pair with domain allowlist to prevent bypass).

## BYOC (vendor docs, via search)
- Run sandboxes on customer infrastructure ("custom regions" with own runner nodes) while Daytona's
  control plane manages them. Built-in shared regions: US and EU. Custom regions invite-only/experimental
  as of Jan 2026; enterprise feature per pricing page.

## Trust center
- Lists GDPR, HIPAA, ISO/IEC 27001, SOC 2. SOC 2 Type II report issued 2026-07-28 by Insight Assurance,
  unqualified opinion, period 2025-12-16 to 2026-03-15, Security/Availability/Confidentiality.
- Sub-processors: Leaseweb, Latitude.sh, OVHcloud, Stripe, AWS.
- CVE-2026-31431 advisory says the "Sysbox runtime isolation boundary" "was not breached".

## Pricing (vendor)
- Usage-based, per second: vCPU $0.0504/h; memory $0.0162/GiB-h; storage $0.000108/GiB-h (5 GiB free);
  Windows $0.0858/vCPU-h; preemptible GPUs $0.57–$4.08/h. $200 free credit; startups up to $50k.
- Enterprise (contact sales): larger limits, SSO, audit logs, BYOC.

## GitHub repo (daytonaio/daytona)
- Description: "Secure and Elastic Infrastructure for Running AI-Generated Code". ~71.5k stars.
- README notice: "This repository is no longer maintained"; core development moved to a private
  codebase as of June 2026. GitHub API: `archived: true` (banner: archived 2026-10-03), last push
  2026-07-24, created 2024-02-06. API reports no detected licence; LICENSE file present at v0.190.0
  (AGPL-3.0 per founder on Latent Space).
