-- 16. List shows and genres
-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.


SELECT title, tv_genres.name AS name 
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
