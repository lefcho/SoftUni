SELECT 
	o.name as "owner",
	COUNT(*) AS count_of_animals
FROM 
	owners as o
	JOIN
		animals as a
	ON
		o.id = a.owner_id
GROUP BY
	o.name
ORDER BY
	count_of_animals DESC, "owner"
LIMIT
	5
;