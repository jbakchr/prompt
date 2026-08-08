# models/improvement_result.py

from dataclasses import dataclass


@dataclass
class ImprovementResult:
    improvements: str
    why: str
    prompt: str