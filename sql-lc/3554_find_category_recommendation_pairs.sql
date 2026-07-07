WITH cte AS (
    SELECT p.user_id, p.product_id, i.category
    FROM ProductPurchases p
    JOIN ProductInfo i ON p.product_id = i.product_id
)

SELECT u1.category AS category1,
    u2.category AS category2,
    COUNT(DISTINCT u1.user_id) AS customer_count
FROM cte u1
JOIN cte u2 ON u1.user_id = u2.user_id AND u1.category < u2.category
GROUP BY u1.category, u2.category
HAVING customer_count >= 3
ORDER BY customer_count DESC, category1 ASC, category2 ASC
