# ROADMAP.md

# prompt Roadmap

This roadmap is intentionally simple.

The goal is not to build the ultimate prompt engineering platform.

The goal is to build a practical CLI that helps users create, improve, and review AI prompts with minimal friction.

---

# Vision

Create a CLI that helps users:

- Create prompts from guided questions
- Improve existing prompts
- Review prompts and receive actionable feedback

The CLI should act as a practical prompt assistant, not a prompt engineering course.

---

# Current Status

## ✅ Phase 1 Complete: Prompt Creation

The `prompt create` command is now a functional MVP.

Implemented:

✅ Guided question flow

✅ Question tips

✅ Example answers

✅ Rich question panels

✅ AI-powered prompt generation

✅ Terminal spinner while AI generates prompts

✅ Generated prompt displayed in a dedicated panel

✅ Suggested next steps

✅ Model selection support

The generated prompts are intended to be useful starting points that users can continue refining.

---

# Phase 2: Save Prompts

## Goal

Allow generated prompts to be stored and reused.

## Features

### Save Generated Prompt

```bash
prompt create --save
```

Prompt the user for a filename and save the generated prompt.

Example:

```bash
prompt create --save
```

```text
Filename:
> summarize-python-article.md
```

### Default Prompt Location

Store prompts in:

```text
~/.prompt/prompts/
```

### Future Enhancements

- Overwrite confirmation
- Automatic filename generation
- Timestamped filenames

## Success Criteria

- Generated prompts can be saved
- Saved prompts are easy to find
- Prompts become reusable assets

---

# Phase 3: Prompt Improvement

## Goal

Allow users to iteratively improve prompts.

## Features

### Improve Existing Prompt

```bash
prompt improve my-prompt.md
```

Read an existing prompt.

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

to an AI.

Generate an improved version.

Display the improved prompt.

Optionally save it.

## Success Criteria

- Improvements feel useful
- Improvements are specific
- Workflow is faster than manually editing prompts

---

# Phase 4: Prompt Review

## Goal

Allow prompts to be reviewed before they are used.

## Features

### Review Prompt

```bash
prompt review my-prompt.md
```

AI analyzes the prompt.

Returns:

- Strengths
- Weaknesses
- Suggestions

Example:

```text
Strengths
---------
- Clear audience
- Good role definition

Weaknesses
----------
- No output constraints
- No length guidance

Suggestions
-----------
- Add summary length
- Specify formatting requirements
```

## Success Criteria

- Reviews are actionable
- Reviews are specific
- Reviews help improve prompts

---

# Phase 5: Better Workflow

## Goal

Reduce friction in day-to-day usage.

## Features

### Clipboard Support

Copy generated prompt directly to clipboard.

### Prompt Preview

Preview prompts before saving.

### Prompt Editing

Allow editing before save.

### Prompt Metadata

Store:

- Model used
- Creation date
- Prompt version

## Success Criteria

- Less manual work
- Faster workflow
- Better prompt management

---

# Phase 6: Prompt Library

## Goal

Make prompts searchable and reusable.

## Features

### List Prompts

```bash
prompt list
```

### Show Prompt

```bash
prompt show my-prompt.md
```

### Search Prompts

```bash
prompt search summarize
```

### Categories

Examples:

```text
summarization/
coding/
writing/
learning/
```

## Success Criteria

- Easy to find prompts
- Reusable prompt collection
- Useful long-term prompt archive

---

# Future Ideas

These ideas are intentionally lower priority.

Implement only if they provide real value.

## Compare Prompts

```bash
prompt compare v1.md v2.md
```

Compare prompt revisions.

---

## Prompt History

Track prompt evolution over time.

---

## Prompt Templates

Generate prompts from predefined templates.

Examples:

- Summarization
- Code Review
- Documentation
- Brainstorming
- Learning

---

## Model-Specific Prompt Generation

Generate prompts optimized for:

- GPT models
- Claude models
- Gemini models
- Ollama models

---

# Current Focus

Current priority:

```text
Save Prompts
      ↓
Improve Prompts
      ↓
Review Prompts
```

The core prompt creation experience is now in place.

The next goal is helping users manage, improve, and evaluate the prompts they generate.

---

# Guiding Principle

A small tool that solves a real problem is better than a large tool with unfinished features.

Focus on:

✅ Simplicity

✅ Practical usefulness

✅ Iterative improvement

Avoid:

❌ Feature creep

❌ Overengineering

❌ Prompt perfectionism

The goal remains:

👉 Generate useful starting prompts quickly.