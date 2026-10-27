# Cilium adopters (FS) and cloud-provider dataplanes

- URLs: https://www.cncf.io/case-studies/rabobank/ ; https://cilium.io/industries/cloud-providers ; https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2 ; https://discuss.google.dev/t/what-cni-plugin-is-used-in-gke-and-are-there-alternatives/137099 ; https://www.sdxcentral.com/articles/analysis/how-ikea-the-new-york-times-and-bloomberg-use-open-source-for-cloud-native-networking-and-security/2023/04/
- Fetched: 2026-10-26 (via search result snippets)
- Good for: FS adoption evidence and the "you may already run it" point for managed Kubernetes.

## Financial services
- Rabobank (CNCF case study): API platform team uses Cilium as default CNI; moved from IP allow lists to FQDN-based network policies, easing maintenance/troubleshooting.
- SDxCentral 2023-04: Bloomberg named among organisations using open-source cloud-native networking/security (Cilium context). Secondary.
- Cisco blog: "a major financial firm" helped reduce tool sprawl — unnamed, marketing.

## Cloud providers
- GKE Dataplane V2 "is implemented with Cilium" (Google Cloud docs); default for new Autopilot clusters; community answer: Cilium-based architecture but not the Cilium OSS plugin, CNI not replaceable.
- "Azure CNI Powered by Cilium" combines Azure CNI control plane with Cilium data plane (cilium.io cloud-providers page; vendor/project page).
- EKS Anywhere ships Cilium as default CNI (cilium.io claim). Standard EKS default CNI is the AWS VPC CNI — EKS hybrid nodes not verified.
