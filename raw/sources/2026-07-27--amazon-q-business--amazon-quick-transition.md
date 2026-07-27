# Amazon Q Business closed to new customers; Amazon Quick is the successor

- URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html
  (AWS primary — "Amazon Q Business availability change" + full migration guide)
  - Also: https://aws.amazon.com/q/business/ (product page End of Support Notice)
  - Also: https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/
    (2025-10-09 — QuickSight → Quick Suite, the *other* half of the Quick lineage)
  - Also: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-whats-next-with-aws-2026-amazon-quick-openai-partnership-and-more-may-4-2026/
    (What's Next with AWS, 2026-04-28 — Amazon Quick feature launches)
- Fetched: 2026-07-27
- Good for: confirms Q Business closure to new customers, that Amazon Quick is a
  QuickSight-lineage consolidation rather than a Q Business rename, the BYOI
  migration path, and — most load-bearing for this wiki — the **entitlement /
  ACL regressions** in the successor.

## The closure

Verbatim from the docs banner:

> Amazon Q Business will no longer be open to new customers starting on July 31,
> 2026. If you would like to use the service, please sign up prior to July 30.
> For capabilities similar to Q Business, explore Amazon Quick.

Verbatim from the `aws.amazon.com/q/business/` product page notice:

> Amazon Q Business will no longer be open to new customers starting on July 30,
> 2026. If you would like to use the service, please sign up prior to July 30,
> 2026.

> Contradiction (soft): AWS's own copy gives **July 30** on the product page and
> **July 31** in the docs banner for the "no longer open to new customers" date.
> Both agree on the actionable instruction — sign up **prior to July 30, 2026**.
> Not worth escalating; recorded so the one-day discrepancy isn't mistaken for a
> transcription error later. Noted 2026-07-27.

Existing customers, verbatim:

> Amazon Q Business remains fully supported and AWS will continue to provide bug
> fixes and security updates for existing customers, however new feature requests
> will no longer be considered.

**No end-of-service / shutdown date has been announced for existing customers.**
Feature development has stopped; the service has not been given a death date.

## What Amazon Quick actually is — a consolidation, not a rename

Two separate product lines converge on the "Quick" brand:

1. **QuickSight → Quick Suite → Amazon Quick.** AWS announced on **2025-10-09**
   that Amazon QuickSight (the BI product, GA since 2016) "evolves to Amazon Quick
   Suite," bundling the existing BI engine with new generative features: Quick
   Sight (dashboards/analyses/datasets), Quick Research, Quick Flows, Quick
   Automate, Quick Index, Quick Chat. The core BI engine and SPICE were unchanged;
   the surface and licensing model changed. By the 2026-04-28 "What's Next with
   AWS" event the name is used as plain **"Amazon Quick"** (the "Suite" suffix has
   been dropped in AWS's own 2026 copy).
2. **Q Business folds into it.** The migration guide (above) directs Q Business
   customers onto Quick.

Evidence that Quick is the **QuickSight** service, not a renamed Q Business:

- Setup asks you to "choose the AWS Region that you want to use for your initial
  data storage capacity, **called SPICE**" — SPICE is QuickSight's engine.
- The migration script uses `boto3.client('quicksight')` and
  `quicksight.update_folder_permissions` with
  `arn:aws:quicksight:...:group/default/...` principals. The Quick control plane
  **is** the QuickSight API.
- Quick is found in the console "under **Analytics**."
- Q Business's own auth mode for the non-IDC path is literally named
  `AWS_QUICKSIGHT_IDP`.

AWS's framing sentence — "Amazon Quick represents the next evolution of Amazon Q
Business" — is marketing positioning aimed at the Q Business reader. The engineering
reality is that Q Business is being absorbed into the QuickSight service lineage.
**Conclusion: capability merge, not a rename.** Same call as Dev Box → Windows 365.

## Migration path

- **BYOI (Bring Your Own Index)** is the recommended first step: connect the
  existing Q Business index to Quick as a knowledge base. Non-destructive — Q
  Business keeps running in parallel.
- Both the Q Business index and the Quick instance must be in the **same AWS
  account and Region**.
- BYOI limits: **max 2 Q Business indexes per Region, quota not increasable**;
  once selected, indexes **cannot be unselected**; the resulting knowledge base
  cannot be modified like a native Quick one.
- Data sources can later be migrated to the native **Quick Index**.
- Connectors with no native Quick equivalent are meant to be bridged via **MCP**
  (Quick acts as MCP client). MCP caveats: 60-second fixed timeout (HTTP 424 on
  exceed), no custom HTTP headers, static tool lists, no step-up authorization,
  and **MCP integrations cannot back a knowledge base** — actions only.
- **Anonymous-access and API-integration** Q Business customers are told to
  contact AWS Support for a custom approach — i.e. no documented self-serve path.

## Governance regressions in the successor (the part that matters here)

These are AWS's own documented gaps, not analysis:

- **Guardrails do not transfer.** "Q Business guardrails (global controls and
  topic-level controls) and Actions are explicitly excluded from the BYOI
  capability." Content filtering rules and blocked topics must be rebuilt.
- **The User Store has no equivalent.** "In Quick, user management operates at the
  knowledge base level rather than through a centralized user store."
- **Non-IDC mode loses per-user entitlement.** "In a non-IDC implementation, all
  Amazon Quick users automatically receive access to connected Q Business
  indexes… you lose the per-user and per-group access distinctions that Q Business
  enforced at the index level." The documented workaround is to shard content into
  multiple knowledge bases by access role and set permissions per knowledge base
  in Quick Spaces — manual scripting, not automatic.
  - IDC (IAM Identity Center) mode preserves entitlement: access is granted only
    to users with access to the selected index. **The IdP choice is therefore a
    security decision, not a convenience one.**
- **Document-level ACLs cover fewer connectors.** Quick supports document-level
  ACLs for **S3, Confluence Cloud, SharePoint, and Google Drive** only. Q Business
  crawled ACLs across its full connector set. For everything else, AWS's advice is
  again to shard into per-role knowledge bases.
- **ACLs must be enabled at knowledge-base creation and are permanent** (same
  irreversibility posture as Q Business ACL crawling).
- One genuine improvement: **Quick's default is stricter.** "Quick does not ingest
  documents that lack an associated ACL entry… In contrast, Q Business grants all
  users access to S3 prefixes that do not appear in the ACL file." AWS warns
  migrators to give every document an explicit ACL entry first or lose content.
- **Q Apps must be hand-rebuilt as Quick Flows** (excluded from BYOI); AWS's
  documented method is to prompt Quick to generate a Flow from the Q App. **Form
  support does not yet exist in Quick Flows.**

## Quick's own capability set (per AWS)

Quick Sight (visualization), Flows (workflow automation), Automate (multi-step
business process automation), Research (cited research over enterprise + public
data), Spaces (unified files/dashboards/topics/knowledge bases), Apps
(interactive apps), Quick Index (shared knowledge base), plus mobile and desktop
apps. Connectors named: Slack, Microsoft Teams, Outlook, Google Workspace, Zoom,
Airtable, Dropbox, CRMs, databases. Subscription tiers gate integration setup —
creating knowledge bases and action connectors requires **Enterprise**;
Professional users can only consume what's shared with them.

## Unrelated but adjacent (do not conflate)

**Amazon Q Developer** — the IDE coding assistant — is separately being sunset in
**2027** in favour of **Kiro**. Different product, different successor, different
timeline. Mentioned in the 2026-05-04 AWS weekly roundup.
