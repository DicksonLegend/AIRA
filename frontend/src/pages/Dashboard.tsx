import React from 'react';
import { motion } from 'framer-motion';
import { Header } from '@/components/layout/Header';
import { KpiCard } from '@/components/ui/KpiCard';
import { AgentCard } from '@/components/ui/AgentCard';
import { DecisionTable } from '@/components/ui/DecisionTable';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { kpiMetrics, agents, decisions } from '@/data/mockData';

export function Dashboard() {
  const handleNewDecision = () => {
    console.log('New Strategic Decision');
  };

  return (
    <div className="flex flex-col h-full">
      <Header
        title="Executive Dashboard"
        subtitle="Strategic oversight and performance monitoring"
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

          {/* Agent Performance Cards */}
          <div>
            <h2 className="text-xl font-bold text-gray-900 mb-6">Agent Performance</h2>
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              {agents.map((agent, index) => (
                <motion.div
                  key={agent.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.3 + index * 0.1 }}
                >
                  <AgentCard agent={agent} />
                </motion.div>
              ))}
            </motion.div>
          </div>

          {/* Tables */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
            >
              <Card>
                <CardHeader>
                  <CardTitle>Active Strategic Decisions</CardTitle>
                </CardHeader>
                <CardContent>
                  <DecisionTable decisions={decisions.filter(d => d.status === 'active')} />
                </CardContent>
              </Card>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.5 }}
            >
              <Card>
                <CardHeader>
                  <CardTitle>Recent Completions</CardTitle>
                </CardHeader>
                <CardContent>
                  <DecisionTable decisions={decisions.filter(d => d.status === 'completed')} />
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </div>
    </div>
  );
}