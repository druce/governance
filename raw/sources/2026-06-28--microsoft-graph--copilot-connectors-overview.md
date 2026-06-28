URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview
Fetched: 2026-06-28
Note: Primary MS Learn doc. Defines Microsoft 365 Copilot connectors (Graph connectors) — synced vs federated — and confirms each ingested item carries an ACL so search/Copilot only return content the user can access in the source system. Good for the external-data + permission-trimming angle and the MCP federated-connector detail.

KEY EXTRACTED TEXT (trimmed):

"Microsoft 365 Copilot connectors extend the reach of Microsoft 365 Copilot and Microsoft Search experiences by connecting to data beyond Microsoft 365. Your organization can either index external data by using synced connectors or connect to data in real time by using federated connectors."

Synced connectors: "crawl and index content from external sources into Microsoft Graph... Respect source permissions; users only access content for which they have appropriate permissions." Organization-level access model; admins configure.

Federated connectors: "use an MCP model to fetch data in real time, without indexing content into Microsoft 365... Secure by design; federated access respects source permissions and authentication (OAuth 2.0)... read-only." User-level access model.

How Copilot connectors work: "A Copilot connector defines a connection to an external data source and syncs content into Microsoft 365. It uses the Microsoft Graph connectors API to ingest items into the Microsoft Graph index. Each item includes content, metadata (like title and URL), and an access control list (ACL) that enforces permissions."
- "Unified index - The item becomes part of your organization's cloud search index. It's full-text searchable and processed by semantic indexing AI for relevance."
- "Permission-based filtering - Search and Copilot only show items to users who have access in the source system."
- "External content is stored securely in your tenant, and users only see what they're allowed to access."

Prebuilt connectors: "over 100 prebuilt connectors" incl. Box, Dropbox, Google Drive, Confluence, Salesforce, ServiceNow, Dynamics 365, SQL/Oracle, SAP, Workday, Zendesk, Jira. Custom connectors via Microsoft 365 Agents Toolkit or Microsoft Graph connectors API. On-prem sources via the Microsoft Graph connector agent.

Copilot Chat / Search: "Security enforced - Users only see content they're authorized to access." Connectors are knowledge sources for custom agents built with Copilot Studio / Agents Toolkit; "Admins control which connectors and actions each agent can use."
