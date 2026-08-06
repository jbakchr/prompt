# prompt

A CLI for creating, reviewing, and improving AI prompts.

prompt helps you generate useful prompts by guiding you through a small set of questions about:

- What the AI should do
- Who the audience is
- What role the AI should take on
- Any special instructions
- Desired output format

The goal is not to generate the perfect prompt.

The goal is to generate a strong starting prompt that can be reviewed, improved, and refined over time.

---

## Why?

Writing prompts often starts with a simple idea:

> I want the AI to summarize an article.

However, producing consistently useful results often requires additional context:

- Who is the intended audience?
- What role should the AI take on?
- Are there any special requirements?
- How should the response be formatted?

Instead of staring at a blank editor, prompt helps you think through these questions and uses AI to generate a prompt you can immediately use.

---

## Features

### ✅ Create Prompts

Generate prompts from a guided question flow.

```bash
prompt create
```

The CLI asks questions such as:

- What should the AI do?
- Who is the intended audience?
- What role should the AI take on?
- Any specific instructions?
- Desired output format?

Each question includes:

- Helpful tips
- Example answers
- Clear visual formatting

Once all questions are answered, an AI generates a prompt and displays it in a dedicated panel.

---

### ✅ Save Prompts

After generating a prompt, prompt can save it to disk.

Example:

```text
Would you like to save this prompt? [y/N]
```

Saved prompts are stored in:

```text
~/.prompt/prompts/
```

making them easy to reuse, review, and improve later.

---

### ✅ Review Prompts

Review an existing prompt and receive constructive feedback.

```bash
prompt review prompt.md
```

The AI analyzes the prompt and returns:

- Strengths
- Weaknesses
- Suggestions

Example:

```text
✅ Strengths

• Clear audience
• Strong role definition

⚠ Weaknesses

• Missing output constraints
• No length guidance

💡 Suggestions

• Specify desired output format
• Add length requirements
```

Reviews are intended to help users identify opportunities for improvement before editing a prompt.

---

### 🧠 AI-Powered Prompt Generation

prompt uses an AI model to transform user requirements into structured prompts.

Generated prompts may include:

- Roles
- Audience information
- Output requirements
- Constraints
- Formatting instructions

The generated prompt is intended to be useful immediately while still serving as a starting point for future refinement.

---

### 🤖 Rich Terminal Interface

prompt uses Rich to provide an improved terminal experience.

Features include:

- Question panels
- Tips and examples
- AI generation spinner
- Generated prompt display panel
- Markdown-rendered prompt reviews

The project values usability as much as prompt quality.

---

## Philosophy

### Good Enough First

The goal of prompt is not to generate giant, over-engineered prompts.

The goal is to generate useful prompts quickly.

---

### Better Questions Lead To Better Prompts

Prompt quality often depends on the information provided.

prompt helps users think through:

- Tasks
- Audience
- Roles
- Constraints
- Formatting

which leads to stronger prompts.

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

prompt is designed around this iterative workflow.

---

## Commands

### Create

Generate a prompt through a guided question flow.

```bash
prompt create
```

---

### Review

Review an existing prompt.

```bash
prompt review <prompt-file>
```

Example:

```bash
prompt review summarize-article.md
```

---

### Improve

Improve an existing prompt.

```bash
prompt improve <prompt-file>
```

Status: Planned.

---

## Example Workflow

Generate a prompt:

```bash
prompt create
```

Save the generated prompt:

```text
Would you like to save this prompt? [y/N]
```

Review the prompt:

```bash
prompt review my-prompt.md
```

Improve the prompt:

```bash
prompt improve my-prompt.md
```

---

## Current Status

### ✅ Implemented

- Interactive prompt creation
- AI-powered prompt generation
- Rich terminal interface
- Question panels with tips and examples
- Prompt generation spinner
- Generated prompt display panel
- Prompt saving
- Prompt review
- Markdown-rendered reviews
- Suggested next steps section

### 🚧 Planned

- Prompt improvement
- Prompt comparison
- Prompt history
- Prompt library commands

---

## Inspiration

This project grew out of experimenting with prompt engineering through small, incremental prompt improvements and observing how those changes affected AI output.

One important lesson quickly became clear:

> Better prompts usually start with better questions.

prompt exists to ask those questions for you.

---

## Core Idea

Good prompts come from good requirements.

Good requirements come from good questions.

prompt helps users ask those questions and turns the answers into a useful starting prompt that can be reviewed and improved over time.