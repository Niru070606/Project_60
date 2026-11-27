import "../../styles/mood/mood.css";

import { useEffect, useState } from "react";

import {
  getMoodState,
  updateMoodSettings,
  resetMood,
} from "../../services/moodService";

import type { MoodState } from "../../types/mood";

import MoodDisplay from "./MoodDisplay";
import MoodHistory from "./MoodHistory";
import MoodControls from "./MoodControls";

export default function MoodDashboard() {
  const [moodState, setMoodState] = useState<MoodState | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadMoodState();
  }, []);

  async function loadMoodState() {
    try {
      setIsLoading(true);
      const data = await getMoodState();
      setMoodState(data);
    } catch (err) {
      setError("Failed to load mood state");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }

  async function handleSettingsChange(settings: Partial<MoodState>) {
    if (!moodState) return;

    try {
      const updated = await updateMoodSettings({
        enable_mood_system: settings.enable_mood_system ?? moodState.enable_mood_system,
        baseline_intensity: settings.baseline_intensity ?? moodState.baseline_intensity,
      });
      setMoodState(updated);
    } catch (err) {
      console.error(err);
    }
  }

  async function handleReset() {
    try {
      const updated = await resetMood();
      setMoodState(updated);
    } catch (err) {
      console.error(err);
    }
  }

  if (isLoading) {
    return (
      <div className="mood-page">
        <h2>Loading mood state...</h2>
      </div>
    );
  }

  if (error || !moodState) {
    return (
      <div className="mood-page">
        <h2>{error || "No mood state available"}</h2>
      </div>
    );
  }

  return (
    <div className="mood-page">
      <div className="mood-header">
        <h2 className="mood-title">Mood Engine</h2>
      </div>

      <div className="mood-state-card">
        <div className="mood-main-content">
          <MoodDisplay
            mood={moodState.current_mood}
            intensity={moodState.intensity}
            cooldownActive={moodState.cooldown_active}
            cooldownUntil={moodState.cooldown_until}
          />

          <MoodHistory history={moodState.mood_history} />
        </div>

        <MoodControls
          enableMoodSystem={moodState.enable_mood_system}
          onEnableChange={handleSettingsChange}
          baselineIntensity={moodState.baseline_intensity}
          onBaselineChange={handleSettingsChange}
          onReset={handleReset}
        />
      </div>
    </div>
  );
}