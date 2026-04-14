import pandas as pd
import sqlite3

df = pd.read_csv('superstore.csv', encoding='latin-1')
conn = sqlite3.connect('superstore.db')
df.to_sql('superstore', conn, if_exists='replace', index=False)
conn.close()

print("Done! Rows loaded:", len(df))