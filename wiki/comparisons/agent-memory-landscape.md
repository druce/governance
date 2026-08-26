---
title: Agent memory — SaaS products and framework modules
type: comparison
name: Agent memory — SaaS products and framework modules
slug: agent-memory-landscape
status: drafted
last_updated: 2026-08-24
confidence: medium
sources_count: 12
---

# Agent memory: SaaS products and framework modules

**Agent memory** is the persistence layer that lets an AI agent remember users,
facts, and prior sessions beyond a single context window — extraction ("what is
worth remembering"), consolidation ("update or contradict what we knew"), and
retrieval ("recall the right facts cheaply at inference time"). As of mid-2026 it
has hardened from a library choice into a distinct infrastructure category, with
dedicated SaaS vendors, hyperscaler managed services, and memory modules embedded
in every major agent framework. The wiki has **no category or vendor pages for
this space yet** — this page is a landscape scan filed back from a query
(2026-08-24), and a candidate seed for a new taxonomy category.

## Dedicated memory SaaS (the shortlist)

| Product | Architecture | Deploy | Notes (as of 2026-08) |
|---|---|---|---|
| **Mem0** | Vector-first, scoped layers (session → user → org) | SaaS + OSS | Category leader by mindshare; $24M Series A (2025-10); free tier then $19–$249/mo; integrates LangChain, CrewAI, LlamaIndex |
| **Zep** | Temporal knowledge graph (OSS **Graphiti** engine, 20k+ GitHub stars) | SaaS + OSS engine | Tracks fact validity over time (edges with validity intervals); Flex plan ~$125/mo (2026-07); best for temporal reasoning |
| **Letta** (ex-MemGPT) | Stateful agent runtime; core / recall / archival tiers; agent edits its own memory blocks | SaaS + OSS | UC Berkeley lineage; free self-host, Pro ~$20/mo; more an agent runtime than a bolt-on memory API |
| **Cognee** | Graph-native; ECL (Extract–Cognify–Load) pipeline into a knowledge graph | OSS + hosted | Berlin; $7.5M seed (Pebblebed); best-regarded self-hosted graph memory |
| **Supermemory** | Universal memory API; dynamic knowledge graphs over user data streams | SaaS | SF; ~$3M raised; founder-led momentum, earlier-stage than the four above |
| **Honcho** (Plastic Labs) | "Social memory" — per-user representations, continual learning | SaaS + OSS | Niche: user-modeling / theory-of-mind angle rather than fact recall |
| **Memobase** | Profile-based user memory | OSS + SaaS | Smaller entrant; profile/persona memory for consumer-style apps |

## Open-source & research memory systems (not SaaS)

Frequently name-checked alongside the SaaS shortlist, but these are OSS projects
or research artifacts — no hosted product to buy (as of 2026-08):

| Project | Who/what | Notes (as of 2026-08) |
|---|---|---|
| **Hindsight** | Vectorize.io OSS (with Virginia Tech, The Washington Post) | Retain / Recall / Reflect model over four memory networks (facts, experiences, entity summaries, beliefs); 91.4% LongMemEval; arXiv paper. Most credible of this group; Vectorize sells the surrounding platform |
| **MemPalace** | MIT-licensed OSS, viral 2026-04 (19.5k GitHub stars in week one) | "Memory palace" hierarchical index (wings/rooms/drawers), verbatim storage, fully local, MCP integration; claims 96.6% LongMemEval — independent commentary flags the benchmark method as inflated (retrieves near-whole dataset) |
| **Memora** | Microsoft Research (ICML 2026 paper + OSS code) | "Harmonic" representation decoupling storage from retrieval; up to 98% context-token reduction claimed. Research framework, not a product; a separate small OSS project shares the name (agentic-box/memora) |
| **OpenBrain** | Small local-first OSS | Personal memory over Postgres/pgvector + Ollama, exposed as an MCP server; provider-agnostic, no cloud dependency. Early/hobbyist-scale |

## Hyperscaler managed memory

| Product | Status | Notes |
|---|---|---|
| **AWS Bedrock AgentCore Memory** | GA since 2025-10 | Short-term session + long-term retention; managed or self-managed extraction strategies; episodic memory at GA; works with LangGraph, CrewAI, Strands. The most operationally complete managed offering |
| **Google Vertex AI Memory Bank** | GA (with Sessions) | HIPAA support; $0.25 per 1,000 session/memory events; part of Agent Engine |
| **[cloudflare](../vendors/cloudflare.md) Agent Memory** | Private beta (2026-04) | Edge-native; pricing unpublished |

## Framework/vendor-embedded memory modules

Not products you buy separately, but the module you get "for free" with a stack —
and the main reason many teams never buy a dedicated memory SaaS:

- **LangMem** (LangChain/LangGraph) — hot-path memory tools plus background
  managers that extract, consolidate, and search long-term memory. Default choice
  if you're already on LangGraph.
- **CrewAI memory** — unified memory API with LLM-assisted scope/category/
  importance inference.
- **LlamaIndex memory** — composable short/long-term memory blocks over its
  retrieval stack.
- **OpenAI memory** — user-level memory in ChatGPT and the Assistants/Responses
  stack; closed, tied to the platform.
- **Anthropic Claude memory tool** — file-based memory directory the agent reads/
  writes via the Agent SDK; app-controlled persistence.
- **Redis Agent Memory Server** — low-latency working + long-term memory backend;
  best when Redis is already in the estate.
- **[pinecone](../vendors/pinecone.md)** and other vector DBs — the storage
  substrate many of the above sit on, not a memory manager by themselves.

## How to read the space

- **The common stack is two layers**: a memory manager (Mem0/Zep/Cognee/LangMem)
  for extraction + consolidation, over a storage layer (Pinecone, Redis, pgvector).
- **Vector vs. graph** is the main architectural split: vector-first (Mem0)
  optimizes cheap similarity recall; graph/temporal (Zep, Cognee, Supermemory)
  optimizes entity- and time-aware reasoning ("what did we know, when").
- **Runtime vs. sidecar**: Letta wants to *be* the agent runtime; Mem0/Zep bolt
  onto whatever runtime you have. Different procurement decisions.
- **For a fund CTO**, the governance angle: memory stores are a new repository of
  client/user data outside the document estate — retention, entitlement, and DLP
  controls rarely reach them yet. Day-2 concern; adjacent to
  [entitlement-aware RAG](entitlement-aware-rag-options.md).

## Open questions

- No `agent-memory` category exists in `taxonomy.yaml`; no vendor pages for Mem0,
  Zep, Letta, Cognee, Supermemory. Decide whether this earns a category (likely
  `emerging` tier) or stays a comparison page.
- Benchmark claims (Mem0's 92.5% LoCoMo, 94.4% LongMemEval) are vendor-reported —
  unverified against independent runs.
- Pricing is volatile; all figures dated 2026-07/08 from secondary sources, not
  cached primary pages.

## Sources

Accessed 2026-08-24 via web search (secondary/roundup-heavy; not yet cached to
`raw/sources/` — do that if any claim gets promoted to a vendor page):

- [Mem0 vs Zep vs Letta vs Cloudflare (Developers Digest)](https://www.developersdigest.tech/blog/best-ai-agent-memory-providers-2026)
- [AI agent memory 2026 comparison (ecorpit)](https://ecorpit.com/ai-agent-memory-mem0-zep-letta-cloudflare-comparison-2026/)
- [Best AI agent memory frameworks 2026 (Atlan)](https://atlan.com/know/best-ai-agent-memory-frameworks-2026/)
- [8 frameworks compared (Vectorize)](https://vectorize.io/articles/best-ai-agent-memory-systems)
- [AWS AgentCore vs Azure vs Vertex, Q2 2026 (AgentMarketCap)](https://agentmarketcap.ai/blog/2026/04/09/aws-bedrock-agentcore-vs-azure-ai-agent-service-vs-google-vertex-ai-agents-q2-2026)
- [Cognee $7.5M seed (cognee.ai)](https://www.cognee.ai/blog/cognee-news/cognee-raises-seven-million-five-hundred-thousand-dollars-seed)
- [Survey of AI agent memory frameworks (Graphlit)](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks)
- [State of AI agent memory 2026 (Mem0 — vendor marketing)](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [Introducing Hindsight (Vectorize — vendor)](https://vectorize.io/blog/introducing-hindsight-agent-memory-that-works-like-human-memory) and [VentureBeat coverage](https://venturebeat.com/data/with-91-accuracy-open-source-hindsight-agentic-memory-provides-20-20-vision)
- [MemPalace explained (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/05/mempalace-explained/) and [critical take on its benchmarks (bymar.co)](https://blog.bymar.co/posts/agent-memory-systems-2026/)
- [Memora announcement (Microsoft Research)](https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity/) — [ICML 2026 paper](https://arxiv.org/abs/2602.03315)
- [OpenBrain MCP server listing (mcpmarket)](https://mcpmarket.com/server/openbrain)
