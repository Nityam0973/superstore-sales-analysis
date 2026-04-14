import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""
SELECT 
    "Customer Name",
    COUNT("Order ID") as total_orders,
    ROUND(SUM(Sales), 2) as total_revenue
FROM superstore
GROUP BY "Customer Name"
ORDER BY total_revenue DESC
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)

conn.close()