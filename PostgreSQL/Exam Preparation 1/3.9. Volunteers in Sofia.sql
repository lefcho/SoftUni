SELECT
	v."name" as volunteers,
	v.phone_number,
	replace(trim(replace(v.address, 'Sofia', '')), ', ', '')
FROM
	volunteers as v
JOIN
	volunteers_departments as vd
ON 
	vd.id = v.department_id
WHERE
	vd.department_name = 'Education program assistant' 
		AND
	v.address LIKE '%Sofia%'
order BY
	v.name;