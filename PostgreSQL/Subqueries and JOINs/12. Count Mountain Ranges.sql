SELECT 
	mc.country_code,
	COUNT(m.id) as mountain_range_count
FROM
	mountains as m
JOIN
	mountains_countries AS mc
ON
	m.id = mc.mountain_id
WHERE
	mc.country_code IN ('US', 'RU', 'BG')
GROUP BY
	mc.country_code
ORDER BY mountain_range_count DESC
;