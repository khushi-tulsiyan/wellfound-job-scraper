from flask import Flask, jsonify, request
from scraper.wellfound_scraper import scrape_jobs
from threading import Thread

app = Flask(__name__)

def threaded_scrape(keyword, result):
    result['data'] = scrape_jobs(keyword)


@app.route('/')
def home():
    return "Welcome to the Wellfound Job Scraper API. Use /scrape endpoint with a keyword."


@app.route('/scrape', methods=['GET'])
def scrape_endpoint():
    keyword = request.args.get('keyword', default='', type=str)
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    result = {}
    thread = Thread(target=threaded_scrape, args=(keyword, result))
    thread.start()
    thread.join()  # Wait for the thread to finish
    
    return jsonify(result.get('data', []))

if __name__ == "__main__":
    app.run(debug=True)
