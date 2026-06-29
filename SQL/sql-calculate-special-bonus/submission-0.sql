SELECT employee_id,
       CASE
           WHEN employee_id % 2 = 0 OR substring(name, 1, 1) = 'M' THEN 0
           ELSE salary
       END AS bonus
FROM employees
Order by employee_id
