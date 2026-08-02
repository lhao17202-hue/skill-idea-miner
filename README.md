# Skill Idea Miner

Skill Idea Miner is a Codex skill for finding practical skill opportunities from real workflow pain points.

It helps turn vague thoughts like "I keep asking Codex to do the same thing" into a ranked list of skill candidates with names, trigger-ready descriptions, likely resources, and validation ideas.

## What It Does

- Finds reusable skill ideas from repeated prompts, tool friction, agent mistakes, and personal work habits
- Filters weak ideas that are too broad, too rare, or better handled as a one-off prompt
- Scores candidates by frequency, friction, specificity, stability, resource fit, and verifiability
- Produces frontmatter-ready skill names and descriptions
- Suggests whether a candidate should use `references/`, `scripts/`, `assets/`, or no bundled resources
- Helps prepare a selected idea for implementation with examples and forward-test prompts

## When To Use

Use this skill when you want Codex to:

- brainstorm useful skill ideas
- convert pain points into concrete skill candidates
- prioritize which skill to build first
- audit whether an idea is worth becoming a skill
- draft `name` and `description` fields before creating a skill
- identify reusable resources for a future skill

Example prompt:

```text
Use $skill-idea-miner to identify practical Codex skill ideas from my recurring workflow pain points.
```

## Repository Structure

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- discovery-methods.md
|   |-- example-candidates.md
|   |-- opportunity-patterns.md
|   |-- output-templates.md
|   `-- validation-playbook.md
|-- scripts/
|   `-- validate_skill.py
|-- .github/
|   `-- workflows/
|       `-- validate.yml
|-- CONTRIBUTING.md
|-- LICENSE
`-- README.md
```

## Install

Copy or clone this repository into your Codex skills directory:

```bash
git clone https://github.com/lhao17202-hue/skill-idea-miner.git ~/.codex/skills/skill-idea-miner
```

On Windows PowerShell:

```powershell
git clone https://github.com/lhao17202-hue/skill-idea-miner.git "$env:USERPROFILE\.codex\skills\skill-idea-miner"
```

Restart Codex or reload skills after installation if your environment does not pick up new skills automatically.

## Validate

Run the lightweight repository validator:

```bash
python scripts/validate_skill.py .
```

The validator checks:

- required files
- `SKILL.md` frontmatter
- skill naming rules
- `agents/openai.yaml` basics
- required reference links
- non-empty linked reference files
- absence of unresolved TODO placeholders

## Design Notes

This repository intentionally keeps the core `SKILL.md` short enough for regular use. Larger idea libraries, templates, and evaluation guidance live in `references/` so Codex can load them only when needed.

## License

MIT
