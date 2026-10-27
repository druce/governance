# Cilium + Tetragon — CNCF project page, GitHub README, tetragon.io

- URLs: https://www.cncf.io/projects/cilium/ ; https://github.com/cilium/cilium ; https://tetragon.io/
- Fetched: 2026-10-26
- Good for: Cilium governance, license, components; Tetragon scope.

## CNCF project page
- Cilium "accepted to CNCF on October 13, 2021 at the Incubating maturity level"; "moved to the Graduated maturity level on October 11, 2023."

## GitHub cilium/cilium (2026-10-26)
- Userspace Apache-2.0; BPF code dual GPL-2.0-only / BSD-2-Clause.
- ~25.7k stars, 4.2k forks. Stable releases v1.20.4 / v1.19.10 / v1.18.16 (2026-10-23); v1.21.0-pre.3 (2026-10-02).
- Components: identity-based L3–L7 network policy ("Identity-based security removes reliance on brittle IP addresses"); DNS-based policy allowing/denying FQDNs and wildcards (e.g. `*.trusted.com`); Hubble observability (service maps, identity-aware flow visibility, DNS-aware filtering); service mesh with L7-aware policy and transparent encryption (IPsec, WireGuard, ztunnel), Gateway API; Cluster Mesh; integrated ingress and egress gateways; can "fully replace kube-proxy".
- Governed by maintainers/committers (MAINTAINERS.md); CNCF Graduated.

## tetragon.io
- "a flexible Kubernetes-aware security observability and runtime enforcement tool" applying policy with eBPF; can "block malicious activities at the kernel level" in-kernel.
- Use cases: control binary execution (e.g. disallow exec from /tmp), detect namespace/privilege changes, Kubernetes data exfiltration, file integrity monitoring.
- "Tetragon is a sub-project under Cilium and a proud CNCF project."
- Runs outside Kubernetes too (release tarball + systemd; container image); Helm for Kubernetes.
- Licence not stated on the homepage.
