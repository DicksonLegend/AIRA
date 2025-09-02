import React from 'react';
import { Button } from '@/components/ui/button';

interface HeaderProps {
  title: string;
  subtitle: string;
  ctaLabel: string;
  onCtaClick: () => void;
}

export function Header({ title, subtitle, ctaLabel, onCtaClick }: HeaderProps) {
  return (
    <div className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">{title}</h1>
          <p className="text-gray-600 mt-1">{subtitle}</p>
        </div>
        <Button onClick={onCtaClick} className="bg-blue-600 hover:bg-blue-700">
          {ctaLabel}
        </Button>
      </div>
    </div>
  );
}