---
title: Mimecast
type: vendor
name: Mimecast
slug: mimecast
aka: [Mimecast Limited, Code42, Incydr, Aware, Elevate Security]
primary_category: dlp
also_listed_in: [comms-surveillance]
website: https://www.mimecast.com/
founded: 2003
hq: London, UK (US HQ Lexington, MA)
ownership_state: pe-owned
owner: Permira
ownership_note: Permira took Mimecast private for $5.8B, completed May 2022 (previously NASDAQ:MIME). Has since acquired Elevate Security (Jan 2024), Code42 (announced 2024-07) and Aware (2024) to build out a "human risk management" platform.
acquisition: {announced: 2021-12, closed: 2022-05, price: $5.8B}
funding_total: null
last_funding: null
market_position: {dlp: legacy-incumbent}
deployment_model: [saas]
form_factor: [inline-proxy, platform, agent]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: verified
target_customer: mid-market to enterprise
last_verified: 2026-08-26
verify_after: null
tags: [email-security, archiving, insider-risk, dlp, human-risk-management, sec-17a-4, finra, pe-owned]
sources:
  - {claim: "Permira acquired Mimecast for $5.8B, completed May 2022", url: "https://www.thedeal.com/mergers-acquisitions/permiras-mimecast-adds-on-pe-backed-code42/", date: 2026-08-26, confidence: medium}
  - {claim: "Mimecast acquired Code42 (cloud-native insider threat management and DLP) to extend its human risk management platform", url: "https://www.mimecast.com/resources/press-releases/mimecast-announces-acquisition-of-code42/", date: 2026-08-26, confidence: high}
  - {claim: "Mimecast acquired Aware (collaboration security) and will embed it in the HRM platform", url: "https://www.mimecast.com/resources/press-releases/mimecast-acquires-aware/", date: 2026-08-26, confidence: high}
  - {claim: "Mimecast Cloud Archive is a SEC 17a-4 validated, tamper-proof WORM archive; Cloud Archive and Supervision are listed on the FINRA Compliance Vendor Directory", url: "https://www.mimecast.com/content/sec-rule-17a-4-compliance/", date: 2026-08-26, confidence: medium}
---

# Mimecast

> Primary category: [dlp](../categories/dlp.md). Also listed in [comms-surveillance](../categories/comms-surveillance.md) — note the category's scope boundary: Mimecast is primarily **capture/archival plus supervisory review**, not a pure surveillance-analytics tool.

**One-liner** — Email security and immutable archiving for regulated firms, now assembled into a "human risk management" platform that adds insider-risk DLP (Code42) and collaboration-channel capture (Aware) — the vendor most likely to already hold your firm's SEC 17a-4 books-and-records archive.

**What it does** — Three things that a CTO at an alternative manager should keep separate in their head:

1. **Email security.** Inline secure email gateway: anti-phishing, impersonation/BEC protection, URL and attachment defence, and outbound email DLP. This is the original business.
2. **Compliance archiving.** **Mimecast Cloud Archive** is a WORM (write-once-read-many) archive marketed as **SEC Rule 17a-4 validated** and listed, together with Mimecast Supervision, on the **FINRA Compliance Vendor Directory**. For a registered adviser or broker-dealer this is the books-and-records obligation, not a security product — retention periods, immutability, indexed search, and auditor access on demand.
3. **Human risk management.** The post-take-private strategy, assembled by acquisition: **Elevate Security** (Jan 2024 — per-user risk scoring), **Code42** (announced July 2024 — Incydr, cloud-native insider-risk detection and DLP across endpoint, cloud and email), and **Aware** (2024 — capture and risk analysis of Slack, Teams and other collaboration channels). Mimecast Engage is the consolidated platform brand.

**Why it belongs in an AI-governance wiki.** Two reasons, both practical. First, the exfiltration surface it covers — email, endpoint, and now Slack/Teams — is exactly where a user pastes MNPI *out of* a chatbot or *into* an unsanctioned one; Code42's Incydr watches file and data movement rather than prompt content, so it is complementary to, not a substitute for, the AI-native tools in [dlp](../categories/dlp.md) such as [prompt-security](prompt-security.md) or [nightfall-ai](nightfall-ai.md). Second, the Aware acquisition matters because **AI assistants generate records in collaboration channels**: Copilot and Claude output inside Teams or Slack is arguably a business communication subject to retention and supervision, and the capture layer is where that obligation lands.

**Naming / provenance** — Founded 2003 in London by Peter Bauer and Neil Murray. IPO on NASDAQ (MIME) in 2015; taken private 2022. The acquired brands are being retired into Mimecast branding, but Code42/Incydr and Aware names still appear in documentation and in the market.

**Ownership & viability** — `pe-owned`. **Permira** completed a **$5.8B** take-private in **May 2022**. Four years into the hold, having made three acquisitions, the pattern is a classic PE roll-up being assembled for resale or IPO. Financially sound; the risks are commercial, not existential — **price increases at renewal and roadmap consolidation are the documented pattern for this shape of asset**, and Mimecast contracts are notoriously sticky because the archive is a records-retention dependency you cannot casually migrate.

**Positioning & differentiators** —
- **The archive is the moat.** Once seven years of retained communications sit in Mimecast under a 17a-4 attestation, switching cost is enormous and the incumbency is close to permanent. This is the single most important commercial fact on this page.
- **Regulatory pedigree.** FINRA Compliance Vendor Directory listing and 17a-4 validation are the specific credentials an examiner asks about. Very few of the AI-native [dlp](../categories/dlp.md) vendors have anything comparable.
- **Versus Microsoft Purview.** The real competitive question for most firms is whether E5's built-in retention, eDiscovery and DLP are sufficient. Mimecast's counter-arguments are independence from the mail platform being protected (a Microsoft outage or compromise does not take the archive with it) and depth of supervisory review. Both are legitimate; the cost delta is not trivial.
- **Human-risk consolidation is unfinished.** Three acquisitions in roughly eighteen months means integration debt. Buying "the platform" today means buying products that were separate companies very recently.

**Who should choose them / anti-fit** — Fits a **registered adviser or broker-dealer with SEC/FINRA books-and-records obligations** that wants archive, supervision, email security and insider-risk in one contract — an extremely common alternative-manager profile. **Anti-fit:** an unregulated firm with no retention obligation, where Microsoft E5 native capability is adequate and cheaper; and any firm whose primary concern is *prompt-level* AI data loss rather than file and message movement — Mimecast does not inspect model traffic.

**Known weaknesses / gotchas** — Integration debt across the acquired products. Renewal pricing pressure under PE ownership. **Vendor lock-in via the archive is severe and should be priced into the decision at purchase, not discovered at renewal** — ask about export format and egress cost before signing. Mimecast also suffered a supply-chain compromise in 2021 (SolarWinds-related threat actor, certificate for Microsoft 365 connections) — old, remediated, and disclosed, but relevant history for a vendor holding the firm's complete communications record.

**Deployment & data handling** — SaaS only. **Data does leave the tenancy by design** — that is what an independent archive is. Data-residency choices (UK/EU/US/other regions) exist and are a required diligence item; specific region availability and retention mechanics are **unverified** here.

**Integrations & partnerships** — Microsoft 365 and Google Workspace mail flow, Slack/Teams capture via Aware, SIEM export, and integration with surveillance vendors that analyse the archive it holds — several vendors in [comms-surveillance](../categories/comms-surveillance.md) ingest from Mimecast rather than replacing it. MCP support unverified.

**Compliance & FS traction** — `verified` at the category level: FINRA Compliance Vendor Directory listing for Cloud Archive and Supervision, and 17a-4 validation, are specific to regulated financial firms and are the reason for this page. Individual customer references not confirmed here.

**Commercial** — Not public. Per-seat subscription, tiered by module; archiving is typically priced separately from email security.

## Open questions

- Which independent assessor issued the 17a-4 validation, and its current date — this is the claim an examiner will test.
- Data residency regions available; archive export format and egress cost on termination.
- How far Code42/Incydr and Aware are actually integrated into Mimecast Engage versus separately administered.
- Whether Mimecast has any **prompt-level** AI-interaction capture (i.e. archiving what employees send to and receive from AI assistants) — the obvious extension of a records obligation into AI, and currently unknown.
- Permira exit timing; renewal-pricing trajectory since 2022.
- Named hedge-fund/asset-manager references.

## Sources

- [Permira's Mimecast Adds On PE-Backed Code42 (The Deal)](https://www.thedeal.com/mergers-acquisitions/permiras-mimecast-adds-on-pe-backed-code42/) — fetched 2026-08-26 — supports: Permira $5.8B take-private, Code42 add-on; confidence: medium
- [Mimecast Announces Acquisition of Code42 (Mimecast)](https://www.mimecast.com/resources/press-releases/mimecast-announces-acquisition-of-code42/) — fetched 2026-08-26 — supports: Code42/Incydr scope and rationale; confidence: high (primary)
- [Mimecast acquires Aware (Mimecast)](https://www.mimecast.com/resources/press-releases/mimecast-acquires-aware/) — fetched 2026-08-26 — supports: Aware acquisition, collaboration capture; confidence: high (primary)
- [SEC Rule 17a-4 Compliance (Mimecast)](https://www.mimecast.com/content/sec-rule-17a-4-compliance/) — fetched 2026-08-26 — supports: WORM archive, 17a-4 validation claim, FINRA vendor directory listing; confidence: medium (vendor marketing — the underlying attestation was not independently retrieved)
- Cached: `raw/sources/2026-08-26--mimecast--ownership-acquisitions-and-fs-compliance.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier B, score 6); promoted to inclusion because the SEC 17a-4 / FINRA archiving role makes it directly relevant to registered advisers, and because it absorbed Code42 — a separate Tier B candidate, covered here rather than as its own page.
