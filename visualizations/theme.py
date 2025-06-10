# Merge datasets on review_id or review_text (if unique)
merged = df_distil.merge(df_lex[['review_text', 'sentiment_label']], on='review_text', suffixes=('_distil', '_lex'))

# Calculate agreement per theme
agreement = merged.groupby('identified_theme').apply(
    lambda x: (x['sentiment_label_distil'] == x['sentiment_label_lex']).mean()
).reset_index(name='agreement_rate')

print(agreement)
