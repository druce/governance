URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-protection.html
Fetched: 2026-06-28
Good for: Amazon Q Business data-protection posture — shared-responsibility model, TLS/encryption, CloudTrail logging, GDPR, FIPS endpoints.

Key extracted text:

The AWS shared responsibility model applies to data protection in Amazon Q Business. AWS protects the global infrastructure; the customer maintains control over their content and the security configuration of the AWS services they use. See Data Privacy FAQ. For data protection in Europe, see the GDPR Center.

Recommendations:
- Protect AWS account credentials; set up individual users with AWS IAM Identity Center or IAM (least privilege).
- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. TLS 1.2 required; TLS 1.3 recommended.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions and default security controls.
- Use Amazon Macie for discovering/securing sensitive data in S3.
- Use FIPS endpoints if FIPS 140-3 validated cryptographic modules are required.

Warning: never put confidential/sensitive info into tags or free-form name fields (may be used for billing/diagnostic logs).

Sub-topics: Data encryption for Amazon Q Business; Data encryption for Q Apps; Key management; Cross-region inference; Amazon Q Business Service improvement.
