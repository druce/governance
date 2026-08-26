# Pensar — AI security engineer, and agent-specific code vulnerability scanning

- URL: https://www.crunchbase.com/organization/pensarai
- URL: https://www.pensarai.app/ai-agents
- URL: https://www.pensarai.com/
- Fetched: 2026-08-26
- Good for: the only vendor found addressing agent vulnerability classes at the
  CODE layer rather than at runtime — a genuine gap in this wiki's coverage.

## Company — earliest stage of anything on this wiki
- Founded **2023**, **New York City**.
- **~10 employees** as of April 2026.
- Investors named: **Abstraction Capital, Basis Set Ventures, Everywhere Ventures,
  Factorial Capital, Antler** (5 of 6 listed).
- **Round sizes NOT disclosed** in any source found. Frontmatter uses nulls.

## Product (vendor claims)
- "An **AI security engineer** that proactively detects and fixes security
  vulnerabilities in application source code" — generates the patch, not the finding.
- **Agent-specific scanner**: detects vulnerabilities specific to **AI agent
  applications** — **unsafe tool usage, insecure code execution, memory
  manipulation** — and generates secure patch suggestions including **input
  validation and sandboxing**.

## Why this is interesting despite the company's size
Conventional SAST models injection, deserialisation, authN/authZ — the classical
taxonomy. It does **not** model "this agent passes untrusted retrieved text into a
tool call that can execute code," because that class postdates the rule sets.
Almost everything on this wiki addressing agent risk does so at **runtime**
(`agent-runtime-security`). Pensar attempts it **pre-deployment, at the code layer**.
Complementary to Operant AI / Lasso / Zenity, not competitive.

## Blocking caveat
Source code is uploaded for analysis. **Retention, isolation and training-use terms
are unverified**, and at this company stage must be established in writing before any
proprietary code is submitted. No certifications, no named customers, no analyst
coverage, no benchmarks found.

## Confidence
- Company facts: medium (Crunchbase). Product: low (vendor only, uncorroborated).
