WITH user_count AS(
    SELECT u.name as results, COUNT(r.movie_id) as counter
    FROM Users u
    JOIN MovieRating r on u.user_id = r.user_id
    GROUP BY u.user_id
    ORDER BY counter DESC, u.name ASC
    LIMIT 1
),
best_movie AS (
    SELECT m.title as results, avg(rating) as average
    FROM Movies m
    JOIN MovieRating r on m.movie_id = r.movie_id
    WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.movie_id
    ORDER BY average DESC, m.title ASC
    LIMIT 1
)

SELECT results FROM user_count
UNION ALL 
SELECT results from best_movie
