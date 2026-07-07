WITH subordinates AS(
    SELECT *
    FROM Employees
    WHERE manager_id IS NOT NULL
)

SELECT s.employee_id
FROM subordinates s
LEFT JOIN Employees e ON s.manager_id = e.employee_id 
WHERE s.salary < 30000 AND e.employee_id IS NULL 
ORDER BY s.employee_id ASC
