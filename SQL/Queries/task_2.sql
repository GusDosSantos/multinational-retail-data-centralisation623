SELECT locality, COUNT(*) AS total_no_stores
FROM dim_store_details
WHERE address NOT IN ('N/A')
GROUP BY locality
ORDER BY total_no_stores DESC