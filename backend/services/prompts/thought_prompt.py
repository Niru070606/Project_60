def build_thought_prompt(thought):

    prompt = "[THOUGHT PLAN]\n"

    prompt += f"Answer Style: {thought.answer_style}\n"

    if thought.emotional:
        prompt += (
            "Respond warmly and naturally.\n"
        )

    if thought.teaching:
        prompt += (
            "Explain clearly with examples.\n"
        )

    if thought.ask_follow_up:
        prompt += (
            "Ask one helpful follow-up question.\n"
        )

    if thought.recall_memory:
        prompt += (
            "Use remembered information naturally.\n"
        )

    return prompt