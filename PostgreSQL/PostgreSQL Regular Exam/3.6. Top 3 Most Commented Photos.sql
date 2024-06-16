SELECT
	c.photo_id,
	p.capture_date,
	p.description,
	COUNT(*) as comments_count
FROM
	photos as p
JOIN
	comments as c
ON 
	p.id = c.photo_id
WHERE
	p.description IS NOT NULL
GROUP BY
	c.photo_id,
	p.capture_date,
	p.description
ORDER BY
	comments_count DESC
LIMIT 3
	;