---
title: Check Point Software
type: vendor
name: Check Point Software
slug: check-point
aka: [Check Point, CHKP, Check Point Software Technologies, Quantum, Harmony, Harmony SASE, Harmony DLP, CloudGuard, Infinity Platform, AI Defense Plane, AI Network Firewall, GenAI Protect]
primary_category: network-security-sase
also_listed_in: [dlp, ai-runtime-security]
website: https://www.checkpoint.com/
founded: null
hq: Tel Aviv, Israel
ownership_state: public
owner: null
ownership_note: NASDAQ:CHKP. FY2025 revenue $2,725M (+6%); Q2 2026 revenue $674M (+1%), security subscriptions $333M (+12%). CEO Nadav Zafrir. AI-security M&A — Lakera closed 2025-10-22 (~$201.8M total consideration per 20-F; ~$190M net cash per results release), Cyata + Cyclops closed Q1 2026 (~$92M net cash combined), Rotate talent acquisition (Q1 2026), Deepchecks team/IP agreement ~2026-05 (secondary sources only).
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {network-security-sase: legacy-incumbent, dlp: platform-module, ai-runtime-security: platform-module}
deployment_model: [on-prem, saas, hybrid]
form_factor: [inline-proxy, agent, api, browser-extension, platform]
data_leaves_tenancy: partial
integrations: []
mcp_support: gateway
certifications: []
pricing_model: appliance + subscription; Infinity platform enterprise agreements
fs_traction: unverified
target_customer: enterprise and upper mid-market; long-standing firewall installed base
last_verified: 2026-10-23
verify_after: null
tags: [firewall, ngfw, sase, dlp, ai-security, public, incumbent, israel, lakera]
sources:
  - {claim: "FY2025 revenue $2,725M; completed Lakera for ~$190M net cash in Q4 2025; announced Cyata, Cyclops, Rotate; 2026 strategy centred on AI transformation (release 2026-02-12)", url: "https://www.checkpoint.com/press-releases/check-point-software-reports-fourth-quarter-and-2025-full-year-results/", date: 2026-10-23, confidence: high}
  - {claim: "Completed Cyata and Cyclops for ~$92M net cash in Q1 2026 (release 2026-04-30)", url: "https://seekingalpha.com/pr/20494062", date: 2026-10-23, confidence: high}
  - {claim: "Q2 2026 revenue $674M (+1%), subscriptions $333M (+12%); AI Network Firewall and AI Defense Plane cited by CEO (release 2026-07-30)", url: "https://www.checkpoint.com/press-releases/check-point-software-reports-2026-second-quarter-financial-results/", date: 2026-10-23, confidence: high}
  - {claim: "AI Network Firewall in R82.20 (2026-07-30): shadow-AI discovery, MCP discovery, prompt-injection blocking, prompt-intent data-exfiltration controls; part of AI Defense Plane", url: "https://www.checkpoint.com/press-releases/check-point-revolutionizes-the-firewall-market-new-ai-network-firewall-closes-the-networks-ai-blind-spot-everywhere/", date: 2026-10-23, confidence: high}
  - {claim: "Harmony endpoint and browser DLP prevents sensitive data exposure across endpoints, browsers, web apps and GenAI tools", url: "https://www.checkpoint.com/resources/items/check-point-data-loss-prevention-dlp", date: 2026-10-23, confidence: medium}
  - {claim: "Lakera acquisition closed 2025-10-22 for total consideration ~$201.8M (20-F FY2025 Note 3)", url: "https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm", date: 2026-07-27, confidence: high}
---

# Check Point Software

> Primary category: [network-security-sase](../categories/network-security-sase.md). Also listed in [dlp](../categories/dlp.md) and [ai-runtime-security](../categories/ai-runtime-security.md). **Parent of [lakera](lakera.md)** (closed 2025-10-22).

**One-liner** — The Israeli firewall incumbent (Quantum gateways, Harmony SASE/workspace, CloudGuard). In 2025–26 it spent heavily to become an AI-security platform: it bought Lakera, Cyata and others, and it now ships prompt-injection blocking and shadow-AI and MCP discovery in its firewall software.

**What it does** — Three product families on one management layer (the **Infinity Platform**):
- **Quantum.** Network firewalls (physical and virtual NGFW). This is the installed base and still a large share of revenue, though appliance demand was soft in Q2 2026.
- **Harmony.** Workspace security: endpoint, email, browser, **Harmony SASE** (the cloud-delivered SSE/ZTNA), and **Harmony DLP** (endpoint plus browser DLP that covers "endpoints, browsers, web applications, and GenAI tools", with copy-paste blocking and AI-assisted classification).
- **CloudGuard.** Cloud and WAF.

The **AI Defense Plane** sits across all three. It is "a unified control plane for discovering, governing, and protecting AI". Its first flagship is the **AI Network Firewall**, shipped 2026-07-30 in firewall release **R82.20**. It discovers shadow and sanctioned AI apps and agents, **discovers MCP traffic and the servers and tools in use**, blocks prompt injection inline "before they reach the LLM", and can stop sensitive data leaving based on a prompt's intent. Other enforcement points are a standalone API (the [lakera](lakera.md) Guard lineage), an endpoint agent, a containerised firewall for AI data centres, and the WAF.

**Naming / provenance** — Company: Check Point Software Technologies Ltd. Product names change often (Quantum, Harmony, CloudGuard, Infinity, GenAI Protect, and now AI Defense Plane), so match quotes to the current SKU. Founding year is not verified this pass; the [lakera](lakera.md) page notes a "©1994" copyright line in Check Point's boilerplate.

**Ownership & viability** — `public`, NASDAQ: **CHKP**. FY2025 revenue was **$2,725M** (+6%). Q2 2026 revenue was **$674M**, up only 1%. Security subscriptions grew 12% while product (appliance) revenue fell. Management says email security, CTEM and AI security together grew ARR by more than 40% (call commentary, secondary). It is a profitable, slow-growing incumbent buying growth in AI security. **AI-security M&A ledger:**
- [lakera](lakera.md): announced 2025-09-16, **closed 2025-10-22**. The audited 20-F gives ~$201.8M total consideration and the results release says ~$190M net cash. These are different measures, not a contradiction.
- **Cyata** (AI-agent discovery and governance) and **Cyclops** (exposure management / CAASM): announced 2026-02-12, **completed in Q1 2026** for ~$92M net cash combined.
- **Rotate**: talent acquisition, Q1 2026.
- **Deepchecks** (LLM evaluation): definitive agreement for the team and IP, ~2026-05-19, est. ~$20M. **Secondary sources only.** Closing not confirmed by Check Point primary material.

**Positioning & differentiators** —
- **AI controls on the firewall you already run.** Against [zscaler](zscaler.md) and [netskope](netskope.md), which put AI controls in a cloud proxy, Check Point puts them in the on-prem or virtual firewall through a software upgrade (R82.20). If you already run Quantum gateways, you need no new infrastructure.
- **Owns a prompt-injection engine.** With [lakera](lakera.md) it owns a dedicated AI guardrail engine, as [palo-alto-networks](palo-alto-networks.md) (Prisma AIRS / Protect AI), [cisco](cisco.md) ([cisco-ai-defense](cisco-ai-defense.md)) and [zscaler](zscaler.md) (SPLX) do. This is the 2025 pattern of platforms buying their guardrails.
- **DLP is a module, not a standalone franchise.** Harmony DLP covers endpoint, browser and GenAI prompt paths. It does not have the depth of [forcepoint](forcepoint.md), [microsoft-purview](microsoft-purview.md) or Digital Guardian in classification and incident workflow. It makes sense when you are consolidating on Harmony.
- **MCP visibility at the network layer.** Network-level MCP discovery is uncommon among firewall vendors as of mid-2026 (vendor-stated). It gives visibility, not authorization. Compare dedicated [mcp-gateway](../categories/mcp-gateway.md) products.

**Who should choose them / anti-fit** — Fits a firm **already standardised on Check Point firewalls or Harmony** that wants AI-usage visibility, prompt-level data controls and prompt-injection defence without adding a new inline vendor. It is the natural choice for a Check Point estate. **Anti-fit:** a cloud-first firm with no on-prem perimeter. A cloud SSE ([zscaler](zscaler.md), [netskope](netskope.md)) matches that architecture better. Also a firm that needs a best-of-breed DLP program (classification, case management, insider-risk workflows) rather than DLP as a feature, and one that wants a model-neutral guardrail vendor with no network-security incumbent attached.

**Known weaknesses / gotchas** — Revenue growth is low and appliance revenue is shrinking, so the AI push is partly defensive. Many recent acquisitions are being integrated at once (Lakera, Cyata, Cyclops, Deepchecks). Expect product renames and roadmap churn. The Lakera trademark has a 1-year useful life in the 20-F (see [lakera](lakera.md)). As with every edge-appliance vendor, firewall CVEs are patch-critical. Specific KEV entries not verified here. DLP was written in by only 1 survey respondent (in production), so evidence that it is used as a primary DLP at hedge funds is thin.

**Deployment & data handling** — Firewalls are on-prem or virtual. Harmony SASE and the Infinity Portal are SaaS. DLP runs on endpoint and browser. Enforcement (firewall, endpoint) is local, while management, threat intelligence and some classification are cloud-based, hence `data_leaves_tenancy: partial`. Whether AI Network Firewall prompt inspection runs entirely on the gateway or calls a Check Point cloud model is **unverified** and is the key question for MNPI-sensitive traffic. TLS inspection is required for any prompt-content control.

**Integrations & partnerships** — Infinity Platform across network, cloud and workspace. Standalone AI guardrail API (Lakera). `mcp_support: gateway` refers to MCP *discovery and visibility* at the firewall (vendor-stated, 2026-07-30), not a full MCP gateway with per-tool authorization. SIEM export and IdP integrations exist but are not itemised here.

**Compliance & FS traction** — **Unverified** for named hedge-fund or asset-manager customers. Check Point firewalls are common in financial services generally. Not evidenced here.

**Commercial** — Appliances plus subscriptions, increasingly sold as Infinity enterprise agreements. AI Network Firewall is "available now" (packaging and price not public).

## Open questions

- Does AI Network Firewall / AI Defense Plane prompt inspection run locally on the gateway or in Check Point's cloud? What retention applies?
- Closing status and price of Deepchecks (primary source).
- How Lakera Guard, GenAI Protect and AI Defense Plane SKUs map to each other after integration.
- Harmony DLP depth vs dedicated DLP (EDM/fingerprinting, OCR, case management): not evaluated.
- Founding year and certifications (SOC 2 / ISO 27001 / FedRAMP for SaaS products), not checked this pass.

## Sources

- [Check Point Q4 and FY2025 results (2026-02-12)](https://www.checkpoint.com/press-releases/check-point-software-reports-fourth-quarter-and-2025-full-year-results/) — fetched 2026-10-23 — supports: FY2025 revenue, Lakera net cash, Cyata/Cyclops/Rotate announcements, AI strategy; confidence: high
- [Check Point Q1 2026 results (2026-04-30)](https://seekingalpha.com/pr/20494062) — fetched 2026-10-23 — supports: Cyata + Cyclops completed, ~$92M net cash; confidence: high (issuer press release, syndicated)
- [Check Point Q2 2026 results (2026-07-30)](https://www.checkpoint.com/press-releases/check-point-software-reports-2026-second-quarter-financial-results/) — fetched 2026-10-23 — supports: Q2 revenue/subscriptions, AI Network Firewall + AI Defense Plane; confidence: high
- [Check Point AI Network Firewall press release (2026-07-30)](https://www.checkpoint.com/press-releases/check-point-revolutionizes-the-firewall-market-new-ai-network-firewall-closes-the-networks-ai-blind-spot-everywhere/) — fetched 2026-10-23 — supports: R82.20, shadow-AI/MCP discovery, prompt-injection blocking, AI Defense Plane enforcement points; confidence: high (vendor primary; capability claims are vendor-stated)
- [Check Point Endpoint and Browser DLP solution brief](https://www.checkpoint.com/resources/items/check-point-data-loss-prevention-dlp) — fetched 2026-10-23 — supports: Harmony DLP scope incl. GenAI tools; confidence: medium (marketing)
- [Check Point Form 20-F FY2025, Note 3(f)](https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm) — fetched 2026-07-27 (via lakera research) — supports: Lakera close 2025-10-22, ~$201.8M total consideration; confidence: high
- [Check Point acquires Deepchecks (Security Boulevard, 2026-05)](https://securityboulevard.com/2026/05/check-point-acquires-deepchecks-as-it-builds-out-agentic-security-platform/) — via search 2026-10-23 — supports: Deepchecks team/IP agreement; confidence: low-medium (secondary)
- Cached: `raw/sources/2026-10-23--check-point--results-acquisitions-ai-firewall.md`, `raw/sources/2026-07-27--lakera--checkpoint-20f-close-date-and-price.md`

## History

- [2026-10-23] Page created and researched. Added because of an Oct-2026 CTO survey write-in under DLP (1 in production). Primary network-security-sase (firewall/SASE core). Cross-listed dlp (Harmony DLP incl. GenAI prompts) and ai-runtime-security (Lakera ownership + AI Defense Plane / AI Network Firewall prompt-injection blocking, GA 2026-07-30). Linked to existing lakera page.
