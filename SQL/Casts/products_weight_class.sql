ALTER TABLE dim_products
ADD COLUMN weight_kg NUMERIC;

UPDATE dim_products
SET weight_kg = 
    CASE
        WHEN weight ~ '(\d+(\.\d+)?)\s*g' 
             THEN CAST(SUBSTRING(weight FROM '(\d+(\.\d+)?)\s*g') AS NUMERIC) / 1000
        WHEN weight ~ '(\d+(\.\d+)?)\s*k' 
             THEN CAST(SUBSTRING(weight FROM '(\d+(\.\d+)?)\s*k') AS NUMERIC)
        ELSE NULL
    END;


ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(50); 

UPDATE dim_products
SET weight_class =
    CASE 
        WHEN weight_kg < 2 THEN 'Light'
        WHEN weight_kg >= 2 AND weight_kg < 40 THEN 'Mid_Sized'
        WHEN weight_kg >= 40 AND weight_kg < 140 THEN 'Heavy'
        ELSE 'Truck_Required'
    END;

