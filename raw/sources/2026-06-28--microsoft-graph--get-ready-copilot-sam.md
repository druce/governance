URL: https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management
Fetched: 2026-06-28
Note: Primary MS Learn doc. Microsoft's own pre-Copilot readiness guide — confirms the oversharing risk (Copilot inherits existing permissions and makes overshared content trivially discoverable) and the remediation tooling (SharePoint Advanced Management / Syntex, Data Access Governance reports, Restricted Access Control, Restricted Content Discovery). Good for the oversharing/Purview/Knostic context.

KEY EXTRACTED TEXT (trimmed):

"Microsoft 365 Copilot and agents work best for your organization when your content is up to date and well governed. Copilot and agents retrieve data from Microsoft Graph and respect existing permissions, sharing settings, and policies."

Content Management Assessment hub: "Identify potentially overshared content; Find issues or risks (such as inactive or ownerless sites); Define Copilot readiness for the organization..."

Step 3 Prevent accidental oversharing: "By default, SharePoint sets sharing settings to the most permissive option." Use Data Access Governance reports to identify oversharing risks:
- Site permissions baseline report — overall access exposure snapshot.
- Site permissions for users report — all sites a given user can access.
- "Everyone except external users (EEEU) report helps you identify the top 100 sites where content was shared with your entire organization in the past 28 days."
- Sharing links activity reports — sites with most "Anyone" / org-wide links.

Restricted Access Control: "Users who aren't part of the specified group can't access the site or its contents, even if they had prior access through permissions or a link." Used to "Ensure that only authorized users can access content and see it in Copilot."

Restricted Content Discovery: "Prevent content from appearing in Copilot or agentic experiences and in organization-wide search queries; Reduce accidental exposure while leaving site permissions unchanged... useful for content that must remain accessible, but shouldn't be broadly discoverable."

Risk signals for high-risk sites: "Broad sharing through 'Anyone,' 'Everyone,' and organization-wide links; Large audiences with excessive permissions; Broken permission inheritance and complex access models; Sensitive content with weak protection; Unlabeled or public sites; Governance gaps with ownerless, inactive, or unreviewed sites."

Also: SharePoint Admin Agent (content governance agent), Microsoft 365 Archive (Copilot not trained on archived content), Microsoft 365 Backup. ms.date 2026-06-25.
