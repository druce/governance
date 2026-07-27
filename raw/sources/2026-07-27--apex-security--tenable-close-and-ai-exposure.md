# Apex Security → Tenable: acquisition close (SEC 10-Q) + rebrand to Tenable One AI Exposure

- URLs:
  - https://www.sec.gov/Archives/edgar/data/1660280/000166028025000090/tenb-20250630.htm (Tenable Holdings 10-Q for Q2 2025, filed ~2025-07; Note 6 "Acquisitions, Goodwill and Intangible Assets")
  - https://www.tenable.com/press-releases/tenable-extends-exposure-management-to-AI-attack-surface (GA press release)
  - https://www.tenable.com/products/ai-exposure (live product page)
  - https://www.tenable.com/blog/introducing-tenable-ai-exposure-stop-guessing-start-securing-your-ai-attack-surface (2025-08-06 preview launch blog)
  - https://www.tenable.com/press-releases/tenable-announces-intent-to-acquire-apex-security-to-expand-exposure-management-across-the-ai-attack-surface (2025-05-29 intent-to-acquire)
- Fetched: 2026-07-27
- Good for: **confirming the Apex acquisition actually CLOSED (June 2025) and the real purchase price ($47.8M per SEC filing, not the >$105M reported in press)**; the successor product name/URL after apexsec.com lapsed.

## Key extracted facts

### Close + price — SEC 10-Q (primary, authoritative)
Verbatim from Note 6 of Tenable Holdings, Inc. Form 10-Q for the quarter ended 2025-06-30:

> "In June 2025, we acquired Apex Security, Inc. ("Apex"), an innovator in securing the rapidly expanding AI attack surface. ... We acquired 100% of Apex's equity through a share purchase agreement for total consideration of $47.8 million, including $47.7 million in cash, net of $2.0 million cash acquired, and $0.1 million fair value of replacement equity."

Purchase price allocation (in thousands): accounts receivable $62; intangible assets $6,800 (Apex proprietary technology, 5-year useful life); goodwill $41,288; deferred revenue $(34); other liabilities, net $(333); **total purchase price $47,783**. Allocation described as preliminary.

Also: "In 2025, we acquired both Vulcan and Apex for a combined $196.2 million in cash." (Vulcan Cyber = $148.5M, Feb 2025.)

- **Close: June 2025** (month-level precision only; the 10-Q does not give a day, and Tenable filed no separate 8-K close announcement — the deal was immaterial for 8-K purposes).
- Announced (intent): 2025-05-29.

### Price contradiction (resolved in favor of SEC)
Calcalist (2025-05-29) and follow-on trade press reported the deal at **">$105 million"**. Tenable's own 10-Q reports **$47.8M total consideration**. The SEC filing is the authoritative figure for consideration transferred; the higher press number most likely folded in retention/employee incentive packages, which are compensation expense rather than purchase consideration under ASC 805. Treated as **soft contradiction — resolved**: use $47.8M as the acquisition price, note the press figure as reported-but-unconfirmed.

### Product successor + URL
- **apexsec.com is dead.** As of 2026-07-27 both `https://apexsec.com` and `https://www.apexsec.com` return HTTP 404 (server: Kestrel); an automated audit also observed a 302 to a HugeDomains "domain for sale" parking page ($15,595 listing). The Apex brand no longer has a web presence.
- Apex's technology was folded into Tenable One as **Tenable One AI Exposure** (sometimes styled "Tenable AI Exposure"). Live product page: **https://www.tenable.com/products/ai-exposure**.
- Timeline of the rebrand: **2025-08-06** — Tenable blog "Introducing Tenable AI Exposure" launches the capability in *private customer preview*, agentless, deployable "in minutes," built into Tenable One. **2026-01-27** — press release "Tenable Extends Exposure Management to AI Attack Surface" announces **general availability of Tenable One AI Exposure**.
- Capabilities per the product page and blog: discover AI platform usage (incl. shadow AI) across SaaS/cloud/APIs/agents; understand who is using AI, for what intent, and what data is exchanged; find unsafe AI platform settings, agent configurations, and third-party integrations; detect and stop AI-specific attacks (direct and indirect prompt injection, jailbreaks) and contain risky or compromised AI agents; enforce usage policy.
- Coverage at GA: **OpenAI ChatGPT Enterprise, Microsoft Copilot, Microsoft 365 Copilot, Microsoft Studio Copilot**, with deeper Google Gemini support signalled as forthcoming. Predecessor/adjacent Tenable capability: AI Aware (2024, in Tenable Vulnerability Management).
- Neither the product page nor the GA press release mentions Apex by name — the brand is fully absorbed.
