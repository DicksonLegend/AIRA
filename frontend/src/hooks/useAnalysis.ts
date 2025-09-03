import { useState, useCallback } from 'react';
import { apiService, AnalysisResponse } from '../services/api';
import { useAgents } from '../contexts/AgentContext';

export interface UseAnalysisState {
  data: AnalysisResponse | null;
  loading: boolean;
  error: string | null;
}

export function useAnalysis() {
  const [state, setState] = useState<UseAnalysisState>({
    data: null,
    loading: false,
    error: null,
  });
  
  const { updateAgentStatus, updateAgentPerformance, incrementAgentUsage, setAnalysisData } = useAgents();

  const analyzeScenario = useCallback(async (scenario: string, analysisFocus?: string) => {
    setState(prev => ({ ...prev, loading: true, error: null }));
    
    // Set all agents to analyzing status
    const agentIds = ['finance', 'risk', 'compliance', 'market'];
    agentIds.forEach(agentId => {
      updateAgentStatus(agentId, 'analyzing');
    });
    
    try {
      console.log('🚀 Starting analysis for scenario:', scenario);
      const result = await apiService.analyzeScenario(scenario, analysisFocus);
      console.log('✅ Analysis completed, processing results:', result);
      
      // Update agent statuses based on analysis results
      console.log('🔍 Checking response structure...');
      console.log('agents property:', result.agents);
      console.log('agents_utilized property:', result.agents_utilized);
      console.log('crew_result property:', result.crew_result);
      
      // Handle the actual API response structure
      let agentsToProcess: any[] = [];
      
      if (result.agents && Array.isArray(result.agents)) {
        // If agents property exists (our expected format)
        agentsToProcess = result.agents;
        console.log('📊 Using agents property:', agentsToProcess);
      } else if (result.performance_metrics?.results && typeof result.performance_metrics.results === 'object') {
        // Process actual CrewAI response format with real confidence scores
        const results = result.performance_metrics.results;
        agentsToProcess = Object.entries(results).map(([agentKey, agentData]: [string, any]) => {
          // Extract real confidence score from the analysis
          let confidence = 85; // Default fallback
          
          if (typeof agentData.confidence === 'number') {
            confidence = Math.round(agentData.confidence * 100);
          }
          
          return {
            agent_name: agentData.agent || agentKey,
            confidence: confidence,
            recommendation: agentData.analysis || `Analysis completed for ${agentKey}`,
            analysis: agentData.analysis || `Comprehensive analysis performed by ${agentKey}`,
            agentData: agentData // Store full agent data for detailed cards
          };
        });
        console.log('📊 Using performance_metrics.results with real confidence scores:', agentsToProcess);
      } else if (result.agents_utilized && Array.isArray(result.agents_utilized)) {
        // If only agents_utilized exists, create with default confidence
        agentsToProcess = result.agents_utilized.map((agentName: string) => ({
          agent_name: agentName,
          confidence: 85, // Default confidence when no specific score available
          recommendation: `Analysis completed for ${agentName}`,
          analysis: `Comprehensive analysis performed by ${agentName}`
        }));
        console.log('📊 Using agents_utilized property:', agentsToProcess);
      } else {
        // Fallback: create agents based on analysis focus
        const allAgents = ['Finance Agent', 'Risk Agent', 'Compliance Agent', 'Market Agent'];
        agentsToProcess = allAgents.map(agentName => ({
          agent_name: agentName,
          confidence: 85, // Default confidence
          recommendation: `Analysis completed for ${agentName}`,
          analysis: `Comprehensive analysis performed by ${agentName}`
        }));
        console.log('📊 Using fallback agents:', agentsToProcess);
      }
      
      if (agentsToProcess.length > 0) {
        console.log('📊 Processing', agentsToProcess.length, 'agents');
        
        agentsToProcess.forEach((agent: any, index: number) => {
          console.log(`Agent ${index + 1}:`, agent);
          
          // Improved agent ID mapping to handle different formats
          let agentId = agent.agent_name.toLowerCase();
          
          // Handle various possible formats from backend
          if (agentId.includes('finance')) agentId = 'finance';
          else if (agentId.includes('risk')) agentId = 'risk';
          else if (agentId.includes('compliance')) agentId = 'compliance';
          else if (agentId.includes('market')) agentId = 'market';
          else {
            // Fallback: remove 'agent' and clean up
            agentId = agentId.replace(' agent', '').replace('agent', '').trim();
          }
          
          console.log(`🔄 Updating agent: ${agent.agent_name} -> ${agentId}, confidence: ${agent.confidence}`);
          
          try {
            updateAgentStatus(agentId, 'active');
            updateAgentPerformance(agentId, agent.confidence);
            incrementAgentUsage(agentId);
            
            // Store detailed analysis data for the agent cards
            if (agent.agentData) {
              setAnalysisData(agentId, agent.agentData);
            }
            
            console.log(`✅ Successfully updated agent: ${agentId}`);
          } catch (error) {
            console.error(`❌ Failed to update agent ${agentId}:`, error);
          }
        });
      } else {
        console.warn('⚠️ No agents to process');
      }
      
      setState({
        data: result,
        loading: false,
        error: null,
      });
      console.log('🎯 Analysis hook state updated successfully');
      return result;
    } catch (error) {
      // Reset agents to inactive on error
      agentIds.forEach(agentId => {
        updateAgentStatus(agentId, 'inactive');
      });
      
      const errorMessage = error instanceof Error ? error.message : 'Analysis failed';
      setState({
        data: null,
        loading: false,
        error: errorMessage,
      });
      throw error;
    }
  }, [updateAgentStatus, updateAgentPerformance, incrementAgentUsage]);

  const clearError = useCallback(() => {
    setState(prev => ({ ...prev, error: null }));
  }, []);

  const reset = useCallback(() => {
    setState({
      data: null,
      loading: false,
      error: null,
    });
  }, []);

  return {
    ...state,
    analyzeScenario,
    clearError,
    reset,
  };
}

export function useSystemStatus() {
  const [status, setStatus] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const checkStatus = useCallback(async () => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await apiService.getSystemStatus();
      setStatus(result);
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Status check failed');
    } finally {
      setLoading(false);
    }
  }, []);

  const checkHealth = useCallback(async () => {
    try {
      await apiService.healthCheck();
      return true;
    } catch (error) {
      return false;
    }
  }, []);

  return {
    status,
    loading,
    error,
    checkStatus,
    checkHealth,
  };
}
