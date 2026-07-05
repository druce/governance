"""Shared helpers for wiki maintenance scripts (migrate / lint / gen-taxonomy)."""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)


def parse_page(path):
    """Return (frontmatter dict or None, body text) for a markdown page."""
    text = Path(path).read_text()
    m = FM_RE.match(text)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), text[m.end():]


def dump_page(path, fm, body):
    y = yaml.safe_dump(
        fm, sort_keys=False, allow_unicode=True, default_flow_style=None, width=1000
    )
    Path(path).write_text(f"---\n{y}---\n{body}")


def load_taxonomy():
    return yaml.safe_load((ROOT / "taxonomy.yaml").read_text())


def cat_index(tax):
    return {c["slug"]: c for c in tax["categories"]}


def iter_pages(*subdirs):
    for sd in subdirs:
        base = ROOT / "wiki" / sd
        if base.exists():
            yield from sorted(base.glob("*.md"))
