-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows tv_show_genres WHERE tv_show.id = tv_show_genres.show_id ORDER BY ASC;
