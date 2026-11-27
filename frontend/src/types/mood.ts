export interface MoodHistoryEntry {
  mood: string;
  intensity: number;
  reason: string | null;
  timestamp: string;
}

export interface MoodState {
  current_mood: string;
  intensity: number;
  enable_mood_system: boolean;
  baseline_intensity: number;
  cooldown_active: boolean;
  cooldown_until: string | null;
  mood_history: MoodHistoryEntry[];
}

export interface MoodExpression {
  tone: string;
  pace: string;
  emoji_chance: number;
  affirmation: string;
}

export interface MoodPayload {
  current_mood: string;
  intensity: number;
  expression: MoodExpression;
  cooldown_active: boolean;
}

export interface MoodSettings {
  enable_mood_system: boolean;
  baseline_intensity: number;
  reset_to_baseline?: boolean;
}