import React from 'react';
import { Sidebar } from './Sidebar';

interface LayoutProps {
  children: React.ReactNode;
}

export function Layout({ children }: LayoutProps) {
  return (
<<<<<<< HEAD
    <div className="flex h-screen animated-gradient">
=======
    <div className="flex h-screen bg-gray-50">
>>>>>>> 50ae69f853291638d6f1f4c49baa7d4614cabe5a
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        {children}
      </div>
    </div>
  );
}