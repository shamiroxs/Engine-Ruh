from emotion_system import EmotionSystem

# Initialize EmotionSystem with a low decay rate (for future use)
emotion_system = EmotionSystem(decay_rate=0.05)

# Set up personality modifiers
emotion_system.personality_modifiers = {
    "fear_sensitivity": 1.5,
    "joy_sensitivity": 0.8
}

# Apply some emotions
emotion_system.apply_emotion("fear", 0.2)   # Expect 0.2 * 1.5 = 0.3
emotion_system.apply_emotion("joy", 0.5)    # Expect 0.5 * 0.8 = 0.4
emotion_system.apply_emotion("fear", 0.5)   # Should add more fear, total capped at 1.0
emotion_system.apply_emotion("trust", 0.7)  # No modifier, so stays at 0.7

# Print out the current emotional state
print("Current Emotions:")
for emotion, intensity in emotion_system.current_emotions.items():
    print(f"  {emotion}: {intensity:.2f}")

# Print out emotion history
print("\nEmotion History:")
for timestamp, emotion, intensity in emotion_system.emotion_history:
    print(f"  [{timestamp:.2f}] {emotion} +{intensity:.2f}")
    
print("\nDecaying emotions...")
emotion_system.decay_emotions()

print("\nAfter Decay:")
for emotion, intensity in emotion_system.current_emotions.items():
    print(f"  {emotion}: {intensity:.2f}")

dominant = emotion_system.get_dominant_emotion()
print(f"\nDominant Emotion: {dominant}")
