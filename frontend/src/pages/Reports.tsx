import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line, PieChart, Pie, Cell } from 'recharts';
import { Download, Filter, RefreshCw, Database, Trash2 } from 'lucide-react';
import { useReports } from '@/hooks/useReports';
import { useEffect, useState } from 'react';

export default function Reports() {
  const { 
    metrics, 
    recentDecisions, 
    isLoading, 
    clearAllData, 
    hasData,
    totalAnalyses,
    hasRealData,
    checkForRealData
  } = useReports();

  const [showDevTools, setShowDevTools] = useState(false);

  // Load only real analysis data - no sample data
  useEffect(() => {
    if (!isLoading) {
      if (hasData) {
        console.log(`📊 Reports loaded with ${totalAnalyses} real analyses`);
      } else {
        console.log('📊 No real analysis data found - run analyses from Dashboard to populate reports');
      }
    }
  }, [isLoading, hasData, totalAnalyses, hasRealData]);

  // Show loading state
  if (isLoading) {
    return (
      <div className="flex-1 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-500 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading reports data...</p>
        </div>
      </div>
    );
  }

  // Default empty state if no metrics
  const defaultMetrics = {
    totalDecisions: 0,
    avgConfidence: 0,
    completedDecisions: 0,
    thisMonthDecisions: 0,
    priorityDistribution: [],
    statusDistribution: [],
    confidenceData: [],
    agentPerformance: [],
    trendsData: []
  };

  const currentMetrics = metrics || defaultMetrics;

  return (
    <div className="flex-1 flex flex-col h-full">
      {/* Header */}
      <motion.div 
        className="flex items-center justify-between p-4 sm:p-6 glass-card border-b-2 border-white/20 flex-shrink-0"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <div>
          <h1 className="text-3xl font-bold text-black">Strategic Reports</h1>
          <p className="text-gray-600">Comprehensive insights from your Four Pillars AI ecosystem</p>
          <div className="flex items-center space-x-4 mt-1">
            <p className="text-sm text-gray-500">
              {totalAnalyses > 0 ? `${totalAnalyses} total analyses` : 'No analyses yet'}
            </p>
            {totalAnalyses > 0 && (
              <Badge variant={hasRealData ? "default" : "secondary"} className="text-xs">
                {hasRealData ? "🔴 Live Data" : "📊 Real Data Only"}
              </Badge>
            )}
          </div>
        </div>
        <div className="flex space-x-3">
          <Button 
            variant="outline" 
            className="glass-button flex items-center gap-2 text-black hover-lift"
            onClick={() => setShowDevTools(!showDevTools)}
          >
            <Database className="w-4 h-4" />
            {showDevTools ? 'Hide' : 'Dev'} Tools
          </Button>
          <Button 
            variant="outline" 
            className="glass-button flex items-center gap-2 text-black hover-lift"
            onClick={checkForRealData}
          >
            <RefreshCw className="w-4 h-4" />
            Refresh
          </Button>
          <Button variant="outline" className="glass-button flex items-center gap-2 text-black hover-lift">
            <Filter className="w-4 h-4" />
            Filter Reports
          </Button>
          <Button className="accent-button font-medium px-6 py-2 flex items-center gap-2 hover-lift">
            <Download className="w-4 h-4" />
            Export Report
          </Button>
        </div>
      </motion.div>

      {/* Dev Tools Panel */}
      {showDevTools && (
        <motion.div 
          className="p-4 bg-yellow-50 border-b border-yellow-200"
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
        >
          <div className="flex items-center gap-4">
            <p className="text-sm text-yellow-700 font-medium">Developer Tools:</p>
            <Button 
              size="sm" 
              variant="outline" 
              onClick={clearAllData}
              className="text-red-700 border-red-300 hover:bg-red-100"
            >
              <Trash2 className="w-3 h-3 mr-1" />
              Clear All Data
            </Button>
            <span className="text-xs text-yellow-600">Current: {totalAnalyses} analyses</span>
          </div>
        </motion.div>
      )}

      <div className="flex-1 overflow-y-auto p-4 sm:p-6 min-h-0">
        {/* No Data State */}
        {!hasData && (
          <motion.div 
            className="text-center py-12"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
          >
            <Database className="w-16 h-16 text-gray-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-700 mb-2">No Analysis Data Available</h3>
            <p className="text-gray-500 mb-6">
              Run some business analyses using Four Pillars AI to see real reports here.
            </p>
            <div className="space-y-4">
              <div className="text-sm text-gray-600 bg-blue-50 p-4 rounded-lg mb-4">
                <p className="font-medium mb-2">💡 To get real data:</p>
                <p>1. Go to "Analysis Workspace" and run a business scenario</p>
                <p>2. Complete the Four Pillars AI analysis</p>
                <p>3. Return here to see real insights and metrics</p>
              </div>
              <Button onClick={checkForRealData} className="accent-button">
                <RefreshCw className="w-4 h-4 mr-2" />
                Check for Real Data
              </Button>
            </div>
          </motion.div>
        )}

        {/* Data Display */}
        {hasData && (
          <>
            {/* KPI Cards */}
            <motion.div 
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mb-4 sm:mb-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2, duration: 0.6, staggerChildren: 0.1 }}
            >
              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 }}>
                <Card className="glass-card hover-lift interactive-border">
                  <CardContent className="p-3 sm:p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-xs font-medium text-gray-600 uppercase tracking-wide">TOTAL DECISIONS</p>
                        <p className="text-2xl font-bold text-black mt-1">{currentMetrics.totalDecisions}</p>
                        <p className="text-xs text-green-600 mt-1 flex items-center">
                          <span className="mr-1">✓</span>
                          Real AI Analysis
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>

              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.4 }}>
                <Card className="glass-card hover-lift interactive-border">
                  <CardContent className="p-3 sm:p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-xs font-medium text-gray-600 uppercase tracking-wide">AVG CONFIDENCE</p>
                        <p className="text-2xl font-bold text-black mt-1">{currentMetrics.avgConfidence}%</p>
                        <p className="text-xs text-gray-600 mt-1">Four Pillars AI accuracy</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>

              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.5 }}>
                <Card className="glass-card hover-lift interactive-border">
                  <CardContent className="p-3 sm:p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-xs font-medium text-gray-600 uppercase tracking-wide">COMPLETED</p>
                        <p className="text-2xl font-bold text-black mt-1">{currentMetrics.completedDecisions}</p>
                        <p className="text-xs text-green-600 mt-1">Successfully analyzed</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>

              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6 }}>
                <Card className="glass-dark hover-lift interactive-border text-white">
                  <CardContent className="p-3 sm:p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-xs font-medium text-gray-300 uppercase tracking-wide">THIS MONTH</p>
                        <p className="text-2xl font-bold text-white mt-1">{currentMetrics.thisMonthDecisions}</p>
                        <p className="text-xs text-yellow-400 mt-1">New analyses</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            </motion.div>

            {/* Charts Row */}
            <motion.div 
              className="grid grid-cols-1 lg:grid-cols-2 gap-3 sm:gap-4 mb-4 sm:mb-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.7, duration: 0.6 }}
            >
              {/* Priority Distribution */}
              <Card className="glass-card hover-lift interactive-border">
                <CardHeader className="pb-2">
                  <CardTitle className="text-black text-base sm:text-lg">Decision Priority Distribution</CardTitle>
                </CardHeader>
                <CardContent>
                  {currentMetrics.priorityDistribution.length > 0 ? (
                    <ResponsiveContainer width="100%" height={180}>
                      <BarChart data={currentMetrics.priorityDistribution}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                        <XAxis dataKey="name" fontSize={11} stroke="#6b7280" />
                        <YAxis fontSize={11} stroke="#6b7280" />
                        <Tooltip 
                          contentStyle={{ 
                            backgroundColor: 'rgba(255, 255, 255, 0.95)', 
                            border: '1px solid rgba(255, 255, 255, 0.3)',
                            borderRadius: '8px',
                            backdropFilter: 'blur(20px)'
                          }} 
                        />
                        <Bar dataKey="value" fill="#10b981" radius={[4, 4, 0, 0]} />
                      </BarChart>
                    </ResponsiveContainer>
                  ) : (
                    <div className="h-[180px] flex items-center justify-center text-gray-500">
                      No priority data available
                    </div>
                  )}
                </CardContent>
              </Card>

              {/* Status Distribution */}
              <Card className="glass-card hover-lift interactive-border">
                <CardHeader className="pb-2">
                  <CardTitle className="text-black text-base sm:text-lg">Decision Status Breakdown</CardTitle>
                </CardHeader>
                <CardContent>
                  {currentMetrics.statusDistribution.length > 0 ? (
                    <ResponsiveContainer width="100%" height={180}>
                      <PieChart>
                        <Pie
                          data={currentMetrics.statusDistribution}
                          cx="50%"
                          cy="50%"
                          innerRadius={40}
                          outerRadius={70}
                          paddingAngle={2}
                          dataKey="count"
                        >
                          {currentMetrics.statusDistribution.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={entry.fill} />
                          ))}
                        </Pie>
                        <Tooltip />
                      </PieChart>
                    </ResponsiveContainer>
                  ) : (
                    <div className="h-[180px] flex items-center justify-center text-gray-500">
                      No status data available
                    </div>
                  )}
                </CardContent>
              </Card>
            </motion.div>

            {/* AI Confidence Analysis */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.8, duration: 0.6 }}
              className="mb-4 sm:mb-6"
            >
              <Card className="glass-card hover-lift interactive-border">
                <CardHeader className="pb-2">
                  <CardTitle className="text-black text-base sm:text-lg">AI Confidence Score Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  {currentMetrics.confidenceData.length > 0 ? (
                    <ResponsiveContainer width="100%" height={200}>
                      <LineChart data={currentMetrics.confidenceData}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                        <XAxis 
                          dataKey="decision" 
                          fontSize={10} 
                          stroke="#6b7280"
                          angle={-45}
                          textAnchor="end"
                          height={60}
                        />
                        <YAxis fontSize={11} stroke="#6b7280" domain={[0, 100]} />
                        <Tooltip 
                          contentStyle={{ 
                            backgroundColor: 'rgba(255, 255, 255, 0.95)', 
                            border: '1px solid rgba(255, 255, 255, 0.3)',
                            borderRadius: '8px',
                            backdropFilter: 'blur(20px)'
                          }} 
                        />
                        <Line 
                          type="monotone" 
                          dataKey="confidence" 
                          stroke="#10b981" 
                          strokeWidth={2}
                          dot={{ fill: '#10b981', strokeWidth: 2, r: 4 }}
                        />
                      </LineChart>
                    </ResponsiveContainer>
                  ) : (
                    <div className="h-[200px] flex items-center justify-center text-gray-500">
                      No confidence data available
                    </div>
                  )}
                </CardContent>
              </Card>
            </motion.div>

            {/* Recent Strategic Decisions */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.9, duration: 0.6 }}
            >
              <Card className="glass-card hover-lift interactive-border">
                <CardHeader className="pb-2 flex flex-row items-center justify-between">
                  <CardTitle className="text-black text-base sm:text-lg">Recent Strategic Decisions</CardTitle>
                  <Badge variant="secondary" className="text-xs">
                    {recentDecisions.length} analyses
                  </Badge>
                </CardHeader>
                <CardContent>
                  {recentDecisions.length > 0 ? (
                    <div className="space-y-3">
                      {recentDecisions.slice(0, 10).map((decision) => (
                        <div 
                          key={decision.id}
                          className="flex items-center justify-between p-3 rounded-lg border border-gray-200 hover:border-emerald-300 transition-colors"
                        >
                          <div className="flex-1">
                            <h4 className="font-medium text-black text-sm leading-tight mb-1">
                              {decision.scenario}
                            </h4>
                            <div className="flex items-center space-x-3 text-xs text-gray-500">
                              <span>{new Date(decision.timestamp).toLocaleDateString()}</span>
                              <span>•</span>
                              <span>{decision.execution_time_seconds.toFixed(1)}s</span>
                              <span>•</span>
                              <span>{decision.agents_utilized.length} agents</span>
                            </div>
                          </div>
                          <div className="flex items-center space-x-3">
                            <Badge 
                              variant={
                                decision.priority === 'critical' ? 'destructive' :
                                decision.priority === 'high' ? 'default' : 'secondary'
                              }
                              className="text-xs"
                            >
                              {decision.priority}
                            </Badge>
                            <div className="text-right">
                              <div className="text-lg font-bold text-emerald-600">
                                {decision.overall_confidence}%
                              </div>
                              <div className="text-xs text-gray-500">confidence</div>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className="text-center py-8 text-gray-500">
                      No recent decisions available
                    </div>
                  )}
                </CardContent>
              </Card>
            </motion.div>
          </>
        )}
      </div>
    </div>
  );
}
