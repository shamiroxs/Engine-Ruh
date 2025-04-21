from datetime import datetime, timedelta
import math

class EmotionSystem:
    def __init__(self, personality_traits=None):
        self.current_emotions = {}  # { 'fear': {'intensity': 0.8, 'timestamp': datetime(...)}, ... }
        self.emotion_history = []
        self.max_history_size = 100
        self.personality_traits = personality_traits or {
            'sensitivity_fear': 1.0,
            'sensitivity_joy': 1.0,
            'forgetfulness': 1.0  # higher = forgets faster
        }

    def get_emotion_profile(self):
        """Returns decayed emotional state."""
        decayed_profile = {}
        now = datetime.utcnow()
        forgetfulness = self.personality_traits.get('forgetfulness', 1.0)
        decay_rate = 0.1 * forgetfulness  # Base decay rate modulated by forgetfulness

        for emotion, data in self.current_emotions.items():
            elapsed = (now - data['timestamp']).total_seconds()
            decayed_intensity = data['intensity'] * math.exp(-decay_rate * elapsed)
            if decayed_intensity > 0.01:  # threshold to remove stale emotions
                decayed_profile[emotion] = round(decayed_intensity, 3)

        return decayed_profile

    def adjust_for_personality(self, emotion_name: str, intensity: float) -> float:
        modifier = self.personality_traits.get(f"sensitivity_{emotion_name}", 1.0)
        return intensity * modifier

    def update_emotion(self, emotion_name: str, raw_intensity: float):
        """Applies new emotion and adjusts existing intensity."""
        now = datetime.utcnow()
        adjusted = self.adjust_for_personality(emotion_name, raw_intensity)
        previous = self.current_emotions.get(emotion_name)

        if previous:
            # Additive blending of new emotion
            elapsed = (now - previous['timestamp']).total_seconds()
            forgetfulness = self.personality_traits.get('forgetfulness', 1.0)
            decay_rate = 0.1 * forgetfulness
            decayed = previous['intensity'] * math.exp(-decay_rate * elapsed)
            new_intensity = min(decayed + adjusted, 1.0)
        else:
            new_intensity = min(adjusted, 1.0)

        self.current_emotions[emotion_name] = {
            'intensity': new_intensity,
            'timestamp': now
        }

        self.record_emotion_history(emotion_name, new_intensity)

    def record_emotion_history(self, emotion_name: str, intensity: float):
        """Logs emotion events with intensity. Older entries are trimmed."""
        timestamp = datetime.utcnow().isoformat()
        self.emotion_history.append((timestamp, emotion_name, intensity))

        if len(self.emotion_history) > self.max_history_size:
            self.emotion_history.pop(0)

    def get_emotion_level(self, emotion_name: str) -> float:
        """Returns decayed intensity of a specific emotion."""
        profile = self.get_emotion_profile()
        return profile.get(emotion_name, 0.0)
