# Amazon Bedrock AgentCore Policy (Cedar) — AWS News Blog + What's New GA + AWS Security Blog multi-agent Cedar post

- URLs: https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/ ; https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/ ; https://aws.amazon.com/blogs/security/enforce-least-privilege-authorization-in-multi-agent-ai-chains-using-cedar/
- Fetched: 2026-10-26
- Good for: AWS's agent/MCP authorization positioning on Cedar; preview and GA dates; whether AVP is in the agent path.

## AWS News Blog (2025-12-02, Danilo Poccia; updated)
- Policy in AgentCore announced in preview 2025-12-02; **GA 2026-03-03** (per update note; What's New page also dated 2026-03).
- Policy "gives you control over the actions agents can take and are applied outside of the agent's reasoning loop".
- Integrates with **AgentCore Gateway**, intercepting tool calls before they run; a policy engine (collection of policies) attaches to one or more gateways.
- Policies authored in natural language (converted to Cedar, checked against the tool schema, automated reasoning flags over-permissive / over-restrictive / unsatisfiable rules) or directly in **Cedar**.
- Enforce mode vs log-only mode.
- The post does **not** say AgentCore Policy runs on Amazon Verified Permissions.
- What's New (GA): 13 regions across US, APAC, Europe.

## AWS Security Blog (2026-07-06, Dhananjay Karanjkar) — "Enforce least-privilege authorization in multi-agent AI chains using Cedar"
- Reference architecture uses **Amazon Verified Permissions** policy store; the evaluator retrieves Cedar policies from it.
- Three-layer Cedar model: L1 agent-to-tool; L2 agent-to-agent delegation (hop limits, capability subsets); L3 originating user (role, MFA, delegation depth).
- AI agent is an **MCP client**; an MCP protocol adapter Lambda normalizes inbound requests. Cognito OAuth 2.0 + TOTP MFA; HMAC-signed user context; OCSF audit events to CloudWatch; API Gateway + WAF; CDK.
- "Cedar evaluates authorization but doesn't establish identity."
- This is a reference pattern (blog + sample), not a packaged product.
