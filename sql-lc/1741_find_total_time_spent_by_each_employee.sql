WITH day_time AS(
    SELECT *, (out_time - in_time) AS day_time
    FROM Employees
)

SELECT event_day as day, emp_id, SUM(day_time) AS total_time
FROM day_time
GROUP BY emp_id, event_day
