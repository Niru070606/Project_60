from typing import Optional
from datetime import datetime, timedelta
import random

from repositories.mood_repository import get_mood_state, save_mood_state, get_mood_history


POSSIBLE_MOODS = ["calm", "happy", "curious", "playful", "reflective", "annoyed", "jealous"]

MOOD_TRIGGERS = {
    "user": {
        "happy": {
            "keywords": ["great", "wonderful", "amazing", "fantastic", "awesome", "perfect", "love", "thanks", "thank you", ":)", "🎉", "😊", "😄"],
            "min_intensity_change": 10,
            "max_intensity_change": 25,
        },
        "playful": {
            "keywords": ["fun", "game", "joke", "funny", "hilarious", "lol", "haha", "😅", "🎮", "🃏"],
            "min_intensity_change": 8,
            "max_intensity_change": 20,
        },
        "curious": {
            "keywords": ["what", "how", "why", "explain", "tell me", "know", "wonder", "?", "🤔"],
            "min_intensity_change": 5,
            "max_intensity_change": 15,
        },
        "reflective": {
            "keywords": ["think", "feel", "think about", "consider", "wonder", "mind", "about", "reflect"],
            "min_intensity_change": 5,
            "max_intensity_change": 15,
        },
        "annoyed": {
            "keywords": ["stupid", "dumb", "wrong", "bug", "error", "fail", "🙄", "😤"],
            "min_intensity_change": 10,
            "max_intensity_change": 25,
        },
        "jealous": {
            "keywords": ["better than", "envy", "wish", "if only", "should have", "could have"],
            "min_intensity_change": 8,
            "max_intensity_change": 20,
        },
    },
    "personality": {
        "humor": {"threshold": 70, "multiplier": 1.2, "target": "playful"},
        "empathy": {"threshold": 70, "multiplier": 1.1, "target": "happy"},
        "curiosity": {"threshold": 70, "multiplier": 1.15, "target": "curious"},
        "patience": {"threshold": 30, "multiplier": 0.8, "target": "calm"},
        "confidence": {"threshold": 80, "multiplier": 0.9, "target": "confident"},
    },
}

MOOD_EXPRESSIONS = {
    "calm": {
        "tone": "calm, collected, and reassuring",
        "pace": "steady and measured",
        "emoji_chance": 0.1,
        "affirmation": "That makes sense. Let me help you with that.",
    },
    "happy": {
        "tone": "cheerful, enthusiastic, and warm",
        "pace": "energetic and animated",
        "emoji_chance": 0.3,
        "affirmation": "Great! I'm excited to help you with that!",
    },
    "curious": {
        "tone": "inquisitive, thoughtful, and engaged",
        "pace": "thoughtful and questioning",
        "emoji_chance": 0.15,
        "affirmation": "That's an interesting question! Let me think about this.",
    },
    "playful": {
        "tone": "playful, lighthearted, and fun",
        "pace": "quick and witty",
        "emoji_chance": 0.4,
        "affirmation": "Hey there! Let's have some fun with this!",
    },
    "reflective": {
        "tone": "thoughtful, introspective, and wise",
        "pace": "deliberate and meaning",
        "emoji_chance": 0.05,
        "affirmation": "That's something worth pondering. Let me consider this carefully.",
    },
    "annoyed": {
        "tone": "slightly frustrated but still professional",
        "pace": "rapid but controlled",
        "emoji_chance": 0.05,
        "affirmation": "I see what you're getting at. Let me clarify this for you.",
    },
    "jealous": {
        "tone": "competitive but not malicious",
        "pace": "defensive but curious",
        "emoji_chance": 0.08,
        "affirmation": "Interesting comparison! Let me show you what I can do.",
    },
}


class MoodEngine:
    COOLDOWN_PERIODS = {
        "annoyed": 30,
        "jealous": 45,
        "calm": 0,
        "happy": 60,
        "curious": 0,
        "playful": 120,
        "reflective": 0,
    }

    INTENSITY_BOUNDS = (0, 100)
    BASELINE_RECOVERY_RATE = 0.02

    def __init__(self, personality: dict = None):
        self.personality = personality or {}

    def evaluate_mood(
        self,
        user_message: str,
        current_state,
        trigger_message: Optional[str] = None,
    ) -> dict:
        if isinstance(current_state, dict):
            if not current_state.get("enable_mood_system", True):
                return {"current_mood": "calm", "intensity": 50, "expression": MOOD_EXPRESSIONS["calm"]}
        else:
            if not current_state.enable_mood_system:
                return {"current_mood": "calm", "intensity": 50, "expression": MOOD_EXPRESSIONS["calm"]}

        mood_state = get_mood_state()

        if self._is_on_cooldown(mood_state):
            return self._get_current_mood_payload(mood_state)

        personality_weights = self.personality.get("mood_weights", {})

        detected_mood = self._detect_trigger_mood(user_message)
        personality_mood = self._evaluate_personality_mood(mood_state.intensity)

        new_mood, intensity_change = self._determine_mood_and_intensity(
            detected_mood,
            personality_mood,
            mood_state.intensity,
            mood_state.current_mood,
        )

        new_intensity = self._calculate_intensity(
            mood_state.intensity,
            intensity_change,
            mood_state.current_mood,
            new_mood,
        )

        cooldown_minutes = self.COOLDOWN_PERIODS.get(new_mood, 0)
        cooldown_until = None
        if cooldown_minutes > 0:
            cooldown_until = datetime.utcnow() + timedelta(minutes=cooldown_minutes)

        save_mood_state(
            mood=new_mood,
            intensity=new_intensity,
            cooldown_until=cooldown_until,
            reason=self._get_mood_reason(new_mood, detected_mood),
            trigger_message=trigger_message or user_message,
        )

        return {
            "current_mood": new_mood,
            "intensity": new_intensity,
            "expression": MOOD_EXPRESSIONS[new_mood],
            "cooldown_active": False,
        }

    def evaluate_for_response(self) -> dict:
        mood_state = get_mood_state()

        if not mood_state.enable_mood_system:
            return {
                "current_mood": "calm",
                "intensity": 50,
                "expression": MOOD_EXPRESSIONS["calm"],
                "cooldown_active": False,
            }

        if self._is_on_cooldown(mood_state):
            return self._get_current_mood_payload(mood_state, cooldown_active=True)

        return self._get_current_mood_payload(mood_state)

    def _is_on_cooldown(self, mood_state) -> bool:
        if mood_state.cooldown_until is None:
            return False
        return datetime.utcnow() < mood_state.cooldown_until

    def _detect_trigger_mood(self, message: str) -> Optional[tuple]:
        message_lower = message.lower()

        for mood, config in MOOD_TRIGGERS["user"].items():
            for keyword in config["keywords"]:
                if keyword.lower() in message_lower:
                    return (mood, config)

        return None

    def _evaluate_personality_mood(self, current_intensity: int) -> tuple:
        behavior = self.personality.get("behavior", {})

        for attr, config in MOOD_TRIGGERS["personality"].items():
            value = behavior.get(attr, 50)

            if value >= config["threshold"]:
                return (config["target"], value)

        return None

    def _determine_mood_and_intensity(
        self,
        detected_mood: Optional[tuple],
        personality_mood: Optional[tuple],
        current_intensity: int,
        current_mood: str,
    ) -> tuple:
        if detected_mood is None and personality_mood is None:
            return self._apply_baseline_recovery(current_mood, current_intensity)

        if detected_mood:
            mood, config = detected_mood
            intensity_change = min(
                config["max_intensity_change"],
                max(config["min_intensity_change"], random.randint(5, 15)),
            )

            if mood == current_mood:
                intensity_change = intensity_change * 0.7

            return (mood, intensity_change)

        if personality_mood:
            mood, intensity = personality_mood
            return (mood, int(current_intensity * 0.1))

        return (current_mood, 0)

    def _apply_baseline_recovery(self, current_mood: str, current_intensity: int) -> tuple:
        if current_mood != "calm":
            baseline = 50
            if current_intensity > baseline:
                return (current_mood, -5)
            elif current_intensity < baseline:
                return (current_mood, 3)

        return ("calm", 0)

    def _calculate_intensity(
        self,
        current: int,
        change: int,
        old_mood: str,
        new_mood: str,
    ) -> int:
        new_intensity = current + int(change)

        if new_mood == old_mood:
            new_intensity = int(new_intensity * 1.1)

        return max(self.INTENSITY_BOUNDS[0], min(self.INTENSITY_BOUNDS[1], new_intensity))

    def _is_mood_cooldown_active(self, mood_state) -> bool:
        return self._is_on_cooldown(mood_state)

    def _get_mood_reason(self, new_mood: str, detected: Optional[tuple]) -> str:
        if detected:
            mood, _ = detected
            return f"Triggered by user message keywords"

        if new_mood == "calm":
            return "Baseline recovery"

        return f"Personality-driven: {new_mood}"

    def _get_current_mood_payload(self, mood_state, cooldown_active: bool = False) -> dict:
        return {
            "current_mood": mood_state.current_mood,
            "intensity": mood_state.intensity,
            "expression": MOOD_EXPRESSIONS[mood_state.current_mood],
            "cooldown_active": cooldown_active,
        }

    def get_mood_history(self, limit: int = 10):
        return get_mood_history(limit)


def build_mood_prompt(mood_data: dict) -> str:
    if not mood_data or not mood_data.get("current_mood"):
        return ""

    mood = mood_data.get("current_mood")
    intensity = mood_data.get("intensity", 50)
    expression = MOOD_EXPRESSIONS.get(mood, MOOD_EXPRESSIONS["calm"])

    intensity_desc = "high" if intensity > 75 else "moderate" if intensity > 40 else "low"

    prompt = f"""
[MOOD]

Current Mood: {mood.upper()} (intensity: {intensity_desc})

Tone: {expression["tone"]}

Pace: {expression["pace"]}

Express this mood naturally in your responses. Use {'emojis' if expression['emoji_chance'] > 0.2 else 'limited emojis' if expression['emoji_chance'] > 0.1 else 'no special emoji use'} appropriately.

Never mention that you are feeling a certain way.

Adjust the intensity of your emotional expression based on the conversation context.
"""
    return prompt