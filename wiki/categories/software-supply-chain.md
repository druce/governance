---
type: category
name: Software Supply Chain & Coding Security
slug: software-supply-chain
layer: foundation
priority: day-2
trifecta_role: untrusted-input
maps_to_seed_doc: Software Supply Chain & Coding Security
maps_to_seed_csv: Software supply chain
vendor_count: 11
status: drafted
last_updated: 2026-06-28
---

# Software Supply Chain & Coding Security

## Business objective

Secure and govern the software supply chain — the code you write, the dependencies
you pull in, and the pipeline that builds and ships it. The seed doc calls it
**the safety inspector for code**: it scans for vulnerabilities, bad or malicious
dependencies, leaked secrets, and provenance — **including the code your copilots
and citizen developers generate.** This spans SAST (static analysis), SCA
(software composition / open-source dependency analysis), secrets scanning,
malicious-package detection, and pipeline/SBOM/provenance controls.

## When you need it

**Day 1 if you're shipping AI-generated code; otherwise Day 2.** This is the seed's
explicit conditional, and it matters for a hedge fund: the moment developers use
Copilot, Cursor, or coding agents, the volume of machine-written code — and the
risk of hallucinated or typosquatted dependencies and silently introduced
vulnerabilities — jumps. AI both *raises* the risk (more code, faster, less human
review) and is the input these tools must vet. If your fund builds and deploys
software, treat this as Day 1; if you only consume SaaS, it's a lower priority.

## Lethal-trifecta role

Best mapped to **untrusted input**: AI-generated code and the open-source
dependencies it reaches for are untrusted content entering your trusted build and
runtime environments. Supply-chain security is where that input gets vetted before
it can execute — catching a poisoned package or an injected vulnerability before it
becomes a foothold an attacker (or a rogue agent) can chain into data access or
egress. Sits at the boundary of the **green zone** (production/build systems);
also reinforces [[promotion-gates]] between experiment and production.

## Vendors

- [[snyk]] — broad developer-first platform spanning SAST, SCA, container, and IaC.
- [[semgrep]] — fast customizable static analysis (SAST + secrets), strong OSS roots.
- [[endor-labs]] — reachability-based SCA and supply-chain/CI risk; AI-code focus.
- [[socket]] — real-time malicious-dependency / supply-chain attack detection.
- [[apiiro]] — application-security posture and code-to-runtime risk graph.
- [[legit-security]] — SDLC/pipeline security and SBOM/provenance governance.
- [[aikido-security]] — consolidated all-in-one AppSec for smaller teams.
- [[sonatype]] — open-source governance / artifact firewall (Nexus heritage).
- [[jfrog]] — artifact management and software-supply-chain platform (Artifactory).
- [[github-advanced-security]] — native code/secret/dependency scanning in GitHub.
- [[gitlab]] — GitLab Ultimate's built-in security scanning across the DevOps platform.

## Consolidation / M&A dynamics

No specific seed M&A flags for this category, but it's an active and crowded space
with frequent funding rounds and acquisitions as platforms converge SAST + SCA +
secrets + pipeline into single "AppSec platform" offerings. The notable recent
shift is positioning around AI-generated code and AI coding agents, with several
vendors ([[endor-labs]], [[socket]], [[semgrep]]) marketing AI-code-specific
detection. Native platform options ([[github-advanced-security]], [[gitlab]]) pull
buyers toward whoever already hosts their repos.

## Adjacent categories

- [[secrets-management]] — secrets scanning here finds leaked credentials; secrets managers store them properly.
- [[promotion-gates]] — supply-chain scans are a natural gate between experiment and production.
- [[policy-as-code]] — pipeline policy enforcement (e.g. block builds failing a scan).
- [[ephemeral-environments]] — short-lived build/dev compute these tools protect.

## Survey

**Question:** Which software supply chain / coding security tool does your firm use
or evaluate, including for AI-generated code?

**Answer options (multi-select):**
- Snyk
- Semgrep
- Endor Labs
- Socket
- Apiiro
- Legit Security
- Aikido Security
- Sonatype
- JFrog
- GitHub Advanced Security
- GitLab Ultimate
- Other (Please Specify)

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:** Long option list — relevant mainly to firms that
actually build software, so route this question behind a "do you develop in-house?"
filter to avoid noise from pure SaaS consumers. Snyk, GitHub Advanced Security, and
GitLab Ultimate are the table-stakes/native options; Socket, Endor, Apiiro, and
Legit are more specialized. Native platform choice (GitHub vs GitLab) strongly
predicts the answer. Aikido skews to smaller teams.

## Open taxonomy questions

- This page bundles SAST, SCA, secrets scanning, and pipeline/SBOM security under
  one slug; if respondents shop these separately we may need sub-categories.
- Overlap with [[secrets-management]] on secrets detection vs storage — keep the
  "find" vs "vault" distinction explicit.
