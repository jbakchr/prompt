# prompt

A CLI for creating, improving, and reviewing AI prompts.

`prompt` helps you craft better prompts by guiding you through a small set of questions about your goal, audience, role, instructions, and desired output.

The goal is not to generate the perfect prompt.

The goal is to generate a good starting prompt that can be refined over time, either by you or by the CLI itself.

---

## Why?

Writing prompts often starts with a simple idea:

> "I want the AI to summarize an article."

However, getting consistently useful output usually requires additional context:

- Who is the intended audience?
- Should the AI take on a specific role?
- Are there any special requirements?
- What output format should be used?

Instead of staring at an empty editor, `prompt` asks these questions for you and generates a prompt draft that is ready to use.

---

## Features

### Create Prompts

Generate a prompt from a guided question flow.

```bash
prompt create
```

Example:

```text
What is the goal?
> Summarize a Python article

Who is the intended audience?
> Intermediate Python developers

Should the AI take on a role?
> Experienced Python developer

Any specific instructions?
> Focus on practical takeaways

Desired output format?
> Markdown bullet points
```

Generated prompt:

```text
You are an experienced Python developer.

Summarize the following article for intermediate Python developers.

Focus on:
- Key concepts
- Practical takeaways

Use Markdown bullet points.

Article:
{article}
```

---

### Improve Existing Prompts

Improve an existing prompt based on specific issues or desired changes.

```bash
prompt improve summarize.md
```

Example:

```text
What would you like to improve?

> The summary is too long
```

The AI analyzes the prompt and generates an improved version.

Possible improvement requests:

- Too verbose
- Too short
- Wrong audience
- Missing structure
- Produces too much code
- Produces too little code
- Not specific enough
- Too generic
- Other

---

### Review Prompts

Review a prompt and receive constructive feedback.

```bash
prompt review summarize.md
```

Example output:

```text
Strengths
---------
- Clear goal
- Well-defined audience

Weaknesses
----------
- No length constraints
- Output format could be clearer

Suggestions
-----------
- Add a maximum length
- Specify whether examples should be included
```

---

## Philosophy

### Good Enough First

The goal of `prompt` is not to generate giant, complicated prompts.

The goal is to generate a solid first version that can be refined and improved over time.

---

### Guided Prompt Creation

The CLI focuses on a handful of questions that frequently improve prompt quality:

- Goal
- Audience
- Role
- Instructions
- Output format

These questions help provide the context that an AI often needs to produce better results.

---

### Iterative Improvement

Prompt engineering is rarely a one-step process.

A typical workflow might look like:

```text
Create Prompt
      ↓
Use Prompt
      ↓
Review Prompt
      ↓
Improve Prompt
      ↓
Use Improved Prompt
```

---

## Commands

### Create

Create a new prompt from a guided series of questions.

```bash
prompt create
```

---

### Improve

Improve an existing prompt.

```bash
prompt improve <prompt-file>
```

---

### Review

Review a prompt and receive suggestions for improvement.

```bash
prompt review <prompt-file>
```

---

## Example Workflow

Create a new prompt:

```bash
prompt create
```

Save the generated prompt:

```text
prompts/summarize-python-article.md
```

Review the prompt:

```bash
prompt review prompts/summarize-python-article.md
```

Improve the prompt:

```bash
prompt improve prompts/summarize-python-article.md
```

Use the updated prompt with your preferred AI model.

---

## Future Ideas

Potential future enhancements:

- Prompt templates
- Prompt version history
- Prompt comparisons
- Prompt scoring
- Prompt libraries
- Interactive refinement sessions
- Export to Markdown
- Export to clipboard

---

## Project Status

Early project idea.

The initial focus is intentionally small:

```bash
prompt create
prompt improve
prompt review
```

The goal is to make these commands genuinely useful before adding more features.

---

## Inspiration

This project grew out of experimenting with prompt engineering through small, incremental prompt changes and observing how those changes affected AI behavior.

One observation quickly became clear:

A prompt that includes information about the audience, role, goal, and desired output often performs dramatically better than a prompt that only describes the task.

`prompt` aims to make it easy to include that context from the start.

---

## Core Idea

Good prompts usually start with good questions.

`prompt` asks those questions for you.
