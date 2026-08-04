# PROJECT_CONTEXT.md

# prompt – Project Context

## 🧠 What This Project Is

prompt is a CLI for creating, improving, and reviewing AI prompts.

The goal is NOT to build the ultimate prompt engineering platform.

The goal is:

👉 Make it fast and easy to create useful prompts from the command line.

The generated prompt does not need to be perfect.

It only needs to be a strong starting point that can be refined over time.

The project focuses on reducing the friction between:

"I know what I want"

and

"I know how to ask an AI for it."

---

## 🎯 Core Philosophy

The goal is NOT:

- Prompt perfection
- Giant prompts
- Prompt engineering theory
- Complex prompt frameworks
- Prompt marketplaces

The goal is:

👉 Generate useful starting prompts quickly.

Success is measured by questions such as:

- Does prompt create generate useful prompts?
- Does prompt improve make prompts noticeably better?
- Does prompt review provide useful feedback?
- Would I actually use this from my terminal?

---

## 🧭 Development Philosophy

This project should be developed incrementally.

Start simple.

Validate usefulness.

Improve based on real usage.

The progression should be:

Create
↓
Improve
↓
Review
↓
Better Workflow
↓
Prompt Library

rather than:

Add lots of features
↓
Hope people use them

---

## 🏗 Core Commands

### create

Purpose:

Generate a useful starting prompt.

The user answers a guided series of questions:

- What should the AI do?
- Who is the intended audience?
- What role should the AI take on?
- Any specific instructions?
- Desired output format?

The answers are sent to an AI model.

The AI generates a prompt.

The generated prompt is displayed in a dedicated Rich panel.

This command is currently implemented and functional.

---

### improve

Purpose:

Improve an existing prompt.

The CLI should:

- Read an existing prompt
- Ask what should be improved
- Send prompt + improvement request to an AI
- Generate an improved prompt

Examples:

- Too verbose
- Too short
- Wrong audience
- Missing structure
- Produces too much code
- Produces too little code

Status:

Planned.

---

### review

Purpose:

Review a prompt and identify opportunities for improvement.

The AI should provide:

- Strengths
- Weaknesses
- Suggestions

The goal is constructive feedback, not scoring prompts.

Status:

Planned.

---

## 📋 Prompt Creation Philosophy

Good prompts often include more than just a task.

For example:

Instead of:

Summarize this article.

A stronger prompt might include:

- A role
- An audience
- Additional instructions
- Output formatting requirements

The CLI helps users think about this context.

---

## ✅ Current Project Status

### Phase 1: Prompt Creation

Implemented:

✅ Typer CLI

✅ Rich terminal UI

✅ AI-powered prompt generation

✅ Question panels

✅ Question tips

✅ Example answers

✅ Question numbering

✅ AI generation spinner

✅ Generated prompt panel

✅ Suggested next steps section

✅ Model selection support

The current implementation produces prompts that are intended to serve as useful starting points.

---

## 🔍 Key Insights Discovered

### 1. Good Questions Lead To Better Prompts

The quality of the generated prompt is heavily influenced by the quality of the user's answers.

Helping users answer questions well is nearly as important as generating the prompt itself.

Question tips and examples significantly improved output quality.

---

### 2. Prompt Generation Is An AI Task

Originally the project generated prompts using string templates.

The project now uses an AI model to generate prompts.

This produces significantly better results.

Current preferred model:

qwen3:8b

---

### 3. Examples Matter

Adding examples to the prompt sent to the prompt-generation model dramatically improved prompt quality.

The AI now generates prompt templates rather than instructions about prompts.

---

### 4. UX Matters

The user experience improved significantly through:

- Rich question panels
- Tips
- Examples
- Visual separation between questions
- AI generation spinner
- Generated prompt panel
- Suggested next steps

The project is not only about AI quality.

It is also about making prompt creation enjoyable.

---

### 5. Prompt Engineering Is Iterative

Prompt creation rarely happens in one step.

Typical workflow:

Create
↓
Use
↓
Review
↓
Improve
↓
Use Again

The CLI should support this process.

---

## 🧭 Current Direction

Current priority:

Save Prompts
↓
Improve Prompts
↓
Review Prompts

The core prompt generation experience has been validated.

The focus should now move toward helping users manage, improve, and evaluate prompts.

---

## 🎯 Near-Term Focus

### Save Generated Prompts

Possible:

```bash
prompt create --save
```

Allow users to store prompts for future use.

---

### Build Prompt Improvement

Implement:

```bash
prompt improve <prompt-file>
```

Allow prompts to be refined through guided AI assistance.

---

### Build Prompt Review

Implement:

```bash
prompt review <prompt-file>
```

Allow prompts to be analyzed and critiqued before use.

---

## 🚫 Non-Goals

At this stage:

- Web application
- User accounts
- Prompt marketplace
- Prompt sharing platform
- Complex prompt scoring systems
- Prompt engineering courses
- Enterprise SaaS platform

Focus remains:

👉 Create prompts

👉 Improve prompts

👉 Review prompts

---

## ✅ What Makes This Project Different

This is NOT:

👉 A prompt marketplace

👉 A prompt library

👉 A prompt engineering course

This IS:

👉 A practical CLI for prompt creation and prompt improvement

Built around:

- Helpful questions
- Useful defaults
- Iterative improvement
- Minimal friction

---

## 🧠 Why This Matters (Personally)

This project exists because prompt creation often starts with:

"I know what I want."

but quickly becomes:

- Who is the audience?
- What role should the AI take on?
- What format should the output use?
- What constraints should be added?

Rather than starting from a blank editor every time, I want a CLI that helps generate a useful starting prompt that can be refined over time.

It is:

- a personal productivity tool
- built from real prompt engineering experiences
- designed around iterative improvement

---

## 🚀 What I Want Help With In A New Chat

Help me:

- Design new commands
- Improve AI prompt generation
- Improve CLI UX
- Build prompt improvement workflows
- Build prompt review workflows
- Keep the project focused
- Identify missing functionality
- Avoid overengineering

Avoid:

- unnecessary complexity
- feature creep
- enterprise architecture
- turning the project into a large platform

---

## 💡 How To Use This In A New Chat

When starting a new conversation:

I'm working on this project:

[paste PROJECT_CONTEXT.md]

Current status:

[describe what has been built]

Current goal:

[describe what feature is being worked on]

Help me:

[describe what you'd like assistance with]

Use this context to:

- understand the philosophy of the project
- stay aligned with project goals
- avoid feature creep
- maintain simplicity
- support incremental development
- prioritize practical usefulness

Remember:

The goal is not to generate perfect prompts.

The goal is to generate useful starting prompts quickly.
``