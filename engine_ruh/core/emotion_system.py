from typing import Dict, List, Tuple, Optional
import time

class EmotionSystem:
    """
    Tracks and updates the NPC's emotional state over time.
    Influences decision-making and behavior based on dominant emotions.
    """

    def __init__(self, decay_rate: float = 0.01, max_emotion_value: float = 1.0):
        self.current_emotions: Dict[str, float] = {}
        self.decay_rate: float = decay_rate
        self.max_emotion_value: float = max_emotion_value
        self.emotion_threshold: float = 0.05  # Below this, emotion is considered inactive
        self.emotion_history: List[Tuple[float, str, float]] = []
        self.personality_modifiers: Dict[str, float] = {}  # Optional traits like fear_sensitivity

    def apply_emotion(self, emotion: str, intensity: float):
    	"""
    	Applies a new emotion to the system, increasing its intensity.
    	Intensity is adjusted via personality modifiers and capped at max_emotion_value.
    	"""
    	if intensity <= 0:
    	    return  # Skip non-positive values

    	# Apply personality modifier if available
    	modifier_key = f"{emotion}_sensitivity"
    	if modifier_key in self.personality_modifiers:
    	    intensity *= self.personality_modifiers[modifier_key]

    	# Add to current emotion intensity
    	current = self.current_emotions.get(emotion, 0.0)
    	updated = min(current + intensity, self.max_emotion_value)
    	self.current_emotions[emotion] = updated

    	# Record to history
    	self.record_emotion_history(emotion, intensity)


    def decay_emotions(self):
        """
        Gradually reduces emotional intensities over time.
        """
        pass

    def get_dominant_emotion(self) -> Optional[str]:
        """
        Returns the most intense current emotion above the threshold, or None.
        """
        pass

    def get_emotion_profile(self) -> Dict[str, float]:
        """
        Returns the current state of all emotions (filtered or full).
        """
        pass

    def adjust_for_personality(self, emotion: str, intensity: float) -> float:
        """
        Modifies incoming emotion based on character's personality sensitivity/resistance.
        """
        pass

    def record_emotion_history(self, emotion: str, intensity: float):
        """
        Stores emotion change in history log for tracking or learning.
        """
        pass
