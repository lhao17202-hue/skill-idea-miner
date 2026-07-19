---
name: skill-idea-miner
description: Identify practical Codex skill ideas from real workflow pain points, repeated prompts, recurring agent mistakes, tool friction, domain-specific procedures, or personal work habits. Use when brainstorming new skills, converting vague needs into skill candidates, prioritizing which skills are worth building, or drafting frontmatter-ready names and descriptions before creating a skill.
---

# Skill Idea Miner

## Core Purpose

Help the user discover skill ideas that are genuinely useful, reusable, and specific enough to trigger well. Prefer ideas grounded in repeated friction over clever but speculative concepts.

## Operating Mode

When the user asks for skill ideas, first infer the context they care about:

- Existing repeated prompts or workflows
- Tools, file types, or platforms they use often
- Places where Codex frequently needs correction
- Procedures that require hidden domain knowledge
- Reviews, checklists, or validations that are easy to forget
- Tasks with enough repetition to justify a reusable workflow

Ask at most two clarifying questions only if the available context is too thin to produce useful candidates. Otherwise, proceed with reasonable assumptions and label them.

## What Counts As A Good Skill

Favor a candidate when it has several of these properties:

- Repeated: likely to be used more than once
- Procedural: benefits from a consistent workflow or checklist
- Triggerable: can be described clearly in the YAML `description`
- Knowledge-heavy: needs project, domain, tool, policy, or format-specific context
- Error-prone: prevents common omissions, wrong assumptions, or risky actions
- Resource-backed: could use scripts, references, assets, schemas, templates, or examples
- Verifiable: has concrete examples or pass/fail checks

Avoid recommending a skill when the task is one-off, trivial for a general model, mostly inspirational, too broad to trigger reliably, or dependent on information that changes too quickly unless the skill includes a verification step.

For more examples and anti-patterns, read `references/opportunity-patterns.md` when the user asks for many ideas, a full audit, or deeper prioritization.

## Mining Workflow

1. Extract pain points from the user request, repository context, chat history, or workflow description.
2. Group similar pain points into reusable skill themes.
3. Filter out weak candidates using the good-skill criteria.
4. Name each surviving candidate in lowercase hyphen-case, under 64 characters.
5. Write a concise description that includes what the skill does and when to use it.
6. Recommend the strongest candidates and explain why they are worth building first.

## Scoring

Use this quick scoring model when prioritization matters. Score each category from 0 to 2.

- Frequency: how often the workflow recurs
- Friction: how much time, confusion, or correction it saves
- Specificity: how clearly the skill can trigger
- Stability: how stable the workflow is over time
- Resource fit: whether bundled references, scripts, or assets would help
- Verification: whether success can be checked

Interpretation:

- 10-12: build soon
- 7-9: useful candidate, refine scope
- 4-6: keep as a prompt or checklist for now
- 0-3: do not make a skill yet

## Output Format

Unless the user requests another format, present 5-8 candidates in a table with:

- `skill name`
- `pain point`
- `description`
- `why useful`
- `likely resources`
- `priority`

After the table, recommend the top 1-3 skills to build first. If one idea is clearly best, say so directly.

## Description Drafting Rules

Write descriptions as frontmatter-ready text:

- Include both capability and trigger context.
- Mention concrete scenarios, artifacts, tools, or workflows.
- Avoid vague descriptions like "helps with productivity" or "improves workflow."
- Avoid implementation details unless they matter for triggering.
- Include enough synonyms that natural user requests will trigger the skill.

Example description shape:

```yaml
description: Analyze recurring user workflows, repeated prompts, tool friction, and agent failure patterns to identify useful Codex skill opportunities. Use when brainstorming new skills, prioritizing skill ideas, or converting vague pain points into concrete skill candidates with names, descriptions, resources, and validation examples.
```

## Resource Planning

For each candidate, suggest only resources that would materially improve execution:

- `references/` for domain rules, schemas, examples, rubrics, policies, or checklists
- `scripts/` for deterministic repeated operations
- `assets/` for templates, boilerplate, icons, design files, or reusable media
- no bundled resources when concise instructions are enough

Do not over-engineer the skill. A small SKILL.md is better than unused folders.

## Handoff To Creation

If the user chooses a candidate and asks to build it, switch to the skill creation workflow:

1. Confirm the save location if it is not already specified.
2. Use the `skill-creator` process to initialize, write, validate, and iterate.
3. Preserve the selected name and description unless implementation reveals a clearer scope.
