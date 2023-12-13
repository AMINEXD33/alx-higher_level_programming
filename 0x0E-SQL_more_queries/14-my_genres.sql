-- genres of the show Dexter in the database hbtn_0d_tvshows
-- ordered by ascending genre name
SELECT a.`name`
  FROM `tv_genres` AS a
       INNER JOIN `tv_show_genres` AS b
       ON a.`id` = b.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = b.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY a.`name`;
 
