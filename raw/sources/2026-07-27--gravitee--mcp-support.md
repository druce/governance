# Gravitee MCP support (MCP Proxy, MCP Tool Server, ACLs, auth), pricing, certs

- URL: https://www.gravitee.io/blog/gravitee-mcp-the-complete-guide-to-mcp-support
  + https://documentation.gravitee.io/apim/ai-agent-management/convert-your-apis-to-mcp-servers
  + https://www.gravitee.io/pricing
  + https://trust.gravitee.io/ and https://www.gravitee.io/news/gravitee-achieves-iso-27001-and-iso-27701-certification
- Fetched: 2026-07-27
- Good for: the MCP-gateway claim specifically; pricing model; certifications.

## MCP facts

- **Two distinct MCP shapes**:
  - **MCP Tool Server** — turns an existing REST API into MCP tools by importing its
    **OpenAPI spec**; "any REST API with an OpenAPI spec becomes an MCP-compliant tool
    with no backend code changes." Implemented by enabling the **MCP Entrypoint** on a
    v4 proxy API. (This is the same trick Kong ships.)
  - **MCP Proxy** — a native v4 API type introduced in **Gravitee 4.10** that sits in
    front of **existing upstream MCP servers**, i.e. a true MCP gateway rather than an
    MCP-server generator.
- **MCP ACL Policy** restricts at the method level: `tools/list`, `tools/call`,
  `prompts/list`, `resources/subscribe`, `resources/read`.
- **Auth**: OAuth 2.1 with PKCE backed by Gravitee Access Management; **Dynamic Client
  Registration**; **MCP Resource Server v2** (Gravitee **4.11**) for token introspection
  and certificate management. Fine-grained authz via **OpenFGA**.
- **Observability**: MCP Analytics dashboard (tool usage, agent behaviour, method
  distribution); **tool invocation throttling** to stop a misbehaving agent hammering an
  endpoint; audit trail per MCP interaction tied to agent identity + OAuth client.
- **Agent Catalog** for tool discovery/registration.
- The APIM MCP Server component is stated to be open source on GitHub; **which of the
  above are Community Edition vs Enterprise is not stated** in the guide.

## Pricing (public list pricing, unusual for this space)

- API Management editions: **Planet $2,500/mo**, **Galaxy** (mid, event-broker support,
  consumption option), **Universe** (custom, unlimited gateways).
- Event Management editions: **Comet $1,250/mo**, **Meteor**, **Asteroid** (custom).
- **Agent Management Package** and **Enterprise Auth Package** are priced separately —
  i.e. the AI/MCP gateway is a paid add-on, not bundled into the base API-management tier.
- Deployment: Gravitee Cloud (SaaS), self-hosted, hybrid (split control/data plane),
  customer-hosted control plane on higher tiers with approval.
- Community Edition exists and is described elsewhere by Gravitee as **Apache 2.0**.

## Certifications

- **ISO/IEC 27001** and **ISO/IEC 27701** certified **2021-12-15**, certificate 175256,
  NQA/UKAS, scope: API management, design and security software solutions.
- Trust Center (trust.gravitee.io) additionally lists **SOC 2 Type 2** and
  **PCI DSS v4.0.0**, with reports available on request. SOC 2 report date/period
  not public.
