import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
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
        </div>
      </CardContent>
    </Card>
  );
}