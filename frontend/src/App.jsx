import React from 'react';
import { JobScraper } from './components/JobScraper';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6 text-center">
          Wellfound Job Scraper
        </h1>
        <JobScraper />
      </div>
    </div>
  );
}

export default App;