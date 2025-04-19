from typing import Optional

class DecisionManager:
    def __init__(self, memory_system, emotion_system, instinct_system, logic_system, personality):
        self.memory_system = memory_system
        self.emotion_system = emotion_system
        self.instinct_system = instinct_system
        self.logic_system = logic_system
        self.personality = personality  # Static NPC traits

    def collect_context(self, environment_data: dict) -> dict:
        # Build a context dictionary to share across all systems
        return {
            "emotions": self.emotion_system.get_emotion_state(),
            "memory": self.memory_system.recall_recent_events(),
            "environment": environment_data,
            "personality": self.personality,
        }

    def decide_action(self, environment_data: dict) -> Optional[str]:
        context = self.collect_context(environment_data)

        # Step 1: Instincts
        instinct_response = self.instinct_system.evaluate(context)
        if instinct_response:
            print(f"[DecisionManager] Instinct triggered: {instinct_response}")
            if instinct_response.override:
                return instinct_response.action

        # Step 2: Logic-based decision
        logic_action = self.logic_system.select_action(context)
        print(f"[DecisionManager] Logic selected: {logic_action}")

        # Step 3: Optional updates to memory or emotion based on chosen action
        # (Can be implemented later)

        return logic_action
