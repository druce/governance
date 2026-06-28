---
title: Third-Party AI Apps
type: category
name: Third-Party AI Apps
slug: third-party-ai-apps
layer: ux
priority: optional
trifecta_role: all
maps_to_seed_doc: Third-Party AI Apps
maps_to_seed_csv: "—"
vendor_count: 0
status: drafted
last_updated: 2026-06-28
---

## Business objective

The niche AI tools — legal review, coding, research, transcription, market-data copilots, deal-diligence assistants — funneled through the same controls as everything else *so they don't go rogue*. This is not a product category you buy; it's an **architecture and process** for bringing the long tail of domain-specific and vendor AI under the same governance you stood up for the general [enterprise-ai-assistant](enterprise-ai-assistant.md). The objective: any sanctioned third-party AI app routes through your [ai-gateway](ai-gateway.md), gets archived and SIEM-logged, runs against vetted vendor terms, and is subject to the same DLP and runtime inspection — rather than being a one-off SaaS login that silently ships your data to a model you've never reviewed.

## When you need it

**Optional / ongoing** — it kicks in *as vendors are onboarded*, not on Day-1. There's no single decision; it's a repeatable pattern you apply each time a desk wants a specialized AI tool. For a hedge fund the recurring cases are predictable: a research team wants an AI transcription/earnings tool, legal wants contract-review AI, engineering wants a coding assistant, an analyst wants a niche market-data copilot. Each is a [vendor-risk](vendor-risk.md) review plus a routing/logging decision. The discipline is to treat "we adopted another AI app" as an event that triggers: vendor-risk assessment → data-handling terms check → route through the gateway → log to SIEM and the comms archive → tag in your AI inventory.

If you skip this, third-party AI apps become indistinguishable from [shadow AI](ai-access-governance.md) — the only difference is whether procurement signed a contract.

## Lethal-trifecta role

Same profile as any assistant: a third-party AI app can take **untrusted input**, touch **sensitive data** you feed it, and **egress** to an external model and the vendor's infrastructure — so potentially **all three legs**. The added wrinkle is *vendor trust*: you're now also relying on a third party's security posture and data-handling, which is why [vendor-risk](vendor-risk.md) is the gating control. These apps sit in the yellow zone at best; until vetted and routed, assume red.

## Vendors

**None listed — this is a process/architecture category, not a shortlist.** The "vendors" are whatever domain-specific AI tools your business units adopt, and they're tracked individually through [vendor-risk](vendor-risk.md) and your AI inventory, not enumerated here. The governance is delivered by the *control* categories below, not by a product in this slot.

## Consolidation / M&A dynamics

N/A — no fixed vendor set. (The relevant M&A is whatever happens to the specific niche tools you've onboarded; track per-vendor.)

## Adjacent categories

- [enterprise-ai-assistant](enterprise-ai-assistant.md) — the general assistant; third-party apps are the specialized long tail that needs the *same* plumbing.
- [ai-gateway](ai-gateway.md) — the chokepoint third-party AI traffic should route through for logging and policy.
- [ai-access-governance](ai-access-governance.md) — the line between a *sanctioned* third-party app and shadow AI is just whether it went through this process; the discovery tooling there surfaces the ones that didn't.
- [vendor-risk](vendor-risk.md) — the gating assessment before any third-party AI touches your data.
- [ai-runtime-security](ai-runtime-security.md) — runtime inspection of prompts/responses for third-party apps you can intercept.
- [comms-surveillance](comms-surveillance.md) — captures outputs from in-scope third-party tools as regulated communications.

## Survey

**Skipped** — no vendor shortlist to ask about. A respondent doesn't "evaluate Third-Party AI Apps" as a product; the meaningful survey signal is *whether they have a process* for onboarding them, which is better captured as a process/maturity question (e.g. "Do you route third-party AI tools through your gateway and vendor-risk process?") than as a vendor multi-select. Flag for the survey designer as a candidate yes/no maturity item rather than a category question.

## Open taxonomy questions

- This is arguably a **process row dressed as a UX-layer category** — it has no vendors and overlaps heavily with [ai-access-governance](ai-access-governance.md) (shadow vs sanctioned) and [vendor-risk](vendor-risk.md) (the gate). Kept as its own page to mirror the seed doc, but flag for the final pass whether to fold it into those two.
- Boundary with [ai-access-governance](ai-access-governance.md): shadow-AI discovery *finds* ungoverned third-party apps; this category is the *onboarding discipline* that legitimizes them. Same coin, two sides — worth a tighter cross-reference.
