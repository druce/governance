URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html (and ACL crawling blog/docs)
Also: https://aws.amazon.com/blogs/machine-learning/enable-or-disable-acl-crawling-safely-in-amazon-q-business/
Fetched: 2026-06-28
Good for: Entitlement-aware retrieval — how Q Business honors source permissions via connectors + identity crawling.

Key extracted text:

- Amazon Q Business supports crawling ACLs for document security by default. It crawls ACL information at the document level from supported data sources.
- As the connector retrieves content, it examines the associated ACL and compiles the list of users/groups with read permissions for each document. It also collects user identifiers, stored in the Amazon Q Business User Store for quick matching during query execution.
- Amazon Q Business crawls and stores principal information (local user alias, local group, federated group identity) into the Amazon Q Business User Store. Useful when connecting multiple data sources with different auth systems into a unified, access-controlled chat experience.
- Identity crawling + the Authorization feature filters chat responses by end-user context: responses are restricted to documents the asking user is permitted to read.
- Connectors with ACL crawling include Box, Confluence (Cloud/Server), WorkDocs, OneDrive, Google Drive, Slack, Exchange, SharePoint, S3, and many more.
- Limitation: once ACL and identity crawling are turned ON, they cannot be turned off (turning them off after enablement is not supported). This is a safety default.

Implication: Q Business is natively entitlement-aware — at query time it filters retrieved enterprise content to the user's existing source-system permissions, rather than indexing everything into a flat store.
