from typing import List, Dict, Callable, Optional

# --- Support Classes ---

class Goal:
    def __init__(self, name: str, base_urgency: float, related_emotions: List[str]):
        self.name = name
        self.base_urgency = base_urgency
        self.current_urgency = base_urgency
        self.related_emotions = related_emotions
        self.is_active = True

    def __repr__(self):
        return f"Goal(name={self.name}, urgency={self.current_urgency:.2f})"


class Action:
    def __init__(self, name: str, associated_goals: List[str], requirements: Optional[Callable] = None):
        self.name = name
        self.associated_goals = associated_goals
        self.requirements = requirements  # A function or condition to check if action is possible

    def is_feasible(self, context: Dict) -> bool:
        if self.requirements:
            return self.requirements(context)
        return True

    def __repr__(self):
        return f"Action(name={self.name})"


# --- Logic System ---

class LogicSystem:
    def __init__(self, goals: List[Goal], actions: List[Action], memory_system, emotion_system, personality_profile: Dict):
        self.goals = goals
        self.actions = actions
        self.memory_system = memory_system
        self.emotion_system = emotion_system
        self.personality_profile = personality_profile
        self.contextual_inputs = {}

    def evaluate_goals(self):
        goal_scores = {}
        for goal in self.goals:
            if not goal.is_active:
                continue
            urgency = goal.base_urgency
            # Apply emotion influence
            for emotion in goal.related_emotions:
                level = self.emotion_system.get_emotion_level(emotion)
                urgency += level * self.personality_profile.get(emotion, 0.5)  # personality modulates influence
            # Apply memory influence
            memory_score = self.memory_system.reason_about_goal(goal.name)
            urgency += memory_score
            goal.current_urgency = urgency
            goal_scores[goal.name] = urgency
        return goal_scores

    def resolve_conflicts(self, goal_scores):
        # Simple resolution: take the goal with the highest score
        if not goal_scores:
            return None
        return max(goal_scores, key=goal_scores.get)

    def decide_next_action(self):
        goal_scores = self.evaluate_goals()
        top_goal_name = self.resolve_conflicts(goal_scores)
        if not top_goal_name:
            return None
        feasible_actions = [a for a in self.actions if top_goal_name in a.associated_goals and a.is_feasible(self.contextual_inputs)]
        return feasible_actions[0] if feasible_actions else None

    def update(self, context_inputs: Dict):
        self.contextual_inputs = context_inputs
        return self.decide_next_action()
