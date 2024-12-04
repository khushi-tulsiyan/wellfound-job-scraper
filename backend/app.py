import os
from flask import Flask
from flask_cors import CORS
from scraper.wellfound_scraper import create_scraper_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(create_scraper_blueprint(), url_prefix='/api')

    # Configuration
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', True)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)