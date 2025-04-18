from typing import List, Optional, Dict
from instincts import InstinctRule, InstinctResponse

class InstinctSystem:
    def __init__(self, instincts: List[InstinctRule]):
        self.instincts = instincts

    def evaluate(self, context: Dict) -> Optional[InstinctResponse]:
        """
        Evaluates the instincts against the current context.
        
        Args:
            context (dict): The current context of the NPC including emotions, memory, environment, etc.

        Returns:
            InstinctResponse or None: Returns the instinct response if an instinct is triggered, else None.
        """
        for instinct in self.instincts:
            if instinct.trigger_condition(context):
                return InstinctResponse(
                    action=instinct.response_action,
                    priority=instinct.priority,
                    override=instinct.override
                )
        return None
