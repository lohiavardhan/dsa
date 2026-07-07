SELECT a.activity_date as day, COUNT(DISTINCT a.user_id) as active_users
FROM Activity a
WHERE a.activity_date >= SUBDATE('2019-07-27', INTERVAL 29 DAY) AND a.activity_date <= '2019-07-27'
GROUP BY a.activity_date
