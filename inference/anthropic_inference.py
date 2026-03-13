import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-haiku-4-5",
  max_tokens=256,
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }]
)
print(message.content[0].text)