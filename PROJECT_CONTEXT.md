# PROJECT_CONTEXT.md

# prompt – Project Context

## 🧠 What This Project Is

prompt is a CLI for creating, reviewing, and improving AI prompts.

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
- Prompt scoring systems

The goal is:

👉 Generate useful prompts quickly.

👉 Help users improve prompts iteratively.

Success is measured by questions such as:

- Does `prompt create` generate useful prompts?
- Does `prompt review` provide useful feedback?
- Does `prompt improve` make prompts noticeably better?
- Would I actually use this from my terminal?

---

## 🧭 Development Philosophy

This project should be developed incrementally.

Start simple.

Validate usefulness.

Improve based on real usage.

The progression should be:

```text
Create
↓
Save
↓
Review
↓
Improve
↓
Better Workflow
↓
Prompt Library
```

rather than:

```text
Add lots of features
↓
Hope people use them
```

Every new feature should justify its existence through practical usefulness.

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

The user may optionally save the prompt.

Status:

✅ Implemented

---

### review

Purpose:

Review an existing prompt and identify opportunities for improvement.

Command:

```bash
prompt review <prompt-file>
```

The AI provides:

- Strengths
- Weaknesses
- Suggestions

The goal is constructive feedback, not scoring prompts.

Reviews are rendered as Markdown within a Rich panel.

Status:

✅ Implemented

---

### improve

Purpose:

Improve an existing prompt.

Command:

```bash
prompt improve <prompt-file>
```

The CLI should:

- Read an existing prompt
- Ask what should be improved
- Send prompt + improvement request to an AI
- Generate an improved prompt
- Display the improved prompt
- Offer to save the result

Examples:

- Too verbose
- Too short
- Wrong audience
- Missing structure
- Produces too much code
- Produces too little code

Status:

🚧 Planned

---

## 📋 Prompt Creation Philosophy

Good prompts often include more than just a task.

For example:

Instead of:

```text
Summarize this article.
```

A stronger prompt might include:

- A role
- An audience
- Additional instructions
- Output formatting requirements

The CLI helps users think about this context.

The quality of the generated prompt is strongly influenced by the quality of the information collected from the user.

---

## ✅ Current Project Status

### Implemented

✅ Typer CLI

✅ Rich terminal UI

✅ AI-powered prompt generation

✅ Guided question flow

✅ Question panels

✅ Tips and examples

✅ Question numbering

✅ AI generation spinner

✅ Generated prompt display panel

✅ Prompt saving

✅ Prompt storage

✅ Prompt review

✅ Markdown-rendered review output

✅ Suggested next steps

✅ Workflow-oriented command structure

✅ PromptRequirements dataclass

---

### Current Prompt Workflow

```text
prompt create
    ↓
Generate Prompt
    ↓
Display Prompt
    ↓
Save Prompt (Optional)
    ↓
prompt review
    ↓
Review Feedback
    ↓
prompt improve (future)
```

---

## 🏛 Current Architecture

Current project structure:

```text
src/prompt
├── ai
│   └── client.py
├── commands
│   ├── create.py
│   ├── improve.py
│   ├── review.py
│   └── questions.py
├── models
│   └── prompt_requirements.py
├── prompts
│   ├── builder.py
│   ├── improver.py
│   └── reviewer.py
├── storage
│   └── prompts.py
└── main.py
```

Architectural responsibilities:

### commands/

User-facing workflows.

Commands should read almost like user stories.

Example:

```python
def create():
    display_create_intro()

    requirements = collect_prompt_requirements()

    generated_prompt = generate_prompt(
        requirements
    )

    display_generated_prompt(
        generated_prompt
    )

    maybe_save_prompt(
        generated_prompt
    )

    display_next_steps()
```

Commands should express workflow, not implementation details.

---

### prompts/

Responsible for constructing prompts sent to AI models.

Examples:

- prompt generation
- prompt review
- prompt improvement

---

### ai/

Responsible for communicating with AI models.

---

### storage/

Responsible for prompt persistence and retrieval.

---

### models/

Contains simple data structures used throughout the application.

---

## 🔍 Key Insights Discovered

### 1. Good Questions Lead To Better Prompts

The quality of generated prompts depends heavily on the quality of answers provided by the user.

Question tips and examples significantly improved output quality.

---

### 2. Prompt Generation Is An AI Task

Originally prompt creation used templates.

Switching to AI-generated prompts produced significantly better results.

Current preferred model:

```text
qwen3:8b
```

---

### 3. Examples Matter

Providing examples dramatically improved prompt quality.

The AI now generates useful prompt templates rather than instructions about prompts.

---

### 4. UX Matters

The quality of the experience improved significantly through:

- Rich panels
- Tips
- Examples
- Visual spacing
- Spinners
- Markdown rendering

The project is not only about AI quality.

It is also about creating a pleasant workflow.

---

### 5. Review Before Improve

An important discovery:

```text
Create
↓
Review
↓
Improve
```

feels more natural than:

```text
Create
↓
Improve
↓
Review
```

Review helps users understand what should be improved.

The review workflow now forms the foundation for future improvement workflows.

---

### 6. Workflow Clarity Matters

Commands become easier to maintain when they describe workflow rather than implementation.

Good:

```python
create()
    ↓
collect requirements
    ↓
generate prompt
    ↓
display prompt
```

Less desirable:

```python
create()
    ↓
100 lines of mixed responsibilities
```

---

## 🧭 Current Direction

Current priority:

```text
Prompt Improvement
↓
Better Workflow
↓
Prompt Library
```

The core creation, saving, and review workflows have been validated.

The next goal is helping users improve prompts using AI-assisted refinement.

---

## 🚫 Non-Goals

At this stage:

- Web application
- User accounts
- Prompt marketplace
- Prompt sharing platform
- Prompt scoring systems
- Enterprise SaaS platform
- Complex prompt engineering frameworks

Focus remains:

👉 Create prompts

👉 Review prompts

👉 Improve prompts

---

## ✅ What Makes This Project Different

This is NOT:

👉 A prompt marketplace

👉 A prompt library platform

👉 A prompt engineering course

👉 A prompt scoring system

This IS:

👉 A practical CLI for prompt creation, review, and improvement

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
- built from real prompt engineering experience
- designed around iterative improvement

---

## 🚀 What I Want Help With In A New Chat

Help me:

- Design new commands
- Improve AI prompt generation
- Improve CLI UX
- Build prompt improvement workflows
- Keep the project focused
- Identify missing functionality
- Improve project structure where beneficial
- Avoid overengineering

Avoid:

- unnecessary complexity
- feature creep
- enterprise architecture
- turning the project into a platform

---

## 🔑 Most Important Rule

Always remember:

The goal is not to generate perfect prompts.

The goal is to generate useful prompts quickly and help users improve them over time.