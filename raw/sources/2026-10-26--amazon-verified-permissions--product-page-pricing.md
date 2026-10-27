# Amazon Verified Permissions — product page + pricing page

- URLs: https://aws.amazon.com/verified-permissions/ ; https://aws.amazon.com/verified-permissions/pricing/
- Fetched: 2026-10-26
- Good for: AWS's own description of AVP, named customers (incl. FIS), and per-request pricing. Vendor marketing for the customer claims.

## Product page
- Tagline: "Fully managed Cedar service for fine grained authorization." "Amazon Verified Permissions is a fully managed authorization service that uses the Cedar policy language."
- Benefits: decouple authorization from application logic; policy-based least privilege; Cedar schema validation to simplify audits; real-time continual authorization decisions; Express framework support; policy templates enforceable in Amazon API Gateway and AWS AppSync.
- No agent / AI / MCP / RAG messaging on the product page itself (2026-10-26).
- Named customers: **FIS** (Prophet team; RBAC+ABAC; "AVP provides a clear audit trail by logging every action—who made it, when it was made"; linked to SOX compliance), Grosvenor Engineering Group ("consumption-based pricing model of AVP" keeps switching costs low), Stedi (up to 700M requests/month via API Gateway), Twilio (Flex data permissions), TELUS (smart-home permissions).
- No certifications listed on the page.

## Pricing page
- Usage-based, per API request; "There are no upfront or minimum fees."
- Single authorization (IsAuthorized, IsAuthorizedWithToken): $0.000005 per request, same in all Regions.
- Batch authorization (BatchIsAuthorized*): $0.00015 first 40M/month; $0.000075 next 60M; $0.00004 above 100M.
- Policy management (CreatePolicy, UpdatePolicy, GetPolicy, ListPolicy): $0.00004 per request.
- No free tier listed.
