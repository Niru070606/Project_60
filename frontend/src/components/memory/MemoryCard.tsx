interface Memory {
  id: number;
  memory: string;
  category: string;
  importance: number;
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
        <span>{memory.category}</span>
        <span>⭐ {memory.importance}</span>
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
