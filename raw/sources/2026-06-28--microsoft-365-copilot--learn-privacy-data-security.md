# Data, Privacy, and Security for Microsoft 365 Copilot — Microsoft Learn

- URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
- Fetched: 2026-06-28
- Good for: PRIMARY source on no-training commitment, EU Data Boundary / Advanced Data Residency, service boundary, entitlement honoring, encryption/sensitivity labels, certifications, Entra authorization. Page ms.date 2026-06-02.

## Key extracted text (trimmed)

Microsoft 365 Copilot coordinates: LLMs; content in Microsoft Graph (emails, chats, documents you have permission to access); the M365 apps (Word, PowerPoint, etc.).

- "Microsoft 365 Copilot ... is compliant with our existing privacy, security, and compliance commitments to Microsoft 365 commercial customers, including the General Data Protection Regulation (GDPR) and European Union (EU) Data Boundary."
- "Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot." (stated twice)
- "Microsoft 365 Copilot operates with multiple protections, which include, but aren't limited to, blocking harmful content, detecting protected material, and blocking prompt injections (jailbreak attacks)."
- Anthropic models are now in Microsoft 365 Copilot experiences, "provided under the Microsoft Product Terms and Data Protection Addendum." NOTE: "Anthropic models are out of scope for the EU Data Boundary and when available, in-country LLM processing commitments." Anthropic is a subprocessor.

Permissions / entitlement:
- "Microsoft 365 Copilot only surfaces organizational data to which individual users have at least view permissions. It's important that you're using the permission models available in Microsoft 365 services, such as SharePoint, to help ensure the right users or groups have the right access to the right content..." (the oversharing caveat)
- "Semantic Index honors the user identity-based access boundary so that the grounding process only accesses content that the current user is authorized to access."
- "When you have data that's encrypted by Microsoft Purview Information Protection, Microsoft 365 Copilot honors the usage rights granted to the user." Applied via sensitivity labels or IRM.

Service boundary / processing:
- "When you enter prompts using Microsoft 365 Copilot, the information contained within your prompts, the data they retrieve, and the generated responses remain within the Microsoft 365 service boundary, in keeping with our current privacy, security, and compliance commitments. Microsoft 365 Copilot uses Azure OpenAI services for processing, not OpenAI's publicly available services. Azure OpenAI doesn't cache customer content..."
- "Microsoft 365 Copilot services have opted out of [abuse monitoring / human review]."
- Stored interaction data (prompt + response + citations = "Copilot activity history") is "encrypted while it's stored and isn't used to train foundation LLMs." Admins manage via Content search or Microsoft Purview; can set retention policies.

EU Data Boundary & residency:
- "For European Union (EU) users, we have additional safeguards to comply with the EU Data Boundary. EU traffic stays within the EU Data Boundary while worldwide traffic can be sent to the EU and other countries or regions for LLM processing."
- "Microsoft 365 Copilot was added as a covered workload in the data residency commitments in Microsoft Product Terms on March 1, 2024."
- "Microsoft Advanced Data Residency (ADR) and Multi-Geo Capabilities offerings include data residency commitments for Microsoft 365 Copilot customers as of March 1, 2024. For EU customers, Microsoft 365 Copilot is an EU Data Boundary service. Customers outside the EU may have their queries processed in the US, EU, or other regions."

Isolation / auth:
- "Logical isolation of customer content within each tenant for Microsoft 365 services is achieved through Microsoft Entra authorization and role-based access control."
- Encryption at rest/in transit: BitLocker, per-file encryption, TLS, IPsec. Compliance with GDPR, ISO/IEC 27018.

Regulatory compliance:
- "Microsoft 365 Copilot provides broad compliance offerings and certifications, including GDPR, ISO 27001, HIPAA, and the ISO 42001 standard for AI management systems."
- EU AI Act commitment noted. Risk Assessment Quickstart on Service Trust Portal.

Copyright Commitment (IP indemnity) applies to Copilot output when customer uses built-in guardrails/content filters.
