-- MySQL script to select shows and value
SELECT name AS 'genre', COUNT(*) AS 'number_shows'
FROM tv_genres, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
