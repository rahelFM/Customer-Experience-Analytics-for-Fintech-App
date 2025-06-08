import pandas as pd
import re
import os

# Function to clean text
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r"http\S+|www\S+|https\S+", '', text)
        text = re.sub(r"[^a-zA-Z0-9\s]", '', text)
        text = re.sub(r"\s+", ' ', text).strip()
        return text
    return ""

def clean_reviews(input_csv, output_csv):
    if not os.path.exists(input_csv):
        print(f" File not found: {input_csv}")
        return

    df = pd.read_csv(input_csv)
    
    if 'review_text' not in df.columns:
        print(" 'review_text' column missing in the CSV.")
        return

    print(f" Cleaning {len(df)} reviews...")
    df['cleaned_review'] = df['review_text'].apply(clean_text)

    df.to_csv(output_csv, index=False)
    print(f"Saved cleaned reviews to {output_csv}")

if __name__ == "__main__":
    # Adjust filenames based on your actual file
    input_file = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\Dashen_reviews_20250608_100000.csv"
    output_file = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\database\\Dashen_reviews_cleaned.csv"
    clean_reviews(input_file, output_file)


