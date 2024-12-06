import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword):
    base_url = "https://wellfound.com/jobs"
    search_url = f"{base_url}?q={keyword.replace(' ', '+')}"
    response = requests.get(search_url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch jobs from Wellfound"}
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='job-listing')  # Adjust based on real structure
    jobs = []

    for job in job_cards[:3]:  # Fetch only the first 3 jobs as a sample
        title = job.find('h2').text.strip() if job.find('h2') else "N/A"
        company = job.find('h3').text.strip() if job.find('h3') else "N/A"
        location = job.find('span', class_='location').text.strip() if job.find('span', class_='location') else "Remote"
        link = base_url + job.find('a')['href'] if job.find('a') else "#"

        jobs.append({
            "job_title": title,
            "company_name": company,
            "location": location,
            "job_link": link
        })

    return jobs
