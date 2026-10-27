# Auth0 / Okta FGA — RAG authorization docs, product page, naming, pricing FAQ (via search snippets)

- URLs: https://auth0.com/ai/docs/intro/authorization-for-rag ; https://auth0.com/fine-grained-authorization ; https://www.helpnetsecurity.com/2024/03/05/okta-fga/ ; https://www.npmjs.com/package/@auth0/fga ; https://community.auth0.com/t/frequently-asked-questions-on-okta-fine-grained-authorization/129768 (404 on direct fetch 2026-10-26; content from search snippet only)
- Fetched: 2026-10-26
- Good for: the commercial managed service built on OpenFGA and its RAG/agent positioning. Vendor marketing.

## Auth0 "Authorization for RAG" (Auth0 AI docs)
- Auth0 FGA "implements Relationship-Based Access Control (ReBAC) control for your RAG pipelines".
- Flow: backend "first fetches relevant documents from a vector database", then asks Auth0 FGA "Is this user allowed to view these documents?"; "Every document is checked against the user's permissions before it's passed to the LLM." (post-retrieval filtering).
- Samples: Vercel AI SDK, LangChain/LangGraph, LlamaIndex, FastAPI; Auth0 AI SDK (TypeScript, Python). Framework SDKs make it "as easy as plugging in a filter in your retriever tool".

## Auth0 FGA product page (search snippet)
- Auth0 FGA is built on OpenFGA (CNCF); pitches modelling relationships among users, agents and data so an agent reaches only authorized documents/tools; cites mitigating prompt-injection-driven data leakage in RAG pipelines.

## Naming
- Help Net Security 2024-03-05: "Okta FGA" launch coverage; Okta announced FGA Limited Early Access late 2023.
- npm @auth0/fga: titled "Okta Fine Grained Authorization (FGA)", describes "Auth0 Fine Grained Authorization (FGA)", deprecated in favour of the OpenFGA JS SDK; API endpoint api.us1.fga.dev.
- Current Okta/Auth0 marketing (2025–2026) uses "Auth0 FGA". Both names in circulation; no formal rename notice found.

## Pricing FAQ (search snippet, unverified directly)
- Okta FGA billed by monthly active users (a user counted when its ID appears in check / list-objects calls); no public rate card; trial with low rate limits, no self-serve free production plan; 99.99% SLA.
