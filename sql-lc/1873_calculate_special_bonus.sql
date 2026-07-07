SELECT employee_id, 
(CASE WHEN ((MOD(employee_id, 2) = 1) AND (LEFT(name, 1) <> 'M')) THEN salary ELSE 0 END) AS bonus 
FROM Employees
GROUP BY employee_id
ORDER BY employee_id
