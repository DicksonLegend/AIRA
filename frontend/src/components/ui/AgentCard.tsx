import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
<<<<<<< HEAD
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';
import { Switch } from '@/components/ui/switch';
import { Zap, Shield, AlertTriangle, TrendingUp, DollarSign } from 'lucide-react';
import { Agent } from '@/types';

const statusStyles = {
  active: 'bg-green-500/20 text-green-600 border-green-500/30',
  inactive: 'bg-gray-400/20 text-gray-600 border-gray-400/30',
  analyzing: 'bg-blue-400/20 text-blue-600 border-blue-400/30',
};

const iconComponents: Record<string, React.ComponentType<{ className?: string }>> = {
  Zap,
  Shield,
  AlertTriangle,
  TrendingUp,
  DollarSign,
};

export function AgentCard({ agent }: { agent: Agent }) {
  const IconComponent = iconComponents[agent.icon] || Zap;

  return (
    <Card className="glass-card hover-lift interactive-border cursor-pointer group">
      <CardHeader className="pb-3">
        <div className="flex items-center space-x-3">
          <div className="w-12 h-12 bg-gradient-to-r from-gray-500 to-gray-600 rounded-xl flex items-center justify-center shadow-lg group-hover:shadow-xl transition-all duration-300 group-hover:scale-110">
            <IconComponent className="w-6 h-6 text-white" />
          </div>
          <div className="flex-1">
            <CardTitle className="text-lg text-black group-hover:text-gray-800 transition-colors">{agent.name}</CardTitle>
            <p className="text-sm text-gray-600 group-hover:text-gray-700 transition-colors">{agent.description}</p>
          </div>
          <Badge className={`${statusStyles[agent.status]} transition-all duration-300 group-hover:scale-105`}>
            {agent.status}
          </Badge>
        </div>
      </CardHeader>
      
      <CardContent className="space-y-4">
        <div className="flex items-center justify-between">
          <span className="text-gray-600 group-hover:text-gray-700 transition-colors">Performance</span>
          <span className="font-medium text-black group-hover:text-gray-800 transition-colors">{agent.performance}%</span>
        </div>
        <Progress value={agent.performance} className="h-3 progress-enhanced" />
        
        <div className="flex items-center justify-between">
          <span className="text-gray-600 group-hover:text-gray-700 transition-colors">Decisions Analyzed</span>
          <span className="font-medium text-black group-hover:text-gray-800 transition-colors">{agent.decisionsAnalyzed}</span>
        </div>
        
        <div className="space-y-3 pt-4 border-t border-gray-200/50 group-hover:border-gray-300/50 transition-colors">
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600 group-hover:text-gray-700 transition-colors">Auto-Processing</span>
            <Switch defaultChecked className="group-hover:scale-110 transition-transform" />
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600 group-hover:text-gray-700 transition-colors">High Priority Alerts</span>
            <Switch defaultChecked className="group-hover:scale-110 transition-transform" />
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600 group-hover:text-gray-700 transition-colors">Learning Mode</span>
            <Switch className="group-hover:scale-110 transition-transform" />
          </div>
        </div>
        
        <div className="flex space-x-2 pt-2">
          <Button variant="outline" size="sm" className="flex-1 glass-button text-black border-gray-500/30 hover:border-gray-500/50 hover:bg-gray-50/50 transition-all duration-300">
            Configure
          </Button>
          <Button variant="outline" size="sm" className="flex-1 glass-button text-black border-gray-500/30 hover:border-gray-500/50 hover:bg-gray-50/50 transition-all duration-300">
            View Logs
          </Button>
=======
import { Progress } from '@/components/ui/progress';
import { Switch } from '@/components/ui/switch';
import { Button } from '@/components/ui/button';
import { 
  DollarSign, 
  Shield, 
  AlertTriangle, 
  TrendingUp,
  Settings,
  Play,
  Pause
} from 'lucide-react';
import { Agent } from '@/types';

const agentIcons = {
  finance: DollarSign,
  risk: Shield,
  compliance: AlertTriangle,
  market: TrendingUp
};

const statusColors = {
  active: 'bg-green-100 text-green-800',
  analyzing: 'bg-yellow-100 text-yellow-800',
  inactive: 'bg-gray-100 text-gray-800'
};

interface AgentCardProps {
  agent: Agent;
  showControls?: boolean;
}

export function AgentCard({ agent, showControls = false }: AgentCardProps) {
  const Icon = agentIcons[agent.id as keyof typeof agentIcons];

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <Icon className="w-5 h-5 text-blue-600" />
            </div>
            <div>
              <CardTitle className="text-lg">{agent.name}</CardTitle>
              <p className="text-sm text-gray-600">{agent.description}</p>
            </div>
          </div>
          <span className={`px-2 py-1 text-xs font-medium rounded-full ${statusColors[agent.status]}`}>
            {agent.status}
          </span>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div>
            <div className="flex justify-between text-sm mb-2">
              <span className="text-gray-600">Performance</span>
              <span className="font-medium">{agent.performance}%</span>
            </div>
            <Progress value={agent.performance} className="h-2" />
          </div>
          
          <div className="flex justify-between text-sm">
            <span className="text-gray-600">Decisions Analyzed</span>
            <span className="font-medium">{agent.decisionsAnalyzed}</span>
          </div>

          {showControls && (
            <div className="space-y-3 pt-4 border-t">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Auto-Processing</span>
                <Switch defaultChecked />
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">High Priority Alerts</span>
                <Switch defaultChecked />
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Learning Mode</span>
                <Switch />
              </div>
              
              <div className="flex space-x-2 pt-2">
                <Button variant="outline" size="sm" className="flex-1">
                  <Settings className="w-4 h-4 mr-1" />
                  Configure
                </Button>
                <Button variant="outline" size="sm" className="flex-1">
                  <Pause className="w-4 h-4 mr-1" />
                  Pause
                </Button>
              </div>
            </div>
          )}
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
        </div>
      </CardContent>
    </Card>
  );
}