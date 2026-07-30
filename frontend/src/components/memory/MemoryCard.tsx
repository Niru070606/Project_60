interface Memory {
  id: number;
  memory: string;
  category: string;
  importance: number;
  retrieval_count: number;
}

interface MemoryCardProps {
  memory: Memory;
  onDelete: (id: number) => void;
}

export default function MemoryCard({ memory, onDelete }: MemoryCardProps) {
  return (
    <div className="memory-card">
      <h4>{memory.memory}</h4>

      <div className="memory-meta">
        <span>Category: {memory.category}</span>
        <span>Importance: {memory.importance}</span>
        <span>Used: {memory.retrieval_count} times</span>
      </div>

      <button
        className="btn btn-outline-danger mt-3"
        onClick={() => onDelete(memory.id)}
      >
        Forget
      </button>
    </div>
  );
}
