import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line, PieChart, Pie, Cell } from 'recharts';
import { Download, Filter } from 'lucide-react';
import { decisions } from '@/data/mockData';

const priorityData = [
  { name: 'Critical', value: 3, fill: '#ef4444' },
  { name: 'High', value: 4, fill: '#f59e0b' },
];

const statusData = [
  { name: 'Active', count: 2, fill: '#10b981' },
  { name: 'Analyzing', count: 5, fill: '#f59e0b' },
  { name: 'Recommendations Ready', count: 5, fill: '#3b82f6' },
];

const confidenceData = [
  { decision: 'market expansion in ...', confidence: 0 },
  { decision: 'market expansion to ...', confidence: 85 },
  { decision: 'Global Market Expans...', confidence: 82 },
  { decision: 'Sustainability Trans...', confidence: 78 },
];

export default function Reports() {
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
          <p className="text-gray-600">Comprehensive insights from your decision ecosystem</p>
        </div>
        <div className="flex space-x-3">
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

      <div className="flex-1 overflow-y-auto p-4 sm:p-6 min-h-0">
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
                    <p className="text-2xl font-bold text-black mt-1">7</p>
                    <p className="text-xs text-green-600 mt-1 flex items-center">
                      <span className="mr-1">↗</span>
                      Active ecosystem
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
                    <p className="text-2xl font-bold text-black mt-1">35%</p>
                    <p className="text-xs text-gray-600 mt-1">AI recommendation accuracy</p>
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
                    <p className="text-2xl font-bold text-black mt-1">0</p>
                    <p className="text-xs text-green-600 mt-1">Successfully implemented</p>
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
                    <p className="text-2xl font-bold text-white mt-1">7</p>
                    <p className="text-xs text-yellow-400 mt-1">New decisions</p>
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
              <ResponsiveContainer width="100%" height={180}>
                <BarChart data={priorityData}>
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
            </CardContent>
          </Card>

          {/* Status Breakdown */}
          <Card className="glass-card hover-lift interactive-border">
            <CardHeader className="pb-2">
              <CardTitle className="text-black text-base sm:text-lg">Decision Status Breakdown</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={180}>
                <PieChart>
                  <Pie
                    data={statusData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name }) => name}
                    outerRadius={70}
                    fill="#8884d8"
                    dataKey="count"
                  >
                    {statusData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Pie>
                  <Tooltip 
                    contentStyle={{ 
                      backgroundColor: 'rgba(255, 255, 255, 0.95)', 
                      border: '1px solid rgba(255, 255, 255, 0.3)',
                      borderRadius: '8px',
                      backdropFilter: 'blur(20px)'
                    }} 
                  />
                </PieChart>
              </ResponsiveContainer>
              <div className="mt-3 text-center">
                <p className="text-xs text-yellow-600 font-medium">Recommendations Ready: 5</p>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        {/* AI Confidence Score Analysis */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.9, duration: 0.6 }}
        >
          <Card className="glass-card hover-lift interactive-border mb-4 sm:mb-6">
            <CardHeader className="pb-2">
              <CardTitle className="text-black text-base sm:text-lg">AI Confidence Score Analysis</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={160}>
                <LineChart data={confidenceData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                  <XAxis dataKey="decision" fontSize={11} stroke="#6b7280" />
                  <YAxis domain={[0, 100]} fontSize={11} stroke="#6b7280" />
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
                    activeDot={{ r: 6, stroke: '#10b981', strokeWidth: 2 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </motion.div>

        {/* Recent Strategic Decisions Table */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.1, duration: 0.6 }}
        >
          <Card className="glass-card hover-lift interactive-border">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-black text-base sm:text-lg flex items-center gap-2">
                <span>📋</span>
                Recent Strategic Decisions
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b border-gray-200/50">
                      <th className="text-left py-2 px-3 font-medium text-gray-700 text-xs">Decision</th>
                      <th className="text-left py-2 px-3 font-medium text-gray-700 text-xs">Priority</th>
                      <th className="text-left py-2 px-3 font-medium text-gray-700 text-xs">Status</th>
                      <th className="text-left py-2 px-3 font-medium text-gray-700 text-xs">Confidence</th>
                      <th className="text-left py-2 px-3 font-medium text-gray-700 text-xs">Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    <motion.tr 
                      className="border-b border-gray-100/50 hover:glass transition-all duration-300"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 1.2 }}
                    >
                      <td className="py-2 px-3">
                        <div>
                          <p className="font-medium text-black text-xs">expansion to europe</p>
                          <p className="text-xs text-gray-500">expansion to europe</p>
                        </div>
                      </td>
                      <td className="py-2 px-3">
                        <Badge className="glass bg-red-100 text-red-700 border-red-200 text-xs">critical</Badge>
                      </td>
                      <td className="py-2 px-3">
                        <span className="text-gray-600 text-xs">analyzing</span>
                      </td>
                      <td className="py-2 px-3">
                        <span className="text-gray-600 text-xs">N/A</span>
                      </td>
                      <td className="py-2 px-3">
                        <span className="text-gray-600 text-xs">Sep 1, 2025</span>
                      </td>
                    </motion.tr>
                    {decisions.slice(1).map((decision, index) => (
                      <motion.tr 
                        key={decision.id} 
                        className="border-b border-gray-100/50 hover:glass transition-all duration-300"
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 1.3 + index * 0.1 }}
                      >
                        <td className="py-2 px-3">
                          <div>
                            <p className="font-medium text-black text-xs">{decision.title}</p>
                          </div>
                        </td>
                        <td className="py-2 px-3">
                          <Badge className={`glass text-xs ${
                            decision.priority === 'high' ? 'bg-red-100 text-red-700 border-red-200' :
                            decision.priority === 'medium' ? 'bg-yellow-100 text-yellow-700 border-yellow-200' :
                            'bg-gray-100 text-gray-700 border-gray-200'
                          }`}>
                            {decision.priority}
                          </Badge>
                        </td>
                        <td className="py-2 px-3">
                          <span className="text-gray-600 text-xs">{decision.status}</span>
                        </td>
                        <td className="py-2 px-3">
                          <span className="text-gray-600 text-xs">{decision.confidence}%</span>
                        </td>
                        <td className="py-2 px-3">
                          <span className="text-gray-600 text-xs">{decision.createdAt}</span>
                        </td>
                      </motion.tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}