from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import ollama


@dataclass
class Response:
    thinking: Optional[str] = None
    answer: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None


class Agent:
    def __init__(
        self,
        name: str = "Agent",
        tools: Optional[List[Dict[str, Any]]] = None,
        model: str = "ministral-3:3b-instruct-2512-q4_K_M",
        system_prompt: Optional[str] = None,
        base_url: str = "http://localhost:11434",
        debug: bool = False
    ):
        self.name = name
        self.tools = tools or []
        self.model = model
        self.debug = debug
        self.system_prompt = open(system_prompt).read() if system_prompt else None
        self.ollama_client = ollama.Client(host=base_url)

    def respond(self, prompt: str) -> Response:

        response = self.ollama_client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            tools=self.tools if self.tools else None
        )

        if self.debug:
            print("Raw response:", response)

        message = response.message

        tool_calls_dict = None
        if message.tool_calls:
            tool_calls_dict = [
                {
                    "id": call.id,  # type: ignore
                    "function": call.function.name,
                    "arguments": call.function.arguments
                }
                for call in message.tool_calls
            ]

        return Response(
            thinking=message.thinking,
            answer=message.content,
            tool_calls=tool_calls_dict
        )

agent = Agent(system_prompt="prompt.md")
print(agent.respond("what is the formula of gravity?"))