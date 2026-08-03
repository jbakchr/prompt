from prompt.ai.client import AIClient

client = AIClient()

response = client.generate(
    "Write a one sentence summary of Python."
)

print(response)