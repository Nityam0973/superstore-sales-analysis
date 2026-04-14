import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

# Create a targets table
cursor.execute("""
CREATE TABLE IF NOT EXISTS targets (
    Region TEXT,
    sales_target REAL
)
""")

# Insert target data
cursor.execute("DELETE FROM targets")
targets = [
    ('West', 650000),
    ('East', 600000),
    ('Central', 500000),
    ('South', 350000)
]
cursor.executemany("INSERT INTO targets VALUES (?, ?)", targets)

# JOIN query
cursor.execute("""
SELECT 
    s.Region,
    ROUND(SUM(s.Sales), 2) as actual_sales,
    t.sales_target,
    ROUND(SUM(s.Sales) - t.sales_target, 2) as difference
FROM superstore s
INNER JOIN targets t ON s.Region = t.Region
GROUP BY s.Region
ORDER BY actual_sales DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()