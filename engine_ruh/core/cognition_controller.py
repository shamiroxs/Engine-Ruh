from memory_system import MemorySystem
from emotion_system import EmotionSystem
from instinct_system import InstinctSystem
from logic_system import LogicSystem, Goal, Action
from decision_manager import DecisionManager


class CognitionController:
    def __init__(self, npc_id):
        self.npc_id = npc_id
        self.memory = MemorySystem(npc_id)
        self.emotion = EmotionSystem(npc_id)
        self.instinct = InstinctSystem(npc_id)
        
        goals = [
        Goal(name="Survival", base_urgency=5.0, related_emotions=["fear"]),
        Goal(name="Socialize", base_urgency=2.5, related_emotions=["joy"]),
	]
        
        actions = [
    	Action(name="run_away", associated_goals=["Survival"]),
    	Action(name="talk", associated_goals=["Socialize"]),
	]
	
        personality = {"fear": 0.8, "joy": 0.4}
	
        self.logic = LogicSystem(goals, actions, self.memory, self.emotion, personality)
        self.decision_manager = DecisionManager(
    	memory_system=self.memory,
    	emotion_system=self.emotion,
    	instinct_system=self.instinct,
    	logic_system=self.logic,
    	personality=personality  # reuse the same personality dict from above
	)
    def perceive(self, external_inputs):
        """
        Accepts environmental stimuli and updates memory, emotions, and instinct triggers.
        """
        self.memory.record_perception(external_inputs)
        
        for emotion, intensity in external_inputs.items():
           self.emotion.update_emotion(emotion, intensity)
        
        
        self.instinct.receive_inputs(external_inputs)

    def evaluate(self):
        """
        Core cognition flow: instinct -> emotion -> logic -> decision.
        """
        # 1. Instinct check
        instinct_action = self.instinct.evaluate()
        if instinct_action:
            return self.decision_manager.execute(instinct_action, source="Instinct")

        # 2. Emotion-modulated context (optional feedback loop)
        emotional_state = self.emotion.get_current_state()

        # 3. Logic reasoning
        logic_action = self.logic.evaluate(
            memory=self.memory,
            emotions=emotional_state
        )
        if logic_action:
            return self.decision_manager.execute(logic_action, source="Logic")

        # 4. Fallback / idle behavior
        return self.decision_manager.execute("idle", source="Default")

    def update(self, external_inputs):
        """
        Main loop tick for this NPC. Called every frame/tick.
        """
        self.perceive(external_inputs)
        return self.evaluate()
