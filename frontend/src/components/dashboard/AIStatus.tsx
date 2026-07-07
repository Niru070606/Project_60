import "./../../styles/dashboard/ai-status.css";

export default function AIStatus() {
  return (
    <div className="card-theme ai-status">
      <h4 className="section-title">AI Status</h4>

      <div className="status-grid">
        <div className="status-item">
          <span>Status</span>
          <strong>🟢 Online</strong>
        </div>

        <div className="status-item">
          <span>Model</span>
          <strong>Project-60 v0.1</strong>
        </div>

        <div className="status-item">
          <span>Growth Stage</span>
          <strong>Baby</strong>
        </div>

        <div className="status-item">
          <span>Memory</span>
          <strong>124 Memories</strong>
        </div>

        <div className="status-item">
          <span>System Health</span>
          <strong>Excellent</strong>
        </div>

        <div className="status-item">
          <span>Last Conversation</span>
          <strong>2 hours ago</strong>
        </div>
      </div>
    </div>
  );
}
