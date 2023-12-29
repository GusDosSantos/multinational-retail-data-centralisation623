SELECT 
    ROUND(CAST(SUM(product_price * product_quantity) AS numeric),2) AS total_sales, store_type, country_code
FROM orders_table
JOIN dim_store_details ON dim_store_details.store_code = orders_table.store_code
JOIN dim_products ON dim_products.product_code = orders_table.product_code
WHERE country_code IN ('DE')
GROUP BY store_type, country_code
ORDER BY total_sales