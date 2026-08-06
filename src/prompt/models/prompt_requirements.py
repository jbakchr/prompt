from dataclasses import dataclass


@dataclass
class PromptRequirements:
    goal: str
    audience: str
    role: str
    instructions: str
    output_format: str