# turbopuffer — product, security/compliance, pricing, customers

- URL: https://turbopuffer.com/
- URL: https://turbopuffer.com/docs/security
- URL: https://turbopuffer.com/pricing
- URL: https://turbopuffer.com/customers
- Fetched: 2026-10-16
- Good for: what turbopuffer is, architecture, deployment tiers (multi-tenant /
  single-tenant / BYOC), certifications, plan minimums, logo list. All vendor-published.

## Product (homepage, vendor marketing)
- "Fast search engine built on object storage": vector search, full-text (BM25),
  hybrid search, metadata filtering. Queries served via memory/SSD cache in front of
  object storage (S3/GCS).
- Scale claims (vendor): 1T+ documents globally (3PB+), 10M+ writes/s, 100k+ queries/s,
  up to 128B docs per namespace, 250M+ namespaces seen. "10x cheaper" than alternatives
  (no unit prices on homepage).
- Example latency in calculator: ~14ms p50 vector query on a warm 10M-doc namespace;
  homepage feature list says "sub-10ms p50". Cold (uncached) namespaces are slower.
- Customer logos on homepage: Anthropic, Cognition, Notion, Atlassian, Ramp,
  **Bridgewater Associates**, fal, Legora, Linear, Granola, Superhuman, Harvey,
  The New York Times, Pylon, TELUS, Clay.

## Customer stories page
- 12 stories: Notion, Legora (BYOC), Linear, Atlassian (BYOC), Superhuman, fal, Mem0,
  Kepler ("searches every financial document"), Pylon, Readwise, PlayerZero, TELUS.
- **No Bridgewater case study.**

## Security & compliance (docs/security)
- SOC 2 Type 2 audits; report + pen test via Trust Center.
- HIPAA BAA on request (Scale+ per pricing); DPA (GDPR/CCPA) for all customers.
- Encryption: TLS 1.2+ in transit; AES-256 at rest; CMEK (Enterprise), defined per namespace.
- Multi-tenant regions; single-tenant clusters; data hosted only in selected region.
- Private networking (Enterprise): AWS PrivateLink, GCP Private Service Connect.
- SSO for dashboard (Scale, Enterprise); IP allowlisting (Scale, Enterprise).
- Staff access to customer data only with written customer consent, logged; paid add-on
  for multi-party approval / time-limited sessions.
- No RBAC within data plane mentioned.

## Pricing (pricing page)
- Usage-based with monthly minimums: Launch $16/mo; Scale $256/mo; Enterprise $4,096/mo
  + 35% usage premium.
- Single-tenancy and BYOC: Enterprise only. Audit logs: Scale+. 99.95% uptime SLA: Enterprise.
