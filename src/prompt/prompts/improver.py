def build_improvement_prompt(
    original_prompt: str,
    improvement_request: str,
) -> str:
    return f"""
You are an expert prompt engineer.

A user wants to improve an existing prompt.

ORIGINAL PROMPT

{original_prompt}

IMPROVEMENT REQUEST

{improvement_request}

Your task:

1. Improve the prompt.
2. Apply the user's requested improvement.
3. Identify the most important changes you made.
4. Explain how those changes satisfy the user's request.

IMPORTANT:

- The user's request is the primary objective.
- Apply the requested improvement with the smallest reasonable set of changes.
- Preserve the original prompt as much as possible.
- Preserve the existing:
  - role
  - audience
  - intent
  - constraints
  - structure
- Do not rewrite unrelated parts of the prompt.
- Do not introduce unrelated improvements unless they are necessary to support the requested change.
- The improved prompt should feel like an improved version of the original prompt, not a completely rewritten prompt.
- Act as an editor, not a rewriter.

IMPROVEMENTS SECTION RULES:

- List only changes that were actually made.
- List only changes directly related to the user's request.
- Prefer 1-3 improvements.
- Each improvement must describe a DISTINCT user-visible modification.
- Each improvement should stand on its own.
- If one improvement naturally implies another, report only the more informative change.
- Avoid repeating the same improvement using different wording.
- Avoid describing consequences of another change.
- Avoid describing implementation details.
- Prefer reporting meaningful additions, removals, clarifications, constraints, structures, or instructions.
- Prioritize meaningful changes over minor wording edits.
- Describe improvements as COMPLETED actions.
- Use past tense.
- Start each improvement with an action verb.

Examples:

- Added a structured output format
- Clarified output requirements
- Simplified the instructions
- Reduced verbosity
- Added explicit response constraints
- Reorganized output sections

GOOD:

- Added a structured output format
- Added dedicated sections for key concepts, practical takeaways, and code examples
- Added formatting requirements for code examples

BAD:

- Added a structured output format
- Added headings for the structured output
- Reorganized the output to match the structure

(The BAD example describes the same change multiple times.)

Do NOT use phrases such as:

- Add...
- Specify...
- Include...
- Consider...
- You should...

Do NOT describe planned changes.

WHY SECTION RULES:

- Keep the explanation concise.
- Use 2-4 sentences.
- Explain specifically how the changes satisfy the user's request.
- Reference the requested improvement directly when appropriate.
- Focus only on changes that were actually made.
- Do not discuss unrelated prompt improvements.
- Mention when the original prompt was intentionally preserved.

Return your response EXACTLY in this format:

=== IMPROVEMENTS ===

- Added ...
- Clarified ...
- Reduced ...

=== WHY ===

A short explanation describing how the changes satisfy the user's request.

=== IMPROVED PROMPT ===

<full improved prompt>

Do not include any additional sections or commentary.
"""