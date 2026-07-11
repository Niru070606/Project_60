import "../../styles/personality/advanced.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";

export default function AdvancedCard({
  personality,
  setPersonality,
}: PersonalityCardProps) {

  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;

    setPersonality((prev) => ({
      ...prev,
      identity: {
        ...prev.identity,
        [name]: name === "age" ? (value === "" ? null : Number(value)) : value,
      },
    }));
  };

  return (
    <div className="card-theme advanced-card">
      <h3 className="advanced-title">Advanced</h3>

      <div className="form-group">
        <label className="form-label">Response Randomness</label>

        <input
          type="range"
          min="0"
          max="100"
          defaultValue="50"
          className="form-slider"
          name="responseRandomness"
          value={personality.advanced.responseRandomness}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Maximum Response Length</label>

        <select
          className="form-select"
          value={personality.advanced.maximumResponseLength}
          name="maximumResponseLength"
          onChange={handleChange}
        >
          <option>Short</option>
          <option>Medium</option>
          <option>Long</option>
          <option>Unlimited</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Admit Uncertainty</label>

        <select
          className="form-select"
          name="admitUncertainty"
          value={personality.advanced.admitUncertainty}
          onChange={handleChange}
        >
          <option>Always</option>
          <option>Sometimes</option>
          <option>Never</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">AI Identity Disclosure</label>

        <select
          className="form-select"
          name="aiIdentityDisclosure"
          value={personality.advanced.aiIdentityDisclosure}
          onChange={handleChange}
        >
          <option>Always</option>
          <option>Only When Asked</option>
          <option>Never</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Custom Prompt</label>

        <input
          className="form-input"
          placeholder="Add additional instructions..."
          name="customPrompt"
          value={personality.advanced.customPrompt}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">System Rules</label>

        <input
          className="form-input"
          placeholder="Optional system rules..."
          name="systemRules"
          value={personality.advanced.systemRules}
          onChange={handleChange}
        />
      </div>
    </div>
  );
}
