---
title: AI Gateway
type: category
name: AI Gateway
slug: ai-gateway
layer: model-prompt
priority: day-1
trifecta_role: egress
maps_to_seed_doc: AI Gateway
maps_to_seed_csv: AI Gateway
vendor_count: 7
status: drafted
last_updated: 2026-06-28
---

# AI Gateway

## Business objective

The traffic cop and toll booth for model calls. An AI gateway is the single exit
door through which all of an organization's LLM traffic flows: it routes requests
to the right model/provider, enforces rate limits and budgets, manages API keys and
fallbacks, caches responses, and — crucially for governance — logs and archives
every prompt and response in one place. Instead of every team wiring its own
OpenAI/Anthropic/Bedrock keys, calls go through one governed chokepoint.

The gateway's value is mostly plumbing and control rather than security inspection:
routing, cost control, reliability (failover, retries), and a complete audit trail.
It is the place you *attach* the security ([ai-runtime-security](ai-runtime-security.md)) and visibility
([llm-observability](llm-observability.md)) controls, because it's the one point every model call must
cross.

## When you need it

Day-1, and lightweight to stand up. The first time more than one team or app calls
a model API, you want a single front door — for cost visibility, for kill-switch
control, and for the audit log that compliance and [comms-surveillance](comms-surveillance.md) will later
need. For a hedge fund the archival angle matters: a gateway that captures every
prompt/response is the cheapest way to make AI traffic reviewable for MAR/MNPI
purposes downstream. If you only use a vendor-hosted [enterprise-ai-assistant](enterprise-ai-assistant.md),
the assistant vendor is effectively your gateway; the moment you build apps on raw
model APIs, you want your own.

## Lethal-trifecta role

Controls **egress** by construction: it is the single outbound path for model
traffic, so it's where you enforce which models can be reached, what gets logged,
and where output-side policy attaches. On its own a gateway is a chokepoint, not an
inspector — it breaks the egress leg only when you bolt guardrails
([ai-runtime-security](ai-runtime-security.md)) onto it. It typically sits at the boundary of the
yellow/green zone, mediating all calls leaving internal apps for external model
providers.

## Vendors

**Developer/OSS-leaning gateways**
- [litellm](../vendors/litellm.md) — widely used open-source proxy/SDK that normalizes 100+ model providers behind one OpenAI-compatible API.
- [portkey](../vendors/portkey.md) — gateway plus guardrails, observability, and prompt management; control-plane oriented.
- [truefoundry](../vendors/truefoundry.md) — AI/ML platform with a gateway plus an [mcp-gateway](mcp-gateway.md) offering.
- [openrouter](../vendors/openrouter.md) — aggregator/marketplace routing to many models behind one API and billing relationship.

**Incumbent infra / API-management gateways**
- [kong](../vendors/kong.md) — API-gateway incumbent extended with an AI gateway (and MCP tool ACLs).
- [f5](../vendors/f5.md) — application-delivery incumbent with an AI gateway (and AI security via the CalypsoAI acquisition, per seed).
- [cloudflare](../vendors/cloudflare.md) — edge platform offering an AI gateway (caching, rate-limiting, analytics) alongside its network stack.

## Consolidation / M&A dynamics

Per seed flags (unverified — to confirm in research): Portkey flagged as acquired by
Palo Alto Networks; F5 flagged as having acquired [calypsoai](../vendors/calypsoai.md) (pairing a gateway
with AI guardrails). The broader pattern is two-sided: API-management and
networking incumbents (Kong, F5, Cloudflare, Palo Alto) are adding AI-gateway
features, while AI-native gateways add security and observability to move up the
stack. Expect gateway + firewall + observability to converge into single suites.

## Adjacent categories

- [ai-runtime-security](ai-runtime-security.md) — the inspection logic that attaches to the gateway chokepoint; often sold together.
- [llm-observability](llm-observability.md) — consumes the gateway's traces/logs; some gateways (Portkey) ship their own observability.
- [mcp-gateway](mcp-gateway.md) — the agent-era analogue: a single doorway for the *tools* agents call, where the AI gateway is the doorway for *model* calls. Several vendors (Kong, TrueFoundry) do both.
- [network-security-sase](network-security-sase.md) — the foundation-layer egress control the AI gateway complements at the application layer.

## Survey

**Question:** Which AI gateway products are you using or evaluating to route, govern,
and log your organization's model/API traffic?

**Answer options:** Portkey, LiteLLM, TrueFoundry, Kong AI Gateway, F5, Cloudflare,
OpenRouter, Other (Please Specify).

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:**
- LiteLLM is the most common OSS default; expect high "in production" among teams building on raw APIs.
- "AI gateway" overlaps confusingly with [mcp-gateway](mcp-gateway.md) (Kong, TrueFoundry appear in both) — clarify "model traffic" vs "agent tool access" in the question stem.
- Many shops use a model provider's native console or a SASE/proxy as a de-facto gateway; the Other field will catch DIY/none.
- M&A dates Portkey (flagged → Palo Alto) and F5 (flagged ← CalypsoAI); show product names respondents will recognize.

## Open taxonomy questions

- AI gateway vs [mcp-gateway](mcp-gateway.md): as agents dominate, does the model-call gateway fold into the tool-call gateway, or stay distinct?
- Where does a gateway end and an [ai-runtime-security](ai-runtime-security.md) firewall begin when one product does both (Portkey, F5, Prisma AIRS)?
