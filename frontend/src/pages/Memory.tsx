import { useEffect, useState } from "react";

import { getMemories, deleteMemory } from "../services/memoryService";

import MemoryCard from "../components/memory/MemoryCard";
import "../styles/memory/memory.css";

interface Memory {
  id: number;
  memory: string;
  category: string;
  importance: number;
  retrieval_count: number;
}

export default function Memory() {
  const [memories, setMemories] = useState<Memory[]>([]);

  async function loadMemories() {
    try {
      const data = await getMemories();

      setMemories(data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadMemories();
  }, []);

  async function handleDelete(id: number) {
    try {
      await deleteMemory(id);

      setMemories((prev) => prev.filter((memory) => memory.id !== id));
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="container py-4">
      <h2>Memory</h2>

      {memories.length === 0 ? (
        <p>No memories yet.</p>
      ) : (
        memories.map((memory) => (
          <MemoryCard key={memory.id} memory={memory} onDelete={handleDelete} />
        ))
      )}
    </div>
  );
}
