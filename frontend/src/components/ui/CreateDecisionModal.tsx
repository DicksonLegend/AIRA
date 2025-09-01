import { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Checkbox } from '@/components/ui/checkbox';
import { Label } from '@/components/ui/label';
import { X } from 'lucide-react';

interface CreateDecisionModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCreateDecision: (decision: {
    title: string;
    description: string;
    priority: 'high' | 'medium' | 'low';
    deadline: string;
    agents: string[];
  }) => void;
}

export function CreateDecisionModal({ isOpen, onClose, onCreateDecision }: CreateDecisionModalProps) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState<'high' | 'medium' | 'low'>('medium');
  const [deadline, setDeadline] = useState('');
  const [selectedAgents, setSelectedAgents] = useState<string[]>([]);

  const agents = [
    { id: 'finance', name: 'Finance Agent' },
    { id: 'risk', name: 'Risk Agent' },
    { id: 'compliance', name: 'Compliance Agent' },
    { id: 'market', name: 'Market Agent' },
  ];

  const handleAgentToggle = (agentId: string) => {
    setSelectedAgents(prev => 
      prev.includes(agentId) 
        ? prev.filter(id => id !== agentId)
        : [...prev, agentId]
    );
  };

  const handleSubmit = () => {
    if (title.trim() && description.trim() && selectedAgents.length > 0) {
      onCreateDecision({
        title: title.trim(),
        description: description.trim(),
        priority,
        deadline,
        agents: selectedAgents,
      });
      
      // Reset form
      setTitle('');
      setDescription('');
      setPriority('medium');
      setDeadline('');
      setSelectedAgents([]);
      onClose();
    }
  };

  const handleCancel = () => {
    // Reset form
    setTitle('');
    setDescription('');
    setPriority('medium');
    setDeadline('');
    setSelectedAgents([]);
    onClose();
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl bg-white">
        <DialogHeader>
          <div className="flex items-center justify-between">
            <DialogTitle className="text-xl font-semibold text-black">
              Create New Strategic Decision
            </DialogTitle>
            <Button
              variant="ghost"
              size="icon"
              onClick={onClose}
              className="h-6 w-6 rounded-full"
            >
              <X className="h-4 w-4" />
            </Button>
          </div>
        </DialogHeader>
        
        <div className="space-y-6 py-4">
          <div className="space-y-2">
            <Label htmlFor="title" className="text-sm font-medium text-black">
              Decision Title
            </Label>
            <Input
              id="title"
              placeholder="e.g., Market Expansion into Asia-Pacific"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full"
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="description" className="text-sm font-medium text-black">
              Description & Context
            </Label>
            <Textarea
              id="description"
              placeholder="Provide detailed context, objectives, and constraints for this strategic decision..."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full min-h-[100px] resize-none"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label className="text-sm font-medium text-black">Priority Level</Label>
              <Select value={priority} onValueChange={(value: 'high' | 'medium' | 'low') => setPriority(value)}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="high">High</SelectItem>
                  <SelectItem value="medium">Medium</SelectItem>
                  <SelectItem value="low">Low</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="deadline" className="text-sm font-medium text-black">
                Decision Deadline
              </Label>
              <Input
                id="deadline"
                type="date"
                value={deadline}
                onChange={(e) => setDeadline(e.target.value)}
                className="w-full"
              />
            </div>
          </div>

          <div className="space-y-3">
            <Label className="text-sm font-medium text-black">AI Agents to Involve</Label>
            <div className="grid grid-cols-2 gap-3">
              {agents.map((agent) => (
                <div key={agent.id} className="flex items-center space-x-2">
                  <Checkbox
                    id={agent.id}
                    checked={selectedAgents.includes(agent.id)}
                    onCheckedChange={() => handleAgentToggle(agent.id)}
                  />
                  <Label htmlFor={agent.id} className="text-sm text-gray-700">
                    {agent.name}
                  </Label>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="flex justify-end space-x-3 pt-4 border-t">
          <Button
            variant="outline"
            onClick={handleCancel}
            className="px-6"
          >
            Cancel
          </Button>
          <Button
            onClick={handleSubmit}
            disabled={!title.trim() || !description.trim() || selectedAgents.length === 0}
            className="px-6 bg-green-600 hover:bg-green-700 text-white"
          >
            Create Decision
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
