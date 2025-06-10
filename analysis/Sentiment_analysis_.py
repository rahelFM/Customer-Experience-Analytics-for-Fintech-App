from transformers import pipeline
import pandas as pd
import os

# Load your cleaned dataset
df = pd.read_csv("C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\cleaned_sampled_reviews.csv")  # update path if needed

# Make sure there are no NaNs in the review column
df['clean_review'] = df['clean_review'].fillna("")

# Load DistilBERT sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Apply to a subset if it's large (e.g., 1200 reviews is OK)
def get_bert_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]  # truncate long text
    return result['label']

# Apply to your DataFrame
df['distilbert_sentiment'] = df['clean_review'].apply(get_bert_sentiment)

# Save results
import os
import pandas as pd

# (Your existing analysis code here)

# Define output directory (corrected)
output_dir = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\sentiment"
os.makedirs(output_dir, exist_ok=True)  # Ensure directory exists

# Save results (corrected)
df.to_csv(os.path.join(output_dir, "sentiment_analysis_distilbert.csv"), index=False)
print("Sentiment analysis distilbert results saved successfully!")