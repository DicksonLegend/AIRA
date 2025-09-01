import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Header } from '@/components/layout/Header';
import { AgentCard } from '@/components/ui/AgentCard';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Progress } from '@/components/ui/progress';
import { Badge } from '@/components/ui/badge';
import { decisions, agents } from '@/data/mockData';

export function Workspace() {
  const [selectedDecision, setSelectedDecision] = useState(decisions[0]);

  const handleRunAnalysis = () => {
    console.log('Run AI Analysis');
  };

  return (
    <div className="flex flex-col h-full">
      <Header
        title="Analysis Workspace"
        subtitle="Collaborative AI analysis and decision insights"
        ctaLabel="Run AI Analysis"
        onCtaClick={handleRunAnalysis}
      />
      
      <div className="flex-1 overflow-hidden">
        <div className="flex h-full">
          {/* Left Panel - Decisions List */}
          <div className="w-80 bg-white border-r border-gray-200 p-4 overflow-auto">
            <h3 className="font-semibold text-gray-900 mb-4">Strategic Decisions</h3>
            <div className="space-y-3">
              {decisions.map((decision) => (
                <motion.div
                  key={decision.id}
                  className={`p-4 rounded-lg border cursor-pointer transition-all ${
                    selectedDecision.id === decision.id 
                      ? 'border-blue-500 bg-blue-50' 
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                  onClick={() => setSelectedDecision(decision)}
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  <h4 className="font-medium text-gray-900 mb-2">{decision.title}</h4>
                  <div className="flex items-center space-x-2 mb-2">
                    <Badge variant="outline" className="text-xs">
                      {decision.priority}
                    </Badge>
                    <Badge variant="outline" className="text-xs">
                      {decision.status}
                    </Badge>
                  </div>
                  <div className="text-xs text-gray-500">
                    Confidence: {decision.confidence}%
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Right Panel - Decision Details */}
          <div className="flex-1 p-6 overflow-auto">
            <motion.div
              key={selectedDecision.id}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.3 }}
            >
              {/* Decision Header */}
              <div className="mb-6">
                <h2 className="text-2xl font-bold text-gray-900 mb-2">
                  {selectedDecision.title}
                </h2>
                <div className="flex items-center space-x-4">
                  <Badge className="capitalize">{selectedDecision.status}</Badge>
                  <span className="text-sm text-gray-600">
                    Created {new Date(selectedDecision.createdAt).toLocaleDateString()}
                  </span>
                </div>
              </div>

              <Tabs defaultValue="analysis" className="w-full">
                <TabsList className="grid w-full grid-cols-3">
                  <TabsTrigger value="analysis">Agent Analysis</TabsTrigger>
                  <TabsTrigger value="insights">Collaborative Insights</TabsTrigger>
                  <TabsTrigger value="tradeoffs">Trade-off Matrix</TabsTrigger>
                </TabsList>

                <TabsContent value="analysis" className="mt-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {agents.map((agent) => (
                      <AgentCard key={agent.id} agent={agent} />
                    ))}
                  </div>
                </TabsContent>

                <TabsContent value="insights" className="mt-6">
                  <div className="space-y-6">
                    <Card>
                      <CardHeader>
                        <CardTitle>Consolidated Recommendation</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-gray-700 mb-4">
                          Based on comprehensive analysis from all agents, we recommend proceeding 
                          with the proposed strategy while implementing enhanced risk mitigation measures.
                        </p>
                        <div className="space-y-2">
                          <div className="flex justify-between text-sm">
                            <span>Overall Confidence</span>
                            <span className="font-medium">{selectedDecision.confidence}%</span>
                          </div>
                          <Progress value={selectedDecision.confidence} className="h-3" />
                        </div>
                      </CardContent>
                    </Card>
                  </div>
                </TabsContent>

                <TabsContent value="tradeoffs" className="mt-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <Card>
                      <CardHeader>
                        <CardTitle className="text-green-600">Advantages</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <ul className="space-y-2 text-sm">
                          <li>• Significant ROI potential (18-22%)</li>
                          <li>• Market positioning advantages</li>
                          <li>• Enhanced operational efficiency</li>
                          <li>• Strategic competitive moat</li>
                        </ul>
                      </CardContent>
                    </Card>
                    
                    <Card>
                      <CardHeader>
                        <CardTitle className="text-red-600">Disadvantages</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <ul className="space-y-2 text-sm">
                          <li>• High initial capital requirement</li>
                          <li>• Implementation complexity</li>
                          <li>• Regulatory compliance risks</li>
                          <li>• Market timing uncertainties</li>
                        </ul>
                      </CardContent>
                    </Card>
                  </div>
                </TabsContent>
              </Tabs>
            </motion.div>
          </div>
        </div>
      </div>
    </div>
  );
}