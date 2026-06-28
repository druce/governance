URL: https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot
Fetched: 2026-06-28
Note: Primary MS Learn doc. Defines the Microsoft Graph semantic index that grounds M365 Copilot and confirms permission-trimmed retrieval (honors user identity-based access boundary; surfaces results only if user already has access). Good for the entitlement-aware-RAG mechanics and the oversharing-vs-indexing distinction.

KEY EXTRACTED TEXT (trimmed):

"Microsoft 365 Copilot maps your organization's data into an advanced lexical and semantic index to power search relevance and accuracy. Copilot can access the context and relationships within your data by utilizing Microsoft Graph... Built with a comprehensive approach to security, compliance, and privacy, Copilot ensures that all organizational boundaries within your tenant are respected."

"The semantic index is generated from content in Microsoft Graph... It allows organizations to search through billions of vectors (mathematical representations of features or attributes) and return related results... It's built on Microsoft's comprehensive approach to security, compliance, and privacy, and respects all organizational boundaries within your tenant."

"Access to tenant data in Microsoft Graph is gated by role-based access control."

How semantic indexing works: "Today, a semantic index is created for every subscription at the tenant and user level. It's an organization-wide index generated from text-based SharePoint Online files. However, it only surfaces the results to a user if the user already has access to the content controlled by role-based access control. Additionally, the SharePoint Online site must remain searchable."

Supported content types: User Mailbox (user level), Word/PowerPoint/PDF/web pages/OneNote (user + tenant level), Copilot connector data (tenant level). Files up to 512 MB for PDF/PPTX/DOCX.

Enablement: "Every Microsoft 365 Copilot customer now has a tenant-level index. The indexing process requires no administrative involvement." "Semantic indexing is an improvement to Microsoft 365 Search and can't be disabled." A semantic index is generated for users with a paid Microsoft 365 Copilot license.

Privacy/security: "The permissions model within your Microsoft 365 tenant can help ensure that data won't unintentionally leak between users, groups, and tenants. Microsoft 365 Copilot presents only data that each individual can access using the same underlying controls for data access used in other Microsoft 365 services. When data is indexed, we continue to honor the user identity-based access boundary so that the grounding process only accesses content that the current user is authorized to access."

"Prompts, responses, and data accessed through semantic indexing aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot."

Storage: "Semantic indexing works only with content to which your users already have permission and doesn't affect storage quotas." Tenant-level index stored in an isolated, protected customer tenant container in the SharePoint region; EUDB customers stored in EU/EFTA datacenter. BYOK (Purview Customer Key) supported.

Third-party data: "Using Copilot connectors, organizations can bring organizational data or content from external sources into Microsoft Graph. Once in Microsoft Graph, that content is indexed so that Copilot may access it - while maintaining access controls for content."

Reduce oversharing: "It's important to note that indexing data doesn't change access permissions to content... For example, sharing content with a link that works with everyone in my organization doesn't make the information part of the tenant level index." Recommends: Syntex/SharePoint Advanced Management add-on to right-size access; Purview Information Protection sensitivity labels (included in search trimming); Purview DLP (E5) to retroactively/temporarily limit access to overshared documents.
