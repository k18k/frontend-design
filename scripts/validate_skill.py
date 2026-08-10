#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
SOURCES = ROOT / "references" / "sources.md"
MIN_SOURCES = 75

errors: list[str] = []

if not SKILL.exists():
    errors.append("SKILL.md is missing")
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md frontmatter is missing")
    for field in ("name:", "description:"):
        if field not in text.split("---", 2)[1]:
            errors.append(f"SKILL.md frontmatter missing {field}")

    refs = sorted(set(re.findall(r"`((?:references|templates)/[^`]+\.md)`", text)))
    for ref in refs:
        if not (ROOT / ref).exists():
            errors.append(f"Referenced file does not exist: {ref}")

if not SOURCES.exists():
    errors.append("references/sources.md is missing")
else:
    source_text = SOURCES.read_text(encoding="utf-8")
    rows = re.findall(r"^- \[S(\d{3})\].*?— (https?://\S+) —", source_text, re.MULTILINE)
    ids = [row[0] for row in rows]
    urls = [row[1] for row in rows]
    unique = set(ids)
    unique_urls = set(urls)
    if len(unique) != len(ids):
        errors.append("Duplicate source IDs detected")
    if len(unique_urls) != len(urls):
        errors.append("Duplicate source URLs detected")
    if len(unique_urls) < MIN_SOURCES:
        errors.append(f"Research corpus has {len(unique_urls)} unique sources; minimum is {MIN_SOURCES}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"OK: skill structure valid; {len(unique_urls)} unique research sources found (minimum {MIN_SOURCES}).")
