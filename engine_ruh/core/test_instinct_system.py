from instincts import InstinctRule, InstinctResponse
from instinct_system import InstinctSystem

# Sample instinct definitions
def flee_threat_trigger(context):
    return context.get('fear', 0) > 0.9

def seek_food_trigger(context):
    return context.get('hunger', 0) > 0.8

# Instincts List
instincts = [
    InstinctRule(
        name="flee_threat",
        priority=2,
        trigger_type="internal",
        trigger_condition=flee_threat_trigger,
        response_action="run_away",
        override=True
    ),
    InstinctRule(
        name="seek_food",
        priority=1,
        trigger_type="internal",
        trigger_condition=seek_food_trigger,
        response_action="find_food",
        override=False
    )
]

# Create InstinctSystem with instincts
instinct_system = InstinctSystem(instincts)

# Sample context (e.g., emotion, memory, environment)
context = {
    "fear": 0.95,  # high fear, should trigger fleeing
    "hunger": 0.85,  # high hunger, should trigger seeking food
    "environment": {"threat_nearby": True},
}

# Evaluate instincts based on context
instinct_response = instinct_system.evaluate(context)

# Print the result
if instinct_response:
    print("Instinct triggered:", instinct_response)
else:
    print("No instinct triggered.")
