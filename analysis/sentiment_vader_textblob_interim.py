import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def analyze_sentiment(text):
    blob = TextBlob(text)
    vader = SentimentIntensityAnalyzer()

    blob_polarity = blob.sentiment.polarity
    vader_score = vader.polarity_scores(text)['compound']

    return blob_polarity, vader_score

def label_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def run_sentiment_analysis(input_file, output_file):
    df = pd.read_csv(input_file)

    print(f" Analyzing {len(df)} reviews...")

    df['textblob_score'], df['vader_score'] = zip(*df['review_text'].map(analyze_sentiment))
    df['textblob_sentiment'] = df['textblob_score'].apply(label_sentiment)
    df['vader_sentiment'] = df['vader_score'].apply(label_sentiment)

    df.to_csv(output_file, index=False)
    print(f" Sentiment analysis saved to {output_file}")

if __name__ == "__main__":
    input_file = os.path.join("database", "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\database\\Dashen_reviews_cleaned.csv")
    output_file = os.path.join("database", "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\Dashen_reviews_sentiment.csv")
    run_sentiment_analysis(input_file, output_file)
