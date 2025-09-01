import { KpiMetric, Agent, Decision, SystemHealth } from '@/types';

export const kpiMetrics: KpiMetric[] = [
  { title: 'Total Decisions', value: '247', change: '+12%', trend: 'up' },
  { title: 'Active Analysis', value: '18', change: '+5%', trend: 'up' },
  { title: 'Completed', value: '229', change: '+8%', trend: 'up' },
  { title: 'Avg Confidence', value: '94.2%', change: '+2.1%', trend: 'up' }
];

export const agents: Agent[] = [
  {
    id: 'finance',
    name: 'Finance',
    description: 'Financial analysis and risk assessment',
    icon: 'DollarSign',
    status: 'active',
    performance: 95,
    decisionsAnalyzed: 64
  },
  {
    id: 'risk',
    name: 'Risk',
    description: 'Risk evaluation and mitigation strategies',
    icon: 'Shield',
    status: 'analyzing',
    performance: 87,
    decisionsAnalyzed: 42
  },
  {
    id: 'compliance',
    name: 'Compliance',
    description: 'Regulatory compliance and legal review',
    icon: 'AlertTriangle',
    status: 'active',
    performance: 92,
    decisionsAnalyzed: 38
  },
  {
    id: 'market',
    name: 'Market',
    description: 'Market analysis and competitive intelligence',
    icon: 'TrendingUp',
    status: 'inactive',
    performance: 89,
    decisionsAnalyzed: 29
  }
];

export const decisions: Decision[] = [
  {
    id: '1',
    title: 'Q4 Budget Allocation Strategy',
    priority: 'high',
    status: 'active',
    confidence: 92,
    createdAt: '2025-01-15T10:30:00Z',
    agents: ['finance', 'risk']
  },
  {
    id: '2',
    title: 'New Market Expansion Plan',
    priority: 'medium',
    status: 'completed',
    confidence: 87,
    createdAt: '2025-01-14T14:20:00Z',
    agents: ['market', 'finance']
  },
  {
    id: '3',
    title: 'Compliance Framework Update',
    priority: 'high',
    status: 'pending',
    confidence: 78,
    createdAt: '2025-01-13T09:15:00Z',
    agents: ['compliance', 'risk']
  }
];

export const systemHealth: SystemHealth = {
  overall: 96,
  activeAgents: 3,
  processingPower: 87,
  systemLoad: 42
};

export const chartData = {
  priorityDistribution: [
    { name: 'High', value: 45, fill: '#EF4444' },
    { name: 'Medium', value: 78, fill: '#F59E0B' },
    { name: 'Low', value: 124, fill: '#10B981' }
  ],
  statusBreakdown: [
    { name: 'Completed', value: 229, fill: '#10B981' },
    { name: 'Active', value: 18, fill: '#3B82F6' },
    { name: 'Pending', value: 12, fill: '#F59E0B' }
  ],
  confidenceOverTime: [
    { month: 'Oct', confidence: 89 },
    { month: 'Nov', confidence: 91 },
    { month: 'Dec', confidence: 93 },
    { month: 'Jan', confidence: 94 }
  ]
};