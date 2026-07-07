WITH first_positive AS (
    SELECT 
        patient_id,
        MIN(CASE WHEN result = 'Positive' THEN test_date END) AS first_positive
    FROM covid_tests
    GROUP BY patient_id
),
with_negative AS (
    SELECT 
        fp.patient_id,
        fp.first_positive,
        MIN(CASE WHEN ct.result = 'Negative' AND ct.test_date > fp.first_positive 
                 THEN ct.test_date END) AS first_negative
    FROM first_positive fp
    JOIN covid_tests ct ON ct.patient_id = fp.patient_id
    GROUP BY fp.patient_id, fp.first_positive
)

SELECT 
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(wn.first_negative, wn.first_positive) AS recovery_time
FROM with_negative wn
JOIN patients p ON p.patient_id = wn.patient_id
WHERE (wn.first_negative - wn.first_positive) IS NOT NULL
ORDER BY recovery_time ASC, p.patient_name ASC
