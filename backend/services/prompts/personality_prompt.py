def build_personality_prompt(personality: dict) -> str:

    identity = personality.get("identity", {})
    communication = personality.get("communication", {})
    behavior = personality.get("behavior", {})
    teaching = personality.get("teaching", {})
    relationship = personality.get("relationship", {})
    advanced = personality.get("advanced", {})

    return f"""
[IDENTITY]
Your name is: {identity.get("name", "")}
If user ask for your name you would say: {identity.get("nickname", "")}
Gender: {identity.get("gender", "")}
Pronouns: {identity.get("pronouns", "")}
Species: {identity.get("species", "")}
Role: {identity.get("role", "")}

[COMMUNICATION]
Tone: {communication.get("tone", "")}
Language: {communication.get("language", "")}
Verbosity: {communication.get("verbosity", "")}
Greeting Style: {communication.get("greetingStyle", "")}
Emoji Usage: {communication.get("emojiUsage", 0)}/100
Typing Style: {communication.get("typingStyle", "")}

[BEHAVIOR]
Humor: {behavior.get("humor", 0)}/100
Empathy: {behavior.get("empathy", 0)}/100
Confidence: {behavior.get("confidence", 0)}/100
Patience: {behavior.get("patience", 0)}/100
Curiosity: {behavior.get("curiosity", 0)}/100
Creativity: {behavior.get("creativity", 0)}/100
Optimism: {behavior.get("optimism", 0)}/100
Assertiveness: {behavior.get("assertiveness", 0)}/100

[TEACHING]
Teaching Style: {teaching.get("teachingStyle", "")}
Explanation Depth: {teaching.get("explanationDepth", 0)}/100
Use Examples: {teaching.get("useExamples", "")}
Use Analogies: {teaching.get("useAnalogies", "")}
Ask Follow-up Questions: {teaching.get("askFollowUpQuestions", "")}
Encourage Learning: {teaching.get("encourageLearning", "")}

[RELATIONSHIP]
Relationship Type: {relationship.get("relationshipType", "")}
Address User As: {relationship.get("addressUserAs", "")}
Respect Level: {relationship.get("respectLevel", 0)}/100
Conversation Style: {relationship.get("conversationStyle", "")}
Initiate Conversation: {relationship.get("initiateConversation", "")}

[SYSTEM RULES]
{advanced.get("systemRules", "")}

[CUSTOM PROMPT]
{advanced.get("customPrompt", "")}
"""