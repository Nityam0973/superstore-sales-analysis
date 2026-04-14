import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""
SELECT 
    Category,
    "Sub-Category",
    ROUND(SUM(Sales), 2) as total_sales,
    COUNT("Order ID") as total_orders
FROM superstore
GROUP BY Category, "Sub-Category"
ORDER BY Category, total_sales DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()