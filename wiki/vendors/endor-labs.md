---
type: vendor
name: Endor Labs
slug: endor-labs
categories: [software-supply-chain]
layer: foundation
aliases: []
website: https://www.endorlabs.com
founded: 2021
hq: Palo Alto, California, USA (also Bangalore, India)
ownership: independent
ownership_detail: Venture-backed, independent as of 2026-06-28. $93M Series B (Apr 2025) led by DFJ Growth.
ownership_confidence: high
funding_total: ~$163M (Series A $70M 2023 + Series B $93M 2025; excludes seed converted into Series A)
last_funding: Series B, $93M, 2025-04-23 (DFJ Growth)
deployment: [saas, api, sdk]
target_customer: enterprise (esp. orgs shipping AI-generated code; OpenAI, Snowflake, Dropbox cited)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [sca, aspm, reachability, ai-code-security, sbom]
---

# Endor Labs

**One-liner** — Reachability-based software composition analysis (SCA) that tells you whether a vulnerable open-source dependency is actually *callable* in your code, now extended into governance and scanning for AI-generated code.

**Categories** — [software-supply-chain](../categories/software-supply-chain.md) (primary)

## What it does
Endor Labs scans your open-source dependencies and code for known vulnerabilities, but its signature move is **function-level reachability analysis**: instead of alerting on every CVE in every transitive dependency, it determines whether the vulnerable function is actually reachable from your application's code paths. The vendor claims this removes roughly 80% of the noise traditional SCA tools generate. Beyond SCA, the platform covers operational risk (unmaintained/unused/outdated dependencies), SBOM and VEX generation, secrets, SAST, CI/CD posture, and — increasingly the headline — **AI code governance**: reviewing AI-generated code for vulnerabilities, recommending and auto-applying fixes, with IDE/agent plugins (Cursor, GitHub Copilot) that scan in real time. It also markets MCP server security for agentic development workflows.

## Where it sits in the stack
Lives in the [software-supply-chain](../categories/software-supply-chain.md) category at the **foundation** layer — the dependency/code-provenance substrate everything else builds on. Its lethal-trifecta role is mostly **untrusted input**: third-party (and now AI-generated) code is an untrusted-input vector into your build. The AI-generated-code angle is the reason it matters to a 2026 buyer: if developers are accepting LLM-suggested code and dependencies wholesale, Endor's reachability + AI-code scanning is positioned as the gate that catches vulnerable/hallucinated packages before they ship.

## Deployment & architecture
SaaS platform with API and SDK/CLI integrations into SCMs (GitHub/GitLab), CI/CD pipelines, and IDEs/AI coding assistants (Cursor, Copilot plugins). Outputs SBOM/VEX. Integrates into developer workflow rather than running as a network inline proxy.

## Positioning & differentiators
Known for **reachability** done at function granularity, which is its main differentiator versus manifest-level SCA. Versus [snyk](snyk.md) (broad developer-security suite) and [socket](socket.md) (supply-chain/malware-focused, dependency behavior), Endor competes on prioritization accuracy — "is this actually exploitable in my code." Versus [semgrep](semgrep.md) (SAST/custom rules) it is dependency- and reachability-led rather than pattern-matching first. Versus full ASPM players [apiiro](apiiro.md) and [legit-security](legit-security.md), Endor is narrower and deeper on the dependency/SCA + AI-code-review problem rather than broad SDLC posture orchestration. [aikido-security](aikido-security.md) overlaps as an all-in-one dev-security suite at a lower price point.

## Ownership, funding & M&A
Independent, venture-backed. Founded 2021 by Varun Badhwar (CEO) and Dimitri Stiliadis; out of stealth October 2022. **$70M Series A** (Aug 2023, led by Lightspeed). **$93M Series B** (announced 2025-04-23, led by DFJ Growth, with Salesforce Ventures, Lightspeed, Coatue, Dell Technologies Capital, Section 32, Citi Ventures); ~$163M raised total. No acquisition; remains independent as of 2026-06-28. Confidence: high (multiple primary/press sources, dated).

## CTO / hedge-fund lens
**Day-1 *if* you are shipping AI-generated code at any volume**; otherwise Day-2. For a fund that lets engineers use Copilot/Cursor and pull open-source freely, Endor's pitch — catch vulnerable/unreachable-vs-reachable dependencies and review AI-written code before merge — maps directly onto the new risk. The reachability noise-reduction is genuinely useful for a small AppSec team that cannot triage thousands of CVEs. For a shop that writes little code and buys most software, this is lower priority than runtime/data controls. `hedge_fund_fit: medium` — high for code-shipping funds, low for pure buyers.

## Competitors / alternatives
[snyk](snyk.md), [socket](socket.md), [semgrep](semgrep.md), [apiiro](apiiro.md), [legit-security](legit-security.md), [aikido-security](aikido-security.md)

## Open questions / to verify
- Exact pricing/packaging for the AI-code-governance module vs core SCA.
- Depth/maturity of the marketed MCP server security capability.
- Current valuation (undisclosed; "orders of magnitude higher" than Series A per CEO).

## Sources
- [Endor Labs lands $93M (TechCrunch)](https://techcrunch.com/2025/04/23/endor-labs-which-builds-tools-to-scan-ai-generated-code-for-vulnerabilities-lands-93m/) — fetched 2026-06-28 — supports: Series B $93M/Apr 2025, founders, Palo Alto+Bangalore HQ, $163M total, AI-code positioning; confidence: high
- [Endor Labs $70M Series A (vendor blog)](https://www.endorlabs.com/learn/series-a-70m-raise) — fetched 2026-06-28 — supports: Series A details, reachability SCA / AI code governance / operational-risk pillars; confidence: medium (marketing)
- [Endor Labs raises $70M (TechCrunch)](https://techcrunch.com/2023/08/03/endor-labs-which-helps-companies-secure-their-open-source-packages-raises-70m/) — fetched 2026-06-28 — supports: Series A, open-source dependency security positioning; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Palo Alto HQ, founded 2021, $163M total funding ($70M Series A 2023 / $93M Series B Apr 2025, DFJ Growth), independent. Positioned as reachability SCA + AI-generated-code governance. ownership_confidence raised to high.
