SELECT
	CONCAT(o."name", ' - ', a."name") AS "owners - animals",
	o.phone_number,
	ac.cage_id
FROM
	owners as o
JOIN 
	animals as a
ON 
	o.id = a.owner_id
JOIN
	animals_cages AS ac
ON 
	ac.animal_id = a.id
WHERE
	a.animal_type_id = 1
ORDER BY
	o."name",
	a."name" DESC;