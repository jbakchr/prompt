# prompts/improvement_parser.py

from prompt.models.improvement_result import (
    ImprovementResult,
)


def parse_improvement_result(
    response: str,
) -> ImprovementResult:
    improvements = ""
    why = ""
    prompt = ""

    sections = response.split(
        "=== "
    )

    for section in sections:

        if section.startswith(
            "IMPROVEMENTS ==="
        ):
            improvements = (
                section.replace(
                    "IMPROVEMENTS ===",
                    "",
                    1,
                ).strip()
            )

        elif section.startswith(
            "WHY ==="
        ):
            why = (
                section.replace(
                    "WHY ===",
                    "",
                    1,
                ).strip()
            )

        elif section.startswith(
            "IMPROVED PROMPT ==="
        ):
            prompt = (
                section.replace(
                    "IMPROVED PROMPT ===",
                    "",
                    1,
                ).strip()
            )

    return ImprovementResult(
        improvements=improvements,
        why=why,
        prompt=prompt,
    )