-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
