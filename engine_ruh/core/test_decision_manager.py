# test_decision_manager.py

from emotion_system import EmotionSystem
from memory_system import MemorySystem
from logic_system import LogicSystem, Goal, Action
from instinct_system import InstinctSystem, Instinct, InstinctResponse
from decision_manager import DecisionManager

# ----- Setup Systems -----

# Personality traits for the NPC
personality = {
    "curiosity": 0.6,
    "sociability": 0.5,
    "caution": 0.8,
}

# Instantiate systems
memory_system = MemorySystem(capacity=10)
emotion_system = EmotionSystem()
logic_system = LogicSystem()

# Register goals in logic
logic_system.add_goal(Goal(name="explore", base_urgency=0.4))
logic_system.add_goal(Goal(name="stay_safe", base_urgency=0.7))
logic_system.add_goal(Goal(name="socialize", base_urgency=0.5))

# Register actions for goals
logic_system.add_action(Action(name="wander", goal="explore"))
logic_system.add_action(Action(name="run_away", goal="stay_safe"))
logic_system.add_action(Action(name="talk", goal="socialize"))

# Define instincts
instincts = [
    Instinct(
        trigger_condition=lambda ctx: ctx["emotions"].get("fear", 0) > 0.7,
        response=InstinctResponse(action="run_away", priority=2, override=True)
    )
]
instinct_system = InstinctSystem(instincts)

# Create decision manager
decision_manager = DecisionManager(
    memory_system=memory_system,
    emotion_system=emotion_system,
    instinct_system=instinct_system,
    logic_system=logic_system,
    personality=personality
)

# ----- Test Run -----

# Apply a strong fear emotion to trigger instinct
emotion_system.apply_emotion("fear", 1.0)

# Simulate environmental input
environment = {
    "threat_nearby": True,
    "time_of_day": "night",
    "other_npcs": ["npc_1", "npc_2"]
}

# Run decision manager
final_action = decision_manager.decide_action(environment)
print(f"\nFinal Chosen Action: {final_action}")
