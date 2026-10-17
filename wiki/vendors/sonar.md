---
title: Sonar
type: vendor
name: Sonar
slug: sonar
aka: [SonarSource, SonarQube, SonarQube Server, SonarQube Cloud, SonarCloud, SonarQube for IDE, SonarLint, SonarQube Community Build]
primary_category: software-supply-chain
also_listed_in: [promotion-gates]
website: https://www.sonarsource.com/
founded: 2008
hq: Geneva, Switzerland (US office Austin, Texas)
ownership_state: independent
owner: null
ownership_note: Private, VC/growth-backed. Last priced round $412M at a $4.7B valuation (2022-04-26), led by Advent International and General Catalyst with Insight Partners and Permira Growth Opportunities. No later priced round found as of 2026-10-16. Acquirer of Tidelift (announced 2024-12-17), AutoCodeRover (announced 2025-02-19) and Gitar (announced 2026-05-21), all on undisclosed terms.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "$412M at $4.7B valuation, 2022-04-26 (Advent International, General Catalyst; Insight Partners, Permira participating)"
market_position: {software-supply-chain: leader, promotion-gates: leader}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [platform, api, agent]
data_leaves_tenancy: partial
integrations: [github, gitlab, azure-devops, bitbucket, github-copilot, claude-code, cursor, openai-codex, azure-openai, aws-bedrock, litellm, ollama, vllm, carahsoft]
mcp_support: server
certifications: [soc2-type2, iso27001]
pricing_model: "LOC-based: Cloud Free (≤50k LOC) / Team from ~$32–34 per month (100k LOC) / Enterprise custom; Server editions per instance per year by LOC; Community Build free"
fs_traction: claimed
target_customer: any size, from individual developers to Fortune 100
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [sast, code-quality, quality-gates, ai-code-assurance, ai-generated-code, sca, agentic-remediation, mcp-server, aie-nyc-2026]
sources:
  - {claim: "$412M raise at $4.7B valuation, led by Advent and General Catalyst, 2022-04-26", url: "https://techcrunch.com/2022/04/26/sonarsource-raises-412m-to-scan-codebases-for-bugs-and-vulnerabilities/", date: 2022-04-26, confidence: high}
  - {claim: "Definitive agreement to acquire Tidelift announced 2024-12-17, terms undisclosed", url: "https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/", date: 2024-12-17, confidence: high}
  - {claim: "SonarQube Advanced Security (SCA + advanced SAST) announced 2025-03-11 as first step integrating Tidelift; GA May 2025", url: "https://devops.com/sonar-combines-sast-and-sca-tools-in-single-offer/", date: 2025-03-11, confidence: medium}
  - {claim: "AutoCodeRover acquisition announced 2025-02-19", url: "https://www.sonarsource.com/company/press-releases/sonar-acquires-autocoderover-to-supercharge-developers-with-ai-agents/", date: 2025-02-19, confidence: high}
  - {claim: "Gitar acquisition announced 2026-05-21, terms undisclosed, remains standalone product", url: "https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/", date: 2026-05-21, confidence: high}
  - {claim: "AI Code Assurance = AI-code project label + 'Sonar way for agentic AI' quality gate + badge", url: "https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview", date: 2026-10-16, confidence: high}
  - {claim: "AI CodeFix sends affected snippet to Sonar-selected OpenAI model or to customer's own Azure OpenAI/Bedrock/self-hosted LLM", url: "https://docs.sonarsource.com/sonarqube-server/2026.4/instance-administration/ai-features/enable-ai-codefix", date: 2026-10-16, confidence: high}
  - {claim: "Sonar Vortex and SonarQube Remediation Agent launched 2026-06-30", url: "https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/", date: 2026-06-30, confidence: high}
  - {claim: "ISO 27001:2022 and SOC 2 Type II; SonarQube Cloud hosted on AWS Frankfurt (default) or N. Virginia", url: "https://sonarsource.com/trust-center/", date: 2026-10-16, confidence: high}
  - {claim: "AIE NYC 2026 Platinum sponsor; five sessions incl. 'Who verifies the software factory?' (Manish Kapur, Sonar + Addy Osmani, Anthropic)", url: "https://www.sonarsource.com/company/press-releases/sonar-at-ai-engineer-new-york/", date: 2026-10-08, confidence: high}
  - {claim: "Plans and pricing: Cloud Free/Team/Enterprise; LOC-based", url: "https://www.sonarsource.com/plans-and-pricing/", date: 2026-10-16, confidence: medium}
---

# Sonar

> Primary category: [software-supply-chain](../categories/software-supply-chain.md). Also listed in [promotion-gates](../categories/promotion-gates.md).

**One-liner** — The incumbent code-quality and static-analysis platform (SonarQube), now pitched as the independent **verification layer for AI-generated code**: quality gates in CI that decide whether code written by humans or agents is allowed to merge.

**What it does** — SonarQube analyses source code for bugs, security vulnerabilities (SAST), code smells, duplication and test coverage, and enforces a **quality gate** on every pull request and branch. It comes in three forms: **SonarQube Server** (self-managed; the free open-source **Community Build** plus paid Developer, Enterprise and Data Center editions), **SonarQube Cloud** (formerly SonarCloud, SaaS), and **SonarQube for IDE** (formerly SonarLint, in-editor linting). Since 2024 the company has layered AI-era features on that base:

- **AI Code Assurance.** A project is flagged "contains AI-generated code" (a manual setting per project; the docs describe no auto-detection), which applies a stricter recommended gate, **"Sonar way for agentic AI"**, and the matching "Sonar agentic AI" quality profile. Projects that pass can show an external AI Code Assurance badge. First announced October 2024. This is a policy wrapper on the existing analysis engine, not a separate detector of AI-written code.
- **AI CodeFix.** LLM-generated fix suggestions for flagged issues.
- **SonarQube Advanced Security** (announced 2025-03-11, GA May 2025). Adds **SCA**: known CVEs in direct and transitive dependencies, licence compliance and SBOM generation, plus deeper SAST. Sonar described it as the first step in integrating **Tidelift**.
- **Agentic products in 2026.** **Sonar Vortex** (launched 2026-06-30) gives coding agents the organisation's rules and quality profiles before they write code and checks their output as they go. Sonar's own benchmark claims up to 36% fewer tokens on refactoring tasks; that is vendor marketing. The **SonarQube Remediation Agent** fixes issues assigned from the dashboard, re-verifies the fix and opens PRs. The **SonarQube Hunter Agent** targets logic-level security flaws. **Gitar** (acquired) does AI code review that fixes PRs and CI failures. Sonar also ships a **SonarQube MCP Server** and plugins for Claude Code, Cursor, Codex, Antigravity and GitHub Copilot CLI, so agents can query issues and quality-gate status themselves.

**Why it matters for this wiki.** The [software-supply-chain](../categories/software-supply-chain.md) trigger says the category becomes Day-1 once you ship AI-generated code. Sonar is the vendor whose whole 2025–26 strategy is built on that trigger. Its claim is that verification has to be **independent of the model that wrote the code**. Its quality gate is also the most widely deployed concrete form of a [promotion gate](../categories/promotion-gates.md): an automated pass/fail between "written" and "merged".

**Naming / provenance** — Founded **2008** in Geneva by Olivier Gaudin, Freddy Mallet and Simon Brandhof (Wikipedia; other profiles list two founders). The legal entity is still SonarSource Sàrl, but the company now markets itself as **Sonar**; the date of that rebrand was not found. Product renames: SonarCloud → **SonarQube Cloud**, SonarLint → **SonarQube for IDE**, and the free SonarQube Community Edition → **Community Build**. "Sonar" is a common brand name; check that a reference means the SonarQube company.

**Ownership & viability** — `independent`, private. The last priced round was **$412M at a $4.7B valuation** (announced 2022-04-26), led by Advent International and General Catalyst with Insight Partners and Permira participating. No later priced round was found. One third-party aggregator mentions a December 2025 dividend recapitalisation, but no primary source confirms it, so it is unverified. Sonar is an active **acquirer**:

| Target | What it adds | Announced | Closed | Terms |
|---|---|---|---|---|
| Tidelift | Open-source maintainer network and package data → SCA in Advanced Security | 2024-12-17 | Not found; integration under way by 2025-03-11 | Undisclosed |
| AutoCodeRover (NUS spinout) | Autonomous program-repair agent; Singapore R&D team | 2025-02-19 | Not found | Undisclosed |
| Gitar | AI-native PR review and CI-failure fixing; stays a standalone product | 2026-05-21 | Not found | Undisclosed (Gitar was a 9-person company with a $9M seed from Venrock, per BankInfoSecurity) |

Viability is strong: a large installed base, a growth-stage cap table and a steady acquisition pace. Several large security platforms could plausibly bid for it, and an IPO is another route, but nothing found suggests either is in progress. If it changed hands, the self-managed Server product would most likely carry on unchanged for existing customers.

**Positioning & differentiators** — `leader` in software-supply-chain for code quality and SAST. That rests on its claimed installed base (75% of the Fortune 100, 7M+ developers; vendor figures) and on Sonar's statement that it is a Gartner Magic Quadrant Leader (which MQ was not confirmed here). It is also `leader` in promotion-gates, because its PR quality gate is the de facto standard for automated merge gating.
- **Code quality plus security in one gate, versus security-only peers.** [snyk](snyk.md), [semgrep](semgrep.md), [checkmarx](checkmarx.md) and [veracode](veracode.md) lead with security findings. Sonar's centre of gravity is maintainability, reliability and coverage, with security added on top. For AI-generated code this matters, because much of the risk is plausible but wrong or unmaintainable code, not CVEs.
- **"Independent verifier" for AI code.** It sells itself as the model-agnostic check on code written by Copilot, Claude Code, Cursor and others, and contrasts that with platforms such as [github-advanced-security](github-advanced-security.md) whose AI writes and reviews the same code. AI Code Assurance and Vortex put this positioning into the product.
- **SCA arrived late and was bought in.** Dependency scanning came from Tidelift in 2025. Against [snyk](snyk.md), [endor-labs](endor-labs.md), [socket](socket.md), [sonatype](sonatype.md) or [black-duck](black-duck.md), Sonar's SCA is younger and less proven. Its advantage is one gate covering first-party code and dependencies together.
- **The free self-hosted tier is real.** Community Build runs fully on-prem at no cost, which matters to firms that will not upload source code to a SaaS scanner.

**Who should choose them / anti-fit** — Fits almost any firm that writes code. It is particularly strong for an engineering organisation that is rolling out AI coding assistants and needs a **measurable, auditable merge gate** to stop quality degrading, and for a firm that wants the analysis engine **self-hosted** next to its source. Where SonarQube is already installed, the AI features arrive as a licence or plan upgrade rather than a new vendor. **Anti-fit:** a firm whose main supply-chain worry is **malicious packages, dependency provenance or container hardening**. For that, look at [socket](socket.md), [endor-labs](endor-labs.md) or Chainguard; Sonar's SCA covers known CVEs and licences, not malware interdiction. Also not the right buy for a team wanting a best-of-breed security-first SAST with deep taint analysis as the primary purchase.

**Known weaknesses / gotchas** —
- **AI Code Assurance is a label plus a stricter gate.** It does not identify which lines an AI wrote, and a project is flagged by hand. Its value depends on teams turning it on and on gate thresholds that are actually enforced.
- **AI CodeFix sends code to an LLM** unless you configure your own model (see below). For proprietary quant code, decide this before enabling it.
- **Buying spree.** Tidelift, AutoCodeRover and Gitar are being integrated alongside several 2026 agent launches (Vortex, Remediation, Hunter). Expect packaging and SKU churn. Several of these features are Enterprise-plan only on Cloud.
- **Pricing is by lines of code.** Large monorepos can push you into high tiers. Cloud pricing is also inconsistent on Sonar's own page ($34 per month vs "$32 per month" for Team as of 2026-10-16).

**Deployment & data handling** — **SaaS** (SonarQube Cloud on AWS; EU/Frankfurt by default, US/N. Virginia available) or **self-managed** (SonarQube Server, on-prem or private cloud; SonarQube Server 2026.5 LTA, 2026-09-29, extends the agentic governance features to self-managed). Data leaving the tenancy is `partial`:
- Self-managed Server keeps source and analysis results in your environment.
- **AI CodeFix** with Sonar's hosted LLM sends the **affected code snippet** to the selected OpenAI model (GPT-5.1 / GPT-4o listed). Sonar says its LLM agreements prohibit training on customer code.
- You can point AI CodeFix at **your own** Azure OpenAI, AWS Bedrock or self-hosted gateway (Ollama, [litellm](litellm.md), vLLM). Current docs say a fully self-hosted setup needs no outbound internet, but community threads report older versions fetching prompts online. Check this for the version you run.

It runs out-of-band in CI and the IDE, so there is no runtime latency.

**Integrations & partnerships** — SCM/CI: GitHub, GitLab, Azure DevOps, Bitbucket. **MCP:** the SonarQube MCP Server exposes analysis, issues, quality gates, hotspots and coverage to AI coding agents. Agent plugins: Claude Code, Cursor, Codex, Antigravity, GitHub Copilot CLI. LLM back-ends for CodeFix: OpenAI (Sonar-hosted), Azure OpenAI, Bedrock and self-hosted. On 2026-10-13 Sonar joined OpenAI's "Daybreak" Cyber Partner Program. A September 2026 trade report says an expanded Carahsoft agreement takes Sonar's AI code verification into commercial markets across North America (secondary source). **AI Engineer New York 2026 (Oct 12–14):** Platinum sponsor, with five sessions in Sonar's press release. They include CEO Tariq Shaukat's main-stage "The Machine that Changed the World, vAI" and **"Who verifies the software factory?"**, given by Sonar's Manish Kapur with **Addy Osmani of Anthropic**.

**Compliance & FS traction** — **ISO 27001:2022** and **SOC 2 Type II** (announced February 2025; covers Server, Cloud and IDE; report under NDA via the trust center). FS evidence is `claimed`: **Goldman Sachs** is among the customers Sonar names in its 2026 press releases, alongside Nvidia, ServiceNow, Booking.com, AstraZeneca and Ford. No FS case study was reviewed. It scales down well, since the free tier and small Cloud plans suit a 20-developer quant shop. AI Code Assurance badges and gate history give a record of controls on AI-written code that can be shown to examiners. Whether that record is examiner-grade is unverified.

**Commercial** — Priced by **lines of code**. **SonarQube Cloud:** Free (private projects up to 50k LOC); Team from about $32–34 per month for 100k LOC, including Advanced Security; Enterprise at custom pricing, including Gitar, Vortex, Remediation Agent and Hunter Agent. Gitar is also a $20/user/month add-on on Team. **SonarQube Server:** Community Build is free and open source; Developer, Enterprise and Data Center are licensed per instance per year by LOC, with no public prices captured here. All figures are as of 2026-10-16.

## Open questions

- Close dates for the Tidelift, AutoCodeRover and Gitar acquisitions (only announcement dates found).
- Whether the December 2025 dividend recap reported by an aggregator happened, and any change in the cap table since 2022.
- Which Gartner Magic Quadrant Sonar claims Leader status in, and the year.
- Whether Tidelift's standalone subscription (maintainer payments, curated catalog) is still sold, or has been folded entirely into Advanced Security.
- Whether AI Code Assurance can now detect AI-generated code automatically, or remains a manual project flag.
- Named FS customers beyond Goldman Sachs, and whether any hedge funds or asset managers are public references.
- Self-managed Server prices by edition and LOC band.

## Sources

- [SonarSource raises $412M (TechCrunch)](https://techcrunch.com/2022/04/26/sonarsource-raises-412m-to-scan-codebases-for-bugs-and-vulnerabilities/) — fetched 2026-10-16 — supports: last round, valuation, investors; confidence: high
- [Sonar to Acquire Tidelift (press release)](https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/) — fetched 2026-10-16 — supports: Tidelift announcement 2024-12-17; confidence: high
- [Sonar combines SAST and SCA tools in single offer (DevOps.com)](https://devops.com/sonar-combines-sast-and-sca-tools-in-single-offer/) — fetched 2026-10-16 — supports: Advanced Security as Tidelift integration; confidence: medium
- [Sonar Acquires AutoCodeRover (press release)](https://www.sonarsource.com/company/press-releases/sonar-acquires-autocoderover-to-supercharge-developers-with-ai-agents/) — fetched 2026-10-16 — supports: AutoCodeRover deal 2025-02-19; confidence: high
- [Sonar Acquires Gitar (press release)](https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/) and [BankInfoSecurity](https://www.bankinfosecurity.net/sonar-acquires-gitar-to-eliminate-ai-code-review-gaps-a-31798) — fetched 2026-10-16 — supports: Gitar deal 2026-05-21, Gitar size/seed; confidence: high / medium
- [AI Code Assurance overview (docs)](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview) — fetched 2026-10-16 — supports: how AI Code Assurance works; confidence: high
- [Enable AI CodeFix (docs, Server 2026.4)](https://docs.sonarsource.com/sonarqube-server/2026.4/instance-administration/ai-features/enable-ai-codefix) — fetched 2026-10-16 — supports: data flow, BYO-LLM; confidence: high
- [Sonar Launches Sonar Vortex and SonarQube Remediation Agent (press release)](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/) — fetched 2026-10-16 — supports: 2026 agentic products; confidence: high (vendor; benchmark claim low)
- [Sonar trust center](https://sonarsource.com/trust-center/) — fetched 2026-10-16 — supports: ISO 27001, SOC 2 Type II, hosting regions; confidence: high
- [Sonar at AI Engineer New York (press release)](https://www.sonarsource.com/company/press-releases/sonar-at-ai-engineer-new-york/), [ai.engineer/nyc](https://www.ai.engineer/nyc), [schedule](https://www.ai.engineer/nyc/schedule) — fetched 2026-10-16 — supports: AIE NYC sponsorship, talks, speakers; confidence: high
- [Plans and pricing](https://www.sonarsource.com/plans-and-pricing/) — fetched 2026-10-16 — supports: pricing tiers; confidence: medium (internal inconsistency)
- Cached: `raw/sources/2026-10-16--sonar--acquisitions-funding.md`, `raw/sources/2026-10-16--sonar--products-data-pricing.md`, `raw/sources/2026-10-16--sonar--aie-nyc-press-and-schedule.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
