WITH converted AS(
    SELECT user_id, 
        SUM(CASE WHEN activity_type = 'free_trial' THEN 1 ELSE 0 END) AS free,
        SUM(CASE WHEN activity_type = 'paid' THEN 1 ELSE 0 END) AS paid
    FROM UserActivity
    GROUP BY user_id
    HAVING free > 0 AND paid > 0
)

SELECT u.user_id, 
ROUND(SUM(CASE WHEN u.activity_type = 'free_trial' THEN u.activity_duration ELSE 0 END) / SUM(CASE WHEN u.activity_type = 'free_trial' THEN 1 ELSE 0 END), 2) AS trial_avg_duration,
ROUND(SUM(CASE WHEN u.activity_type = 'paid' THEN u.activity_duration ELSE 0 END) / SUM(CASE WHEN u.activity_type = 'paid' THEN 1 ELSE 0 END), 2) AS paid_avg_duration
FROM UserActivity u
JOIN converted c ON u.user_id = c.user_id
GROUP BY user_id
