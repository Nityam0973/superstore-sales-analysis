SELECT 
    Region,
    COUNT(Order_ID) as total_orders,
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(AVG(Sales), 2) as avg_order_value
FROM superstore
GROUP BY Region
ORDER BY total_sales DESC;