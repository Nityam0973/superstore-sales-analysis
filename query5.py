import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""

SELECT 
    Region,
    State,
    Sales,
    ROUND(SUM(Sales) OVER (PARTITION BY Region), 2) as region_total
FROM superstore
Limit 10
""")

for row in cursor.fetchall():
    print(row)

conn.close()