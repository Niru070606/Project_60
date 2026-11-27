import "../../styles/mood/mood.css";

interface MoodDisplayProps {
  mood: string;
  intensity: number;
  cooldownActive: boolean;
  cooldownUntil: string | null;
}

const MOOD_EMOJIS: Record<string, string> = {
  calm: "🧘",
  happy: "😊",
  curious: "🤔",
  playful: "🎮",
  reflective: "🌙",
  annoyed: "😤",
  jealous: "😏",
};

export default function MoodDisplay({
  mood,
  intensity,
  cooldownActive,
  cooldownUntil,
}: MoodDisplayProps) {
  const emoji = MOOD_EMOJIS[mood] || "💭";
  const intensityPercent = Math.round((intensity / 100) * 100);

  return (
    <div className="mood-display">
      <div className="mood-indicator">
        {emoji}
      </div>

      <div className="mood-label">
        {mood.charAt(0).toUpperCase() + mood.slice(1)}
      </div>

      <div className="mood-intensity">
        <span className="intensity-value">{intensity}%</span>
        <div className="intensity-bar">
          <div
            className="intensity-fill"
            style={{ width: `${intensityPercent}%` }}
          />
        </div>
      </div>

      {cooldownActive && cooldownUntil && (
        <div className="mood-cooldown">
          ⏳ Cooldown until: {cooldownUntil}
        </div>
      )}
    </div>
  );
}