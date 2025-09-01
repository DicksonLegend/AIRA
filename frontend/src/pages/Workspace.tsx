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
        </div>
      </div>
    </div>
  );
}