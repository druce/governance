URL: https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls ; https://docs.cloud.google.com/gemini/enterprise/docs/identity ; https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores ; https://workspaceupdates.googleblog.com/2026/06/google-vault-now-supports-retention-rules-and-litigation-holds-for-Gemini-app.html ; https://workspaceupdates.googleblog.com/2025/07/gemini-audit-logs-reporting-api-audit-and-security-invesitgation-tools.html
Fetched: 2026-06-28
Note: Certifications, entitlement-aware (ACL) search, IdP federation, and Google Vault/audit coverage for Gemini. Core governance evidence.

Compliance certifications (Gemini Enterprise Standard, Plus, NotebookLM Enterprise):
- FedRAMP (Google Cloud has FedRAMP High authorization broadly; verify SKU scope), ISO/IEC 27001, 27017, 27018, 27701, SOC 1, SOC 2, SOC 3, PCI DSS, BSI C5:2020, HIPAA (search product name in Google Cloud compliance pages to confirm SKU coverage).
- ISO/IEC 42001 (AI management system) awarded May 2025 to Gemini for Google Cloud, Vertex AI Agents, Gemini Code Assist.
- Security controls: VPC Service Controls (supported), CMEK (US/EU multi-region APIs only), Access Transparency (supported, not in `global` region), Google Cloud audit logging, data residency (DRZ).

Entitlement-aware enterprise search (ACLs):
- "Access control for your data sources in Gemini Enterprise limits the data that users can view in your search app's results."
- Connectors ingest both data and associated ACLs from sources (e.g., SharePoint, Jira, ServiceNow); at query time the user's verified identity is checked against source ACLs and only authorized documents are retrieved/summarized.
- Two methods: Pure ACLs (AclInfo; email-based identities recognized by Google Cloud) vs Identity Mapping (usernames/legacy/external IDs).
- "Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents."
- Workforce Identity Federation (WIF) supports syncless access via third-party IdPs (Entra ID, Okta, Ping) over OIDC/SAML 2.0 (per connector intro docs / community). Workspace connectors (Drive, Gmail, Chat, Calendar) require Google Identity and delegate ACLs to the native Workspace platform.

Google Vault / eDiscovery / audit (Gemini app in Workspace):
- 2025-02: Google Vault added support for the Gemini app (search/export prompts & responses).
- 2026-06: Google Vault now supports retention rules and litigation holds for the Gemini app; Vault retention/holds take precedence over Admin console / user settings.
- Caveat: applies to the Gemini app (web/mobile). "Gemini in Workspace" features embedded in other apps (e.g., "Help me write" in Gmail/Docs) are NOT retained in the same manner.
- 2025-07: Gemini audit logs accessible via Reporting API (Admin SDK) and surfaced in the security investigation tool / audit investigation tool.
