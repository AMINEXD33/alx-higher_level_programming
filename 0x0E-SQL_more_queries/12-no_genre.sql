-- shows in the database hbtn_0d_tvshows without a genre linked.
-- ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT a.`title`, b.`genre_id`
  FROM `tv_shows` AS a
       LEFT JOIN `tv_show_genres` AS b
       ON a.`id` = b.`show_id`
       WHERE b.`genre_id` IS NULL
 ORDER BY a.`title`, b.`genre_id`;
 
