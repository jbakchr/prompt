# prompt

A CLI for creating, improving, and reviewing AI prompts.

`prompt` helps you generate better prompts by guiding you through a small set of questions about:

- What the AI should do
- Who the audience is
- What role the AI should take on
- Any special instructions
- Desired output format

The goal is not to generate the perfect prompt.

The goal is to generate a strong starting prompt that can be refined over time.

---

## Why?

Writing prompts often starts with a simple idea:

> "I want the AI to summarize an article."

However, producing consistently useful results often requires additional context:

- Who is the intended audience?
- What role should the AI take on?
- Are there any special requirements?
- How should the response be formatted?

Instead of staring at a blank editor, `prompt` helps you think through these questions and uses AI to generate a prompt you can immediately use or improve further.

---

## Features

### ✅ Create Prompts

Generate a prompt from a guided question flow.

```bash
prompt create
```

The CLI asks questions such as:

```text
What should the AI do?
Who is the intended audience?
What role should the AI take on?
Any specific instructions?
Desired output format?
```

Each question includes:

- Helpful tips
- Example answers
- The ability to skip a question

Example:

```text
💬 DESCRIBE WHAT YOU NEED AND AN AI WILL GENERATE A STARTING PROMPT.

Question 1 of 5

What should the AI do?

Examples:
- Summarize the following article
- Review the provided Python code
- Create a learning roadmap for FastAPI
```

Once all questions are answered, an AI generates a starting prompt.

Example output:

```text
You are an experienced Python developer.

Summarize the following article for beginner Python developers.

Focus on:
- Practical explanations
- Easy-to-understand language

Use bullet points.

Article:

{article}
```

---

### 🧠 AI-Powered Prompt Generation

`prompt` uses an AI model to transform your answers into a structured prompt.

The generated prompt:

- Includes relevant context
- Includes roles when appropriate
- Includes output requirements
- Can be copied and used immediately

---

### 🤖 Generated Prompt Display

Generated prompts are displayed in a dedicated panel for easy reading and copying.

Example:

```text
╭──────────── 🤖 Generated Prompt ────────────╮
│ You are an experienced Python developer.    │
│                                              │
│ Summarize the following article...           │
│                                              │
│ Article:                                     │
│ {article}                                    │
╰──────────────────────────────────────────────╯
```

---

### 👉 Suggested Next Steps

After generating a prompt, the CLI suggests possible next actions.

Example:

```text
👉 Suggested Next Steps

• Use the generated prompt as a starting point.

• Save the generated prompt:
  prompt create --save

• Try generating the prompt with a different model:
  prompt create --model <model-name>

• Improve a prompt:
  prompt improve <prompt-file>

• Review a prompt:
  prompt review <prompt-file>
```

---

## Philosophy

### Good Enough First

The goal of `prompt` is not to generate giant, over-engineered prompts.

The goal is to generate a strong starting point that can be refined over time.

---

### Better Questions Lead To Better Prompts

Prompt quality often depends on the information provided.

`prompt` helps users provide:

- Better task descriptions
- Better audience definitions
- Better role definitions
- Better instructions

Which leads to better generated prompts.

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

Generate a prompt through a guided question flow.

```bash
prompt create
```

Generate using a specific model:

```bash
prompt create --model qwen3:8b
```

Save the generated prompt:

```bash
prompt create --save
```

---

### Improve

Improve an existing prompt.

```bash
prompt improve <prompt-file>
```

Planned.

---

### Review

Review a prompt and receive suggestions for improvement.

```bash
prompt review <prompt-file>
```

Planned.

---

## Example Workflow

Generate a prompt:

```bash
prompt create
```

Copy and use the generated prompt.

Optionally save it:

```bash
prompt create --save
```

Experiment with different models:

```bash
prompt create --model qwen3:8b
```

Later:

```bash
prompt review my-prompt.md
prompt improve my-prompt.md
```

---

## Current Status

### Implemented

✅ Interactive prompt creation

✅ Rich-based terminal interface

✅ Question panels with tips and examples

✅ AI-powered prompt generation

✅ Prompt generation spinner

✅ Generated prompt display panel

✅ Suggested next steps section

### Planned

- Save generated prompts
- Prompt improvement
- Prompt review
- Prompt comparison
- Prompt history

---

## Inspiration

This project grew out of experimenting with prompt engineering through small, incremental prompt improvements and observing how those changes affected AI output.

One important lesson quickly became clear:

> Better prompts usually start with better questions.

`prompt` exists to ask those questions for you.

---

## Core Idea

Good prompts come from good requirements.

Good requirements come from good questions.

`prompt` helps you ask those questions and turns the answers into a useful starting prompt.