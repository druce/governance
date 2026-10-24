---
title: Clarier
type: vendor
name: Clarier
slug: clarier
aka: [Clarier Technologies, Clarier Technologies LLC]
primary_category: ai-access-governance
also_listed_in: [ai-governance-platform, vendor-risk]
website: "https://clarier.ai"
founded: null
hq: "Hollywood, FL (per founder letter; unconfirmed)"
ownership_state: independent
owner: null
ownership_note: "Early-stage, founder-led (Adam Pfefer, Founder & CEO). No funding round, investors or acquisition found as of 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {ai-access-governance: niche-specialist, ai-governance-platform: niche-specialist, vendor-risk: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: partial
integrations: [Microsoft Entra ID, Google Workspace, Beyond Identity, Cato Networks, Palo Alto Prisma, Cisco Umbrella, Zscaler, Netskope, CrowdStrike, SentinelOne, ThreatLocker, Fortinet, Cyberhaven, Microsoft Defender for Cloud Apps, Proofpoint, Claude (MCP)]
mcp_support: server
certifications: [SOC 2 Type I (vendor-stated, 2026-07-22; Type II in progress)]
pricing_model: null
fs_traction: claimed
target_customer: alternative investment managers (hedge funds, PE, asset managers) and PE portfolio companies that need an AI-tool inventory, approval workflow and exam/DDQ evidence
last_verified: 2026-10-24
verify_after: null
tags: [shadow-ai, ai-inventory, ai-vendor-diligence, ai-approval-workflow, alternative-investments, sec-exam-readiness, ddq, survey-write-in]
sources:
  - {claim: "Product capabilities (shadow-AI discovery, spend, vendor trust reports, approval workflow, evidence log); analyst-led deployment; target market; no agent/MCP/posture language on homepage", url: "https://clarier.ai/", date: 2026-10-24, confidence: low}
  - {claim: "Team: Adam Pfefer Founder & CEO (ex-hedge-fund IT), Chirag Gupta, Roberto Jusay, Jake Myers; Hollywood, FL", url: "https://clarier.ai/about", date: 2026-10-24, confidence: medium}
  - {claim: "Discovery integrations across IdP, SSE/DNS, EDR, DLP and email security", url: "https://clarier.ai/integrations", date: 2026-10-24, confidence: low}
  - {claim: "Remote MCP connector (OAuth 2.1, up to 25 tools) documented for Claude", url: "https://clarier.ai/docs", date: 2026-10-24, confidence: medium}
  - {claim: "SOC 2 Type I 2026-07-22 (Johanson LLP), Type II in progress; data retention and model-use policies", url: "https://clarier.ai/trust", date: 2026-10-24, confidence: low}
  - {claim: "Silver Regulatory Associates launches AI governance program for investment advisers with Clarier (2026-08-11)", url: "https://clarier.ai/news/silver-regulatory-associates", date: 2026-08-11, confidence: medium}
---

# Clarier

> Primary category: [ai-access-governance](../categories/ai-access-governance.md). Also listed in [ai-governance-platform](../categories/ai-governance-platform.md) and [vendor-risk](../categories/vendor-risk.md).

**One-liner** — A young AI-governance platform built for hedge funds, PE firms and their portfolio companies. It finds the AI tools staff actually use by reading telemetry from the firm's existing security stack, grades the AI vendors behind them, routes approval requests through compliance, and keeps an evidence log for SEC exams and allocator DDQs.

**Survey placement** — Written in once in the October 2026 CTO survey under Q35 "AI-SPM / Agent Security Posture" (1 respondent, in production). Clarier does not market agent or AI-workload posture management. Its homepage does not mention agents, MCP or posture. The product governs *employee use of third-party AI tools* and the vendors behind them, so the wiki lists it under [ai-access-governance](../categories/ai-access-governance.md) (shadow-AI), not [ai-spm](../categories/ai-spm.md). The respondent's placement is a useful signal that buyers lump "AI inventory" tools together with posture tools. This overlap is the AI-SPM vs shadow-AI boundary.

**What it does** (vendor-described, 2026-10-24):
- **Shadow-AI discovery.** Inventories AI tools in use, including unapproved tools and personal accounts holding company data. It pulls from existing telemetry, not employee self-reporting. Listed sources are the IdP (Entra ID, Google Workspace incl. Gemini usage, Beyond Identity), SSE/DNS (Zscaler, Netskope, Palo Alto Prisma, Cisco Umbrella, Cato), EDR (CrowdStrike, SentinelOne, ThreatLocker, Fortinet), DLP and email (Cyberhaven, Defender for Cloud Apps, Proofpoint). It also maps AI embedded in existing tools, delivered as add-ons, or built internally.
- **Spend visibility.** Flags untracked AI spend and redundant subscriptions.
- **Vendor trust reports.** Grades an AI vendor on model-training use, data retention, breach history, SOC 2 status and subprocessors, against gating criteria the firm sets (e.g. "zero retention required").
- **Approval workflow + evidence log.** Requests route through compliance review. Every discovery, review and approval is logged and exportable for DDQs, SEC exams, allocator inquiries and board reporting.
- **Continuous oversight.** Watches for vendor term changes and new tools between reviews.
- **MCP connector.** A remote MCP server (OAuth 2.1, up to 25 tools) lets Claude or other MCP clients query the AI estate, review vendor risk and submit governed changes with confirmation. This is an interface *to* Clarier. Clarier does not control MCP traffic.

**Naming / provenance** — Legal entity Clarier Technologies, LLC. Founding date not stated (site copyright 2026; first dated public item found is the 2026-08-11 Silver announcement). Founder and CEO Adam Pfefer previously ran IT inside a hedge fund. G2 describes the team as having "two decades running technology inside a hedge fund". Not to be confused with **Clarity AI** (ESG data) or **Clarista** (wealth-data platform), which turn up in the same searches.

**Ownership & viability** — `independent`, early stage. No funding round, investors or headcount found (2026-10-24). The G2 listing has zero ratings. Viability risk is high in the usual seed-stage way: small team and a narrow vertical. Shadow-AI discovery is also being folded into SSE suites ([zscaler](zscaler.md), [netskope](netskope.md)) and into larger AI-usage-control startups. Plausible exits are an acquisition by an alt-industry compliance or cyber provider, or a GRC vendor. If it exits, customers keep only what they can export, so check evidence-export formats up front.

**Positioning & differentiators** —
- **Vertical, compliance-first.** Peers such as [harmonic-security](harmonic-security.md), [witnessai](witnessai.md), [nudge-security](nudge-security.md) and [portal26](portal26.md) are horizontal and security-team-led, and several enforce inline (browser or proxy). Clarier is built for the CCO/COO of an RIA. Its output is an approval record and exam evidence, not a block or redact action.
- **Reads your stack, doesn't sit inline.** Discovery comes from logs you already have (SSE, EDR, IdP). That makes deployment fast but means no real-time prompt-level control. Pair it with an inline tool or [dlp](../categories/dlp.md) if you need enforcement.
- **AI-vendor diligence built in.** The trust report overlaps lightweight [vendor-risk](../categories/vendor-risk.md) tooling, but it covers AI vendors only (training use, retention).
- **Channel via compliance consultants.** Silver Regulatory Associates (compliance consultant to SEC-registered advisers and private fund managers) launched an AI governance program on Clarier (2026-08-11). This is the same route alt managers use to buy compliance tech.

**Who should choose them / anti-fit** — Fits a **small or mid-sized hedge fund, PE firm or RIA** that already runs a modern SSE/EDR stack, has an AI acceptable-use policy, and needs to *prove* to the SEC and LPs what AI is in use and who approved it. **Anti-fit:** firms that need inline enforcement (prompt DLP, redaction, blocking). Also firms looking for posture management of their *own* agents, models or AI workloads (see [ai-spm](../categories/ai-spm.md)). Also bank-affiliated firms needing SR 11-7 model risk management (see [ai-governance-platform](../categories/ai-governance-platform.md) leaders such as [credo-ai](credo-ai.md)), and large enterprises wanting a mature, multi-year vendor.

**Known weaknesses / gotchas** —
- **Not AI-SPM.** Despite the survey placement, there is no claimed coverage of agent permissions, model/workload misconfiguration or AI-pipeline posture.
- **Out-of-band only.** Discovery quality depends on the telemetry sources the firm already has. A firm without SSE/DNS logging will see less.
- **Very thin public record.** No independent reviews, no named customers beyond the Silver channel partner, and all claims are vendor-stated.
- **Naming inconsistency.** The homepage banner says "NewSilver Regulatory Associates", the announcement page says "Silver Regulatory Associates". Confirm the partner's actual name.

**Deployment & data handling** — SaaS (hosting provider and region not named). The homepage says "analyst-led deployment with data staying in your environment" and a few hours of the client's time. The Trust page says raw integration data and file/message content are not persisted, and raw AI inputs/outputs are not retained, but metadata is. So inventory metadata does leave the tenancy, hence `partial`. It uses enterprise LLM providers with pinned model versions and no-training contracts. Decision scores come from a fixed formula, not the model. Audit logs are retained permanently. Customer data is deleted 30 days after termination. Encryption is TLS 1.2+ in transit and AES-256 at rest.

**Integrations & partnerships** — Discovery connectors listed above. MCP **server** (remote connector) documented for Claude. Channel partner: Silver Regulatory Associates (2026-08-11). It has a partner program. No cloud-marketplace listing found.

**Compliance & FS traction** — SOC 2 **Type I** (report dated 2026-07-22, Johanson LLP), Type II observation underway. Vendor-stated, report under NDA. **FS traction claimed and structural:** the site says Clarier "runs AI governance for SEC-registered advisers and PE-backed portfolio companies" (no count, no names). Exam-readiness features (evidence export for SEC exams and DDQs) are the core of the product.

**Commercial** — Pricing not public (demo-led). Model unknown.

## Open questions

- Founding date, funding, headcount, named customers.
- Hosting provider, data region, subprocessor list; what "data staying in your environment" means technically, given that it is SaaS.
- Whether any agent inventory or posture features exist or are on the roadmap (would justify an ai-spm cross-list).
- Pricing model (per seat, per firm, via consultant bundle?).
- Correct name of the channel partner (NewSilver vs Silver Regulatory Associates).

## Sources

- [Clarier homepage](https://clarier.ai/): fetched 2026-10-24. Supports: capabilities, deployment claim, target market. Confidence: low (vendor marketing).
- [Clarier About](https://clarier.ai/about): fetched 2026-10-24. Supports: team, Hollywood FL. Confidence: medium.
- [Clarier Integrations](https://clarier.ai/integrations): fetched 2026-10-24. Supports: discovery data sources. Confidence: low.
- [Clarier Docs](https://clarier.ai/docs): fetched 2026-10-24. Supports: MCP connector. Confidence: medium.
- [Clarier Trust](https://clarier.ai/trust): fetched 2026-10-24. Supports: SOC 2 Type I, data handling. Confidence: low (self-reported).
- [Silver Regulatory Associates launches AI governance program with Clarier](https://clarier.ai/news/silver-regulatory-associates): dated 2026-08-11, fetched 2026-10-24. Confidence: medium (vendor-published).
- [G2 listing](https://www.g2.com/products/clarier/discuss): via search snippet 2026-10-24 (page 403). Supports: telemetry-based discovery, hedge-fund team background. Confidence: low.
- Cached: `raw/sources/2026-10-24--clarier--homepage-about-integrations.md`, `raw/sources/2026-10-24--clarier--trust-and-silver-partnership.md`

## History

- [2026-10-24] Page created and researched. Triggered by one in-production write-in under Q35 "AI-SPM / Agent Security Posture" in the October 2026 CTO survey. Primary set to ai-access-governance (shadow-AI discovery is the headline capability). Cross-listed in ai-governance-platform (policy/approval/evidence) and vendor-risk (AI vendor trust reports). Not listed in ai-spm, because the vendor makes no posture claim.
