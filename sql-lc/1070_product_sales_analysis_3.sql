with ranking as(
    SELECT *, ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY year ASC) AS rn
    FROM Sales
),

first_year as(
    SELECT *
    FROM ranking
    WHERE rn = 1
)

SELECT s.product_id, s.year as first_year, s.quantity, s.price
FROM first_year r
LEFT JOIN Sales s ON r.year = s.year AND r.product_id = s.product_id 
