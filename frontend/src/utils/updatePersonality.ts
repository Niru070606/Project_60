import type { Personality } from "../types/personality";

export function updatePersonality<T extends keyof Personality>(
  section: T,
  name: string,
  value: unknown,
  setPersonality: React.Dispatch<React.SetStateAction<Personality>>,
) {
  setPersonality((prev) => ({
    ...prev,

    [section]: {
      ...prev[section],

      [name]: value,
    },
  }));
}
