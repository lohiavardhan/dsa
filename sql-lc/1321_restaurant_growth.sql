WITH amount_average AS (
    SELECT DISTINCT *, (sum(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW)) as totalamount, ROUND((sum(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW)) / 7, 2) as average_amount
    FROM Customer
    ORDER BY visited_on
),
minimum_date as (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) as minimum
    FROM Customer
)

SELECT DISTINCT a.visited_on, a.totalamount as amount, a.average_amount
FROM amount_average a, minimum_date m
WHERE a.visited_on >= m.minimum

