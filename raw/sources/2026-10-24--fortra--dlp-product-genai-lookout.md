# Fortra DLP (ex-Digital Guardian) — product scope, GenAI controls, Lookout Cloud Security acquisition, GoAnywhere CVE

- URLs:
  - https://dope.security/post/digital-guardian-dlp-2026 (fetched; COMPETITOR BLOG citing Fortra docs)
  - https://www.fortra.com/platform/data-loss-prevention/ai (via search; VENDOR MARKETING)
  - https://www.fortra.com/resources/press-releases/fortra-achieves-key-customer-milestone-expanded-offerings-its-digital (2023-10, via search)
  - https://www.gartner.com/reviews/product/fortra-dlp (via search)
  - https://www.fortra.com/resources/articles/undercode-news-toshiba-digital-engineering-releases-ai-data-loss-prevention (2026-04, via search)
  - https://www.businesswire.com/news/home/20250508462614/en/Lookout-Announces-Sale-of-Its-Cloud-Security-Business-to-Fortra (via search)
  - https://www.fortra.com/resources/press-releases/fortra-breaks-cloud-attack-chain-acquisition-lookout-cloud-security (via search)
  - https://www.helpnetsecurity.com/2025/09/26/fortra-goanywhere-zero-day-cve-2025-10035/ (via search)
- Fetched: 2026-10-24
- Good for: what the DLP product covers today; GenAI claims (labelled marketing); adjacent Fortra assets; vendor-risk signal.

## Extract
- **Architecture (dope.security citing Fortra docs):** kernel-level endpoint agent enforcing "prior to allowing execution of an operation"; works offline, tamper resistance, optional Stealth Mode; Windows, macOS, Linux, Citrix VDI. Classification by context, content, user; tags persist; 300+ file types, 90 languages; database record matching (EDM-like). Fortra Data Classification Suite (Titus + Boldon James) via SDK.
- **Deployment:** cloud-delivered on AWS since 2017 (vendor claim); SaaS, on-prem, or **Managed Security Program** (managed DLP; "production in 90 days or less" claim). Analytics & Reporting Cloud (ARC). Network DLP appliance (SPAN/TAP, inline MTA). Cloud Data Protection via APIs (Office 365, Box). Gartner Peer Insights: SaaS or managed service; subscription priced per endpoint or user.
- **Scale:** ~600 customers, 5.5M+ users (Fortra, 2023-10). 2023 release also: policies to monitor/restrict ChatGPT.
- **GenAI (VENDOR MARKETING):** "Generative AI Content Pack" — prebuilt policies to block classified data leaving via copy/paste, file upload, form submission to AI sites, with reporting on PII/PCI event volumes; modes from full block to content block to monitor-only. Toshiba Digital Engineering (Japan distributor) selling Fortra DLP for GenAI prompt leakage (2026-04).
- **Competitor-stated gaps (dope.security, unverified):** no documented tenant-vs-personal-account control on the same AI domain; no documented prompt inspection inside desktop AI apps; Mac web inspection needed explicit proxy until v9.0 transparent proxy (2025-03), browsers + legacy Outlook only; Mac/Linux feature lag vs Windows; policy authoring needs skill; agent CPU/memory complaints (PeerSpot sample). Gartner MQ Leader x5 through the 2017 edition (Gartner retired that MQ).
- **Lookout Cloud Security:** Lookout announced sale of its Cloud Security business (CASB, ZTNA, SWG) to Fortra on **2025-05-12** (business wire dated 2025-05-08 in URL); Fortra acquired assets, IP and personnel (~54 staff per Twin Cities Business); Fortra says this gives it a DSPM offering. Terms undisclosed. fortra.com/lookout: "Lookout SSE is now Fortra". Prior Fortra–Lookout DLP integration partnership (2024-03).
- **GoAnywhere MFT CVE-2025-10035** (CVSS 10, deserialization in License Servlet): Fortra advisory 2025-09-18; exploitation from ~2025-09-10 (watchTowr); Microsoft tied it to Storm-1175 / Medusa ransomware; CISA KEV 2025-09-29. Not the DLP product, but a vendor-level security signal (earlier GoAnywhere CVE-2023-0669 was mass-exploited by Clop).
