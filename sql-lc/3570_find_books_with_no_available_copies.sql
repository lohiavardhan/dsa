WITH answer AS(
    SELECT b.book_id, l.title, l.author, l.publication_year, l.genre, l.total_copies, SUM(CASE WHEN return_date IS NULL THEN 1 ELSE 0 END) AS current_borrowers
    FROM borrowing_records b
    JOIN library_books l ON l.book_id = b.book_id
    GROUP BY b.book_id
    HAVING l.total_copies = current_borrowers
)

SELECT book_id, title, author, genre, publication_year, current_borrowers
FROM answer
ORDER BY current_borrowers DESC, title ASC
