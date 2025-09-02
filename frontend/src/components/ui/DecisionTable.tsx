import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Decision } from '@/types';

interface DecisionTableProps {
  decisions: Decision[];
}

const priorityColors = {
  high: 'bg-red-100 text-red-800',
  medium: 'bg-yellow-100 text-yellow-800',
  low: 'bg-green-100 text-green-800'
};

const statusColors = {
  active: 'bg-blue-100 text-blue-800',
  completed: 'bg-green-100 text-green-800',
  pending: 'bg-gray-100 text-gray-800'
};

export function DecisionTable({ decisions }: DecisionTableProps) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Decision</TableHead>
          <TableHead>Priority</TableHead>
          <TableHead>Status</TableHead>
          <TableHead>Confidence</TableHead>
          <TableHead>Created</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {decisions.map((decision) => (
          <TableRow key={decision.id} className="hover:bg-gray-50">
            <TableCell className="font-medium">{decision.title}</TableCell>
            <TableCell>
              <Badge className={priorityColors[decision.priority]}>
                {decision.priority}
              </Badge>
            </TableCell>
            <TableCell>
              <Badge className={statusColors[decision.status]}>
                {decision.status}
              </Badge>
            </TableCell>
            <TableCell>{decision.confidence}%</TableCell>
            <TableCell>
              {new Date(decision.createdAt).toLocaleDateString()}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}