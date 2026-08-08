# prompt - Roadmap

This roadmap is intentionally simple.

The goal is not to build the ultimate prompt engineering platform.

The goal is to build a practical CLI that helps users create, review, and improve AI prompts with minimal friction.

---

## Vision

Create a CLI that helps users:

- Create prompts from guided questions
- Review prompts and receive actionable feedback
- Improve prompts through iterative refinement
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

✅ Workflow-oriented command structure

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

### ✅ Phase 4 Complete: Prompt Improvement

The `prompt improve` command is now implemented.

Implemented:

✅ Load existing prompts

✅ Guided improvement requests

✅ AI-powered prompt improvement

✅ Targeted prompt editing

✅ Preservation of original intent

✅ Improvement summaries

✅ "Improvements Made" section

✅ Explanation of why changes help

✅ Rich improved-prompt display

✅ Optional prompt saving

Example:

```bash
prompt improve my-prompt.md
```

Workflow:

```text
Load Prompt
      ↓
Describe Desired Improvement
      ↓
AI Improves Prompt
      ↓
See Improvements Made
      ↓
See Why They Help
      ↓
Review Improved Prompt
      ↓
Save (Optional)
```

The improvement workflow is intentionally designed to behave like an editor rather than a rewriter.

The goal is to make focused improvements while preserving the original purpose of the prompt.

Example improvement requests:

- Add a structured output format
- Make the response shorter
- Generate more code examples
- Require step-by-step explanations
- Focus on practical learning

Success Criteria Achieved:

✅ Improvements feel useful

✅ Improvements are focused

✅ Original intent is preserved

✅ Workflow is faster than manual editing

✅ Users can iteratively refine prompts

---

## Phase 5: Better Workflow

### Goal

Reduce friction between creating, reviewing, and improving prompts.

### Features

#### Review → Improve Workflow

Allow review results to drive prompt improvements.

Possible future command:

```bash
prompt improve prompt.md --use-review
```

Workflow:

```text
Review Prompt
      ↓
Weaknesses & Suggestions
      ↓
Improve Prompt Using Feedback
```

The long-term goal is for review and improvement to work together seamlessly.

---

#### Clipboard Support

Allow prompts to be copied directly to the clipboard.

Possible use cases:

```text
Generate Prompt
      ↓
Copy
      ↓
Paste Into AI
```

```text
Improve Prompt
      ↓
Copy
      ↓
Paste Into AI
```

---

#### Prompt Editing

Allow users to edit generated or improved prompts before saving.

Goal:

Reduce the need to leave the CLI for small prompt adjustments.

---

#### Prompt Comparison

Compare two prompt versions.

Example:

```bash
prompt compare original.md improved.md
```

Goal:

Help users understand how prompts evolve over time.

### Success Criteria

✅ Less manual editing

✅ Faster prompt iteration

✅ Better review → improve workflow

✅ Lower workflow friction

---

## Phase 6: Prompt Library

### Goal

Make prompts searchable and reusable.

### Features

#### List Prompts

```bash
prompt list
```

---

#### Show Prompt

```bash
prompt show my-prompt.md
```

---

#### Search Prompts

```bash
prompt search summarize
```

---

#### Categories

Possible examples:

```text
summarization/
coding/
writing/
learning/
research/
```

### Success Criteria

✅ Easy to find prompts

✅ Reusable prompt collection

✅ Useful long-term prompt archive

---

## Future Ideas

These ideas are intentionally lower priority.

Implement only if they provide clear practical value.

### Prompt History

Track prompt evolution over time.

Goal:

Help users see how prompts have changed through iterative refinement.

---

### Prompt Explain

Analyze a prompt and explain:

- Intended role
- Intended audience
- Output format
- Constraints
- Potential weaknesses

Possible command:

```bash
prompt explain prompt.md
```

Useful when working with older prompts or prompts created by others.

---

### Prompt Testing

Evaluate prompts against sample inputs.

Possible command:

```bash
prompt test prompt.md
```

Long-term goal:

Allow prompt quality improvements to be driven by actual results instead of assumptions.

---

## Current Focus

Current priority:

```text
Review
      ↓
Improve
      ↓
Repeat
```

The core create, save, review, and improve workflows are now implemented.

The next goal is reducing friction between review and improvement while helping users refine prompts more efficiently over time.

---

## What Has Been Validated

The following assumptions have now been validated through implementation:

✅ Guided questions improve prompt quality

✅ AI-generated prompts are more useful than simple templates

✅ Rich CLI UX improves the experience

✅ Prompt saving is valuable

✅ AI-powered prompt review provides useful feedback

✅ AI-assisted prompt improvement is valuable

✅ Users benefit from seeing what changed

✅ Users benefit from understanding why changes were made

✅ The Create → Review → Improve workflow feels natural

---

## Guiding Principle

A small tool that solves a real problem is better than a large tool with unfinished features.

Focus on:

✅ Simplicity

✅ Practical usefulness

✅ Iterative improvement

✅ Workflow clarity

✅ Minimal friction

Avoid:

❌ Feature creep

❌ Overengineering

❌ Prompt perfectionism

❌ Becoming a platform

The goal remains:

👉 Generate useful prompts quickly.

👉 Review them constructively.

👉 Improve them iteratively.