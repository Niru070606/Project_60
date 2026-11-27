import type { MoodState, MoodSettings, MoodPayload } from "../types/mood";

const API_URL = "http://127.0.0.1:5000";

export async function getMoodState(): Promise<MoodState> {
  const response = await fetch(`${API_URL}/mood`);

  if (!response.ok) {
    throw new Error("Failed to fetch mood state");
  }

  return response.json();
}

export async function updateMoodSettings(
  settings: MoodSettings
): Promise<MoodState> {
  const response = await fetch(`${API_URL}/mood/settings`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(settings),
  });

  if (!response.ok) {
    throw new Error("Failed to update mood settings");
  }

  return response.json();
}

export async function resetMood(): Promise<MoodState> {
  const response = await fetch(`${API_URL}/mood/reset`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Failed to reset mood");
  }

  return response.json();
}

export async function getMoodExpression(): Promise<MoodPayload> {
  const response = await fetch(`${API_URL}/mood/expression`);

  if (!response.ok) {
    throw new Error("Failed to fetch mood expression");
  }

  const data = await response.json();
  return data.mood;
}