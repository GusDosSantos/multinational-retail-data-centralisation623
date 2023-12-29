
-- ALTER TABLE dim_products
-- RENAME COLUMN removed TO still_available;

ALTER TABLE dim_products
-- ALTER COLUMN EAN TYPE VARCHAR(255),
ALTER COLUMN product_price TYPE FLOAT USING REPLACE(product_price, '£', '')::FLOAT,
ALTER COLUMN weight TYPE FLOAT USING NULLIF(REGEXP_REPLACE(weight, '[^\d.]', '', 'g')::FLOAT, 0),
ALTER COLUMN product_code TYPE VARCHAR(255), 
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID USING 
  CASE 
    WHEN LENGTH(uuid) = 36 THEN uuid::UUID
    ELSE NULL
  END,
ALTER COLUMN still_available TYPE BOOLEAN USING (still_available = 'still_available'),
ALTER COLUMN weight_class TYPE VARCHAR(255);
