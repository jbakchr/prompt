from textwrap import dedent


def build_prompt(
    goal: str,
    audience: str,
    role: str,
    instructions: str,
    output_format: str,
) -> str:
    sections = []

    if role:
        sections.append(
            f"You are a {role}."
        )

    if goal:
        if audience:
            sections.append(
                f"{goal} for {audience}."
            )
        else:
            sections.append(goal)

    if instructions:
        sections.append(
            f"Instructions:\n{instructions}"
        )

    if output_format:
        sections.append(
            f"Output Format:\n{output_format}"
        )

    return dedent(
        "\n\n".join(sections)
    ).strip()