import os
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing GROQ_API_KEY environment variable"
    )

client = Groq(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="openai/gpt-oss-120b",
    temperature=0.7,
    stop=None,
    max_completion_tokens=512,
    reasoning_effort="low",
    reasoning_format="parsed",
    include_reasoning=True,
    stream=False,
)

print(chat_completion.choices[0].message)