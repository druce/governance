---
title: Enterprise AI Assistant
type: category
name: Enterprise AI Assistant
slug: enterprise-ai-assistant
layer: ux
priority: day-1
trifecta_role: all
maps_to_seed_doc: Enterprise AI Assistant
maps_to_seed_csv: Enterprise Chat & RAG
vendor_count: 9
status: drafted
last_updated: 2026-06-30
---

## Business objective

The actual chatbot your people use, with enterprise plumbing attached. A governed, compliant, general-purpose assistant: the same conversational AI employees would otherwise reach for in the consumer web, but wired into your tenant with SSO, admin controls, logging, archival, retention, data-residency, and a contractual promise that prompts aren't used to train the vendor's models. This is the user-experience layer — the thing everyone actually touches — and the reason the entire rest of the stack exists.

The seed's blunt observation matters: *if people aren't using the enterprise assistant, most of the other layers don't come into play* — they'll use the consumer version instead, and you've lost visibility entirely. So picking a sanctioned assistant people actually *like* is itself a security control: it's how you pull usage out of [shadow AI](ai-access-governance.md) and into something you can govern.

## When you need it

**Day-1.** This is usually the first deliberate AI decision a firm makes, and it's the anchor the rest of the stack hangs off. Most hedge funds will standardize on one of: the assistant bundled with their existing productivity suite (M365 Copilot for Microsoft shops, Gemini for Google shops), a frontier-lab enterprise plan (ChatGPT Enterprise, Claude Enterprise), and/or a cross-source work assistant (Glean). Many run two: a general frontier assistant *plus* the suite-native one.

The governance to stand up alongside it:
- Route it through your [ai-gateway](ai-gateway.md) and [network-security-sase](network-security-sase.md) so traffic is logged and inspectable.
- Confirm the data-handling terms (no-training, retention, residency) before rollout.
- If it retrieves internal data (Copilot, Glean, Q Business), [entitlement-aware-rag](entitlement-aware-rag.md) is a hard prerequisite — see that page; an assistant pointed at unclean permissions is a leak engine.
- Capture prompts/responses for [comms-surveillance](comms-surveillance.md) — for a regulated fund, assistant chats are in-scope communications.

## Lethal-trifecta role

The assistant is where **all three legs can converge**, which is exactly why it's the focal point. It takes **untrusted input** (a user paste, a retrieved document carrying an injected instruction), touches **sensitive data** (via RAG, file uploads, connected tools), and has **egress** (it can summarize-and-send, call tools, or simply be screenshotted). On its own a raw assistant lights up the whole trifecta. The job of the surrounding stack — [ai-runtime-security](ai-runtime-security.md) on the prompt path, [entitlement-aware-rag](entitlement-aware-rag.md) on retrieval, [ai-access-governance](ai-access-governance.md) on what data flows to which model, trust-zone design underneath — is to ensure the three legs never line up inside it. The assistant sits in the yellow zone: trusted UX, untrusted content flowing through it.

## Vendors

Three rough groups: frontier-lab assistants, suite-native copilots, and cross-source work assistants.

**Frontier-lab enterprise assistants** (general-purpose, model-maker direct)
- [openai-chatgpt-enterprise](../vendors/openai-chatgpt-enterprise.md) — ChatGPT Enterprise; the broadest consumer-familiarity, enterprise plan with SSO/admin/no-training terms.
- [anthropic-claude-enterprise](../vendors/anthropic-claude-enterprise.md) — Claude Enterprise; positioned on safety, long context, and coding; common second assistant.
- [perplexity-enterprise](../vendors/perplexity-enterprise.md) — Perplexity Enterprise; answer-engine framing with cited web + internal search; lighter-weight research assistant.

**Suite-native copilots** (bundled with the productivity platform you already own)
- [microsoft-365-copilot](../vendors/microsoft-365-copilot.md) — M365 Copilot; retrieves across your tenant via [microsoft-graph](../vendors/microsoft-graph.md), honoring existing permissions; default for Microsoft shops.
- [gemini-enterprise](../vendors/gemini-enterprise.md) — Gemini Enterprise / Agentspace; Google's equivalent for Workspace shops, with agent-building.
- [amazon-q-business](../vendors/amazon-q-business.md) — Amazon Q Business; AWS-native assistant over enterprise connectors, strong for AWS-centric estates.

**Cross-source work assistant** (search-grounded, source-agnostic)
- [glean](../vendors/glean.md) — connects across SaaS and document stores with a permissions-mirroring index; for many buyers Glean is simultaneously the assistant and the [entitlement-aware-rag](entitlement-aware-rag.md) layer. Cross-listed there.

**Vertical / in-tenant (regulated finance)** (a niche alternative to the horizontal players)
- [audition-ai](../vendors/audition-ai.md) — compliance-first AI assistant + agent platform purpose-built for hedge funds, deployed inside the customer's own Azure tenant with DLP, permission-aware retrieval, and audit baked in. Cross-listed in [ai-governance-platform](ai-governance-platform.md) and [dlp](dlp.md).

**Entitlement overlay** (not an assistant, but bought alongside one)
- [knostic](../vendors/knostic.md) — knowledge-boundary guardrail over Copilot/Glean-class assistants; see [entitlement-aware-rag](entitlement-aware-rag.md).

## Consolidation / M&A dynamics

No startup-roll-up dynamic here — the field is anchored by the largest tech and AI companies (Microsoft, Google, Amazon, OpenAI, Anthropic), so "consolidation" looks like platform bundling, not acquisition. The competitive pressure runs the other way: suite-native copilots (free-ish with your existing licenses) squeezing standalone assistants and cross-source players like Glean, which must justify a separate line item against "you already have Copilot." No seed M&A flags in this category.

## Adjacent categories

- [entitlement-aware-rag](entitlement-aware-rag.md) — the safety precondition when the assistant retrieves internal data; non-negotiable for Copilot/Glean/Q.
- [ai-access-governance](ai-access-governance.md) — governs employees reaching for *unsanctioned* assistants; the sanctioned assistant here is the carrot, shadow-AI control is the stick.
- [ai-gateway](ai-gateway.md) — the logging/routing chokepoint assistant traffic should pass through.
- [ai-runtime-security](ai-runtime-security.md) — prompt-injection / jailbreak / leak inspection on the assistant's I/O.
- [third-party-ai-apps](third-party-ai-apps.md) — domain-specific AI tools that aren't the general assistant but need the same controls.
- [comms-surveillance](comms-surveillance.md) — captures assistant chats as regulated communications.
- [content-sources](content-sources.md) / [vector-retrieval](vector-retrieval.md) — the retrieval plumbing behind a RAG-enabled assistant.

## Survey

**Question.** Which enterprise AI assistant(s) is your firm using or evaluating as the sanctioned general-purpose chat/RAG tool? (Select all that apply.)

**Answer options.**
- ChatGPT Enterprise (OpenAI)
- Claude Enterprise (Anthropic)
- Microsoft 365 Copilot
- Gemini Enterprise / Agentspace (Google)
- Amazon Q Business
- Perplexity Enterprise
- Glean
- Audition AI (finance-vertical, in-tenant)
- Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.**
- **Table-stakes:** ChatGPT Enterprise, Claude Enterprise, M365 Copilot are the dominant shortlist; expect most respondents to pick at least one, and many to run two (a frontier assistant + their suite copilot). The seed's note — *"if people are not using enterprise, most of the layers don't come into play"* — makes this the single most diagnostic question in the survey; an empty answer means the firm likely has ungoverned shadow usage.
- **Suite-native vs standalone** is the real axis: Copilot/Gemini/Q come "free" with the platform, so adoption may reflect existing vendor lock-in more than preference. Consider asking *why* (bundled vs chosen).
- **Glean straddles** assistant and [entitlement-aware-rag](entitlement-aware-rag.md) — some respondents think of it as search, others as their assistant. The cross-listing is intentional; a short clarifier helps.
- Don't merge this with the [entitlement-aware-rag](entitlement-aware-rag.md) question — keep "which assistant" separate from "how you enforce who-sees-what," or you'll double-count.
- **Audition AI is niche/vertical** — purpose-built for regulated finance and far smaller than the incumbents. Useful as an explicit option for this survey's hedge-fund audience (it competes on data-residency + compliance, not breadth), but expect low penetration; most "Other" write-ins for a fund-specific assistant belong here.

## Open taxonomy questions

- **Assistant vs RAG-platform overlap.** Glean (and arguably Copilot) belong in both this and [entitlement-aware-rag](entitlement-aware-rag.md). Resolved by cross-listing; flag for final pass whether the survey should explicitly de-dupe.
- Whether "answer engines" (Perplexity) deserve a sub-segment from "chat assistants" — different usage pattern (research/citations vs general task), same governance needs. Left grouped for now.
- Coding assistants (Copilot for code, Claude Code, Cursor) are deliberately *not* here — they map to [software-supply-chain](software-supply-chain.md) and developer tooling, a different control surface.
