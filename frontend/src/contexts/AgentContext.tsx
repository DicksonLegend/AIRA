import { createContext, useContext, useState, ReactNode } from 'react';

export interface AgentStatus {
  id: string;
  name: string;
  status: 'active' | 'analyzing' | 'inactive';
  lastUsed?: Date;
  performanceScore?: number;
  decisionsAnalyzed?: number;
}

export interface AgentAnalysisData {
  agent: string;
  model?: string;
  analysis?: string;
  confidence?: number;
  metrics?: Record<string, any>;
  real_data?: Record<string, any>;
  [key: string]: any;
}

interface AgentContextType {
  agents: AgentStatus[];
  latestAnalysisData: Record<string, AgentAnalysisData>;
  updateAgentStatus: (agentId: string, status: 'active' | 'analyzing' | 'inactive') => void;
  updateAgentPerformance: (agentId: string, score: number) => void;
  incrementAgentUsage: (agentId: string) => void;
  resetAllAgents: () => void;
  testAgentUpdates: () => void;
  setAnalysisData: (agentId: string, data: AgentAnalysisData) => void;
}

const AgentContext = createContext<AgentContextType | undefined>(undefined);

// Initial agent state - all inactive until used
const initialAgents: AgentStatus[] = [
  {
    id: 'finance',
    name: 'Finance',
    status: 'inactive',
    performanceScore: 0,
    decisionsAnalyzed: 0
  },
  {
    id: 'risk',
    name: 'Risk',
    status: 'inactive',
    performanceScore: 0,
    decisionsAnalyzed: 0
  },
  {
    id: 'compliance',
    name: 'Compliance',
    status: 'inactive',
    performanceScore: 0,
    decisionsAnalyzed: 0
  },
  {
    id: 'market',
    name: 'Market',
    status: 'inactive',
    performanceScore: 0,
    decisionsAnalyzed: 0
  }
];

export function AgentProvider({ children }: { children: ReactNode }) {
  const [agents, setAgents] = useState<AgentStatus[]>(initialAgents);
  const [latestAnalysisData, setLatestAnalysisData] = useState<Record<string, AgentAnalysisData>>({});

  const updateAgentStatus = (agentId: string, status: 'active' | 'analyzing' | 'inactive') => {
    console.log(`AgentContext: Updating agent ${agentId} to status ${status}`);
    setAgents(prev => prev.map(agent => 
      agent.id === agentId 
        ? { ...agent, status, lastUsed: status === 'active' ? new Date() : agent.lastUsed }
        : agent
    ));
  };

  const updateAgentPerformance = (agentId: string, score: number) => {
    console.log(`AgentContext: Updating agent ${agentId} performance to ${score}`);
    setAgents(prev => prev.map(agent => 
      agent.id === agentId 
        ? { ...agent, performanceScore: score }
        : agent
    ));
  };

  const incrementAgentUsage = (agentId: string) => {
    console.log(`AgentContext: Incrementing usage for agent ${agentId}`);
    setAgents(prev => prev.map(agent => 
      agent.id === agentId 
        ? { 
            ...agent, 
            decisionsAnalyzed: (agent.decisionsAnalyzed || 0) + 1,
            lastUsed: new Date()
          }
        : agent
    ));
  };

  const setAnalysisData = (agentId: string, data: AgentAnalysisData) => {
    console.log(`AgentContext: Setting analysis data for agent ${agentId}`, data);
    setLatestAnalysisData(prev => ({
      ...prev,
      [agentId]: data
    }));
  };

  const resetAllAgents = () => {
    setAgents(initialAgents);
    setLatestAnalysisData({});
  };

  // Test function to verify UI updates work
  const testAgentUpdates = () => {
    console.log('🧪 Testing agent updates...');
    setAgents(prev => prev.map(agent => ({
      ...agent,
      status: 'active' as const,
      performanceScore: Math.floor(Math.random() * 40) + 60, // Random score 60-100
      decisionsAnalyzed: Math.floor(Math.random() * 5) + 1, // Random 1-5
      lastUsed: new Date()
    })));
  };

  return (
    <AgentContext.Provider value={{
      agents,
      latestAnalysisData,
      updateAgentStatus,
      updateAgentPerformance,
      incrementAgentUsage,
      resetAllAgents,
      testAgentUpdates,
      setAnalysisData
    }}>
      {children}
    </AgentContext.Provider>
  );
}

export function useAgents() {
  const context = useContext(AgentContext);
  if (context === undefined) {
    throw new Error('useAgents must be used within an AgentProvider');
  }
  return context;
}
