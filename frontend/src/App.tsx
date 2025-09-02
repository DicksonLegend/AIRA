import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { Dashboard } from '@/pages/Dashboard';
import Workspace from '@/pages/Workspace';
import Reports from '@/pages/Reports';
import Agents from '@/pages/Agents';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/workspace" element={<Workspace />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/agents" element={<Agents />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;