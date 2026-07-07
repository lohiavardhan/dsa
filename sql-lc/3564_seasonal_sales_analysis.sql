WITH get_season AS (
    SELECT *, 
CASE WHEN MONTH(sale_date) IN (MONTH('2025-01-01'), MONTH('2025-02-01'), MONTH('2025-12-01')) THEN 'Winter'
    WHEN MONTH(sale_date) IN (MONTH('2025-03-01'), MONTH('2025-04-01'), MONTH('2025-05-01')) THEN 'Spring' 
    WHEN MONTH(sale_date) IN (MONTH('2025-06-01'), MONTH('2025-07-01'), MONTH('2025-08-01')) THEN 'Summer'
    WHEN MONTH(sale_date) IN (MONTH('2025-09-01'), MONTH('2025-10-01'), MONTH('2025-11-01')) THEN 'Fall' 
END AS season
        FROM sales
),
quantity_rev AS (
    SELECT s.season, p.category, SUM(s.quantity) AS total_quantity, SUM(s.quantity * s.price) AS total_revenue
    FROM get_season s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY s.season, p.category  
),
get_rank AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_revenue DESC) AS rn
    FROM quantity_rev
)

SELECT season, category, total_quantity, total_revenue
FROM get_rank
WHERE rn = 1
ORDER BY season
