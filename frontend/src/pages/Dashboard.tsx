import { useState } from 'react';
import { motion } from 'framer-motion';
import { Header } from '@/components/layout/Header';
import { KpiCard } from '@/components/ui/KpiCard';
import { DecisionTable } from '@/components/ui/DecisionTable';
import { CreateDecisionModal } from '@/components/ui/CreateDecisionModal';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { kpiMetrics, agents, decisions } from '@/data/mockData';
import { Decision } from '@/types';

export function Dashboard() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [allDecisions, setAllDecisions] = useState(decisions);

  const handleNewDecision = () => {
    setIsModalOpen(true);
  };

  const handleCreateDecision = (newDecision: {
    title: string;
    description: string;
    priority: 'high' | 'medium' | 'low';
    deadline: string;
    agents: string[];
  }) => {
    const decision: Decision = {
      id: String(allDecisions.length + 1),
      title: newDecision.title,
      priority: newDecision.priority,
      status: 'active',
      confidence: Math.floor(Math.random() * 20) + 75, // Random confidence between 75-95
      createdAt: new Date().toLocaleDateString(),
      agents: newDecision.agents,
    };

    setAllDecisions(prev => [decision, ...prev]);
  };

  const activeDecisions = allDecisions.filter(d => d.status === 'active');
  const completedDecisions = allDecisions.filter(d => d.status === 'completed');

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar */}
      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        <Header
          title="Executive Dashboard"
          subtitle="Real-time insights from your AI decision ecosystem"
          ctaLabel="New Strategic Decision"
          onCtaClick={handleNewDecision}
        />
        <div className="flex-1 overflow-auto p-6">
          <div className="space-y-8">
            {/* KPI Cards */}
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, staggerChildren: 0.1 }}
            >
              {kpiMetrics.map((metric, index) => (
                <motion.div
                  key={metric.title}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <KpiCard metric={metric} />
                </motion.div>
              ))}
            </motion.div>

            {/* Agent Performance Section - Clean Card Layout */}
            <div className="">
              <h2 className="text-xl font-bold text-black mb-6">Agent Performance</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                {agents.map((agent) => (
                  <div key={agent.id} className="bg-white rounded-xl shadow p-6 flex flex-col items-start">
                    <div className="flex items-center mb-2">
                      <div className="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center mr-3">
                        {/* Icon */}
                        {agent.icon === 'DollarSign' && <span className="text-green-500 text-xl">$</span>}
                        {agent.icon === 'Shield' && <span className="text-blue-500 text-xl">🛡️</span>}
                        {agent.icon === 'AlertTriangle' && <span className="text-yellow-500 text-xl">⚠️</span>}
                        {agent.icon === 'TrendingUp' && <span className="text-purple-500 text-xl">📈</span>}
                      </div>
                      <span className="font-semibold text-lg text-black mr-2">{agent.name}</span>
                      <span className={`px-2 py-1 rounded text-xs font-medium ml-auto ${agent.status === 'active' ? 'bg-green-100 text-green-700' : agent.status === 'analyzing' ? 'bg-yellow-100 text-yellow-700' : 'bg-gray-100 text-gray-500'}`}>{agent.status}</span>
                    </div>
                    <p className="text-sm text-gray-500 mb-4">{agent.description}</p>
                    <div className="flex items-center w-full mb-2">
                      <span className="text-xs text-gray-500 mr-2">Performance</span>
                      <span className="font-bold text-black text-sm">{agent.performance}%</span>
                    </div>
                    <div className="w-full h-2 bg-gray-200 rounded mb-2">
                      <div className="h-2 rounded bg-green-500" style={{ width: `${agent.performance}%` }}></div>
                    </div>
                    <div className="flex items-center w-full">
                      <span className="text-xs text-gray-500 mr-2">Decisions Analyzed</span>
                      <span className="font-bold text-black text-sm">{agent.decisionsAnalyzed}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Strategic Decisions Section with Scroll */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card className="glass-card border-gray-600/20 max-h-[400px] overflow-y-auto">
                <CardHeader>
                  <CardTitle className="text-black flex items-center gap-2">
                    <span className="text-yellow-500"><svg width="24" height="24" fill="none" viewBox="0 0 24 24"><path d="M12 2v2m0 16v2m8-10h2M2 12H4m15.07-7.07l1.42 1.42M4.93 19.07l1.42-1.42M19.07 19.07l-1.42-1.42M4.93 4.93l-1.42 1.42" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/></svg></span>
                    Active Strategic Decisions
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <DecisionTable decisions={activeDecisions} />
                </CardContent>
              </Card>

              <Card className="glass-card border-gray-600/20 max-h-[400px] overflow-y-auto">
                <CardHeader>
                  <CardTitle className="text-black flex items-center gap-2">
                    <span className="text-green-500"><svg width="24" height="24" fill="none" viewBox="0 0 24 24"><path d="M9 12l2 2l4-4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/></svg></span>
                    Recent Completions
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <DecisionTable decisions={completedDecisions} />
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </div>
      
      <CreateDecisionModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onCreateDecision={handleCreateDecision}
      />
    </div>
  );
}