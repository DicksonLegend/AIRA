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
      <div className="flex items-center justify-between p-6 border-b border-gray-200">
        <div>
          <h1 className="text-3xl font-bold text-black">Strategic Reports</h1>
          <p className="text-gray-600">Comprehensive insights from your decision ecosystem</p>
        </div>
        <div className="flex space-x-3">
          <Button variant="outline" className="flex items-center gap-2 text-black border-gray-300">
            <Filter className="w-4 h-4" />
            Filter Reports
          </Button>
          <Button className="bg-yellow-500 hover:bg-yellow-600 text-black font-medium px-6 py-2 flex items-center gap-2">
            <Download className="w-4 h-4" />
            Export Report
          </Button>
        </div>
      </div>

      <div className="flex-1 overflow-auto p-6">
        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card className="bg-white border border-gray-200">
            <CardContent className="p-6">
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

          <Card className="bg-white border border-gray-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">AVG CONFIDENCE</p>
                  <p className="text-3xl font-bold text-black mt-2">35%</p>
                  <p className="text-sm text-gray-600 mt-1">AI recommendation accuracy</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-white border border-gray-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">COMPLETED</p>
                  <p className="text-3xl font-bold text-black mt-2">0</p>
                  <p className="text-sm text-green-600 mt-1">Successfully implemented</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900 text-white border border-gray-800">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-300 uppercase tracking-wide">THIS MONTH</p>
                  <p className="text-3xl font-bold text-white mt-2">7</p>
                  <p className="text-sm text-yellow-400 mt-1">New decisions</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Priority Distribution */}
          <Card className="bg-white border border-gray-200">
            <CardHeader>
              <CardTitle className="text-black text-xl">Decision Priority Distribution</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={priorityData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#374151" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Status Breakdown */}
          <Card className="bg-white border border-gray-200">
            <CardHeader>
              <CardTitle className="text-black text-xl">Decision Status Breakdown</CardTitle>
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
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
              <div className="mt-4 text-center">
                <p className="text-sm text-yellow-600">Recommendations Ready: 5</p>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* AI Confidence Score Analysis */}
        <Card className="bg-white border border-gray-200 mb-8">
          <CardHeader>
            <CardTitle className="text-black text-xl">AI Confidence Score Analysis</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={200}>
              <LineChart data={confidenceData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="decision" />
                <YAxis domain={[0, 100]} />
                <Tooltip />
                <Line 
                  type="monotone" 
                  dataKey="confidence" 
                  stroke="#f59e0b" 
                  strokeWidth={3}
                  dot={{ fill: '#f59e0b', strokeWidth: 2, r: 6 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Recent Strategic Decisions Table */}
        <Card className="bg-white border border-gray-200">
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle className="text-black text-xl flex items-center gap-2">
              <span>📋</span>
              Recent Strategic Decisions
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b border-gray-200">
                    <th className="text-left py-3 px-4 font-medium text-gray-700">Decision</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-700">Priority</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-700">Status</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-700">Confidence</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-700">Date</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-gray-100">
                    <td className="py-3 px-4">
                      <div>
                        <p className="font-medium text-black">expansion to europe</p>
                        <p className="text-sm text-gray-500">expansion to europe</p>
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <Badge className="bg-red-100 text-red-700 border-red-200">critical</Badge>
                    </td>
                    <td className="py-3 px-4">
                      <span className="text-gray-600">analyzing</span>
                    </td>
                    <td className="py-3 px-4">
                      <span className="text-gray-600">N/A</span>
                    </td>
                    <td className="py-3 px-4">
                      <span className="text-gray-600">Sep 1, 2025</span>
                    </td>
                  </tr>
                  {decisions.slice(1).map((decision) => (
                    <tr key={decision.id} className="border-b border-gray-100">
                      <td className="py-3 px-4">
                        <div>
                          <p className="font-medium text-black">{decision.title}</p>
                        </div>
                      </td>
                      <td className="py-3 px-4">
                        <Badge className={`${
                          decision.priority === 'high' ? 'bg-red-100 text-red-700 border-red-200' :
                          decision.priority === 'medium' ? 'bg-yellow-100 text-yellow-700 border-yellow-200' :
                          'bg-gray-100 text-gray-700 border-gray-200'
                        }`}>
                          {decision.priority}
                        </Badge>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600">{decision.status}</span>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600">{decision.confidence}%</span>
                      </td>
                      <td className="py-3 px-4">
                        <span className="text-gray-600">{decision.createdAt}</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}