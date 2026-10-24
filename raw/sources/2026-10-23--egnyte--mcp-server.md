# Egnyte — MCP server (Microsoft connector doc + Egnyte helpdesk release notes)

- URL: https://learn.microsoft.com/en-us/connectors/egnytemcpserver/ (doc updated 2026-07-22)
- URL (search snippets, not fetched): https://helpdesk.egnyte.com/hc/en-us/articles/43408860792461 ; https://helpdesk.egnyte.com/hc/en-us/articles/44361750683661
- Fetched: 2026-10-23
- Good for: MCP support level, how agent access is permissioned.

## Extract (Microsoft Learn, "Egnyte MCP Server (Preview)", publisher Egnyte, Inc.)
- "Every request honors existing Egnyte permissions, roles, and folder-level security controls, so enterprise content stays governed and never leaves Egnyte's control."
- Requires a plan with the **AI add-on**; admin must enable "Allow external LLM clients to connect to Egnyte via MCP" and select allowed apps.
- OAuth 2.0; operations performed on behalf of the signed-in user.
- Tools: search, advanced_search, list_filesystem_by_path, ask_document, ask_copilot, summarize_document, ask_knowledge_base, fetch, download_file_by_id/path, upload_file (text formats only), create_folder, set_file_metadata, create_link, list_links, comments.
## Extract (search snippets, Egnyte helpdesk)
- Feb 2026 release notes: MCP server moved from limited availability to all customers on plans with the AI add-on; works as an app in ChatGPT and connector in Claude.
- Mar 2026: per-app admin controls; ChatGPT, Claude, Microsoft Copilot and local CLI tools enabled by default; unregistered web MCP clients off by default ("highly permissive" warning).
