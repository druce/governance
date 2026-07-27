# CyberArk → Palo Alto Networks close (SEC-verified) + the Idira rebrand

- **URLs:**
  - https://www.sec.gov/Archives/edgar/data/1327567/000119312526045600/d40626d8k.htm
    (PANW Form 8-K, event date 2026-02-11, filed 2026-02-11)
  - https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/panw-20260430.htm
    (PANW Form 10-Q, quarter ended 2026-04-30, filed 2026-06-03 — CyberArk purchase accounting)
  - https://www.cyberark.com (live, no redirect — carries the acquisition banner + "CyberArk is now Idira")
  - https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-introduces-idira-next-generation-identity
  - https://www.paloaltonetworks.com/idira
- **Fetched:** 2026-07-27
- **Good for:** the **legally exact** close date and the **actual** purchase consideration
  (which differs materially from the announced headline number), plus primary confirmation
  that "Idira" is PANW's own name for the acquired CyberArk portfolio.

---

## 1. Close date — PANW Form 8-K (primary, definitive)

Event date and filing date both **February 11, 2026**. Item 8.01, quoted verbatim:

> "On the Closing Date, PANW completed the acquisition of CyberArk pursuant to the Agreement
> and Plan of Merger, dated as of July 30, 2025 (the 'Merger Agreement'), by and among PANW,
> Athens Strategies Ltd., a company organized under the laws of the State of Israel and a
> wholly owned subsidiary of PANW ('Merger Sub'), and CyberArk. On the Closing Date, pursuant
> to the Merger Agreement, and upon the terms therein, Merger Sub merged with and into
> CyberArk (the 'Merger'), with CyberArk continuing as the surviving corporation in the Merger
> and a wholly owned subsidiary of PANW."

Item 1.01 defines the term explicitly: *"on February 11, 2026 (the 'Closing Date')"*.

So **announced 2025-07-30 (merger agreement date), closed 2026-02-11** — the blog/press
"completion" date and the legal close date agree here. Reverse-triangle merger via Israeli
Merger Sub "Athens Strategies Ltd."; CyberArk Software Ltd. survives as a wholly owned PANW
subsidiary (it was **not** dissolved — the legal entity persists).

**Corroborating CyberArk (CIK 0001598110) filings, all consistent:**

| Form | Filed | Meaning |
|---|---|---|
| 6-K | 2026-02-11 | completion report |
| 25-NSE | 2026-02-11 | Nasdaq delisting notification (CYBR ceases trading) |
| POSASR + 15× S-8 POS | 2026-02-11 | deregistration of unsold securities / employee plans |
| 15-12G | 2026-02-23 | Exchange Act deregistration — reporting obligations terminate |

## 2. Purchase price — PANW Form 10-Q (Q3 FY2026), Note 7 "Acquisitions"

**This is where the headline number and the accounting number diverge.** Quoted:

> "On February 11, 2026, we completed our acquisition of CyberArk, an identity security
> company, forming our next-generation identity security platform. CyberArk shareholders
> received $45.00 in cash and 2.2005 shares of our common stock for each CyberArk share.
> The total purchase consideration for the acquisition of CyberArk was **$21.1 billion**"

Breakdown (US$ millions):

| Component | Amount |
|---|---|
| Cash | 2,308 |
| Common stock (112 million shares) | 18,488 |
| Fair value of replacement awards | 265 |
| **Total** | **21,061** |

**Why $21.1B ≠ the ~$25B announced.** The announced figure (2025-07-30) was an ~$25B *equity
value* struck off PANW's share price at announcement. ~88% of the consideration was PANW
stock (112M shares), and the exchange ratio was fixed at 2.2005, so the value moved with
PANW's share price over the ~6.5 months to close. The $21.1B is the GAAP fair value of
consideration measured **on the closing date**. Both numbers are correct for what they
measure; cite the ~$25B as the *announced* value and $21.1B as the *final* consideration.

Preliminary purchase price allocation (US$ millions): Goodwill 14,802; identified intangibles
6,279; cash and equivalents 743; AR 312; investments 1,217; net assets acquired 61;
convertible senior notes (1,303); deferred revenue (776); deferred tax liabilities (274).

Identified intangibles: developed technology $2,537M (5 yr); **platform renewals $3,500M
(12–14 yr)**; customer contracts $219M (2 yr); trade name **$23M, 1-year useful life**.
The 1-year life assigned to the CyberArk trade name is itself evidence PANW planned to retire
the brand fast — consistent with the May 2026 rebrand three months after close.

Also disclosed: CyberArk transaction costs $41M (Q3) / $56M (9 months); a post-close workforce
optimization plan with total estimated cost **$59M**, expected substantially complete by end
of fiscal 2027 ($12M paid as of 2026-04-30). "Substantially all of goodwill is deductible for
U.S. income tax purposes."

## 3. Idira in PANW's own SEC filing (not just marketing)

The same 10-Q's business description names the platform under a new "Identity Security"
segment heading:

> "**Idira™**, our next-generation identity security platform, is designed to secure human,
> agentic and machine identities across the enterprise with intelligent privilege controls and
> continuous threat prevention. By unifying identity access management, privilege access
> management and identity governance and administration, organizations can continuously
> discover and protect against identity risk throughout the end-to-end identity lifecycle."

Five modules named in the 10-Q: **Workforce Identity Security**; **IT and Developer Identity
Security (Modern Privilege Access Management)** — just-in-time privileged access, session
isolation, credential protection, zero standing privileges; **Machine Identity Security** —
secrets discovery/management, certificate lifecycle automation, workload identity issuance,
PKI-as-a-service, Kubernetes certificate management, code signing; **Identity Governance and
Administration (IGA)**; **AI Agents Security** — discovers AI agents, assigns identity
attributes, restricts access to task-specific resources, records activity, suspends/revokes on
behavioral deviation.

Note the trademark symbol and the SEC-filing usage: Idira is the *registered platform brand*,
not a marketing skin. "CyberArk" does not appear as a product-line name anywhere in the
10-Q's business description — only as the acquired entity in the acquisitions note.

## 4. Rebrand announcement

PANW investor press release **"Palo Alto Networks Introduces Idira: the Next-Generation
Identity Security Platform Built for the AI Enterprise"**, dated **2026-05-12** (this settles
the 2026-05-12 vs 2026-05-13 ambiguity flagged in the conjur source file — 05-12 is the PANW
release date; 05-13 is SDxCentral's story date). Peretz Regev, Chief Product and Technology
Officer, quoted: *"Identity has become the new battleground of the AI enterprise. With
adversaries now logging in rather than breaking in..."* The release frames Idira as combining
"the deep expertise of the industry's original PAM pioneers with the unparalleled scale and
speed of Palo Alto Networks," on three pillars: **discover** identity risk, **control**
privileges via zero standing privilege, **automate** governance.

Existing-customer treatment per the release: current SaaS customers get tiered upgrades —
traditional PAM users get discovery improvements and may add Zero Standing Privilege; modern
PAM users get ZSP and enhancements **at no additional cost**; Workforce Access customers get
UX upgrades with ZSP available; machine/AI identity customers can add traditional PAM.

## 5. cyberark.com status (verified 2026-07-27, curl + fetch)

`https://www.cyberark.com` returns **HTTP 200 — no redirect** (WP Engine / Cloudflare origin,
still a WordPress site). The domain is very much alive but is now a transitional landing page:

- Banner: **"Palo Alto Networks Completes Acquisition of CyberArk to Secure the AI Era"**,
  the linked press release dated **February 11, 2026**.
- Prominent headline: **"CyberArk is now Idira"** — *"The next-generation platform that
  secures every identity for the AI enterprise."* — linking to
  `https://www.paloaltonetworks.com/idira`.

Contrast with `conjur.org`, which 301s outright. cyberark.com has *not* been redirected yet,
which makes it still useful (and still the canonical destination for CyberArk-branded legacy
docs, support, and the community site) — but it is signposting its own replacement. Treat it
as authoritative-but-transitional; expect an eventual redirect to the Idira pages.

The site's CSP header still whitelists `venafi.cloud` / `venafi.eu`, a leftover from
CyberArk's own 2024 Venafi acquisition.

## 6. Idira FAQ — what changes for existing customers

From `paloaltonetworks.com/idira`:

> "CyberArk has long been your trusted partner for securing privilege and defending your
> critical assets. Now, we're introducing Idira, the next-generation identity security
> platform, built on CyberArk's legacy and powered by Palo Alto Networks."

> "If you're an existing CyberArk customer, you can continue to use the platform as you always
> have. You'll just notice a new logo and design."

Three identity categories: **Human** (modern privileged access, endpoint, identity
governance), **Machine** (secrets management, workload security), **Agentic** (AI agent
discovery, control, governance).

**What the FAQ does NOT say** (absence of evidence, worth recording): it does not address
contract/licensing paper changes, whether renewals now paper through PANW entities, support
channel migration, or the fate of `cyberark.com` / `docs.cyberark.com`. Trade coverage
(SDxCentral, 2026-05-13) reports the underlying technical platform and component names are
unchanged and only commercial branding moved.
