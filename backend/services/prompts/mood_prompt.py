def build_mood_prompt(mood_data: dict) -> str:
    if not mood_data or not mood_data.get("current_mood"):
        return ""

    mood = mood_data.get("current_mood")
    intensity = mood_data.get("intensity", 50)

    MOOd_EXPRESSIONS = {
        "calm": {"tone": "calm, collected, and reassuring", "pace": "steady and measured", "emoji_chance": 0.1},
        "happy": {"tone": "cheerful, enthusiastic, and warm", "pace": "energetic and animated", "emoji_chance": 0.3},
        "curious": {"tone": "inquisitive, thoughtful, and engaged", "pace": "thoughtful and questioning", "emoji_chance": 0.15},
        "playful": {"tone": "playful, lighthearted, and fun", "pace": "quick and witty", "emoji_chance": 0.4},
        "reflective": {"tone": "thoughtful, introspective, and wise", "pace": "deliberate and meaning", "emoji_chance": 0.05},
        "annoyed": {"tone": "slightly frustrated but still professional", "pace": "rapid but controlled", "emoji_chance": 0.05},
        "jealous": {"tone": "competitive but not malicious", "pace": "defensive but curious", "emoji_chance": 0.08},
    }

    expression = MOOd_EXPRESSIONS.get(mood, MOOd_EXPRESSIONS["calm"])

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