# Customer-Experience-Analytics-for-Fintech-App

This project is part of the Week 2 challenge from 10 Academy’s KAIM 5 & 6 program. The goal is to analyze customer reviews from Ethiopian fintech apps (starting with Dashen Bank's SuperApp), and extract insights on user sentiment and experience.

---

## ✅ Project Objectives (Task 1)
1. **Scrape** customer reviews from Google Play Store.
2. **Clean** and preprocess the text.
3. **Perform sentiment analysis** using both VADER and TextBlob.
4. Save cleaned and analyzed reviews for further tasks.

---

## 🗂️ Project Structure

Customer-Experience-Analytics-for-Fintech-App/
├── scraping/ # Scripts to collect data from Google Play
│ └── play_store_scraper.py
├── Preprocessing/ # Text cleaning scripts
│ └── clean_reviews.py
├── Sentiment/ # Sentiment analysis (VADER, TextBlob)
│ └── sentiment_analysis.py
├── data/ # Raw reviews from Google Play
├── database/ # Cleaned and sentiment-annotated reviews
├── requirements.txt
└── README.md


## 📌 Tools & Libraries

- `google-play-scraper` – For scraping reviews
- `pandas`, `numpy` – Data handling
- `TextBlob`, `VADER` – Sentiment analysis
- `regex`, `schedule`, `logging` – Automation and cleaning

---

## 🔄 Workflow Summary

### 1. Scraping Dashen Super App Reviews
We collected the latest 449 reviews from:
- App ID: `com.dashen.dashensuperapp`

> Output: `data/Dashen_reviews_<timestamp>.csv`

### 2. Cleaning the Reviews
We removed:
- URLs
- Special characters
- Extra spaces
- Converted to lowercase

> Output: `database/Dashen_reviews_cleaned.csv`

### 3. Sentiment Analysis
We applied:
- **TextBlob**: polarity-based
- **VADER**: rule-based

Each review now includes:
- `textblob_score` and `textblob_sentiment`
- `vader_score` and `vader_sentiment`

> Output: `database/Dashen_reviews_sentiment.csv`


## 📈 Next Steps
- Perform **topic modeling** or **keyword-based clustering**
- Create visual dashboards (bar charts, word clouds, etc.)
- Expand to other Ethiopian fintech apps

## 🚀 Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Customer-Experience-Analytics-for-Fintech-App.git
   cd Customer-Experience-Analytics-for-Fintech-App
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the scripts:

bash
Copy
Edit
python scraping/play_store_scraper.py
python Preprocessing/clean_reviews.py
python Sentiment/sentiment_analysis.py

Author
Rahel Sileshi Abdisaa

10 Academy – KAIM 5 & 6 Program Week 2

