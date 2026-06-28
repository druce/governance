---
type: category
name: AI-SPM (AI Security Posture Management)
slug: ai-spm
layer: model-prompt
priority: day-2
trifecta_role: none-detection (posture/inventory across all three legs; not an inline control)
maps_to_seed_doc: AI-SPM / Agent Governance
maps_to_seed_csv: AI-SPM
vendor_count: 14
status: drafted
last_updated: 2026-06-28
---

# AI-SPM (AI Security Posture Management)

## Business objective

AI-SPM is the **inventory-and-posture layer for your AI estate**: it discovers every
model, AI feature, copilot, agent, prompt, dataset, and API key that touches AI across
the org, scores how exposed each is, and flags drift from policy. In the seed doc's
register it's "the supervisor watching the bots and agents you didn't know you had" —
the tool that answers "what AI do we actually have running, who built it, what can it
reach, and where is it misconfigured?" before something goes wrong.

It is mostly a **visibility and governance** plane, not an inline enforcement plane.
Where [[ai-runtime-security]] sits in the request path and blocks a bad prompt in real
time, AI-SPM works more like CSPM/DSPM for AI: continuous discovery, configuration
assessment, and risk scoring of the AI assets themselves.

## When you need it

Day-2 for most hedge funds — it earns its place **once AI usage sprawls**: multiple
copilots, home-grown LLM apps, a handful of agents, model endpoints in more than one
cloud. A 50-person fund running only ChatGPT/Claude Enterprise through a gateway doesn't
need a dedicated AI-SPM tool yet; the gateway and [[ai-access-governance]] cover the
visibility. The trigger to buy is **agent and shadow-AI proliferation** — when no single
person can list every AI system and its blast radius. Under SR 11-7 model-risk
expectations, an authoritative AI inventory also becomes useful evidence, which can pull
this earlier for a regulated shop.

## Lethal-trifecta role

AI-SPM doesn't *break* a specific leg inline — it **maps where all three legs line up**.
It surfaces the AI systems that simultaneously take untrusted input, can reach sensitive
data, and have an egress path, so you can prioritise controls (segmentation, runtime
firewalling, authz). It spans trust zones rather than living in one: it inventories
red/yellow/green assets and flags the ones that violate your zone design.

## Vendors

**AI-native posture & agent inventory**
- [[noma-security]] — discovery, posture, and runtime governance for AI/ML pipelines and agents; common AI-SPM shortlist anchor.
- [[cranium]] — AI inventory, supply-chain/model risk, and posture aimed at governance/compliance teams.
- [[quilr]] — AI discovery and posture with overlap into shadow-AI/data-governance (positioning straddles AI-SPM and access governance).
- [[reco]] — SaaS-security-rooted AI discovery and posture across the SaaS estate; cross-listed with shadow-AI.
- [[nudge-security]] — SaaS/AI discovery via email/OAuth telemetry; finds shadow AI and accounts org-wide.

**Platform / cloud-security extensions (AI-SPM as a module)**
- [[wiz]] — AI-SPM as an add-on to its cloud-security platform (model/endpoint discovery in cloud).
- [[prisma-airs]] — Palo Alto's AI security platform; AI-SPM alongside runtime firewalling and an agent gateway.
- [[prompt-security]] — AI security suite spanning posture, runtime, and shadow-AI (per seed, acq. by SentinelOne — unverified).
- [[aim-security]] — enterprise AI security covering posture and runtime (per seed, acq. by Cato — unverified).
- [[astrix-security]] — non-human-identity roots; posture over agent/app identities and their access (per seed, acq. by Cisco — unverified).

**Agent-governance / overlap**
- [[zenity]] — governance and security for agents and low-code/copilot builders; primary in [[agent-runtime-security]], strong AI-SPM overlap.
- [[torq]] — SOC automation vendor with an AI-governance posture offering; overlaps SecOps tooling.
- [[hiddenlayer]] — model scanning and ML asset risk; posture angle overlaps with its runtime/red-teaming work.
- [[pillar-security]] — AI app discovery and posture alongside runtime protection.

## Consolidation / M&A dynamics

This category is consolidating into bigger security platforms. Per seed flags
(all **unverified — to confirm in research**): Wiz acq. by Google; Prompt Security acq.
by SentinelOne; Aim Security acq. by Cato; Astrix acq. by Cisco; Prisma AIRS is Palo
Alto and reportedly folds in former Protect AI. The pattern: cloud-security, SASE, EDR,
and AI-firewall vendors all want AI-SPM as a module, squeezing standalone players toward
the AI-native independents (Noma, Cranium, Quilr).

## Adjacent categories

- [[agent-runtime-security]] — the inline/runtime sibling; AI-SPM inventories agents, agent-runtime protects them as they act. Heavy vendor overlap (Zenity, Noma).
- [[ai-runtime-security]] — the real-time firewall; AI-SPM finds the apps, runtime security guards their traffic.
- [[ai-access-governance]] — shadow-AI discovery for *employee usage*; AI-SPM leans toward *systems/agents you build and run*. Reco/Nudge/Quilr span both.
- [[ai-governance-platform]] — model-risk/compliance governance; AI-SPM feeds it the technical inventory and posture evidence.
- [[dspm]] — same posture-management pattern applied to data rather than AI assets.

## Survey

**Question.** Which AI Security Posture Management (AI-SPM) tools is your organization
using or evaluating to discover and govern your AI/agent estate? *(Select all that apply
and indicate stage.)*

**Answer options.** Noma · Wiz · Prisma AIRS (Palo Alto) · Prompt Security · Aim Security ·
Astrix · Cranium · Quilr · Zenity · Reco · Nudge Security · Torq · Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- **Table-stakes / most-recognized:** Noma, Wiz, Prisma AIRS. **Niche / specialised:** Cranium, Quilr, Torq.
- **Overlap risk:** Zenity and Noma also appear under [[agent-runtime-security]]; Reco, Nudge, and Quilr also appear under [[ai-access-governance]]. Respondents may not distinguish "AI-SPM" from "agent security" or "shadow-AI" — consider a short definition line ("discovery/inventory/posture of your AI systems and agents") to disambiguate.
- **M&A dates the options:** Wiz, Prompt Security, Aim, and Astrix may show up under acquirer brands (Google, SentinelOne, Cato, Cisco) — keep both names recognizable.

## Open taxonomy questions

- **ai-spm vs [[agent-runtime-security]] is the messiest overlap in this layer.** The seed doc folds "Agent Security" into the "AI-SPM / Agent Governance" row; the CSV splits them into separate survey questions. We keep both as distinct categories (see Q1 in taxonomy-gaps.md) and accept that several vendors (Zenity, Noma, Lasso) legitimately span both. Rule of thumb used here: **AI-SPM = discover/inventory/assess posture (visibility plane); agent-runtime-security = protect agents while they act (enforcement plane).** Many products sell both and the line is marketing-driven, not architectural.
- Quilr/Reco/Nudge also straddle [[ai-access-governance]] (shadow-AI). Whether "AI-SPM" should absorb shadow-AI discovery, or stay scoped to built/owned AI systems, is an open cut.
- Candidate to revisit after research: whether "AI-SPM" and "AI governance platform" converge for regulated buyers who mainly want the inventory as compliance evidence.
