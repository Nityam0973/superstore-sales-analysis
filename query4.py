import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""

select state,Round(sum(Sales),2)
from superstore
group by state
order by sum(Sales) desc
limit 5
""")

for row in cursor.fetchall():
    print(row)

conn.close()