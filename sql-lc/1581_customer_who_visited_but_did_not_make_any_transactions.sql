WITH get_null AS (
    SELECT v.customer_id
    FROM Visits v
    LEFT JOIN Transactions t ON v.visit_id = t.visit_id
    WHERE t.transaction_id IS NULL
)

SELECT customer_id, COUNT(*) AS count_no_trans
FROM get_null
GROUP BY customer_id
ORDER BY count_no_trans
