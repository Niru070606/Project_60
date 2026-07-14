import "../../styles/personality/communication.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";
import { updatePersonality } from "../../utils/updatePersonality";

export default function CommunicationCard({
  personality,
  setPersonality,
}: PersonalityCardProps) {
  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;

    updatePersonality(
      "communication",

      name,

      name === "emojiUsage" ? Number(value) : value,

      setPersonality,
    );
  };

  return (
    <div className="card-theme form-card communication-card">
      <h3 className="form-title">Communication</h3>

      <div className="form-group">
        <label className="form-label">Tone</label>

        <select
          className="form-select"
          name="tone"
          value={personality.communication.tone}
          onChange={handleChange}
        >
          <option>Friendly</option>
          <option>Professional</option>
          <option>Calm</option>
          <option>Playful</option>
          <option>Serious</option>
          <option>Motivational</option>
          <option>Supportive</option>
          <option>Sarcastic</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Language</label>

        <select
          className="form-select"
          name="language"
          value={personality.communication.language}
          onChange={handleChange}
        >
          <option>English</option>
          <option>Filipino</option>
          <option>Japanese</option>
          <option>Spanish</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Verbosity</label>

        <select
          className="form-select"
          name="verbosity"
          value={personality.communication.verbosity}
          onChange={handleChange}
        >
          <option>Very Short</option>
          <option>Short</option>
          <option>Medium</option>
          <option>Detailed</option>
          <option>Very Detailed</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Greeting Style</label>

        <select
          className="form-select"
          name="greetingStyle"
          value={personality.communication.greetingStyle}
          onChange={handleChange}
        >
          <option>Casual</option>
          <option>Formal</option>
          <option>Warm</option>
          <option>Energetic</option>
          <option>Minimal</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">
          Emoji Usage ({personality.communication.emojiUsage}%)
        </label>

        <input
          type="range"
          className="form-slider"
          name="emojiUsage"
          min="0"
          max="100"
          value={personality.communication.emojiUsage}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Typing Style</label>

        <select
          className="form-select"
          name="typingStyle"
          value={personality.communication.typingStyle}
          onChange={handleChange}
        >
          <option>Natural</option>
          <option>Fast</option>
          <option>Thoughtful</option>
          <option>Expressive</option>
        </select>
      </div>
    </div>
  );
}
