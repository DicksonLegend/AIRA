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

<<<<<<< HEAD
export interface DetailedAgentAnalysis {
  id: string;
  name: string;
  icon: string;
  iconColor: string;
  costImpact?: string;
  revenueImpact?: string;
  roiEstimate?: string;
  budgetRequired?: string;
  riskScore?: string;
  successProbability?: string;
  riskFactors?: string[];
  complianceScore?: string;
  legalConsiderations?: string[];
  marketOpportunity?: string;
  marketTrends?: string[];
  recommendation: string;
}

=======
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
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