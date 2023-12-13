-- shows and genres linked to the show from the database hbtn_0d_tvshows
-- ordered by ascending show title and genre name
SELECT a.`title`, b.`name`
  FROM `tv_shows` AS a
       LEFT JOIN `tv_show_genres` AS s
       ON a.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS b
       ON s.`genre_id` = b.`id`
 ORDER BY a.`title`, b.`name`;
 
