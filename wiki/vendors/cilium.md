---
title: Cilium (Isovalent / Cisco)
type: vendor
name: Cilium (Isovalent / Cisco)
slug: cilium
aka: [Cilium, Isovalent, Cisco Isovalent, Hubble, Tetragon, Isovalent Enterprise]
primary_category: trust-zone-segmentation
also_listed_in: []
website: https://cilium.io
founded: null
hq: CNCF project (commercial steward Isovalent, now part of Cisco, San Jose, CA)
ownership_state: oss-foundation
owner: null
ownership_note: 'Open-source CNCF Graduated project (accepted 2021-10-13 at Incubating; Graduated 2023-10-11). Userspace Apache-2.0, eBPF code GPL-2.0/BSD-2-Clause. Tetragon is a Cilium sub-project under CNCF. Created by Isovalent, the main commercial contributor. Cisco announced it would acquire Isovalent on 2023-12-21 and closed on 2024-04-12 (price undisclosed). The Isovalent team joined the Cisco Security Business Group. Cisco owns the company and its enterprise distribution, not the project.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (project); Isovalent raised ~$69M before acquisition (secondary)
last_funding: n/a
market_position: {trust-zone-segmentation: oss-default}
deployment_model: [self-hosted, on-prem]
form_factor: [agent, platform]
data_leaves_tenancy: "false"
integrations: [kubernetes, gke-dataplane-v2, azure-cni-powered-by-cilium, eks-anywhere, prometheus, grafana, opentelemetry, wireguard, ipsec, gateway-api, cisco-nexus]
mcp_support: none
certifications: []
pricing_model: oss (free); Cisco Isovalent enterprise subscription, sales-quoted
fs_traction: claimed
target_customer: Platform and security teams running Kubernetes (cloud or on-prem) who need to enforce which workloads, namespaces and external domains can talk to each other, with flow-level audit
last_verified: 2026-10-26
verify_after: null
tags: [ebpf, kubernetes, cni, network-policy, egress-control, fqdn-policy, hubble, tetragon, runtime-enforcement, cncf, cncf-graduated, cisco, isovalent, segmentation]
sources:
  - {claim: "Cilium accepted to CNCF 2021-10-13 (Incubating); Graduated 2023-10-11", url: "https://www.cncf.io/projects/cilium/", date: 2023-10-11, confidence: high}
  - {claim: "Apache-2.0 userspace, GPL-2.0/BSD-2 BPF; identity-based L3-L7 policy; DNS/FQDN policy; Hubble; service mesh with IPsec/WireGuard/ztunnel; Cluster Mesh; egress gateways; kube-proxy replacement; v1.20.4 2026-10-23; ~25.7k stars", url: "https://github.com/cilium/cilium", date: 2026-10-26, confidence: high}
  - {claim: "Tetragon: Kubernetes-aware security observability and in-kernel runtime enforcement; sub-project under Cilium and CNCF; runs outside Kubernetes", url: "https://tetragon.io/", date: 2026-10-26, confidence: high}
  - {claim: "Cisco announced intent to acquire Isovalent 2023-12-21; price undisclosed", url: "https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2023/m12/cisco-to-acquire-isovalent-to-define-the-future-of-multicloud-networking-and-security.html", date: 2023-12-21, confidence: high}
  - {claim: "Cisco completed Isovalent acquisition 2024-04-12; team joins Cisco Security Business Group; commitment to eBPF, Cilium, Tetragon communities", url: "https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m04/cisco-completes-acquisition-of-isovalent-to-define-the-future-of-multicloud-networking-and-security.html", date: 2024-04-12, confidence: high}
  - {claim: "Isovalent raised ~$69M over two rounds; Cisco invested in Series A", url: "https://aragonresearch.com/cisco-to-acquire-isovalent-one-big-step/", date: 2023-12, confidence: medium}
  - {claim: "Cisco Isovalent positioned for AI/LLM Kubernetes platforms and secure multi-tenancy; paired with Nexus One", url: "https://blogs.cisco.com/datacenter/extending-infrastructure-fabric-the-journey-to-cloud-native-isovalent-networking", date: 2026-02-23, confidence: medium}
  - {claim: "Rabobank uses Cilium as default CNI with FQDN-based network policies", url: "https://www.cncf.io/case-studies/rabobank/", date: 2026-10-26, confidence: medium}
  - {claim: "GKE Dataplane V2 implemented with Cilium; Azure CNI Powered by Cilium; EKS Anywhere ships Cilium as default CNI", url: "https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2", date: 2026-10-26, confidence: medium}
---

# Cilium (Isovalent / Cisco)

> Primary category: [trust-zone-segmentation](../categories/trust-zone-segmentation.md), a **practice** category with no survey question. Cilium is one of the tools that enforces zone boundaries on Kubernetes. It is not an AI product. Open-source **CNCF Graduated** project. Its creator, Isovalent, has been owned by Cisco since 2024-04-12. Sources cached under `raw/sources/2026-10-26--cilium--*`.

**One-liner**: The standard open-source networking and network-security layer for Kubernetes. It decides which pods may talk to which other pods and to which outside domains, records every connection (Hubble), and with its sister project Tetragon can watch and block what processes do inside a container. It runs in the Linux kernel using eBPF.

**What it does**: Cilium replaces Kubernetes' default networking plumbing (the "CNI" and kube-proxy) with eBPF programs in the kernel. The parts that matter for AI governance:

- **Identity-based network policy (L3–L7).** Rules are written against workload labels ("pods labelled `zone=yellow` may reach the warehouse service, nothing else"), not IP addresses. Rules can go down to HTTP method and path, and to DNS names.
- **FQDN / DNS-aware egress policy.** Allow or deny outbound traffic by domain (`api.openai.com`, `*.trusted.com`). This is how you give an agent namespace a short allowlist of model and tool endpoints and block the rest of the internet.
- **Egress gateway.** Sends a namespace's outbound traffic through fixed exit nodes and IPs, so a firewall, SASE or [ai-gateway](../categories/ai-gateway.md) can see and control it.
- **Hubble.** Flow-level observability: which workload connected to which, allowed or dropped, with DNS names. This is your evidence that a zone boundary held.
- **Transparent encryption** (WireGuard, IPsec, ztunnel), **Cluster Mesh** (multi-cluster policy), and a **service mesh** with L7 policy.
- **Tetragon** (a CNCF sub-project of Cilium): in-kernel runtime security. It observes process execution, file access and privilege changes, and can **block in the kernel**. Examples: no binaries executed from `/tmp`, alert on writes to sensitive paths, detect exfiltration patterns. It also runs on plain Linux hosts without Kubernetes.

## Agent-security role: the lethal trifecta

The lethal trifecta is the core agent-security threat model: untrusted input, sensitive data and outbound access in one agent context. Zone design removes one leg per zone. On Kubernetes, Cilium is how you **actually remove the egress leg and the lateral-movement path** instead of just declaring it removed:

- **Yellow zone (no egress):** default-deny egress for the namespace, plus allow rules only to the internal data services it needs. Hubble shows every attempted connection to the internet as dropped.
- **Red zone (no sensitive data):** egress to the internet is allowed, but network policy denies any route to internal data services, secrets stores or other namespaces.
- **Green zone (no untrusted input):** inbound only from approved services, and egress only to named production endpoints.
- **Tetragon** adds a second line inside the zone. If a compromised agent runs `curl`, spawns a shell or reads a credentials file, it can be blocked or flagged in the kernel.

What Cilium does **not** do: it does not understand prompts, MCP messages or what is in the data. An allowed domain is allowed for any content. An agent permitted to call `api.github.com` can send secrets to a public gist. Content-level controls belong to [ai-runtime-security](../categories/ai-runtime-security.md), [dlp](../categories/dlp.md), [ai-gateway](../categories/ai-gateway.md) and [mcp-gateway](../categories/mcp-gateway.md). Cilium makes those choke points unavoidable by blocking every other route out. It also only governs workloads on clusters or hosts where it runs. Agents on laptops or in SaaS are outside its reach.

**Naming / provenance**: Cilium was started at Isovalent (Isovalent leadership named in coverage: Thomas Graf and Dan Wendlandt; Cilium's start date, commonly given as about 2015, was not verified). It was accepted into the CNCF on **2021-10-13** (Incubating) and **graduated on 2023-10-11**. **Hubble** is its observability layer and **Tetragon** its runtime-security sub-project. Cisco now sells the commercial side as **"Cisco Isovalent"** (2026-02 Cisco blog). Exact current SKU names were not verified. Many firms already run Cilium without choosing it: **GKE Dataplane V2** is built on Cilium (Google Cloud docs; it is Google's build, not the OSS plugin, and can't be swapped out), Azure offers **"Azure CNI Powered by Cilium"**, and **EKS Anywhere** ships it as the default CNI. Standard EKS defaults to the AWS VPC CNI.

**Ownership & viability**: The project is `oss-foundation` (CNCF Graduated, the top maturity tier). Isovalent, its creator and main commercial contributor, was **acquired by Cisco**: intent announced **2023-12-21**, closed **2024-04-12**, price undisclosed (Isovalent had raised about $69M, per Aragon Research, secondary). The team joined Cisco's Security Business Group. Cisco publicly committed to "nurturing and supporting eBPF, Cilium, Tetragon, and cloud native open source communities." The project itself is healthy: about 25.7k GitHub stars and three stable branches patched on 2026-10-23. Steward risk is moderate and worth watching. Cisco employs the Isovalent team, which includes core maintainers (exact share not verified), and is positioning Isovalent within its broader security platform (secondary reporting links Cilium and Tetragon to Cisco Hypershield). If Cisco steered features toward its paid products, the CNCF governance and the cloud providers that build on Cilium (Google, Microsoft) act as a counterweight. Isovalent is not mentioned on [cisco](cisco.md) yet.

**Positioning & differentiators**:
- **vs Calico (Tigera)**: the other major Kubernetes network-policy engine (its eBPF and DNS-policy features were not verified on this pass). The choice usually comes down to which one your managed Kubernetes provider uses and which vendor you want support from. Calico has no wiki page.
- **vs Istio / service meshes**: overlapping L7 policy and mTLS. Cilium works at the kernel and CNI level and can enforce without sidecars. Istio is richer for application-layer routing. Many shops run both.
- **vs agent sandbox runtimes** ([nvidia-openshell](nvidia-openshell.md), [docker-sandboxes](docker-sandboxes.md)): those enforce egress and filesystem policy per agent sandbox, with agent-aware approval flows. Cilium enforces per workload or namespace across a whole cluster and knows nothing about agents. It suits firms that run agents as ordinary Kubernetes services, not as coding-agent sandboxes.
- **vs SASE / [network-security-sase](../categories/network-security-sase.md)** ([zscaler](zscaler.md), [palo-alto-networks](palo-alto-networks.md), [cisco](cisco.md) Secure Access): SASE controls traffic from users and branches out to the internet. Cilium controls traffic between workloads and out of the cluster. They complement each other, and Cilium's egress gateway can feed a SASE or firewall exit.

*Market position*: `oss-default` for enforcing [trust-zone-segmentation](../categories/trust-zone-segmentation.md) on Kubernetes. It is the CNCF-graduated eBPF CNI and is built into GKE and Azure options, so many platforms run it by default.

**Who should choose them / anti-fit**: Fits firms that **self-host agents, model serving, RAG services or MCP servers on Kubernetes** and need provable network boundaries between zones, an egress allowlist per namespace, and flow logs for audit. Check first whether your managed Kubernetes already runs it. **Anti-fit**: funds that consume AI only as SaaS (ChatGPT Enterprise, Copilot, Claude) or run agents on laptops. Cilium has nothing to enforce there, so put the effort into SASE, browser and identity controls. Teams without Kubernetes or platform-engineering staff. Anyone expecting it to stop prompt injection or data leaks through allowed destinations.

**Known weaknesses / gotchas**:
- **It is plumbing, not a governance product.** There is no AI inventory, no policy-by-risk-tier UI and no agent awareness. Someone has to translate the zone design into labels and policies and keep them current.
- **FQDN allowlists are coarse.** Allowing a large SaaS or cloud domain (for example `*.amazonaws.com`) allows a lot of attacker-usable space. Pair it with an egress gateway into an AI or API gateway that inspects content.
- **Default-allow unless you change it.** Kubernetes networking is open until a policy selects a pod. Zones only exist once default-deny policies are applied and tested. Hubble's dropped-flow view is how you verify.
- **Managed variants differ.** GKE Dataplane V2 is Cilium-based but not the full OSS feature set. Check which Cilium features (FQDN policy, Hubble, Tetragon) your provider actually exposes.
- **Steward concentration.** One company (now Cisco) contributes much of the code. Watch for useful features moving into the enterprise edition.

**Deployment & data handling**: Self-hosted inside your clusters (an agent DaemonSet on every node plus an operator). Hubble and Tetragon run in-cluster. Flow and event data stays with you unless you export it to your SIEM or observability stack, so `data_leaves_tenancy: "false"` for the OSS deployment. Whether the Cisco enterprise offering includes a SaaS console that receives telemetry was not verified. Enforcement is **inline in the kernel datapath**: policy is checked as packets and syscalls happen, with no proxy hop for L3/L4 rules. L7 rules add a proxy hop (Envoy, per general project documentation; not re-verified here).

**Integrations & partnerships**: Kubernetes (all major distributions), GKE Dataplane V2, Azure CNI Powered by Cilium, EKS Anywhere. Hubble and Tetragon export metrics and events (Prometheus, Grafana, OpenTelemetry/JSON export for SIEM; specific SIEM connectors not verified). Gateway API. Cisco Nexus One as underlay in Cisco's 2026 positioning. `mcp_support: none`: it has no MCP-aware features and treats MCP over HTTP like any other HTTP traffic.

**Compliance & FS traction**: The project has no certifications. Cisco's commercial offering certifications were not verified. FS evidence: **Rabobank** (CNCF case study) uses Cilium as its default CNI and moved from IP allowlists to FQDN-based policies. Bloomberg is cited (SDxCentral, 2023) among organisations using open-source cloud-native networking. Cisco claims an unnamed "major financial firm". Hubble flow logs and Tetragon events support evidence of segmentation for audits or exams.

**Commercial**: Cilium, Hubble and Tetragon are free (Apache-2.0 userspace). Cisco sells an enterprise distribution with support under the Isovalent name. Pricing is not public and quoted by sales. Managed-Kubernetes users may get Cilium-based networking as part of their cloud bill.

## Open questions

- Current Cisco product names and packaging for Isovalent (enterprise platform, runtime security), and what is held back from the OSS editions.
- Whether Cisco has folded Cilium or Tetragon into Hypershield or [cisco-ai-defense](cisco-ai-defense.md) for agent workloads. Only secondary German-language reporting links them to Hypershield.
- Tetragon's licence and whether it has CNCF standing separate from Cilium (the site says "sub-project under Cilium").
- Any Isovalent or Cisco material specifically on containing AI agents. A 2026 Isovalent training session on this was seen in search results but not fetched.
- Should Cilium also be cross-listed to [policy-as-code](../categories/policy-as-code.md)? Its policies are declarative Kubernetes resources kept in Git, but that category today means admission and IaC policy (OPA, Kyverno, Sentinel). Not cross-listed for now.

## Sources

- [CNCF: Cilium](https://www.cncf.io/projects/cilium/) — fetched 2026-10-26 — supports: CNCF dates; confidence: high
- [cilium/cilium on GitHub](https://github.com/cilium/cilium) — fetched 2026-10-26 — supports: licence, components, release cadence; confidence: high
- [tetragon.io](https://tetragon.io/) — fetched 2026-10-26 — supports: Tetragon scope, sub-project status; confidence: high
- [Cisco newsroom: Cisco to acquire Isovalent](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2023/m12/cisco-to-acquire-isovalent-to-define-the-future-of-multicloud-networking-and-security.html) — via search 2026-10-26 — supports: announcement 2023-12-21; confidence: high
- [Cisco newsroom: Cisco completes acquisition of Isovalent](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m04/cisco-completes-acquisition-of-isovalent-to-define-the-future-of-multicloud-networking-and-security.html) — fetched 2026-10-26 — supports: close 2024-04-12, Security Business Group, OSS commitment; confidence: high
- [Aragon Research: Cisco to acquire Isovalent](https://aragonresearch.com/cisco-to-acquire-isovalent-one-big-step/) — via search 2026-10-26 — supports: ~$69M raised; confidence: medium
- [Cisco blog: the journey to cloud-native Isovalent networking](https://blogs.cisco.com/datacenter/extending-infrastructure-fabric-the-journey-to-cloud-native-isovalent-networking) — fetched 2026-10-26 — supports: "Cisco Isovalent" branding, AI-platform positioning (2026-02-23); confidence: medium (marketing)
- [CNCF case study: Rabobank](https://www.cncf.io/case-studies/rabobank/) — via search 2026-10-26 — supports: FS adopter, FQDN policies; confidence: medium
- [Google Cloud: GKE Dataplane V2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) — via search 2026-10-26 — supports: Dataplane V2 built on Cilium; confidence: medium

## History

- [2026-10-26] Page created and researched in one pass (user-requested addition). Slugged `cilium` (the CNCF project), not `isovalent`. Reasons: buyers meet Cilium as a CNI, often already inside GKE or AKS; it is foundation-governed; and Isovalent the company is now a Cisco business unit whose corporate story belongs on [cisco](cisco.md). The title "Cilium (Isovalent / Cisco)" follows the agentgateway convention. Primary is the practice category trust-zone-segmentation (no survey answer option). Confirmed Cisco acquisition of Isovalent: announced 2023-12-21, closed 2024-04-12.
