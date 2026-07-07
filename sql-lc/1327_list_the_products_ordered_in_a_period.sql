WITH feb_only_data AS (
    SELECT *
    FROM Orders
    WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
),

cumulative_sum AS(
    SELECT p.product_id, p.product_name, o.order_date, o.unit, 
    SUM(unit) OVER (PARTITION BY p.product_id ROWS UNBOUNDED PRECEDING) AS output
    FROM Products p
    LEFT JOIN feb_only_data o on p.product_id = o.product_id
)

SELECT product_name, MAX(output) as unit
FROM cumulative_sum
WHERE output >= 100
GROUP BY product_name
