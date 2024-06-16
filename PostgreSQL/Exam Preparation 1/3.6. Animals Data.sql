SELECT 
	a."name",
	aty.animal_type,
	TO_CHAR(a.birthdate, 'DD.MM.YYYY') as birthdate
FROM
	animals as a
JOIN
	animal_types as aty
ON
	aty.id = a.animal_type_id
ORDER BY
	a."name"
;