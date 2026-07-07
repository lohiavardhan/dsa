WITH bounds AS (
  SELECT student_id, subject,
         MIN(exam_date) AS first_date,
         MAX(exam_date) AS latest_date
  FROM Scores
  GROUP BY student_id, subject
)

SELECT s.student_id, s.subject, SUM(CASE WHEN exam_date = first_date THEN score ELSE 0 END) AS first_score, 
    SUM(CASE WHEN exam_date = latest_date THEN score else 0 END) AS latest_score 
FROM Scores s
JOIN bounds b ON s.student_id = b.student_id AND s.subject = b.subject
GROUP BY s.student_id, s.subject
HAVING latest_score > first_score
ORDER BY s.student_id
