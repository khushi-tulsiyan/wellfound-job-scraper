import React, { useState } from 'react';
import axios from 'axios';

const JobScraper = () => {
  const [keyword, setKeyword] = useState('');
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    if (!keyword.trim()) return;

    setLoading(true);
    setError('');
    try {
      const response = await axios.get(`/api/scrape?keyword=${keyword}`);
      setJobs(response.data);
    } catch (err) {
      setError('Failed to fetch data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div>
        <input
          type="text"
          placeholder="Enter keyword"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />
        <button onClick={handleSearch}>Search Jobs</button>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div>
        {jobs.length > 0 ? (
          <ul>
            {jobs.map((job, index) => (
              <li key={index}>
                <h3>{job.job_title}</h3>
                <p>{job.company_name}</p>
                <p>{job.location}</p>
                <a href={job.job_link} target="_blank" rel="noopener noreferrer">
                  View Job
                </a>
              </li>
            ))}
          </ul>
        ) : (
          !loading && <p>No jobs found.</p>
        )}
      </div>
    </div>
  );
};

export default JobScraper;
