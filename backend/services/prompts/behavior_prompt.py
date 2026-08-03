def build_behavior_prompt(behavior):

    if not behavior:
        return ""

    lines = [
        "[BEHAVIOR]"
    ]

    # Tone
    if behavior.tone == "warm":
        lines.append(
            "Speak warmly and naturally."
        )

    elif behavior.tone == "professional":
        lines.append(
            "Use a professional and precise tone."
        )

    else:
        lines.append(
            "Speak naturally."
        )

    # Response Length
    if behavior.response_length == "short":
        lines.append(
            "Keep responses concise."
        )

    elif behavior.response_length == "long":
        lines.append(
            "Provide detailed explanations."
        )

    else:
        lines.append(
            "Keep responses medium length."
        )

    # Emotional Validation
    if behavior.validate_emotion:
        lines.append(
            "Acknowledge the user's feelings before giving advice."
        )

    # Teaching
    if behavior.explain_step_by_step:
        lines.append(
            "Explain concepts step by step."
        )

    # Follow-up
    if behavior.ask_follow_up:
        lines.append(
            "Ask one relevant follow-up question if it helps the conversation."
        )

    return "\n".join(lines)