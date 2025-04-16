from memory_system import MemorySystem
import time

def run_tests():
    memsys = MemorySystem()

    print("=== Storing memories ===")
    memsys.store(
        event_type="wolf encounter",
        context="forest edge",
        emotion="fear",
        importance=0.8,
        outcome="ran away",
        tags=["danger", "animal", "wolf"]
    )

    memsys.store(
        event_type="ate berries",
        context="north hill",
        emotion="joy",
        importance=0.4,
        outcome="satisfied",
        tags=["food", "foraging"]
    )

    memsys.store(
        event_type="campfire talk",
        context="village center",
        emotion="trust",
        importance=0.6,
        outcome="learned new info",
        tags=["social", "npc"]
    )

    memsys.store(
        event_type="ambushed by bandit",
        context="mountain trail",
        emotion="anger",
        importance=0.9,
        outcome="injured",
        tags=["danger", "npc", "bandit"]
    )

    print(f"\nMemory Summary: {memsys}")

    print("\n=== Query: danger ===")
    danger_memories = memsys.query("danger")
    for mem in danger_memories:
        print(f"- {mem.event_type} ({mem.emotion}) at {mem.timestamp}")

    print("\n=== Query: food ===")
    food_memories = memsys.query("food")
    for mem in food_memories:
        print(f"- {mem.event_type} ({mem.emotion})")

    print("\n=== Evaluate Experience: npc ===")
    sentiment_npc = memsys.evaluate_experience("npc")
    print(f"Sentiment toward NPCs: {sentiment_npc}")

    print("\n=== Evaluate Experience: wolf ===")
    sentiment_wolf = memsys.evaluate_experience("wolf")
    print(f"Sentiment toward wolves: {sentiment_wolf}")

    print("\n=== Evaluate Experience: foraging ===")
    sentiment_forage = memsys.evaluate_experience("foraging")
    print(f"Sentiment toward foraging: {sentiment_forage}")

    print("\n=== Simulating Memory Decay ===")
    print("Waiting 2 seconds...")
    time.sleep(2)
    memsys.age_memories()
    print(f"After aging: {memsys}")

if __name__ == "__main__":
    run_tests()
