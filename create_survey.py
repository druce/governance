#!/usr/bin/env python3
"""Create the AI governance vendor survey in SurveyMonkey from survey-v2.csv.

Usage:  python3 create_survey.py [--plain] [--dry-run] [--title "..."]
  --plain    use "Name (url)" instead of HTML <a> links (if your plan strips HTML)
  --dry-run  parse the CSV and print what would be created; no API calls

Needs SURVEYMONKEY_ACCESS_TOKEN (or SM_ACCESS_TOKEN) in .env or the environment.
One page + one checkbox-matrix question per category; products are matrix rows,
the standard usage scale are the columns; "Other (Please Specify), and Additional Comments" becomes the
question's open-ended comment field.
"""
import argparse, csv, os, sys
from collections import OrderedDict

WIKI = "https://github.com/druce/governance/blob/master/wiki/categories/%s.md"
SCALE = ["Interested in a demo", "Considering/Evaluating", "Piloting/Implementing",
         "In production", "Recommended", "Not Recommended"]

# CSV category -> (wiki category slug, one-line description)

CATEGORIES = {
 "AI Gateway": ("ai-gateway", "Single governed exit door for all model/API traffic — routing, logging, cost and policy control."),
 "LLM Observability & Eval": ("llm-observability", "Prompt-level evaluation, tracing, debugging, and monitoring of LLM usage."),
 "AI Runtime Security / AI Firewall": ("ai-runtime-security", "Inline defense of AI apps at runtime: prompt injection, jailbreaks, output leakage."),
 "AI-SPM (AI estate inventory & posture)": ("ai-spm", "Discovery, inventory and posture management of your AI/agent estate."),
 "Agent Security (runtime protection of agents)": ("agent-runtime-security", "Runtime protection of agentic applications as they act."),
 "AI Antiphishing/deepfake/social engineering defense": ("anti-deepfake", "Defense against AI-generated phishing, deepfakes and social engineering."),
 "AI Governance, Model Risk & Compliance": ("ai-governance-platform", "Inventory AI use cases and map them to frameworks (NIST AI RMF, EU AI Act, SR 11-7 model risk)."),
 "Comms Surveillance": ("comms-surveillance", "Market-abuse / conduct monitoring of communications, including AI assistant prompts."),
 "Authorization Engine (Agent / Tool)": ("authorization-engine", "Fine-grained externalized access decisions for agents and tools."),
 "MCP Gateway / Tool Access Control": ("mcp-gateway", "The doorway/allowlist that brokers and governs the tools your agents can reach."),
 "Tool Identity & Integration (Agent Auth)": ("tool-identity-integration", "Managed auth and connectors for agent-to-SaaS access."),
 "Shadow-AI / Insider risk": ("ai-access-governance", "Discover unsanctioned AI use and enforce inline policy on data flowing to AI tools."),
 "Enterprise Browser Security": ("enterprise-browser", "Managed browsers and extensions securing browser-based AI use."),
 "SaaS Security Posture Management (SSPM)": ("sspm", "Harden SaaS configurations and catch default-on AI features."),
 "Non-Human Identity / Agent Identity Governance": ("non-human-identity", "Identity governance for service accounts, workloads and AI agents."),
 "AI Red Teaming / Guardrails": ("ai-red-teaming", "Test AI apps for vulnerabilities and enforce input/output safety controls."),
 "Enterprise AI Assistant": ("enterprise-ai-assistant", "The sanctioned general-purpose chat/RAG assistant staff actually use."),
 "Entitlement-Aware RAG / Retrieval Permissions": ("entitlement-aware-rag", "Enforcing who-sees-what when AI retrieves internal content."),
 "SIEM/SOAR/SecOps": ("siem-soc", "Enterprise logging, detection and security-operations platform."),
 "AI SOC analysts": ("ai-soc-analysts", "Agentic AI analysts that triage and investigate security alerts."),
 "AI-aware Network Security (SSE/SASE)": ("network-security-sase", "SASE/SSE platforms inspecting and controlling traffic to AI services."),
 "General Identity": ("identity-access", "Identity provider / SSO — the human and agent front door."),
 "Identity Governance & Visibility (IGA / ISPM)": ("identity-governance", "Joiner/mover/leaver, access certification and identity visibility."),
 "Secrets Manager": ("secrets-management", "Vaulting and rotation of credentials, keys and secrets."),
 "EDR / XDR": ("edr-xdr", "Endpoint detection and response."),
 "DSPM / Data Security Posture": ("dspm", "Discover and classify sensitive data at rest."),
 "Data Access Governance": ("data-access-governance", "Audit and right-size who can access sensitive data."),
 "Data Loss Prevention (DLP)": ("dlp", "Egress-time controls on data leaving the firm, including via AI prompts."),
 "Software supply chain": ("software-supply-chain", "Code, dependency and pipeline security — including AI-generated code."),
 "Enterprise Governance, Risk & Compliance": ("enterprise-grc", "System of record for risk, controls, policy and audit."),
 "Vendor Risk Rating & Monitoring": ("vendor-risk", "Third-party risk assessment and cyber ratings, extended to AI vendors."),
}

def load_token():
    if os.path.exists(".env"):
        for line in open(".env"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    tok = (os.environ.get("SURVEYMONKEY_ACCESS_TOKEN") or os.environ.get("SM_ACCESS_TOKEN")
           or os.environ.get("SURVEYMONKEY_API_KEY"))
    if not tok:
        sys.exit("No SurveyMonkey token found: set SURVEYMONKEY_ACCESS_TOKEN in .env")
    return tok

def read_csv(path):
    cats = OrderedDict()
    for r in csv.DictReader(open(path)):
        cats.setdefault(r["Category (survey question)"], []).append(r)
    return cats

def page_payload(cat, html):
    slug, desc = CATEGORIES[cat]
    wiki = WIKI % slug
    link = f'<a href="{wiki}" target="_blank">{slug}</a>' if html else wiki
    return {"title": cat, "description": f'{desc} Research wiki: {link}'}

def build_question(rows, html):
    heading = ("Which of the following products are you evaluating or using? "
               "Select all stages that apply per product. Leave blank if category is not applicable to your firm.")
    matrix_rows = []
    for r in rows:
        name, url = r["Product (answer option)"], r["Vendor URL"]
        if name.startswith("Other (Please"):
            continue  # becomes the open-ended "other" field below
        if url:
            text = f'<a href="{url}" target="_blank">{name}</a>' if html else f'{name} ({url})'
        else:
            text = name
        matrix_rows.append({"text": text})
    return {"headings": [{"heading": heading}], "family": "matrix", "subtype": "multi",
            "answers": {"rows": matrix_rows, "choices": [{"text": c} for c in SCALE],
                        "other": [{"text": "Other (Please Specify), and Additional Comments", "num_chars": 300, "num_lines": 2}]}}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plain", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--csv", default="survey-v2.csv")
    ap.add_argument("--title", default="AI Governance & Security Stack — CTO Usage Survey")
    args = ap.parse_args()
    cats = read_csv(args.csv)
    unknown = [c for c in cats if c not in CATEGORIES]
    if unknown:
        sys.exit(f"Categories missing from CATEGORIES map: {unknown}")
    if args.dry_run:
        for cat, rows in cats.items():
            q = build_question(rows, not args.plain)
            print(f"{cat}: {len(q['answers']['rows'])} rows")
            print("  page desc:", page_payload(cat, not args.plain)["description"][:140])
        print(f"\n{len(cats)} pages/questions would be created.")
        return
    import requests
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {load_token()}", "Content-Type": "application/json"})
    BASE = "https://api.surveymonkey.com/v3"
    def post(url, payload):
        r = s.post(url, json=payload)
        if r.status_code >= 400:
            raise RuntimeError(f"API error {r.status_code} at {url}:\n{r.text}")
        return r.json()
    try:
        survey = post(f"{BASE}/surveys", {"title": args.title})
    except RuntimeError as e:
        sys.exit(str(e))
    sid = survey["id"]
    print(f"Created survey {sid}: {args.title}")
    try:
        for i, (cat, rows) in enumerate(cats.items(), 1):
            page = post(f"{BASE}/surveys/{sid}/pages", page_payload(cat, not args.plain))
            post(f"{BASE}/surveys/{sid}/pages/{page['id']}/questions",
                 build_question(rows, not args.plain))
            print(f"  [{i}/{len(cats)}] {cat} ({len(rows)-1} products)")
    except RuntimeError as e:
        s.delete(f"{BASE}/surveys/{sid}")
        sys.exit(f"{e}\nDeleted partial survey {sid} — fix the error and rerun.")
    # the API auto-creates an empty first page on new surveys — remove it
    first = s.get(f"{BASE}/surveys/{sid}/pages").json()["data"][0]
    if first.get("question_count", 0) == 0:
        s.delete(f"{BASE}/surveys/{sid}/pages/{first['id']}")
    details = s.get(f"{BASE}/surveys/{sid}").json()
    for k in ("edit_url", "preview", "analyze_url", "summary_url", "href"):
        if details.get(k):
            print(f"{k}: {details[k]}")

if __name__ == "__main__":
    main()
