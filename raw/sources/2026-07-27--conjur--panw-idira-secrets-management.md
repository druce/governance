# Conjur → Palo Alto Networks "Idira" Secrets Manager

- **URLs:**
  - https://www.conjur.org (301 redirect target verified by curl)
  - https://www.paloaltonetworks.com/idira/machine/secrets-management
  - https://www.paloaltonetworks.com/idira
  - https://github.com/cyberark/conjur
  - https://www.sdxcentral.com/news/palo-alto-networks-rebrands-cyberark-with-idira-platform-release/
- **Fetched:** 2026-07-27
- **Good for:** confirming the Conjur brand URL now resolves to Palo Alto Networks' Idira
  platform, that Idira is the PANW rebrand of the acquired CyberArk portfolio, and where
  Conjur's secrets-management capability now lives in the PANW product line.

## Redirect (verified 2026-07-27, curl)

```
$ curl -sSI https://www.conjur.org
301 -> https://www.paloaltonetworks.com/idira/machine/secrets-management
final: https://www.paloaltonetworks.com/idira/machine/secrets-management (200)
```

The `conjur.org` domain — the long-standing home of Conjur Open Source — no longer serves
any Conjur- or CyberArk-branded content. It 301s to a Palo Alto Networks page with zero
Conjur or CyberArk branding.

## Destination page: paloaltonetworks.com/idira/machine/secrets-management

Product is named **"Secrets Manager"**, sold under the **Idira** platform's *Machine
Identity* pillar. Offered as SaaS or self-hosted. Quoted from the page:

> "Secrets Manager gives security teams centralized control over secrets across cloud,
> on-premises and hybrid environments."

Capabilities listed: centralized storage/retrieval of API keys, tokens, passwords and
certificates; automated rotation and credential lifecycle; universal cryptographic
workload identity (SPIFFE); audit trails and compliance reporting; native integrations
with applications, containers and CI/CD pipelines. No mention of "Conjur" or "CyberArk"
anywhere on the page.

## What Idira is (paloaltonetworks.com/idira)

Palo Alto Networks' umbrella brand for the identity-security portfolio it acquired with
CyberArk. FAQ on the page states directly:

> "CyberArk has long been your trusted partner for securing privilege and defending your
> critical assets. Now, we're introducing Idira, the next-generation identity security
> platform, built on CyberArk's legacy and powered by Palo Alto Networks."

Modules named on the page:

- **Human Identity** — Privileged Access Management, Identity and Access Management,
  Endpoint Privilege Manager, Identity Governance, Workforce Password Management, Vendor
  Privileged Access
- **Machine Identity** — Secrets Management, Unified Secrets Governance, Application
  Credentials Delivery, Certificate Manager
- **Agentic Identity** — Agentic Identities (Secure AI Agents)

Conjur's capability maps to the **Machine Identity → Secrets Management** slot.

## Rebrand timing

The Idira brand was launched in **May 2026** (PANW's own page references a May 2026 launch
blog; SDxCentral dates its rebrand story 2026-05-13). This is downstream of the Palo Alto
Networks acquisition of CyberArk, which **closed 2026-02-11** (announced 2025-07-30,
~$25B) — see `2026-06-28--cyberark--panw-acquire-press-release.md`. Reporting notes the
underlying technical platform and component names are unchanged; only the commercial
branding moved.

*Note:* sources differ by a day on the announcement (2026-05-12 vs 2026-05-13); recorded
here as "May 2026" rather than picking one. Not load-bearing for this page.

## Conjur open source (github.com/cyberark/conjur)

Repo is still public and not archived as of 2026-07-27. README carries a "Migrating to
CyberArk Secrets Manager, Self-Hosted" section pointing users at the commercial product.
No Idira or Palo Alto Networks branding in the repo yet — the OSS project still sits under
the `cyberark` GitHub org. Confidence: medium on future investment; the repo is live but
the marketing domain is gone.

## Commercial naming lineage

Prior to the PANW rebrand, CyberArk had already renamed the commercial editions:
Conjur Cloud → **Secrets Manager, SaaS**; Conjur Enterprise → **Secrets Manager,
Self-Hosted**. Idira keeps the "Secrets Manager" name. So "Conjur" now survives only as
the open-source project name and in API/SDK repo names (e.g. `conjur-api-go`, documented
as the "Go client for the CyberArk Secrets Manager API").
