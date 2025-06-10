import pandas as pd
import re
from datetime import datetime
import os

# === Step 1: Load data ===
df_cbe = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\CBE_reviews_20250610_005040 copy.csv')
df_boa = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\BOA_bank_20250610_005729.csv')
df_dashen = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\Dashen_reviews_20250608_100000.csv')

# Step 2: Add 'bank' column if not already present
df_cbe['bank'] = 'CBE'
df_boa['bank'] = 'BOA'
df_dashen['bank'] = 'Dashen'

# Step 3: Combine all into one DataFrame
df_all = pd.concat([df_cbe, df_boa, df_dashen], ignore_index=True)

# Step 4: Drop duplicates & rows with empty reviews
df_all.drop_duplicates(subset=['review_text'], inplace=True)
df_all.dropna(subset=['review_text'], inplace=True)

# Step 5: Normalize date column
df_all['date'] = pd.to_datetime(df_all['date'], errors='coerce').dt.date

# Step 6: Clean text
def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\b\w{1,2}\b", "", text)  # remove 1-2 character words
    return text.strip()

df_all['clean_review'] = df_all['review_text'].apply(clean_text)

# Step 7: Save cleaned dataset
os.makedirs("data/cleaned", exist_ok=True)
df_all.to_csv("data/cleaned/all_banks_cleaned_reviews.csv", index=False)
print("Cleaned data saved to data/cleaned/all_banks_cleaned_reviews.csv")
