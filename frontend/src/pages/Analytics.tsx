import "../styles/analytics/analytics.css";
import "../styles/dashboard/stat-card.css";

import { useEffect, useState } from "react";
import { Brain, Users, TrendingUp, Clock } from "lucide-react";

import StatCard from "../components/dashboard/StatCard";

import {
  getMemoryOverview,
  getMemoryGrowth,
  getMemoryCategories,
  getEntities,
  getRetrievalStats,
  getChatUsage,
} from "../services/DashboardApi";

import type {
  MemoryOverview,
  MemoryGrowthDataPoint,
  MemoryCategory,
  EntityStats,
  RetrievalStats,
  ChatUsage,
} from "../services/DashboardApi";

export default function Analytics() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Memory Overview
  const [memoryOverview, setMemoryOverview] = useState<MemoryOverview>({
    total_memories: 0,
    memories_added: 0,
    memories_merged: 0,
    total_entities: 0,
  });

  // Memory Growth
  const [memoryGrowth, setMemoryGrowth] = useState<{
    growth_data: MemoryGrowthDataPoint[];
    total_growth: number;
  }>({
    growth_data: [],
    total_growth: 0,
  });

  // Memory Categories
  const [categories, setCategories] = useState<MemoryCategory[]>([]);

  // Entities
  const [entities, setEntities] = useState<EntityStats[]>([]);

  // Retrieval Stats
  const [retrievalStats, setRetrievalStats] = useState<RetrievalStats>({
    total_retrievals: 0,
    average_retrieval_score: 0,
    top_retrieved: [],
    retrieval_activity: [],
  });

  // Chat Usage
  const [chatUsage, setChatUsage] = useState<ChatUsage>({
    total_conversations: 0,
    total_messages: 0,
    total_sessions: 0,
    average_messages_per_session: 0,
    activity_over_time: [],
  });

  useEffect(() => {
    async function loadAnalytics() {
      try {
        setLoading(true);
        setError(null);

        const [
          overview,
          growth,
          cats,
          ents,
          retrieval,
          chat,
        ] = await Promise.allSettled([
          getMemoryOverview(),
          getMemoryGrowth(),
          getMemoryCategories(),
          getEntities(),
          getRetrievalStats(),
          getChatUsage(),
        ]);

        if (overview.status === "fulfilled") {
          setMemoryOverview(overview.value);
        }

        if (growth.status === "fulfilled") {
          setMemoryGrowth(growth.value);
        }

        if (cats.status === "fulfilled") {
          setCategories(cats.value.categories);
        }

        if (ents.status === "fulfilled") {
          setEntities(ents.value.entities);
        }

        if (retrieval.status === "fulfilled") {
          setRetrievalStats(retrieval.value);
        }

        if (chat.status === "fulfilled") {
          setChatUsage(chat.value);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "Failed to load analytics");
      } finally {
        setLoading(false);
      }
    }

    loadAnalytics();
  }, []);

  if (loading) {
    return (
      <div className="analytics-container">
        <div className="loading-container">
          <div className="loading-spinner" />
          <p>Loading analytics...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="analytics-container">
        <div className="error-message">
          <p>⚠️ {error}</p>
          <button onClick={() => window.location.reload()} style={{ marginTop: "0.5rem" }}>
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="analytics-container">
      {/* Memory Overview - Stat Cards */}
      <section className="analytics-section">
        <h4 className="section-title">Memory Overview</h4>
        <div className="row g-4 mb-4">
          <div className="col-lg-3 col-md-6">
            <StatCard
              title="Total Memories"
              value={memoryOverview.total_memories}
              icon={<Brain size={28} />}
            />
          </div>
          <div className="col-lg-3 col-md-6">
            <StatCard
              title="Memories Added"
              value={memoryOverview.memories_added}
              icon={<Clock size={28} />}
            />
          </div>
          <div className="col-lg-3 col-md-6">
            <StatCard
              title="Merged"
              value={memoryOverview.memories_merged}
              icon={<TrendingUp size={28} />}
            />
          </div>
          <div className="col-lg-3 col-md-6">
            <StatCard
              title="Total Entities"
              value={memoryOverview.total_entities}
              icon={<Users size={28} />}
            />
          </div>
        </div>
      </section>

      {/* Memory Growth */}
      <section className="analytics-section">
        <div className="card-theme">
          <h4 className="section-title card-with-header">Memory Growth</h4>
          <div className="growth-chart">
            {memoryGrowth.growth_data.length > 0 ? (
              <BarChart data={memoryGrowth.growth_data} />
            ) : (
              <div className="chart-placeholder">
                <p>No memory growth data available yet.</p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Memory Categories */}
      <section className="analytics-section">
        <div className="card-theme">
          <h4 className="section-title card-with-header">Memory Categories</h4>
          <div className="table-section">
            {categories.length > 0 ? (
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Category</th>
                    <th>Count</th>
                    <th>Percentage</th>
                  </tr>
                </thead>
                <tbody>
                  {categories.map((cat) => (
                    <tr key={cat.category}>
                      <td>{cat.category}</td>
                      <td>{cat.count}</td>
                      <td>{((cat.count / categories.reduce((a, c) => a + c.count, 0)) * 100).toFixed(1)}%</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-container">
                <p>No categories yet. Add memories to see category breakdown.</p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Entities */}
      <section className="analytics-section">
        <div className="card-theme">
          <h4 className="section-title card-with-header">Frequently Mentioned Entities</h4>
          <div className="table-section">
            {entities.length > 0 ? (
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Linked Memories</th>
                  </tr>
                </thead>
                <tbody>
                  {entities.map((entity, idx) => (
                    <tr key={idx}>
                      <td>{entity.name}</td>
                      <td>{entity.type}</td>
                      <td>{entity.memory_count}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-container">
                <p>No entities identified yet.</p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Retrieval Performance */}
      <section className="analytics-section">
        <div className="card-theme">
          <h4 className="section-title card-with-header">Retrieval Performance</h4>
          <div className="metrics-grid" style={{ marginBottom: "1rem" }}>
            <div className="metric-item">
              <span className="metric-label">Total Retrievals</span>
              <span className="metric-value">{retrievalStats.total_retrievals}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Avg Retrieval Count</span>
              <span className="metric-value">{retrievalStats.average_retrieval_score}</span>
            </div>
          </div>
          <div className="activity-list">
            {retrievalStats.top_retrieved.length > 0 ? (
              retrievalStats.top_retrieved.map((mem) => (
                <div key={mem.id} className="activity-item">
                  <div className="activity-dot" />
                  <div className="activity-content">
                    <span className="activity-title">{mem.text}</span>
                    <span className="activity-time">{mem.retrieval_count} retrievals</span>
                  </div>
                </div>
              ))
            ) : (
              <div className="empty-container">
                <p>No retrievals recorded yet.</p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Chat Usage */}
      <section className="analytics-section">
        <div className="card-theme">
          <h4 className="section-title card-with-header">Chat Usage</h4>
          <div className="metrics-grid" style={{ marginBottom: "1rem" }}>
            <div className="metric-item">
              <span className="metric-label">Total Messages</span>
              <span className="metric-value">{chatUsage.total_messages}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Total Sessions</span>
              <span className="metric-value">{chatUsage.total_sessions}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Avg Messages/Session</span>
              <span className="metric-value">{chatUsage.average_messages_per_session}</span>
            </div>
          </div>
          <div className="growth-chart">
            {chatUsage.activity_over_time.length > 0 ? (
              <BarChart data={chatUsage.activity_over_time} />
            ) : (
              <div className="chart-placeholder">
                <p>No chat activity data available yet.</p>
              </div>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}

// Custom BarChart component
interface BarChartProps {
  data: { date: string; count: number }[];
}

function BarChart({ data }: BarChartProps) {
  const maxCount = Math.max(...data.map((d) => d.count), 1);
  const displayData = data.slice(-10);

  return (
    <div className="bar-chart">
      {displayData.map((item, idx) => (
        <div key={idx} className="bar-row">
          <span className="bar-label">{item.date}</span>
          <div className="bar-container">
            <div
              className="bar-fill"
              style={{ width: `${(item.count / maxCount) * 100}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}