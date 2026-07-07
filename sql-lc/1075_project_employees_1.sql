
SELECT project_id, ROUND(avg(experience_years), 2) as average_years
FROM Employee as e
INNER JOIN Project AS p ON p.employee_id = e.employee_id
GROUP BY project_id