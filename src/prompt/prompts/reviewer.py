def build_prompt_review_request(
    prompt: str,
) -> str:
    """
    Build a review request
    for the AI model.
    """

    return f"""
Review the following AI prompt.

Provide feedback using exactly
these sections:

# ✅ STRENGTHS

# ⚠️ WEAKNESSES

# 💡 SUGGESTIONS

Be specific.

Do not score the prompt.

Do not assign a rating.

Prompt:

{prompt}
"""