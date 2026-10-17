# turbopuffer — Permissions doc (how to do access control)

- URL: https://turbopuffer.com/docs/permissions (markdown: https://turbopuffer.com/docs-md/permissions.md)
- Fetched: 2026-10-16
- Good for: deciding whether turbopuffer belongs in entitlement-aware-rag. Primary source.

## Extracted
- turbopuffer has **no built-in row-/document-level access control**: permissions
  "currently have to be implemented at the user-level with filters."
- Recommended pattern: store `user_id`s / `group_ids` with read access as array
  attributes on each document; at query time the application's auth layer supplies the
  caller's user and group IDs, passed as a filter (e.g. OR over `groups` and `user_ids`),
  combinable with vector or BM25 ranking. Generally faster than filtering on document IDs.
- Arrays up to 8 MiB; inverted index handles tens of thousands of IDs per attribute
  "without major slowdown". Declare UUID type explicitly for cheaper storage.
- Public docs: use an explicit `is_public: true` boolean; an empty permission array
  should mean "no access" (and filtering on empty arrays post-filters, slower).
- The page does **not** cover: syncing ACLs from source systems, handling permission
  changes, or identity-provider integration. Those remain the application's job.
