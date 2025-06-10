import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV
file_path = "C:\\Users\\Rahel\\Desktop\\KAIM 5&6\\Week2\\Customer-Experience-Analytics-for-Fintech-App\\data\\sentiment\\thematic_analysis\\textblob_vader.csv"
df = pd.read_csv(file_path)

# Fix column name if needed
if 'identified_themes' in df.columns:
    df['identified_themes'] = df['identified_themes'].astype(str)
else:
    print(" 'identified_themes' column not found!")
    print("Available columns:", df.columns.tolist())
    exit()

# --- PLOT 1: Theme distribution per bank ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="identified_themes", hue="bank")
plt.title("Theme Distribution by Bank")
plt.xlabel("Identified Themes")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- PLOT 2: Sentiment distribution per theme ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="identified_themes", hue="textblob_vader_sentiment")
plt.title("Sentiment Distribution per Theme (DistilBERT)")
plt.xlabel("Theme")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
