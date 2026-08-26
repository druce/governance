# DNSFilter — funding, scale, and the protective-DNS scope boundary

- URL: https://www.dnsfilter.com/newsroom/dnsfilter-raises-another-15-million-in-series-a-extension-from-insight-partners
- URL: https://www.insightpartners.com/ideas/dnsfilter-raises-30m-in-funding-to-fight-growing-number-of-dns-based-security-threats/
- URL: https://www.businesswire.com/news/home/20260630616164/en/DNSFilter-Launches-New-MSP-Partner-Program-Turning-Security-Squeeze-Into-a-Growth-Opportunity-for-its-Partners
- Fetched: 2026-08-26
- Good for: DNSFilter's funding state and, more importantly, establishing that it
  is protective DNS rather than an SSE — a scope distinction the survey's
  category placement obscures.

## Funding
- **$30M Series A led by Insight Partners, July 2021.**
- **$15M Series A extension from Insight Partners, August 2023.**
- **~$62M total** venture funding, two rounds led by Insight.
- Founded 2015, Washington DC. 150+ employees.

## Scale
- Protects **27M+ end users monthly** across **~30,000 organisations**.
- Proprietary AI scans billions of domains daily for malware, ransomware,
  phishing, deception and fraud infrastructure.
- Heavy **MSP channel**; partner programme expanded again **2026-06-30**.

## Scope boundary — the reason this matters for the wiki
Protective DNS blocks or allows **at the domain level, before connection**. It:
- CAN block an unsanctioned AI service outright, estate-wide, very quickly.
- CANNOT distinguish the sanctioned enterprise tenant from the consumer one on the
  same domain, inspect prompt content, apply DLP, or see any payload.
- Is bypassable via DoH/DoT, VPN, or a hardcoded resolver unless separately blocked.
Listing it beside Zscaler/Netskope in a survey question risks respondents reporting
equivalent coverage where the control is much weaker. Noted on the wiki page.

## Confidence
- Funding: high (primary vendor release + Insight Partners).
- Scale figures: medium (vendor-supplied).
