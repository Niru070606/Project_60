import type { Personality } from "../types/personality";

const STORAGE_KEY = "project60_personality";

export function savePersonality(personality: Personality): void {

  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(personality)
  );
}

export function loadPersonality(): Personality | null {
  const data = localStorage.getItem(STORAGE_KEY);

  if (!data) return null;

  try {
    return JSON.parse(data) as Personality;
  } catch {
    return null;
  }
}

export function deletePersonality(): void {
  localStorage.removeItem(STORAGE_KEY);
}
