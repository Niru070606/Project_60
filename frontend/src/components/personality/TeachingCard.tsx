import "../../styles/personality/teaching.css";

import type { ChangeEvent } from "react";
import type { PersonalityCardProps } from "../../types/personalityCardProps";
import { updatePersonality } from "../../utils/updatePersonality";

export default function TeachingCard({
  personality,
  setPersonality,
}: PersonalityCardProps) {

  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;

    updatePersonality(
      "teaching",

      name,

      name === "explanationDepth" ? Number(value) : value,

      setPersonality,
    );
  };

  return (
    <div className="card-theme teaching-card">
      <h3 className="teaching-title">Teaching</h3>

      <div className="form-group">
        <label className="form-label">Teaching Style</label>

        <select
          className="form-select"
          value={personality.teaching.teachingStyle}
          onChange={handleChange}
        >
          <option>Socratic</option>
          <option>Direct</option>
          <option>Step-by-Step</option>
          <option>Project-Based</option>
          <option>Storytelling</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Explanation Depth</label>

        <input
          type="range"
          min="0"
          max="100"
          defaultValue="70"
          className="form-slider"
          value={personality.teaching.explanationDepth}
          onChange={handleChange}
          name="explanationDepth"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Use Examples</label>

        <select
          className="form-select"
          value={personality.teaching.useExamples}
          onChange={handleChange}
          name="useExamples"
        >
          <option>Never</option>
          <option>Sometimes</option>
          <option>Often</option>
          <option>Always</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Use Analogies</label>

        <select
          className="form-select"
          value={personality.teaching.useAnalogies}
          onChange={handleChange}
          name="useAnalogies"
        >
          <option>Never</option>
          <option>Sometimes</option>
          <option>Often</option>
          <option>Always</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Ask Follow-up Questions</label>

        <select
          className="form-select"
          value={personality.teaching.askFollowUpQuestions}
          onChange={handleChange}
          name="askFollowUpQuestions"
        >
          <option>Never</option>
          <option>Sometimes</option>
          <option>Often</option>
          <option>Always</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Encourage Learning</label>

        <select
          className="form-select"
          value={personality.teaching.encourageLearning}
          onChange={handleChange}
          name="encourageLearning"
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>
      </div>
    </div>
  );
}
