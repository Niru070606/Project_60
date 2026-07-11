import "../../styles/personality/relationship.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";

export default function RelationshipCard({
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
    <div className="card-theme relationship-card">
      <h3 className="relationship-title">Relationship</h3>

      <div className="form-group">
        <label className="form-label">Relationship Type</label>
        <select
          className="form-select"
          value={personality.relationship.relationshipType}
          name="relationshipType"
          onChange={handleChange}
        >
          <option>Assistant</option>
          <option>Companion</option>
          <option>Friend</option>
          <option>Best Friend</option>
          <option>Mentor</option>
          <option>Tutor</option>
          <option>Coach</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Address User As</label>

        <input
          className="form-input"
          placeholder="Neil"
          value={personality.relationship.addressUserAs}
          name="addressUserAs"
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Respect Level</label>
        <input
          type="range"
          min="0"
          max="100"
          defaultValue="70"
          className="form-slider"
          value={personality.relationship.respectLevel}
          name="respectLevel"
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Conversation Style</label>

        <select
          className="form-select"
          value={personality.relationship.conversationStyle}
          name="conversationStyle"
          onChange={handleChange}
        >
          <option>Balanced</option>
          <option>Professional</option>
          <option>Friendly</option>
          <option>Supportive</option>
          <option>Playful</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Initiate Conversation</label>

        <select
          className="form-select"
          value={personality.relationship.initiateConversation}
          name="initiateConversation"
          onChange={handleChange}
        >
          <option>Never</option>
          <option>Sometimes</option>
          <option>Often</option>
        </select>
      </div>
    </div>
  );
}
