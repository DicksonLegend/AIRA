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
<<<<<<< HEAD
    <div className="glass border-b-2 border-white/20 px-8 py-6">
      <div className="flex items-center justify-between">
        <div className="group">
          <h1 className="text-3xl font-bold text-black group-hover:text-gray-800 transition-colors">{title}</h1>
          <p className="text-gray-600 group-hover:text-gray-700 transition-colors mt-2">{subtitle}</p>
        </div>
        <Button 
          onClick={onCtaClick} 
          className="accent-button hover:bg-green-600 transition-all duration-300 text-lg px-8 py-3 rounded-xl shadow-lg hover:shadow-xl"
        >
=======
    <div className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">{title}</h1>
          <p className="text-gray-600 mt-1">{subtitle}</p>
        </div>
        <Button onClick={onCtaClick} className="bg-blue-600 hover:bg-blue-700">
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
          {ctaLabel}
        </Button>
      </div>
    </div>
  );
}