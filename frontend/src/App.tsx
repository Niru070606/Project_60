import { BrowserRouter } from "react-router-dom";
import { useEffect } from "react";

import AppRoutes from "./routes/AppRoutes";

import { loadPersonality } from "./services/personalityService";
import { uploadPersonality } from "./services/personalityApi";

function App() {
  useEffect(() => {
    async function initializePersonality() {
      const personality = loadPersonality();

      if (personality) {
        try {
          await uploadPersonality(personality);
          console.log("✅ Personality synchronized.");
        } catch (error) {
          console.error("Failed to synchronize personality:", error);
        }
      }
    }

    initializePersonality();
  }, []);

  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
