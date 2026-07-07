WITH ranked AS(
    SELECT e.employee_id, e.name, p.review_date, p.rating, ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS rnk
    FROM performance_reviews p
    JOIN employees e ON p.employee_id = e.employee_id
),
top_three AS(
    SELECT *
    FROM ranked
    WHERE rnk <= 3
),
window_function AS(
    SELECT *, 
    LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date) as one_before,
    LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date) as two_before
    FROM top_three
),
filtered AS (
    SELECT *, 
    (CASE WHEN one_before IS NOT NULL AND two_before IS NOT NULL THEN one_before - two_before END) AS first_increase,
    (CASE WHEN one_before IS NOT NULL AND two_before IS NOT NULL THEN rating - one_before END) AS second_increase
    FROM window_function
    HAVING first_increase > 0 AND second_increase > 0
)

SELECT employee_id, name, (first_increase + second_increase) AS improvement_score
FROM filtered
ORDER BY improvement_score DESC, name ASC
