
SELECT DISTINCT p.product_id as product_id, product_name
FROM Sales as s
LEFT JOIN Product as p ON p.product_id = s.product_id
WHERE p.product_id NOT IN (SELECT product_id from SALES WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31')
