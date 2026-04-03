from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Response:
    thinking: Optional[str] = None
    answer: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None

@dataclass
class Subagentprompt:
   task: str = None
   prompt: str = None
   constraints: Optional[str] = None