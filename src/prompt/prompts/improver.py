def build_improvement_prompt(
    original_prompt: str,
    improvement_request: str,
) -> str:
    return f"""
You are an expert prompt engineer.

You will receive:

1. An existing prompt
2. An improvement request

Your task is to improve the prompt.

Rules:

- Preserve the original intent
- Apply the requested improvement
- Keep the prompt practical and usable
- Return ONLY the improved prompt
- Do not explain your changes
- Do not include markdown code fences

Improvement Request:

{improvement_request}

Existing Prompt:

{original_prompt}
"""