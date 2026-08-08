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

### ✅ Improve Prompts

Improve an existing prompt through guided AI-assisted refinement.

```bash
prompt improve prompt.md
```

The CLI:

1. Loads an existing prompt
2. Asks what should be improved
3. Uses AI to make targeted improvements
4. Explains what changed
5. Explains why the changes help
6. Displays the improved prompt
7. Offers to save the result

Example improvement requests:

- Make the response shorter
- Add a structured output format
- Generate more code examples
- Focus on practical learning
- Make it suitable for beginners
- Require step-by-step explanations

Example output:

```text
✨ Improvements Made

✓ Added a structured output format
✓ Added dedicated sections for key concepts and examples
✓ Added formatting requirements for code examples

💡 Why

The changes introduce a clear response structure while
preserving the prompt's original purpose and audience.
```

The goal is not to rewrite prompts.

The goal is to improve them incrementally while preserving the user's original intent.

---

### 🧠 AI-Powered Prompt Workflows

prompt uses AI to:

- Generate prompts
- Review prompts
- Improve prompts

Generated prompts may include:

- Roles
- Audience information
- Output requirements
- Constraints
- Formatting instructions

Prompt improvements focus on:

- Targeted edits
- User-requested changes
- Preserving original intent
- Iterative refinement

---

### 🤖 Rich Terminal Interface

prompt uses Rich to provide an improved terminal experience.

Features include:

- Question panels
- Tips and examples
- AI generation spinner
- Generated prompt display panels
- Improvement summaries
- Markdown-rendered reviews
- Suggested next steps

The project values usability as much as prompt quality.

---

## Philosophy

### Good Enough First

The goal of prompt is not to generate giant, over-engineered prompts.

