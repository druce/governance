URL: https://docs.glean.com/administration/identity/roles/faq
Fetched: 2026-06-28
Good for: Primary product docs on how Glean reads identity/groups and defers ACL enforcement to source systems.

Key extracted text:
- RBAC hierarchy: Super Admin > Admin > Setup Admin > Member; "the highest-precedence role wins."
- Effective permissions merged from user's direct assignments + group memberships.
- Source-of-truth ACLs: "Glean only **reads** groups and members from your identity provider.
  It does not sync or enforce IdP permission rules, and it never overrides your connector ACLs."
- "All document- and app-level permissions continue to be enforced by the original source systems."
- Group syncing currently for Azure AD and Google Groups; Okta group-based role assignment "Not yet."
- Page does NOT cover deployment types (SaaS/VPC/self-hosted) or data residency.
