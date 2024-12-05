import threading
from flask import Blueprint, jsonify, request
import requests
from bs4 import BeautifulSoup
import logging

def create_scraper_blueprint():
    scraper_bp = Blueprint('scraper', __name__)
    
    @scraper_bp.route('/scrape', methods=['POST'])
    def scrape_jobs():
        data = request.json
        keyword = data.get('keyword', '')
        
        if not keyword:
            return jsonify({'error': 'Keyword is required'}), 400
        
        try:
            jobs = scrape_wellfound(keyword)
            return jsonify(jobs)
        except Exception as e:
            logging.error(f"Scraping error: {e}")
            return jsonify({'error': 'Scraping failed'}), 500
    
    return scraper_bp

def scrape_wellfound(keyword):
    url = f"https://wellfound.com/jobs?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    job_listings = soup.select('.job-card')
    
    for job in job_listings[:15]:
        try:
            company = job.select_one('.company-name').text.strip()
            title = job.select_one('.job-title').text.strip()
            location = job.select_one('.job-location').text.strip() if job.select_one('.job-location') else 'N/A'
            
            jobs.append({
                'company': company,
                'title': title,
                'location': location
            })
        except Exception as e:
            logging.warning(f"Could not parse job: {e}")
    
    return jobs