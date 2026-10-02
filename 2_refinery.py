import pandas as pd

df = pd.read_csv("shop_raw.csv")
df['GENERE'] = df['GENERE'].replace({'Maschio' : "M", "m" : "M", "Femmina" : "F", "f" : "F"})
df['ETA'] = df['ETA'].fillna(df['ETA'].median())

df['GENERE'] = df['GENERE'].astype('category').cat.codes

df.to_csv("shop_cleaned.csv", index=False)

print("File creato con successo")

