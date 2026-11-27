import "../../styles/mood/mood.css";

import { useState } from "react";

interface MoodControlsProps {
  enableMoodSystem: boolean;
  onEnableChange: (settings: Partial<{
    enable_mood_system: boolean;
    baseline_intensity: number;
  }>) => void;
  baselineIntensity: number;
  onBaselineChange: (settings: Partial<{
    enable_mood_system: boolean;
    baseline_intensity: number;
  }>) => void;
  onReset: () => void;
}

export default function MoodControls({
  enableMoodSystem,
  onEnableChange,
  baselineIntensity,
  onBaselineChange,
  onReset,
}: MoodControlsProps) {
  const [isResetting, setIsResetting] = useState(false);

  async function handleReset() {
    setIsResetting(true);
    await onReset();
    setIsResetting(false);
  }

  return (
    <div className="mood-controls">
      <div className="mood-toggle">
        <label className="form-label" style={{ marginBottom: 0 }}>
          Enable Mood System
        </label>
        <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
          <span>Off</span>
          <label className="switch">
            <input
              type="checkbox"
              checked={enableMoodSystem}
              onChange={(e) =>
                onEnableChange({ enable_mood_system: e.target.checked })
              }
            />
            <span className="slider" />
          </label>
          <span>On</span>
        </div>
      </div>

      <div className="form-group" style={{ marginBottom: 0 }}>
        <label className="form-label">Baseline Intensity</label>
        <input
          type="range"
          min="0"
          max="100"
          value={baselineIntensity}
          className="form-slider"
          onChange={(e) =>
            onBaselineChange({ baseline_intensity: Number(e.target.value) })
          }
        />
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.85rem", color: "var(--text-secondary)" }}>
          <span>0%</span>
          <span>{baselineIntensity}%</span>
          <span>100%</span>
        </div>
      </div>

      <button
        className="mood-reset-btn"
        onClick={handleReset}
        disabled={isResetting}
      >
        {isResetting ? "Resetting..." : "Reset to Baseline"}
      </button>
    </div>
  );
}