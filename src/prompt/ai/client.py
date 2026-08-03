from ollama import chat


class AIClient:
    def __init__(
        self,
        model: str = "qwen3:8b",
    ) -> None:
        self.model = model

    def generate_prompt(
        self,
        request: str,
    ) -> str:
        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": request,
                    }
                ],
            )

            return response["message"]["content"]

        except Exception as error:
            raise RuntimeError(
                f"Failed to generate response: {error}"
            )