# Output Templates

Use these templates when the user asks for a specific deliverable.

## Ranked Backlog

```markdown
| rank | skill name | pain point | description | resources | score | priority |
|---:|---|---|---|---|---:|---|
| 1 | skill-name | Repeated friction. | Frontmatter-ready description. | references/ | 11 | build soon |
```

After the table, explain:

- why the top candidate is first
- what to build next
- what not to build yet

## One-Page Skill Spec

```markdown
## skill-name

Pain point:
The repeated problem this removes.

Target user:
Who benefits from the skill.

Description:
Frontmatter-ready description.

Core workflow:
1. First thing Codex should inspect or ask.
2. Main decision or transformation.
3. Expected output.
4. Validation step.

Resources:
- SKILL.md: core workflow and routing
- references/: detailed examples or rubrics
- scripts/: deterministic repeated operations, if any
- assets/: reusable templates or media, if any

Example triggers:
- "Use $skill-name to..."
- "Help me..."

Validation:
- Realistic prompt to test the skill
- Expected shape of a good answer
- Common failure mode to watch for
```

## Frontmatter Draft

```yaml
---
name: skill-name
description: Do the specific task. Use when Codex needs to handle concrete trigger scenario A, scenario B, or scenario C.
---
```

## Weak Candidate Explanation

```markdown
I would not make this a skill yet.

Reason:
The task is too rare / too broad / too unstable / better handled by a short prompt.

Better alternative:
Keep it as a saved prompt, checklist, or section inside another skill.
```

## Build Recommendation

```markdown
Build first: `skill-name`

Why:
It is frequent, specific, and easy to validate. It also benefits from reusable references, so the skill will save context and reduce repeated explanation.

Next step:
Create the skill with `references/` for examples and a compact `SKILL.md` workflow.
```
