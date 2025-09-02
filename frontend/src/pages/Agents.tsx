import React from 'react';
import { motion } from 'framer-motion';
import { Header } from '@/components/layout/Header';
import { AgentCard } from '@/components/ui/AgentCard';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Switch } from '@/components/ui/switch';
import { Progress } from '@/components/ui/progress';
import { Activity, Cpu, Zap, Server } from 'lucide-react';
import { agents, systemHealth } from '@/data/mockData';

export function Agents() {
  const handleConfigure = () => {
    console.log('Configure system');
  };

  const healthMetrics = [
    { title: 'Overall Health', value: systemHealth.overall, icon: Activity, color: 'text-green-600' },
    { title: 'Active Agents', value: systemHealth.activeAgents, icon: Cpu, color: 'text-blue-600' },
    { title: 'Processing Power', value: systemHealth.processingPower, icon: Zap, color: 'text-yellow-600' },
    { title: 'System Load', value: systemHealth.systemLoad, icon: Server, color: 'text-purple-600' }
  ];

  const systemConfigs = [
    { label: 'Auto-Analysis', description: 'Automatically analyze new decisions', enabled: true },
    { label: 'Collaborative Mode', description: 'Enable cross-agent collaboration', enabled: true },
    { label: 'Notifications', description: 'Real-time alerts and updates', enabled: false },
    { label: 'External Data', description: 'Access external data sources', enabled: true },
    { label: 'Advanced Analytics', description: 'Deep learning insights', enabled: true },
    { label: 'Performance Monitoring', description: 'Real-time performance tracking', enabled: true }
  ];

  return (
    <div className="flex flex-col h-full">
      <Header
        title="Agent Management"
        subtitle="AI agent monitoring and system configuration"
        ctaLabel="Configure System"
        onCtaClick={handleConfigure}
      />
      
      <div className="flex-1 overflow-auto p-6">
        <div className="space-y-8">
          {/* System Health Cards */}
          <div>
            <h2 className="text-xl font-bold text-gray-900 mb-6">System Health</h2>
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              {healthMetrics.map((metric, index) => {
                const Icon = metric.icon;
                return (
                  <motion.div
                    key={metric.title}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <Card>
                      <CardContent className="p-6">
                        <div className="flex items-center space-x-3 mb-3">
                          <Icon className={`w-5 h-5 ${metric.color}`} />
                          <h3 className="font-medium text-gray-900">{metric.title}</h3>
                        </div>
                        <p className="text-2xl font-bold text-gray-900 mb-2">
                          {typeof metric.value === 'number' && metric.title !== 'Active Agents' 
                            ? `${metric.value}%` 
                            : metric.value}
                        </p>
                        {typeof metric.value === 'number' && metric.title !== 'Active Agents' && (
                          <Progress value={metric.value} className="h-2" />
                        )}
                      </CardContent>
                    </Card>
                  </motion.div>
                );
              })}
            </motion.div>
          </div>

          {/* Individual Agent Cards */}
          <div>
            <h2 className="text-xl font-bold text-gray-900 mb-6">Agent Configuration</h2>
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 gap-6"
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
                  <AgentCard agent={agent} showControls />
                </motion.div>
              ))}
            </motion.div>
          </div>

          {/* System Configuration */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            <Card>
              <CardHeader>
                <CardTitle>System Configuration</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {systemConfigs.map((config) => (
                    <div key={config.label} className="flex items-center justify-between py-2">
                      <div>
                        <p className="font-medium text-gray-900">{config.label}</p>
                        <p className="text-sm text-gray-600">{config.description}</p>
                      </div>
                      <Switch defaultChecked={config.enabled} />
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </motion.div>
        </div>
      </div>
    </div>
  );
}