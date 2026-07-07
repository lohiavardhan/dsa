WITH unique_sell_product AS(
    SELECT DISTINCT sell_date, product
    FROM Activities
)

SELECT sell_date, COUNT(product) as num_sold, GROUP_CONCAT(product ORDER BY product) as products
FROM unique_sell_product
GROUP BY sell_date
