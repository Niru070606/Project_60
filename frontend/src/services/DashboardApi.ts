const API_URL = "http://127.0.0.1:5000";

export interface Memory {
  id: number;
  memory: string;
  category: string;
  importance: number;
  retrieval_count: number;
  created_at: string;
}

export interface Message {
  id: number;
  sender: string;
  message: string;
  time: string;
}

export interface PersonalityData {
  identity?: {
    name?: string;
    nickname?: string;
  };
  behavior?: {
    curiosity?: number;
    optimism?: number;
  };
  relationship?: {
    relationshipType?: string;
  };
  [key: string]: unknown;
}

// Analytics interfaces
export interface MemoryOverview {
  total_memories: number;
  memories_added: number;
  memories_merged: number;
  total_entities: number;
}

export interface MemoryGrowthDataPoint {
  date: string;
  count: number;
}

export interface MemoryCategory {
  category: string;
  count: number;
}

export interface EntityStats {
  name: string;
  type: string;
  memory_count: number;
}

export interface TopRetrievedMemory {
  id: number;
  text: string;
  retrieval_count: number;
}

export interface RetrievalStats {
  total_retrievals: number;
  average_retrieval_score: number;
  top_retrieved: TopRetrievedMemory[];
  retrieval_activity: MemoryGrowthDataPoint[];
}

export interface ChatUsage {
  total_conversations: number;
  total_messages: number;
  total_sessions: number;
  average_messages_per_session: number;
  activity_over_time: MemoryGrowthDataPoint[];
}

export interface AnalyticsSummary {
  memory_count: number;
  chat_count: number;
  entity_count: number;
  categories: MemoryCategory[];
  created_date: string | null;
}

// Existing API functions
export async function getMemories(): Promise<Memory[]> {
  const response = await fetch(`${API_URL}/memories`);
  if (!response.ok) throw new Error("Failed to fetch memories");
  return response.json();
}

export async function getMessages(): Promise<Message[]> {
  const response = await fetch(`${API_URL}/messages`);
  if (!response.ok) throw new Error("Failed to fetch messages");
  return response.json();
}

export async function getPersonality(): Promise<PersonalityData> {
  const response = await fetch(`${API_URL}/personality`);
  if (!response.ok) throw new Error("Failed to fetch personality");
  return response.json();
}

export async function getSummary(): Promise<{
  memoryCount: number;
  chatCount: number;
  mood: string;
  personalityTrait: string;
}> {
  const [memories, messages, personality] = await Promise.allSettled([
    getMemories(),
    getMessages(),
    getPersonality(),
  ]);

  return {
    memoryCount: memories.status === "fulfilled" ? memories.value.length : 0,
    chatCount: messages.status === "fulfilled" ? messages.value.length : 0,
    mood: "Happy",
    personalityTrait: personality.status === "fulfilled" && personality.value.relationship?.relationshipType
      ? personality.value.relationship.relationshipType
      : "Curious",
  };
}

// Analytics API functions
export async function getMemoryOverview(): Promise<MemoryOverview> {
  const response = await fetch(`${API_URL}/analytics/memory-overview`);
  if (!response.ok) throw new Error("Failed to fetch memory overview");
  return response.json();
}

export async function getMemoryGrowth(): Promise<{
  growth_data: MemoryGrowthDataPoint[];
  total_growth: number;
}> {
  const response = await fetch(`${API_URL}/analytics/memory-growth`);
  if (!response.ok) throw new Error("Failed to fetch memory growth");
  return response.json();
}

export async function getMemoryCategories(): Promise<{
  categories: MemoryCategory[];
}> {
  const response = await fetch(`${API_URL}/analytics/memory-categories`);
  if (!response.ok) throw new Error("Failed to fetch memory categories");
  return response.json();
}

export async function getEntities(): Promise<{
  entities: EntityStats[];
}> {
  const response = await fetch(`${API_URL}/analytics/entities`);
  if (!response.ok) throw new Error("Failed to fetch entities");
  return response.json();
}

export async function getRetrievalStats(): Promise<RetrievalStats> {
  const response = await fetch(`${API_URL}/analytics/retrieval-stats`);
  if (!response.ok) throw new Error("Failed to fetch retrieval stats");
  return response.json();
}

export async function getChatUsage(): Promise<ChatUsage> {
  const response = await fetch(`${API_URL}/analytics/chat-usage`);
  if (!response.ok) throw new Error("Failed to fetch chat usage");
  return response.json();
}

export async function getAnalyticsSummary(): Promise<AnalyticsSummary> {
  const response = await fetch(`${API_URL}/analytics/summary`);
  if (!response.ok) throw new Error("Failed to fetch analytics summary");
  return response.json();
}