# prompt - Roadmap

This roadmap is intentionally simple.

The goal is not to build the ultimate prompt engineering platform.

The goal is to build a practical CLI that helps users create, review, and improve AI prompts with minimal friction.

---

## Vision

Create a CLI that helps users:

- Create prompts from guided questions
- Review prompts and receive actionable feedback
- Improve existing prompts
- Build a reusable collection of prompts over time

The CLI should act as a practical prompt assistant, not a prompt engineering course.

---

## Current Status

### ✅ Phase 1 Complete: Prompt Creation

The `prompt create` command is now a functional MVP.

Implemented:

✅ Guided question flow

✅ Question tips

✅ Example answers

✅ Rich question panels

✅ AI-powered prompt generation

✅ AI generation spinner

✅ Generated prompt display panel

✅ Suggested next steps

✅ Prompt requirements model

✅ Refactored workflow-oriented command structure

The generated prompts are intended to be useful starting points that users can continue refining.

---

### ✅ Phase 2 Complete: Prompt Saving

Generated prompts can now be saved directly from the create workflow.

Implemented:

✅ Optional save step after prompt generation

✅ User-provided filenames

✅ Default prompt storage location

```text
~/.prompt/prompts/
```

✅ Prompt file persistence

The save workflow keeps prompts available for future review and improvement.

---

### ✅ Phase 3 Complete: Prompt Review

The `prompt review` command is now implemented.

Implemented:

✅ Load saved prompts

✅ AI-powered prompt analysis

✅ Strengths section

✅ Weaknesses section

✅ Suggestions section

✅ Rich review panel

✅ Markdown-rendered review output

✅ No scoring or ratings

The review workflow helps users identify opportunities for improvement before editing a prompt.

Example:

```bash
prompt review my-prompt.md
```

Returns:

```text
✅ Strengths

⚠ Weaknesses

💡 Suggestions
```

with actionable feedback.

---

## Phase 4: Prompt Improvement

### Goal

Allow users to iteratively improve prompts.

### Features

#### Improve Existing Prompt

```bash
prompt improve my-prompt.md
```

Read a saved prompt.

Ask:

```text
What would you like to improve?
```

Examples:

- Too verbose
- Too short
- Wrong audience
- Missing structure
- Produces too much code
- Produces too little code
- Other

Send:

```text
Existing prompt
+
Improvement request
```

to an AI model.

Generate an improved prompt.

Display the improved prompt.

Offer to save the improved version.

---

### Success Criteria

- Improvements feel useful
- Improvements are specific
- Workflow is faster than manually editing prompts
- Improvements build naturally from review feedback

---

## Phase 5: Better Workflow

### Goal

Reduce friction in day-to-day usage.

### Features

#### Clipboard Support

Copy generated prompts directly to the clipboard.

#### Prompt Preview

Preview prompts before saving.

#### Prompt Editing

Allow editing before save.

#### Prompt Metadata

Store metadata such as:

- Creation date
- Prompt version
- Model used

#### Review → Improve Workflow

Allow review feedback to drive prompt improvements.

Possible future idea:

```bash
prompt improve prompt.md --use-review
```

---

### Success Criteria

- Less manual work
- Faster workflow
- Better user experience
- Better prompt management

---

## Phase 6: Prompt Library

### Goal

Make prompts searchable and reusable.

### Features

#### List Prompts

```bash
prompt list
```

#### Show Prompt

```bash
prompt show my-prompt.md
```

#### Search Prompts

```bash
prompt search summarize
```

#### Categories

Examples:

```text
summarization/
coding/
writing/
learning/
```

---

### Success Criteria

- Easy to find prompts
- Reusable prompt collection
- Useful long-term prompt archive

---

## Future Ideas

These ideas are intentionally lower priority.

Implement only if they provide real value.

### Compare Prompts

```bash
prompt compare v1.md v2.md
```

Compare prompt revisions.

### Prompt History

Track prompt evolution over time.

### Prompt Templates

Generate prompts from predefined templates.

Examples:

- Summarization
- Code Review
- Documentation
- Brainstorming
- Learning

### Model-Specific Prompt Generation

Generate prompts optimized for:

- GPT models
- Claude models
- Gemini models
- Ollama models

---

## Current Focus

Current priority:

```text
Improve Prompts
      ↓
Better Workflow
      ↓
Prompt Library
```

The create, save, and review workflows are now implemented.

The next major goal is helping users improve prompts using AI-assisted refinement.

---

## What Has Been Validated

The following assumptions have now been validated through implementation:

✅ Guided questions improve prompt quality

✅ AI-generated prompts are more useful than simple templates

✅ Rich CLI UX improves the experience

✅ Prompt saving is valuable

✅ AI-powered prompt review provides useful feedback

✅ The Create → Review workflow feels natural

---

## Guiding Principle

A small tool that solves a real problem is better than a large tool with unfinished features.

Focus on:

✅ Simplicity

✅ Practical usefulness

✅ Iterative improvement

✅ Workflow clarity

Avoid:

❌ Feature creep

❌ Overengineering

❌ Prompt perfectionism

The goal remains:

👉 Generate useful prompts quickly.

👉 Review them constructively.

👉 Improve them iteratively.