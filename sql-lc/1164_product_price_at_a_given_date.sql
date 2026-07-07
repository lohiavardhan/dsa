with ranked as(
    SELECT product_id, new_price, ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rn
    FROM Products
    WHERE change_date <= '2019-08-16'
),


latest as(
    SELECT product_id, new_price
    FROM ranked
    WHERE ranked.rn = 1
)

SELECT DISTINCT p.product_id, COALESCE(latest.new_price, 10) as price
FROM Products p
LEFT JOIN latest ON p.product_id = latest.product_id
