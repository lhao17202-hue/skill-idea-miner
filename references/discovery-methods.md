# Discovery Methods

Use these methods when the user wants skill ideas but gives only a broad area such as "my daily work", "coding", "writing", or "Codex usage".

## Mine Repetition

Look for language that signals repetition:

- "I always ask Codex to..."
- "Every time I start a project..."
- "I keep correcting..."
- "Before I finish, I need to check..."
- "This is easy to forget..."

Convert repetition into candidate skills only when the workflow has stable steps.

## Mine Corrections

Repeated corrections are often strong skill seeds. Ask what Codex tends to get wrong:

- output format
- tool choice
- repository conventions
- safety rules
- review depth
- local environment assumptions
- language, tone, or naming style

Good candidate shape:

```text
Pain point: Codex repeatedly misses local project conventions.
Skill: repo-convention-reader
Resource fit: references/conventions.md or generated project-specific notes
```

## Mine Context Rehydration

If the user repeatedly explains the same background, look for a domain knowledge skill:

- product rules
- schema relationships
- brand voice
- release process
- deployment steps
- legal or policy constraints

The skill should reduce repeated onboarding, not freeze unstable facts.

## Mine Quality Gates

Look for tasks where the user trusts Codex to finish but still needs a final check:

- UI screenshot checks
- test coverage checks
- release note checks
- accessibility checks
- migration safety checks
- citation checks

These are good candidates because they are procedural and verifiable.

## Mine Tool Rituals

Tools often create skill opportunities when they involve repeated setup:

- CLI flags
- authentication quirks
- local paths
- API paging
- export formats
- rate limits
- Windows vs Unix command differences

Recommend scripts only when the ritual includes deterministic repeated actions.

## Low-Context Questions

Ask no more than two questions. Prefer these:

```text
What kind of work do you repeat most often with Codex: coding, writing, research, operations, design, or personal workflow?
```

```text
What do you most often have to correct Codex about?
```

If the user does not answer, produce a general candidate list and label assumptions.
