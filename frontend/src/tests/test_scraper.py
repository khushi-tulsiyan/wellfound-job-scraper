import unittest
from backend.scraper.wellfound_scraper import scrape_jobs

class TestScraper(unittest.TestCase):
    def test_scrape_jobs(self):
        jobs = scrape_jobs("backend developer")
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)
        self.assertIn("job_title", jobs[0])
        self.assertIn("company_name", jobs[0])

if __name__ == '__main__':
    unittest.main()
