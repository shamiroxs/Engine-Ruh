import random
from datetime import datetime
from typing import List
from collections import deque


class MemoryEntry:
    def __init__(self, timestamp, description, emotion_tag=None, goal_tag=None, intensity=0.0):
        self.timestamp = timestamp
        self.description = description
        self.emotion_tag = emotion_tag
        self.goal_tag = goal_tag
        self.intensity = intensity  # Emotional intensity influences memory strength

    def __repr__(self):
        return f"<MemoryEntry {self.timestamp}: {self.description} (Emotion: {self.emotion_tag}, Intensity: {self.intensity})>"


class MemorySystem:
    def __init__(self,  npc_id, capacity=50):
    	self.npc_id = npc_id
    	self.capacity = capacity
    	self.memory = deque(maxlen=capacity)  # Automatically discards oldest if full
    	self.personality_traits = {
            "forgetfulness": 0.2  # 0.0 = perfect memory, 1.0 = very forgetful
        }

    def add_memory(self, description, emotion_tag=None, goal_tag=None, intensity=0.0):
        timestamp = datetime.utcnow().isoformat()
        entry = MemoryEntry(timestamp, description, emotion_tag, goal_tag, intensity)

        # Forgetfulness check (we might skip storing some low-intensity memories)
        forgetfulness = self.personality_traits.get("forgetfulness", 0.0)
        chance_to_forget = forgetfulness * (1.0 - intensity)
        if random.random() < chance_to_forget:
            return  # Memory was too weak and forgotten

        self.memory.append(entry)

    def recall_recent_events(self, limit: int = 5) -> List[MemoryEntry]:
        """Returns the most recent memory entries up to a limit."""
        return list(self.memory)[-limit:]

    def reason_about_goal(self, goal_name: str) -> float:
        """Estimates the relevance of a goal based on recent memory frequency."""
        recent = self.recall_recent_events(20)
        related = [entry for entry in recent if entry.goal_tag == goal_name]
        if not recent:
            return 0.0
        return len(related) / len(recent)  # Score from 0.0 to 1.0
        
    def record_perception(self, external_inputs: dict):
        """
        Basic interpretation of inputs to memory entries.
        Can be extended with goal/emotion tagging logic.
        """
        for key, value in external_inputs.items():
            description = f"Perceived {key}: {value}"
            self.add_memory(description=description, goal_tag=key)

