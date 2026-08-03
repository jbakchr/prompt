from textwrap import dedent


def build_prompt_generation_request(
    goal: str,
    audience: str,
    role: str,
    instructions: str,
    output_format: str,
) -> str:
    audience = audience or "Not specified"
    role = role or "Not specified"
    instructions = instructions or "Not specified"
    output_format = output_format or "Not specified"

    return dedent(
        f"""
You are an expert prompt engineer.

Your task is to generate the final prompt that will be used directly with another AI.

The generated prompt should be practical, well-structured, and immediately usable.

Requirements:

Goal:
{goal}

Audience:
{audience}

Role:
{role}

Instructions:
{instructions}

Output Format:
{output_format}

The generated prompt should include:

- The specified role (when provided)
- A clear task description
- Any additional instructions
- Output formatting requirements (when provided)

Prompt Structure:

1. Role statement
2. Task description
3. Additional instructions
4. Output requirements
5. Input placeholder (if needed)

Example:

You are an experienced Python developer.

Summarize the following article for Python developers.

Focus on:
- Key concepts
- Practical takeaways

Use bullet points.

Article:

{{article}}

Rules:

- Return ONLY the generated prompt.
- Do NOT explain the prompt.
- Do NOT describe the prompt.
- Do NOT add commentary.
- Do NOT introduce new requirements.
- Do NOT invent topics.
- Do NOT invent placeholders unless they are required as input.
- Use only the requirements provided by the user.
- Do not add additional instructions that were not requested.
- The generated prompt should resemble the structure and style of the example above.
- Start directly with the generated prompt.
- The generated prompt must be ready to copy and use immediately.

Generate the prompt now.
"""
    ).strip()