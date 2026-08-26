# Vendict — funding, and GenAI security-questionnaire automation (both directions)

- URL: https://vendict.com/blog/series-a-announcement
- URL: https://venturebeat.com/security/vendict-emerges-with-9-5m-in-funding-to-automate-security-compliance-with-generative-ai
- URL: https://vendict.com/security-questionnaire-automation
- Fetched: 2026-08-26
- Good for: the rare vendor addressing the ANSWERING side of security
  questionnaires — directly relevant to managers facing allocator ODD.

## Funding
- **$10M Series A** led by **Moneta VC** and **JAL Ventures**, with **NFX**,
  **Cardumen Capital**, **Disruptive AI** and **Cyber Club London**. Announced
  **August 2025**.
- Prior **$9.5M** at stealth exit. **~$20M total.**
- Founded 2022, Tel Aviv.
- Note: **Moneta VC also backs Panorays** — adjacent rather than directly competing,
  but worth knowing.

## Product mechanism
- Ingests the organisation's **existing compliance corpus** — policies, SOC 2
  reports, ISO certificates, prior questionnaire responses.
- Generative-AI stack **drafts answers to each question** in the counterparty's
  required format. Claim: assessments from **weeks to hours**, improving with use.
- Also covers the reverse direction (assessing own vendors), trust centres and audit
  workflow. Listed on **AWS Marketplace**.

## Why it matters for this wiki's audience
An alternative manager **answers** exhaustive operational due-diligence
questionnaires from allocators, consultants and fund administrators — a recurring
load on a small ops/compliance team — as well as **issuing** them to its own
vendors. Most of `vendor-risk` addresses only the issuing side. Whistic is the
closest comparison.

## The unresolved governance question
An LLM drafting answers that go to **allocators and regulators must not fabricate**.
Everything depends on grounding in the source corpus, flagging gaps rather than
filling them, and the mandatory human review step. **Test in a pilot with
deliberately unanswerable questions.** Not established by any source found.

Also unverified: whether the uploaded compliance corpus trains shared models;
retention; residency; and whether Vendict holds its own certifications.

## Confidence
- Funding: high (primary). Mechanism: medium. Safeguards: unverified.
