# Mock EmotionSystem for testing
class MockEmotionSystem:
    def __init__(self, emotions):
        self.emotions = emotions  # Dict[str, float]

    def get_emotion_level(self, emotion):
        return self.emotions.get(emotion, 0.0)


# Mock MemorySystem for testing
class MockMemorySystem:
    def reason_about_goal(self, goal_name):
        # Simplified logic: add a memory-based modifier to urgency
        if goal_name == "stay_safe":
            return 0.2  # Memory of danger increases urgency
        elif goal_name == "explore":
            return -0.1  # Past risks make exploring less desirable
        return 0.0


# Setup
from logic_system import Goal, Action, LogicSystem

# Define personality profile (how emotions impact decisions)
personality = {
    "fear": 0.8,
    "joy": 0.4,
    "trust": 0.6
}

# Goals
goals = [
    Goal("stay_safe", base_urgency=0.5, related_emotions=["fear"]),
    Goal("explore", base_urgency=0.3, related_emotions=["joy"]),
    Goal("socialize", base_urgency=0.2, related_emotions=["trust"])
]

# Actions
actions = [
    Action("run_away", associated_goals=["stay_safe"]),
    Action("wander", associated_goals=["explore"]),
    Action("talk_to_npc", associated_goals=["socialize"])
]

# Context: All actions are feasible for this test
context_inputs = {}

# Emotion levels
emotions = {
    "fear": 0.6,
    "joy": 0.4,
    "trust": 0.7
}

# Instantiate system
logic_system = LogicSystem(
    goals=goals,
    actions=actions,
    memory_system=MockMemorySystem(),
    emotion_system=MockEmotionSystem(emotions),
    personality_profile=personality
)

# Run decision logic
action = logic_system.update(context_inputs)
print("Selected Action:", action)

# Optional: Print evaluated goals for transparency
print("\nGoal Evaluations:")
for goal in goals:
    print(goal)
