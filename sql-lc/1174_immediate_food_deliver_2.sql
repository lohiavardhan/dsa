with first_order AS(
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) as rn
    FROM Delivery
),


earliest_order AS(
    SELECT *
    FROM first_order
    WHERE rn = 1
)

SELECT ROUND((SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100 / COUNT(order_date)), 2) as immediate_percentage 
FROM earliest_order
