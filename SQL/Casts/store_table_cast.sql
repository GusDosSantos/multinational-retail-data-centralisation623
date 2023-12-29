UPDATE dim_store_details
SET latitude = 'N/A'
WHERE latitude IS NULL;

UPDATE dim_store_details
SET longitude = 'N/A'
WHERE longitude IS NULL;


ALTER TABLE dim_store_details
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(12),
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date TYPE DATE,
ALTER COLUMN store_type TYPE VARCHAR(255),
ALTER COLUMN country_code TYPE VARCHAR(10),
ALTER COLUMN continent TYPE VARCHAR(255),
ALTER COLUMN longitude TYPE FLOAT USING NULLIF(NULLIF(longitude, ''), 'N/A')::FLOAT,
ALTER COLUMN latitude TYPE FLOAT USING NULLIF(NULLIF(latitude, ''), 'N/A')::FLOAT;
