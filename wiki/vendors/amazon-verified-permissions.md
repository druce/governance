---
title: Amazon Verified Permissions (Cedar)
type: vendor
name: Amazon Verified Permissions (Cedar)
slug: amazon-verified-permissions
aka: [AVP, Verified Permissions, Cedar, Cedar policy language, cedar-policy]
primary_category: authorization-engine
also_listed_in: []
website: https://aws.amazon.com/verified-permissions/
founded: 2023
hq: Seattle, Washington, USA (Amazon Web Services)
ownership_state: public
owner: Amazon (AWS)
ownership_note: 'Verified Permissions is an AWS managed service (Amazon, NASDAQ: AMZN). Preview 2022-11-28, GA 2023-06-13. The Cedar language and engine it runs were open-sourced by AWS on 2023-05-10 (Apache-2.0) and accepted into the CNCF as a Sandbox project on 2025-10-08. Cedar is foundation-hosted; maintainer diversity outside AWS not verified.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (AWS product)
last_funding: n/a
market_position: {authorization-engine: platform-module}
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: partial
integrations: [amazon-cognito, amazon-api-gateway, aws-appsync, express, bedrock-agentcore]
mcp_support: unverified
certifications: []
pricing_model: usage (per authorization request; no minimum)
fs_traction: claimed
target_customer: AWS-centric engineering teams that want a managed policy decision point for their own applications, APIs and (increasingly) agent tool calls
last_verified: 2026-10-26
verify_after: null
tags: [authorization, pdp, cedar, aws, abac, rbac, rebac, formal-verification, cncf-sandbox, agent-authorization]
sources:
  - {claim: "AVP is a fully managed authorization service using Cedar; API Gateway/AppSync integration; Express support; named customers FIS, Grosvenor, Stedi, Twilio, TELUS; no agent/MCP messaging on product page", url: "https://aws.amazon.com/verified-permissions/", date: 2026-10-26, confidence: high}
  - {claim: "Per-request pricing: $0.000005 per single authorization request; tiered batch pricing; $0.00004 per policy-management request; no upfront or minimum fees", url: "https://aws.amazon.com/verified-permissions/pricing/", date: 2026-10-26, confidence: high}
  - {claim: "Cedar accepted to CNCF on 2025-10-08 at Sandbox level", url: "https://www.cncf.io/projects/cedar/", date: 2025-10-08, confidence: high}
  - {claim: "Cedar CNCF Sandbox announcement; spec formally verified in Lean; adopters Cloudflare, MongoDB, StrongDM, Cloudinary, Bedrock AgentCore Policy, AWS Systems Manager", url: "https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project", date: 2025-12-15, confidence: high}
  - {claim: "Cedar engine is Apache-2.0, written in Rust", url: "https://github.com/cedar-policy/cedar", date: 2026-10-26, confidence: high}
  - {claim: "AgentCore Policy: preview 2025-12-02, GA 2026-03-03; Cedar policies attached to AgentCore Gateway intercept tool calls outside the agent loop; natural-language authoring converted to Cedar; enforce or log-only mode; post does not say AVP is used", url: "https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/", date: 2026-03-03, confidence: high}
  - {claim: "Reference architecture for multi-agent MCP chains using Cedar in an AVP policy store; three policy layers (agent-to-tool, agent-to-agent, originating user)", url: "https://aws.amazon.com/blogs/security/enforce-least-privilege-authorization-in-multi-agent-ai-chains-using-cedar/", date: 2026-07-06, confidence: high}
  - {claim: "Timeline: preview 2022-11-28; Cedar open-sourced 2023-05-10; AVP GA 2023-06-13; Cedar 4 migration 2025; Cedar 2 policy stores disabled from 2026-04", url: "https://hidekazu-konishi.com/entry/aws_history_and_timeline_amazon_verified_permissions_and_cedar.html", date: 2026-10-26, confidence: medium}
  - {claim: "Policy store aliases, named policies and named policy templates (2026-04-06)", url: "https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-verified-permissions-policy-store", date: 2026-04-06, confidence: high}
---

# Amazon Verified Permissions (Cedar)

> Primary category: [authorization-engine](../categories/authorization-engine.md). This one page covers both the managed AWS service and the open-source **Cedar** language it runs. Other pages that mention Cedar ([keycard](keycard.md), [docker-sandboxes](docker-sandboxes.md), [permit-io](permit-io.md)) mean the language. Sources cached under `raw/sources/2026-10-26--amazon-verified-permissions--*`.

**One-liner**: AWS's managed authorization service. You write access rules in **Cedar**, AWS's open-source policy language, store them in AWS, and your applications (or agent tool gateways) call an API to get allow or deny for each request. Billing is per request.

**What it does**: Verified Permissions is a hosted **policy decision point**. You define a schema (principal types, resource types, actions) and Cedar policies such as "users in the PM group may read positions in their own book." Your code then calls `IsAuthorized` with the principal, action, resource and context. AVP validates policies against the schema, evaluates them, and returns a decision you can audit. Policy templates can be enforced directly in Amazon API Gateway and AWS AppSync. Cedar covers role-based, attribute-based and some relationship-based patterns in one language. AVP is decision-only. Your app or gateway still has to call it and enforce the answer, and it stores policies, not a relationship graph like [authzed](authzed.md) or [openfga](openfga.md).

**Cedar, the language**: AWS open-sourced Cedar (language plus Rust evaluation engine, Apache-2.0) on 2023-05-10. The CNCF accepted it as a **Sandbox** project on **2025-10-08**. Sandbox is the CNCF's entry tier. [open-policy-agent](open-policy-agent.md) is Graduated and [openfga](openfga.md) is Incubating. AWS says the language specification is **formally verified with the Lean theorem prover**, and the Rust engine is tested against that spec. This is Cedar's main technical difference from Rego: policies are designed to be analysable, so tools can check whether one policy set permits more than another. Cedar runs in many places besides AVP. AWS names Cloudflare, MongoDB, StrongDM and Cloudinary as adopters. In this wiki, [keycard](keycard.md), [docker-sandboxes](docker-sandboxes.md) and [permit-io](permit-io.md) use it. You can embed the open-source engine yourself with no AWS dependency.

**Agent authorization on AWS**: AWS's agent-authorization product is not AVP itself. It is **Policy in Amazon Bedrock AgentCore**, announced in preview 2025-12-02 and **generally available 2026-03-03**. AgentCore Policy attaches a set of Cedar policies to an **AgentCore Gateway**, which turns APIs and Lambda functions into MCP tools. The gateway checks every tool call against the policies before it runs, outside the agent's reasoning loop. Policies can be written in plain English, which AWS converts to Cedar and checks for rules that are too broad or can never match. Each gateway can run in enforce or log-only mode. AWS's launch post does **not** say AgentCore Policy runs on AVP. Treat them as two products that share a language. Separately, an AWS Security Blog reference design (2026-07-06) puts Cedar policies in an **AVP policy store** to authorize multi-hop chains of MCP agents. It uses three policy layers: agent to tool, agent to agent (hop limits, narrowing capabilities), and originating user (role, MFA). That design is a sample you build yourself, not a packaged feature.

## Agent-security role: the lethal trifecta

The lethal trifecta is the core agent-security threat model: untrusted input, sensitive data and outbound access in one agent context. AVP or AgentCore Policy cuts the **sensitive-data** and **egress** legs **per call**. It can deny the read of a record, or deny a tool call that would send data out, based on who the agent is acting for. It does not look at prompt content and will not detect an injection. A hijacked agent still gets every action its policy allows. The control is only as good as the policy's scope. AWS's own multi-agent post says "Cedar evaluates authorization but doesn't establish identity," so it depends on a trustworthy identity layer upstream (Cognito, your IdP, [non-human-identity](../categories/non-human-identity.md) tooling).

**Naming / provenance**: Previewed at re:Invent on 2022-11-28, GA on 2023-06-13 (per a third-party timeline that quotes AWS What's New; DevClass covered the GA on 2023-06-14). People often say "Cedar" and "Verified Permissions" interchangeably. They are not the same thing. Cedar is the CNCF language and engine. AVP is the AWS-hosted store and API. AgentCore Policy is a third thing that also uses Cedar. AVP moved its back end from Cedar 2.x to Cedar 4 during 2025. Per the same timeline (secondary, not verified against AWS docs), authorization calls were disabled from April 2026 for policy stores still on Cedar 2.

**Ownership & viability**: `public`, an AWS service. The usual AWS caveat applies: the service is unlikely to vanish, but AWS does deprecate things. Recent releases suggest active investment: Cedar 4.5 support (2025-08), policy store aliases and named policies (2026-04-06), and multiple namespaces (2026-05, secondary source). Cedar's move to the CNCF reduces lock-in risk at the language level. How many maintainers work outside AWS was not verified, and Sandbox status means governance is early. A firm that writes Cedar can move those policies to the open-source engine, to [permit-io](permit-io.md), or to another Cedar-based product, but not to OPA or OpenFGA without a rewrite.

**Positioning & differentiators**:
- **vs [open-policy-agent](open-policy-agent.md)**: OPA's Rego is more general and has a much larger ecosystem (Kubernetes admission control, infra policy). Cedar is narrower, focused on application authorization, easier to read, and built for formal analysis. OPA is something you run yourself. AVP is a managed AWS API.
- **vs [authzed](authzed.md) / [openfga](openfga.md)**: those are Zanzibar-style relationship databases that store "who is related to what" and walk the graph. AVP stores policies and expects you to pass in entity data with each request. For deep sharing hierarchies, ReBAC engines fit better.
- **vs [cerbos](cerbos.md) / [oso](oso.md) / [permit-io](permit-io.md)**: these are cloud-neutral, managed or self-hosted, and pitch agent and MCP authorization explicitly. AVP's advantages are AWS billing, AWS-native integration (API Gateway, AppSync, Cognito tokens), and no extra vendor. Its drawback is that it is AWS-only.

*Market position*: `platform-module` in [authorization-engine](../categories/authorization-engine.md). AWS-native shops adopt it as part of AWS, not as a separate vendor decision, and the Cedar language reaches further than the service does.

**Who should choose them / anti-fit**: Fits a fund that **builds internal apps or agents on AWS** (Lambda, API Gateway, Bedrock AgentCore) and wants a managed, auditable decision point without another vendor contract. FIS is a public reference for audit-trail use. Also fits if you have already standardised on Cedar through a product like Keycard or Docker and want the same language for your own apps. **Anti-fit**: multi-cloud or on-prem estates that need the PDP running locally next to the workload (use self-hosted OPA, Cerbos, or the open-source Cedar engine). Firms whose authorization is mostly relationship graphs ([openfga](openfga.md), [authzed](authzed.md)). Teams that want a vendor-supplied agent/MCP authorization product today, since AWS's packaged answer is AgentCore Policy and only covers tools behind AgentCore Gateway.

**Known weaknesses / gotchas**:
- **Three Cedar things, not one.** AVP, AgentCore Policy and open-source Cedar are separate. Buying one does not get you the others. Confirm which one a vendor or internal team means.
- **Network hop per decision.** Every check is a call to a regional AWS API. Latency and availability depend on that, unlike an embedded or sidecar PDP. Batch APIs help but are priced higher per call.
- **Cost scales with traffic.** At $0.000005 per single check, 1 billion checks a month costs about $5,000. Agent loops that check every tool call can generate many decisions. Model it before rollout.
- **No identity of its own.** AVP trusts the principal and context you send. Spoofed or over-broad agent identity defeats it.
- **Cedar version churn.** The forced Cedar 2 to Cedar 4 migration (2025–2026) shows that AWS will retire old policy-store versions.

**Deployment & data handling**: SaaS only, regional AWS service within your AWS account. `data_leaves_tenancy: partial`: entity attributes and context you send with each request (user groups, record tags, amounts) are processed by the AVP regional endpoint, not inside your VPC. No prompts or documents go to AVP unless you put them in the request context. AWS markets centralized monitoring of authorization requests and policy changes. Which log destination (CloudTrail or other) was not verified for this page. It sits **inline in the request path**: your app or gateway blocks on the decision.

**Integrations & partnerships**: Amazon API Gateway and AWS AppSync (policy templates enforced natively), Amazon Cognito and OIDC tokens via `IsAuthorizedWithToken`, Express (Node.js) framework support. Agent support comes indirectly through Cedar in AgentCore Policy and the AWS multi-agent MCP reference design. No AVP-specific MCP server was confirmed (`mcp_support: unverified`). Third-party products that use Cedar policies: [keycard](keycard.md), [docker-sandboxes](docker-sandboxes.md) / [docker-mcp-gateway](docker-mcp-gateway.md), [permit-io](permit-io.md); StrongDM and Cloudflare per AWS.

**Compliance & FS traction**: AWS service-level compliance programs (SOC, ISO, etc.) were not confirmed for AVP specifically on this pass, so `certifications` is left empty. Check AWS Artifact or the services-in-scope list. FS evidence: **FIS** (payments, Prophet team) uses AVP for RBAC plus ABAC with an audit trail it ties to Sarbanes-Oxley compliance. This is AWS marketing but names the customer. Size is not a problem: Stedi reports up to 700M requests a month.

**Commercial**: Usage-based, no minimum. Single check $0.000005. Batch checks are tiered from $0.00015 down to $0.00004 per request. Policy-management calls are $0.00004. No free tier is listed. The open-source Cedar engine is free.

## Open questions

- Does AgentCore Policy run on AVP internally, or on a separate Cedar engine? AWS's launch post doesn't say.
- Exact Cedar 2 cut-off date and current Cedar version on AVP. The April 2026 deprecation comes from a secondary timeline.
- Which AWS compliance attestations list AVP as in scope.
- Whether AWS ships an MCP server for AVP itself (policy authoring by agents) — not found.
- Cedar maintainer diversity outside AWS, and any CNCF Incubation application.

## Sources

- [Amazon Verified Permissions product page](https://aws.amazon.com/verified-permissions/) — fetched 2026-10-26 — supports: managed Cedar service, API Gateway/AppSync, customers incl. FIS; confidence: high (customer quotes are marketing)
- [AVP pricing](https://aws.amazon.com/verified-permissions/pricing/) — fetched 2026-10-26 — supports: per-request prices; confidence: high
- [CNCF: Cedar](https://www.cncf.io/projects/cedar/) — fetched 2026-10-26 — supports: Sandbox 2025-10-08; confidence: high
- [AWS Open Source Blog: Cedar joins CNCF as a Sandbox project](https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project) — fetched 2026-10-26 — supports: Lean verification, adopters; confidence: high
- [cedar-policy/cedar on GitHub](https://github.com/cedar-policy/cedar) — fetched 2026-10-26 — supports: Apache-2.0, Rust; confidence: high
- [AWS News Blog: AgentCore adds quality evaluations and policy controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) — fetched 2026-10-26 — supports: AgentCore Policy preview 2025-12-02, GA 2026-03-03, gateway interception, Cedar; confidence: high
- [AWS Security Blog: least-privilege authorization in multi-agent AI chains using Cedar](https://aws.amazon.com/blogs/security/enforce-least-privilege-authorization-in-multi-agent-ai-chains-using-cedar/) — fetched 2026-10-26 — supports: AVP + MCP reference design (2026-07-06); confidence: high
- [AVP and Cedar timeline (hidekazu-konishi.com)](https://hidekazu-konishi.com/entry/aws_history_and_timeline_amazon_verified_permissions_and_cedar.html) — fetched 2026-10-26 — supports: preview/GA/open-source dates, Cedar 4 migration; confidence: medium
- [AWS What's New: policy store aliases and named policies](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-verified-permissions-policy-store) — fetched 2026-10-26 — supports: 2026-04-06 release; confidence: high

## History

- [2026-10-26] Page created and researched in one pass (user-requested addition). Decided on one page covering AVP and Cedar, slugged on the AWS product, rather than a separate `cedar` project page. Reason: buyers pay for AVP; elsewhere Cedar shows up as a language inside other products (Keycard, Docker, Permit.io, AgentCore), not as a separate thing to adopt. Revisit if Cedar gets its own survey answer option or moves to CNCF Incubation. Confirmed Cedar CNCF Sandbox (2025-10-08) and AgentCore Policy GA (2026-03-03).
