
# Amazon Review Scraper and Sentiment Analyzer

This project provides a complete pipeline to scrape Amazon product reviews, store them in MongoDB Atlas, perform sentiment analysis, and display results via a Flask web app. It is designed for data collection, natural language processing, and web-based visualization.

## Features
- Scrape reviews from Amazon using Selenium
- Store reviews in MongoDB Atlas
- Analyze sentiment with TextBlob
- View results in a Flask web interface
- Jupyter notebook for interactive scraping
- Export reviews and sentiment to CSV

## Project Structure

```
Amazon-Reviews/
├── analysis.py                # Sentiment analysis and MongoDB update
├── chromedriver-win64/        # ChromeDriver for Selenium
│   ├── chromedriver.exe
│   ├── LICENSE.chromedriver
│   └── THIRD_PARTY_NOTICES.chromedriver
├── flask_app/
│   ├── app.py                 # Flask backend
│   └── templates/
│       └── index.html         # HTML template
├── requirements.txt           # Python dependencies
├── reviews.csv                # Exported review data
├── scraper.ipynb              # Jupyter notebook for scraping
├── scraper_pipeline.py        # Script for scraping and MongoDB pipeline
├── .venv/                     # Python virtual environment
└── README.md                  # Project documentation
```

## Setup Instructions
1. Clone the repository and navigate to the folder.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Download ChromeDriver and place it in `chromedriver-win64`. Match the version to your Chrome browser.
5. Set up MongoDB Atlas and update the connection string in the scripts if needed.
6. Run the scraper:
	- Use `scraper.ipynb` for interactive scraping.
	- Or run `python scraper_pipeline.py` for automated scraping and MongoDB storage.
7. Run sentiment analysis:
	- Execute `analysis.py` to analyze and update sentiment labels in MongoDB.
8. Start the Flask app:
	```bash
	python flask_app/app.py
	```
	Visit `http://127.0.0.1:5000/` in your browser to view the results.

## Notes
- Requires Google Chrome installed.
- Respect Amazon's terms of service when scraping data.
- For educational purposes only.