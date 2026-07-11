import "../../styles/personality/behavior.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";

const behaviorTraits = [
  { key: "humor", label: "Humor" },
  { key: "empathy", label: "Empathy" },
  { key: "confidence", label: "Confidence" },
  { key: "patience", label: "Patience" },
  { key: "curiosity", label: "Curiosity" },
  { key: "creativity", label: "Creativity" },
  { key: "optimism", label: "Optimism" },
  { key: "assertiveness", label: "Assertiveness" },
] as const;

export default function BehaviorCard({
  personality,
  setPersonality,
}: PersonalityCardProps) {
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;

    setPersonality((prev) => ({
      ...prev,

      behavior: {
        ...prev.behavior,

        [name]: Number(value),
      },
    }));
  };

  return (
    <div className="card-theme form-card behavior-card">
      <h3 className="form-title">Behavior</h3>

      {behaviorTraits.map((trait) => (
        <div className="form-group" key={trait.key}>
          <div className="form-header">
            <label className="form-label">{trait.label}</label>

            <span className="form-value">
              {personality.behavior[trait.key]}
            </span>
          </div>

          <input
            type="range"
            className="form-slider"
            name={trait.key}
            min="0"
            max="100"
            value={personality.behavior[trait.key]}
            onChange={handleChange}
          />
        </div>
      ))}
    </div>
  );
}
