SELECT
	ca.id AS car_id, 
	make,
	mileage,
	COUNT(co.id) AS count_of_courses,
	ROUND(AVG(co.bill), 2) AS average_bill
FROM
	courses as co
RIGHT JOIN
	cars as ca
ON
	ca.id = co.car_id
GROUP BY
	ca.id, make, mileage
HAVING
	COUNT(co.id) <> 2
ORDER BY
	count_of_courses DESC,
	ca.id;