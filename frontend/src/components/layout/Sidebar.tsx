<<<<<<< HEAD
=======
import React from 'react';
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
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
<<<<<<< HEAD
    <div className="w-64 glass-dark h-screen flex flex-col border-r-2 border-white/10 overflow-hidden">
      {/* Logo & Title */}
      <div className="p-6 border-b-2 border-white/10 flex-shrink-0">
        <div className="flex items-center space-x-3">
          <div className="w-12 h-12 rounded-xl flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105 overflow-hidden bg-white/10">
            <img 
              src="/Screenshot 2025-09-02 102251.png" 
              alt="AIRA Logo" 
              className="w-10 h-10 object-contain rounded-lg"
            />
          </div>
          <div>
            <h1 className="font-bold text-xl text-white">AIRA</h1>
            <p className="text-xs text-gray-300">AI DECISION ECOSYSTEM</p>
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
          </div>
        </div>
      </div>

<<<<<<< HEAD
      {/* Scrollable Content */}
      <div className="flex-1 overflow-y-auto p-4">
        {/* Navigation */}
        <nav className="space-y-2 mb-8">
          <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4">
            Navigation
          </h3>
=======
      {/* Navigation */}
      <div className="flex-1 p-4">
        <nav className="space-y-2">
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
          {navigation.map((item) => {
            const isActive = location.pathname === item.href;
            const Icon = item.icon;
            
            return (
              <Link
                key={item.name}
                to={item.href}
                className={cn(
<<<<<<< HEAD
                  "flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-300 relative group",
                  isActive 
                    ? "accent-button text-white shadow-lg" 
                    : "text-gray-300 hover:text-white hover:bg-white/10 border border-transparent hover:border-white/20"
=======
                  "flex items-center space-x-3 px-4 py-3 rounded-lg transition-all relative",
                  isActive 
                    ? "bg-blue-600 text-white" 
                    : "text-gray-300 hover:bg-gray-800 hover:text-white"
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
                )}
              >
                {isActive && (
                  <motion.div
                    layoutId="activeTab"
<<<<<<< HEAD
                    className="absolute inset-0 accent-button rounded-xl"
=======
                    className="absolute inset-0 bg-blue-600 rounded-lg"
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
                    initial={false}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
<<<<<<< HEAD
                <Icon className="w-5 h-5 relative z-10 group-hover:scale-110 transition-transform" />
                <span className="font-medium relative z-10 group-hover:scale-105 transition-transform">{item.name}</span>
=======
                <Icon className="w-5 h-5 relative z-10" />
                <span className="font-medium relative z-10">{item.name}</span>
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
              </Link>
            );
          })}
        </nav>

        {/* Agent Status List */}
<<<<<<< HEAD
        <div>
          <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4">
            AI Agents Status
=======
        <div className="mt-8">
          <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4">
            Agent Status
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
          </h3>
          <div className="space-y-3">
            {agents.map((agent) => {
              const Icon = agentIcons[agent.id as keyof typeof agentIcons];
              
              return (
<<<<<<< HEAD
                <div key={agent.id} className="flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-white/10 transition-all duration-300 group cursor-pointer border border-transparent hover:border-white/20">
                  <Icon className="w-4 h-4 text-gray-400 group-hover:text-white transition-colors group-hover:scale-110" />
                  <span className="text-sm text-gray-300 group-hover:text-white transition-colors flex-1">{agent.name} Agent</span>
                  <div className="flex items-center space-x-2">
                    <span className="text-xs text-gray-400 capitalize">{agent.status}</span>
                    <div className={cn("w-3 h-3 rounded-full shadow-sm transition-all duration-300 group-hover:scale-110", statusColors[agent.status])} />
                  </div>
=======
                <div key={agent.id} className="flex items-center space-x-3 px-4 py-2">
                  <Icon className="w-4 h-4 text-gray-400" />
                  <span className="text-sm text-gray-300 flex-1">{agent.name}</span>
                  <div className={cn("w-2 h-2 rounded-full", statusColors[agent.status])} />
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
                </div>
              );
            })}
          </div>
        </div>
      </div>

<<<<<<< HEAD
      {/* User Profile - Fixed at bottom */}
      <div className="p-4 border-t border-white/10 flex-shrink-0">
        <div className="flex items-center space-x-3 p-3 rounded-lg bg-white/5">
          <div className="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
            <User className="w-4 h-4 text-white" />
          </div>
          <div>
            <p className="text-sm font-medium text-white">Enterprise Admin</p>
            <p className="text-xs text-gray-400">Strategic Decision Maker</p>
=======
      {/* User Profile */}
      <div className="p-4 border-t border-gray-700">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-gray-600 rounded-full flex items-center justify-center">
            <User className="w-4 h-4" />
          </div>
          <div>
            <p className="text-sm font-medium">Sarah Chen</p>
            <p className="text-xs text-gray-400">Strategic Director</p>
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
          </div>
        </div>
      </div>
    </div>
  );
}