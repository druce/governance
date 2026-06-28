URL: https://www.perplexity.ai/help-center/en/articles/11187708-data-retention-and-privacy-for-enterprise-organizations-and-users ; https://www.perplexity.ai/help-center/en/articles/11652747-audit-logs ; https://www.perplexity.ai/help-center/en/articles/12569435-how-to-use-the-microsoft-sharepoint-connector ; https://www.perplexity.ai/help-center/en/articles/12009761-enterprise-file-limits
Fetch date: 2026-06-28
Note: Perplexity Enterprise retention, admin controls, connectors, audit logs. (Help center 403 on WebFetch; captured via WebSearch summaries 2026-06-28.)

Key extracted points:
- Data retention: Uploaded files retained 7 days by default (some sources: 1-day auto-deletion for uploaded files). The Thread containing files is not deleted unless requested. Organizations with 50+ Enterprise Pro seats OR 1 Enterprise Max seat can set CUSTOM data retention periods and force deletion at any time. ("Configuring Data Retention" admin video exists.)
- Admin controls: Admins manage file, sharing, and connector permissions org-wide from admin control panel — file upload/download permissions, shared content (Threads, Pages, Spaces) permissions, and data integrations/connectors (Google Drive, OneDrive, SharePoint, Box, Dropbox) enable/disable per org.
- Connectors honor source permissions: For SharePoint, deleting a file or removing access in SharePoint immediately removes it from Perplexity. Files uploaded to Spaces from connected apps are searchable by anyone with Space access, but users need permissions on the connected app to VIEW file contents (permission-aware retrieval at view time).
- Spaces limits: Enterprise Pro Spaces up to 500 files / 50MB each; Enterprise Max up to 5,000 files.
- Audit Logs: capture end-to-end queries (user input, agent steps, answers) plus admin settings changes; each entry has event type, timestamp, user email, IP. Delivered in REAL TIME to a customer-configured WEBHOOK endpoint via HTTP POST. Exclusive to orgs with 50+ seats or >=1 Enterprise Max user.
- Data export: organizations can export data in JSON, CSV, PDF.
