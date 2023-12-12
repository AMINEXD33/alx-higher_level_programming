-- list all records that have a name value
-- ORDERED BY DESC

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
