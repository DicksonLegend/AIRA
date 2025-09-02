import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';
import { 
  LayoutDashboard, 
  Microscope, 
  FileText, 
  Settings,
  DollarSign,
  Shield,
  AlertTriangle,
  TrendingUp,
  User
} from 'lucide-react';
import { cn } from '@/lib/utils';
import { agents } from '@/data/mockData';

const navigation = [
  { name: 'Executive Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Analysis Workspace', href: '/workspace', icon: Microscope },
  { name: 'Strategic Reports', href: '/reports', icon: FileText },
  { name: 'Agent Management', href: '/agents', icon: Settings }
];

const agentIcons = {
  finance: DollarSign,
  risk: Shield,
  compliance: AlertTriangle,
  market: TrendingUp
};

const statusColors = {
  active: 'bg-green-500',
  analyzing: 'bg-yellow-500',
  inactive: 'bg-gray-400'
};

export function Sidebar() {
  const location = useLocation();

  return (
    <div className="w-64 bg-gray-900 text-white h-screen flex flex-col">
      {/* Logo & Title */}
      <div className="p-6 border-b border-gray-700">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
            <span className="font-bold text-sm">AI</span>
          </div>
          <div>
            <h1 className="font-bold text-lg">AIRA</h1>
            <p className="text-xs text-gray-400">AI DECISION ECOSYSTEM</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex-1 p-4">
        <nav className="space-y-2">
          {navigation.map((item) => {
            const isActive = location.pathname === item.href;
            const Icon = item.icon;
            
            return (
              <Link
                key={item.name}
                to={item.href}
                className={cn(
                  "flex items-center space-x-3 px-4 py-3 rounded-lg transition-all relative",
                  isActive 
                    ? "bg-blue-600 text-white" 
                    : "text-gray-300 hover:bg-gray-800 hover:text-white"
                )}
              >
                {isActive && (
                  <motion.div
                    layoutId="activeTab"
                    className="absolute inset-0 bg-blue-600 rounded-lg"
                    initial={false}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
                <Icon className="w-5 h-5 relative z-10" />
                <span className="font-medium relative z-10">{item.name}</span>
              </Link>
            );
          })}
        </nav>

        {/* Agent Status List */}
        <div className="mt-8">
          <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4">
            Agent Status
          </h3>
          <div className="space-y-3">
            {agents.map((agent) => {
              const Icon = agentIcons[agent.id as keyof typeof agentIcons];
              
              return (
                <div key={agent.id} className="flex items-center space-x-3 px-4 py-2">
                  <Icon className="w-4 h-4 text-gray-400" />
                  <span className="text-sm text-gray-300 flex-1">{agent.name}</span>
                  <div className={cn("w-2 h-2 rounded-full", statusColors[agent.status])} />
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* User Profile */}
      <div className="p-4 border-t border-gray-700">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-gray-600 rounded-full flex items-center justify-center">
            <User className="w-4 h-4" />
          </div>
          <div>
            <p className="text-sm font-medium">Sarah Chen</p>
            <p className="text-xs text-gray-400">Strategic Director</p>
          </div>
        </div>
      </div>
    </div>
  );
}