export interface Personality {
  identity: Identity;

  communication: Communication;

  behavior: Behavior;

  teaching: Teaching;

  relationship: Relationship;

  advanced: Advanced;
}

/* ======================================
   Identity
====================================== */

export interface Identity {
  name: string;

  nickname: string;

  gender: string;

  pronouns: string;

  species: string;

  role: string;

  age: number | null;

  birthday: string;
}

/* ======================================
   Communication
====================================== */

export interface Communication {
  tone: string;

  language: string;

  verbosity: string;

  greetingStyle: string;

  emojiUsage: number;

  typingStyle: string;
}

/* ======================================
   Behavior
====================================== */

export interface Behavior {
  humor: number;

  empathy: number;

  confidence: number;

  patience: number;

  curiosity: number;

  creativity: number;

  optimism: number;

  assertiveness: number;
}

/* ======================================
   Teaching
====================================== */

export interface Teaching {
  teachingStyle: string;

  explanationDepth: number;

  useExamples: string;

  useAnalogies: string;

  askFollowUpQuestions: string;

  encourageLearning: string;
}

/* ======================================
   Relationship
====================================== */

export interface Relationship {
  relationshipType: string;

  addressUserAs: string;

  respectLevel: number;

  conversationStyle: string;

  initiateConversation: string;
}

/* ======================================
   Advanced
====================================== */

export interface Advanced {
  responseRandomness: number;

  maximumResponseLength: string;

  admitUncertainty: string;

  aiIdentityDisclosure: string;

  customPrompt: string;

  systemRules: string;
}
