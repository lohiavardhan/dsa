with weight_till AS (
    SELECT *, SUM(Weight) OVER (ROWS UNBOUNDED PRECEDING) AS weights_till_now
    FROM Queue
    ORDER BY turn
),

allowed AS (
    SELECT *
    FROM weight_till
    WHERE weights_till_now <= 1000
)

SELECT person_name
FROM allowed
ORDER BY turn DESC
LIMIT 1
