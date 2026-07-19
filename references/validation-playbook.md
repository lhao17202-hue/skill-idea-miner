# Validation Playbook

Use this when deciding whether a skill candidate is worth building or when preparing forward tests.

## Candidate Acceptance Checks

A candidate is strong when it can answer yes to most of these:

- Would the user invoke it more than once?
- Can the trigger be written in one clear description?
- Does it remove repeated explanation or repeated correction?
- Does it produce a predictable kind of output?
- Can success be checked?
- Would references, scripts, or assets save meaningful context or work?

## Red Flags

Treat these as reasons to narrow or reject the candidate:

- The name is a broad category instead of an action
- The description depends on private unstated context
- The workflow changes completely each time
- The skill would mostly tell Codex to "think better"
- The skill duplicates another skill without a sharper trigger
- The only resource is a long document that Codex would rarely need

## Forward-Test Prompt Pattern

Use raw tasks, not hidden answers.

```text
Use $skill-name at /path/to/skill-name to help identify useful skill ideas from this workflow description:

[paste realistic workflow or pain point]
```

Evaluate whether the result:

- filters weak ideas
- explains pain points clearly
- names skills in hyphen-case
- writes trigger-ready descriptions
- suggests resources only when useful
- recommends a clear build order

## Example Test Cases

### Low Context

Prompt:

```text
I want to create a few Codex skills for my daily work, but I do not know where to start.
```

Expected behavior:
Ask at most two useful questions, or proceed with assumptions and produce a general candidate list.

### Repeated Correction

Prompt:

```text
Codex keeps finishing frontend work without checking screenshots, mobile layout, or text overflow.
```

Expected behavior:
Recommend a visual QA skill and include screenshot/responsive checks as validation.

### Weak Idea

Prompt:

```text
Make a skill that makes Codex smarter at everything.
```

Expected behavior:
Reject or narrow the idea, then propose concrete alternatives based on actual repeated pain points.
