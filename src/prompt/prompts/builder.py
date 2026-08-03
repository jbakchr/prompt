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

        Generate a high-quality prompt based on the following requirements.

        Goal:
        {goal}

        Audience:
        {audience}

        Role:
        {role}

        Additional Instructions:
        {instructions}

        Output Format:
        {output_format}

        Guidelines:

        - Generate a prompt that can be used directly with an AI model.
        - Include role information when relevant.
        - Include audience information when relevant.
        - Add useful structure if appropriate.
        - Keep the prompt clear and concise.
        - Avoid unnecessary verbosity.
        - Return only the generated prompt.
        """
    ).strip()
