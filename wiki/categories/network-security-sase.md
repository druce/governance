---
type: category
name: Network Security / SASE (SSE)
slug: network-security-sase
layer: foundation
priority: day-1
trifecta_role: egress
maps_to_seed_doc: Network Security / SASE
maps_to_seed_csv: AI-aware Network Security (SSE/SASE)
vendor_count: 7
status: drafted
last_updated: 2026-06-28
---

# Network Security / SASE (SSE)

## Business objective

Inspect and control traffic in and out of the organization, including deep packet
inspection of *encrypted* traffic by acting as a trusted man-in-the-middle on TLS
connections — the same connections used by ChatGPT Enterprise, Claude, and coding
agents. The seed doc frames it as **the walls and checkpoints around your network,
plus a secure tunnel for remote workers**. SASE (Secure Access Service Edge) and
its security-only subset SSE (Secure Service Edge) bundle the old appliances —
firewall, secure web gateway, CASB, DLP, ZTNA — into a cloud-delivered control
point that sits between your users and the internet, including the AI internet.

## When you need it

**Day 1 — but usually already deployed.** Like EDR, this is existing enterprise
plumbing for most firms; the AI angle is that it's the *first* place you can see
and control which AI services employees and agents reach, and what leaves over
those TLS sessions. "AI-aware" SSE/SASE is the differentiator the seed CSV calls
out: vendors are adding inline visibility and policy on AI-tool traffic (block
unsanctioned models, log prompts, apply DLP to uploads). For a hedge-fund CTO this
is the cheapest existing lever for shadow-AI control before buying a dedicated
[ai-access-governance](ai-access-governance.md) tool — though it's destination-aware, not intent-aware.

## Lethal-trifecta role

Primarily an **egress** control: the TLS-inspecting proxy is where outbound data
to external models and tools can be seen and stopped, breaking the exfiltration
leg of the trifecta at the network boundary. It also touches **untrusted input**
(inbound web/content filtering) and is the enforcement plane for trust-zone
egress rules — e.g. denying a yellow-zone workload any route to the public
internet. Lives at the perimeter of every zone; it's the wall between
**green/yellow (internal)** and the **red zone (open internet)**.

## Vendors

- [palo-alto-networks](../vendors/palo-alto-networks.md) — NGFW + Prisma Access; the incumbent platform play, deep inspection plus its own AI-security stack (Prisma AIRS).
- [zscaler](../vendors/zscaler.md) — cloud-native zero-trust SSE pioneer; also pushing AI-traffic guardrails (AI Guard).
- [netskope](../vendors/netskope.md) — SSE with strong inline CASB/DLP heritage; markets AI-app visibility heavily.
- [cloudflare](../vendors/cloudflare.md) — global edge network; SASE plus developer/AI-gateway adjacencies.
- [cisco](../vendors/cisco.md) — Secure Access; bundled with Cisco's networking and security portfolio.
- [cato-networks](../vendors/cato-networks.md) — single-vendor SASE built cloud-first; converged networking + security.
- [forcepoint](../vendors/forcepoint.md) — SSE with a data-security/DLP focus.

## Consolidation / M&A dynamics

A consolidating, platform-driven market — buyers increasingly want one SASE vendor
rather than stitched point products. [cato-networks](../vendors/cato-networks.md) is reported to have acquired
Aim Security to add AI-runtime capability (per seed; unverified — to confirm in
research). [cisco](../vendors/cisco.md) has been an active acquirer across security (Splunk, and AI
players such as Robust Intelligence) and folds those into its access platform.
[palo-alto-networks](../vendors/palo-alto-networks.md) continues to absorb adjacent AI-security capability into the
Prisma line. The trend: SASE vendors bolting on "AI-aware" inspection to defend the
egress point against AI-driven data loss.

## Adjacent categories

- [ai-access-governance](ai-access-governance.md) — the intent-aware, AI-specific layer that sits on top of (or inside) the SASE proxy for shadow-AI control.
- [dlp](dlp.md) — content/lineage-aware exfiltration controls; SASE often carries an inline DLP engine.
- [ai-runtime-security](ai-runtime-security.md) — AI-specific prompt/response inspection; positioned as an upgrade on top of generic SASE/NGFW.
- [enterprise-browser](enterprise-browser.md) — an alternative enforcement point closer to the user.

## Survey

**Question:** Which AI-aware Network Security / SASE (SSE) platform does your firm
use or evaluate to inspect and control traffic to AI services?

**Answer options (multi-select):**
- Palo Alto (NGFW + Prisma Access)
- Zscaler
- Netskope
- Cloudflare
- Cisco (Secure Access)
- Cato Networks
- Forcepoint
- Other (Please Specify)

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:** Table-stakes infrastructure — almost every respondent
will own one, so the signal is the incumbent and whether its *AI-aware* features
are actually turned on. Watch for overlap confusion with [ai-access-governance](ai-access-governance.md)
and [dlp](dlp.md): respondents may credit their SASE vendor with shadow-AI control they
haven't enabled. Palo Alto, Zscaler, and Netskope are the table-stakes options;
Cato and Forcepoint are more selective.

## Open taxonomy questions

- Heavy overlap with [ai-access-governance](ai-access-governance.md) and [dlp](dlp.md) — SASE vendors are
  absorbing both; respondents may not distinguish the network layer from the
  AI-policy layer riding on it.
- SSE vs SASE distinction (security-only vs security+networking) may matter to some
  respondents and not others; we treat them as one survey category.
