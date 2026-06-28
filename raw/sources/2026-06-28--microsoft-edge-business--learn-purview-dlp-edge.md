URL: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-dlp (and /purview/dlp-browser-dlp-learn, /intune/solutions/edge-data-security/overview)
Fetched: 2026-06-28
Note: Microsoft Learn docs — technical detail on how Purview DLP and Edge management service work together inside Edge for Business.

## Key extracted text

- Microsoft Edge for Business supports Microsoft Purview Data Loss Prevention (DLP): enforces admin-configured policies for sensitive files and records audit events for non-compliant activities (printing, copying from a website, uploading files to an excluded website, etc.).
- Edge supports Microsoft Information Protection (MIP) sensitivity labels as conditions in Purview DLP policies; when users open labeled documents in Office Online (Word, Excel, PowerPoint), Edge enforces label-based restrictions directly in the browser.
- "Sensitive service domains" used with device DLP policies help safeguard against data exfiltration.
- After saving the first Purview collection or DLP policy targeting unmanaged apps in Edge for Business, the Microsoft Edge management service automatically creates the required Edge configuration policies, Microsoft Intune policies, and security groups to activate the policy and prevent circumvention; these stay in sync and update automatically with the Purview policies.
- Defender SmartScreen: analyzes visited webpages for suspicious behavior and checks against a dynamic list of reported phishing/malicious sites.
- Native support for Microsoft Entra Conditional Access for role-based access and governance.
