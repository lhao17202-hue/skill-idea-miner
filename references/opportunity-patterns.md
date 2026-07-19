# Skill Opportunity Patterns

Use this reference when brainstorming a broad set of skill ideas or deciding whether a pain point deserves a dedicated skill.

## Strong Patterns

### Repeated Long Prompt

The user repeatedly gives Codex the same setup, preferences, or checklist.

Good skill shape:

- Capture the reusable workflow in `SKILL.md`
- Move long examples or standards to `references/`
- Include trigger phrases from the user's natural wording

### Fragile Multi-Step Workflow

The task has a correct order and mistakes are costly or annoying.

Good skill shape:

- Put the order of operations in the core workflow
- Include stop conditions and validation checks
- Add scripts when mechanical steps are frequently rewritten

### Domain Knowledge Cache

The task depends on context Codex cannot reliably infer, such as company policy, schema rules, brand voice, naming conventions, or local infrastructure.

Good skill shape:

- Keep the core workflow short
- Store detailed domain material in `references/`
- Tell Codex when to load each reference

### Tool Or Platform Ritual

The task involves a tool with repeated setup, authentication assumptions, path conventions, CLI flags, or failure modes.

Good skill shape:

- Include environment checks
- Prefer official CLIs or APIs
- Document common error recovery

### Review Or Quality Gate

The task is easy to "finish" while missing important checks.

Good skill shape:

- Turn the skill into a review checklist
- Require concrete evidence such as tests, screenshots, logs, or diffs
- Lead with findings when the skill is a review skill

### Artifact Generator

The task repeatedly produces the same kind of document, UI, report, issue, release note, or project scaffold.

Good skill shape:

- Use `assets/` for templates or boilerplate
- Include output acceptance criteria
- Keep formatting rules explicit

## Weak Patterns

Avoid making a skill when:

- The task is a one-time request
- The name would be too broad, such as `better-coding`
- The description cannot say when to use it
- The workflow changes every time
- The result is mostly taste without stable constraints
- A short saved prompt would be enough
- The skill would duplicate an existing skill without clearer scope

## Candidate Rubric

Use this lightweight rubric when comparing candidates.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Frequency | Rare | Occasional | Repeated |
| Friction | Minor | Noticeable | High-cost or tedious |
| Specificity | Vague | Some boundaries | Clear trigger context |
| Stability | Changes often | Mostly stable | Stable workflow |
| Resource fit | None | Some examples help | References/scripts/assets help a lot |
| Verification | Hard to check | Partly checkable | Clear pass/fail checks |

## Candidate Template

Use this compact structure when the user wants detail for a single candidate:

```markdown
### skill-name

Pain point:
What repeated friction this skill removes.

Description:
Frontmatter-ready description with capability and trigger context.

Core workflow:
1. What Codex should do first.
2. What Codex should inspect or decide.
3. What Codex should produce.
4. How Codex should validate the result.

Resources:
Whether to include `references/`, `scripts/`, `assets/`, or none.

Example triggers:
- "Natural user request that should invoke this."
- "Another wording that should invoke this."
```
