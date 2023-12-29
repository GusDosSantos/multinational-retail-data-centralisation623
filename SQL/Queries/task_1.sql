SELECT country_code AS country, COUNT(*) AS total_no_stores
FROM dim_store_details
WHERE address NOT IN ('N/A')
GROUP BY country_code