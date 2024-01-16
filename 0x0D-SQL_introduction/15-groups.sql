-- groups data with the same score
SELECT COUNT(*) AS `number` GROUP BY `score` ORDER BY `number` DESC