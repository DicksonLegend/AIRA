import React from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';
import { KpiMetric } from '@/types';

interface KpiCardProps {
  metric: KpiMetric;
}

export function KpiCard({ metric }: KpiCardProps) {
  const getTrendIcon = () => {
    switch (metric.trend) {
      case 'up':
        return <TrendingUp className="w-4 h-4 text-green-600" />;
      case 'down':
        return <TrendingDown className="w-4 h-4 text-red-600" />;
      default:
        return <Minus className="w-4 h-4 text-gray-400" />;
    }
  };

  const getTrendColor = () => {
    switch (metric.trend) {
      case 'up':
        return 'text-green-600';
      case 'down':
        return 'text-red-600';
      default:
        return 'text-gray-400';
    }
  };

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-2">
          <p className="text-sm font-medium text-gray-600">{metric.title}</p>
          {getTrendIcon()}
        </div>
        <p className="text-3xl font-bold text-gray-900">{metric.value}</p>
        <div className="flex items-center mt-2">
          <span className={`text-sm font-medium ${getTrendColor()}`}>
            {metric.change}
          </span>
          <span className="text-sm text-gray-500 ml-1">vs last month</span>
        </div>
      </CardContent>
    </Card>
  );
}