import os
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv("C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\data\\cleaned\\cleaned_sampled_reviews.csv")

# === TextBlob Analysis ===
def get_textblob_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

df['textblob_sentiment'] = df['clean_review'].apply(get_textblob_sentiment)

# === VADER Analysis ===
def get_vader_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"
    score = analyzer.polarity_scores(text)['compound']
    if score > 0.1:
        return 'positive'
    elif score < -0.1:
        return 'negative'
    else:
        return 'neutral'

df['vader_sentiment'] = df['clean_review'].apply(get_vader_sentiment)

# === Fix: Create the full output directory ===
output_dir = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\sentiment"
os.makedirs(output_dir, exist_ok=True)  # Ensures the directory exists
df.to_csv(os.path.join(output_dir, "sentiment_textblob_vader.csv"), index=False)

print("Sentiment analysis with TextBlob and VADER completed and saved.")