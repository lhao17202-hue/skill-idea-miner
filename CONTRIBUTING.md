# Contributing

Contributions should make the skill more useful without turning it into a generic brainstorming guide.

## Good Contributions

- Add realistic pain-point patterns from repeated Codex usage
- Improve trigger wording in `SKILL.md`
- Add concise examples that help distinguish strong and weak skill candidates
- Improve validation checks
- Tighten output templates

## Avoid

- Broad productivity advice
- Long essays that Codex does not need at runtime
- Duplicate candidate examples with only superficial differences
- Resources that are not linked from `SKILL.md`
- Instructions that depend on private user context

## Development Workflow

1. Edit `SKILL.md` or the relevant file in `references/`.
2. Run:

```bash
python scripts/validate_skill.py .
```

3. Check that new material supports progressive disclosure:

- core behavior belongs in `SKILL.md`
- detailed examples belong in `references/`
- deterministic checks belong in `scripts/`

4. Use clear commit messages, for example:

```text
feat: add validation playbook examples
fix: tighten weak candidate filter
docs: clarify installation path
```

## Review Checklist

- The skill name remains `skill-idea-miner`
- `SKILL.md` frontmatter has only `name` and `description`
- Description includes both capability and trigger context
- New references are linked from `SKILL.md`
- No unresolved TODO placeholders remain
- `python scripts/validate_skill.py .` passes
