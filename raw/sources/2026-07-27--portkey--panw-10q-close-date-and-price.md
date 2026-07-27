# Palo Alto Networks 10-Q (Q3 FY2026) — Portkey, Inc. acquisition: signing, price, and close

- **URL:** https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm
- **Filing:** Palo Alto Networks Inc. (NASDAQ: PANW), CIK 0001327567, Form 10-Q for the
  quarterly period ended 2026-04-30, filed **2026-06-03**, accession 0001327567-26-000015
- **Fetched:** 2026-07-27
- **Good for:** the authoritative primary-source record of the PANW–Portkey deal — the
  definitive-agreement date, the **purchase price ($140M), which PANW's own press releases
  never disclosed**, and an explicit statement that the deal **closed 2026-05-29**.
  Supersedes press-release and trade-press wording.

## Verbatim quotes

**Note 6, Business Combinations → Portkey, Inc.** (signing + price):

> Portkey, Inc.
>
> On April 30, 2026, we entered into a definitive agreement to acquire Portkey, Inc., a
> privately-held AI Gateway company ("Portkey"), in exchange for total consideration of
> $140 million in cash and replacement awards, subject to adjustments. We expect the
> acquisition will enhance the capabilities of Prisma AIRS. Refer to Note 17. Subsequent
> Events for additional information.

**Note 17, Subsequent Events → Portkey, Inc.** (close):

> Portkey, Inc.
>
> On May 29, 2026, we completed the acquisition of Portkey. This acquisition will be
> accounted for as a business combination in the fourth quarter of fiscal 2026.

**MD&A** (close, restated, with strategic rationale):

> On February 11, 2026, we completed the acquisition of CyberArk, forming our
> next-generation identity security platform. Additionally, on April 14, 2026, we completed
> the acquisition of Koi, to add agentic endpoint security capabilities to our security
> operations platform and enhance Prisma AIRS. **On May 29, 2026, we completed the
> acquisition of Portkey, Inc., a privately-held AI Gateway company, to enhance our
> Prisma AIRS capabilities.**

## Corroborating XBRL context

The filing tags the Portkey signing disclosure as `panw:PortkeyInc.Member` with context
period `2026-04-30 2026-04-30` — machine-readable confirmation of the definitive-agreement
date. The close is disclosed under Note 17 Subsequent Events (i.e. after the 2026-04-30
balance-sheet date but before the 2026-06-03 filing date), stated as an **actual**
completion, not a `srt:ScenarioForecastMember` forecast.

## Key facts established

| Fact | Value |
|---|---|
| Legal target entity | Portkey, Inc. |
| Definitive agreement signed / publicly announced | 2026-04-30 (same day) |
| Total consideration | **$140 million in cash and replacement awards, subject to adjustments** |
| Expected close (per announcement PR) | PANW fiscal Q4 2026 |
| Actually closed | **2026-05-29 — CONFIRMED** (PANW 10-Q Note 17 + MD&A; PANW completion press release) |
| Accounting | Business combination recorded in PANW fiscal Q4 2026 (quarter ended 2026-07-31) |

## Close==announced bug check (negative — no bug present)

The wiki page already carried `announced: 2026-04-30, closed: 2026-05-29`. Both dates are
independently confirmed and **distinct**, so the copy-paste failure mode found on
`natoma.md` (a `closed` date duplicated from `announced`) is **not** present here. The
2026-06-28 research pass on this page was correct on dates; it was only missing the price,
which no press release disclosed and which only the SEC filing supplies.

## Other sources consulted

- PANW press release, "Palo Alto Networks **Completes** Acquisition of Portkey to Secure AI
  Agents" — https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents
  — dateline "SANTA CLARA, Calif., May 29, 2026 ... today announced it has closed the
  acquisition of Portkey." Terms **not** disclosed. Describes Portkey as the foundational
  **AI Gateway** of Prisma AIRS, feeding three capabilities: AI Runtime Security (inspecting
  AI traffic for agent-based threats), Agent Identity Security via **Idira** (authenticating
  agentic interactions to prevent unauthorized tool use), and AI Observability via
  **Chronosphere** (production-scale telemetry).
- PANW press release, "Palo Alto Networks **to Acquire** Portkey to Secure the Rise of AI
  Agents" — https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents
  — dateline April 30, 2026. No price. "Subject to customary closing conditions, the
  transaction is expected to close in Palo Alto Networks fourth quarter in fiscal 2026."
- PANW blog, "Securing and Governing AI Agents At Scale Through A Unified AI Gateway" —
  https://www.paloaltonetworks.com/blog/2026/05/securing-and-governing-ai-agents-at-scale-through-a-unified-ai-gateway/
- portkey.ai — live, HTTP 200, no redirect (audited 2026-07-27). Site carries a banner
  "Palo Alto Networks has completed the acquisition of Portkey" linking to the PANW
  completion release. Domain and product site still operating under the Portkey brand.

## Deal context (same PANW fiscal year)

Portkey is a small tuck-in relative to PANW's other FY2026 deals and must not be conflated
with them: **CyberArk** closed 2026-02-11 ($21.1B final GAAP consideration), **Chronosphere**
closed earlier in FY2026, and **Koi Security** closed 2026-04-14 ($231M). Portkey at $140M
is the smallest of the four and the only one whose price appears solely in the 10-Q.
