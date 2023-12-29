SELECT ROUND(CAST(SUM(product_price * product_quantity) AS numeric),2) AS total_sales, month
FROM orders_table
JOIN dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
JOIN dim_products ON dim_products.product_code = orders_table.product_code
GROUP BY month
ORDER BY total_sales DESC