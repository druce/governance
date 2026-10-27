---
title: Google Cloud Workstations
type: vendor
name: Google Cloud Workstations
slug: google-cloud-workstations
aka: [Cloud Workstations, GCP Cloud Workstations]
primary_category: ephemeral-environments
also_listed_in: []
website: https://cloud.google.com/workstations
founded: 2023
hq: Mountain View, CA, USA
ownership_state: public
owner: Alphabet Inc
ownership_note: 'First-party Google Cloud service of Alphabet Inc. (NASDAQ: GOOGL/GOOG). GA 2023-05-10. No ownership change.'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {ephemeral-environments: platform-module}
deployment_model: [in-tenant]
form_factor: [platform]
data_leaves_tenancy: "false"
integrations: [vpc-service-controls, private-service-connect, cloud-iam, cloud-audit-logs, artifact-registry, vscode, jetbrains, gemini-code-assist, antigravity-cli, assured-workloads]
mcp_support: unverified
certifications: [hipaa-baa]
pricing_model: usage
fs_traction: unverified
target_customer: Google Cloud customers who want managed developer workstations inside their own GCP project and VPC
last_verified: 2026-10-26
verify_after: 2027-04-26
tags: [first-party, google-cloud, dev-environments, cloud-development-environments, vpc-service-controls, coding-agents]
sources:
  - {claim: "Architecture: VMs in customer project/VPC; ephemeral VM deleted on stop; persistent home disk; idle/running timeouts; IAM", url: "https://docs.cloud.google.com/workstations/docs/overview", date: 2026-10-26, confidence: high}
  - {claim: "Google-managed controller and gateway; PSC to customer VPC; public gateway by default, fully private gateway option", url: "https://docs.cloud.google.com/workstations/docs/architecture", date: 2026-10-26, confidence: high}
  - {claim: "Private clusters inside VPC-SC perimeter; disable public IPs; no device/IP/location access control", url: "https://docs.cloud.google.com/workstations/docs/configure-private-clusters", date: 2026-10-26, confidence: high}
  - {claim: "Audit logs cover API control-plane methods (create/start/stop, GenerateAccessToken), not in-workstation activity", url: "https://docs.cloud.google.com/workstations/docs/audit-logging", date: 2026-10-26, confidence: high}
  - {claim: "GA 2023-05-10; agent-optimized experience 2026-08-26; HIPAA BAA 2026-09-24; Assured Workloads control packages 2026-10-05; Antigravity CLI 2026-05-29", url: "https://docs.cloud.google.com/workstations/docs/release-notes", date: 2026-10-26, confidence: high}
  - {claim: "Suspend-on-idle plus keep-alive hooks for long-running coding agents (Antigravity CLI, Claude Code)", url: "https://docs.cloud.google.com/workstations/docs/agent-optimized-development", date: 2026-10-26, confidence: medium}
---

# Google Cloud Workstations

> Primary category: [ephemeral-environments](../categories/ephemeral-environments.md).

**One-liner** — Google Cloud's managed developer workstations. Developers get a container-based dev environment on a VM that runs in **the firm's own GCP project and VPC**. Admins define them centrally, they shut down on idle, and they can be fenced inside a VPC Service Controls perimeter. It is the Google Cloud counterpart to [github-codespaces](github-codespaces.md) and Microsoft's former [azure-dev-boxes](azure-dev-boxes.md).

**What it does** — Admins create a **cluster** (one region, attached to one of your VPCs) and **configurations** (templates for machine type, container image, IDE, persistent disk, and idle and running timeouts). Developers then start **workstations** from those configurations. Each workstation is a container on a Compute Engine VM in your project. The VM is **deleted when the workstation stops**, along with all runtime data. Only the optional persistent home directory survives. Supported IDEs are Code OSS in the browser, local VS Code, JetBrains IDEs, and SSH. Gemini Code Assist is built in, and since 2026-05-29 the preconfigured images include Google's Antigravity CLI.

**Why a CTO would use it for isolation** — Most of the [trust-zone-segmentation](../categories/trust-zone-segmentation.md) controls come from GCP primitives a Google Cloud shop already runs:

- **Zone-scoped network.** Each cluster attaches to a VPC you choose, so a red-zone cluster and a yellow-zone cluster can sit on different VPCs with different firewall and NAT rules. A **private cluster** inside a **VPC Service Controls** perimeter blocks connections from outside the perimeter. Combined with an org policy that forbids external IPs, it keeps workstation traffic and Google API calls inside the perimeter. That is the standard GCP pattern for stopping data from leaving.
- **Short-lived by default.** The VM is rebuilt from the configuration on every start. Idle and running timeouts stop forgotten workstations, so drift and stray credentials do not accumulate.
- **Central configuration.** Developers choose from configurations admins publish, and IAM controls who can use which ones. Root inside the container can be turned off (`CLOUD_WORKSTATIONS_CONFIG_DISABLE_SUDO`).
- **Agent support (2026).** On **2026-08-26** Google added an "agent-optimized development experience". It suspends the VM on idle instead of deleting it, and uses keep-alive hooks so long-running coding agents (Antigravity CLI and Claude Code are named) are not killed by idle timeouts. This is a *lifecycle* feature for agents. It does **not** add any control specific to agents. Unlike [coder](coder.md)'s Agent Firewall or [docker-sandboxes](docker-sandboxes.md)' egress proxy, it has no separate egress policy for the agent process. The agent gets whatever network access the workstation has.

**Naming / provenance** — Announced as "Cloud Workstations" and **GA on 2023-05-10** with an SLA. It is a product of Google Cloud (Alphabet). The slug is the product name, following the [github-codespaces](github-codespaces.md) and [azure-dev-boxes](azure-dev-boxes.md) precedent, because it is the unit people shop for. It is different from Vertex AI Workbench, which provides managed notebooks for data science on separate infrastructure.

**Ownership & viability** — First-party Google Cloud service of Alphabet Inc. (public, NASDAQ: GOOGL/GOOG). Development is active. The 2026 release notes show steady feature work: regional endpoints GA (2026-09-23), HIPAA BAA coverage (2026-09-24), Assured Workloads control packages including FedRAMP, IL2/IL4/IL5 and US and EU data boundaries (2026-10-05), and boost-configuration failover in Preview (2026-10-20). There are no signs of the product being sunset. Contrast Azure Dev Box, which closed to new customers in 2025.

**Positioning & differentiators** — `platform-module`: a feature of Google Cloud, bought with and governed by the rest of GCP, not a standalone product.

- **vs. [github-codespaces](github-codespaces.md):** Codespaces VMs run in GitHub's Azure infrastructure. Cloud Workstations VMs run **in your GCP project and VPC**, under your VPC Service Controls, firewall and logging. That is a meaningful difference for firms that keep proprietary code and data in GCP.
- **vs. [coder](coder.md):** both keep workspaces in your network. Cloud Workstations is fully managed, so there is no control plane to run, but it is GCP-only and has no LLM gateway or agent-level egress control. Coder runs on any cloud, on-prem or air-gapped, and adds AI Gateway and Agent Firewall, but you operate it yourself.
- **vs. agent sandboxes ([daytona](daytona.md), [modal](modal.md)):** Cloud Workstations are workstations for people, lasting hours or days, that agents can also work in. They are not created in large numbers by API, one per tool call.

**Who should choose them / anti-fit** — Fits a **GCP-centric firm**, especially one whose research data already sits in BigQuery or GCS behind VPC Service Controls. Workstations inside the same perimeter keep developers and their coding agents next to the data and away from the internet without adding a vendor. **Anti-fit:** AWS- or Azure-primary firms (it is GCP-only); firms that need agent-specific egress allowlists or a central record of prompts and tool calls (add a gateway, or look at Coder); firms that need on-prem or air-gapped workspaces; and anyone hoping the workstation audit log records what happens inside the workstation.

**Known weaknesses / gotchas** —
- **The audit log covers the control plane only.** Cloud Audit Logs record creating, starting, stopping and updating workstations, IAM changes, and `GenerateAccessToken`. They do not record commands, files or network activity inside the workstation. For that you need VPC Flow Logs, VPC-SC violation logs, container output logging, or an agent or gateway inside the workstation.
- **Default gateway is public.** The cluster gateway is public unless you configure a private cluster with Private Service Connect endpoints. That takes deliberate setup, and the perimeter needs specific egress rules for image streaming and preconfigured IDE images.
- **Coarse access control in perimeter mode.** Private clusters cannot apply access control by device, IP or location. Access depends only on whether the connecting network is inside the perimeter.
- **Turning off sudo does not fully contain root.** Google's own docs warn that users "might be able to obtain root privileges on the underlying VM". Treat the VM, not the container, as the security boundary.
- **Persistent home directories persist.** The VM is short-lived, but `$HOME` is not, so credentials and data written there survive restarts. Suspend-on-idle for agents keeps even more state around. That is useful for agents but reduces the short-lived property this category is about.

**Deployment & data handling** — Managed service whose **workstation VMs and disks run in the customer's GCP project and VPC** (`in-tenant`). The cluster controller and gateway are Google-managed and connect to your VPC through Private Service Connect. Source code and data stay in your Google Cloud tenancy, so `data_leaves_tenancy: "false"`. The caveat is that client traffic passes through the Google-managed cluster gateway, which can be made private. Model calls from Gemini Code Assist or from an agent you install go wherever that tool sends them. The workstation does not change that. Regional endpoints (GA 2026-09-23) and Assured Workloads data-boundary packages help with data-residency requirements.

**Integrations & partnerships** — VPC Service Controls, Private Service Connect, Cloud IAM, Cloud Audit Logs, Artifact Registry for custom images, CMEK for persistent disks (beta in 2023; current status not rechecked). IDEs: Code OSS, VS Code, JetBrains. AI: Gemini Code Assist, Antigravity CLI, and the Data Agent Toolkit extension installed by default since 2026-07-08. MCP support was not verified.

**Compliance & FS traction** — Covered under the Google Cloud HIPAA BAA since 2026-09-24. Since 2026-10-05 it supports Assured Workloads control packages (FedRAMP, IL2/IL4/IL5, US and EU data boundaries). Google Cloud's platform-wide SOC and ISO attestations were not checked for this product's scope on this pass. No named financial-services customers of Cloud Workstations were found.

**Commercial** — Usage-based Google Cloud billing for the underlying VMs and disks, plus any service fees. The pricing page could not be read on this pass, so management-fee and cluster-fee rates are **unverified**.

## Open questions

- Current pricing structure: management fee per workstation-hour, cluster fee, rates.
- Whether CMEK for persistent disks is GA.
- Whether there is a supported way to apply an egress allowlist per agent process inside a workstation, or whether network policy is only per VPC.
- Named FS customers.
- Which of Google Cloud's SOC 2 and ISO 27001 certifications explicitly list Cloud Workstations in scope.

## Sources

- [Cloud Workstations overview](https://docs.cloud.google.com/workstations/docs/overview). Fetched 2026-10-26. Supports: architecture, deletion of the VM on stop, timeouts, IDEs. Confidence: high.
- [Architecture](https://docs.cloud.google.com/workstations/docs/architecture). Fetched 2026-10-26. Supports: VMs in the customer's project, Google-managed controller and gateway, PSC, private gateway option. Confidence: high.
- [Configure VPC Service Controls and private clusters](https://docs.cloud.google.com/workstations/docs/configure-private-clusters). Fetched 2026-10-26. Supports: perimeter requirements, public-IP constraint, access-control limits. Confidence: high.
- [Audit logging](https://docs.cloud.google.com/workstations/docs/audit-logging). Fetched 2026-10-26. Supports: which operations are and are not audited. Confidence: high.
- [Customize container images](https://docs.cloud.google.com/workstations/docs/customize-container-images). Fetched 2026-10-26. Supports: the disable-sudo option and its caveat. Confidence: high.
- [Release notes](https://docs.cloud.google.com/workstations/docs/release-notes). Fetched 2026-10-26. Supports: GA date and dated 2026 features. Confidence: high.
- [Agent-optimized development](https://docs.cloud.google.com/workstations/docs/agent-optimized-development). Via search summary, 2026-10-26. Supports: suspend-on-idle and keep-alive for agents. Confidence: medium.
- Cached: `raw/sources/2026-10-26--google-cloud-workstations--docs.md`

## History

- [2026-10-26] Page created via wiki-create + wiki-research. Product slug `google-cloud-workstations`, consistent with the github-codespaces and azure-dev-boxes precedent.
