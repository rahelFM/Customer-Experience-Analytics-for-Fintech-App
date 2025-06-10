import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Parameters (from you)
file_path = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\sentiment\\sentiment_textblob_vader.csv"
review_col = "clean_review"
sentiment_label_col = "sentiment_label"
sentiment_score_col = "sentiment_score"
review_id_col = None  # Use df.index as ID
bank_col = "bank"

# Load SpaCy model (English)
nlp = spacy.load("en_core_web_sm")

# Load data
df = pd.read_csv(file_path)

# Preprocessing function: tokenization, stopword removal, lemmatization
def preprocess(text):
    doc = nlp(str(text))
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

print("Preprocessing reviews...")
df['processed_review'] = df[review_col].apply(preprocess)

# Function to extract top keywords per bank using TF-IDF
def extract_keywords(df_bank, ngram_range=(1,2), top_n=30):
    tfidf = TfidfVectorizer(ngram_range=ngram_range, max_features=top_n)
    X = tfidf.fit_transform(df_bank['processed_review'])
    features = tfidf.get_feature_names_out()
    scores = X.sum(axis=0).A1  # sum TF-IDF scores across docs
    keywords_scores = sorted(zip(features, scores), key=lambda x: x[1], reverse=True)
    return [kw for kw, score in keywords_scores]

# Collect keywords per bank
banks = df[bank_col].unique()
bank_keywords = {}

print("Extracting keywords per bank...")
for bank in banks:
    df_bank = df[df[bank_col] == bank]
    keywords = extract_keywords(df_bank)
    bank_keywords[bank] = keywords
    print(f"\nTop keywords for {bank}:")
    print(keywords[:15])  # print top 15 keywords per bank for inspection

# --- Manual theme grouping ---
# You can customize these theme keywords based on the extracted keywords
# For example purposes, I define generic themes (adjust as you see fit)

theme_definitions = {
    'Account Access Issues': ['login', 'password', 'access', 'account', 'lock', 'reset', 'verification'],
    'Transaction Performance': ['transfer', 'transaction', 'payment', 'delay', 'failed', 'processing', 'speed'],
    'User Interface & Experience': ['ui', 'interface', 'design', 'app', 'slow', 'crash', 'bug'],
    'Customer Support': ['support', 'service', 'help', 'response', 'customer', 'call', 'agent'],
    'Feature Requests': ['feature', 'add', 'improve', 'update', 'option', 'notification', 'wish'],
}

# Function to assign themes to reviews based on presence of theme keywords
def assign_themes(text):
    text_tokens = set(text.split())
    matched_themes = []
    for theme, keywords in theme_definitions.items():
        if any(k in text_tokens for k in keywords):
            matched_themes.append(theme)
    return "; ".join(matched_themes) if matched_themes else "Other"

print("\nAssigning themes to each review...")
df['identified_themes'] = df['processed_review'].apply(assign_themes)

# Save results with themes
output_dir = os.path.join(os.path.dirname(file_path), "thematic_analysis")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "textblob_vader.csv")

df.to_csv(output_path, index=review_id_col is None)
print(f"\nThematic analysis saved to:\n{output_path}")
