import type { Personality } from "../types/personality";

const API_URL = "http://127.0.0.1:5000/personality";

export async function uploadPersonality(personality: Personality) {
  const response = await fetch(API_URL, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(personality),
  });

  return await response.json();
}
