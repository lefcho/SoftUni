SELECT
    a."name",
    EXTRACT(YEAR FROM a.birthdate) AS birth_year,
    aty.animal_type
FROM
    animals AS a
JOIN
    animal_types AS aty
ON
    aty.id = a.animal_type_id
WHERE
    a.owner_id IS NULL
    	AND
    aty.animal_type <> 'Birds'
    	AND
    AGE('01/01/2022', a.birthdate) < '5 years'
order BY
	a.name;