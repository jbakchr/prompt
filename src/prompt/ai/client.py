from ollama import chat

# qwen3:8b

# gpt-oss:120b-cloud

class AIClient:
    def __init__(
        self,
        model: str = "gpt-oss:120b-cloud",
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