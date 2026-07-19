# Example Skill Candidates

Use these as inspiration, not as a fixed catalog. Adapt names and descriptions to the user's real pain points.

## Skill Development

### skill-description-optimizer

Pain point:
Skill descriptions are the main trigger surface, but they are easy to make vague or too broad.

Description:
Improve Codex skill names and YAML descriptions for accurate triggering, clear scope, and reduced false positives. Use when drafting or revising skill frontmatter, especially the `name` and `description` fields.

Likely resources:
`references/` with good and bad trigger examples.

### skill-auditor

Pain point:
Completed skills may contain bloated context, unclear resource routing, or weak validation.

Description:
Review existing Codex skills for triggering accuracy, context bloat, unclear instructions, missing validation, unnecessary files, and weak progressive disclosure. Use when checking whether a skill is useful, maintainable, and well-structured.

Likely resources:
`references/` audit rubric.

## Coding

### repo-onboarding-reader

Pain point:
Agents can edit too early before understanding project structure, scripts, conventions, and risk.

Description:
Systematically inspect unfamiliar repositories before editing by identifying stack, entry points, scripts, tests, conventions, and risky areas. Use when starting work in a new or unknown codebase.

Likely resources:
No bundled resources, or `references/` for stack-specific checklist variants.

### task-finish-checker

Pain point:
Coding tasks often end with missing tests, unclear final summaries, or forgotten output files.

Description:
Run a completion checklist for coding and artifact tasks, including changed files, verification commands, user-facing outputs, residual risks, and concise final response details. Use before finalizing a Codex task.

Likely resources:
`references/` final response templates.

## Frontend

### frontend-visual-qa

Pain point:
UI can compile while still having overflow, layout, blank canvas, or responsive failures.

Description:
Verify frontend work with screenshots, responsive viewport checks, text overflow checks, asset loading checks, and interaction smoke tests. Use after building or editing visual web apps, dashboards, games, or interactive tools.

Likely resources:
`scripts/` for screenshot checks, `references/` for visual QA rubric.

### design-system-matcher

Pain point:
New UI features can drift from the existing application's components, density, colors, and interaction style.

Description:
Analyze an existing frontend design system and apply matching layout, component, spacing, color, typography, and interaction patterns to new UI work. Use when extending an existing app without a provided mockup.

Likely resources:
`references/` style audit checklist.

## Writing And Research

### source-backed-answer

Pain point:
Research answers may mix recalled facts with unsupported claims.

Description:
Produce source-backed answers with current verification, precise citations, and clear separation between sourced facts and inference. Use when accuracy, recency, quotes, or attribution matter.

Likely resources:
`references/` citation and source-quality rubric.

### long-doc-synthesizer

Pain point:
Long documents require consistent extraction of claims, decisions, risks, and action items.

Description:
Synthesize long documents into structured summaries, decisions, risks, open questions, and action items while preserving important nuance. Use when analyzing lengthy reports, transcripts, meeting notes, or policy documents.

Likely resources:
`references/` output templates.

## Personal Workflow

### personal-workflow-capturer

Pain point:
User preferences and recurring process details are scattered across chats.

Description:
Extract personal working preferences, repeated commands, naming conventions, review habits, and output formats into reusable Codex skill or automation candidates. Use when building a personal Codex workflow system.

Likely resources:
`references/` interview prompts.

### windows-dev-helper

Pain point:
Windows development tasks often hit path quoting, PowerShell, execution policy, encoding, and port issues.

Description:
Provide Windows-first development guidance for Codex tasks, including PowerShell-safe commands, path handling, encoding, local server checks, and common Windows CLI pitfalls. Use when working in Windows repositories or desktop paths.

Likely resources:
`references/` Windows command patterns, `scripts/` only for deterministic checks.
