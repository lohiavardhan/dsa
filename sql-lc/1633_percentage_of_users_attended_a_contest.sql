WITH user_count AS(
    SELECT COUNT(user_id) AS total_count
    FROM Users
)

SELECT contest_id, ROUND((COUNT(r.user_id) / user_count.total_count) * 100, 2) AS percentage
FROM (Register r, user_count)
LEFT JOIN Users u ON r.user_id = u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
