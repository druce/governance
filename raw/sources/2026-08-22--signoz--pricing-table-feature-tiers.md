# SigNoz — pricing page feature table, read row by row (correction source)

- URL: https://signoz.io/pricing/
- Fetched: 2026-08-22 (re-read carefully; an earlier summarized read got two rows wrong)
- Good for: which access-control and audit features actually ship, per tier.

## Prices

- **Teams — $49/month**, which includes usage worth $49 (reduced from $199
  promotional pricing).
- **Enterprise — "Custom", "starts at $4000/month".**
- Usage: logs $0.3/GB and traces $0.3/GB (15-day retention); metrics $0.1 per
  million samples (1-month retention).
- Enterprise delivery options: dedicated environment on SigNoz cloud, bring your
  own cloud, or self-host with a support contract.

## Feature table — the five rows that matter

| Feature | Community | Teams | Enterprise |
|---|---|---|---|
| SSO support | ✓ | ✓ | ✓ |
| SAML support | ✗ | ✓ | ✓ |
| Audit Logs | ✗ | ✗ | **COMING SOON** |
| Finer RBAC with custom roles | ✗ | ✗ | **COMING SOON** |
| Multi-tenancy | ✗ | ✗ | **COMING SOON** |

## The two corrections this forces

1. **SSO is on all three tiers, including free Community. SAML starts at Teams
   ($49/mo), not Enterprise.** So SSO/SAML is NOT "gated behind the $4,000/mo
   Enterprise minimum" — it is a $49/mo feature, and plain SSO is free.
2. **Audit Logs are marked COMING SOON on Enterprise — i.e. they do not ship
   today at any price.** Advising a buyer to "budget for Enterprise if you need
   audit trails" is therefore wrong: $4,000/mo does not currently buy audit logs.
   Finer RBAC with custom roles and multi-tenancy are in the same state.

## Caveat worth carrying

The presence of an `ee/auditor` package in the SigNoz repository is **not**
evidence the feature ships. Code in a repo is not a shipped, supported,
documented feature; the vendor's own pricing table marks it COMING SOON. Follow
the pricing table.
