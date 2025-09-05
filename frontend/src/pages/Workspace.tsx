import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { DetailedAgentCard } from '@/components/ui/DetailedAgentCard';
import { useAgents } from '@/contexts/AgentContext';
import { DetailedAgentAnalysis } from '@/types';

export default function Workspace() {
  const [searchTerm, setSearchTerm] = useState('');
  const { agents, latestAnalysisData } = useAgents();
  const navigate = useNavigate();

  // Load persisted search term on mount
  useEffect(() => {
    try {
      const savedSearchTerm = localStorage.getItem('aira_workspace_search_term');
      if (savedSearchTerm) {
        setSearchTerm(savedSearchTerm);
      }
    } catch (error) {
      console.warn('⚠️ Failed to load workspace search term:', error);
    }
  }, []);

  // Save search term whenever it changes
  useEffect(() => {
    try {
      localStorage.setItem('aira_workspace_search_term', searchTerm);
    } catch (error) {
      console.warn('⚠️ Failed to save workspace search term:', error);
    }
  }, [searchTerm]);

  const handleNavigateToDashboard = () => {
    navigate('/dashboard');
  };

  // Convert agent context data to detailed analysis format
  const getDetailedAgentAnalysisFromContext = (): DetailedAgentAnalysis[] => {
    return agents.map((agentData) => {
      const agentName = agentData.name + ' Agent';
      
      // Map agent types to appropriate icons and colors
      const iconMap: Record<string, string> = {
        finance: 'DollarSign',
        risk: 'AlertTriangle', 
        compliance: 'Shield',
        market: 'TrendingUp'
      };

      const colorMap: Record<string, string> = {
        finance: 'text-green-500',
        risk: 'text-orange-500',
        compliance: 'text-blue-500', 
        market: 'text-purple-500'
      };

      // Create detailed analysis based on agent type and real performance data
      const baseAnalysis: DetailedAgentAnalysis = {
        id: agentData.id,
        name: agentName,
        icon: iconMap[agentData.id] || 'TrendingUp',
        iconColor: colorMap[agentData.id] || 'text-gray-500',
        recommendation: `Based on current analysis with ${agentData.performanceScore || 0}% confidence, this agent provides strategic insights for decision making.`
      };

      // Add type-specific data based on real performance
      const performance = agentData.performanceScore || 0;
      const usageCount = agentData.decisionsAnalyzed || 0;

      if (agentData.id === 'finance') {
        return {
          ...baseAnalysis,
          costImpact: `$${(performance * 50000).toLocaleString()}`,
          revenueImpact: `$${(performance * 100000).toLocaleString()}`,
          roiEstimate: `${(performance * 0.2).toFixed(1)}%`,
          budgetRequired: `$${(performance * 70000).toLocaleString()}`,
          recommendation: `Financial analysis shows ${performance}% confidence. ${usageCount > 0 ? `Completed ${usageCount} analysis cycles.` : 'Ready for analysis.'}`
        };
      }

      if (agentData.id === 'risk') {
        return {
          ...baseAnalysis,
          riskScore: `${Math.max(1, Math.round((100 - performance) / 5))}/100`,
          successProbability: `${performance}%`,
          riskFactors: performance > 80 ? ['Low market risk', 'Minimal operational risk'] : 
                      performance > 60 ? ['Moderate market conditions', 'Standard operational risks'] :
                      ['High market volatility', 'Operational challenges', 'Regulatory uncertainty'],
          recommendation: `Risk assessment confidence: ${performance}%. ${usageCount > 0 ? `Analyzed ${usageCount} scenarios.` : 'Awaiting scenario input.'}`
        };
      }

      if (agentData.id === 'compliance') {
        return {
          ...baseAnalysis,
          complianceScore: `${Math.max(1, Math.round(performance / 5))}/100`,
          legalConsiderations: performance > 80 ? ['Regulatory compliance verified', 'Legal framework clear'] :
                              performance > 60 ? ['Standard compliance requirements', 'Legal review recommended'] :
                              ['Complex regulatory environment', 'Legal expert consultation required'],
          recommendation: `Compliance analysis confidence: ${performance}%. ${usageCount > 0 ? `Reviewed ${usageCount} compliance aspects.` : 'Ready for compliance review.'}`
        };
      }

      if (agentData.id === 'market') {
        return {
          ...baseAnalysis,
          marketOpportunity: `${Math.max(0.1, (performance / 50)).toFixed(1)}/100`,
          marketTrends: performance > 80 ? ['Strong market conditions', 'Positive growth trends'] :
                       performance > 60 ? ['Stable market environment', 'Moderate growth potential'] :
                       ['Challenging market conditions', 'Market analysis required'],
          recommendation: `Market analysis confidence: ${performance}%. ${usageCount > 0 ? `Evaluated ${usageCount} market scenarios.` : 'Awaiting market data.'}`
        };
      }

      return baseAnalysis;
    });
  };

  // Calculate overall confidence based on agent performance
  const getOverallConfidence = (): number => {
    const agentPerformances = agents.map(agent => agent.performanceScore || 0);
    return agentPerformances.length > 0 
      ? Math.round(agentPerformances.reduce((sum, perf) => sum + perf, 0) / agentPerformances.length)
      : 0;
  };

  // Get active agents count
  const getActiveAgentsCount = (): number => {
    return agents.filter(agent => agent.status === 'active').length;
  };

  const analysisData = getDetailedAgentAnalysisFromContext();
  const overallConfidence = getOverallConfidence();
  const activeAgentsCount = getActiveAgentsCount();

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Left Panel - Strategic Decisions */}
      <div className="w-72 glass border-r-2 border-white/20 p-4 overflow-auto">
        <h3 className="font-semibold text-black mb-4 text-lg">Strategic Decisions</h3>
        
        <div className="space-y-3 mb-4">
          <Input
            placeholder="Search decisions..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className={
              searchTerm
                ? 'glass-input border-green-500/40 focus-enhanced'
                : 'glass-input hover:border-gray-500/30 focus-enhanced'
            }
          />
        </div>

        <div className="space-y-3">
          <div
            className="p-3 rounded-lg cursor-pointer transition-all duration-300 hover-lift group glass-card border-green-500/40 shadow-lg"
          >
            <h4 className="font-medium text-black group-hover:text-gray-800 transition-colors mb-2 text-sm">Live Analysis</h4>
            <div className="flex gap-2 mb-2">
              <Badge className="bg-green-100 text-green-800 text-xs">AI Powered</Badge>
              <Badge className="bg-blue-100 text-blue-800 text-xs">Real-time</Badge>
            </div>
            <p className="text-xs text-gray-600">Connect to Four Pillars AI backend</p>
          </div>
          
          <div className="p-3 rounded-lg glass-card border-2 border-white/20">
            <h4 className="font-medium text-black mb-2 text-sm">Current Analysis Session</h4>
            <div className="flex gap-2 mb-2">
              <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-600">
                Active Agents: {activeAgentsCount}
              </Badge>
              <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-600">
                Confidence: {overallConfidence}%
              </Badge>
            </div>
            <div className="text-xs text-gray-600">
              Real-time agent performance data
            </div>
          </div>
        </div>
      </div>

      {/* Right Panel - Decision Details */}
      <div className="flex-1 flex flex-col overflow-hidden">
        <div className="p-4 border-b border-white/20">
          <div className="flex items-center justify-between mb-3">
            <div>
              <h2 className="text-2xl font-bold text-black mb-1">AI Analysis Workspace</h2>
              <p className="text-gray-600 text-sm">Collaborative intelligence from your AI agent ecosystem</p>
            </div>
            <Button 
              onClick={handleNavigateToDashboard}
              className="bg-blue-500 hover:bg-blue-600 text-white font-medium px-4 py-2 rounded-lg flex items-center gap-2"
            >
              <span className="text-lg">📊</span>
              View Dashboard
            </Button>
          </div>

          <div className="mb-3">
            <h3 className="text-lg font-semibold text-black mb-1">AI Agent Analysis Workspace</h3>
            <p className="text-xs text-gray-600">
              {activeAgentsCount > 0 
                ? `Real-time analysis powered by Four Pillars AI agents - ${activeAgentsCount} agents active`
                : 'Use "New Strategic Decision" from the Dashboard to run AI analysis and see results here'
              }
            </p>
          </div>
        </div>

        <div className="flex-1 overflow-auto p-4">
          <Tabs defaultValue="analysis" className="w-full h-full">
            <TabsList className="glass mb-4 p-1 rounded-xl">
              <TabsTrigger value="analysis" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Historical Analysis
              </TabsTrigger>
              <TabsTrigger value="insights" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Collaborative Insights
              </TabsTrigger>
              <TabsTrigger value="tradeoffs" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Trade-off Matrix
              </TabsTrigger>
            </TabsList>

            <TabsContent value="analysis" className="h-full">
              <div className="grid grid-cols-1 xl:grid-cols-2 gap-4 h-full">
                {analysisData.map((analysis) => (
                  <DetailedAgentCard key={analysis.id} analysis={analysis} />
                ))}
              </div>
            </TabsContent>

            <TabsContent value="insights" className="space-y-8">
              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Consolidated Recommendation</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-600 mb-6 text-lg leading-relaxed">
                    {activeAgentsCount > 0 
                      ? (() => {
                          const avgConfidence = overallConfidence;
                          
                          if (avgConfidence >= 80) {
                            return `Based on comprehensive analysis from all ${activeAgentsCount} agents, the recommended approach is to proceed with the strategic initiative. The collective assessment shows strong viability across all dimensions with ${avgConfidence}% overall confidence. Financial projections indicate positive ROI potential, risk factors are manageable, compliance requirements are well-understood, and market conditions are favorable for implementation.`;
                          } else if (avgConfidence >= 60) {
                            return `Based on analysis from ${activeAgentsCount} active agents, the system recommends proceeding with cautious optimism and targeted risk mitigation measures. With ${avgConfidence}% overall confidence, the collective analysis suggests moderate viability that requires careful monitoring of identified risk factors and enhanced due diligence in areas showing lower confidence scores.`;
                          } else if (avgConfidence > 0) {
                            return `The collective analysis from ${activeAgentsCount} agents indicates significant challenges that require thorough reassessment before proceeding. With ${avgConfidence}% overall confidence, multiple factors need attention across financial, risk, compliance, and market dimensions. Consider revisiting the strategic approach or seeking additional expert consultation.`;
                          } else {
                            return "Awaiting comprehensive analysis from all agents to provide consolidated strategic recommendations.";
                          }
                        })()
                      : "Run AI analysis to generate consolidated recommendations from all agents based on your business scenario."
                    }
                  </p>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600 text-lg">Overall Confidence</span>
                      <span className="font-medium text-black text-xl">{overallConfidence}%</span>
                    </div>
                    <Progress value={overallConfidence} className="h-4 progress-enhanced" />
                  </div>
                </CardContent>
              </Card>

              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Key Insights</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-3 text-lg text-gray-600">
                    {activeAgentsCount > 0 ? (() => {
                      const financeAgent = agents.find(a => a.id === 'finance');
                      const riskAgent = agents.find(a => a.id === 'risk');
                      const complianceAgent = agents.find(a => a.id === 'compliance');
                      const marketAgent = agents.find(a => a.id === 'market');
                      
                      const financeScore = financeAgent?.performanceScore || 0;
                      const riskScore = riskAgent?.performanceScore || 0;
                      const complianceScore = complianceAgent?.performanceScore || 0;
                      const marketScore = marketAgent?.performanceScore || 0;
                      
                      const insights = [];
                      
                      // Cross-agent insights based on combined analysis
                      if (financeScore > 70 && marketScore > 70) {
                        insights.push({
                          color: 'bg-green-500',
                          text: `Financial and market analysis align positively - strong foundation for investment with projected ROI and favorable market conditions`
                        });
                      } else if (financeScore > 0 && marketScore > 0) {
                        insights.push({
                          color: 'bg-yellow-500',
                          text: `Financial and market factors require balanced consideration - moderate opportunity with careful planning needed`
                        });
                      }
                      
                      if (riskScore > 75 && complianceScore > 75) {
                        insights.push({
                          color: 'bg-blue-500',
                          text: `Risk and compliance assessments show strong alignment - regulatory framework supports low-risk implementation`
                        });
                      } else if (riskScore > 0 && complianceScore > 0) {
                        insights.push({
                          color: 'bg-orange-500',
                          text: `Risk and compliance factors need coordinated attention - structured mitigation approach recommended`
                        });
                      }
                      
                      // Strategic synthesis insights
                      if (overallConfidence >= 80) {
                        insights.push({
                          color: 'bg-purple-500',
                          text: `All agents converge on high-confidence recommendation - proceed with strategic implementation and monitoring protocols`
                        });
                      } else if (overallConfidence >= 60) {
                        insights.push({
                          color: 'bg-indigo-500',
                          text: `Agents indicate moderate consensus - phased approach with milestone reviews recommended for risk management`
                        });
                      } else if (overallConfidence > 0) {
                        insights.push({
                          color: 'bg-red-500',
                          text: `Agents identify significant concerns - comprehensive strategy revision needed before proceeding`
                        });
                      }
                      
                      // Cross-dimensional insights
                      const highPerformers = agents.filter(a => (a.performanceScore || 0) > 80);
                      const lowPerformers = agents.filter(a => (a.performanceScore || 0) < 60 && (a.performanceScore || 0) > 0);
                      
                      if (highPerformers.length >= 2) {
                        insights.push({
                          color: 'bg-emerald-500',
                          text: `Strong consensus across ${highPerformers.map(a => a.name.toLowerCase()).join(' and ')} dimensions - leverage these strengths for implementation`
                        });
                      }
                      
                      if (lowPerformers.length > 0) {
                        insights.push({
                          color: 'bg-amber-500',
                          text: `Focus required on ${lowPerformers.map(a => a.name.toLowerCase()).join(' and ')} considerations - address these factors before full commitment`
                        });
                      }
                      
                      return insights.length > 0 ? insights.map((insight, index) => (
                        <li key={index} className="flex items-center space-x-3">
                          <div className={`w-2 h-2 ${insight.color} rounded-full`}></div>
                          <span>{insight.text}</span>
                        </li>
                      )) : (
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-gray-400 rounded-full"></div>
                          <span>Complete analysis in progress - comprehensive insights will be available shortly</span>
                        </li>
                      );
                    })() : [
                      { color: 'bg-blue-500', text: 'Run AI analysis to generate comprehensive cross-agent insights' },
                      { color: 'bg-green-500', text: 'Collaborative intelligence will synthesize findings from all Four Pillars agents' },
                      { color: 'bg-purple-500', text: 'Strategic recommendations will emerge from multi-dimensional analysis' },
                      { color: 'bg-orange-500', text: 'Decision framework will incorporate financial, risk, compliance, and market factors' }
                    ].map((insight, index) => (
                      <li key={index} className="flex items-center space-x-3">
                        <div className={`w-2 h-2 ${insight.color} rounded-full`}></div>
                        <span>{insight.text}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>

              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Next Steps</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-3 text-lg text-gray-600">
                    {activeAgentsCount === 0 ? (
                      <>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                          <span>Run AI Analysis to activate agents</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                          <span>Input business scenario for analysis</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                          <span>Review agent recommendations</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-orange-500 rounded-full"></div>
                          <span>Make informed strategic decisions</span>
                        </li>
                      </>
                    ) : (
                      <>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                          <span>Review current agent analysis results</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                          <span>Monitor agent performance metrics</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                          <span>Execute recommended strategies</span>
                        </li>
                        <li className="flex items-center space-x-3">
                          <div className="w-2 h-2 bg-orange-500 rounded-full"></div>
                          <span>Schedule follow-up analysis</span>
                        </li>
                      </>
                    )}
                  </ul>
                </CardContent>
              </Card>

              {/* Agent Analysis Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {agents.filter(agent => agent.status === 'active').map((agent) => {
                  const analysisData = latestAnalysisData[agent.id];
                  
                  const agentConfig = {
                    finance: {
                      title: 'Financial Analysis',
                      icon: '💰',
                      color: 'border-green-200 bg-green-50',
                      iconColor: 'text-green-600'
                    },
                    risk: {
                      title: 'Risk Assessment',
                      icon: '🛡️',
                      color: 'border-red-200 bg-red-50',
                      iconColor: 'text-red-600'
                    },
                    compliance: {
                      title: 'Compliance Analysis',
                      icon: '⚖️',
                      color: 'border-blue-200 bg-blue-50',
                      iconColor: 'text-blue-600'
                    },
                    market: {
                      title: 'Market Intelligence',
                      icon: '📈',
                      color: 'border-purple-200 bg-purple-50',
                      iconColor: 'text-purple-600'
                    }
                  }[agent.id] || {
                    title: `${agent.name} Analysis`,
                    icon: '📊',
                    color: 'border-gray-200 bg-gray-50',
                    iconColor: 'text-gray-600'
                  };

                  return (
                    <Card key={agent.id} className={`glass-card interactive-border ${agentConfig.color}`}>
                      <CardHeader>
                        <CardTitle className="text-black text-lg flex items-center gap-2">
                          <span className="text-2xl">{agentConfig.icon}</span>
                          {agentConfig.title}
                          <Badge className={`ml-auto ${agent.performanceScore && agent.performanceScore >= 80 ? 'bg-green-100 text-green-800' : agent.performanceScore && agent.performanceScore >= 60 ? 'bg-yellow-100 text-yellow-800' : 'bg-red-100 text-red-800'}`}>
                            {agent.performanceScore || 0}%
                          </Badge>
                        </CardTitle>
                      </CardHeader>
                      <CardContent className="space-y-4">
                        {analysisData ? (
                          <>
                            {/* Analysis Summary */}
                            <div>
                              <h4 className="font-semibold text-black mb-2">Analysis</h4>
                              <p className="text-gray-700 text-sm leading-relaxed">
                                {analysisData.analysis || 'Analysis completed successfully'}
                              </p>
                            </div>

                            {/* Agent-specific Metrics */}
                            {agent.id === 'finance' && analysisData.metrics && (
                              <div className="space-y-2">
                                <h5 className="font-medium text-black">Financial Ratios</h5>
                                <div className="grid grid-cols-2 gap-2 text-sm">
                                  {Object.entries(analysisData.metrics).map(([key, value]) => (
                                    <div key={key} className="flex justify-between">
                                      <span className="text-gray-600 capitalize">{key.replace(/_/g, ' ')}:</span>
                                      <span className="font-medium">{typeof value === 'number' ? value.toFixed(2) : String(value)}</span>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            {agent.id === 'risk' && analysisData.risk_categories && (
                              <div className="space-y-2">
                                <h5 className="font-medium text-black">Risk Categories</h5>
                                <div className="space-y-1">
                                  {Object.entries(analysisData.risk_categories).map(([category, level]) => (
                                    <div key={category} className="flex justify-between text-sm">
                                      <span className="text-gray-600 capitalize">{category.replace(/_/g, ' ')}:</span>
                                      <Badge variant="outline" className={`text-xs ${level === 'low' ? 'text-green-600' : level === 'medium' ? 'text-yellow-600' : 'text-red-600'}`}>
                                        {String(level)}
                                      </Badge>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            {agent.id === 'compliance' && analysisData.compliance_scores && (
                              <div className="space-y-2">
                                <h5 className="font-medium text-black">Compliance Scores</h5>
                                <div className="space-y-1">
                                  {Object.entries(analysisData.compliance_scores).map(([area, score]) => (
                                    <div key={area} className="flex justify-between items-center text-sm">
                                      <span className="text-gray-600 capitalize">{area.replace(/_/g, ' ')}:</span>
                                      <div className="flex items-center gap-2">
                                        <Progress value={(score as number) * 100} className="w-16 h-2" />
                                        <span className="font-medium">{((score as number) * 100).toFixed(0)}%</span>
                                      </div>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            {agent.id === 'market' && analysisData.market_metrics && (
                              <div className="space-y-2">
                                <h5 className="font-medium text-black">Market Metrics</h5>
                                <div className="grid grid-cols-1 gap-2 text-sm">
                                  {Object.entries(analysisData.market_metrics).map(([metric, value]) => (
                                    <div key={metric} className="flex justify-between">
                                      <span className="text-gray-600 capitalize">{metric.replace(/_/g, ' ')}:</span>
                                      <span className="font-medium">{typeof value === 'number' ? value.toFixed(2) : String(value)}</span>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            {/* Data Sources */}
                            {analysisData.real_data && (
                              <div className="pt-2 border-t border-gray-200">
                                <h5 className="font-medium text-black mb-2 text-sm">Data Sources</h5>
                                <div className="flex flex-wrap gap-1">
                                  {Object.entries(analysisData.real_data).map(([source, data]) => (
                                    <Badge key={source} variant="outline" className="text-xs">
                                      {source.replace(/_/g, ' ')}: {Array.isArray(data) ? data.length : typeof data === 'object' && data !== null ? Object.keys(data).length : 1}
                                    </Badge>
                                  ))}
                                </div>
                              </div>
                            )}
                          </>
                        ) : (
                          <div className="text-center py-4">
                            <p className="text-gray-500 text-sm">Analysis data will appear here after running AI analysis</p>
                          </div>
                        )}
                      </CardContent>
                    </Card>
                  );
                })}
              </div>
            </TabsContent>

            <TabsContent value="tradeoffs" className="space-y-8">
              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl flex items-center gap-2">
                    <span className="text-2xl">⚖️</span>
                    Strategic Trade-off Matrix
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  {activeAgentsCount > 0 ? (
                    <div className="space-y-8">
                      {/* Investment vs. Risk Section */}
                      <div className="bg-gray-50 rounded-lg p-6">
                        <h3 className="text-lg font-semibold text-black mb-6">Investment vs. Risk</h3>
                        <div className="grid grid-cols-2 gap-8">
                          {/* Advantages */}
                          <div>
                            <h4 className="text-green-600 font-medium mb-4 flex items-center gap-2">
                              <span className="text-lg">📈</span>
                              Advantages
                            </h4>
                            <ul className="space-y-3">
                              {agents.filter(agent => agent.id === 'finance' || agent.id === 'market').map(agent => {
                                const performance = agent.performanceScore || 0;
                                let advantage = '';
                                if (agent.id === 'finance' && performance > 70) {
                                  advantage = 'Potential for high returns';
                                } else if (agent.id === 'market' && performance > 70) {
                                  advantage = 'Economic growth opportunities';
                                } else if (performance > 0) {
                                  advantage = `${agent.name} analysis shows positive indicators`;
                                }
                                
                                return advantage ? (
                                  <li key={agent.id} className="flex items-center gap-3 text-gray-700">
                                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                                    <span>{advantage}</span>
                                  </li>
                                ) : null;
                              })}
                              {agents.filter(agent => (agent.id === 'finance' || agent.id === 'market') && (agent.performanceScore || 0) > 70).length === 0 && (
                                <li className="text-gray-400 italic">Run analysis to identify investment advantages</li>
                              )}
                            </ul>
                          </div>
                          
                          {/* Disadvantages */}
                          <div>
                            <h4 className="text-red-600 font-medium mb-4 flex items-center gap-2">
                              <span className="text-lg">📉</span>
                              Disadvantages
                            </h4>
                            <ul className="space-y-3">
                              {agents.filter(agent => agent.id === 'risk').map(agent => {
                                const performance = agent.performanceScore || 0;
                                const riskFactors = performance < 80 ? [
                                  'Exposure to political and economic instability',
                                  'High initial capital investment'
                                ] : performance < 60 ? [
                                  'Market volatility concerns',
                                  'Regulatory uncertainty'
                                ] : [
                                  'Standard market risks',
                                  'Moderate capital requirements'
                                ];
                                
                                return riskFactors.map((factor, index) => (
                                  <li key={`${agent.id}-${index}`} className="flex items-center gap-3 text-gray-700">
                                    <div className="w-2 h-2 bg-red-500 rounded-full"></div>
                                    <span>{factor}</span>
                                  </li>
                                ));
                              })}
                              {agents.filter(agent => agent.id === 'risk').length === 0 && (
                                <li className="text-gray-400 italic">Run risk analysis to identify potential disadvantages</li>
                              )}
                            </ul>
                          </div>
                        </div>
                      </div>

                      {/* Compliance vs. Speed Section */}
                      <div className="bg-gray-50 rounded-lg p-6">
                        <h3 className="text-lg font-semibold text-black mb-6">Compliance vs. Speed</h3>
                        <div className="grid grid-cols-2 gap-8">
                          {/* Advantages */}
                          <div>
                            <h4 className="text-green-600 font-medium mb-4 flex items-center gap-2">
                              <span className="text-lg">📈</span>
                              Advantages
                            </h4>
                            <ul className="space-y-3">
                              {agents.filter(agent => agent.id === 'compliance').map(agent => {
                                const performance = agent.performanceScore || 0;
                                const advantages = performance > 80 ? [
                                  'Ensures legal operation',
                                  'Builds local trust'
                                ] : performance > 60 ? [
                                  'Standard regulatory compliance',
                                  'Established legal framework'
                                ] : [
                                  'Basic compliance measures',
                                  'Regulatory guidance available'
                                ];
                                
                                return advantages.map((advantage, index) => (
                                  <li key={`${agent.id}-adv-${index}`} className="flex items-center gap-3 text-gray-700">
                                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                                    <span>{advantage}</span>
                                  </li>
                                ));
                              })}
                              {agents.filter(agent => agent.id === 'compliance').length === 0 && (
                                <li className="text-gray-400 italic">Run compliance analysis to identify advantages</li>
                              )}
                            </ul>
                          </div>
                          
                          {/* Disadvantages */}
                          <div>
                            <h4 className="text-red-600 font-medium mb-4 flex items-center gap-2">
                              <span className="text-lg">📉</span>
                              Disadvantages
                            </h4>
                            <ul className="space-y-3">
                              {agents.filter(agent => agent.id === 'compliance').map(agent => {
                                const performance = agent.performanceScore || 0;
                                const disadvantages = performance < 80 ? [
                                  'Delays in project timeline',
                                  'Additional costs for legal processes'
                                ] : performance < 60 ? [
                                  'Extended approval processes',
                                  'Complex regulatory requirements'
                                ] : [
                                  'Standard processing time',
                                  'Routine compliance costs'
                                ];
                                
                                return disadvantages.map((disadvantage, index) => (
                                  <li key={`${agent.id}-dis-${index}`} className="flex items-center gap-3 text-gray-700">
                                    <div className="w-2 h-2 bg-red-500 rounded-full"></div>
                                    <span>{disadvantage}</span>
                                  </li>
                                ));
                              })}
                              {agents.filter(agent => agent.id === 'compliance').length === 0 && (
                                <li className="text-gray-400 italic">Run compliance analysis to identify potential delays</li>
                              )}
                            </ul>
                          </div>
                        </div>
                      </div>

                      {/* Impact vs Feasibility Matrix */}
                      <div className="bg-white rounded-lg border border-gray-200 p-6">
                        <h3 className="text-lg font-semibold text-black mb-6">Impact vs Feasibility Matrix</h3>
                        <div className="relative">
                          {/* Matrix Grid */}
                          <div className="bg-gray-50 rounded-lg p-8 relative" style={{ height: '300px' }}>
                            {/* Grid Lines */}
                            <div className="absolute inset-8 border-l-2 border-b-2 border-gray-300"></div>
                            <div className="absolute left-1/2 top-8 bottom-8 border-l border-gray-200 transform -translate-x-px"></div>
                            <div className="absolute top-1/2 left-8 right-8 border-t border-gray-200 transform -translate-y-px"></div>
                            
                            {/* Axis Labels */}
                            <div className="absolute bottom-2 left-1/2 transform -translate-x-1/2 text-sm text-gray-600">
                              Impact (Low → High)
                            </div>
                            <div className="absolute left-2 top-1/2 transform -rotate-90 -translate-y-1/2 text-sm text-gray-600 origin-center">
                              Feasibility (High → Low)
                            </div>
                            
                            {/* Quadrant Labels */}
                            <div className="absolute top-12 left-12 text-xs text-gray-500">Low Impact</div>
                            <div className="absolute top-12 right-12 text-xs text-gray-500">High Impact</div>
                            
                            {/* Agent Positioning */}
                            {agents.map((agent, index) => {
                              const performance = agent.performanceScore || 0;
                              const impact = performance; // Use performance as impact score
                              const feasibility = performance; // Use performance as feasibility score
                              
                              // Calculate position (percentage from left and top)
                              const leftPercent = Math.max(5, Math.min(95, (impact / 100) * 80 + 10));
                              const topPercent = Math.max(5, Math.min(95, ((100 - feasibility) / 100) * 80 + 10));
                              
                              const colors = [
                                { bg: 'bg-green-500', border: 'border-green-600' },
                                { bg: 'bg-blue-500', border: 'border-blue-600' },
                                { bg: 'bg-purple-500', border: 'border-purple-600' },
                                { bg: 'bg-orange-500', border: 'border-orange-600' }
                              ];
                              
                              return (
                                <div
                                  key={agent.id}
                                  className={`absolute w-8 h-8 ${colors[index % colors.length].bg} ${colors[index % colors.length].border} border-2 rounded-full flex items-center justify-center text-white text-xs font-bold shadow-lg`}
                                  style={{
                                    left: `${leftPercent}%`,
                                    top: `${topPercent}%`,
                                    transform: 'translate(-50%, -50%)'
                                  }}
                                  title={`${agent.name}: Impact ${impact}%, Feasibility ${feasibility}%`}
                                >
                                  {agent.name.charAt(0)}
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      </div>

                      {/* Decision Factors Summary */}
                      <div className="bg-white rounded-lg border border-gray-200 p-6">
                        <h3 className="text-lg font-semibold text-black mb-6">Decision Factors Summary</h3>
                        <div className="grid grid-cols-2 gap-8">
                          <div>
                            <h4 className="text-green-600 font-medium mb-4">Advantages</h4>
                            <ul className="space-y-2">
                              {agents.filter(agent => (agent.performanceScore || 0) > 75).map(agent => (
                                <li key={`summary-adv-${agent.id}`} className="flex items-center gap-2 text-gray-700">
                                  <div className="w-1 h-1 bg-green-500 rounded-full"></div>
                                  <span className="text-sm">{agent.name} analysis shows high confidence ({agent.performanceScore}%)</span>
                                </li>
                              ))}
                              {agents.filter(agent => (agent.performanceScore || 0) > 75).length === 0 && (
                                <li className="text-gray-400 text-sm italic">Run analysis to identify advantages</li>
                              )}
                            </ul>
                          </div>
                          <div>
                            <h4 className="text-orange-600 font-medium mb-4">Considerations</h4>
                            <ul className="space-y-2">
                              {agents.filter(agent => (agent.performanceScore || 0) < 75 && (agent.performanceScore || 0) > 0).map(agent => (
                                <li key={`summary-cons-${agent.id}`} className="flex items-center gap-2 text-gray-700">
                                  <div className="w-1 h-1 bg-orange-500 rounded-full"></div>
                                  <span className="text-sm">{agent.name} analysis requires attention ({agent.performanceScore}%)</span>
                                </li>
                              ))}
                              {agents.filter(agent => (agent.performanceScore || 0) < 75 && (agent.performanceScore || 0) > 0).length === 0 && (
                                <li className="text-gray-400 text-sm italic">No significant considerations identified</li>
                              )}
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  ) : (
                    <div className="text-center py-12">
                      <p className="text-gray-600 text-lg leading-relaxed mb-4">
                        Strategic Trade-off Matrix will be displayed here after running AI analysis.
                      </p>
                      <p className="text-gray-500 text-sm">
                        The matrix will show Investment vs. Risk, Compliance vs. Speed, and Impact vs. Feasibility analysis.
                      </p>
                    </div>
                  )}
                </CardContent>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </div>
    </div>
  );
}