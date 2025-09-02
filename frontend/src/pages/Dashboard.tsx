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
    <div className="flex min-h-screen">
      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        <Header
          title="Executive Dashboard"
          subtitle="Real-time insights from your AI decision ecosystem"
          ctaLabel="New Strategic Decision"
          onCtaClick={handleNewDecision}
        />
        <div className="flex-1 overflow-auto p-4 sm:p-6">
          <div className="space-y-6">
            {/* KPI Cards */}
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4"
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

            {/* Agent Performance Section */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
            >
              <h2 className="text-xl font-bold text-black mb-4">Agent Performance</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                {agents.map((agent, index) => (
                  <motion.div
                    key={agent.id}
                    className="glass-card hover-lift p-4 rounded-xl"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.5 + index * 0.1 }}
                  >
                    <div className="flex items-center mb-3">
                      <div className="w-10 h-10 glass rounded-lg flex items-center justify-center mr-3">
                        {agent.icon === 'DollarSign' && <span className="text-green-500 text-lg">$</span>}
                        {agent.icon === 'Shield' && <span className="text-blue-500 text-lg">🛡️</span>}
                        {agent.icon === 'AlertTriangle' && <span className="text-yellow-500 text-lg">⚠️</span>}
                        {agent.icon === 'TrendingUp' && <span className="text-purple-500 text-lg">📈</span>}
                      </div>
                      <div className="flex-1">
                        <span className="font-semibold text-base text-black">{agent.name}</span>
                        <span className={`ml-2 px-2 py-1 rounded-full text-xs font-medium ${
                          agent.status === 'active' ? 'bg-green-100 text-green-700' : 
                          agent.status === 'analyzing' ? 'bg-yellow-100 text-yellow-700' : 
                          'bg-gray-100 text-gray-500'
                        }`}>
                          {agent.status}
                        </span>
                      </div>
                    </div>
                    <p className="text-sm text-gray-600 mb-3">{agent.description}</p>
                    <div className="space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-gray-500">Performance</span>
                        <span className="font-bold text-black text-sm">{agent.performance}%</span>
                      </div>
                      <div className="w-full h-2 glass rounded-full overflow-hidden">
                        <div 
                          className="h-full bg-gradient-to-r from-green-400 to-green-600 transition-all duration-500 ease-out rounded-full" 
                          style={{ width: `${agent.performance}%` }}
                        />
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-gray-500">Decisions Analyzed</span>
                        <span className="font-bold text-black text-sm">{agent.decisionsAnalyzed}</span>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </motion.div>

            {/* Strategic Decisions Section */}
            <motion.div
              className="grid grid-cols-1 xl:grid-cols-2 gap-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.8 }}
            >
              <Card className="glass-card interactive-border hover-lift">
                <CardHeader className="pb-3">
                  <CardTitle className="text-black flex items-center gap-2 text-lg">
                    <span className="text-yellow-500">⚡</span>
                    Active Strategic Decisions
                  </CardTitle>
                </CardHeader>
                <CardContent className="max-h-80 overflow-y-auto">
                  <DecisionTable decisions={activeDecisions} />
                </CardContent>
              </Card>

              <Card className="glass-card interactive-border hover-lift">
                <CardHeader className="pb-3">
                  <CardTitle className="text-black flex items-center gap-2 text-lg">
                    <span className="text-green-500">✓</span>
                    Recent Completions
                  </CardTitle>
                </CardHeader>
                <CardContent className="max-h-80 overflow-y-auto">
                  <DecisionTable decisions={completedDecisions} />
                </CardContent>
              </Card>
            </motion.div>
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