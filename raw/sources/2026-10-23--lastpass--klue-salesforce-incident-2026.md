# Klue OAuth / Salesforce incident (June 2026) — LastPass and BeyondTrust affected

- URL: https://www.finra.org/rules-guidance/guidance/cybersecurity-alert-klue-oauth-breach-and-salesforce-data-exfiltration (FINRA cybersecurity alert, primary regulator)
- URL: https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/ (2026-06-23)
- URL: https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/ (2026-06-24)
- URL: https://www.beyondtrust.com/trust-center/security-advisories/klue-security-incident (BeyondTrust advisory; site blocks fetch — content via search snippet)
- Fetched: 2026-10-23
- Good for: a second, unrelated 2026 LastPass incident (CRM data, not vaults), and the same incident at BeyondTrust; FINRA flagged it to member firms.

## FINRA alert
- Klue detected breach 2026-06-12. Threat actor "Icarus" used a compromised service-account credential to reach Klue's backend, stole customer OAuth tokens, bulk-exported CRM data from connected platforms incl. Salesforce. Data: business contact info, support case data, BI reports. Extortion campaign with Tor leak site. Salesforce and Gong disabled the Klue Battlecards integration.
- Named affected (non-exhaustive): LastPass, 8x8, Pendo, HackerOne, Huntress, Insurity, Jamf, OneTrust, Recorded Future, Snyk, Sprout Social, Tanium, BeyondTrust, NoPass (formerly LogMeIn), GMS.
- Recommendations: check whether firm or critical vendors use Klue; review Salesforce logs; revoke/rotate Klue OAuth tokens; watch for extortion emails; review third-party integration controls.

## LastPass (BleepingComputer / SecurityWeek)
- Learned 2026-06-12. Exposed: customer names, phone numbers, email and physical addresses, support case data, sales/CRM data. "LastPass products, services, and infrastructure were not impacted in any way, and customer vaults remain secure." Disabled Klue, rotated tokens, notified law enforcement.

## BeyondTrust (SecurityWeek / advisory snippet)
- "business contact and sales-related information was stolen" from its Salesforce instance. Advisory: learned 2026-06-12; no employee accounts compromised; no infrastructure, network, products or product cloud environments accessed. SecurityWeek notes BeyondTrust disclosed later than other affected firms.
