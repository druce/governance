---
title: JFrog
type: vendor
name: JFrog
slug: jfrog
categories: [software-supply-chain]
layer: foundation
aliases: [Artifactory, Xray, JFrog Platform, JFrog ML]
website: "https://jfrog.com"
founded: 2008
hq: Sunnyvale, California, USA (dual HQ with Netanya, Israel)
ownership: public
ownership_detail: "Public — NASDAQ: FROG since IPO Sept 2020; market cap ~$3.5B-$4.5B (as of early 2025, volatile)"
ownership_confidence: high
funding_total: "~$509M raised at IPO (Sept 2020, ~$3.9B valuation); pre-IPO VC ~$226M"
last_funding: "IPO Sept 2020 (NASDAQ: FROG)"
deployment: [saas, self-hosted, on-prem, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [artifact-repository, sca, mlops, devsecops]
---

# JFrog

**One-liner** — The "system of record" for software binaries: a universal artifact repository (Artifactory) plus dependency/security scanning (Xray) that has extended into storing and scanning ML models.

**What it does** — JFrog runs the [software-supply-chain](../categories/software-supply-chain.md) spine for many engineering orgs. **Artifactory** is a universal binary/artifact repository that proxies, caches, and stores every package type (Maven, npm, PyPI, Docker, Go, NuGet, Helm, etc.) as the single source of truth for build artifacts. **Xray** scans those artifacts and their transitive dependencies for known vulnerabilities (CVEs), license issues, and malicious packages (software composition analysis). Around these sit the broader JFrog Platform: distribution, CI/CD integration, and — since the 2024 Qwak acquisition — **JFrog ML** for model management.

**Where it sits in the stack** — Foundation layer of [software-supply-chain](../categories/software-supply-chain.md). It controls what code/dependencies enter your build (the *untrusted-input* leg of the lethal trifecta as applied to your own supply chain). **AI-generated-code relevance:** when developers ship LLM-generated code, that code pulls in open-source dependencies — and LLMs are known to hallucinate package names ("slopsquatting" risk). The Artifactory-as-proxy + Xray-scan model is exactly the choke point that catches a malicious or non-existent dependency before it lands in a build. **ML/model-management angle:** via Qwak, JFrog now treats ML models as first-class artifacts — Artifactory acts as the **model registry** (single system of record), and Xray scans models for security/compliance (MLSecOps). This makes JFrog one of the few software-supply-chain players spanning both code dependencies *and* model artifacts.

**Deployment & architecture** — Available as SaaS (JFrog Cloud), self-hosted/on-prem, and hybrid. Architecturally it is a repository/proxy that sits between public registries (Maven Central, npm, Docker Hub) and your CI/CD, caching approved binaries and enforcing policy. Deep integrations with CI/CD systems, IDEs, and container/K8s tooling. Self-hosted/on-prem option matters for regulated and air-gapped shops.

**Positioning & differentiators** — JFrog's moat is the **repository itself**: it is the de-facto enterprise artifact store, and Xray rides on top of assets it already holds. That makes it more "platform/infrastructure" than a pure scanner. Contrast with [snyk](snyk.md) and [endor-labs](endor-labs.md) (developer-first SCA/reachability analysis that scan source/dependencies but don't own the binary store), [sonatype](sonatype.md) (its closest peer — Nexus Repository + repository firewall + SCA, the other artifact-repository-plus-supply-chain vendor), and [aikido-security](aikido-security.md) (consolidated dev-first AppSec for smaller shops). JFrog's distinctive extension is binary distribution at scale plus the new model-management layer.

**Ownership, funding & M&A** — Public company, **NASDAQ: FROG** since its IPO in **September 2020** (raised ~$509M at a ~$3.9B valuation). Founded **2008** in Netanya, Israel by Shlomi Ben Haim (CEO), Yoav Landman (CTO), and Fred Simon; dual-HQ in Sunnyvale, CA. Notable M&A: acquired **Qwak** (AI/MLOps platform) — announced **2024-06-25**, press-reported at ~$230M (deal value not disclosed by JFrog) — to add ML model training/serving and the JFrog ML offering. (ownership_confidence: high; market-cap figure is as-of early 2025 and volatile.)

**CTO / hedge-fund lens** — **Day-1 if you ship meaningful in-house or AI-generated code** at scale and need a controlled binary repository + dependency scanning; **Day-2/optional** for a small fund that consumes mostly SaaS and writes little code. The Artifactory + Xray combination is the heavyweight, enterprise-grade choice and can be overkill (and over-priced) for a 50-person shop, where a consolidated dev-first tool ([aikido-security](aikido-security.md)) or a pure SCA ([snyk](snyk.md)) may be enough. The model-management angle is interesting for funds building/serving their own ML models, but most asset managers consuming third-party AI won't need it Day-1. Self-hosted option is a plus for regulated environments.

**Competitors / alternatives** — [sonatype](sonatype.md) (closest: repository + supply-chain firewall), [snyk](snyk.md), [endor-labs](endor-labs.md), [aikido-security](aikido-security.md); cloud-native registries (GitHub Packages, AWS/Azure artifact registries) at the low end.

## Open questions / to verify
- Current market cap / latest quarterly financials (volatile — re-check at use).
- Exact Qwak deal value (JFrog did not disclose; press cites ~$230M).
- Pricing tiers relevant to a small fund (Artifactory + Xray bundle vs standalone).

## Sources
- [JFrog to Acquire Qwak to Streamline AI Models](https://jfrog.com/press-room/jfrog-to-acquire-qwak-to-streamline-ai-models-from-development-to-production/) — fetched 2026-06-28 — supports: Qwak acquisition 2024-06-25, NASDAQ FROG, Sunnyvale HQ, Artifactory model registry + Xray model scanning; confidence: high
- [JFrog — Crunchbase / Tracxn / jfrog.com (web-search synthesis)](https://www.crunchbase.com/organization/jfrog-ltd) — fetched 2026-06-28 — supports: founded 2008 Netanya, founders, IPO Sept 2020 ticker FROG ~$509M at ~$3.9B, dual HQ; confidence: medium (secondary for market cap)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established public ownership (NASDAQ: FROG, IPO Sept 2020), founded 2008 (Ben Haim/Landman/Simon), dual HQ Sunnyvale+Netanya, Artifactory+Xray supply-chain spine, and Qwak (2024-06-25, ~$230M press) ML model-management angle. ownership_confidence high.
