# Hermes Skills Phase 3 Local Refactor Report

> Date: 2026-05-02
> Scope: local Hermes runtime registry only
> Path: `/Users/marovole/.hermes/skills`
> Repository policy: Superpowers repo is docs + promoted skills, not a full mirror

---

## Goal

Reduce overcrowding in the two largest local runtime categories:

- `creative`: 28 active skills
- `software-development`: 19 active skills

This Phase 3 refactor intentionally did not mirror all local skills into the Superpowers GitHub repository. It only reorganized the local Hermes runtime registry and records the result here for traceability.

---

## Result Summary

- Active skills before: 175
- Active skills after: 175
- Duplicate active skill names after: 0
- Missing active skill names after: 0
- Direct leftovers under old `creative/*/SKILL.md`: 0
- Direct leftovers under old `software-development/*/SKILL.md`: 0
- Moved skill frontmatter category mismatches: 0

Both overcrowded categories were decomposed into focused subcategories below the >15 threshold.

---

## New Creative Structure

Original:

```text
creative: 28
```

New:

```text
creative/code-visuals: 8
creative/content: 7
creative/design: 6
creative/image: 7
```

### creative/design

- `claude-design`
- `huashu-design`
- `sketch`
- `popular-web-designs`
- `design-md`
- `html-deck`

Purpose: UI, visual design, design systems, decks, prototypes, design artifacts.

### creative/image

- `image-generation`
- `gpt-image-2-workflow`
- `concept-poster-prompt`
- `json-style-protocol`
- `handmade-newspaper-prompt`
- `pixel-art`
- `comfyui`

Purpose: image generation, visual prompt systems, image pipelines, consistent visual style production.

### creative/code-visuals

- `p5js`
- `manim-video`
- `touchdesigner-mcp`
- `pretext`
- `ascii-art`
- `ascii-video`
- `architecture-diagram`
- `excalidraw`

Purpose: code-generated visuals, diagrams, animation, interactive visual systems, ASCII and drawing tools.

### creative/content

- `humanizer`
- `long-form-translation`
- `baoyu-comic`
- `baoyu-infographic`
- `songwriting-and-ai-music`
- `markdown-to-social-cards`
- `creative-ideation`

Purpose: writing, translation, comics, infographics, music, social cards, ideation.

---

## New Software Development Structure

Original:

```text
software-development: 19
```

New:

```text
software-development/ai-coding: 4
software-development/code-quality: 3
software-development/debugging: 4
software-development/planning: 4
software-development/skill-authoring: 4
```

### software-development/debugging

- `systematic-debugging`
- `debugging-hermes-tui-commands`
- `node-inspect-debugger`
- `python-debugpy`

Purpose: root-cause debugging, TUI debugging, runtime inspector workflows.

### software-development/code-quality

- `code-review`
- `requesting-code-review`
- `test-driven-development`

Purpose: review, TDD, quality gates, pre-commit checks.

### software-development/planning

- `plan`
- `writing-plans`
- `spike`
- `github-project-portfolio-analysis`

Purpose: planning, implementation plan writing, throwaway experiments, portfolio/project analysis.

### software-development/skill-authoring

- `gpt-5.5-prompt-strategy`
- `hermes-agent-skill-authoring`
- `skill-repository-refactoring`
- `skill-classification-decision-tree`

Purpose: creating, reviewing, classifying, and refactoring Hermes skills.

### software-development/ai-coding

- `subagent-driven-development`
- `cmux-multi-agent-terminal`
- `team-ai-coding-sop`
- `multi-model-task-router`

Purpose: AI coding workflows, multi-agent execution, team SOP, model routing.

---

## Validation

Validated after moves:

```text
active_total: 175
duplicate_names: {}
missing_names: []
old_creative_direct_leftovers: []
old_software_direct_leftovers: []
moved_category_frontmatter_mismatches: []
```

Representative `skill_view` checks passed after move:

- `gpt-image-2-workflow` → `creative/image/gpt-image-2-workflow`
- `systematic-debugging` → `software-development/debugging/systematic-debugging`
- `gpt-5.5-prompt-strategy` → `software-development/skill-authoring/gpt-5.5-prompt-strategy`
- `subagent-driven-development` → `software-development/ai-coding/subagent-driven-development`

---

## Full Category Counts After Phase 3

```text
(root): 2
apple: 4
autonomous-ai-agents: 9
content-publishing: 1
creative/code-visuals: 8
creative/content: 7
creative/design: 6
creative/image: 7
data-science: 1
devops: 9
document-processing: 4
email: 3
external-tools: 3
gaming: 2
github: 6
inference: 2
leisure: 1
mcp: 2
media: 6
mlops: 5
mlops/cloud: 2
mlops/evaluation: 5
mlops/inference: 6
mlops/models: 6
mlops/research: 1
mlops/training: 11
mlops/vector-databases: 1
note-taking: 2
productivity: 4
red-teaming: 1
research: 15
smart-home: 1
social-media: 3
software-development/ai-coding: 4
software-development/code-quality: 3
software-development/debugging: 4
software-development/planning: 4
software-development/skill-authoring: 4
task-management: 4
web-automation: 2
workspace-integration: 4
```

---

## Notes

- This was a local runtime refactor, not a Superpowers repo mirror operation.
- Superpowers keeps its方案 2 policy: docs + promoted skills only.
- Future promoted skills can use these local category paths as reference, but repo paths are not required to mirror runtime paths unless explicitly promoted.

---

*来自翡冷翠* | Phase 3 completed 2026-05-02
