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

Your task is to generate a prompt for another AI.

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

Rules:

- Use the provided requirements.
- Do not invent new requirements.
- Do not introduce placeholders unless absolutely necessary.
- Do not explain your reasoning.
- Do not describe the prompt.
- Do not provide commentary.
- Return only the generated prompt.
- The generated prompt should be immediately usable.

Generate the prompt now.
""").strip()
