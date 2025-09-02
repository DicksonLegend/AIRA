<<<<<<< HEAD
import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { DetailedAgentCard } from '@/components/ui/DetailedAgentCard';
import { decisions, getDetailedAgentAnalysis } from '@/data/mockData';

export default function Workspace() {
  const [selectedDecision, setSelectedDecision] = useState(decisions[0]);
  const [searchTerm, setSearchTerm] = useState('');

  const filteredDecisions = decisions.filter(decision =>
    decision.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Left Panel - Strategic Decisions */}
      <div className="w-72 glass border-r-2 border-white/20 p-4 overflow-auto">
        <h3 className="font-semibold text-black mb-4 text-lg">Strategic Decisions</h3>
        
        <div className="space-y-3 mb-4">
          <Input
            placeholder="Search decisions..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className={
              searchTerm
                ? 'glass-input border-green-500/40 focus-enhanced'
                : 'glass-input hover:border-gray-500/30 focus-enhanced'
            }
          />
        </div>

        <div className="space-y-3">
          {filteredDecisions.map((decision) => (
            <div
              key={decision.id}
              className={`p-3 rounded-lg cursor-pointer transition-all duration-300 hover-lift group ${
                selectedDecision.id === decision.id
                  ? 'glass-card border-green-500/40 shadow-lg'
                  : 'glass-input hover:border-gray-500/30'
              }`}
              onClick={() => setSelectedDecision(decision)}
            >
              <h4 className="font-medium text-black group-hover:text-gray-800 transition-colors mb-2 text-sm">{decision.title}</h4>
              <div className="flex gap-2 mb-2">
                <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-600 group-hover:scale-105 transition-transform">
                  {decision.priority}
                </Badge>
                <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-600 group-hover:scale-105 transition-transform">
                  {decision.status}
                </Badge>
              </div>
              <div className="text-xs text-gray-600 group-hover:text-gray-700 transition-colors">
                Confidence: {decision.confidence}%
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Right Panel - Decision Details */}
      <div className="flex-1 flex flex-col overflow-hidden">
        <div className="p-4 border-b border-white/20">
          <div className="flex items-center justify-between mb-3">
            <div>
              <h2 className="text-2xl font-bold text-black mb-1">AI Analysis Workspace</h2>
              <p className="text-gray-600 text-sm">Collaborative intelligence from your AI agent ecosystem</p>
            </div>
            <Button className="bg-yellow-500 hover:bg-yellow-600 text-black font-medium px-4 py-2 rounded-lg flex items-center gap-2">
              <span className="text-lg">⚡</span>
              Run AI Analysis
            </Button>
          </div>

          <div className="mb-3">
            <h3 className="text-lg font-semibold text-black mb-1">{selectedDecision.title}</h3>
            <p className="text-gray-600 text-xs">
              {selectedDecision.title.includes('shoe factory') 
                ? 'starting an shoe factory outlet in south africa in a large scale'
                : 'Analysis for strategic decision implementation'
              }
            </p>
          </div>
        </div>

        <div className="flex-1 overflow-auto p-4">
          <Tabs defaultValue="analysis" className="w-full h-full">
            <TabsList className="glass mb-4 p-1 rounded-xl">
              <TabsTrigger value="analysis" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Agent Analysis
              </TabsTrigger>
              <TabsTrigger value="insights" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Collaborative Insights
              </TabsTrigger>
              <TabsTrigger value="tradeoffs" className="text-black data-[state=active]:accent-button rounded-lg px-4 py-2 transition-all duration-300">
                Trade-off Matrix
              </TabsTrigger>
            </TabsList>

            <TabsContent value="analysis" className="h-full">
              <div className="grid grid-cols-1 xl:grid-cols-2 gap-4 h-full">
                {getDetailedAgentAnalysis(selectedDecision.id).map((analysis) => (
                  <DetailedAgentCard key={analysis.id} analysis={analysis} />
                ))}
              </div>
            </TabsContent>

            <TabsContent value="insights" className="space-y-8">
              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Consolidated Recommendation</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-600 mb-6 text-lg leading-relaxed">
                    Based on analysis from all agents, the recommended approach is to proceed with the budget allocation strategy with moderate risk mitigation measures.
                  </p>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600 text-lg">Overall Confidence</span>
                      <span className="font-medium text-black text-xl">{selectedDecision.confidence}%</span>
                    </div>
                    <Progress value={selectedDecision.confidence} className="h-4 progress-enhanced" />
                  </div>
                </CardContent>
              </Card>

              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Key Insights</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-3 text-lg text-gray-600">
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span>Financial analysis shows positive ROI projections</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                      <span>Risk assessment identifies manageable threats</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                      <span>Compliance review confirms regulatory alignment</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-orange-500 rounded-full"></div>
                      <span>Market analysis indicates favorable conditions</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Next Steps</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-3 text-lg text-gray-600">
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span>Implement risk mitigation strategies</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                      <span>Establish monitoring protocols</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                      <span>Schedule quarterly reviews</span>
                    </li>
                    <li className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-orange-500 rounded-full"></div>
                      <span>Prepare stakeholder communications</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>
            </TabsContent>

            <TabsContent value="tradeoffs" className="space-y-8">
              <Card className="glass-card interactive-border">
                <CardHeader>
                  <CardTitle className="text-black text-xl">Trade-off Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-600 text-lg leading-relaxed">
                    Trade-off matrix analysis will be displayed here, showing the relationship between different decision factors and their impact on outcomes.
                  </p>
                </CardContent>
              </Card>
            </TabsContent>
          </Tabs>
=======
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
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
        </div>
      </div>
    </div>
  );
}