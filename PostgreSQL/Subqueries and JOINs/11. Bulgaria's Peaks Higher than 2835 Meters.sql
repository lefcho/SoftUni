SELECT 
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM
	peaks as p
JOIN
	mountains as m
ON
	p.mountain_id = m.id
JOIN
	mountains_countries AS mc
ON
	m.id = mc.mountain_id
WHERE
	p.elevation > 2835 AND mc.country_code = 'BG' 
ORDER BY 
	p.elevation DESC;