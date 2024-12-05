import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

export function JobScraper() {
  const [keyword, setKeyword] = useState('');
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleScrape = async () => {
    if (!keyword) return;

    setLoading(true);
    try {
      const response = await fetch('/api/scrape', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ keyword })
      });
      
      const data = await response.json();
      setJobs(data);
    } catch (error) {
      console.error('Scraping failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex space-x-2">
        <Input
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="Enter job keyword"
        />
        <Button onClick={handleScrape} disabled={loading}>
          {loading ? 'Scraping...' : 'Scrape Jobs'}
        </Button>
      </div>

      {jobs.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Job Listings</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid gap-4">
              {jobs.map((job, index) => (
                <div key={index} className="border p-4 rounded">
                  <h3 className="font-bold">{job.title}</h3>
                  <p className="text-muted-foreground">{job.company}</p>
                  <p className="text-sm">{job.location}</p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}