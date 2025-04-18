from typing import Callable, Dict, Any
from dataclasses import dataclass

@dataclass
class InstinctResponse:
    action: str
    priority: int
    override: bool = False

@dataclass
class InstinctRule:
    name: str
    priority: int  # e.g., 0 = subtle, 1 = suggestive, 2 = override
    trigger_type: str  # "internal" or "external"
    trigger_condition: Callable[[Dict[str, Any]], bool]
    response_action: str
    override: bool = False
