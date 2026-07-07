WITH primary_yes as (
    SELECT *
    FROM Employee
    WHERE primary_flag = 'Y'
),

only_one as (
    SELECT *, COUNT(*) AS counter
    FROM Employee
    GROUP BY employee_id
    HAVING counter = 1
)

SELECT employee_id, department_id
FROM primary_yes
UNION
SELECT employee_id, department_id
FROM only_one
