# Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot — Microsoft Learn

- URL: https://learn.microsoft.com/en-us/purview/ai-m365-copilot
- Fetched: 2026-06-28
- Good for: PRIMARY source on Purview governance over Copilot — audit, eDiscovery, retention, DLP, Communication Compliance, Insider Risk, sensitivity labels, DSPM for AI, oversharing risk assessments. Page ms.date 2026-05-01.

## Capabilities supported (table) — all "✓" for M365 Copilot & Copilot Chat
DSPM and DSPM for AI (classic); Auditing; Data classification; Sensitivity labels; Encryption without sensitivity labels; Data loss prevention; Insider Risk Management; Communication compliance; eDiscovery; Data Lifecycle Management; Compliance Manager.

## Key extracted text (trimmed)

DSPM for AI / oversharing:
- "Data risk assessments help you identify and fix issues that could result in oversharing of data." Recommendations: "Protect your data from potential oversharing risks" (default weekly assessment); "Protect sensitive data references in Copilot and agent responses."
- One-click policies: protect with sensitivity labels; detect risky AI usage; detect unethical behavior; protect items with sensitivity labels from Copilot/agent processing; detect sensitive info shared with AI via network.

Auditing:
- "Like other activities, prompts and responses are captured in the unified audit log. Events include how and when users interact with the AI app, ... in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured." Flows into Activity Explorer / DSPM for AI.

Sensitivity labels:
- AI apps "use existing controls to ensure that data stored in your tenant is never returned to the user or used by a large language model (LLM) if the user doesn't have access to that data."
- When sensitivity label applies encryption, "users must have the EXTRACT usage right, as well as VIEW, for the AI apps to return the data."
- Copilot Chat displays the highest-priority (most restrictive) sensitivity label for cited items. Copilot in Word/PowerPoint/Outlook supports sensitivity label inheritance for new content.
- Tip: enable sensitivity labels for SharePoint and OneDrive; otherwise encrypted files Copilot can access are limited to data-in-use from Office apps on Windows.

DLP:
- "Use the Microsoft 365 Copilot and Copilot Chat policy location to restrict the processing of prompts that contain sensitive information types, or processing files and emails that have specific sensitivity labels applied."
- Endpoint DLP can warn/block pasting sensitive info into third-party gen-AI sites (e.g. ChatGPT) in a browser.

Insider Risk Management:
- "Risky AI usage policy template to detect risky usage that includes prompt injection attacks and accessing protected materials." Signals integrate into Microsoft Defender XDR.

Communication Compliance:
- "Microsoft Purview Communication Compliance provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps." Privacy by default (pseudonymized usernames, RBAC).

eDiscovery:
- "Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use search when a user's mailbox is selected as the source..." Query builder: Add condition > Type > Contains any of > Copilot activity. Or eDiscovery search using ItemClass property value `IPM.SkypeTeams.Message.Copilot.*`.

Data Lifecycle / retention:
- "Use retention policies to automatically retain or delete user prompts and responses for AI apps." Select "Microsoft Copilot Experiences." Retention labels can retain files referenced in Copilot (cloud attachments — version at time referenced).

Compliance Manager: regulatory templates / assessments for AI regulations.
