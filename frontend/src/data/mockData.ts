<<<<<<< HEAD
import { KpiMetric, Agent, Decision, SystemHealth, DetailedAgentAnalysis } from '@/types';

export const kpiMetrics: KpiMetric[] = [
  {
    title: 'Total Decisions',
    value: '156',
    change: '+12%',
    trend: 'up',
  },
  {
    title: 'Avg Confidence',
    value: '89%',
    change: '+3%',
    trend: 'up',
  },
  {
    title: 'Active Agents',
    value: '4',
    change: '0%',
    trend: 'neutral',
  },
  {
    title: 'System Health',
    value: '94%',
    change: '+2%',
    trend: 'up',
  },
=======
import { KpiMetric, Agent, Decision, SystemHealth } from '@/types';

export const kpiMetrics: KpiMetric[] = [
  { title: 'Total Decisions', value: '247', change: '+12%', trend: 'up' },
  { title: 'Active Analysis', value: '18', change: '+5%', trend: 'up' },
  { title: 'Completed', value: '229', change: '+8%', trend: 'up' },
  { title: 'Avg Confidence', value: '94.2%', change: '+2.1%', trend: 'up' }
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
];

export const agents: Agent[] = [
  {
    id: 'finance',
    name: 'Finance',
    description: 'Financial analysis and risk assessment',
    icon: 'DollarSign',
    status: 'active',
    performance: 95,
<<<<<<< HEAD
    decisionsAnalyzed: 64,
=======
    decisionsAnalyzed: 64
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
  },
  {
    id: 'risk',
    name: 'Risk',
    description: 'Risk evaluation and mitigation strategies',
    icon: 'Shield',
    status: 'analyzing',
    performance: 87,
<<<<<<< HEAD
    decisionsAnalyzed: 42,
=======
    decisionsAnalyzed: 42
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
  },
  {
    id: 'compliance',
    name: 'Compliance',
    description: 'Regulatory compliance and legal review',
    icon: 'AlertTriangle',
    status: 'active',
    performance: 92,
<<<<<<< HEAD
    decisionsAnalyzed: 38,
=======
    decisionsAnalyzed: 38
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
  },
  {
    id: 'market',
    name: 'Market',
    description: 'Market analysis and competitive intelligence',
    icon: 'TrendingUp',
<<<<<<< HEAD
    status: 'active',
    performance: 89,
    decisionsAnalyzed: 29,
  },
];

// Detailed agent analysis for specific decisions
export const getDetailedAgentAnalysis = (decisionId: string): DetailedAgentAnalysis[] => {
  const analysisMap: Record<string, DetailedAgentAnalysis[]> = {
    '1': [ // "starting an shoe factory outlet in south africa" decision
      {
        id: 'finance',
        name: 'Finance Agent',
        icon: 'DollarSign',
        iconColor: 'text-green-500',
        costImpact: '$5,000,000',
        revenueImpact: '$10,000,000',
        roiEstimate: '0.2%',
        budgetRequired: '$7,000,000',
        recommendation: 'Conduct a detailed financial feasibility study to refine budget estimates and assess potential profitability.'
      },
      {
        id: 'risk',
        name: 'Risk Agent',
        icon: 'AlertTriangle',
        iconColor: 'text-orange-500',
        riskScore: '7/100',
        successProbability: '0.75%',
        riskFactors: ['Political instability', 'Supply chain disruptions', 'Economic downturns'],
        recommendation: 'Develop a comprehensive risk management plan to address identified risks and enhance project resilience.'
      },
      {
        id: 'compliance',
        name: 'Compliance Agent',
        icon: 'Shield',
        iconColor: 'text-blue-500',
        complianceScore: '8/100',
        legalConsiderations: ['Non-compliance penalties', 'Intellectual property disputes'],
        recommendation: 'Engage local legal experts to navigate regulatory requirements and ensure full compliance.'
      },
      {
        id: 'market',
        name: 'Market Agent',
        icon: 'TrendingUp',
        iconColor: 'text-purple-500',
        marketOpportunity: '0.3/100',
        marketTrends: ['Growing middle-class consumer base', 'Increasing demand for affordable footwear'],
        recommendation: 'Leverage market research to identify underserved segments and tailor offerings accordingly.'
      }
    ],
    '2': [ // Default analysis for other decisions
      {
        id: 'finance',
        name: 'Finance Agent',
        icon: 'DollarSign',
        iconColor: 'text-green-500',
        costImpact: '$2,500,000',
        revenueImpact: '$8,500,000',
        roiEstimate: '15.2%',
        budgetRequired: '$3,200,000',
        recommendation: 'Financial projections look favorable. Recommend proceeding with phased implementation approach.'
      },
      {
        id: 'risk',
        name: 'Risk Agent',
        icon: 'AlertTriangle',
        iconColor: 'text-orange-500',
        riskScore: '4/100',
        successProbability: '85%',
        riskFactors: ['Market competition', 'Regulatory changes'],
        recommendation: 'Risk levels are manageable. Implement monitoring protocols for identified risk factors.'
      }
    ]
  };
  
  return analysisMap[decisionId] || analysisMap['2'];
};

export const decisions: Decision[] = [
  {
    id: '1',
    title: 'starting an shoe factory outlet in south africa',
    priority: 'high',
    status: 'active',
    confidence: 92,
    createdAt: '1/15/2025',
    agents: ['finance', 'risk', 'compliance'],
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
  },
  {
    id: '2',
    title: 'New Market Expansion Plan',
    priority: 'medium',
    status: 'completed',
    confidence: 87,
<<<<<<< HEAD
    createdAt: '1/14/2025',
    agents: ['market', 'finance', 'risk'],
=======
    createdAt: '2025-01-14T14:20:00Z',
    agents: ['market', 'finance']
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
  },
  {
    id: '3',
    title: 'Compliance Framework Update',
    priority: 'high',
    status: 'pending',
    confidence: 78,
<<<<<<< HEAD
    createdAt: '1/13/2025',
    agents: ['compliance', 'risk'],
  },
  {
    id: '4',
    title: 'Technology Investment Strategy',
    priority: 'medium',
    status: 'active',
    confidence: 85,
    createdAt: '1/12/2025',
    agents: ['finance', 'market'],
  },
  {
    id: '5',
    title: 'Operational Efficiency Initiative',
    priority: 'low',
    status: 'completed',
    confidence: 91,
    createdAt: '1/11/2025',
    agents: ['finance', 'compliance'],
  },
];

export const systemHealth: SystemHealth = {
  overall: 94,
  activeAgents: 3,
  processingPower: 87,
  systemLoad: 72,
=======
    createdAt: '2025-01-13T09:15:00Z',
    agents: ['compliance', 'risk']
  }
];

export const systemHealth: SystemHealth = {
  overall: 96,
  activeAgents: 3,
  processingPower: 87,
  systemLoad: 42
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
};

export const chartData = {
  priorityDistribution: [
<<<<<<< HEAD
    { name: 'High', value: 45, fill: '#ef4444' },
    { name: 'Medium', value: 78, fill: '#3b82f6' },
    { name: 'Low', value: 32, fill: '#6b7280' },
  ],
  statusBreakdown: [
    { name: 'Active', value: 23, fill: '#10b981' },
    { name: 'Completed', value: 67, fill: '#3b82f6' },
    { name: 'Pending', value: 12, fill: '#f59e0b' },
  ],
  confidenceOverTime: [
    { month: 'Jan', confidence: 85 },
    { month: 'Feb', confidence: 88 },
    { month: 'Mar', confidence: 92 },
    { month: 'Apr', confidence: 89 },
    { month: 'May', confidence: 94 },
    { month: 'Jun', confidence: 91 },
  ],
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
};