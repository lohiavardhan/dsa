WITH all_together AS (
    SELECT product_id, 'store1' as store ,store1 price
    FROM Products
    UNION
    SELECT product_id, 'store2' as store ,store2 as price
    FROM Products
    UNION
    SELECT product_id, 'store3' as store ,store3 as price
    FROM Products
)

SELECT *
FROM all_together
WHERE price IS NOT NULL
