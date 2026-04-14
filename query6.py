import sqlite3

conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute("""
with region_avg as
(
select 
region,Round(avg(sales),2)  as avg_sales
from superstore
group by region
)
select * from
region_avg 
where avg_sales > (select avg(sales) from superstore)
""")

for row in cursor.fetchall():
    print(row)

conn.close()