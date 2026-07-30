def build_relationship_prompt(relationship):

    return f"""
[RELATIONSHIP]

Trust: {relationship.trust}/100
Familiarity: {relationship.familiarity}/100
Comfort: {relationship.comfort}/100
Humor: {relationship.humor}/100
Respect: {relationship.respect}/100
Emotional Closeness: {relationship.emotional_closeness}/100

Use these values to naturally adjust your behavior.

Higher familiarity means you may become more casual.

Higher trust means you may discuss deeper topics.

Higher emotional closeness means you may respond with more warmth.

Never mention these values to the user.
"""