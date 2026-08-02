#!/usr/bin/env python3
"""Lightweight repository validator for this Codex skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/opportunity-patterns.md",
    "references/discovery-methods.md",
    "references/example-candidates.md",
    "references/output-templates.md",
    "references/validation-playbook.md",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
]

REQUIRED_SKILL_LINKS = [
    "references/opportunity-patterns.md",
    "references/discovery-methods.md",
    "references/example-candidates.md",
    "references/output-templates.md",
    "references/validation-playbook.md",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter.")

    try:
        _, raw, _ = text.split("---\n", 2)
    except ValueError:
        fail("SKILL.md frontmatter must be delimited by --- lines.")

    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")

    return fields


def validate(root: Path) -> None:
    missing = [path for path in REQUIRED_FILES if not (root / path).is_file()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    fields = parse_frontmatter(skill_text)

    if set(fields) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description.")

    name = fields["name"]
    if name != "skill-idea-miner":
        fail("Skill name must be skill-idea-miner.")

    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        fail("Skill name must use lowercase letters, digits, and hyphens only.")

    description = fields["description"]
    if len(description) < 120:
        fail("Description is too short to trigger reliably.")
    if "Use when" not in description:
        fail('Description must include trigger context with "Use when".')
    if "TODO" in skill_text:
        fail("SKILL.md contains TODO placeholder text.")

    for link in REQUIRED_SKILL_LINKS:
        if link not in skill_text:
            fail(f"SKILL.md does not link {link}.")
        if not (root / link).read_text(encoding="utf-8").strip():
            fail(f"{link} is empty.")

    openai_yaml = (root / "agents/openai.yaml").read_text(encoding="utf-8")
    for required in ["display_name", "short_description", "default_prompt"]:
        if required not in openai_yaml:
            fail(f"agents/openai.yaml missing {required}.")
    if "$skill-idea-miner" not in openai_yaml:
        fail("agents/openai.yaml default_prompt must mention $skill-idea-miner.")

    all_text_files = [
        *root.glob("*.md"),
        *root.glob("references/*.md"),
        root / "agents/openai.yaml",
    ]
    for path in all_text_files:
        text = path.read_text(encoding="utf-8")
        if "[TODO" in text or "TODO:" in text:
            fail(f"{path.relative_to(root)} contains unresolved TODO text.")

    print("[OK] skill-idea-miner repository is valid.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Path to skill repository")
    args = parser.parse_args()
    validate(Path(args.root).resolve())


if __name__ == "__main__":
    try:
        main()
    except UnicodeDecodeError as exc:
        fail(f"Text file is not valid UTF-8: {exc}")
