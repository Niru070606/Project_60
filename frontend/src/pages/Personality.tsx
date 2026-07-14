import "../styles/common/form.css";
import "../styles/personality/personality.css";

import { useEffect, useState } from "react";

import { defaultPersonality } from "../utils/defaultPersonality";

import {
  loadPersonality,
  savePersonality,
  deletePersonality
} from "../services/personalityService";

import { uploadPersonality } from "../services/personalityApi";

import IdentityCard from "../components/personality/IdentityCard";
import CommunicationCard from "../components/personality/CommunicationCard";
import BehaviorCard from "../components/personality/BehaviorCard";
import TeachingCard from "../components/personality/TeachingCard";
import RelationshipCard from "../components/personality/RelationshipCard";
import AdvancedCard from "../components/personality/AdvancedCard";

export default function Personality() {
  const [personality, setPersonality] = useState(
    () => loadPersonality() ?? defaultPersonality,
  );

  const handleReset = () => {
    deletePersonality();
    setPersonality(structuredClone(defaultPersonality));
  };

  useEffect(() => {
    savePersonality(personality);
    uploadPersonality(personality);
  }, [personality]);

  return (
    <div className="container py-4 marginizer">
      <h2 className="mb-4">Personality</h2>

      <IdentityCard personality={personality} setPersonality={setPersonality} />

      <br />

      <CommunicationCard
        personality={personality}
        setPersonality={setPersonality}
      />

      <br />

      <BehaviorCard personality={personality} setPersonality={setPersonality} />

      <br />

      <TeachingCard personality={personality} setPersonality={setPersonality} />

      <br />

      <RelationshipCard
        personality={personality}
        setPersonality={setPersonality}
      />

      <br />

      <AdvancedCard personality={personality} setPersonality={setPersonality} />
      <br />
      <div className="d-flex justify-content-end mt-4">
        <button className="btn btn-outline-danger" onClick={handleReset}>
          Reset to Default
        </button>
      </div>
    </div>
  );
}
