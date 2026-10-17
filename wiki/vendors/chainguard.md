---
title: Chainguard
type: vendor
name: Chainguard
slug: chainguard
aka: [Chainguard Images, Chainguard Containers, Chainguard Libraries, Chainguard OS, Wolfi]
primary_category: software-supply-chain
also_listed_in: []
website: https://www.chainguard.dev/
founded: 2021
hq: Kirkland, Washington, USA
ownership_state: independent
owner: null
ownership_note: Private, VC-backed. Series D $356M at $3.5B valuation (2025-04-23, co-led by Kleiner Perkins and IVP), then $280M non-dilutive growth financing from General Catalyst's Customer Value Fund (2025-10-23). Total raised ~$892M. No 2026 round and no acquisitions (by or of Chainguard) found as of 2026-10-16.
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$892M (company figure, 2025-10-23)"
last_funding: "$280M growth financing, General Catalyst Customer Value Fund, 2025-10-23 (last priced: $356M Series D at $3.5B, 2025-04-23)"
market_position: {software-supply-chain: challenger}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "false"
integrations: [docker, kubernetes, maven, pypi, npm, claude-code, cursor, github-copilot, gemini-cli, datadog]
mcp_support: unverified
certifications: []
pricing_model: "Subscription per image / catalog and per library ecosystem; quote-based. Free starter tier (five non-FIPS images, beta)."
fs_traction: claimed
target_customer: mid-market to large enterprise and public sector running containers
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [hardened-containers, minimal-images, distroless, slsa, sigstore, sbom, fips, malware-resistant-dependencies, agent-skills, aie-nyc-2026]
sources:
  - {claim: "$356M Series D at $3.5B valuation; ARR 7x to $40M in FY2025", url: "https://fortune.com/2025/04/23/exclusive-chainguard-secures-356-million-series-d-as-valuation-soars-to-3-5-billion", date: 2025-04-23, confidence: high}
  - {claim: "$280M growth financing from General Catalyst CVF; $892M total raised", url: "https://www.securityweek.com/chainguard-raises-280-million-in-growth-funding/", date: 2025-10-23, confidence: high}
  - {claim: "Founded Oct 2021 by ex-Google Sigstore/SLSA engineers incl. Dan Lorenc", url: "https://research.contrary.com/report/chainguard", date: 2026-10-16, confidence: medium}
  - {claim: "Chainguard Libraries for Python: packages rebuilt from source on SLSA L2 infrastructure, 2025-05-14", url: "https://www.chainguard.dev/unchained/announcing-chainguard-libraries-for-python-malware-resistant-dependencies-built-securely-from-source", date: 2025-05-14, confidence: high}
  - {claim: "Chainguard Agent Skills: hardened agent-skills catalog announced 2026-03-17", url: "https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills", date: 2026-03-17, confidence: high}
  - {claim: "Product list, FS segments, Gartner MQ Leader claim, 98% CVE reduction claim", url: "https://www.chainguard.dev/solutions/financial-services", date: 2026-10-16, confidence: medium}
  - {claim: "AIE NYC 2026 Silver sponsor", url: "https://www.ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Chainguard

> Primary category: [software-supply-chain](../categories/software-supply-chain.md).

**One-liner** — A supplier of **hardened, minimal, continuously rebuilt open-source artifacts**: container images, language libraries (Java, Python, JavaScript) and VM images built from source with signed provenance. You swap them in for public Docker Hub images and PyPI or Maven packages, so most known CVEs and much of the malicious-package risk disappear at the source rather than being scanned for afterwards.

**What it does** — Chainguard does not scan your code. It **replaces the open-source inputs** your software is built from:
- **Chainguard Containers** (also called Chainguard Images). Minimal, distroless-style images rebuilt daily on Chainguard OS (which grew out of the **Wolfi** "undistro"), shipped with SBOMs and Sigstore signatures, and offered in FIPS variants. The CPU/GPU **AI images** (PyTorch, Conda and others, announced August 2024) are aimed at ML workloads; the PyTorch image is described as FIPS-enabled and STIG-hardened (vendor).
- **Chainguard Libraries.** Language packages **rebuilt from source** on Chainguard's own SLSA infrastructure instead of pulled from public registries. Java launched first (Assemble 2025); **Libraries for Python** was announced 2025-05-14 and includes wheels with native code. Chainguard says it has built more than 13,000 Python libraries. The pitch is resistance to build- and distribution-stage attacks such as the Ultralytics and PyTorch incidents it cites. Its own test claims about 98% of roughly 3,000 known malicious packages would have been avoided; that is a vendor test, not independent. **This is the most relevant piece for AI teams**, whose Python dependency trees (torch, transformers and friends) are deep and a frequent supply-chain target.
- **Chainguard VMs and OS packages**, plus newer lines: **Actions**, **Workspaces**, **Harness** and **Checks** (descriptions not researched).
- **Chainguard Agent Skills** (announced 2026-03-17). A catalog of **hardened AI-agent skills**: community skills that have been reviewed, permission-scoped and integrity-checked, with an audit trail, and re-hardened automatically when upstream changes. At launch it held 1,000+ skills, installed via `chainctl` into Claude Code, Cursor, GitHub Copilot and Gemini CLI. It was later opened to all users and gained a private registry for internal skills. This takes Chainguard's "curated, verified upstream" model to a new kind of artifact that coding agents pull in.

**Naming / provenance** — Founded October **2021** by ex-Google engineers **Dan Lorenc (CEO)**, Matt Moore, Kim Lewandowski, Ville Aikas and Scott Nichols (Contrary Research; an early article names only Lorenc and Lewandowski). The team built **Sigstore** and **SLSA** at Google, which explains the provenance-first design. Chainguard Containers were long marketed as "Chainguard Images" and both names are still used. Wolfi is the open-source base distro; Chainguard OS is the commercial name.

**Ownership & viability** — `independent`, private. Funding milestones:

| Date | Event | Amount / valuation |
|---|---|---|
| 2024-07 | Series C | $1.12B valuation |
| 2025-04-23 | Series D, co-led by Kleiner Perkins and IVP (new: Salesforce Ventures, Datadog Ventures) | $356M at **$3.5B** |
| 2025-10-23 | Growth financing from General Catalyst's Customer Value Fund (non-dilutive, earmarked for sales and marketing) | $280M |

Total raised is **~$892M** (company figure). Fortune reported FY2025 ARR up 7x to **$40M**, and a target of more than $100M ARR by the end of FY2026. No 2026 round was found; a July 2026 "raises $800M" headline restates cumulative funding. **No acquisitions by or of Chainguard were found.** Viability is strong: the company is very well funded for its revenue. The flip side is that a $3.5B valuation on about $40M ARR sets a high bar. A strategic acquirer would most likely be a cloud, registry or security platform, but that is speculation, and no reporting suggests a sale.

**Positioning & differentiators** — `challenger` in software-supply-chain. It leads the **hardened-images** niche and claims Leader status in a 2026 Gartner Magic Quadrant for Software Supply Chain Security (vendor claim, not checked). It is not a broad AppSec platform, so it sits beside the scanner leaders rather than replacing them.
- **Prevent rather than detect.** [snyk](snyk.md), [sonatype](sonatype.md), [jfrog](jfrog.md), [endor-labs](endor-labs.md) and [socket](socket.md) tell you what is wrong with the open source you already pulled. Chainguard hands you a version already rebuilt and patched, so the findings never appear. The two approaches complement each other; most Chainguard customers still run a scanner.
- **Build-from-source provenance** for libraries is a stronger guarantee against tampered registry uploads than reputation scoring or malware detection on the public registry, which is [socket](socket.md)'s approach. The trade-off is coverage: only packages Chainguard has rebuilt are protected.
- **Competition in hardened images.** Docker (Docker Hardened Images; no wiki page) and smaller players such as Echo and Minimus compete directly; third-party commentary reports Echo bought technology assets from Minimus. Chainguard is the best-funded and broadest catalog. Free alternatives exist (Wolfi itself, Google distroless, cloud-vendor base images), at the cost of maintaining them yourself.

**Who should choose them / anti-fit** — Fits a firm that **runs a lot of containers** and whose security or vulnerability-management teams are drowning in base-image CVEs. It also fits any team shipping **Python ML/AI services** that wants a defensible answer to "where did this torch wheel come from?", and firms with FIPS, FedRAMP-adjacent or DORA-style evidence needs. **Anti-fit:** a small hedge fund whose software is mostly SaaS-consumed and notebooks, with few production containers. The per-image subscription is hard to justify there, and a scanner plus pinned dependencies may be enough. It also does not help with **first-party code quality or SAST** (see [sonar](sonar.md), [semgrep](semgrep.md)) or with AI-generated code review.

**Known weaknesses / gotchas** —
- **Migration cost.** Minimal images have no shell or package manager by default, so Dockerfiles, debugging habits and some vendor software need rework. Teams sometimes reintroduce `-dev` variants and give back part of the security benefit.
- **Coverage limits.** Libraries protect only what Chainguard has rebuilt. Exotic or internal-mirror packages fall back to public sources unless you block them.
- **Free tier is narrow.** The free Starter tier offers limited images, `:latest` only, with no SLA. Pinned versions and full catalog access are paid.
- **Opaque pricing.** All substantive pricing goes through sales.

**Deployment & data handling** — A **SaaS registry**: customers pull images and packages from Chainguard's registry, usually mirrored into their own Artifactory, Nexus or ECR. `data_leaves_tenancy: "false"` in the sense that customer code, prompts and data are not sent to Chainguard. The traffic is artifact downloads inbound, plus account and pull telemetry. The artifacts then run wherever your workloads run. It is not inline at runtime, so there is no latency impact.

**Integrations & partnerships** — Drop-in for Docker/OCI and Kubernetes, and for Maven, PyPI and npm via registry configuration. Agent Skills installs into Claude Code, Cursor, GitHub Copilot and Gemini CLI. A Datadog partnership was announced at Assemble 2025 (Datadog Ventures is also an investor). MCP support was not researched (`unverified`). **AI Engineer New York 2026 (Oct 12–14):** listed as a **Silver sponsor**; no Chainguard talk appears on the published conference schedule.

**Compliance & FS traction** — Certifications of Chainguard **as a company** are **unverified**. A third-party blog says it holds SOC 2 Type II, and a Chainguard case study describes its own SOC 2 Type II preparation, but no trust-center confirmation was fetched. Product-side, it offers FIPS-validated images, SBOMs, signed provenance and SLSA build levels, which help customers with PCI DSS, NYDFS, DORA and SOC 2 evidence (vendor framing). FS traction is `claimed`: the financial-services page lists G-SIBs, fintech, wealth management, PE, VC and crypto as segments served, but **names no FS customer**; the featured case study is Anduril (defense). Chainguard was named a CVE Numbering Authority in September 2026 (secondary listing, unverified).

**Commercial** — Quote-based subscription priced per image or catalog and per library ecosystem. There is a free starter tier (docs: any five non-FIPS images, in beta, business email required). A third-party site suggests a catalog floor of about $19k per year for a 10-person team, which is unverified. Pricing is as of 2026-10-16.

## Open questions

- Chainguard's own certifications (SOC 2 Type II, ISO 27001, FedRAMP status), from its trust center.
- Named financial-services customers, especially buy-side.
- Which Python AI/ML packages (torch, CUDA wheels, transformers, vLLM) Chainguard Libraries for Python covers, and the CUDA versions in the AI images.
- What Actions, Workspaces, Harness and Checks are, and whether any of them is an MCP or agent-runtime product that would warrant cross-listing.
- Whether Agent Skills is priced separately or bundled.
- Current revenue against the >$100M FY2026 ARR target.

## Sources

- [Chainguard secures $356M Series D (Fortune)](https://fortune.com/2025/04/23/exclusive-chainguard-secures-356-million-series-d-as-valuation-soars-to-3-5-billion) — fetched 2026-10-16 — supports: Series D, valuation, ARR; confidence: high
- [Chainguard raises $280M in growth funding (SecurityWeek)](https://www.securityweek.com/chainguard-raises-280-million-in-growth-funding/) and [GeekWire](https://www.geekwire.com/2025/chainguard-lands-280m-to-help-scale-cybersecurity-startups-open-source-software-protections/) — fetched 2026-10-16 — supports: Oct 2025 financing, total raised; confidence: high
- [Chainguard report (Contrary Research)](https://research.contrary.com/report/chainguard) — fetched 2026-10-16 — supports: founding, founders; confidence: medium
- [Announcing Chainguard Libraries for Python (vendor)](https://www.chainguard.dev/unchained/announcing-chainguard-libraries-for-python-malware-resistant-dependencies-built-securely-from-source) — fetched 2026-10-16 — supports: Libraries for Python scope and claims; confidence: high (claims are vendor)
- [Introducing Chainguard Agent Skills (vendor)](https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills) and [open-to-everyone follow-up](https://www.chainguard.dev/unchained/chainguard-agent-skills-is-now-open-to-everyone-with-a-private-registry-to-manage-your-internal-skills) — fetched 2026-10-16 — supports: Agent Skills; confidence: high
- [Chainguard launches CPU/GPU containers for AI frameworks (The New Stack)](https://thenewstack.io/chainguard-launches-cpu-gpu-containers-for-ai-frameworks/) — fetched 2026-10-16 — supports: AI images; confidence: medium
- [Financial Services solutions page (vendor)](https://www.chainguard.dev/solutions/financial-services) — fetched 2026-10-16 — supports: product list, FS segments, MQ claim; confidence: medium (marketing)
- [Pricing (vendor)](https://www.chainguard.dev/pricing) and [Catalog Starter docs](https://edu.chainguard.dev/chainguard/containers/about/catalog-starter/) — fetched 2026-10-16 — supports: free tier; confidence: medium
- [AI Engineer New York sponsors](https://www.ai.engineer/nyc) and [schedule](https://www.ai.engineer/nyc/schedule) — fetched 2026-10-16 — supports: Silver sponsorship, no talk found; confidence: high
- Cached: `raw/sources/2026-10-16--chainguard--funding-company.md`, `raw/sources/2026-10-16--chainguard--products-ai.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
