WITH 
  sales_per_store AS (
    SELECT 
      dim_store_details.store_type,
      ROUND(SUM(dim_products.product_price * orders_table.product_quantity)::NUMERIC, 2) AS total_sales
    FROM 
      orders_table
      JOIN dim_store_details ON dim_store_details.store_code = orders_table.store_code
      JOIN dim_products ON dim_products.product_code = orders_table.product_code
    GROUP BY 
      dim_store_details.store_type
  ),
  all_sales AS (
    SELECT 
      SUM(total_sales) AS all_sales
    FROM 
      sales_per_store
  )
SELECT 
  sales_per_store.store_type,
  sales_per_store.total_sales, 
  all_sales.all_sales,
  ROUND((sales_per_store.total_sales / all_sales.all_sales) * 100, 2) AS percent
FROM 
  sales_per_store, 
  all_sales
ORDER BY 
  sales_per_store.total_sales DESC;
