# Modal — Sandboxes docs, networking, security page, regions, pricing

- URL: https://modal.com/docs/guide/sandbox
- URL: https://modal.com/docs/guide/sandbox-networking
- URL: https://modal.com/docs/guide/security
- URL: https://modal.com/docs/guide/region-selection
- URL: https://modal.com/pricing
- Fetched: 2026-10-16
- Good for: isolation runtime, egress controls, certifications, data retention, data residency, pricing. Vendor docs.

## Sandboxes
- "Secure containers for running untrusted user or agent code", created at runtime via `Sandbox.create`.
- Two runtimes: **gVisor** (default-suitable, "strong isolation") or **VM** (own Linux kernel; needed for
  Docker-in-sandbox, FUSE). GPU sandboxes gVisor only.
- Lifetime default 5 min, max 24 h; idle_timeout; filesystem snapshots to persist beyond 24 h.
- SDK examples: Python, JavaScript, Go.
- Use cases: LLM-generated code execution, isolated envs for untrusted code, CI, test suites.

## Networking
- Default: no inbound, no access to your Modal resources; **outbound to any public IP allowed by default**.
- `block_network=True`; `outbound_cidr_allowlist`; `outbound_domain_allowlist` (beta; TLS/443 SNI-based,
  no decryption; domain fronting can bypass — use a Sidecar proxy). Runtime policy updates (alpha).
- Inbound: tunnels (encrypted/unencrypted/h2), inbound CIDR allowlist, connect tokens; custom domains on Team/Enterprise.

## Security page
- Containers isolated with "gVisor or microVMs".
- SOC 2 Type II (report on request); HIPAA on Enterprise (some products out of scope for PHI); GDPR DPA. ISO not mentioned.
- TLS 1.3 in transit, encryption at rest; customer-supplied encryption keys available.
- Retention: Function inputs/outputs up to 7 days; volumes/images until deleted.
- No self-hosted / BYOC option mentioned anywhere fetched. Runs "across multiple different clouds".

## Regions
- `region=` on functions and `Sandbox.create` (us/eu/ap, narrower, jp/uk/ca). Inputs route via us-east
  by default; `routing_region` selectable; >2 MiB I/O still staged in us-east object storage.
  Multiplier 1.15x (broad) to 1.75x (narrow).

## Pricing
- Starter $0 (+$30/mo credit), Team $250/mo (+$100 credit), Enterprise custom.
- Sandbox CPU $0.00003942/core-s (~3x standard Function CPU); memory $0.00000667/GiB-s.
- Non-preemptible 3x; region 1.15–1.75x. Enterprise-only: Okta SSO, HIPAA, audit logs, marketplace committed spend (AWS, GCP).
- SOC 2 on all plans.
