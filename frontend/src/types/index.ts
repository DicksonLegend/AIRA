export interface KpiMetric {
  title: string;
  value: string;
  change: string;
  trend: 'up' | 'down' | 'neutral';
}

export interface Agent {
  id: string;
  name: string;
  description: string;
  icon: string;
  status: 'active' | 'analyzing' | 'inactive';
  performance: number;
  decisionsAnalyzed: number;
}

export interface Decision {
  id: string;
  title: string;
  priority: 'high' | 'medium' | 'low';
  status: 'active' | 'completed' | 'pending';
  confidence: number;
  createdAt: string;
  agents: string[];
}

export interface SystemHealth {
  overall: number;
  activeAgents: number;
  processingPower: number;
  systemLoad: number;
}