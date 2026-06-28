URL: https://github.com/docker/mcp-gateway
Fetched: 2026-06-28
Note: Source repo — authoritative for license and feature list. NOTE license = MIT (not Apache-2.0).

---

License: MIT ("This project is licensed under the MIT License - see the LICENSE file for details.")

Project: "a docker CLI plugin" implementing the Model Context Protocol (MCP), enabling AI apps to securely connect to external tools/services. Manages MCP server lifecycle within Docker containers; unified interface for multiple AI clients.

Key features (from README):
- Container-based Servers: Run MCP servers as Docker containers with proper isolation
- Server Management: List, inspect, and call MCP tools, resources and prompts from multiple servers
- Secrets Management: Secure handling of API keys and credentials via Docker Desktop
- OAuth Integration: Built-in OAuth flows for service authentication
- Server Catalog: Manage and configure multiple MCP catalogs
- Dynamic Discovery: Automatic tool, prompt, and resource discovery from running servers
- Monitoring: Built-in logging and call tracing capabilities

Container execution: isolates each MCP server in its own Docker container with restricted host privileges; npx and uvx servers receive minimal permissions.
