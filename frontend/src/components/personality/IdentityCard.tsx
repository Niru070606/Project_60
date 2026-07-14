import "../../styles/personality/identity.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";
import { updatePersonality } from "../../utils/updatePersonality";

export default function IdentityCard({
  personality,
  setPersonality,
}: PersonalityCardProps) {
  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;

    updatePersonality(
      "identity",

      name,

      name === "age" ? (value === "" ? null : Number(value)) : value,

      setPersonality,
    );
  };

  return (
    <div className="card-theme form-card identity-card">
      <h3 className="form-title">Identity</h3>

      <div className="form-group">
        <label className="form-label">Name</label>

        <input
          className="form-input"
          name="name"
          value={personality.identity.name}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Nickname</label>

        <input
          className="form-input"
          name="nickname"
          value={personality.identity.nickname}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Gender</label>

        <select
          className="form-select"
          name="gender"
          value={personality.identity.gender}
          onChange={handleChange}
        >
          <option>Male</option>
          <option>Female</option>
          <option>Non-binary</option>
          <option>Custom</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Pronouns</label>

        <input
          className="form-input"
          name="pronouns"
          value={personality.identity.pronouns}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Species</label>

        <input
          className="form-input"
          name="species"
          value={personality.identity.species}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Role</label>

        <input
          className="form-input"
          name="role"
          value={personality.identity.role}
          onChange={handleChange}
        />
      </div>

      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Age</label>

          <input
            type="number"
            className="form-input"
            name="age"
            value={personality.identity.age ?? ""}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label className="form-label">Birthday</label>

          <input
            type="date"
            className="form-input"
            name="birthday"
            value={personality.identity.birthday}
            onChange={handleChange}
          />
        </div>
      </div>
    </div>
  );
}
