WITH time_diff AS (
  SELECT 
    year::numeric, 
    month::numeric, 
    day::numeric, 
    timestamp::time, 
    LEAD(timestamp::time) OVER (ORDER BY year, month, day, timestamp::time) - timestamp::time AS time_difference
  FROM 
    dim_date_times
  ORDER BY 
    year, month, day, timestamp
),
adj_time_diff AS (
  SELECT 
    year, 
    month, 
    day, 
    timestamp,
    CASE
      WHEN time_difference < '00:00:00' THEN time_difference + '24 hours'::interval
      ELSE time_difference
    END AS adjusted_value
  FROM 
    time_diff
)

SELECT 
  year,
  CONCAT(
    '"hours": ', EXTRACT(hour FROM AVG(adjusted_value)),
    ', "minutes": ', EXTRACT(minute FROM AVG(adjusted_value)),
    ', "seconds": ', EXTRACT(second FROM AVG(adjusted_value)),
    ', "milliseconds": ', EXTRACT(milliseconds FROM AVG(adjusted_value))
  ) AS actual_time_taken
FROM 
  adj_time_diff
GROUP BY 
  year
ORDER BY 
  AVG(adjusted_value) DESC;
