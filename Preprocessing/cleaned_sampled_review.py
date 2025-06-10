import pandas as pd
import re
import os

# === Load data ===
df_cbe = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\CBE_reviews_20250610_005040 copy.csv')
df_boa = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\BOA_bank_20250610_005729.csv')
df_dashen = pd.read_csv('C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\Dashen_reviews_20250608_100000.csv')

# === Sample 400 reviews from each (or fewer if not available) ===
df_cbe = df_cbe.sample(n=min(400, len(df_cbe)), random_state=42)
df_boa = df_boa.sample(n=min(400, len(df_boa)), random_state=42)
df_dashen = df_dashen.sample(n=min(400, len(df_dashen)), random_state=42)

# === Add bank column ===
df_cbe["bank"] = "CBE"
df_boa["bank"] = "BOA"
df_dashen["bank"] = "Dashen"

# === Combine ===
df_all = pd.concat([df_cbe, df_boa, df_dashen], ignore_index=True)

# === Show counts for verification ===
print("Sample counts per bank:")
print(df_all['bank'].value_counts())
print("\nTotal sampled rows:", len(df_all))

# === Clean review text ===
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\b\w{1,2}\b", "", text)
    return text.strip()

df_all['clean_review'] = df_all['review_text'].apply(clean_text)

# === Normalize date ===
df_all['date'] = pd.to_datetime(df_all['date'], errors='coerce').dt.date

# === Save cleaned sample ===
os.makedirs("data/cleaned", exist_ok=True)
df_all.to_csv("data/cleaned/cleaned_sampled_reviews.csv", index=False)
print("\n Cleaned sample saved to data/cleaned/cleaned_sampled_reviews.csv")
