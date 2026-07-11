import type { Dispatch, SetStateAction } from "react";
import type { Personality } from "./personality";

export interface PersonalityCardProps {
  personality: Personality;

  setPersonality: Dispatch<SetStateAction<Personality>>;
}
