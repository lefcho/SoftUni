SELECT
	d.first_name,
	d.last_name,
	c.make,
	c.model,
	c.mileage
from
	drivers as d
JOIN
	cars_drivers as cd
ON
	d.id = cd.driver_id
JOIN
	cars as c
on
	c.id = cd.car_id
WHERE
	c.mileage IS NOT NULL
ORDER by
	c.mileage DESC,
	d.first_name;