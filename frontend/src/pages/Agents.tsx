<<<<<<< HEAD
import { useState } from 'react';
import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';
import { Switch } from '@/components/ui/switch';
import { Header } from '@/components/layout/Header';
import { DollarSign, Shield, CheckCircle, BarChart3, Settings, RotateCcw, Pause } from 'lucide-react';

const systemMetrics = [
  {
    title: 'OVERALL HEALTH',
    value: '94%',
    status: 'Excellent',
    statusColor: 'bg-green-100 text-green-700',
    icon: CheckCircle,
    iconColor: 'text-green-500',
  },
  {
    title: 'ACTIVE AGENTS',
    value: '4/4',
    status: 'Optimal',
    statusColor: 'bg-blue-100 text-blue-700',
    icon: CheckCircle,
    iconColor: 'text-blue-500',
  },
  {
    title: 'PROCESSING POWER',
    value: '87%',
    status: 'High',
    statusColor: 'bg-purple-100 text-purple-700',
    icon: BarChart3,
    iconColor: 'text-purple-500',
  },
  {
    title: 'SYSTEM LOAD',
    value: '23%',
    status: 'Low',
    statusColor: 'bg-orange-100 text-orange-700',
    icon: Shield,
    iconColor: 'text-orange-500',
  },
];

const agentData = [
  {
    id: 'finance',
    name: 'Finance Agent',
    description: 'Analyzes financial impact, ROI, and budget requirements',
    icon: DollarSign,
    iconColor: 'bg-green-500',
    status: 'Active',
    statusColor: 'bg-green-100 text-green-700',
    performanceScore: 94,
    capabilities: [
      { name: 'Cost Analysis', position: 'left' },
      { name: 'Revenue Projections', position: 'right' },
      { name: 'ROI Calculations', position: 'left' },
      { name: 'Budget Planning', position: 'right' },
    ],
    settings: {
      autoProcessing: true,
      highPriorityAlerts: true,
      learningMode: false,
    }
  },
  {
    id: 'risk',
    name: 'Risk Agent',
    description: 'Evaluates risks and develops mitigation strategies',
    icon: Shield,
    iconColor: 'bg-orange-500',
    status: 'Active',
    statusColor: 'bg-green-100 text-green-700',
    performanceScore: 91,
    capabilities: [
      { name: 'Risk Assessment', position: 'left' },
      { name: 'Mitigation Planning', position: 'right' },
      { name: 'Probability Analysis', position: 'left' },
      { name: 'Scenario Modeling', position: 'right' },
    ],
    settings: {
      autoProcessing: true,
      highPriorityAlerts: true,
      learningMode: false,
    }
  },
  {
    id: 'compliance',
    name: 'Compliance Agent',
    description: 'Ensures regulatory compliance and legal adherence',
    icon: CheckCircle,
    iconColor: 'bg-blue-500',
    status: 'Active',
    statusColor: 'bg-green-100 text-green-700',
    performanceScore: 96,
    capabilities: [
      { name: 'Regulatory Review', position: 'left' },
      { name: 'Legal Analysis', position: 'right' },
      { name: 'Compliance Scoring', position: 'left' },
      { name: 'Approval Tracking', position: 'right' },
    ],
    settings: {
      autoProcessing: true,
      highPriorityAlerts: true,
      learningMode: false,
    }
  },
  {
    id: 'market',
    name: 'Market Agent',
    description: 'Analyzes market opportunities and competitive landscape',
    icon: BarChart3,
    iconColor: 'bg-purple-500',
    status: 'Active',
    statusColor: 'bg-green-100 text-green-700',
    performanceScore: 89,
    capabilities: [
      { name: 'Market Research', position: 'left' },
      { name: 'Competitive Analysis', position: 'right' },
      { name: 'Trend Detection', position: 'left' },
      { name: 'Timing Assessment', position: 'right' },
    ],
    settings: {
      autoProcessing: true,
      highPriorityAlerts: true,
      learningMode: false,
    }
  },
];

export default function Agents() {
  const [agents, setAgents] = useState(agentData);

  const handleSettingChange = (agentId: string, setting: string, value: boolean) => {
    setAgents(prev => prev.map(agent => 
      agent.id === agentId 
        ? { ...agent, settings: { ...agent.settings, [setting]: value } }
        : agent
    ));
  };

  const handleSystemSettings = () => {
    console.log('System Settings');
  };

  return (
    <div className="flex min-h-screen bg-gradient-to-br from-gray-50 to-white">
      <div className="flex-1 flex flex-col">
        <Header
          title="Agent Management"
          subtitle="Configure and monitor your AI decision ecosystem"
          ctaLabel="System Settings"
          onCtaClick={handleSystemSettings}
        />
        
        <div className="flex-1 overflow-auto p-4 sm:p-6">
          <div className="space-y-8">
            {/* System Health KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6">
              {systemMetrics.map((metric, index) => (
                <motion.div
                  key={metric.title}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <Card className="glass-card border-0 hover-lift">
                    <CardContent className="p-4 lg:p-6">
                      <div className="flex items-center justify-between mb-4">
                        <div className="text-sm font-medium text-gray-600">{metric.title}</div>
                        <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                          metric.iconColor === 'text-green-500' ? 'bg-green-500' :
                          metric.iconColor === 'text-blue-500' ? 'bg-blue-500' :
                          metric.iconColor === 'text-purple-500' ? 'bg-purple-500' :
                          'bg-orange-500'
                        }`}>
                          <metric.icon className="w-5 h-5 text-white" />
                        </div>
                      </div>
                      <div className="text-3xl font-bold text-black mb-2">{metric.value}</div>
                      <Badge className={`${metric.statusColor} border-0 text-xs`}>
                        {metric.status}
                      </Badge>
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </div>

            {/* Agent Cards */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-8">
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
              {agents.map((agent, index) => (
                <motion.div
                  key={agent.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
<<<<<<< HEAD
                  transition={{ delay: (index + 4) * 0.1 }}
                >
                  <Card className="glass-card border-0 hover-lift">
                    <CardHeader className="pb-4">
                      <div className="flex items-center justify-between mb-4">
                        <div className="flex items-center space-x-3">
                          <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${agent.iconColor}`}>
                            <agent.icon className="w-6 h-6 text-white" />
                          </div>
                          <div>
                            <h3 className="text-xl font-semibold text-black">{agent.name}</h3>
                            <p className="text-sm text-gray-600">{agent.description}</p>
                          </div>
                        </div>
                        <Badge className={`${agent.statusColor} border-0`}>
                          {agent.status}
                        </Badge>
                      </div>
                    </CardHeader>
                    
                    <CardContent className="space-y-6">
                      {/* Performance Score */}
                      <div>
                        <div className="flex justify-between items-center mb-2">
                          <span className="text-sm font-medium text-gray-600">Performance Score</span>
                          <span className="text-lg font-bold text-black">{agent.performanceScore}%</span>
                        </div>
                        <Progress value={agent.performanceScore} className="h-2" />
                      </div>

                      {/* Core Capabilities */}
                      <div>
                        <h4 className="text-sm font-medium text-gray-600 mb-3">Core Capabilities</h4>
                        <div className="grid grid-cols-2 gap-y-2 gap-x-4">
                          {agent.capabilities.map((capability, index) => (
                            <div key={index} className="text-sm text-gray-700">
                              {capability.name}
                            </div>
                          ))}
                        </div>
                      </div>

                      {/* Settings */}
                      <div className="space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="text-sm text-gray-700">Enable Auto-Processing</span>
                          <Switch 
                            checked={agent.settings.autoProcessing}
                            onCheckedChange={(checked) => handleSettingChange(agent.id, 'autoProcessing', checked)}
                          />
                        </div>
                        <div className="flex items-center justify-between">
                          <span className="text-sm text-gray-700">High Priority Alerts</span>
                          <Switch 
                            checked={agent.settings.highPriorityAlerts}
                            onCheckedChange={(checked) => handleSettingChange(agent.id, 'highPriorityAlerts', checked)}
                          />
                        </div>
                        <div className="flex items-center justify-between">
                          <span className="text-sm text-gray-700">Learning Mode</span>
                          <Switch 
                            checked={agent.settings.learningMode}
                            onCheckedChange={(checked) => handleSettingChange(agent.id, 'learningMode', checked)}
                          />
                        </div>
                      </div>

                      {/* Action Buttons */}
                      <div className="flex space-x-2 pt-4 border-t border-gray-200/50">
                        <Button variant="outline" size="sm" className="glass-button flex-1 flex items-center justify-center gap-2 hover-lift">
                          <Settings className="w-4 h-4" />
                          Configure
                        </Button>
                        <Button variant="outline" size="sm" className="glass-button flex-1 flex items-center justify-center gap-2 hover-lift">
                          <RotateCcw className="w-4 h-4" />
                          Restart
                        </Button>
                        <Button variant="outline" size="sm" className="glass-button flex-1 flex items-center justify-center gap-2 hover-lift">
                          <Pause className="w-4 h-4" />
                          Pause
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </div>
          </div>
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
        </div>
      </div>
    </div>
  );
}