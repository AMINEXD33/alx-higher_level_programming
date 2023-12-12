-- list the numbers of ricords with the same score
-- records are also ordered by descending count.

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
