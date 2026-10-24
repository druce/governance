# Survey write-in triage — 2026-10-23

Input: `survey-write-in-vendors.csv` (103 vendors deduplicated from the `*` write-ins in `surveyfinal.pdf`, 2026-10-08, N=123). Rule: a page is added when the write-in is in a security/governance question, the vendor is identifiable, and either 2+ firms run it in production or it is specific to alternative-investment buyers / a major platform gap. Single mentions are named on the category page. Business-app questions (Q6–Q27) have no wiki category and are out of scope. Machine-readable: `triage.csv`.

## added (13)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| ACA Group | 1 | 1 | Q38 | aca-group (comms-surveillance; +enterprise-grc) |
| Bitwarden | 5 | 5 | Q49 | bitwarden (secrets-management) |
| Check Point | 1 | 1 | Q52 | check-point (network-security-sase; +dlp, ai-runtime-security). Parent of lakera |
| Dashlane | 2 | 2 | Q49 | dashlane (secrets-management) |
| Drawbridge | 3 | 3 | Q55 | drawbridge (vendor-risk; +enterprise-grc). Vendor DD is advisor-delivered |
| Egnyte | 5 | 4 | Q17; Q50; Q51; Q54 | egnyte (data-access-governance; +dspm, content-sources). GRC placement = respondent misplacement |
| Geordie AI | 2 | 2 | Q33; Q34 | geordie-ai (agent-runtime-security; +ai-spm). LLM-observability placement = misplacement |
| LastPass | 5 | 5 | Q49 | lastpass (secrets-management) |
| Lepide | 2 | 2 | Q50; Q51 | lepide (data-access-governance; +dspm) |
| ManageEngine (Zoho) | 2 | 2 | Q46 | manageengine (siem-soc) |
| ReliaQuest | 2 | 2 | Q47 | reliaquest (ai-soc-analysts; +siem-soc). Managed outcome, not pure software |
| Sophos (Secureworks Taegis) | 2 | 2 | Q46 | sophos (edr-xdr; +siem-soc, network-security-sase, ai-access-governance). Secureworks closed 2025-02-03 |
| VISO Trust | 2 | 2 | Q54; Q55 | viso-trust (vendor-risk; +enterprise-grc). Acquired by Protecht 2026-04 |

## cross-listed (11)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| BeyondTrust | 1 | 1 | Q48 | beyondtrust +identity-governance (ISPM side only) |
| Cisco (Duo) | 1 | 1 | Q29 | cisco +identity-access (Duo) |
| Datadog | 2 | 1 | Q46; Q47 | datadog +siem-soc (Cloud SIEM), +ai-soc-analysts (Bits AI Security Analyst) |
| Dope Security | 1 | 0 | Q31 | dope-security +ai-access-governance |
| Island | 1 | 1 | Q31 | island +ai-access-governance (AI Protect) |
| LiteLLM | 1 | 1 | Q39 | litellm +mcp-gateway |
| Portkey (Palo Alto Networks) | 2 | 1 | Q23; Q39 | portkey +mcp-gateway; now branded Prisma AIRS AI Gateway |
| Quilr | 1 |  | Q23 | quilr +mcp-gateway |
| SentinelOne | 2 | 2 | Q30; Q41 | prompt-security +browser-security-extension. SSE/SASE placement = misplacement |
| Strata (ambiguous) | 2 | 2 | Q31; Q32 | most likely PANW AI Access Security -> palo-alto-networks +ai-access-governance; Strata Identity (Rubrik) alternative noted in taxonomy-gaps |
| Zscaler | 2 | 2 | Q44; Q52 | zscaler +dlp, ai-red-teaming, ai-runtime-security |

## no change (6)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| Audition AI | 2 |  | Q14 | audition-ai exists (enterprise-ai-assistant); Q14 foundation-model placement is loose |
| Chainguard | 1 | 1 | Q53 | chainguard already software-supply-chain |
| Docker | 1 |  | Q22 | docker-sandboxes already ephemeral-environments |
| Glean | 1 |  | Q6 | glean exists (entitlement-aware-rag) |
| OpenRouter | 1 |  | Q15 | openrouter exists (ai-gateway); written under model hosting |
| Reco | 1 | 0 | Q42 | reco already sspm |

## named (15)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| Adlumin (N-able) | 1 | 1 | Q46 | MDR; siem-soc page + MDR gap |
| Blackpoint | 2 | 2 | Q46 | MDR; siem-soc page + MDR gap in taxonomy-gaps |
| BlueVoyant | 1 | 1 | Q55 | vendor-risk page (Supply Chain Defense) |
| Click Studios (Passwordstate) | 1 | 1 | Q49 | secrets-management page |
| Fortra (Digital Guardian) | 1 | 1 | Q52 | dlp page |
| Inedo | 1 | 1 | Q53 | software-supply-chain page (ProGet) |
| LogPoint | 1 | 1 | Q46 | siem-soc page (rebranded guardsix 2026-03-12) |
| Mitratech | 1 | 1 | Q55 | vendor-risk page (Prevalent, acquired 2024-10-02) |
| Proofpoint | 1 | 1 | Q52 | dlp page; wiki page proofpoint-dspm is product-slugged (Normalyze DSPM), Proofpoint DLP named on dlp page rather than cross-listing a DSPM page |
| Proton | 1 | 1 | Q49 | secrets-management page (Proton Pass) |
| Red Canary (Zscaler) | 1 | 1 | Q46 | MDR; covered on zscaler page (closed 2025-08-01); MDR gap in taxonomy-gaps |
| Safe Security | 1 | 0 | Q55 | vendor-risk page (SAFE TPRM) |
| Sevii | 1 | 1 | Q47 | ai-soc-analysts page |
| Soteria | 1 | 0 | Q46 | MDR (Charleston SC); siem-soc page + MDR gap |
| eSentire | 1 | 1 | Q47 | MDR; siem-soc page + MDR gap |

## covered elsewhere (2)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| Qdrant | 1 |  | Q23 | vector-database-landscape comparison (no-stub stance 2026-08-24) |
| Zep | 1 |  | Q23 | agent-memory-landscape comparison |

## not added (3)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| Coder | 1 |  | Q22 | agent/dev sandbox; ephemeral-environments is practice-tier, no shortlist |
| FalkorDB | 1 |  | Q23 | graph DB used for agent memory; adjacent infra, no category |
| Union.ai (Flyte) | 2 |  | Q17; Q22 | orchestrator; out of scope |

## unidentified (5)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| ASKB | 1 |  | Q9 |  |
| Clarier | 1 | 1 | Q35 | AI-SPM write-in; not found |
| Elteni | 1 | 1 | Q55 | TPRM write-in; not found |
| Firegate | 1 | 1 | Q32 | LLM-gateway write-in; possibly FortiGate or Fireraven FireGuard |
| MIK | 1 |  | Q26 |  |

## out of scope (48)

| Vendor | Mentions | In prod | Questions | Detail |
|---|---|---|---|---|
| Accelex | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| Airbyte | 1 |  | Q17 | business-app question (no wiki category); security/governance-only scope |
| AlphaSense | 2 |  | Q6 | business-app question (no wiki category); security/governance-only scope |
| AlphaSights | 1 |  | Q6 | business-app question (no wiki category); security/governance-only scope |
| Anduin | 1 |  | Q10 | business-app question (no wiki category); security/governance-only scope |
| Blue J | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| CENTRL | 2 |  | Q10 | business-app question (no wiki category); security/governance-only scope |
| Canoe Intelligence | 1 |  | Q10 | business-app question (no wiki category); security/governance-only scope |
| Carta | 3 |  | Q10; Q26 | business-app question (no wiki category); security/governance-only scope |
| Checkbox | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| Claren | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| Clarity AI | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| Dagster Labs | 2 |  | Q17 | business-app question (no wiki category); security/governance-only scope |
| Dakota | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| Daloopa | 3 |  | Q7; Q11 | business-app question (no wiki category); security/governance-only scope |
| DuckDB Labs (DuckLake) | 1 |  | Q16 | business-app question (no wiki category); security/governance-only scope |
| Entrilia | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| FIS | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| Fivetran | 1 |  | Q17 | business-app question (no wiki category); security/governance-only scope |
| Harmonic (harmonic.ai) | 1 |  | Q13 | business-app question (no wiki category); security/governance-only scope |
| Hebbia | 2 |  | Q11; Q21 | business-app question (no wiki category); security/governance-only scope |
| LSEG (Refinitiv) | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| LawVu | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| Lightkeeper | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| Litera | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| Loopio | 1 |  | Q10 | business-app question (no wiki category); security/governance-only scope |
| Mastra | 1 |  | Q21 | business-app question (no wiki category); security/governance-only scope |
| MetaView | 1 |  | Q25 | business-app question (no wiki category); security/governance-only scope |
| Moody's | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| Nasdaq Data Link (Quandl) | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| Notion | 1 |  | Q25 | business-app question (no wiki category); security/governance-only scope |
| Ontra | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |
| OpenCode | 1 |  | Q20 | business-app question (no wiki category); security/governance-only scope |
| PitchBook (Morningstar) | 1 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| Quill | 1 |  | Q25 | business-app question (no wiki category); security/governance-only scope |
| Responsive | 1 |  | Q10 | business-app question (no wiki category); security/governance-only scope |
| Rogo | 1 |  | Q11 | business-app question (no wiki category); security/governance-only scope |
| S&P Global (Capital IQ) | 2 |  | Q19 | business-app question (no wiki category); security/governance-only scope |
| SS&C Advent (Geneva) | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| Salesforce | 1 |  | Q13 | business-app question (no wiki category); security/governance-only scope |
| Superblocks | 1 |  | Q20 | business-app question (no wiki category); security/governance-only scope |
| TS Imagine | 1 |  | Q26 | business-app question (no wiki category); security/governance-only scope |
| Understory | 1 |  | Q11 | business-app question (no wiki category); security/governance-only scope |
| Vantager (MSCI) | 2 |  | Q6; Q13 | business-app question (no wiki category); security/governance-only scope |
| Wealthbox | 1 |  | Q25 | business-app question (no wiki category); security/governance-only scope |
| Workato | 1 |  | Q17 | business-app question (no wiki category); security/governance-only scope |
| dbt Labs | 1 |  | Q17 | business-app question (no wiki category); security/governance-only scope |
| iManage | 1 |  | Q27 | business-app question (no wiki category); security/governance-only scope |

