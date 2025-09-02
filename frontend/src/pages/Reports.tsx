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
    <div className="flex-1 flex flex-col">
      {/* Header */}
      <motion.div 
        className="flex items-center justify-between p-4 sm:p-6 glass-card border-b-2 border-white/20"
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

      <div className="flex-1 overflow-auto p-4 sm:p-6">
        {/* KPI Cards */}
        <motion.div 
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 mb-6 sm:mb-8"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.6, staggerChildren: 0.1 }}
        >
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 }}>
            <Card className="glass-card hover-lift interactive-border">
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">TOTAL DECISIONS</p>
                    <p className="text-3xl font-bold text-black mt-2">7</p>
                    <p className="text-sm text-green-600 mt-1 flex items-center">
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
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">AVG CONFIDENCE</p>
                    <p className="text-3xl font-bold text-black mt-2">35%</p>
                    <p className="text-sm text-gray-600 mt-1">AI recommendation accuracy</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.5 }}>
            <Card className="glass-card hover-lift interactive-border">
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">COMPLETED</p>
                    <p className="text-3xl font-bold text-black mt-2">0</p>
                    <p className="text-sm text-green-600 mt-1">Successfully implemented</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6 }}>
            <Card className="glass-dark hover-lift interactive-border text-white">
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-300 uppercase tracking-wide">THIS MONTH</p>
                    <p className="text-3xl font-bold text-white mt-2">7</p>
                    <p className="text-sm text-yellow-400 mt-1">New decisions</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        </motion.div>

        {/* Charts Row */}
        <motion.div 
          className="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6 mb-6 sm:mb-8"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7, duration: 0.6 }}
        >
          {/* Priority Distribution */}
          <Card className="glass-card hover-lift interactive-border">
            <CardHeader className="pb-3">
              <CardTitle className="text-black text-lg sm:text-xl">Decision Priority Distribution</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={priorityData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                  <XAxis dataKey="name" fontSize={12} stroke="#6b7280" />
                  <YAxis fontSize={12} stroke="#6b7280" />
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
            <CardHeader className="pb-3">
              <CardTitle className="text-black text-lg sm:text-xl">Decision Status Breakdown</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={250}>
                <PieChart>
                  <Pie
                    data={statusData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name }) => name}
                    outerRadius={80}
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
              <div className="mt-4 text-center">
                <p className="text-sm text-yellow-600 font-medium">Recommendations Ready: 5</p>
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
          <Card className="glass-card hover-lift interactive-border mb-6 sm:mb-8">
            <CardHeader className="pb-3">
              <CardTitle className="text-black text-lg sm:text-xl">AI Confidence Score Analysis</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={200}>
                <LineChart data={confidenceData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                  <XAxis dataKey="decision" fontSize={12} stroke="#6b7280" />
                  <YAxis domain={[0, 100]} fontSize={12} stroke="#6b7280" />
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
                    strokeWidth={3}
                    dot={{ fill: '#10b981', strokeWidth: 2, r: 6 }}
                    activeDot={{ r: 8, stroke: '#10b981', strokeWidth: 2 }}
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
            <CardHeader className="flex flex-row items-center justify-between pb-3">
              <CardTitle className="text-black text-lg sm:text-xl flex items-center gap-2">
                <span>📋</span>
                Recent Strategic Decisions
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b border-gray-200/50">
                      <th className="text-left py-3 px-4 font-medium text-gray-700 text-sm">Decision</th>
                      <th className="text-left py-3 px-4 font-medium text-gray-700 text-sm">Priority</th>
                      <th className="text-left py-3 px-4 font-medium text-gray-700 text-sm">Status</th>
                      <th className="text-left py-3 px-4 font-medium text-gray-700 text-sm">Confidence</th>
                      <th className="text-left py-3 px-4 font-medium text-gray-700 text-sm">Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    <motion.tr 
                      className="border-b border-gray-100/50 hover:glass transition-all duration-300"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 1.2 }}
                    >
                      <td className="py-3 px-4">
                        <div>
                          <p className="font-medium text-black text-sm">expansion to europe</p>
                          <p className="text-xs text-gray-500">expansion to europe</p>
                        </div>
                      </td>
                      <td className="py-3 px-4">
                        <Badge className="glass bg-red-100 text-red-700 border-red-200 text-xs">critical</Badge>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600 text-sm">analyzing</span>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600 text-sm">N/A</span>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600 text-sm">Sep 1, 2025</span>
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
                        <td className="py-3 px-4">
                          <div>
                            <p className="font-medium text-black text-sm">{decision.title}</p>
                          </div>
                        </td>
                        <td className="py-3 px-4">
                          <Badge className={`glass text-xs ${
                            decision.priority === 'high' ? 'bg-red-100 text-red-700 border-red-200' :
                            decision.priority === 'medium' ? 'bg-yellow-100 text-yellow-700 border-yellow-200' :
                            'bg-gray-100 text-gray-700 border-gray-200'
                          }`}>
                            {decision.priority}
                          </Badge>
                        </td>
                        <td className="py-3 px-4">
                          <span className="text-gray-600 text-sm">{decision.status}</span>
                        </td>
                        <td className="py-3 px-4">
                          <span className="text-gray-600 text-sm">{decision.confidence}%</span>
                        </td>
                        <td className="py-3 px-4">
                          <span className="text-gray-600 text-sm">{decision.createdAt}</span>
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