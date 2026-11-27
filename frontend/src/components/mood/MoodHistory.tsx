import "../../styles/mood/mood.css";

import type { MoodHistoryEntry } from "../../types/mood";

interface MoodHistoryProps {
  history: MoodHistoryEntry[];
}

const MOOD_COLORS: Record<string, string> = {
  calm: "bg-blue-500",
  happy: "bg-yellow-400",
  curious: "bg-purple-500",
  playful: "bg-pink-500",
  reflective: "bg-indigo-500",
  annoyed: "bg-red-500",
  jealous: "bg-green-500",
};

export default function MoodHistory({ history }: MoodHistoryProps) {
  if (!history || history.length === 0) {
    return (
      <div className="mood-history">
        <h3 className="history-title">Recent Mood Changes</h3>
        <div className="no-history">
          No mood history yet. The mood system will start tracking when you send messages.
        </div>
      </div>
    );
  }

  return (
    <div className="mood-history">
      <h3 className="history-title">Recent Mood Changes</h3>

      <div className="history-list">
        {history.map((entry, idx) => (
          <div key={idx} className="history-item">
            <div className="history-mood">
              <div
                className={`history-mood-dot ${MOOD_COLORS[entry.mood] || "bg-gray-500"}`}
              />
              <span className="history-mood-name">
                {entry.mood.charAt(0).toUpperCase() + entry.mood.slice(1)}
              </span>
            </div>

            <div className="history-details">
              <div className="history-intensity">
                Intensity: {entry.intensity}%
              </div>

              {entry.reason && (
                <div className="history-reason">{entry.reason}</div>
              )}
            </div>

            <div className="history-time">{entry.timestamp}</div>
          </div>
        ))}
      </div>
    </div>
  );
}