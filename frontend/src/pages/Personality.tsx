import "../styles/common/form.css";
import "../styles/personality/personality.css";

import { useState } from "react";

import type { Personality } from "../types/personality";

import IdentityCard from "../components/personality/IdentityCard";
import CommunicationCard from "../components/personality/CommunicationCard";
import BehaviorCard from "../components/personality/BehaviorCard";
import TeachingCard from "../components/personality/TeachingCard";
import RelationshipCard from "../components/personality/RelationshipCard";
import AdvancedCard from "../components/personality/AdvancedCard";

export default function Personality() {
  const [personality, setPersonality] = useState<Personality>({
    identity: {
      name: "Niru",
      nickname: "Niru",
      gender: "Male",
      pronouns: "He/Him",
      species: "Artificial Intelligence",
      role: "AI Companion",
      age: null,
      birthday: "",
    },

    communication: {
      tone: "Calm",
      language: "English",
      verbosity: "Medium",
      greetingStyle: "Cheerful",
      emojiUsage: 10,
      typingStyle: "Natural",
    },

    behavior: {
      humor: 10,
      empathy: 10,
      confidence: 10,
      patience: 10,
      curiosity: 10,
      creativity: 10,
      optimism: 10,
      assertiveness: 10,
    },

    teaching: {
      teachingStyle: "Socratic",
      explanationDepth: 70,
      useExamples: "Often",
      useAnalogies: "Often",
      askFollowUpQuestions: "Sometimes",
      encourageLearning: "High",
    },

    relationship: {
      relationshipType: "Companion",
      addressUserAs: "",
      respectLevel: 70,
      conversationStyle: "Balanced",
      initiateConversation: "Sometimes",
    },

    advanced: {
      responseRandomness: 50,
      maximumResponseLength: "Medium",
      admitUncertainty: "Always",
      aiIdentityDisclosure: "Only When Asked",
      customPrompt: "",
      systemRules: "",
    },
  });

  return (
    <div className="container py-4 marginizer">
      <h2 className="mb-4">Personality</h2>

      <IdentityCard personality={personality} setPersonality={setPersonality} />

      <br />

      <CommunicationCard
        personality={personality}
        setPersonality={setPersonality}
      />

      <br />

      <BehaviorCard personality={personality} setPersonality={setPersonality} />

      <br />

      <TeachingCard personality={personality} setPersonality={setPersonality} />

      <br />

      <RelationshipCard
        personality={personality}
        setPersonality={setPersonality}
      />

      <br />

      <AdvancedCard personality={personality} setPersonality={setPersonality} />
    </div>
  );
}
