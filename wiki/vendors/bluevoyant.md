---
title: BlueVoyant
type: vendor
name: BlueVoyant
slug: bluevoyant
aka: [BlueVoyant AI, BlueVoyant MDR, BlueVoyant Supply Chain Defense, BlueVoyant Third-Party Risk, Conquest Cyber, Marclay Associates]
primary_category: ai-soc-analysts
also_listed_in: [vendor-risk]
website: https://www.bluevoyant.com/
founded: 2017
hq: null
ownership_state: independent
owner: null
ownership_note: "Private, venture/growth backed. Series D $250M (2021) at >$1B valuation led by Liberty Strategic Capital (Mnuchin). Series E >$140M led by Liberty Strategic Capital and ISTARI, raised alongside the Conquest Cyber acquisition (coverage dated 2023-11-30). Co-founder Jim Rosenthal moved from CEO to board chair when John Hernandez became CEO (2026-05-05). No sale or later round found through 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "Series E >$140M led by Liberty Strategic Capital and ISTARI (coverage dated 2023-11-30)"
market_position: {ai-soc-analysts: niche-specialist, vendor-risk: niche-specialist}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: "true"
integrations: [Microsoft Sentinel, Microsoft Defender, Microsoft 365, Microsoft Entra, Microsoft Purview, Microsoft Security Copilot]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market and enterprise organisations on the Microsoft security stack; firms wanting third-party cyber-risk monitoring run as a service
last_verified: 2026-10-24
verify_after: null
tags: [mdr, managed-soc, microsoft-security, agentic-soc, tprm, supply-chain-risk, survey-write-in, security-operations]
sources:
  - {claim: "John Hernandez replaces co-founder Jim Rosenthal as CEO (Rosenthal to board chair); founded 2017; MDR, third-party risk management, digital risk protection; 1,000+ clients; 'AI-led cybersecurity platform'", url: "https://itbrief.co.uk/story/bluevoyant-names-john-hernandez-as-chief-executive-officer", date: 2026-10-24, confidence: medium}
  - {claim: "BlueVoyant AI agentic SecOps platform launched (2026-06): alert enrichment/triage, response actions with humans in the loop; managed or self-service; built around Microsoft; 2,500+ Microsoft-environment deployments", url: "https://securitybrief.co.uk/story/bluevoyant-launches-ai-platform-for-security-operations", date: 2026-10-24, confidence: medium}
  - {claim: "Supply Chain Defense: fully managed third-party cyber-risk monitoring; Risk Operations Center validates findings and works remediation with the third parties", url: "https://bluevoyant.com/platform/3rd-party-cyber-risk-management", date: 2026-10-23, confidence: medium}
  - {claim: "Series E >$140M led by Liberty Strategic Capital and ISTARI alongside Conquest Cyber acquisition; Series D $250M led by Liberty Strategic Capital", url: "https://www.bluevoyant.com/press-releases/bluevoyant-acquires-conquest-cyber", date: 2026-10-24, confidence: medium}
---

# BlueVoyant

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md). Also listed in [vendor-risk](../categories/vendor-risk.md).

**One-liner** — A managed-security firm founded in 2017 with two businesses. One is an MDR / managed-SOC service built mainly on the Microsoft security stack, now driven by its "BlueVoyant AI" agent platform. The other is a fully managed third-party cyber-risk service in which its analysts chase your vendors to fix exposures.

**What it does** —
- *MDR / managed SOC.* 24/7 detection and response, run mainly on the customer's **Microsoft Sentinel and Defender**. The site cites 500+ Sentinel deployments, and 2,500+ customer deployments in Microsoft environments overall. It also offers Microsoft "manage and monitor" services and Microsoft 365 E7 / Purview / Security Copilot readiness bundles (2026-07). It does not appear to sell its own SIEM. It runs yours (usually Sentinel), so it is **not** cross-listed in [siem-soc](../categories/siem-soc.md).
- *Third-party risk ("Supply Chain Defense").* Described as "a fully managed solution that identifies, validates, and resolves critical cybersecurity issues in your third-party ecosystem". It monitors suppliers' internet-facing exposure from the outside. BlueVoyant's **Risk Operations Center** checks the findings and **works the remediation directly with the third parties**. A questionnaire module and a Business Risk Monitoring add-on (2024-02, non-cyber risk categories) round it out. This is why it is cross-listed in [vendor-risk](../categories/vendor-risk.md). The 2023 acquisition of Conquest Cyber (a risk-management SaaS for US defense / government) added cyber-programme risk tooling.
- *Digital risk protection* (brand/domain/dark-web monitoring) is also listed.

**What AI it claims (vendor marketing).** **BlueVoyant AI**, launched 2026-06 as an "Agentic SecOps Platform". Every alert is automatically enriched, analysed and triaged. Agents can take response actions (isolate a device, revoke credentials, remove a malicious email) "with humans in the loop". BlueVoyant says its models are trained on its operational work in Microsoft 365, Defender and Entra environments. It comes either as the AI behind the managed SOC or as **self-service SaaS** for an internal team. CEO quote: "We're not augmenting the SOC. We are helping it evolve." Site performance claims (e.g. lower Sentinel cost, more true positives than native Defender) are **vendor-stated and unverified**. Which underlying models it uses is not disclosed. No AI claims specific to the TPRM service were found.

**Naming / provenance** — Founded 2017; Jim Rosenthal is a co-founder (other founders not checked). Its board has included Tom Glocer (ex-Thomson Reuters CEO) and, since the 2021 round, Steven Mnuchin. Acquisitions: Marclay Associates (UK incident response) and **Conquest Cyber** (Nashville; bought from United Data Technologies, terms undisclosed; coverage dated 2023-11-30). HQ **unverified**: trade press calls it New York-based, but this was not confirmed on a primary page.

**Ownership & viability** — `independent`, private and venture/growth-backed. **Series D $250M (2021)** at a valuation above $1B, led by **Liberty Strategic Capital**. **Series E >$140M**, led by Liberty Strategic Capital and **ISTARI** (Temasek-founded), raised alongside the Conquest acquisition (coverage dated 2023-11-30). Earlier backers per PitchBook (secondary) include Temasek, Winton Ventures, 8VC and DNS Capital. On **2026-05-05** **John Hernandez** (ex-Quest Software, where he ran the Microsoft Platform Management business; Salesforce, IBM, Cisco) replaced co-founder Rosenthal as CEO, and Rosenthal became chair. Press describes a pivot "from traditional service delivery to a more scalable, technology-first model". BlueVoyant was a services-heavy business that has raised large sums, so expect pressure to raise again, be sold, or improve margins through the AI platform. Possible buyers would be a security platform vendor or PE.

**Positioning & differentiators** —
- **Microsoft-specialist MDR.** If you are an E5 / Sentinel shop, BlueVoyant runs your Microsoft tools rather than adding its own agent or SIEM. Compare [esentire](esentire.md) (vendor-agnostic Atlas) and [crowdstrike](crowdstrike.md) Falcon Complete (its own stack). Its natural competitor set is Microsoft-focused MSSPs and Microsoft's own Defender Experts.
- **Managed or self-run AI SOC.** The 2026 self-service option puts it up against AI-SOC software ([dropzone-ai](dropzone-ai.md), [7ai](7ai.md), [radiant-security](radiant-security.md)) as well as MDRs. Unproven at launch.
- **TPRM as a managed service, not a score.** [bitsight](bitsight.md) and [securityscorecard](securityscorecard.md) sell ratings your team acts on. [panorays](panorays.md) sells a platform. BlueVoyant's analysts validate the findings and contact the vendor for you. Compare [drawbridge](drawbridge.md), which also does TPRM as a service but only for alternative-investment managers.
- **One vendor for SOC + supply chain.** Few MDRs also run third-party risk. That suits a firm that wants to outsource both, but it concentrates two risk functions on one supplier.

**Who should choose them / anti-fit** — Fits a **fund standardised on Microsoft 365 E5 / Sentinel with a thin security team** that wants 24/7 managed response on those tools. Also a firm that wants vendor exposures chased down for it rather than just scored. **Anti-fit:** a non-Microsoft SIEM/EDR estate (Splunk, Google SecOps, CrowdStrike-centric; non-Microsoft support not confirmed). Also a firm whose TPRM programme is questionnaire- and contract-driven due diligence; that is GRC/TPRM-platform territory ([vendor-risk](../categories/vendor-risk.md) peers).

**Known weaknesses / gotchas** — Survey write-in (2026-10): written into **Q55 Third-Party Risk (TPRM)** by **1 respondent, in production**. So the survey evidence is for the **Supply Chain Defense / TPRM service**, not the MDR. CEO change in 2026-05 and a strategy pivot to SaaS mean roadmap and packaging are in flux. bluevoyant.com blocked fetches (403), so several product details come from trade press and search snippets. AI performance claims are unverified. Non-Microsoft coverage is unclear.

**Deployment & data handling** — SaaS / managed service. For MDR it works inside the customer's Microsoft tenant (Sentinel/Defender) via delegated access. Whether alert data and investigation context also leave the tenancy for BlueVoyant AI processing is **unverified**, though `data_leaves_tenancy: true` is assumed for the AI platform and the SOC. Supply Chain Defense uses outside-in data about your vendors, and you share your vendor list with BlueVoyant. Retention, residency and training-use terms unverified.

**Integrations & partnerships** — Microsoft Sentinel partner ecosystem (2025-09-30), Defender, M365, Entra, Purview, Security Copilot / Agent 365. Sold via account specialists and selected VARs. UK G-Cloud listing for the TPRM service. MCP support unverified.

**Compliance & FS traction** — Certifications not checked. No named FS customers found. The one survey respondent (hedge-fund / PE-heavy sample) uses the TPRM service in production.

**Commercial** — Not public.

## Open questions

- HQ (New York?) and current funding total; any 2024-26 round or sale.
- Full founding team and founder backgrounds (not checked).
- Which models power BlueVoyant AI; whether customer data trains them; data residency.
- Non-Microsoft SIEM/EDR support for MDR and BlueVoyant AI.
- SOC 2 / ISO 27001 status.
- TPRM pricing basis (per monitored vendor?) and how many vendors the Risk Operations Center actively works per tier.

## Sources

- [IT Brief UK: BlueVoyant names John Hernandez CEO (2026-05-05)](https://itbrief.co.uk/story/bluevoyant-names-john-hernandez-as-chief-executive-officer) — fetched 2026-10-24 — supports: CEO change, founding 2017, business lines, client count; confidence: medium
- [SecurityBrief UK: BlueVoyant launches AI platform for security operations (2026-06-10)](https://securitybrief.co.uk/story/bluevoyant-launches-ai-platform-for-security-operations) — fetched 2026-10-24 — supports: BlueVoyant AI capabilities, managed vs self-service, Microsoft focus; confidence: medium
- [BlueVoyant: 3rd-party cyber risk management](https://bluevoyant.com/platform/3rd-party-cyber-risk-management) — search snippet 2026-10-23 (fetch 403) — supports: Supply Chain Defense description; confidence: medium (marketing)
- [BlueVoyant acquires Conquest Cyber](https://www.bluevoyant.com/press-releases/bluevoyant-acquires-conquest-cyber) — search snippet 2026-10-24 (fetch 403) — supports: Series E, Conquest acquisition; confidence: medium
- [SecurityWeek: BlueVoyant raises $250 million](https://www.securityweek.com/bluevoyant-raises-250-million-boost-technical-capabilities-global-expansion/) — search snippet 2026-10-24 — supports: Series D; confidence: medium
- [BlueVoyant: Microsoft Sentinel partner ecosystem participant](https://www.bluevoyant.com/press-releases/microsoft-sentinel-partner-ecosystem-participant) — search snippet 2026-10-24 — supports: Sentinel partnership; confidence: medium
- Cached: `raw/sources/2026-10-24--bluevoyant--ceo-ai-platform-funding.md`; TPRM detail in `raw/sources/2026-10-23--vendor-risk--write-in-one-liners.md`

## History

- [2026-10-24] Page created and researched. Added because of an Oct-2026 CTO survey write-in under Q55 Third-Party Risk (1 respondent, in production). Primary ai-soc-analysts per the 2026-10 MDR-placement decision; vendor-risk cross-list for Supply Chain Defense. No siem-soc cross-list (it operates customers' Sentinel rather than its own SIEM).
