# Google Cloud Workstations — architecture, private clusters/VPC-SC, audit logging, release notes, agent mode

- URL: https://docs.cloud.google.com/workstations/docs/overview
- URL: https://docs.cloud.google.com/workstations/docs/architecture
- URL: https://docs.cloud.google.com/workstations/docs/configure-private-clusters
- URL: https://docs.cloud.google.com/workstations/docs/audit-logging
- URL: https://docs.cloud.google.com/workstations/docs/customize-container-images
- URL: https://docs.cloud.google.com/workstations/docs/release-notes
- URL: https://docs.cloud.google.com/workstations/docs/agent-optimized-development (via search summary)
- URL: https://cloud.google.com/workstations/pricing (fetch truncated — no rates captured)
- Fetched: 2026-10-26
- Good for: where workstations run, network isolation options, what is and isn't audited, compliance
  coverage dates, agent-specific features. All Google-published docs.

## Architecture
- Cluster (region + VPC in your project; Google-managed controller and gateway), configuration (template:
  machine type, persistent disk, container image, IDE), workstation.
- Workstations "run on Compute Engine VMs in your project, with a persistent disk attached"; "When a
  workstation stops, its ephemeral VM is deleted along with all workstation runtime data." Persistent home
  directory survives. Idle timeout and running timeout set in the config. IAM grants per team/developer.
- Controller connects to your VPC via Private Service Connect; default is a public cluster gateway; a
  "fully private gateway" restricts access to endpoints in your private network.
- IDEs: Code OSS (browser), Base Editor, local VS Code, JetBrains; SSH.

## Private clusters / VPC Service Controls
- Private cluster "prevents connections to your workstations from outside your VPC service perimeter";
  needs two PSC endpoints. Inside a VPC-SC perimeter: restrict Compute Engine API too; public clusters
  blocked; turn off public IPs (org policy constraints/compute.vmExternalIpAccess); egress rules needed for
  image streaming and preconfigured IDE images. "Access control based on device, external IP address, or
  location is not supported."
- Egress from the VM otherwise follows your VPC firewall/NAT config (standard GCP networking).

## Hardening
- `CLOUD_WORKSTATIONS_CONFIG_DISABLE_SUDO=true` turns off sudo in the container; docs warn users "might
  be able to obtain root privileges on the underlying VM".
- CMEK for persistent disks (beta as of 2023-02-07 release note; current status not rechecked).

## Audit logging
- Admin Activity: create/delete/start/stop/suspend/update of workstations, clusters, configs; SetIamPolicy.
- Data Access (ADMIN_READ): GenerateAccessToken, get/list, GetIamPolicy.
- Covers API methods only; in-workstation activity not covered by audit logs on this page.

## Release notes (selected)
- 2023-05-10: GA with SLA.
- 2026-04-13: /google/scripts/keep_alive.sh to prevent idle timeouts.
- 2026-05-08: workstation authorization URL for clusters.
- 2026-05-29: Antigravity CLI in preconfigured base images.
- 2026-07-08: Data Agent Toolkit extension installed by default in Code OSS.
- 2026-08-12: Compute Engine suspend and resume (Preview) via IdleAction.
- 2026-08-26: "Cloud Workstations supports an agent-optimized development experience" — suspend on idle
  instead of stop + keep-alive lifecycle hooks so long-running agents (Antigravity CLI, Claude Code) don't
  lose context to idle timeouts.
- 2026-09-23: regional endpoints GA.
- 2026-09-24: covered under Google Cloud HIPAA BAA.
- 2026-10-05: Assured Workloads control packages (FedRAMP, IL2/IL4/IL5, US and EU data boundary).
- 2026-10-20: automatic failover for boost configurations (Preview).
