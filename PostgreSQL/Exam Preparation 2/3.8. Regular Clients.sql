SELECT
	cl.full_name,
	COUNT(co.car_id) AS count_of_cars,
	SUM(co.bill) AS total_sum
FROM
	clients as cl
JOIN
	courses as co
ON 
	cl.id = co.client_id
GROUP BY 
	cl.id
HAVING
	full_name LIKE '_a%'
		and 
	COUNT(co.car_id) <> 1
ORDER BY
	cl.full_name;