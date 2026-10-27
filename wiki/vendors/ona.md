---
title: Ona (OpenAI)
type: vendor
name: Ona
slug: ona
aka: [Gitpod, Gitpod Classic, Gitpod Flex, Gitpod Enterprise, Ona Agents, Ona Cloud, Ona Guardrails, Veto, gitpod.io, ona.com]
primary_category: ephemeral-environments
also_listed_in: []
website: https://ona.com/
founded: null
hq: null
ownership_state: acquired-closed
owner: OpenAI
ownership_note: 'Formerly Gitpod; renamed Ona 2025-09-02. OpenAI acquisition announced 2026-06-11 (terms undisclosed) and, per an update on Ona''s announcement post, closed 2026-08-10; Ona joined the Codex team. Hosted Ona Cloud winds down 2026-10-31; the status of customer-VPC (Enterprise) deployments under OpenAI is not publicly stated.'
acquisition: {announced: 2026-06-11, closed: 2026-08-10, price: null}
funding_total: null
last_funding: null
market_position: {ephemeral-environments: platform-module}
deployment_model: [saas, in-tenant]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: [aws, github, gitlab, devcontainer, openai-codex, claude-code, vscode, jetbrains, cursor]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: Enterprises running background coding agents in their own AWS VPC; now positioned as part of OpenAI Codex
last_verified: 2026-10-26
verify_after: 2026-12-31
tags: [cloud-development-environments, coding-agents, rename, gitpod, openai, codex, hosted-service-shutdown, product-sunset]
sources:
  - {claim: "Gitpod renamed Ona 2025-09-02, 'mission control for software engineering agents'", url: "https://ona.com/stories/gitpod-is-now-ona", date: 2025-09-02, confidence: high}
  - {claim: "Independent coverage of rename; components; multi-tenant cloud (US/EU) or customer AWS VPC; agents request full GitHub read/write", url: "https://www.theregister.com/2025/09/03/gitpod_rebrands_as_ona/", date: 2025-09-03, confidence: high}
  - {claim: "Gitpod Classic PAYG sunset 2025-10-15; Enterprise on custom timelines; self-hosting only on Enterprise", url: "https://ona.com/stories/gitpod-classic-payg-sunset", date: 2025-09-02, confidence: high}
  - {claim: "OpenAI acquisition agreement announced 2026-06-11; closing update 2026-08-10", url: "https://ona.com/stories/ona-joins-openai", date: 2026-08-10, confidence: high}
  - {claim: "OpenAI's own announcement (title only; page returned 403)", url: "https://openai.com/index/openai-to-acquire-ona/", date: 2026-06-11, confidence: medium}
  - {claim: "Anthropic ended Ona-managed model access; BYOK continues for now", url: "https://ona.com/stories/anthropic-model-access-in-ona", date: 2026-08-05, confidence: high}
  - {claim: "Ona Cloud winding down 2026-10-31; signups closed; migrate to Codex Cloud", url: "https://ona.com/stories/ona-core-shutdown", date: 2026-10-13, confidence: high}
  - {claim: "Homepage: 'Part of OpenAI'; runs in your VPC; kernel-level policy enforcement; audit trails", url: "https://ona.com/", date: 2026-10-26, confidence: medium}
---

# Ona (OpenAI)

> **Hosted service ends 2026-10-31.** Ona, formerly Gitpod, is now part of OpenAI: the acquisition was announced 2026-06-11 and closed 2026-08-10. On 2026-10-13 Ona announced it is "winding down Ona Cloud on October 31, 2026". Sign-ups are closed and users are being sent to OpenAI's Codex Cloud. The homepage still sells an enterprise product that "runs in your VPC", but neither Ona nor OpenAI has said publicly what happens to those deployments. **Do not start a new evaluation without a written roadmap from OpenAI.** Verified 2026-10-26.

**One-liner** — A platform for running background coding agents in disposable cloud environments, either in Ona's cloud or in the customer's own AWS VPC. It began as Gitpod, the cloud-dev-environment company, and is now part of OpenAI's Codex organisation.

**What it does** — Ona provides three pieces:

- **Environments:** reproducible, sandboxed dev environments built from `devcontainer.json` plus Ona's automations file.
- **Agents:** they write code, run commands, open branches and pull requests, and respond to review comments. Users can connect from VS Code, Cursor, Windsurf, JetBrains or Zed.
- **Guardrails:** short-lived cloud credentials, a command deny list, audit logs, and **Veto**, an early-access kernel-level enforcement engine. Veto runs as a Linux Security Module and identifies binaries by SHA-256 hash rather than by path.

Ona has said its customers include "the oldest bank in the US" and "one of Asia's largest sovereign wealth funds", without naming them.

**Why a CTO would have used it for isolation** — Ona's pitch fits this category directly. Each agent task gets a fresh, short-lived environment, ideally inside the firm's own VPC, with scoped credentials and an audit trail, so a misbehaving agent cannot reach a developer's laptop or the corporate network. Ona also published useful research on agent containment. It showed Claude Code getting around a path-based command deny list by calling the binary through `/proc/self/root`. That finding is what led to Veto's hash-based identification. The independent point holds whatever happens to the product: **deny lists keyed on paths are not a containment boundary.**

**Naming / provenance** — The company was Gitpod, an open-source cloud IDE and dev-environment platform; its GitHub repo is AGPL-3.0. Product generations, newest last:

- **Gitpod Classic:** multi-tenant SaaS with `.gitpod.yml`. The last tagged open-source release was 2022.11.3, in June 2023.
- **Gitpod Flex / Enterprise:** self-hosted runners in the customer's AWS account. This lineage is reported by third-party comparison sites; Ona's own sunset post names only "Enterprise".
- **Ona:** the agent-first relaunch, announced in a post by CEO Johannes Landgraf dated **2025-09-02**. The Register covered it on 2025-09-03.

**Gitpod Classic** pay-as-you-go was retired on **2025-10-15**. Ona's post says "Pay-as-you-go users will not be able to login or start new environments after October 15th". Classic enterprise customers moved on custom timelines, and `.gitpod.yml` was deprecated. Search results and old comparisons that say "Gitpod" describe products that no longer exist in that form.

**Ownership & viability** — `acquired-closed`. OpenAI's acquisition was **announced 2026-06-11**, with terms not disclosed and closing subject to regulatory approvals. It **closed 2026-08-10**, according to an update Ona added to its announcement post. OpenAI's own announcement page could not be fetched (403), so the closing date rests on the acquired company's statement. Confidence is still high, because the homepage now reads "Part of OpenAI". Ona's team joined the **Codex** group.

The acquisition had immediate effects:

- **2026-08-05:** Anthropic ended Ona's Ona-managed access to Claude models, a decision Ona linked to the deal. Existing automations were moved to OpenAI models. Enterprise customers using their own Anthropic API keys could continue "today", but Ona was "not confident that will remain the case".
- **2026-10-13:** Ona announced that Ona Cloud ends on **2026-10-31**, with migration to **Codex Cloud**. Environments do not transfer automatically.

This reads as an **acquire-and-absorb**: the technology and team are going into Codex, and the standalone hosted product is being shut down. Pre-acquisition funding is **unverified**. One aggregator lists $39.9M, but no primary source was found.

**Positioning & differentiators** — `platform-module`: as of 2026-08-10 it is becoming a component of OpenAI Codex, not an independent product. Retrospective comparison:

- **vs. [coder](coder.md):** both offered self-hosted dev environments with agent controls. Coder runs on any cloud or on-prem and is still independent. Ona's self-hosted option ran on AWS.
- **vs. [github-codespaces](github-codespaces.md):** Ona offered a customer-VPC option, where Codespaces runs only on GitHub's infrastructure. Ona was also more aggressively agent-first.
- **vs. agent sandboxes ([daytona](daytona.md), [modal](modal.md)):** Ona's environments were full dev environments that an agent works in for a long time, not sandboxes created per tool call.

**Who should choose them / anti-fit** — **New buyers: not now.** The hosted product is shutting down, and the future of the in-VPC enterprise product has not been stated publicly. **Existing Ona Enterprise (in-VPC) customers:** get OpenAI to commit in writing to support term, roadmap and model choice. The forced switch from Anthropic to OpenAI models shows that model neutrality is not guaranteed under the new owner. **Anti-fit:** any firm that wants its agent environment to be independent of its model vendor. That is now structurally impossible here.

**Known weaknesses / gotchas** —
- **A hosted service is ending.** Ona Cloud workspaces and data must be exported by 2026-10-31. The shutdown post sets no separate data-deletion date. Ona says it will refund October payments and unused credits.
- **Model lock-in after the acquisition.** Anthropic access was cut off for Ona-managed usage, and the bring-your-own-key route was flagged as at risk.
- **Broad repository permissions.** The Register noted that Ona agents request full read/write access to GitHub repositories and workflows, so prompt-injection risk remains even inside a sandbox.
- **Veto was early access,** and a third-party write-up reports a later bypass through the ELF dynamic linker. Do not treat it as proven.
- **Name confusion:** Gitpod Classic, Flex, Enterprise and Ona are different products from different periods. Older evaluations do not carry over.

**Deployment & data handling** — Two modes, per Ona and The Register:

- **Ona Cloud:** multi-tenant SaaS in US and EU regions. Ends 2026-10-31.
- **Enterprise in the customer's AWS VPC:** "deploy Ona entirely within their own VPC". Whether any control-plane metadata still reaches Ona/OpenAI was not confirmed.

Model calls went to Ona-managed providers, and now OpenAI, unless the customer brought its own keys. Hence `data_leaves_tenancy: unverified`.

**Integrations & partnerships** — `devcontainer.json`; GitHub and GitLab; local IDEs (VS Code, Cursor, Windsurf, JetBrains, Zed); agent harnesses including Codex, Claude Code (BYOK) and OpenCode. The homepage now pitches "one governed way to run Ona, Codex, and other agents". MCP support was not verified.

**Compliance & FS traction** — `fs_traction: claimed`: the customers are described ("the oldest bank in the US", "one of Asia's largest sovereign wealth funds") but not named. Certifications were not verified on this pass.

**Commercial** — The hosted product had Free, Core and Enterprise tiers, and Free and Core are being retired with Ona Cloud. Enterprise is contact-sales, and its pricing under OpenAI is unknown.

## Open questions

- What happens to Ona Enterprise in-VPC deployments under OpenAI: continued as a product, folded into a Codex enterprise offering, or retired? On what timeline? (`verify_after` 2026-12-31.)
- Confirmation of the 2026-08-10 close from OpenAI's side. The OpenAI page returned 403.
- Whether bring-your-own-key access to non-OpenAI models survives in Enterprise.
- Data-deletion timeline for Ona Cloud after 2026-10-31.
- Pre-acquisition funding, founding year and HQ. Gitpod's history was not re-verified on this pass.
- Certifications (SOC 2, etc.) and whether they carry over under OpenAI.

## Sources

- [Gitpod is now Ona (Ona, Johannes Landgraf, 2025-09-02)](https://ona.com/stories/gitpod-is-now-ona). Fetched 2026-10-26 via search summary. Supports: rename and date. Confidence: high.
- [Gitpod reinvents itself as Ona (The Register, 2025-09-03)](https://www.theregister.com/2025/09/03/gitpod_rebrands_as_ona/). Fetched 2026-10-26. Supports: independent coverage of the rename, components, deployment modes, the repository-permissions caveat. Confidence: high.
- [Gitpod Classic PAYG sunset (Ona, 2025-09-02)](https://ona.com/stories/gitpod-classic-payg-sunset). Fetched 2026-10-26. Supports: the 2025-10-15 sunset, Enterprise timelines, self-hosting on Enterprise only. Confidence: high.
- [Ona is joining OpenAI (Ona, 2026-06-11; close update 2026-08-10)](https://ona.com/stories/ona-joins-openai). Fetched 2026-10-26. Supports: announced and closed dates, Codex team, unnamed FS customers. Confidence: high (acquired company's statement).
- [OpenAI to acquire Ona (OpenAI)](https://openai.com/index/openai-to-acquire-ona/). 403 on fetch; title and URL seen in search. Supports: the acquirer's announcement. Confidence: medium.
- [An update on Anthropic model access in Ona (Ona, 2026-08-05)](https://ona.com/stories/anthropic-model-access-in-ona). Fetched 2026-10-26. Supports: Anthropic cutoff, BYOK status. Confidence: high.
- [Ona Cloud is shutting down on October 31, 2026 (Ona, 2026-10-13)](https://ona.com/stories/ona-core-shutdown). Fetched 2026-10-26. Supports: the shutdown and migration to Codex Cloud. Confidence: high.
- [Ona homepage](https://ona.com/). Fetched 2026-10-26. Supports: "Part of OpenAI", in-VPC positioning. Confidence: medium (marketing).
- [Introducing Veto (Ona)](https://ona.com/stories/introducing-veto-security-for-the-next-era-of-software) and [How Claude Code escapes its own denylist and sandbox (Ona)](https://ona.com/blog/how-claude-code-escapes-its-own-denylist-and-sandbox). Via search summary, 2026-10-26. Supports: how Veto works, the deny-list bypass research. Confidence: medium.
- Cached: `raw/sources/2026-10-26--ona--openai-acquisition-and-shutdown.md`

## History

- [2025-09-02] Gitpod renamed Ona; agent-first relaunch. (Event date; recorded 2026-10-26.)
- [2025-10-15] Gitpod Classic pay-as-you-go retired. (Event date; recorded 2026-10-26.)
- [2026-06-11] OpenAI acquisition announced. (Event date; recorded 2026-10-26.)
- [2026-08-10] Acquisition closed, per Ona. (Event date; recorded 2026-10-26.)
- [2026-10-31] Ona Cloud scheduled shutdown. (Announced 2026-10-13.)
- [2026-10-26] Page created via wiki-create + wiki-research. Slug `ona`, the current company name, with Gitpod names in `aka`. Title follows the "X (Acquirer)" convention (lint rule 5).
