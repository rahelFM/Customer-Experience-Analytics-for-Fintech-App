from google_play_scraper import reviews_all
import pandas as pd

apps = {
    "CBE": "com.combankethio.mobile.android",
    "BOA": "com.abyssiniasoftware.boa",
    "Dashen": "com.dashenbank.app"
}

all_data = []

for bank, package in apps.items():
    result = reviews_all(package, lang='en', country='us')
    for r in result:
        all_data.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].date(),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_data)
df.to_csv("C:\Users\Rahel\Desktop\KAIM 5&6\Week2\Customer-Experience-Analytics-for-Fintech-App\data\Dashen_reviews_20250608_100000.csv", index=False)
print("✅ Scraping complete. Saved to data/raw_reviews.csv")
