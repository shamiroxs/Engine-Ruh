import time

from collections import deque
from datetime import datetime

class MemoryEntry:
    def __init__(self, event_type, context, emotion, importance, outcome, tags=None):
        self.event_type = event_type
        self.context = context
        self.timestamp = datetime.now()
        self.emotion = emotion
        self.importance = importance  # 0.0 to 1.0
        self.outcome = outcome
        self.tags = tags or []  # Optional list of labels like ["danger", "wolf", "exploration"]

    def __repr__(self):
        return f"<MemoryEntry {self.event_type} [{self.emotion}] @ {self.timestamp}>"

class MemorySystem:
    def __init__(self, capacity: int = 10, decay_rate=0.01, memory_threshold=0.5):
        self.short_term_memory = deque()
        self.long_term_memory = []
        self.memory_decay_rate = decay_rate
        self.memory_threshold = memory_threshold
        self.capacity = capacity
        self.memory = []
    
    def remember(self, event: str):
        """Store a memory event, evict the oldest if capacity is exceeded."""
        if len(self.memory) >= self.capacity:
            self.memory.pop(0)  # Remove the oldest memory
        self.memory.append(event)

    def recall_recent_events(self):
        """Return the most recent memories."""
        return self.memory

    def clear_memory(self):
        """Clear all stored memories."""
        self.memory = []


    def store(self, event_type, context, emotion, importance, outcome, tags=None):
        memory = MemoryEntry(event_type, context, emotion, importance, outcome, tags)
        self.short_term_memory.append(memory)

        if importance >= self.memory_threshold:
            self.long_term_memory.append(memory)

    def query(self, keyword):
        """
        Query memories based on keyword in event_type, context, or tags.
        Results are sorted by importance (desc), then recency.
        """
        results = [
            mem for mem in self.long_term_memory
            if keyword in mem.event_type or keyword in mem.context or keyword in mem.tags
        ]
        return sorted(results, key=lambda mem: (mem.importance, mem.timestamp), reverse=True)

    def recall_recent(self, event_type):
        """
        Get recent memories of a certain event type from short-term memory.
        """
        return [
            mem for mem in self.short_term_memory
            if event_type in mem.event_type
        ]

    def evaluate_experience(self, related_to):
        """
        Analyze memory outcomes and emotional tone of past related experiences.
        Returns a simple sentiment analysis: 'positive', 'negative', or 'neutral'.
        """
        related = self.query(related_to)
        if not related:
            return "unknown"

        positive = 0
        negative = 0

        for mem in related:
            if mem.emotion in ['joy', 'trust', 'relief']:
                positive += mem.importance
            elif mem.emotion in ['fear', 'anger', 'disgust', 'sadness']:
                negative += mem.importance

        if positive > negative:
            return "positive"
        elif negative > positive:
            return "negative"
        else:
            return "neutral"

    def age_memories(self):
        """
        Decay short-term memories over time. Removes old low-importance entries.
        """
        current_time = datetime.now()
        for memory in list(self.short_term_memory):
            age_in_seconds = (current_time - memory.timestamp).total_seconds()
            if age_in_seconds > self.memory_decay_rate * 100:
                self.short_term_memory.remove(memory)

    def __str__(self):
        return f"Short-Term: {len(self.short_term_memory)} | Long-Term: {len(self.long_term_memory)}"
