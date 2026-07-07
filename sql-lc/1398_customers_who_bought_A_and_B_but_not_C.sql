WITH result_col AS (
    SELECT o.customer_id, c.customer_name, 
        SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) as acount, 
        SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) as bcount,
        SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) as ccount
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY o.customer_id, c.customer_name
)

SELECT customer_id, customer_name
FROM result_col
WHERE acount > 0 and bcount > 0 and ccount = 0
ORDER BY customer_name
