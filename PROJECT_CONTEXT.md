# PROJECT_CONTEXT.md

# prompt – Project Context

## 🧠 What This Project Is

prompt is a CLI for creating, improving, and reviewing AI prompts.

The goal is NOT to create the ultimate prompt engineering platform.

The goal is:

👉 Make it faster and easier to create good prompts from the command line.

The CLI should help users think about the information that often improves prompt quality:

- Goal
- Audience
- Role
- Instructions
- Output Format

The generated prompt does not need to be perfect.

It only needs to be a strong starting point that can be refined over time.

---

## 🎯 Core Philosophy

The goal is NOT:

- Generating giant prompts
- Prompt perfection
- Complex prompt frameworks
- Teaching prompt engineering theory

The goal is:

👉 Generate useful prompts with minimal friction.

Success is measured by questions such as:

- Does prompt create generate useful prompt drafts?
- Does prompt improve make prompts noticeably better?
- Does prompt review provide actionable feedback?
- Is using the CLI faster than starting with a blank file?

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
Enhance UX

rather than:

Build every possible feature
    ↓
Hope people use it

---

## 🏗 Core Commands

### create

Purpose:

Generate a first version of a prompt.

The CLI should ask questions such as:

- What is the goal?
- Who is the intended audience?
- Should the AI take on a role?
- Any specific instructions?
- Desired output format?

The answers are sent to an AI model.

The AI returns a prompt draft.

---

### improve

Purpose:

Improve an existing prompt.

The CLI should:

- Read an existing prompt
- Ask what should be improved
- Send prompt + improvement request to an AI
- Generate an improved version

Examples:

- Too verbose
- Too short
- Too generic
- Produces too much code
- Wrong audience
- Missing structure

---

### review

Purpose:

Review a prompt and identify opportunities for improvement.

The AI should provide:

- Strengths
- Weaknesses
- Suggestions

The goal is constructive feedback, not scoring prompts.

---

## 📋 Prompt Creation Philosophy

Good prompts often include more than just a task.

For example:

Instead of:

Summarize this article.

A more useful prompt might include:

- A role
- An audience
- Additional instructions
- Desired output format

The CLI should help users think about these aspects.

---

## ✅ MVP Scope

The first useful version should only contain:

```bash
prompt create
prompt improve
prompt review
```

Nothing else is required.

A small tool that works well is preferable to a larger tool with unfinished features.

---

## ⚙️ Current Project Status

### Planning

✅ Project idea defined

✅ README created

✅ ROADMAP created

✅ Core commands identified

### Planned Commands

- create
- improve
- review

### Future Commands

Possible future additions:

- list
- show
- compare

Only add these if they provide genuine value.

---

## 🔍 Key Insights Behind The Project

### 1. Good Questions Lead To Better Prompts

Many prompt problems come from missing context:

- Who is the audience?
- What is the goal?
- What output format is desired?

The CLI should help users provide this context.

---

### 2. Prompt Engineering Is Iterative

Prompt creation is rarely a one-step process.

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

The CLI should support this workflow.

---

### 3. Simplicity Matters

The project should remain:

- CLI-first
- Fast
- Focused
- Practical

Avoid unnecessary complexity.

---

### 4. Usefulness Over Features

The most important question is:

"Would I actually use this from my terminal?"

If the answer is no, the feature probably should not be added.

---

## 🧭 Current Direction

Current priority:

Build create
    ↓
Validate usefulness
    ↓
Build improve
    ↓
Build review

The goal is to validate each capability before moving to the next one.

---

## 🎯 Near-Term Focus

### Phase 1

Implement:

```bash
prompt create
```

Questions:

- Goal
- Audience
- Role
- Instructions
- Output format

Generate prompt.

Display prompt.

Allow prompt to be saved.

Success means:

👉 Prompt creation feels genuinely useful.

---

## 🚫 Non-Goals

At this stage:

- Prompt marketplaces
- Prompt sharing systems
- User accounts
- Web applications
- Complex prompt scoring
- Prompt engineering courses
- Overengineered frameworks

Focus remains:

👉 Create prompts

👉 Improve prompts

👉 Review prompts

---

## ✅ What Makes This Project Different

This is NOT:

👉 A prompt engineering learning platform

👉 A prompt template marketplace

👉 A prompt database

This IS:

👉 A practical CLI for prompt creation and improvement

Built around:

- Asking useful questions
- Reducing friction
- Supporting iterative improvement

---

## 🧠 Why This Matters (Personally)

This project exists because creating prompts often begins with an idea but quickly becomes a process of:

- Determining audience
- Defining goals
- Adding context
- Refining instructions

Rather than starting from a blank editor every time, I want a CLI that helps me create a good starting prompt and improve it over time.

It is:

- a personal productivity tool
- built from real prompt engineering experiences
- designed around iterative improvement

---

## 🚀 What I Want Help With In A New Chat

Help me:

- Design CLI commands
- Design user flows
- Improve prompts sent to AI models
- Review project structure
- Keep the scope focused
- Improve UX
- Identify missing functionality
- Build features incrementally

Avoid:

- unnecessary complexity
- feature creep
- overengineering
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

- stay aligned with project goals
- avoid feature creep
- maintain simplicity
- support incremental development
- prioritize practical usefulness
