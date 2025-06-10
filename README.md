# Customer Experience Analytics for Fintech App

This project analyzes customer reviews from Google Play Store for three major Ethiopian banks' fintech apps: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank. The goal is to extract customer sentiment and recurring themes to help banks enhance their digital customer experience.

---

##  Overview

- **Sentiment Analysis**: Performed using TextBlob, VADER, and DistilBERT.
- **Thematic Analysis**: Extracted keywords with TF-IDF and clustered into themes.
- **Visualization**: Insights across banks, sentiment models, and themes.
- **Outcome**: Identified satisfaction drivers and pain points per app.

---

##  Project Structure

Customer-Experience-Analytics-for-Fintech-App/
│
├── data/
│ └── sentiment/
│ ├── sentiment_analysis_textblob_vader.csv
│ ├── sentiment_analysis_distilbert.csv
│ └── thematic_analysis/
│ ├── textblob_vader.csv
│ └── distilbert_reviews_with_themes.csv
│
├── analysis/
│ ├── Sentiment_analysis.py
│ └── thematic_analysis.py
│
├── visualizations/
│ └── generate_plots.py
│
└── README.md


##  Models Used

- **TextBlob**: Rule-based, lexicon-driven.
- **VADER**: Specialized for short social media text.
- **DistilBERT**: Transformer-based model for contextual sentiment understanding.

---

##  Themes

Identified themes across all apps:
1. **Account Access Issues**
2. **Transaction Performance**
3. **User Interface & Experience**
4. **Customer Support**
5. **Feature Requests**

Keywords were grouped using TF-IDF and manually clustered.

---

##  Key Findings

- **DistilBERT outperforms** TextBlob and VADER in accurately detecting sentiment nuances.
- Common positive keywords: "good", "fast", "easy", "super app"
- Frequent complaints include: "login error", "crash", "slow update"

---

## Visualizations

- Bar charts for sentiment distribution per model & bank
- Theme-wise sentiment comparison
- Model performance per identified theme



## Setup Instructions

```bash
# 1. Clone repository
git clone https://github.com/your-username/Customer-Experience-Analytics-for-Fintech-App.git
cd Customer-Experience-Analytics-for-Fintech-App

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 4. Run analysis
python analysis/Sentiment_analysis.py
python analysis/thematic_analysis.py

# 5. Visualize
python visualizations/generate_plots.py

## Dependencies
pandas

matplotlib

seaborn

scikit-learn

spacy

transformers

nltk

vaderSentiment

textblob

## Authors
Rahel (Lead Data Analyst)

10 Academy Week 2 Project Team

## License
MIT License.
