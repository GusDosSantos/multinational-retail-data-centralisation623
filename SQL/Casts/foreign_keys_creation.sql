ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_user_uuid
FOREIGN KEY (user_uuid)
REFERENCES dim_users(user_uuid)
ON DELETE SET NULL;

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_product_code
FOREIGN KEY (product_code)
REFERENCES dim_products(product_code)
ON DELETE SET NULL;

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_store_code
FOREIGN KEY (store_code)
REFERENCES dim_store_details(store_code)
ON DELETE SET NULL;

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_date_uuid
FOREIGN KEY (date_uuid)
REFERENCES dim_date_times(date_uuid)
ON DELETE SET NULL;

