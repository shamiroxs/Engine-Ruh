import random
from cognition_controller import CognitionController

# Instantiate the NPC brain
npc_brain = CognitionController(npc_id="npc_001")

# Define a series of simulated world states over time
simulated_ticks = [
    {"hunger": 10, "threat_level": 0, "opportunities": ["explore", "rest"]},
    {"hunger": 40, "threat_level": 0, "opportunities": ["gather", "rest"]},
    {"hunger": 70, "threat_level": 0, "opportunities": ["gather", "hunt"]},
    {"hunger": 90, "threat_level": 20, "opportunities": ["hunt", "flee"]},
    {"hunger": 50, "threat_level": 80, "opportunities": ["flee", "hide"]},
    {"hunger": 30, "threat_level": 10, "opportunities": ["explore", "rest"]},
]

# Run mock game loop
print("=== AI Simulation Start ===")
for tick_num, inputs in enumerate(simulated_ticks, start=1):
    print(f"\n--- Tick {tick_num} ---")
    print(f"Inputs: {inputs}")

    npc_brain.update(inputs)

print("\n=== AI Simulation End ===")
