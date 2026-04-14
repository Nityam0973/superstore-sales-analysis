import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""
SELECT 
    Region,
    COUNT("Order ID") as total_orders,
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(AVG(Sales), 2) as avg_order_value
FROM superstore
GROUP BY Region
ORDER BY total_sales DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()